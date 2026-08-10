<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="etymology">
    <xsl:param name="pos-index"/>
    <xsl:variable name="matched-li" select="ul/li[text()[contains(., $pos-index)]]"/>
    <xsl:variable name="use-li"
                  select="if ($matched-li) then $matched-li else ul/li[not(table)]"/>
    <xsl:if test="$use-li">
      <section>
        <xsl:apply-templates select="h4" mode="section-heading"/>
        <ul>
          <xsl:apply-templates select="$use-li" mode="clean-content"/>
        </ul>
      </section>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
