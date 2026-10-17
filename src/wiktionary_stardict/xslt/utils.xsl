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
      <xsl:choose>
        <xsl:when test="self::ruby or .//ruby">
          <xsl:variable
              name="kanji-form"
              select=".//text()[not(ancestor::rp or ancestor::rt)] =>
                      string-join() => normalize-space()"/>
          <xsl:variable
              name="kana-form"
              select=".//text()[ancestor::rt or not(ancestor::ruby)] =>
                      string-join() => normalize-space()"/>
          <xsl:sequence select="$kanji-form, $kana-form"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:sequence select="replace(normalize-space(.), '·', '')"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:for-each>
  </xsl:function>

  <xsl:function name="myfn:convert-template-name" as="xs:string">
    <xsl:param name="name" as="xs:string"/>
    <xsl:sequence select="replace(normalize-space($name), '_', ' ')"/>
  </xsl:function>

  <xsl:function name="myfn:is-template" as="xs:boolean">
    <xsl:param name="inputs" as="xs:string*"/>
    <xsl:param name="templates" as="xs:string*"/>
    <xsl:sequence
        select="some $json in $inputs ! parse-json(.) satisfies
                some $wt in $json?parts?*[. instance of map(*)]?template?target?wt
                satisfies myfn:convert-template-name($wt) = $templates"/>
  </xsl:function>

  <xsl:function name="myfn:is-template-suffix" as="xs:boolean">
    <xsl:param name="inputs" as="xs:string*"/>
    <xsl:param name="suffixes" as="xs:string*"/>
    <xsl:sequence
        select="some $json in $inputs ! parse-json(.) satisfies
                some $wt in $json?parts?*[. instance of map(*)]?template?target?wt
                satisfies (some $suffix in $suffixes satisfies
                ends-with(myfn:convert-template-name($wt), $suffix))"/>
  </xsl:function>

  <xsl:function name="myfn:is-template-prefix" as="xs:boolean">
    <xsl:param name="inputs" as="xs:string*"/>
    <xsl:param name="prefixes" as="xs:string*"/>
    <xsl:sequence
        select="some $json in $inputs ! parse-json(.) satisfies
                some $wt in $json?parts?*[. instance of map(*)]?template?target?wt
                satisfies (some $prefix in $prefixes satisfies
                starts-with(myfn:convert-template-name($wt), $prefix))"/>
  </xsl:function>

  <xsl:function name="myfn:get-template-arg" as="xs:string?">
    <xsl:param name="inputs" as="xs:string*"/>
    <xsl:param name="t-name" as="xs:string+"/>
    <xsl:param name="arg-name" as="xs:string"/>
    <xsl:sequence
        select="(for $json in $inputs ! parse-json(.) return
                $json?parts?*[. instance of map(*)]?template
                [myfn:convert-template-name(?target?wt) = $t-name][1]
                ?params?($arg-name)?wt)[1]"/>
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
        <xsl:when test="exists(a) and exists(span[normalize-space(.) = '/'])">
          <xsl:sequence select="myfn:a-forms(a)"/>
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
        <xsl:variable name="first-a-str" select="myfn:ruby-text($e/a[1])[1]"/>
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
                select="myfn:combine-a-forms(myfn:a-forms(tail($e/a)))"/>
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
                  let $title := normalize-space($a/@title),
                      $texts := myfn:ruby-text($a)
                  return if ($title = '' or count($texts) gt 1) then array{$texts}
                  else if ($title = $texts or (string-length($texts) = 1 and
                    ends-with($title, $texts)))
                  then array{$title} else array{$texts, $title}"/>
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
      match="(span|meta|div)[contains-token(@typeof, 'mw:LanguageVariant')]"
      mode="lang-converter">
    <xsl:variable name="json-data" select="parse-json(@data-mw-variant)"/>
    <xsl:if test="map:contains($json-data, 'disabled')">
      <xsl:apply-templates
          select="parse-xml-fragment($json-data?disabled?t)" mode="lang-converter"/>
    </xsl:if>
  </xsl:template>
  <xsl:mode name="lang-converter" on-no-match="shallow-copy"/>

  <xsl:function name="myfn:get-pos-section-ids" as="xs:string*">
    <xsl:param name="section" as="element(section)"/>
    <xsl:sequence
        select="distinct-values((myfn:get-section-ids($section/ancestor::section),
                $section//*/@id[myfn:is-valid-id(.)]))"/>
  </xsl:function>

  <xsl:function name="myfn:get-section-ids" as="xs:string*">
    <xsl:param name="sections" as="element(section)*"/>
    <xsl:sequence
        select="distinct-values(for $section in $sections return
                $section/*[not(self::section)]/descendant-or-self::*/
                @id[myfn:is-valid-id(.)])"/>
  </xsl:function>

  <xsl:function name="myfn:is-valid-id" as="xs:boolean">
    <xsl:param name="id" as="xs:string"/>
    <xsl:sequence
        select="not(some $prefix in ('mw', 'cite_ref') satisfies
                starts-with($id, $prefix))"/>
  </xsl:function>

  <xsl:function name="myfn:process-form-parenthesis" as="xs:string*">
    <xsl:param name="forms" as="xs:string*"/>
    <xsl:sequence
        select="for $form in $forms return
                if (matches($form, '\(.+?\)|（.+?）')) then
                (replace($form, '\(.+?\)|（.+?）', ''), replace($form, '[()（）]', ''))
                else $form"/>
  </xsl:function>

  <xsl:function name="myfn:is-bword-link" as="xs:boolean">
    <xsl:param name="a" as="element(a)?"/>
    <xsl:sequence
        select="boolean(contains-token($a/@rel, 'mw:WikiLink') and
                not(some $class in ('new', 'mw-selflink-fragment', 'mw-selflink')
                satisfies contains-token($a/@class, $class)) and
                starts-with($a/@href, './') and not(contains($a/@title, ':')))"/>
  </xsl:function>

  <xsl:function name="myfn:get-form-of-texts" as="xs:string*">
    <xsl:param name="elements" as="element()*"/>
    <xsl:sequence
        select="for $e in $elements return
                if ($e instance of element(a)) then myfn:get-a-element-target($e) else
                if (count($e/*) = 1 and myfn:is-bword-link($e/a))
                then myfn:get-a-element-target($e/a) else normalize-space($e)"/>
  </xsl:function>

  <xsl:function name="myfn:get-a-element-target" as="xs:string*">
    <xsl:param name="a" as="element(a)"/>
    <xsl:sequence
        select="let $href := substring-after($a/@href, './') return
                if (contains($href, '#')) then $href else replace($href, '_', ' ')"/>
  </xsl:function>

  <xsl:function name="myfn:get-links" as="xs:string*">
    <xsl:param name="section"/>
    <xsl:sequence
        select="distinct-values($section//a/@href/substring-after(., 'bword://'))"/>
  </xsl:function>
</xsl:stylesheet>
