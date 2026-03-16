<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:include href="../image.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:param name="language"/>
    <xsl:variable
        name="pos" select="normalize-space((h3 | h4 | h5 | h6)[1])" as="xs:string"/>
    <xsl:if test="not(starts-with($pos, 'Forma '))">
      <xsl:variable name="definition">
        <section>
          <xsl:apply-templates select="h3 | h4 | h5 | h6" mode="pos"/>
          <xsl:apply-templates select="p | dl" mode="pos"/>
        </section>
      </xsl:variable>

      <xsl:variable name="images" as="xs:string*">
        <xsl:sequence select="$definition//img/@src"/>
      </xsl:variable>

      <xsl:variable name="final-definition">
        <xsl:apply-templates select="$definition" mode="convert-img"/>
      </xsl:variable>

      <xsl:sequence
          select="array{$language, array{$title}, $final-definition, array{$images}}"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="h3 | h4 | h5 | h6" mode="pos">
    <h4><xsl:apply-templates mode="clean-content"/></h4>
  </xsl:template>

  <xsl:template match="dl" mode="pos">
    <dl><xsl:apply-templates mode="pos"/></dl>
  </xsl:template>

  <xsl:template match="dd" mode="pos">
    <dd><xsl:apply-templates mode="pos"/></dd>
  </xsl:template>

  <xsl:template match="ul" mode="pos">
    <xsl:variable name="linkages" select="li[b/text() = ('Sinónimos:', 'Antónimo:')]"/>
    <xsl:variable
        name="examples"
        select="li[b/text() = 'Ejemplo:' and
                not(div[contains(@class, 'mw-collapsed')])]"/>
    <xsl:if test="$linkages/* or $examples/*">
      <ul>
        <xsl:apply-templates select="$linkages" mode="clean-content"/>
        <xsl:apply-templates
            select="($examples[string-length() = min($examples/string-length())])[1]"
            mode="clean-content"/>
      </ul>
    </xsl:if>
  </xsl:template>

  <xsl:template match="*" mode="pos">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>
</xsl:stylesheet>
