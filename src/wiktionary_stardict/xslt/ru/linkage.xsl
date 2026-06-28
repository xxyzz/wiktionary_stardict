<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="linkage">
    <xsl:variable name="content" select="myfn:filter-linkage-li(ol)"/>
    <xsl:if test="$content">
      <section>
        <xsl:apply-templates select="h4" mode="section-title"/>
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
    <xsl:variable name="content" select="myfn:filter-linkage-li($list)"/>
    <xsl:if test="$content">
      <section>
        <xsl:apply-templates select="." mode="section-title"/>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>

  <xsl:template
      match="span[contains-token(@class, 'mw-cite-backlink')]" mode="gloss-linkage-ol"/>
  <xsl:mode name="gloss-linkage-ol" on-no-match="shallow-copy"/>

  <xsl:function name="myfn:filter-linkage-li" as="element(ol)*">
    <xsl:param name="ol" as="element(ol)*"/>
    <xsl:sequence
        select="$ol[li and not(every $li in li satisfies normalize-space($li) =
                ('—', '?'))]"/>
  </xsl:function>
</xsl:stylesheet>
