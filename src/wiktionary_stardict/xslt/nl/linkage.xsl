<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="linkage">
    <xsl:if test=".//ul">
      <section>
        <xsl:apply-templates select="h5" mode="section-heading"/>
        <ul>
          <xsl:apply-templates
              select="(.//ul/li)[position() le 6]" mode="clean-content"/>
        </ul>
      </section>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
