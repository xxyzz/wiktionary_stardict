<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:svg="http://www.w3.org/2000/svg"
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
    <xsl:sequence
        select="parse-xml-fragment($images(parse-json(@data-mw)?body?extsrc))/node()"/>
  </xsl:template>

  <xsl:template
      match="*[some $cls in ('mw-ext-score', 'mw-ext-score-disabled')
             satisfies contains-token(@class, $cls) and @data-mw]"
      mode="add-svg">
    <xsl:copy>
      <xsl:copy-of select="@* except @data-mw"/>
      <xsl:apply-templates
          select="parse-xml-fragment($images(parse-json(@data-mw)?body?extsrc))/node()"
          mode="enlarge-score-svg"/>
    </xsl:copy>
  </xsl:template>

  <xsl:mode name="enlarge-score-svg" on-no-match="shallow-copy"/>
  <xsl:template
      match="svg:svg/@*[local-name() = ('width', 'height')]" mode="enlarge-score-svg">
    <xsl:attribute name="{name()}" select="number(.) * 2"/>
  </xsl:template>
</xsl:stylesheet>
