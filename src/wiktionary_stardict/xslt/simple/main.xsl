<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output method="json" indent="no" encoding="UTF-8"/>

  <xsl:include href="../clean.xsl"/>
  <xsl:include href="pos.xsl"/>

  <xsl:variable
      name="title" select="html/head/title/text()" as="xs:string"/>

  <!-- https://simple.wiktionary.org/wiki/Wiktionary:Entry_layout_explained -->
  <xsl:template match="/">
    <xsl:variable name="results" as="map(*)*">
      <xsl:apply-templates select="html/body/section[h2]" mode="pos"/>
    </xsl:variable>
    <xsl:sequence select="array{$results}"/>
  </xsl:template>

  <!-- IPA key link -->
  <xsl:template match="sup[normalize-space() = '(key)']" mode="clean-content"/>
</xsl:stylesheet>
