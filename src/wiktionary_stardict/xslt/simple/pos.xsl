<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:map="http://www.w3.org/2005/xpath-functions/map"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:include href="../utils.xsl"/>
  <xsl:include href="../image.xsl"/>
  <xsl:include href="config.xsl"/>
  <xsl:include href="alt_forms.xsl"/>
  <xsl:include href="pronunciation.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:if test="ol/li[myfn:is-gloss-li(.)]">
      <xsl:variable
          name="title-form"
          as="xs:string"
          select="if (starts-with($title, 'Unsupported titles/') and
                      map:contains($unsupported-titles, $title))
                  then $unsupported-titles($title) else $title"/>
      <xsl:variable
          name="table-forms"
          as="xs:string*"
          select="table[contains-token(@class, 'inflection-table')]//td//
                  span[contains-token(@class, 'form-of')] ! normalize-space()"/>
      <xsl:variable
          name="unique-forms"
          select="distinct-values(($title-form, $table-forms)[. != ''])"
          as="xs:string*"/>

      <xsl:variable name="definition">
        <section class="mw-parser-output" dir="ltr" lang="en">
          <xsl:apply-templates select="h2" mode="section-heading"/>
          <xsl:apply-templates
              select="preceding-sibling::section[normalize-space(h3) = 'Pronunciation']"
              mode="pron"/>
          <xsl:apply-templates select="ol" mode="pos-li"/>
          <xsl:apply-templates
              select="section[normalize-space(h3) = 'Usage notes']" mode="usage-notes"/>
          <xsl:apply-templates select="myfn:get-alt-form-section(.)" mode="alt-form"/>
        </section>
      </xsl:variable>

      <xsl:variable name="images" as="xs:string*">
        <xsl:sequence select="$definition//img/@src"/>
      </xsl:variable>

      <xsl:variable name="final-definition">
        <xsl:apply-templates select="$definition" mode="convert-img"/>
      </xsl:variable>

      <xsl:variable
          name="form-of-only" as="xs:boolean"
          select="boolean(every $li in ol/li[myfn:is-gloss-li(.)]
                  satisfies myfn:is-form-of($li))"/>

      <xsl:sequence
          select="map{'lang': 'English',
                  'forms': array{$unique-forms},
                  'def': serialize(
                    $final-definition, map{'method': 'html', 'indent': false()}),
                  'images': array{$images},
                  'form_of_targets': array{if ($form-of-only) then
                    myfn:form-of-targets(ol/li) else ()},
                  'form_of_only': $form-of-only,
                  'ids': array{string(h2/@id)}}"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="h2 | h3 | h4 | h5 | h6" mode="section-heading">
    <h4><xsl:apply-templates mode="clean-content"/></h4>
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
        name="color-box"
        select="dd[div[@data-mw and myfn:is-template(@data-mw, 'colorbox')]]"/>
    <xsl:variable
        name="examples"
        select="dd[i or span[contains-token(@class, 'mwe-math-element')]]"/>
    <xsl:if test="$examples or $color-box">
      <dl>
        <xsl:apply-templates select="$color-box" mode="clean-content"/>
        <xsl:apply-templates
            select="($examples[string-length() = min($examples/string-length())])[1]"
            mode="clean-content"/>
      </dl>
    </xsl:if>
  </xsl:template>

  <xsl:template match="*" mode="pos-li">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>

  <xsl:function name="myfn:is-gloss-li" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean($li/node() and
                not(contains-token($li/@class, 'mw-empty-let')))"/>
  </xsl:function>

  <!-- https://simple.wiktionary.org/wiki/Category:Form_of_templates -->
  <xsl:function name="myfn:is-form-of" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean($li[link[@rel = 'mw:PageProp/Category' and
                (some $cat in ('_forms', '_participles', 'Plurals')
                 satisfies ends-with(@href, $cat))]])"/>
  </xsl:function>

  <xsl:function name="myfn:form-of-targets" as="xs:string*">
    <xsl:param name="li" as="element(li)*"/>
    <xsl:sequence select="distinct-values($li/i ! normalize-space(.))"/>
  </xsl:function>

  <xsl:template match="section" mode="usage-notes">
    <xsl:variable name="content" select="p | ul"/>
    <xsl:if test="$content">
      <section>
        <xsl:apply-templates select="h3" mode="section-heading"/>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
