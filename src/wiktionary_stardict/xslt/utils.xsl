<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:map="http://www.w3.org/2005/xpath-functions/map"
    xmlns:array="http://www.w3.org/2005/xpath-functions/array"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:function name="myfn:ruby-text" as="xs:string*">
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

  <xsl:function name="myfn:is-template-suffix" as="xs:boolean">
    <xsl:param name="data-mw" as="xs:string"/>
    <xsl:param name="suffixes" as="xs:string*"/>
    <xsl:variable name="json" select="parse-json($data-mw)"/>
    <xsl:sequence
        select="some $wt in $json?parts?*[. instance of map(*)]?template?target?wt
                satisfies (some $suffix in $suffixes satisfies
                ends-with(normalize-space($wt), $suffix))"/>
  </xsl:function>

  <xsl:function name="myfn:get-element-forms" as="xs:string*">
    <xsl:param name="input" as="element()*"/>
    <xsl:for-each select="$input">
      <xsl:choose>
        <xsl:when test="self::a">
          <xsl:sequence select="myfn:a-forms(.)"/>
        </xsl:when>
        <xsl:when test="exists(a) and empty(node() except a)">
          <xsl:sequence select="myfn:adjacent-a-forms(.)"/>
        </xsl:when>
        <xsl:when test="br">
          <xsl:for-each-group select="node()" group-adjacent="boolean(self::br)">
            <xsl:if test="not(current-grouping-key())">
              <xsl:variable name="new-e">
                <span><xsl:copy-of select="current-group()"/></span>
              </xsl:variable>
              <xsl:sequence select="myfn:get-element-forms($new-e/span)"/>
            </xsl:if>
          </xsl:for-each-group>
        </xsl:when>
        <xsl:otherwise>
          <xsl:sequence select="myfn:ruby-text(.)"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:for-each>
  </xsl:function>

  <xsl:function name="myfn:adjacent-a-forms" as="xs:string*">
    <xsl:param name="e" as="element()"/>
    <xsl:choose>
      <xsl:when test="count($e/a) gt 1">
        <xsl:variable name="first-a-str" select="myfn:ruby-text($e/a[1])"/>
        <xsl:variable
            name="prefix"
            select="if (starts-with($first-a-str, '(') and ends-with($first-a-str, ')'))
                    then replace($first-a-str, '^\(|\)$', '') else ''"/>
        <xsl:choose>
          <xsl:when test="$prefix = ''">
            <xsl:sequence select="myfn:combine-a-forms(myfn:a-forms($e/a))"/>
          </xsl:when>
          <xsl:otherwise>
            <xsl:variable
                name="a-forms"
                select="myfn:combine-a-forms(myfn:a-forms($e/a[position() gt 1]))"/>
            <xsl:sequence
                select="$a-forms, for $a-form in $a-forms return $prefix || $a-form"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:when>
      <xsl:otherwise>
        <xsl:sequence select="myfn:a-forms($e/a)"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:function>

  <xsl:function name="myfn:a-forms" as="array(xs:string)*">
    <xsl:param name="a-ele" as="element(a)*"/>
    <xsl:sequence
        select="for $a in $a-ele return
                let $text := myfn:ruby-text($a),
                $title := normalize-space($a/@title)
                return if (string-length($text) = 1 and ends-with($title, $text))
                then array{$title} else array{$text, $title}"/>
  </xsl:function>

  <xsl:function name="myfn:combine-a-forms" as="xs:string*">
    <xsl:param name="a-forms" as="array(xs:string)*"/>
    <xsl:for-each select="1 to 2">
      <xsl:variable name="index" select="."/>
      <xsl:sequence
          select="string-join(for $data in $a-forms return
                  if (array:size($data) ge $index) then $data($index) else $data(1))"/>
    </xsl:for-each>
  </xsl:function>

  <!-- https://www.mediawiki.org/wiki/Language_Converter -->
  <!-- https://www.mediawiki.org/wiki/Specs/HTML#Language_conversion_blocks -->
  <xsl:template
      match="(span|meta|div)[@typeof='mw:LanguageVariant']" mode="lang-converter">
    <xsl:variable name="json-data" select="parse-json(@data-mw-variant)"/>
    <xsl:if test="map:contains($json-data, 'disabled')">
      <xsl:apply-templates
          select="parse-xml-fragment($json-data?disabled?t)" mode="lang-converter"/>
    </xsl:if>
  </xsl:template>
  <xsl:mode name="lang-converter" on-no-match="shallow-copy"/>
</xsl:stylesheet>
