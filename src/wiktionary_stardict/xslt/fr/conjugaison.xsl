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
        select="if (starts-with($title, 'Conjugaison:français/'))
                  then myfn:fr-conj(.)
                else if (starts-with($title, 'Conjugaison:espagnol/'))
                  then myfn:es-conj(.)
                else ()"/>
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
        select="$root//td[a and not(exists(.//span[contains(@class, 'API')]))]/
                myfn:get-element-forms(.)"/>
  </xsl:function>
</xsl:stylesheet>
