<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema">

  <xsl:template match="section" mode="alt-forms" as="xs:string*">
    <xsl:sequence select="ul/li/span[@lang]//text()"/>
  </xsl:template>
</xsl:stylesheet>
