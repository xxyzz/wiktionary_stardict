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

  <xsl:template match="/">
    <xsl:variable name="results" as="map(*)*">
      <xsl:apply-templates
          select="html/body/section[normalize-space(h2/a[1]) = $allowed-languages]"
          mode="language"/>
    </xsl:variable>
    <xsl:sequence select="array{$results}"/>
  </xsl:template>

  <xsl:template match="section" mode="language">
    <xsl:variable name="language" select="normalize-space(h2/a[1])"/>
    <xsl:apply-templates
        select=".//section[h3 and p[@data-mw and
                myfn:is-template(@data-mw, 'Bedeutungen') and
                following-sibling::*[1][self::dl]]]"
        mode="pos">
      <xsl:with-param name="language" select="$language"/>
    </xsl:apply-templates>
  </xsl:template>
</xsl:stylesheet>
