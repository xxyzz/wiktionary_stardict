<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:function name="myfn:is-form-of" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:variable
        name="form-of-span"
        select="$li/*[not(self::ol or self::ul or self::dl)]/
                descendant-or-self::span[contains-token(@class, 'form-of-definition')]"/>
    <xsl:variable
        name="target-span"
        select="$form-of-span/span[contains-token(@class, 'form-of-definition-link')]"/>
    <xsl:variable
        name="has-gloss"
        select="exists(($target-span|$li)/span[contains-token(@class, 'mention-gloss')])
                or (myfn:is-template($li/span/@data-mw, ('tcl', 'transclude')) and
                not(exists(myfn:get-template-arg(
                  $li/span/@data-mw, ('tcl', 'transclude'), 'nogloss')))) or
                exists($li/node()[self::a or
                  self::text()[not(normalize-space(.) = ('', '.', '。', ',', '，'))]])"/>
    <xsl:variable
        name="has-contraction-plus"
        select="exists($target-span/following-sibling::node()[1]
                [self::text() and normalize-space(.) = '+'])"/>
    <xsl:sequence
        select="boolean(exists($form-of-span) and exists($target-span) and
                not($has-gloss) and not($has-contraction-plus))"/>
  </xsl:function>

  <xsl:function name="myfn:form-of-targets" as="xs:string*">
    <xsl:param name="li" as="element(li)*"/>
    <xsl:sequence
        select="distinct-values(myfn:get-form-of-texts(
                $li/*[not(self::ol or self::ul or self::dl)]/
                descendant-or-self::span[contains-token(@class, 'form-of-definition')]/
                span[contains-token(@class, 'form-of-definition-link')]/i[@lang]))
                [. != '']"/>
  </xsl:function>
</xsl:stylesheet>
