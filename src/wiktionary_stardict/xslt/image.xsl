<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:mode name="convert-img" on-no-match="shallow-copy"/>

  <xsl:template match="img/@src" mode="convert-img">
    <xsl:attribute name="src">
      <xsl:value-of
          select="if (contains(., 'math/render/svg/')) then
                  substring-after(., 'math/render/svg/') || '.svg' else
                  replace(substring-before(tokenize(., '/')[last()] || '?', '?'),
                  '\..*\.', '.')"/>
    </xsl:attribute>
  </xsl:template>
</xsl:stylesheet>
