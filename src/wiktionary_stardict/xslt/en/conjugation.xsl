<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="conj" as="xs:string*">
    <xsl:variable name="forms" as="xs:string*">
      <xsl:apply-templates mode="conj-template"/>
    </xsl:variable>
    <xsl:choose>
      <xsl:when test="exists($forms)">
        <xsl:sequence select="$forms"/>
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

  <xsl:mode name="conj-template" on-no-match="shallow-skip"/>
  <xsl:template
      match="*[@data-mw and myfn:is-template-prefix(@data-mw, 'ja-')]"
      as="xs:string*" mode="conj-template">
    <!-- vi edition "ja-go-u" template has "ja-Jpan" value -->
    <xsl:variable name="spans" select=".//tbody//td/span[@lang = ('ja', 'ja-Jpan')]"/>
    <xsl:sequence
        select="distinct-values(for $span in $spans return
                if ($span/a) then myfn:get-element-forms($span)
                else myfn:process-form-parenthesis($span/text()/tokenize(., '、') !
                normalize-space()))[. != '']"/>
  </xsl:template>

  <xsl:template
      match="*[@data-mw and myfn:is-template-prefix(@data-mw, 'ko-conj')]"
      as="xs:string*" mode="conj-template">
    <xsl:sequence
        select="distinct-values(
                myfn:get-element-forms(.//tbody//td//span[@lang = 'ko'])
                ! tokenize(., ',') ! normalize-space(.))[. != '']"/>
  </xsl:template>

  <xsl:template
      match="*[@data-mw and myfn:is-template-prefix(@data-mw, 'de-conj')]"
      as="xs:string*" mode="conj-template">
    <xsl:sequence
        select="distinct-values(myfn:get-element-forms(.//tbody//td/span
                [contains-token(@class, 'form-of') and @lang = 'de']))[. != '']"/>
  </xsl:template>
</xsl:stylesheet>
