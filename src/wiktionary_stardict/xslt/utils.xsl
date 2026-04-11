<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:function name="myfn:ruby_text" as="xs:string*">
    <xsl:param name="nodes" as="node()*"/>
    <xsl:for-each select="$nodes">
      <xsl:sequence
          select=".//text()[not(parent::rp or ancestor::rt)] =>
                  string-join('') => replace('⫽', '') => normalize-space()"/>
    </xsl:for-each>
  </xsl:function>

  <xsl:function name="myfn:is-template" as="xs:boolean">
    <xsl:param name="data-mw" as="xs:string"/>
    <xsl:param name="templates" as="xs:string*"/>
    <xsl:variable name="json" select="parse-json($data-mw)"/>
    <xsl:sequence
        select="some $wt in $json?parts?*[. instance of map(*)]?template?target?wt
                satisfies normalize-space($wt) = $templates"/>
  </xsl:function>

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
