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
    <xsl:sequence
        select="parse-xml-fragment($images(parse-json(@data-mw)?body?extsrc))/node()"/>
  </xsl:template>
</xsl:stylesheet>
