<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz">

  <xsl:function name="myfn:get-alt-forms" as="xs:string*">
    <xsl:param name="section" as="element(section)"/>
    <xsl:variable
        name="alt-forms-section"
        select="($section/preceding-sibling::section |
                $section/parent::section/preceding-sibling::section |
                $section/section)[normalize-space(h3|h4|h5|h6) = ('異表記・別形',
                '別表記', '代替表記', '異形', '表記揺れ')]"/>
    <xsl:sequence
        select="myfn:get-element-forms($alt-forms-section/ul/li/span
                [@lang and not(ends-with(@lang, '-Latn'))])"/>
  </xsl:function>
</xsl:stylesheet>
