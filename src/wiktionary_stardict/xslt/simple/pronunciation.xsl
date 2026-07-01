<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="pron">
    <xsl:apply-templates select="ul" mode="pron-ul"/>
  </xsl:template>

  <xsl:template match="ul" mode="pron-ul">
    <xsl:variable name="lists">
      <xsl:apply-templates
          select="li[a[@title = 'w:en:IPA chart for English']]" mode="clean-content"/>
    </xsl:variable>
    <xsl:if test="$lists/*">
      <ul><xsl:copy-of select="$lists"/></ul>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
