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

  <xsl:variable
      name="title" select="html/head/title/text()" as="xs:string"/>

  <xsl:template match="/">
    <xsl:variable
        name="forms" as="xs:string*"
        select="if (starts-with($title, 'Conjugaison:français/')) then
                  myfn:fr-conj(.)
                else if (some $prefix in ('Conjugaison:japonais/',
                'Annexe:Déclinaison en allemand/', 'Conjugaison:portugais/') satisfies
                starts-with($title, $prefix)) then
                  myfn:ja-conj(.)
                else if (starts-with($title, 'Conjugaison:coréen/')) then
                  myfn:ko-conj(.)
                else if (starts-with($title, 'Conjugaison:tchèque/')) then
                  myfn:cs-conj(.)
                else myfn:es-conj(.)"/>
    <xsl:sequence select="array{distinct-values($forms[. != ''])}"/>
  </xsl:template>

  <xsl:function name="myfn:fr-conj" as="xs:string*">
    <xsl:param name="root"/>
    <xsl:sequence
        select="$root//td[@align='left' and not(contains-token(@class, 'API'))]/
                myfn:get-element-forms(.)"/>
  </xsl:function>

  <xsl:function name="myfn:es-conj" as="xs:string*">
    <xsl:param name="root"/>
    <xsl:sequence
        select="$root//td[(a or b) and not(exists(.//span[contains(@class, 'API')]))]/
                myfn:get-element-forms(if (b) then b else .)"/>
  </xsl:function>

  <xsl:function name="myfn:ja-conj" as="xs:string*">
    <xsl:param name="root"/>
    <xsl:sequence
        select="myfn:process-form-parenthesis(myfn:get-element-forms($root//td//bdi))"/>
  </xsl:function>

  <xsl:function name="myfn:ko-conj" as="xs:string*">
    <xsl:param name="root"/>
    <xsl:sequence
        select="$root//section/table[contains-token(@class, 'wikitable')]//td//bdi/
                myfn:get-element-forms(.)"/>
  </xsl:function>

  <!-- https://fr.wiktionary.org/wiki/Modèle:cs-conj-i -->
  <xsl:function name="myfn:cs-conj" as="xs:string*">
    <xsl:param name="root"/>
    <xsl:apply-templates select="$root//td" mode="cs-conj-td"/>
  </xsl:function>

  <xsl:template match="td" mode="cs-conj-td" as="xs:string*">
    <xsl:variable name="is-futur" select="position() mod 5 = 3"/>
    <xsl:for-each-group select="node()" group-adjacent="boolean(self::br)">
      <xsl:if test="not(current-grouping-key())">
        <xsl:sequence
            select="myfn:get-element-forms(current-group()[self::bdi]
                    [if ($is-futur) then last() else 1])"/>
      </xsl:if>
    </xsl:for-each-group>
  </xsl:template>
</xsl:stylesheet>
