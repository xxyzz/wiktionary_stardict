<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:svg="http://www.w3.org/2000/svg"
    xmlns:xlink="http://www.w3.org/1999/xlink"
    expand-text="yes">
  <xsl:output indent="no" encoding="UTF-8"/>
  <xsl:param name="data"/>
  <xsl:variable name="images" select="parse-json($data)"/>

  <xsl:template match="/">
    <xsl:apply-templates mode="add-svg"/>
  </xsl:template>

  <xsl:mode name="add-svg" on-no-match="shallow-copy"/>
  <xsl:template
      match="*[contains-token(@class, 'mwe-math-element') and @data-mw]"
      mode="add-svg">
    <xsl:apply-templates
        select="parse-xml-fragment($images(parse-json(@data-mw)?body?extsrc))/node()"
        mode="mod-svg-id">
      <xsl:with-param name="svg-id" select="@id"/>
    </xsl:apply-templates>
  </xsl:template>

  <xsl:template
      match="*[some $cls in ('mw-ext-score', 'mw-ext-score-disabled')
             satisfies contains-token(@class, $cls) and @data-mw]"
      mode="add-svg">
    <xsl:variable name="svg">
      <xsl:apply-templates
          select="parse-xml-fragment($images(parse-json(@data-mw)?body?extsrc))/node()"
          mode="mod-svg-id">
        <xsl:with-param name="svg-id" select="@id"/>
      </xsl:apply-templates>
    </xsl:variable>
    <xsl:copy>
      <xsl:copy-of select="@*[not(local-name() = ('id', 'data-mw'))]"/>
      <xsl:apply-templates select="$svg" mode="set-score-size"/>
    </xsl:copy>
  </xsl:template>

  <!-- lilypond's default font size is 11 points -->
  <!-- https://lilypond.org/doc/v2.26/Documentation/notation/formatting-text#selecting-font-and-font-size -->
  <!-- https://lilypond.org/doc/v2.26/Documentation/notation/setting-the-staff-size -->
  <xsl:mode name="set-score-size" on-no-match="shallow-copy"/>
  <xsl:template
      match="svg:svg/@*[local-name() = ('width', 'height')]" mode="set-score-size">
    <xsl:attribute name="{name()}" select="round(number(.) div 11, 1) || 'em'"/>
  </xsl:template>

  <xsl:mode name="mod-svg-id" on-no-match="shallow-copy"/>
  <xsl:template match="@id" mode="mod-svg-id">
    <xsl:param name="svg-id"/>
    <xsl:attribute name="id" select="$svg-id || ."/>
  </xsl:template>
  <xsl:template match="@xlink:href" mode="mod-svg-id">
    <xsl:param name="svg-id"/>
    <xsl:attribute name="xlink:href" select="'#' || $svg-id || substring(., 2)"/>
  </xsl:template>

  <!-- sanitize SVG -->
  <xsl:template
      match="*[lower-case(local-name()) = ('script', 'foreignobject', 'iframe',
             'handler', 'audio', 'video', 'embed', 'object')]"
      mode="mod-svg-id"/>
  <xsl:template
      match="@*[starts-with(lower-case(local-name()), 'on')]" mode="mod-svg-id"/>
  <xsl:template
      match="@*[lower-case(local-name()) = 'href' and
             starts-with(lower-case(replace(., '\s+', '')), 'javascript:')]"
      mode="mod-svg-id"/>
</xsl:stylesheet>
