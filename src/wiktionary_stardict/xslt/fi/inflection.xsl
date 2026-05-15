<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:function name="myfn:get-headword-table-forms" as="xs:string*">
    <xsl:param name="table" as="element(table)*"/>
    <xsl:sequence select="myfn:get-element-forms($table//td/b)"/>
  </xsl:function>

  <xsl:function name="myfn:get-inflection-section-forms" as="xs:string*">
    <xsl:param name="section" as="element(section)*"/>
    <xsl:sequence
        select="distinct-values((for $tbody in $section//tbody return
                if ($tbody//td/span[@lang]) then
                $tbody//td/span[@lang] else $tbody//td) !
                myfn:get-element-forms(.))[not(. = ('', '-'))]"/>
  </xsl:function>
</xsl:stylesheet>
