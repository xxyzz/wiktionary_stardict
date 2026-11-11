<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="morphology">
    <section>
      <xsl:apply-templates select="h3[1]" mode="section-heading"/>
      <xsl:apply-templates select="p" mode="clean-content"/>
    </section>
  </xsl:template>

  <xsl:function name="myfn:morphology-forms" as="xs:string*">
    <xsl:param name="section" as="element(section)*"/>
    <xsl:variable
        name="bold-form"
        select="translate(normalize-space(($section/p/b)[1]), '-·', '')"/>
    <xsl:variable
        name="table-forms"
        as="xs:string*">
      <xsl:sequence
          select="for $td in $section/table[contains-token(@class, 'morfotable')]//td
                  return if ($td/a) then ($td/a/text(), $td/a/@title) else $td/text()"/>
    </xsl:variable>
    <xsl:variable
        name="comparative-forms"
        select="$section/p/text()[contains(., 'Сравнительная степень')][1]/
                following-sibling::i/a[text() and not(*)]/myfn:get-element-forms(.)
                [. != 'более']"/>
    <xsl:variable
        name="superlative-forms"
        select="$section/p/text()[contains(., 'Превосходная степень')][1]/
                following-sibling::*[self::i or self::a]/myfn:get-element-forms(.)"/>
    <xsl:sequence
        select="(($bold-form, $table-forms, $comparative-forms, $superlative-forms)
                ! normalize-space())[not(. = ('', '//', '—'))]"/>
  </xsl:function>
</xsl:stylesheet>
