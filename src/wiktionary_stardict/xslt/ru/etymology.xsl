<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="etymology">
    <xsl:variable name="content">
      <xsl:apply-templates
          select="p[node() and not(link[@rel = 'mw:PageProp/Category' and
                  ends-with(@href, 'Категория:Нужна_этимология')])]"
          mode="clean-content"/>
    </xsl:variable>
    <xsl:if test="$content/*">
      <section>
        <h4>Этимология</h4>
        <xsl:copy-of select="$content"/>
      </section>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
