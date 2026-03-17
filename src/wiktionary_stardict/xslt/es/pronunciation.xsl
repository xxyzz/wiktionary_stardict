<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:template match="table" mode="pron">
    <xsl:variable name="lists">
      <xsl:apply-templates select=".//tr" mode="pron"/>
    </xsl:variable>
    <xsl:if test="$lists">
      <ul><xsl:copy-of select="$lists"/></ul>
    </xsl:if>
  </xsl:template>

  <xsl:template match="tr" mode="pron">
    <xsl:for-each
        select="td[b[normalize-space() = 'silabación'] or
                a[@title = 'Alfabeto Fonético Internacional']]">
      <li>
        <xsl:apply-templates select="./node()" mode="clean-content"/>
        <xsl:text>: </xsl:text>
        <xsl:apply-templates
            select="following-sibling::td/text()" mode="clean-content"/>
      </li>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>
