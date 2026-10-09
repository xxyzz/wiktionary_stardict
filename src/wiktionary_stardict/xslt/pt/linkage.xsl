<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="linkage">
    <xsl:param name="use-h5" select="false()" as="xs:boolean"/>
    <xsl:variable name="contents">
      <xsl:apply-templates mode="linkage-content"/>
    </xsl:variable>
    <xsl:if test="$contents//ul">
      <section>
        <xsl:apply-templates select="h2 | h3 | h4 | h5 | h6" mode="section-heading">
          <xsl:with-param name="use-h5" select="$use-h5"/>
        </xsl:apply-templates>
        <xsl:apply-templates
            select="$contents/(p | *[self::ul or .//ul])" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>

  <xsl:mode name="linkage-content" on-no-match="shallow-copy"/>

  <xsl:template match="ul" mode="linkage-content">
    <xsl:copy>
      <xsl:copy-of select="@*"/>
      <xsl:apply-templates select="li[position() le 6]" mode="linkage-content"/>
    </xsl:copy>
  </xsl:template>

  <xsl:template match="ul[contains-token(@class, 'gallery')]" mode="linkage-content"/>

  <xsl:template match="section" mode="linkage-content">
    <xsl:apply-templates select="." mode="linkage">
      <xsl:with-param name="use-h5" select="true()"/>
    </xsl:apply-templates>
  </xsl:template>

  <xsl:template match="table" mode="linkage-content">
    <xsl:apply-templates select=".//td/*" mode="linkage-content"/>
  </xsl:template>
</xsl:stylesheet>
