<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output method="json" indent="no" encoding="UTF-8"/>

  <xsl:include href="config.xsl"/>
  <xsl:include href="pos.xsl"/>

  <xsl:variable
      name="title" select="html/head/title/text()" as="xs:string"/>

  <xsl:template match="/">
    <xsl:choose>
      <xsl:when test="not(ends-with($title, '/translations'))">
        <xsl:variable name="results" as="array(*)*">
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
        select=".//section[p/span[@class='headword-line']]"
        mode="pos">
      <xsl:with-param name="language" select="$language"/>
    </xsl:apply-templates>
  </xsl:template>

  <!-- Remove attributes except class and style -->
  <xsl:template match="*" mode="clean-content">
    <xsl:element name="{name()}">
      <xsl:copy-of select="@*[not(name() = ('typeof', 'about', 'id', 'rel', 'srcset', 'resource') or starts-with(name(), 'data-'))]"/>
      <xsl:apply-templates mode="clean-content"/>
    </xsl:element>
  </xsl:template>

  <!-- Remove category links -->
  <xsl:template match="link" mode="clean-content"/>

  <!-- Remove a elements but keep their text content -->
  <xsl:template match="a" mode="clean-content">
    <xsl:apply-templates mode="clean-content"/>
  </xsl:template>

  <!-- Remove empty li elements -->
  <xsl:template match="li[not(*)]" mode="clean-content"/>

  <!-- Copy text nodes as-is -->
  <xsl:template match="text()" mode="clean-content">
    <xsl:copy/>
  </xsl:template>

  <!-- Remove hidden elements -->
  <xsl:template
      match="*[contains(@style, 'display: none;')]"
      mode="clean-content"/>

  <!-- IPA key link -->
  <xsl:template match="sup[normalize-space(.) = '(key)']" mode="clean-content"/>

  <xsl:template
      match="sup[contains(@class, 'mw-ref')]" mode="clean-content"/>
  <xsl:template
      match="figure[@typeof = 'mw:File/Thumb']" mode="clean-content"/>

  <!-- Remove "audio" element expanded from "score sound" -->
  <xsl:template match="div[audio]" mode="clean-content"/>
</xsl:stylesheet>
