<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="conj" as="xs:string*">
    <xsl:sequence
        select="distinct-values((for $tbody in .//tbody return
                if ($tbody//td/span[contains-token(@class, 'form-of')]) then
                $tbody//td/span[contains-token(@class, 'form-of')] else
                $tbody//td/(span[@lang and not(ends-with(@lang, '-Latn'))] |
                            a[parent::td/child::*[1][self::a]])) !
                myfn:get-element-forms(.))[. != '']"/>
  </xsl:template>

  <xsl:function name="myfn:get-element-forms" as="xs:string*">
    <xsl:param name="ele" as="element()*"/>
    <xsl:sequence
        select="for $n in $ele return
                if ($n/a) then myfn:a-forms($n/a) else myfn:a-forms($n)"/>
  </xsl:function>

  <xsl:function name="myfn:a-forms" as="xs:string*">
    <xsl:param name="a-ele" as="element()*"/>
    <xsl:sequence
        select="for $a in $a-ele return
                let $text := myfn:ruby_text($a),
                    $title := normalize-space($a/@title)
                return if (string-length($text) = 1 and ends-with($title, $text))
                then $title else ($text, $title)"/>
  </xsl:function>
</xsl:stylesheet>
