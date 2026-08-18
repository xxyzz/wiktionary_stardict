<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:function name="myfn:get-conj-forms" as="xs:string*">
    <xsl:param name="section" as="element(section)*"/>
    <xsl:sequence
        select="distinct-values(myfn:get-element-forms(
                for $td in $section//td return if ($td/dl//b) then $td//b else
                if ($td/a) then $td/a else $td))[. != '']"/>
  </xsl:function>

  <xsl:function name="myfn:get-alt-forms" as="xs:string*">
    <xsl:param name="section" as="element(section)*"/>
    <xsl:sequence
        select="distinct-values(myfn:get-element-forms($section//li/a))[. != '']"/>
  </xsl:function>
</xsl:stylesheet>
