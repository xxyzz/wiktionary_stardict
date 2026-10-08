<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:template match="p" mode="pronunciation">
    <xsl:apply-templates select="following-sibling::dl[1]" mode="pron"/>
  </xsl:template>

  <xsl:template match="dl" mode="pron">
    <xsl:variable name="lists">
      <xsl:apply-templates select="dd" mode="pron"/>
    </xsl:variable>
    <xsl:if test="exists($lists/*)">
      <dl><xsl:apply-templates select="$lists" mode="clean-content"/></dl>
    </xsl:if>
  </xsl:template>

  <xsl:template match="dd" mode="pron">
    <xsl:if test="exists(.//span[contains-token(@class, 'ipa') and
                  not(normalize-space(.) = '…')])">
      <dd><xsl:apply-templates mode="pron"/></dd>
    </xsl:if>
  </xsl:template>
  <xsl:mode name="pron" on-no-match="shallow-copy"/>
</xsl:stylesheet>
