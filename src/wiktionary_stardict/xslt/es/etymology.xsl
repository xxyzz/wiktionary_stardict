<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    expand-text="yes"
    exclude-result-prefixes="#all">

 <xsl:template match="section" mode="etymology">
    <xsl:variable name="content">
      <xsl:apply-templates select="p | ul" mode="etymology-child"/>
    </xsl:variable>

    <xsl:if test="$content/node()">
      <section>
        <h4>Etimología</h4>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
 </xsl:template>

 <!-- missing etymology -->
 <xsl:template
     match="p[.//link[@rel = 'mw:PageProp/Category' and
            ends-with(@href, ':Palabras_de_etimología_sin_precisar')]]"
     mode="etymology-child"/>

 <xsl:mode name="etymology-child" on-no-match="shallow-copy"/>
</xsl:stylesheet>
