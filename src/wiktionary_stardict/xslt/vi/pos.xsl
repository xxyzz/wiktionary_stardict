<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:mathml="http://www.w3.org/1998/Math/MathML"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:include href="../image.xsl"/>
  <xsl:include href="alt_forms.xsl"/>
  <xsl:include href="../en/conjugation.xsl"/>
  <xsl:include href="pronunciation.xsl"/>
  <xsl:include href="../en/etymology.xsl"/>
  <xsl:include href="../en/linkage.xsl"/>
  <xsl:include href="../en/form_of.xsl"/>
  <xsl:include href="../en/headword.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:param name="language"/>
    <xsl:if test="ol/li[myfn:is-gloss-li(.)]">
      <xsl:variable
          name="headword-p"
          select="p[span[contains-token(@class, 'headword-line')] or .//b]"/>
      <xsl:variable name="alt-forms" as="xs:string*"
                    select="myfn:get-alt-forms(., $language)"/>
      <xsl:variable name="conj-forms" as="xs:string*">
        <xsl:apply-templates
            select="section[normalize-space((h4 | h5 | h6)[1]) =
                    ('Chia động từ', 'Biến cách')]"
            mode="conj"/>
      </xsl:variable>
      <xsl:variable
          name="unique-forms"
          select="distinct-values((myfn:headword-strong-forms($headword-p), $title,
                  $alt-forms, myfn:headword-b-forms($headword-p), $conj-forms,
                  myfn:li-alt-forms(./ol//li[parent::ol]))
                  [. != ''])"
          as="xs:string*"/>

      <xsl:variable
          name="etymology-section"
          select="(ancestor::section | preceding-sibling::section |
                  parent::section/preceding-sibling::section)
                  [starts-with(normalize-space((h3|h4)[1]), 'Từ nguyên')][last()]"/>

      <xsl:variable name="definition">
        <section class="mw-parser-output" dir="ltr" lang="vi">
          <xsl:apply-templates
              select="(h3 | h4 | h5 | h6)[1]" mode="section-heading"/>
          <xsl:apply-templates
              select="(ancestor::section | preceding-sibling::section |
                      parent::section/preceding-sibling::section)
                      [starts-with(normalize-space((h3|h4)[1]), 'Cách phát âm')]
                      [last()]"
              mode="pron">
            <xsl:with-param name="language" select="$language"/>
          </xsl:apply-templates>
          <xsl:apply-templates select="p | ol" mode="pos-li"/>
          <xsl:apply-templates
              select="section[normalize-space((h4|h5|h6)[1]) =
                      ('Ghi chú sử dụng', 'Chú ý')]"
              mode="etymology"/>
          <xsl:apply-templates select="myfn:get-alt-form-section(.)[1]" mode="linkage"/>
          <xsl:apply-templates
              mode="linkage"
              select="myfn:get-linkage-section(.,
                      ('Đồng nghĩa', 'Từ đồng nghĩa', 'Trái nghĩa'))"/>
          <xsl:apply-templates select="$etymology-section" mode="etymology"/>
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
                  satisfies myfn:vi-is-form-of($li))"/>

      <xsl:variable name="math" select="myfn:get-math-tex(.)"/>

      <xsl:sequence
          select="map{'lang': $language,
                  'forms': array{$unique-forms},
                  'def': if (exists($math)) then serialize($final-definition) else
                    serialize($final-definition, map{'method': 'html',
                    'indent': false(), 'escape-uri-attributes': false()}),
                  'images': array{$images},
                  'form_of_targets': array{if ($form-of-only) then
                    myfn:vi-form-of-targets(ol/li) else ()},
                  'form_of_only': $form-of-only,
                  'ids': array{distinct-values((myfn:get-pos-section-ids(.),
                    myfn:get-section-ids($etymology-section)))},
                  'math': array{$math},
                  'links': array{myfn:get-links($final-definition)}}"/>
    </xsl:if>
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
        select="dd[mathml:math or math or
                div[contains-token(@class, 'h-usage-example')] or
                span[some $c in ('e-example', 'affixusex', 'mwe-math-element',
                'h-usage-example') satisfies contains-token(@class, $c)] or
                dl[contains-token(@class, 'zhusex')] or
                span[@data-mw and myfn:is-template(@data-mw, ('zh-co', 'zh-x'))]]"/>
    <xsl:variable
        name="color-panel"
        select="dd[div[contains-token(@class, 'color-panel')]]"/>
    <xsl:variable
        name="nyms"
        select="dd[span[contains-token(@class, 'nyms') and
                (some $c in ('đồng-nghĩa', 'trái-nghĩa', 'Dạng-thay-thế',
                'từ-cùng-trường-nghĩa', 'Gần-đồng-nghĩa')
                satisfies contains-token(@class, $c))]]"/>
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

  <xsl:function name="myfn:vi-is-form-of" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean(myfn:is-form-of($li) or
                $li/span[@data-mw and myfn:is-template-suffix(@data-mw, ' of')])"/>
  </xsl:function>

  <xsl:function name="myfn:vi-form-of-targets" as="xs:string*">
    <xsl:param name="li" as="element(li)*"/>
    <xsl:sequence
        select="distinct-values(
                let $targets := myfn:form-of-targets($li) return
                if (exists($targets)) then $targets else
                $li/span[contains-token(@class, 'use-with-mention')]/span
                [contains-token(@class, 'mention')] ! normalize-space(.))[. != '']"/>
  </xsl:function>

  <xsl:function name="myfn:li-alt-forms" as="xs:string*">
    <xsl:param name="li" as="element(li)*"/>
    <xsl:sequence
        select="$li/dl/dd/span[contains-token(@class, 'nyms') and
                contains-token(@class, 'Dạng-thay-thế')]/
                span[@lang and not(contains-token(@class, 'tr'))]/normalize-space()"/>
  </xsl:function>
</xsl:stylesheet>
