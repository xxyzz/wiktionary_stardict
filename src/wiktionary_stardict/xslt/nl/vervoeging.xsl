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
        select="if (.//section[@data-mw and myfn:is-template(@data-mw,
                ('-deadjc-decl', '-deadjc-decl-stellend'))]) then
                myfn:deadjc-decl-forms(.//table[contains-token(@class, 'infoboxlinks')])
                else myfn:common-table-forms(.//table
                [contains-token(@class, 'infoboxlinks')])"
        as="xs:string*"/>
    <xsl:sequence select="array{distinct-values($forms[not(. = ('', '-', '—'))])}"/>
  </xsl:template>

  <xsl:function name="myfn:common-table-forms" as="xs:string*">
    <xsl:param name="tables" as="element(table)*"/>
    <xsl:sequence
        select="for $td in $tables//td[not(contains-token(@class, 'infoboxrijhoofding'))]
                return if ($td/a)
                then myfn:get-element-forms($td/a) else myfn:get-element-forms($td)"/>
  </xsl:function>

  <xsl:function name="myfn:deadjc-decl-forms" as="xs:string*">
    <xsl:param name="tables" as="element(table)*"/>
    <xsl:sequence
        select="myfn:process-form-parenthesis(
                $tables//td[position() mod 2 = 0]/myfn:get-element-forms(.))"/>
  </xsl:function>

  <xsl:function name="myfn:process-form-parenthesis" as="xs:string*">
    <xsl:param name="forms" as="xs:string*"/>
    <xsl:sequence
        select="for $form in $forms return
                if (matches($form, '\(.+\)')) then
                (replace($form, '\(.+\)', ''), replace($form, '[()]', ''))
                else $form"/>
  </xsl:function>
</xsl:stylesheet>
