<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:mode name="convert-img" on-no-match="shallow-copy"/>

  <xsl:template match="img/@src" mode="convert-img">
    <xsl:attribute name="src">
      <xsl:value-of
          select="replace(substring-before(tokenize(., '/')[last()] || '?', '?'),
                  '\..*\.', '.')"/>
    </xsl:attribute>
  </xsl:template>

  <xsl:function name="myfn:get-svg-data" as="item()*">
    <xsl:param name="input-ele"/>
    <xsl:sequence
        select="$input-ele//*[some $cls in ('mw-ext-score', 'mw-ext-score-disabled',
                'mwe-math-element') satisfies contains-token(@class, $cls)]/@data-mw !
                parse-json(.)"/>
  </xsl:function>
</xsl:stylesheet>
