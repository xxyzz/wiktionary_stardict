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

  <xsl:variable
      name="title" select="html/head/title/text()" as="xs:string"/>

  <!-- https://el.wiktionary.org/wiki/Βικιλεξικό:Δομή_λημμάτων -->
  <xsl:template match="/">
    <xsl:choose>
      <!-- skip language portal pages -->
      <xsl:when test="not(starts-with($title, 'Πύλη:'))">
        <xsl:variable name="results" as="map(*)*">
          <xsl:apply-templates
              select="html/body/section[myfn:get-language(h2) = $allowed-languages]"
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
        select=".//section[(h3|h4)[span[contains-token(@class, 'partofspeech')]] and
                (ol or ul)]"
        mode="pos">
      <xsl:with-param name="language" select="myfn:get-language(h2)"/>
    </xsl:apply-templates>
  </xsl:template>

  <xsl:function name="myfn:get-language" as="xs:string">
    <xsl:param name="h2" as="element(h2)?"/>
    <xsl:sequence select="normalize-space(substring-before($h2, '('))"/>
  </xsl:function>

  <!-- sound file -->
  <xsl:template match="span[contains-token(@typeof, 'mw:Extension/phonos')]"
                mode="clean-content"/>
</xsl:stylesheet>
