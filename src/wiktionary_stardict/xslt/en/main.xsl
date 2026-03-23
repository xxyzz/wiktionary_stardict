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

  <xsl:template match="/">
    <xsl:choose>
      <xsl:when test="not(ends-with($title, '/translations'))">
        <xsl:variable name="results" as="map(*)*">
          <xsl:apply-templates
              select="html/body/section[h2/text() = $allowed-languages]"
              mode="language"/>
        </xsl:variable>
        <xsl:sequence select="array{$results}"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:sequence select="array{()}"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

  <!-- Language section -->
  <xsl:template match="section" mode="language">
    <xsl:variable name="language" select="h2/text()"/>
    <xsl:apply-templates
        select=".//section[p/span[@class='headword-line'] and ol]"
        mode="pos">
      <xsl:with-param name="language" select="$language"/>
    </xsl:apply-templates>
  </xsl:template>

  <!-- Remove empty li elements -->
  <xsl:template match="li[not(node())]" mode="clean-content"/>

  <!-- IPA key link -->
  <xsl:template match="sup[normalize-space() = '(key)']" mode="clean-content"/>

  <!-- Remove "audio" element expanded from "score sound" -->
  <xsl:template match="div[audio]" mode="clean-content"/>
</xsl:stylesheet>
