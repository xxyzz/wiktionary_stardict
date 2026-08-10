<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="pron">
    <xsl:param name="pos-index"/>
    <xsl:variable name="matched-ul" select="ul/li[text()[contains(., $pos-index)]]/ul"/>
    <xsl:variable name="use-ul" select="if ($matched-ul) then $matched-ul else ul"/>
    <xsl:variable
        name="ipa-li" select="$use-ul/li[a[@title = 'WikiWoordenboek:IPA']]"/>
    <xsl:if test="$ipa-li">
      <ul>
        <xsl:apply-templates select="$ipa-li" mode="clean-content"/>
      </ul>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
