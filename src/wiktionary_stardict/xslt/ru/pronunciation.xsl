<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="pronunciation">
    <xsl:variable name="content">
      <xsl:apply-templates select=".//ul" mode="pron-ul"/>
    </xsl:variable>
    <xsl:if test="$content/ul/*">
      <section>
        <h4>Произношение</h4>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>

  <xsl:template match="li" mode="pron-ul">
    <xsl:if test="normalize-space(a[1]) = 'МФА'">
      <li>
        <xsl:apply-templates mode="pron-ul"/>
      </li>
    </xsl:if>
  </xsl:template>
  <xsl:template match="table[contains-token(@class, 'audiotable')]" mode="pron-ul"/>
  <xsl:mode name="pron-ul" on-no-match="shallow-copy"/>
</xsl:stylesheet>
