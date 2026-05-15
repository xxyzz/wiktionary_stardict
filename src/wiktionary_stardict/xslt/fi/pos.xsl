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

  <xsl:template match="section" mode="pos">
    <xsl:param name="language"/>

    <xsl:variable name="headword-p" select="p[b]"/>
    <xsl:variable
        name="headword-b" select="normalize-space($headword-p/b[1])" as="xs:string"/>
    <xsl:variable
        name="headword-forms" as="xs:string*"
        select="myfn:get-element-forms(tail($headword-p/b))"/>
    <xsl:variable
          name="unique-forms"
          select="distinct-values(($headword-b, $title, $headword-forms)[. != ''])"
          as="xs:string*"/>

    <xsl:variable name="definition">
      <section class="mw-parser-output" dir="ltr" lang="fi">
        <xsl:apply-templates
            select="h3 | h4 | h5 | h6" mode="pos-heading"/>
        <xsl:apply-templates select="p | ol" mode="pos-li"/>
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
          select="boolean(myfn:is-form-of(.) or
                  (every $li in ol/li satisfies myfn:is-form-of($li)))"/>
    </xsl:variable>

    <xsl:sequence
        select="map{'lang': $language,
                'forms': array{$unique-forms},
                'def': serialize(
                  $final-definition, map{'method': 'html', 'indent': false()}),
                'images': array{$images},
                'form_of_targets': array{
                  myfn:form-of-targets(ol/li[if ($is-form-only) then true() else
                    myfn:is-form-of(.)])},
                'form_of_only': $is-form-only}"/>
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

  <!-- Find the shortest usage example -->
  <xsl:template match="dl" mode="pos-li">
    <xsl:variable name="examples" select="dd"/>
    <dl>
      <xsl:apply-templates
          select="($examples[string-length() = min($examples/string-length())])[1]"
          mode="clean-content"/>
    </dl>
  </xsl:template>

  <xsl:template match="*" mode="pos-li">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>

  <xsl:function name="myfn:is-form-of" as="xs:boolean">
    <xsl:param name="node" as="element()"/>
    <xsl:sequence
        select="boolean($node/link[@rel = 'mw:PageProp/Category' and
                contains(@href, '_taivutusmuodot#')])"/>
  </xsl:function>

  <xsl:function name="myfn:form-of-targets" as="xs:string*">
    <xsl:param name="li" as="element(li)*"/>
    <xsl:sequence select="distinct-values($li/b ! normalize-space(.))"/>
  </xsl:function>
</xsl:stylesheet>
