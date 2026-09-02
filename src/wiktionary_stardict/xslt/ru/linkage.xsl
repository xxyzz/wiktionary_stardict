<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="linkage">
    <xsl:variable name="content">
      <xsl:apply-templates select="ol" mode="filter-linkage-ol"/>
    </xsl:variable>
    <xsl:if test="$content/*">
      <section>
        <xsl:apply-templates select="h4" mode="section-heading"/>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>

  <xsl:template match="h4" mode="linkage-from-gloss">
    <xsl:variable name="list" as="element(ol)*">
      <xsl:apply-templates
          select="following-sibling::div
                  [contains-token(@class, 'mw-references-wrap')][1]/ol"
          mode="gloss-linkage-ol"/>
    </xsl:variable>
    <xsl:variable name="content">
      <xsl:apply-templates select="$list" mode="filter-linkage-ol"/>
    </xsl:variable>
    <xsl:if test="$content/*">
      <section>
        <xsl:apply-templates select="." mode="section-heading"/>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>

  <xsl:template
      match="span[contains-token(@class, 'mw-cite-backlink')]" mode="gloss-linkage-ol"/>
  <xsl:mode name="gloss-linkage-ol" on-no-match="shallow-copy"/>

  <xsl:template match="ol" mode="filter-linkage-ol">
    <xsl:variable name="lists">
      <xsl:apply-templates select="li" mode="filter-linkage-li"/>
    </xsl:variable>
    <xsl:if test="$lists/*">
      <xsl:copy>
        <xsl:copy-of select="@*"/>
        <xsl:copy-of select="$lists"/>
      </xsl:copy>
    </xsl:if>
  </xsl:template>

  <xsl:template match="li" mode="filter-linkage-li">
    <xsl:if test="not(normalize-space(.) = ('—', '?', '-', ''))">
      <xsl:copy>
        <xsl:copy-of select="@*"/>
        <xsl:attribute name="value">{position()}</xsl:attribute>
        <xsl:copy-of select="node()"/>
      </xsl:copy>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
