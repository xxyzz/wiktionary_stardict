<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="etymology">
    <xsl:variable name="content">
      <xsl:apply-templates select="p | ul" mode="etymology-child"/>
    </xsl:variable>

    <xsl:if test="$content/node()">
      <section>
        <xsl:apply-templates select="(h3 | h4)[1]" mode="section-heading"/>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>

  <xsl:template match="p" mode="etymology-child">
    <xsl:variable name="clean-p">
      <xsl:apply-templates select="node()" mode="clean-content"/>
    </xsl:variable>

    <xsl:if
        test="normalize-space(string-join($clean-p//text()[not(parent::style)], ''))">
      <xsl:copy-of select="."/>
    </xsl:if>
  </xsl:template>

  <xsl:mode name="etymology-child" on-no-match="shallow-copy"/>
</xsl:stylesheet>
