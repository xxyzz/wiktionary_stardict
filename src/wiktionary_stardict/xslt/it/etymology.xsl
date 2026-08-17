<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="etymology">
    <xsl:variable name="content" select="p | ul"/>
    <xsl:if test="$content">
      <section>
        <xsl:apply-templates select="h3" mode="section-heading"/>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
