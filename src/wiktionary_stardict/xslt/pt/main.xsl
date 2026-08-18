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
              select="html/body/section[normalize-space(h1[1]) = $allowed-languages]"
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
    <xsl:variable
        name="t-names"
        select="parse-json((h1/style[@data-mw]/@data-mw)[1])?parts?*
                [. instance of map(*)]?template?target?wt !
                myfn:convert-template-name(.)"/>
    <xsl:variable
        name="lemma-code"
        select="replace($t-names[starts-with(., '-') and ends-with(., '-')][1],
                '^-|-$', '')"/>
    <xsl:apply-templates select=".//section[p/b and ol]" mode="pos">
      <xsl:with-param name="language" select="normalize-space(h1[1])"/>
      <xsl:with-param name="lemma-code" select="$lemma-code"/>
    </xsl:apply-templates>
  </xsl:template>
</xsl:stylesheet>
