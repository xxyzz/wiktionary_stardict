<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:include href="../utils.xsl"/>
  <xsl:include href="../image.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:param name="language"/>

    <xsl:param
        name="table-forms"
        select="table[contains-token(@class, 'wikitable')]//td/bdi[normalize-space()]"
        as="xs:string*"/>
    <xsl:variable
        name="unique-forms"
        select="distinct-values(($title, $table-forms)[. != ''])"
        as="xs:string*"/>

    <xsl:variable name="definition">
      <section lang="fr" dir="ltr">
        <xsl:apply-templates
            select="h3 | h4 | h5 | h6" mode="pos-li"/>
        <xsl:apply-templates select="p | ol" mode="pos-li"/>
      </section>
    </xsl:variable>

    <xsl:variable name="images" as="xs:string*">
      <xsl:sequence select="$definition//img/@src"/>
    </xsl:variable>

    <xsl:variable name="final-definition">
      <xsl:apply-templates select="$definition" mode="convert-img"/>
    </xsl:variable>

    <xsl:sequence select="map{'lang': $language,
                          'forms': array{$unique-forms},
                          'def': $final-definition,
                          'images': array{$images}}"/>
  </xsl:template>

  <xsl:template match="h3 | h4 | h5 | h6" mode="pos-li">
    <h4><xsl:apply-templates mode="clean-content"/></h4>
  </xsl:template>

  <xsl:template match="ol" mode="pos-li">
    <ol><xsl:apply-templates mode="pos-li"/></ol>
  </xsl:template>

  <xsl:template match="li" mode="pos-li">
    <xsl:if test="node()">
      <li><xsl:apply-templates mode="pos-li"/></li>
    </xsl:if>
  </xsl:template>

  <!-- Find the shortest usage example -->
  <xsl:template match="ul" mode="pos-li">
    <xsl:variable name="examples" select="li[span[q]]"/>
    <xsl:if test="$examples">
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
</xsl:stylesheet>
