<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:fn="http://www.w3.org/2005/xpath-functions"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <!-- https://pl.wiktionary.org/wiki/Wikisłownik:Zasady_tworzenia_haseł#Numeracja_w_polach_innych_niż_znaczenia -->
  <xsl:function name="myfn:match-dd" as="element(dd)*">
    <xsl:param name="dd-nodes" as="element(dd)*"/>
    <xsl:param name="pos-index" as="xs:integer"/>
    <xsl:sequence
        select="for $dd in $dd-nodes
                return let $dd-index := $dd/(text()/
                  analyze-string(., '\(([\d\s,.-]+)\)')//fn:group)[1]
                return if ($dd[node()] and
                  (($dd-index and myfn:match-pos-index($dd-index, $pos-index))
                  or not($dd-index))) then $dd else ()"/>
  </xsl:function>

  <xsl:function name="myfn:match-pos-index" as="xs:boolean">
    <xsl:param name="dd-index-range" as="xs:string?"/>
    <xsl:param name="pos-index" as="xs:integer"/>
    <xsl:sequence
        select="boolean(
                let $index-list := tokenize($dd-index-range, ',') return
                if (contains($index-list[1], '.') and (every $index in tail($index-list)
                satisfies matches(normalize-space($index), '^\d+$'))) then
                  normalize-space(substring-before($index-list[1], '.')) =
                  string($pos-index)
                else (some $dd-index in $index-list satisfies
                  let $index-parts := tokenize($dd-index, '-') return
                    if (contains($index-parts[1], '.')) then
                      normalize-space(substring-before($index-parts[1], '.')) =
                      string($pos-index)
                    else if (count($index-parts) = 2) then
                      number($index-parts[1]) le $pos-index and
                      $pos-index le number($index-parts[2])
                    else normalize-space($index-parts[1]) = string($pos-index)))"/>
  </xsl:function>
</xsl:stylesheet>
