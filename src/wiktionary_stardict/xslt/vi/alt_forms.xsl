<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz">

  <xsl:import href="../en/alt_forms.xsl"/>

  <xsl:function name="myfn:get-alt-form-section" as="element(section)*">
    <xsl:param name="section" as="element(section)"/>
    <xsl:sequence
        select="($section/preceding-sibling::section |
                $section/parent::section/preceding-sibling::section |
                $section/section)
                [normalize-space((h3|h4|h5|h6)[1]) = 'Cách viết khác']"/>
  </xsl:function>

  <xsl:function name="myfn:get-alt-forms" as="xs:string*">
    <xsl:param name="section" as="element(section)"/>
    <xsl:param name="language" as="xs:string"/>
    <xsl:variable
        name="alt-forms-section" select="myfn:get-alt-form-section($section)"/>
    <xsl:variable
        name="alt-forms"
        select="myfn:alt-forms-section($alt-forms-section)"/>
    <xsl:choose>
      <xsl:when test="$language = 'Tiếng Trung Quốc'">
        <xsl:sequence
            select="$alt-forms,
                    $section/ancestor::section[h2|h3] ! myfn:zh-forms(., 'anagram')"/>
      </xsl:when>
      <xsl:when test="$language = 'Tiếng Nhật'">
        <xsl:variable
            name="above-sections"
            select="$section/ancestor::section[h2 | h3] |
                    $section/preceding-sibling::section[h3 | h4]"/>
        <xsl:sequence select="$alt-forms, $above-sections ! myfn:ja-kanjitab(.)"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:sequence select="$alt-forms"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:function>

  <xsl:function name="myfn:alt-forms-section" as="xs:string*">
    <xsl:param name="section" as="element(section)*"/>
    <xsl:sequence
        select="myfn:get-element-forms($section/ul/li/(
                if (span[@lang and not(ends-with(@lang, '-Latn'))]) then
                  span[@lang and not(ends-with(@lang, '-Latn'))]
                else a))"/>
  </xsl:function>

  <xsl:function name="myfn:ja-kanjitab" as="xs:string*">
    <xsl:param name="section" as="element(section)"/>
    <xsl:sequence
        select="$section/table[.//th[starts-with(
                normalize-space(), 'Cách viết khác')]]//
                td/span[@lang = 'ja'] ! normalize-space(.)"/>
  </xsl:function>
</xsl:stylesheet>
