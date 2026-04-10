<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:template match="p" mode="pronunciation">
    <section>
      <xsl:apply-templates select="following-sibling::dl[1]" mode="pron"/>
    </section>
  </xsl:template>

  <xsl:template match="dl" mode="pron">
    <xsl:variable name="lists">
      <xsl:apply-templates select="dd" mode="pron"/>
    </xsl:variable>
    <xsl:if test="$lists/*">
      <dl><xsl:apply-templates select="$lists" mode="clean-content"/></dl>
    </xsl:if>
  </xsl:template>

  <xsl:template match="dd" mode="pron">
    <xsl:if test="a[@title = 'Hilfe:IPA']">
      <dd><xsl:apply-templates mode="pron"/></dd>
    </xsl:if>
  </xsl:template>
  <xsl:mode name="pron" on-no-match="shallow-copy"/>
</xsl:stylesheet>
