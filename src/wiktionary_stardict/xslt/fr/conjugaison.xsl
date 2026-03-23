<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output method="json" indent="no" encoding="UTF-8"/>

  <xsl:template match="/">
    <xsl:variable
        name="forms"
        select=".//td[@align='left' and not(contains-token(@class, 'API'))]/
                normalize-space()"
        as="xs:string*"/>
    <xsl:sequence select="array{distinct-values($forms[. != ''])}"/>
  </xsl:template>
</xsl:stylesheet>
