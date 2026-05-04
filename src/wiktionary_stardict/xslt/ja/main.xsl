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

  <!-- https://ja.wiktionary.org/wiki/Wiktionary:スタイルマニュアル -->
  <xsl:template match="/">
    <xsl:choose>
      <xsl:when
          test="not(starts-with($title, 'シソーラス:') or ends-with($title, '(活用)'))">
        <xsl:variable name="results" as="map(*)*">
          <xsl:apply-templates
              select="html/body/section[normalize-space(h2) = $allowed-languages]"
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
    <xsl:variable name="language" select="normalize-space(h2)"/>
    <xsl:apply-templates
        select=".//section[
                  ol and (p/strong[contains-token(@class, 'headword')] or p//b)]"
        mode="pos">
      <xsl:with-param name="language" select="$language"/>
    </xsl:apply-templates>
  </xsl:template>

  <!-- IPA appendix link -->
  <xsl:template match="(small|sup)[normalize-space() = '(?)']" mode="clean-content"/>

  <!-- Remove Template:maintenance line -->
  <xsl:template
      match="span[contains-token(@class, 'maintenance-line')]" mode="clean-content"/>
  <!-- Remove Template:wikipedia -->
  <xsl:template
      match="div[contains-token(@class, 'sisterproject')]" mode="clean-content"/>

  <xsl:template match="a[contains-token(@class, 'mw-selflink')]" mode="clean-content">
    <b><xsl:apply-templates mode="clean-content"/></b>
  </xsl:template>

  <!-- Template:wikipedia-s -->
  <xsl:template match="sup[normalize-space() = '(wp)']" mode="clean-content"/>
</xsl:stylesheet>
