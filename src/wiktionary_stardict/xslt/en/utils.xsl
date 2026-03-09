<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:function name="myfn:ruby_text" as="xs:string">
    <xsl:param name="node" as="node()"/>
    <xsl:sequence select="normalize-space(string-join($node//text()[not(parent::rp or ancestor::rt)], ''))"/>
  </xsl:function>

  <xsl:function name="myfn:is-template" as="xs:boolean">
    <xsl:param name="data-mw" as="xs:string"/>
    <xsl:param name="template" as="xs:string"/>
    <xsl:variable name="json" select="parse-json($data-mw)"/>
    <xsl:sequence
	select="some $wt in $json?parts?*?template?target?wt
		satisfies normalize-space($wt) = $template"/>
  </xsl:function>
</xsl:stylesheet>
