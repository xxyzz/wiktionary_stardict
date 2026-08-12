<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="pron">
    <xsl:variable name="ipa-dd" select="dl/dd[a[@title = 'ΔΦΑ']]"/>
    <xsl:if test="$ipa-dd">
      <dl>
        <xsl:apply-templates select="$ipa-dd" mode="clean-content"/>
      </dl>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
