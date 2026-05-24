<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output method="json" indent="no" encoding="UTF-8"/>

  <xsl:include href="../clean.xsl"/>
  <xsl:include href="../utils.xsl"/>
  <xsl:include href="config.xsl"/>
  <xsl:include href="pos.xsl"/>

  <xsl:variable
      name="title" select="html/head/title/text()" as="xs:string"/>

  <!-- https://zh.wiktionary.org/wiki/Wiktionary:佈局解釋
       https://zh.wiktionary.org/wiki/Wiktionary:體例說明 -->
  <xsl:template match="/">
    <xsl:choose>
      <xsl:when test="not(some $suffix in ('/翻譯', '/衍生詞')
                      satisfies ends-with($title, $suffix))">
        <xsl:variable name="results" as="map(*)*">
          <xsl:apply-templates
              select="html/body/section[
                      myfn:combine-lang(normalize-space(h2)) = $allowed-languages]"
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
    <xsl:variable name="language" select="myfn:combine-lang(normalize-space(h2))"/>
    <xsl:variable name="new-section">
      <xsl:apply-templates select="." mode="lang-converter"/>
    </xsl:variable>
    <xsl:apply-templates
        select="$new-section//section[p/span[contains-token(@class, 'headword-line')]
                and ol]"
        mode="pos">
      <xsl:with-param name="language" select="$language"/>
    </xsl:apply-templates>
  </xsl:template>

  <!-- IPA key link -->
  <xsl:template match="sup[normalize-space() = '(幫助)']" mode="clean-content"/>

  <!-- Remove Template:maintenance line -->
  <xsl:template
      match="span[contains-token(@class, 'maintenance-line')]" mode="clean-content"/>
  <!-- Remove Template:wikipedia Template:multiple images -->
  <xsl:template
      match="div[some $class in ('floatright', 'tmulti')
             satisfies contains-token(@class, $class)]" mode="clean-content"/>
  <!-- Remove hidden node from Template:Pedialite -->
  <xsl:template
      match="*[contains-token(@class, 'interProject')]" mode="clean-content"/>
</xsl:stylesheet>
