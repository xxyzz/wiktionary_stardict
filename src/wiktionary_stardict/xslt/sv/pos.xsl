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
  <xsl:include href="inflection.xsl"/>
  <xsl:include href="pronunciation.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:param name="language"/>
    <xsl:variable
        name="headword-forms" select="p/b[1] ! normalize-space(.)" as="xs:string*"/>
    <xsl:variable
        name="table-forms" as="xs:string*"
        select="myfn:get-grammar-table-forms(
                table[contains-token(@class, 'grammar')])"/>
    <xsl:variable
        name="unique-forms" as="xs:string*"
        select="distinct-values(($headword-forms, $title, $table-forms)[. != ''])"/>

    <xsl:variable name="definition">
      <section class="mw-parser-output" dir="ltr" lang="sv">
        <xsl:apply-templates select="h3 | h4 | h5 | h6" mode="pos-heading"/>
        <xsl:apply-templates select="p | ul | ol | dl" mode="pos-li"/>
      </section>
    </xsl:variable>

    <xsl:variable name="images" as="xs:string*">
      <xsl:sequence select="$definition//img/@src"/>
    </xsl:variable>

    <xsl:variable name="final-definition">
      <xsl:apply-templates select="$definition" mode="convert-img"/>
    </xsl:variable>

    <xsl:variable name="form-of-only" as="xs:boolean">
      <xsl:sequence
          select="boolean(every $li in ol/li satisfies myfn:is-form-of($li))"/>
    </xsl:variable>

    <xsl:sequence
        select="map{'lang': $language,
                'forms': array{$unique-forms},
                'def': serialize(
                  $final-definition, map{'method': 'html', 'indent': false()}),
                'images': array{$images},
                'form_of_targets': array{if ($form-of-only) then
                  myfn:form-of-targets(ol/li) else ()},
                'form_of_only': $form-of-only,
                'ids': array{myfn:get-ancestor-section-ids(.)}}"/>
  </xsl:template>

  <xsl:template match="h3 | h4 | h5 | h6" mode="pos-heading">
    <h4><xsl:apply-templates mode="clean-content"/></h4>
  </xsl:template>

  <xsl:template match="ol" mode="pos-li">
    <ol><xsl:apply-templates mode="pos-li"/></ol>
  </xsl:template>

  <xsl:template match="li" mode="pos-li">
    <li><xsl:apply-templates mode="pos-li"/></li>
  </xsl:template>

  <xsl:template match="dl" mode="pos-li">
    <xsl:variable
        name="examples"
        select="dd[node() and not(em or span[contains-token(@typeof, 'mw:File')])]"/>
    <xsl:variable
        name="linkages"
        select="dd[some $cls in ('template-synonymer', 'template-antonymer',
                'template-etymologi', 'template-användning')
                satisfies contains-token(@class, $cls)]"/>
    <xsl:if test="$examples or $linkages">
      <dl>
        <xsl:apply-templates
            select="($examples[string-length() = min($examples/string-length())])[1]"
            mode="clean-content"/>
        <xsl:apply-templates select="$linkages" mode="clean-content"/>
      </dl>
    </xsl:if>
  </xsl:template>

  <xsl:template match="ul" mode="pos-li">
    <xsl:apply-templates select="." mode="pron"/>
  </xsl:template>

  <xsl:template match="*" mode="pos-li">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>

  <xsl:function name="myfn:is-form-of" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean($li/link[contains-token(@rel, 'mw:PageProp/Category') and
                contains(@href, 'former#')])"/>
  </xsl:function>

  <xsl:function name="myfn:form-of-targets" as="xs:string*">
    <xsl:param name="li" as="element(li)*"/>
    <xsl:sequence select="distinct-values($li/a ! normalize-space(.))"/>
  </xsl:function>
</xsl:stylesheet>
