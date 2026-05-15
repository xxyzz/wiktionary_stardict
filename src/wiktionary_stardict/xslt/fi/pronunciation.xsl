<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="pron">
    <xsl:apply-templates select="ul" mode="pron-ul"/>
  </xsl:template>

  <xsl:template match="ul" mode="pron-ul">
    <xsl:variable name="lists">
      <xsl:apply-templates select="li" mode="pron-ul"/>
    </xsl:variable>
    <xsl:if test="$lists/*">
      <ul><xsl:copy-of select="$lists"/></ul>
    </xsl:if>
  </xsl:template>

  <xsl:template match="li" mode="pron-ul">
    <xsl:if test="a[@title = 'Liite:Ääntäminen'] or starts-with(text(), 'tavutus:')">
      <li>
        <xsl:apply-templates mode="pron-ul"/>
      </li>
    </xsl:if>
  </xsl:template>

  <xsl:template match="*" mode="pron-ul">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>
</xsl:stylesheet>
