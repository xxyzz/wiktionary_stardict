<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output method="json" indent="no" encoding="UTF-8"/>

  <xsl:include href="../utils.xsl"/>
  <xsl:include href="../clean.xsl"/>
  <xsl:include href="config.xsl"/>
  <xsl:include href="pos.xsl"/>

  <xsl:variable name="title" select="html/head/title/text()" as="xs:string"/>

  <!-- https://pt.wiktionary.org/wiki/Wikcionário:Livro_de_estilo -->
  <xsl:template match="/">
    <xsl:choose>
      <!-- skip translation pages -->
      <xsl:when
          test="not(contains($title, '/traduções') or contains($title, '/tradução'))">
        <xsl:variable name="results" as="map(*)*">
          <xsl:apply-templates
              select="html/body/section
                      [h1 and myfn:get-lang-name(h1[1]) = $allowed-languages]"
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
    <xsl:apply-templates select=".//section[p/b and ol]" mode="pos">
      <xsl:with-param name="language" select="myfn:get-lang-name(h1[1])"/>
    </xsl:apply-templates>
  </xsl:template>

  <xsl:function name="myfn:get-lang-name" as="xs:string">
    <xsl:param name="h1" as="element(h1)?"/>
    <xsl:variable name="new-h1">
      <xsl:apply-templates select="$h1" mode="lang-name"/>
    </xsl:variable>
    <xsl:sequence select="tokenize(normalize-space($new-h1), '/')[1]"/>
  </xsl:function>

  <xsl:mode name="lang-name" on-no-match="shallow-copy"/>
  <xsl:template match="style" mode="lang-name"/>
</xsl:stylesheet>
