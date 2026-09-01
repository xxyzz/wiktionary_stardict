<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:include href="../utils.xsl"/>
  <xsl:include href="../image.xsl"/>
  <xsl:include href="alt_forms.xsl"/>
  <xsl:include href="pronunciation.xsl"/>
  <xsl:include href="conjugation.xsl"/>
  <xsl:include href="etymology.xsl"/>
  <xsl:include href="../en/linkage.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:param name="language"/>
    <xsl:variable
        name="headword-p"
        select="p[span[contains-token(@class, 'headword-line')]]"/>
    <xsl:variable
        name="headword-strong"
        select="myfn:ruby-text(
                $headword-p//strong[contains-token(@class, 'headword')])"
        as="xs:string*"/>
    <xsl:variable
        name="headword-forms" as="xs:string*"
        select="myfn:get-element-forms($headword-p
                [not(span[@data-mw and myfn:is-template(@data-mw, 'th-noun')])]//b)"/>
    <xsl:variable name="alt-forms" as="xs:string*"
                  select="myfn:get-alt-forms(., $language)"/>
    <xsl:variable name="conj-forms" as="xs:string*">
      <xsl:apply-templates
          select="section[normalize-space((h4|h5|h6)[1]) = ('การผันรูป', 'การผัน',
                  'คำกริยาในรูปต่าง ๆ', 'การผันคำกริยา', 'การผันคำ', 'การกลายรูป', 'การผันคำนาม')]"
          mode="conj">
        <xsl:with-param name="language" select="$language"/>
      </xsl:apply-templates>
    </xsl:variable>
    <xsl:variable
          name="unique-forms"
          select="distinct-values(($headword-strong, $title, $alt-forms,
                  $headword-forms, $conj-forms)
                  [. != ''])"
          as="xs:string*"/>

    <xsl:variable name="definition">
      <section class="mw-parser-output" dir="ltr" lang="th">
        <xsl:apply-templates
            select="h3 | h4 | h5 | h6" mode="section-heading"/>
        <xsl:apply-templates
            select="(ancestor::section | preceding-sibling::section |
                    parent::section/preceding-sibling::section)
                    [some $s-title in ('การออกเสียง', 'การอ่านออกเสียง', 'ออกเสียง')
                    satisfies starts-with(normalize-space((h3|h4|h5|h6)[1]), $s-title)]
                    [last()]"
            mode="pron">
          <xsl:with-param name="language" select="$language"/>
        </xsl:apply-templates>
        <xsl:apply-templates select="p | ol" mode="pos-li"/>
        <xsl:apply-templates
            select="section[normalize-space((h4|h5|h6)[1]) = ('การใช้', 'หมายเหตุการใช้')]"
            mode="usage-notes"/>
        <xsl:apply-templates select="myfn:get-alt-form-section(.)[1]" mode="linkage"/>
        <xsl:apply-templates
            mode="linkage"
            select="myfn:get-linkage-section(.,
                    ('คำพ้องความ', 'คำตรงข้าม', 'คำตรงกันข้าม', 'สุภาษิต', 'สำนวน'))"/>
        <xsl:apply-templates
            select="(ancestor::section | preceding-sibling::section |
                    parent::section/preceding-sibling::section)
                    [starts-with(normalize-space((h3|h4|h5|h6)[1]), 'รากศัพท์')][last()]"
            mode="etymology"/>
      </section>
    </xsl:variable>

    <xsl:variable name="images" as="xs:string*">
      <xsl:sequence select="$definition//img/@src"/>
    </xsl:variable>

    <xsl:variable name="final-definition">
      <xsl:apply-templates select="$definition" mode="convert-img"/>
    </xsl:variable>

    <xsl:variable
        name="form-of-only" as="xs:boolean"
        select="boolean(every $li in ol/li[myfn:is-gloss-li(.)]
                satisfies myfn:is-form-of($li))"/>

    <xsl:sequence
        select="map{'lang': $language,
                'forms': array{$unique-forms},
                'def': serialize($final-definition, map{'method': 'html',
                  'indent': false(), 'escape-uri-attributes': false()}),
                'images': array{$images},
                'form_of_targets': array{if ($form-of-only) then
                  myfn:form-of-targets(ol/li) else ()},
                'form_of_only': $form-of-only,
                'ids': array{myfn:get-pos-section-ids(.)}}"/>
  </xsl:template>

  <xsl:template match="h3 | h4 | h5 | h6" mode="section-heading">
    <h4><xsl:apply-templates mode="clean-content"/></h4>
  </xsl:template>

  <xsl:template match="ol" mode="pos-li">
    <ol><xsl:apply-templates mode="pos-li"/></ol>
  </xsl:template>

  <xsl:template match="li" mode="pos-li">
    <xsl:if test="myfn:is-gloss-li(.)">
      <li><xsl:apply-templates mode="pos-li"/></li>
    </xsl:if>
  </xsl:template>

  <!-- Remove quote examples -->
  <xsl:template match="ul" mode="pos-li"/>

  <!-- Find the shortest usage example -->
  <xsl:template match="dl" mode="pos-li">
    <xsl:variable
        name="examples"
        select="dd[div[contains-token(@class, 'h-usage-example')] or
                span[some $c in ('e-example', 'affixusex', 'mwe-math-element',
                'h-usage-example') satisfies contains-token(@class, $c)] or
                dl[contains-token(@class, 'zhusex')] or
                span[@data-mw and myfn:is-template(@data-mw, ('zh-co', 'zh-x'))] or
                math]"/>
    <xsl:variable
        name="color-panel"
        select="dd[div[contains-token(@class, 'color-panel')]]"/>
    <xsl:variable
        name="nyms"
        select="dd[span[contains-token(@class, 'nyms') and
                (some $c in ('คำพ้องความ', 'คำตรงข้าม', 'รูปแบบอื่น', 'coordinate-term',
                'คำใกล้เคียง', 'คำที่เกี่ยวข้อง') satisfies contains-token(@class, $c))]]"/>
    <xsl:if test="$examples or $color-panel or $nyms">
      <dl>
        <xsl:apply-templates select="$color-panel" mode="clean-content"/>
        <xsl:apply-templates select="$nyms" mode="clean-content"/>
        <xsl:apply-templates
            select="($examples[string-length() = min($examples/string-length())])[1]"
            mode="clean-content"/>
      </dl>
    </xsl:if>
  </xsl:template>

  <xsl:template match="*" mode="pos-li">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>

  <xsl:function name="myfn:is-gloss-li" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean($li/node() and
                not(contains-token($li/@class, 'mw-empty-elt')) and
                not(($li|$li/i)[@data-mw and myfn:is-template(@data-mw, 'rfdef')]))"/>
  </xsl:function>

  <xsl:function name="myfn:is-form-of" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean($li/span[contains-token(@class, 'form-of-definition')])"/>
  </xsl:function>

  <xsl:function name="myfn:form-of-targets" as="xs:string*">
    <xsl:param name="li" as="element(li)*"/>
    <xsl:sequence
        select="distinct-values($li/span[contains-token(@class, 'form-of-definition')]/
                span[contains-token(@class, 'form-of-definition-link')]/i[@lang] !
                normalize-space(.))[. != '']"/>
  </xsl:function>

  <xsl:template match="section" mode="usage-notes">
    <xsl:variable name="content" select="p | ul | dl | table"/>
    <xsl:if test="$content">
      <section>
        <xsl:apply-templates select="h3 | h4 | h5 | h6" mode="section-heading"/>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
