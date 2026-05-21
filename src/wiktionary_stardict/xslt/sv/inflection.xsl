<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:function name="myfn:get-grammar-table-forms" as="xs:string*">
    <xsl:param name="table" as="element(table)*"/>
    <xsl:sequence
        select="distinct-values($table//td/span/(a|span) ! myfn:get-element-forms(.))"/>
  </xsl:function>
</xsl:stylesheet>
