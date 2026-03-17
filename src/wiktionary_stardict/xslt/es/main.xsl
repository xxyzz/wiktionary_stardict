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
    <xsl:variable name="results" as="array(*)*">
      <xsl:apply-templates
          select="html/body/section[some $lang in $allowed-languages
                  satisfies starts-with(normalize-space(h2), $lang)]"
          mode="language"/>
    </xsl:variable>
    <xsl:sequence select="array{$results}"/>
  </xsl:template>

  <!-- Language section -->
  <xsl:template match="section" mode="language">
    <xsl:variable name="h2-text" select="normalize-space(h2)"/>
    <xsl:apply-templates select=".//section[dl]" mode="pos">
      <xsl:with-param
          name="language" select="$allowed-languages[starts-with($h2-text, .)][1]"/>
    </xsl:apply-templates>
  </xsl:template>
</xsl:stylesheet>
