<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output method="json" indent="no" encoding="UTF-8"/>

  <xsl:include href="../utils.xsl"/>

  <xsl:template match="/">
    <xsl:variable
        name="forms"
        select=".//table[contains-token(@class, 'inflection-table')]//td/a/
                myfn:a-forms(.)"
        as="xs:string*"/>
    <xsl:sequence select="array{distinct-values($forms[. != ''])}"/>
  </xsl:template>
</xsl:stylesheet>
