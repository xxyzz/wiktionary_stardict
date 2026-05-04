<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:include href="../image.xsl"/>
  <xsl:include href="../utils.xsl"/>
  <xsl:include href="alt_forms.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:param name="language"/>
    <xsl:if test="ol/li[myfn:is-gloss-li(.)]">
      <xsl:variable
          name="headword-p"
          select="p[strong[contains-token(@class, 'headword')] or .//b]"/>
      <xsl:variable
          name="headword-strong"
          select="for $b in (
                  let $strong := $headword-p/strong[contains-token(@class, 'headword')]
                  return if ($strong) then $strong else $headword-p//b[1]) return
                  let $text := myfn:ruby_text($b)
                  return if ($headword-p/span[@data-mw and myfn:is-template(@data-mw,
                    ('jachars', 'zhchars', 'kochar', 'vichar'))])
                    then replace($text, ' ', '') else $text"
          as="xs:string*"/>
      <xsl:variable
          name="headword-forms"
          select="for $b in $headword-p//b[not(parent::span[@data-mw and
                  myfn:is-template(@data-mw,
                  ('jachars', 'zhchars', 'kochar', 'vichar'))])]
                  return myfn:ruby_text($b)"
          as="xs:string*"/>
      <xsl:variable
          name="alt-forms" as="xs:string*" select="myfn:get-alt-forms(.)"/>
      <xsl:variable
          name="unique-forms"
          select="distinct-values(($headword-strong, $title, $alt-forms,
                  $headword-forms)[. != ''])"
          as="xs:string*"/>

      <xsl:variable name="definition">
        <section class="mw-parser-output" dir="ltr" lang="ja">
          <xsl:apply-templates
              select="h3 | h4 | h5 | h6" mode="pos-heading"/>
          <xsl:apply-templates select="p | ol" mode="pos-li"/>
          <xsl:apply-templates
              select="section[normalize-space(h4|h5|h6) =
                      ('用法', '注意点', '留意点', '注意', '備考', '表記', '補足', '補足')]"
              mode="usage-notes"/>
        </section>
      </xsl:variable>

      <xsl:variable name="images" as="xs:string*">
        <xsl:sequence select="$definition//img/@src"/>
      </xsl:variable>

      <xsl:variable name="final-definition">
        <xsl:apply-templates select="$definition" mode="convert-img"/>
      </xsl:variable>

      <xsl:variable name="is-form-only" as="xs:boolean">
        <xsl:sequence
            select="boolean(myfn:section-is-form-of(.) or (
                    every $li in ol/li[myfn:is-gloss-li(.)]
                    satisfies myfn:li-is-form-of($li)))"/>
      </xsl:variable>

      <xsl:sequence
          select="map{'lang': $language,
                  'forms': array{$unique-forms},
                  'def': serialize(
                    $final-definition, map{'method': 'html', 'indent': false()}),
                  'images': array{$images},
                  'form_of_targets': array{
                    myfn:form-of-targets(ol/li[if ($is-form-only) then
                      myfn:is-gloss-li(.) else myfn:li-is-form-of(.)])},
                  'form_of_only': $is-form-only}"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="h3 | h4 | h5 | h6" mode="pos-heading">
    <h4 class="Jpan"><xsl:apply-templates mode="clean-content"/></h4>
  </xsl:template>

  <xsl:template match="ol" mode="pos-li">
    <ol><xsl:apply-templates mode="pos-li"/></ol>
  </xsl:template>

  <xsl:template match="li" mode="pos-li">
    <xsl:if test="myfn:is-gloss-li(.)">
      <li><xsl:apply-templates mode="pos-li"/></li>
    </xsl:if>
  </xsl:template>

  <!-- Find the shortest usage example -->
  <xsl:template match="dl" mode="pos-li">
    <xsl:variable
        name="examples"
        select="dd[div[some $class in ('h-usage-example', 'citation-whole')
                satisfies contains-token(@class, $class)]]"/>
    <xsl:variable
        name="color-panel" select="dd[div[contains-token(@class, 'color-panel')]]"/>
    <xsl:variable
        name="nyms"
        select="dd[span[@data-mw and myfn:is-template(@data-mw, ('syn', 'ant'))]]"/>
    <xsl:if test="$examples or $color-panel or $nyms">
      <dl>
        <xsl:apply-templates select="$color-panel" mode="clean-content"/>
        <xsl:apply-templates select="$nyms" mode="clean-content"/>
        <xsl:apply-templates
            select="($examples[string-length() = min($examples/string-length())])[1]"
            mode="clean-content"/>
      </dl>
    </xsl:if>
  </xsl:template>
  <xsl:template match="ul" mode="pos-li">
    <xsl:variable
        name="examples"
        select="li[node() and not(contains-token(., 'mw-empty-elt'))]"/>
    <xsl:if test="li">
      <ul>
        <xsl:apply-templates
            select="($examples[string-length() = min($examples/string-length())])[1]"
            mode="clean-content"/>
      </ul>
    </xsl:if>
  </xsl:template>

  <xsl:template match="*" mode="pos-li">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>

  <xsl:function name="myfn:is-gloss-li" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean($li/node() and
                not(contains-token($li/@class, 'mw-empty-elt')) and
                not($li/i[@data-mw and myfn:is-template(@data-mw, 'rfdef')]))"/>
  </xsl:function>

  <xsl:function name="myfn:section-is-form-of" as="xs:boolean">
    <xsl:param name="section" as="element(section)"/>
    <xsl:sequence
        select="boolean($section//link[@rel = 'mw:PageProp/Category' and
                (contains(@href, '和語の漢字表記') or ends-with(@href, '定形'))])"/>
  </xsl:function>

  <xsl:function name="myfn:li-is-form-of" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean($li/span[@data-mw and (myfn:is-template-suffix(@data-mw, ' of')
                or myfn:is-template(@data-mw, ('alt form', '変化形', 'alt sp',
                'altspell')))])"/>
  </xsl:function>

  <xsl:function name="myfn:form-of-targets" as="xs:string*">
    <xsl:param name="li" as="element(li)*"/>
    <xsl:sequence select="distinct-values($li//a[1] ! normalize-space(.))"/>
  </xsl:function>

  <xsl:template match="section" mode="usage-notes">
    <section>
      <h4 class="Jpan">用法</h4>
      <xsl:apply-templates select="p | ul | dl" mode="clean-content"/>
    </section>
  </xsl:template>
</xsl:stylesheet>
