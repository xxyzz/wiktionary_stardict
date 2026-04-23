<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz">

  <xsl:function name="myfn:get-alt-forms" as="xs:string*">
    <xsl:param name="section" as="element(section)"/>
    <xsl:param name="language" as="xs:string"/>
    <xsl:variable
        name="alt-forms-section"
        select="($section/preceding-sibling::section |
                $section/parent::section/preceding-sibling::section |
                $section/section)[normalize-space(h3|h4|h5|h6) = 'Alternative forms']"/>
    <xsl:variable
        name="alt-forms"
        select="myfn:alt-forms-section($alt-forms-section)"/>
    <xsl:choose>
      <xsl:when test="$language = 'Chinese'">
        <xsl:sequence
            select="$alt-forms, $section/ancestor::section[h2|h3] ! myfn:zh-forms(.)"/>
      </xsl:when>
      <xsl:when test="$language = 'Japanese'">
        <xsl:variable
            name="above-sections"
            select="$section/ancestor::section[h2 | h3] |
                    $section/preceding-sibling::section[h3 | h4]"/>
        <xsl:sequence select="$alt-forms, $above-sections ! myfn:ja-kanjitab(.)"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:copy-of select="$alt-forms"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:function>

  <xsl:function name="myfn:alt-forms-section" as="xs:string*">
    <xsl:param name="section" as="element(section)*"/>
    <xsl:sequence
        select="myfn:get-element-forms($section/ul/li/span
                [@lang and not(ends-with(@lang, '-Latn'))])"/>
  </xsl:function>

  <xsl:function name="myfn:zh-forms" as="xs:string*">
    <xsl:param name="section" as="element(section)"/>
    <xsl:variable
        name="span_node"
        select="$section/span[@data-mw and myfn:is-template(@data-mw, 'zh-forms')]"/>
    <xsl:if test="$span_node">
      <xsl:variable name="table" select="$span_node/following-sibling::table"/>
      <xsl:variable
          name="th-forms"
          select="$table//th//span[starts-with(@lang, 'zh-Han')]/a/text()"/>
      <xsl:variable
          name="td-forms"
          select="$table//td[preceding-sibling::th[1][text() != 'anagram']]//
                  span[starts-with(@lang, 'zh-Han')]//text()"/>
      <xsl:sequence select="$th-forms, $td-forms"/>
    </xsl:if>
  </xsl:function>

  <xsl:function name="myfn:ja-kanjitab" as="xs:string*">
    <xsl:param name="section" as="element(section)"/>
    <xsl:sequence
        select="$section/table[.//th[starts-with(text(), 'Alternative spelling')]]//
                td/span[@lang = 'ja']//text()"/>
  </xsl:function>
</xsl:stylesheet>
