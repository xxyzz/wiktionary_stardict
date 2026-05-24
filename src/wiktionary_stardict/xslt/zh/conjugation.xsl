<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="conj" as="xs:string*">
    <xsl:param name="language" as="xs:string"/>
    <xsl:choose>
      <xsl:when test="$language = '日語'">
        <xsl:variable name="spans"
                      select=".//tbody//td/span[starts-with(@lang, 'ja') and
                              not(ends-with(@lang, '-Latn'))]"/>
        <xsl:sequence
            select="distinct-values(for $span in $spans return
                    if ($span/a) then myfn:get-element-forms($span)
                    else $span/text()/normalize-space())[. != '']"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:sequence
            select="distinct-values((for $tbody in .//tbody return
                    if ($tbody//td/span[contains-token(@class, 'form-of')]) then
                    $tbody//td/span[contains-token(@class, 'form-of')] else
                    $tbody//td/(span[@lang and not(ends-with(@lang, '-Latn'))] |
                                a[parent::td/child::*[1][self::a]])) !
                    myfn:get-element-forms(.))[. != '']"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
</xsl:stylesheet>
