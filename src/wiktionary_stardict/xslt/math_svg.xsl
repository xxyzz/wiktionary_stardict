<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:svg="http://www.w3.org/2000/svg"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output
      method="html"
      html-version="5"
      indent="no"
      escape-uri-attributes="no"
      encoding="UTF-8"/>
  <xsl:param name="data"/>
  <xsl:variable name="images" select="parse-json($data)"/>

  <xsl:template match="/">
    <xsl:apply-templates mode="convert-math"/>
  </xsl:template>

  <xsl:mode name="convert-math" on-no-match="shallow-copy"/>
  <xsl:template
      match="*[contains-token(@class, 'mwe-math-element') and @data-mw]"
      mode="convert-math">
    <xsl:variable
        name="parsed-node"
        select="parse-xml-fragment($images(parse-json(@data-mw)?body?extsrc))/node()"/>
    <xsl:apply-templates select="$parsed-node" mode="modify-svg"/>
  </xsl:template>

  <!-- the default "ex" unit probably not supported very well and the image is -->
  <!-- too small, switch to "em" -->
  <xsl:mode name="modify-svg" on-no-match="shallow-copy"/>
  <xsl:template match="svg:svg/@style" mode="modify-svg">
    <xsl:variable
        name="size"
        select="substring-before(., 'ex') => substring-after('vertical-align:') =>
                number()"/>
    <xsl:attribute name="style">vertical-align:{$size * 1.5}em</xsl:attribute>
  </xsl:template>
  <xsl:template
      match="svg:svg/@*[local-name() = ('width', 'height')]" mode="modify-svg">
    <xsl:variable name="size" select="number(substring-before(., 'ex'))"/>
    <xsl:attribute name="{name()}" select="string($size * 1.5) || 'em'"/>
  </xsl:template>
</xsl:stylesheet>
