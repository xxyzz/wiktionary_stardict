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
        <h4 class="Jpan">語源</h4>
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
      <p><xsl:copy-of select="$clean-p"/></p>
    </xsl:if>
  </xsl:template>

  <xsl:mode name="etymology-child" on-no-match="shallow-copy"/>
</xsl:stylesheet>
