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

  <xsl:function name="myfn:get-math-tex" as="xs:string*">
    <xsl:param name="input-ele"/>
    <xsl:sequence
        select="$input-ele//*[contains-token(@class, 'mwe-math-element') and @data-mw]/
                parse-json(@data-mw)?body?extsrc"/>
  </xsl:function>
</xsl:stylesheet>
