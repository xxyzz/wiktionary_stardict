<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:function name="myfn:get-inflection-forms" as="xs:string*">
    <xsl:param name="dl" as="element(dl)?"/>
    <xsl:param name="pos-index" as="xs:integer"/>
    <xsl:variable name="matched-dd" select="myfn:match-dd($dl/dd, $pos-index)"/>
    <xsl:variable
        name="form-texts"
        select="for $td in $matched-dd//td[not(contains-token(@class, 'forma'))]
                return if ($td/span[contains-token(@class, 'potential-form')]) then
                $td/span[contains-token(@class, 'potential-form')]/text()
                else $td/text()"/>
    <xsl:sequence
        select="(for $form in $form-texts return tokenize($form, ',|/')) !
                normalize-space()"/>
  </xsl:function>

  <xsl:function name="myfn:get-alt-forms" as="xs:string*">
    <xsl:param name="dl" as="element(dl)?"/>
    <xsl:sequence select="$dl/dd/a/normalize-space()"/>
  </xsl:function>

  <xsl:function name="myfn:get-zh-forms" as="xs:string*">
    <xsl:param name="dl" as="element(dl)?"/>
    <xsl:sequence select="$dl/dd/span[@lang='zh']/normalize-space()"/>
  </xsl:function>
</xsl:stylesheet>
