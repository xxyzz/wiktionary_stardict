<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:function name="myfn:conj-forms" as="xs:string*">
    <xsl:param name="node" as="node()"/>
    <xsl:for-each select="$node//td">
      <xsl:sequence select="myfn:conj-td-forms(.)"/>
    </xsl:for-each>
  </xsl:function>

  <xsl:function name="myfn:conj-td-forms" as="xs:string*">
    <xsl:param name="td" as="element(td)"/>
    <xsl:for-each-group
        select="$td/a"
        group-adjacent="if (normalize-space(preceding-sibling::text()) = ',') then
                        'after-comma' else 'before-comma'">
      <xsl:sequence select="normalize-space(current-group()[last()])"/>
    </xsl:for-each-group>
  </xsl:function>
</xsl:stylesheet>
