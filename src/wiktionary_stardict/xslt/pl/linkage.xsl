<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">
  <xsl:template match="dl" mode="linkage">
    <xsl:param name="pos-index" as="xs:integer"/>
    <xsl:variable name="selected-dd" select="myfn:match-dd(dd, $pos-index)"/>
    <xsl:if test="$selected-dd">
      <dl>
        <xsl:apply-templates select="dt" mode="clean-content"/>
        <xsl:apply-templates select="$selected-dd" mode="clean-content"/>
      </dl>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
