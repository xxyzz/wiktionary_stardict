<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:function name="myfn:headword-strong-forms" as="xs:string*">
    <xsl:param name="p" as="element(p)*"/>
    <xsl:sequence
        select="myfn:ruby-text($p//strong[contains-token(@class, 'headword')]) !
                replace(., '⫽', '')"/>
  </xsl:function>

  <xsl:function name="myfn:headword-b-forms" as="xs:string*">
    <xsl:param name="p" as="element(p)*"/>
    <xsl:sequence
        select="myfn:get-element-forms($p
                [not(span[@data-mw and myfn:is-template(@data-mw,
                ('th-noun', 'ja-noun', 'de-verb'))])]//b)"/>
  </xsl:function>
</xsl:stylesheet>
