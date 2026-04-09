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
      <h4>Тип и синтаксические свойства сочетания</h4>
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
    <xsl:sequence select="(($bold-form, $table-forms) ! normalize-space())
                          [not(. = ('', '//', '—'))]"/>
  </xsl:function>
</xsl:stylesheet>
