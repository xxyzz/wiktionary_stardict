<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:template match="section" mode="linkage">
    <xsl:variable name="content">
      <xsl:apply-templates select="div[contains-token(@class, 'boite')] | ul"
                           mode="linkage-list"/>
    </xsl:variable>
    <xsl:if test="$content">
      <section>
        <xsl:apply-templates select="h4 | h5 | h6" mode="section-title"/>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>

  <xsl:template match="ul" mode="linkage-list">
    <ul>
      <xsl:sequence select="li[position() lt 7]"/>
    </ul>
  </xsl:template>
  <xsl:mode name="linkage-list" on-no-match="shallow-copy"/>
</xsl:stylesheet>
