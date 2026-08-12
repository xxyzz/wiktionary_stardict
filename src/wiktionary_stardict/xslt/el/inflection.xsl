<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:function name="myfn:get-table-forms" as="xs:string*">
    <xsl:param name="section" as="element(section)"/>
    <xsl:variable
        name="tables" select="$section/table | $section/preceding-sibling::table"/>
    <xsl:variable
        name="tds"
        select="for $table in $tables return
                if ($table/preceding-sibling::*[1][self::span[@data-mw and
                    myfn:is-template-prefix(@data-mw, ('el-', 'grc-'))]])
                then $table//td[@align = 'left']
                else $table//td[not(contains(@style, 'background'))]"/>
    <xsl:sequence
        select="for $td in $tds return
                if ($td/a) then myfn:get-element-forms($td/a)
                else myfn:get-element-forms($td)"/>
  </xsl:function>

  <xsl:function name="myfn:get-inf-section-forms" as="xs:string*">
    <xsl:param name="section" as="element(section)*"/>
    <xsl:sequence
        select="for $form in myfn:get-element-forms(
                $section//td[not(contains(@style, 'background'))])
                return (tokenize($form, '&amp;|-|/| και ') =>
                       myfn:process-form-parenthesis() => myfn:rm-particle()) !
                       normalize-space()"/>
  </xsl:function>

  <xsl:function name="myfn:rm-particle" as="xs:string*">
    <xsl:param name="forms" as="xs:string*"/>
    <xsl:sequence
        select="for $form in $forms return replace($form, '^(θα|να|έχω|είχα|θα έχω|
                να έχω|έχεις|είχες|θα έχεις|να έχεις|έχει|είχε|θα έχει|να έχει|έχουμε|
                είχαμε|θα έχουμε|να έχουμε|έχετε|είχατε|θα έχετε|να έχετε|έχουν|είχαν|
                θα έχουν|να έχουν)\s+', '')"/>
  </xsl:function>

  <xsl:function name="myfn:get-alt-forms" as="xs:string*">
    <xsl:param name="section" as="element(section)*"/>
    <xsl:sequence
        select="$section/ul/li/a[not(span[contains(@style, 'background')]) and
                not(preceding-sibling::*[1][self::span[@data-mw and
                  myfn:is-template(@data-mw, 'ετ')]])] !
                normalize-space()"/>
  </xsl:function>
</xsl:stylesheet>
