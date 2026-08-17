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

  <!-- https://it.wiktionary.org/wiki/Wikizionario:Manuale_di_stile
       https://it.wiktionary.org/wiki/Aiuto:Come_iniziare_una_pagina -->
  <xsl:template match="/">
    <xsl:variable name="results" as="map(*)*">
      <xsl:apply-templates
          select="html/body/section[normalize-space((h2/a)[1]) = $allowed-languages]"
          mode="language"/>
    </xsl:variable>
    <xsl:sequence select="array{$results}"/>
  </xsl:template>

  <xsl:template match="section" mode="language">
    <xsl:variable
        name="t-names"
        select="parse-json(h2/(span|link)[@data-mw]/@data-mw)?parts?*
                [. instance of map(*)]?template?target?wt !
                myfn:convert-template-name(.)"/>
    <xsl:variable
        name="lemma-code"
        select="replace($t-names[starts-with(., '-') and ends-with(., '-')][1],
                '^-|-$', '')"/>
    <xsl:apply-templates select=".//section[(p/b or div//big) and ol]" mode="pos">
      <xsl:with-param name="language" select="normalize-space((h2/a)[1])"/>
      <xsl:with-param name="lemma-code" select="$lemma-code"/>
    </xsl:apply-templates>
  </xsl:template>
</xsl:stylesheet>
