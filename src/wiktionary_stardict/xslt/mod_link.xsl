<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output
      method="html"
      html-version="5"
      indent="no"
      escape-uri-attributes="no"
      encoding="UTF-8"/>
  <xsl:param name="data"/>
  <xsl:variable name="links" select="parse-json($data)"/>

  <xsl:template match="/">
    <xsl:apply-templates mode="convert-link"/>
  </xsl:template>

  <xsl:mode name="convert-link" on-no-match="shallow-copy"/>
  <xsl:template
      match="a/@href[contains(., '#') and not(substring-after(., 'bword://') = $links)]"
      mode="convert-link">
    <xsl:attribute name="href">
      <xsl:sequence select="substring-before(., '#')"/>
    </xsl:attribute>
  </xsl:template>
</xsl:stylesheet>
