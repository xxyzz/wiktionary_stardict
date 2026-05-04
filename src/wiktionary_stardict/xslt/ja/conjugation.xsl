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
      <xsl:when test="$language = ('日本語', '古典日本語')">
        <xsl:variable name="auxiliary-verb-forms" as="xs:string*">
          <xsl:sequence
              select="myfn:ja-aux-verb-forms(table[@data-mw and myfn:is-template(
                      @data-mw, ('日本語助動詞活用', '古典日本語助動詞活用'))])"/>
        </xsl:variable>
        <xsl:variable name="classical-forms" as="xs:string*">
          <xsl:sequence
              select="myfn:ja-classical-conj-forms(table[@data-mw and myfn:is-template(
                      @data-mw, ('古典日本語ク活用', '古典日本語シク活用', '古典日本語ナリ活用',
                      '古典日本語タリ活用'))])"/>
        </xsl:variable>
        <xsl:variable name="combine-forms" as="xs:string*">
          <xsl:sequence
              select="myfn:ja-combine-forms(div[@data-mw and myfn:is-template(
                      @data-mw, ('日本語形容動詞活用', '日本語五段活用', '日本語五段活用/表示',
                      '日本語上一段活用', '日本語上一段活用2', '日本語下一段活用',
                      '日本語形容詞活用', '日本語形容詞活用/表示', '日本語形容詞活用2',
                      '日本語タルト活用', '日本語ダ活用', '日本語サ変活用', '日本語一段活用',
                      '日本語カ変活用', '日本語サ変活用', '日本語ザ変活用', '日本語変格活用',
                      '古典日本語四段活用', '古典日本語上一段活用', '古典日本語上二段活用',
                      '古典日本語下一段活用', '古典日本語下二段活用', '古典日本語変格活用',
                      '可能動詞下一段活用'))])"/>
        </xsl:variable>
        <xsl:sequence
            select="distinct-values(
                    ($auxiliary-verb-forms, $classical-forms, $combine-forms))
                    [. != '']"/>
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

  <!-- テンプレート:日本語助動詞活用 -->
  <xsl:function name="myfn:ja-aux-verb-forms" as="xs:string*">
    <xsl:param name="table" as="element(table)*"/>
    <xsl:sequence select="$table//td[position() le 6]/text()/normalize-space()"/>
  </xsl:function>

  <xsl:function name="myfn:ja-classical-conj-forms" as="xs:string*">
    <xsl:param name="table" as="element(table)*"/>
    <xsl:variable name="stem" as="xs:string"
                  select="normalize-space($table//td[@rowspan and position() = 2])"/>
    <xsl:sequence
        select="for $td in $table//td[not(@rowspan)] return
                let $td-text := normalize-space($td) => replace('[\(\)\-○]', '') return
                if ($td-text) then $stem || $td-text else ()"/>
  </xsl:function>

  <xsl:function name="myfn:ja-combine-forms" as="xs:string*">
    <xsl:param name="div" as="element(div)*"/>
    <xsl:variable name="first" as="xs:string*"
                  select="myfn:first-ja-combine-table($div//table[1])"/>
    <xsl:variable
        name="second" as="xs:string*"
        select="$div//table[2]//td[position() mod 2 = 0]/text() ! normalize-space()"/>
    <xsl:sequence select="$first, $second"/>
  </xsl:function>

  <xsl:function name="myfn:first-ja-combine-table" as="xs:string*">
    <xsl:param name="table" as="element(table)*"/>
    <xsl:variable name="stem" as="xs:string"
                  select="normalize-space($table//td[position() = 1])"/>
    <xsl:sequence
        select="for $td in $table//td[position() gt 1]/text() return
                let $td-text := normalize-space($td) => replace('[\(\)]', '') return
                if (not($td-text = ('', '無し'))) then $stem || $td-text else ()"/>
  </xsl:function>
</xsl:stylesheet>
