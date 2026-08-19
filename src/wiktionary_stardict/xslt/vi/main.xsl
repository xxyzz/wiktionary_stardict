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
  <xsl:include href="config.xsl"/>
  <xsl:include href="pos.xsl"/>

  <xsl:variable name="title" select="html/head/title/text()" as="xs:string"/>

  <!-- https://vi.wiktionary.org/wiki/Wiktionary:Sơ_đồ_mục_từ -->
  <xsl:template match="/">
    <xsl:choose>
      <!-- skip thesaurus, rhyme, quote, reconstruct pages -->
      <xsl:when
          test="not(some $prefix in ('Kho từ vựng:', 'Vần:', 'Kho ngữ liệu:',
                'Từ tái tạo:') satisfies starts-with($title, $prefix))">
        <xsl:variable name="results" as="map(*)*">
          <xsl:apply-templates
              select="html/body/section
                      [myfn:convert-lang(normalize-space(h2[last()]))
                      = $allowed-languages]"
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
        select=".//section[p[span[contains-token(@class, 'headword-line')] or .//b]
                and ol]"
        mode="pos">
      <xsl:with-param
          name="language" select="myfn:convert-lang(normalize-space(h2[last()]))"/>
    </xsl:apply-templates>
  </xsl:template>

  <!-- Remove Template:maintenance line, also used in Template:ja-see -->
  <xsl:template
      match="(span|small)[contains-token(@class, 'maintenance-line')]"
      mode="clean-content"/>
</xsl:stylesheet>
