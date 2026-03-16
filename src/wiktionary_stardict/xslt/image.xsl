<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:template match="img" mode="convert-img">
    <img>
      <xsl:copy-of select="@*[not(local-name() = 'src')]"/>
      <xsl:attribute name="src">
        <xsl:choose>
          <xsl:when test="contains(@src, 'math/render/svg/')">
            <xsl:value-of select="substring-after(@src, 'math/render/svg/')"/>
            <xsl:text>.svg</xsl:text>
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of
                select="replace(
                        substring-before(tokenize(@src, '/')[last()] || '?', '?'),
                        '\..*\.',
                        '.')"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:attribute>
    </img>
  </xsl:template>

  <xsl:template match="*" mode="convert-img">
    <xsl:element name="{local-name()}">
      <xsl:copy-of select="@*"/>
      <xsl:apply-templates mode="convert-img"/>
    </xsl:element>
  </xsl:template>
</xsl:stylesheet>
