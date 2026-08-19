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
  <xsl:include href="utils.xsl"/>
  <xsl:include href="pos.xsl"/>

  <xsl:variable name="title" select="html/head/title/text()" as="xs:string"/>

  <!-- https://pl.wiktionary.org/wiki/Wikisłownik:Zasady_tworzenia_haseł -->
  <xsl:template match="/">
    <xsl:variable name="results" as="map(*)*">
      <xsl:apply-templates
          select="html/body/section[normalize-space(
                  h2/span[contains-token(@class, 'lang-code')]) = $allowed-languages]"
          mode="language"/>
    </xsl:variable>
    <xsl:sequence select="array{$results}"/>
  </xsl:template>

  <xsl:template match="section" mode="language">
    <xsl:apply-templates select="p[i]" mode="pos">
      <xsl:with-param
          name="language"
          select="normalize-space((h2/span[contains-token(@class, 'lang-code')])[1])"/>
      <xsl:with-param
          name="ids"
          select="h2/@id, h2/span[contains-token(@class, 'lang-code')]/@id"/>
    </xsl:apply-templates>
  </xsl:template>
</xsl:stylesheet>
