<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output method="json" indent="no" encoding="UTF-8"/>

  <xsl:include href="../clean.xsl"/>
  <xsl:include href="config.xsl"/>
  <xsl:include href="pos.xsl"/>

  <xsl:variable
      name="title" select="html/head/title/text()" as="xs:string"/>

  <!-- https://th.wiktionary.org/wiki/วิธีใช้:คู่มือในการเขียน -->
  <xsl:template match="/">
    <xsl:choose>
      <!-- skip translation pages -->
      <xsl:when test="not(ends-with($title, '/คำแปลภาษาอื่น'))">
        <xsl:variable name="results" as="map(*)*">
          <xsl:apply-templates
              select="html/body/section[normalize-space(h2[1]) = $allowed-languages]"
              mode="language"/>
        </xsl:variable>
        <xsl:sequence select="array{$results}"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:sequence select="array{()}"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <xsl:template match="section" mode="language">
    <xsl:apply-templates
        select=".//section[p/span[contains-token(@class, 'headword-line')] and ol]"
        mode="pos">
      <xsl:with-param name="language" select="normalize-space(h2[1])"/>
    </xsl:apply-templates>
  </xsl:template>

  <!-- IPA key link -->
  <xsl:template match="sup[normalize-space() = '(คำอธิบาย)']" mode="clean-content"/>
</xsl:stylesheet>
