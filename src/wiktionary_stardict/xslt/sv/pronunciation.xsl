<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:template match="ul" mode="pron">
    <xsl:variable name="lists">
      <xsl:apply-templates select="li" mode="pron-ul"/>
    </xsl:variable>
    <xsl:if test="$lists/*">
      <ul><xsl:copy-of select="$lists"/></ul>
    </xsl:if>
  </xsl:template>

  <xsl:template match="li" mode="pron-ul">
    <xsl:variable
        name="ipa"
        select=".//span[some $cls in ('ipa', 'oo-ui-labelElement-label')
                satisfies contains-token(@class, $cls)]"/>
    <xsl:if test="$ipa">
      <li>
        <b>uttal: </b>
        <xsl:for-each select="$ipa">
          <span class="ipa">{normalize-space(.)}</span>
        </xsl:for-each>
      </li>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
