<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:include href="../image.xsl"/>
  <xsl:include href="morphology.xsl"/>
  <xsl:include href="pronunciation.xsl"/>
  <xsl:include href="etymology.xsl"/>
  <xsl:include href="linkage.xsl"/>

  <xsl:template match="section" mode="gloss">
    <xsl:param name="language"/>

    <xsl:variable
        name="meaning-section"
        select="section[normalize-space(h4[1]) = ('Значение', 'Значения',
                'Как самостоятельный глагол',
                'В значении вспомогательного глагола или связки') and ol]"/>

    <xsl:if test="$meaning-section/*">
      <xsl:variable
        name="morphology-section"
        select="preceding-sibling::section[normalize-space(h3[1]) =
                ('Морфологические и синтаксические свойства',
                'Тип и синтаксические свойства сочетания',
                'Тип и свойства сочетания')]"/>

      <xsl:variable name="definition">
        <section class="mw-parser-output" dir="ltr" lang="ru">
          <xsl:apply-templates select="$morphology-section" mode="morphology"/>
          <xsl:apply-templates
              select="preceding-sibling::section
                      [normalize-space(h3[1]) = 'Произношение']"
              mode="pronunciation"/>
          <xsl:apply-templates select="$meaning-section" mode="meaning"/>
          <xsl:apply-templates
              select="section[normalize-space((h4|h5|h6)[1]) = $linkage-titles]"
              mode="linkage"/>
          <xsl:apply-templates
              select="$meaning-section/h4[normalize-space(.) = $linkage-titles]"
              mode="linkage-from-gloss"/>
          <xsl:apply-templates
              select="following-sibling::section[normalize-space(h3[1]) = 'Этимология']"
              mode="etymology"/>
        </section>
      </xsl:variable>

      <xsl:variable
          name="unique-forms"
          select="distinct-values(($title, myfn:morphology-forms($morphology-section)))
                  [. != '']"
          as="xs:string*"/>

      <xsl:variable name="images" as="xs:string*">
        <xsl:sequence select="$definition//img/@src"/>
      </xsl:variable>

      <xsl:variable name="final-definition">
        <xsl:apply-templates select="$definition" mode="convert-img"/>
      </xsl:variable>

      <xsl:variable
          name="form-of-only" as="xs:boolean"
          select="boolean(every $li in $meaning-section/ol/li[myfn:is-gloss-li(.)]
                  satisfies myfn:is-form-of($li))"/>
      <xsl:variable name="form-of-targets" as="xs:string*">
        <xsl:choose>
          <xsl:when test="$form-of-only">
            <xsl:apply-templates
                select="$meaning-section/ol/li" mode="form-of-targets"/>
          </xsl:when>
          <xsl:otherwise><xsl:sequence select="()"/></xsl:otherwise>
        </xsl:choose>
      </xsl:variable>

      <xsl:sequence
          select="map{'lang': $language,
                  'forms': array{$unique-forms},
                  'def': serialize($final-definition),
                  'images': array{$images},
                  'ids': array{myfn:get-pos-section-ids(.)},
                  'svg': array{myfn:get-svg-data($final-definition)},
                  'links': array{myfn:get-links($final-definition)},
                  'form_of_targets': array{distinct-values($form-of-targets)[. != '']},
                  'form_of_only': $form-of-only}"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="section" mode="meaning">
    <xsl:apply-templates select="h4[1]" mode="section-heading"/>
    <xsl:apply-templates select="p | ol" mode="gloss-li"/>
  </xsl:template>

  <xsl:template match="ol" mode="gloss-li">
    <ol><xsl:apply-templates mode="gloss-li"/></ol>
  </xsl:template>

  <xsl:template match="li" mode="gloss-li">
    <xsl:if test="myfn:is-gloss-li(.)">
      <xsl:variable
          name="examples"
          select="span[contains-token(@class, 'example-fullblock') and
                  span[contains-token(@class, 'example-block') and
                  not(span[contains-token(@class, 'example-absent')])]]"/>
      <li>
        <xsl:apply-templates
            select="node()[not(self::span[contains-token(@class, 'example-fullblock')]
                    or self::ol)]"
            mode="clean-content"/>
        <xsl:apply-templates
            select="($examples[string-length() = min($examples/string-length())])[1]"
            mode="clean-content"/>
        <xsl:apply-templates select="ol" mode="gloss-li"/>
      </li>
    </xsl:if>
  </xsl:template>

  <xsl:template match="*" mode="gloss-li">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>

  <xsl:template match="h3 | h4 | h5 | h6" mode="section-heading">
    <h4><xsl:apply-templates mode="clean-content"/></h4>
  </xsl:template>

  <xsl:function name="myfn:is-gloss-li" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean($li/node() and
                not(contains-token($li/@class, 'mw-empty-elt')))"/>
  </xsl:function>

  <xsl:function name="myfn:is-form-of" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="exists($li/(i|a)[myfn:is-template(@data-mw, ('прич.', 'причастие',
                'сравн.', 'нареч.', 'наречие', 'превосх.'))])"/>
  </xsl:function>

  <xsl:mode name="form-of-targets" on-no-match="shallow-skip"/>
  <xsl:template
      match="li/a[myfn:is-template(@data-mw, ('нареч.', 'наречие'))]"
      as="xs:string*" mode="form-of-targets">
    <xsl:sequence select="myfn:get-form-of-texts(following-sibling::i[1])"/>
  </xsl:template>

  <xsl:template
      match="li/i[myfn:is-template(@data-mw, ('прич.', 'причастие'))]"
      as="xs:string*" mode="form-of-targets">
    <xsl:sequence select="myfn:get-form-of-texts(following-sibling::a[1])"/>
  </xsl:template>

  <xsl:template
      match="li/a[myfn:is-template(@data-mw, ('сравн.', 'превосх.'))]"
      as="xs:string*" mode="form-of-targets">
    <xsl:sequence select="myfn:get-form-of-texts(following-sibling::a[1])"/>
  </xsl:template>
</xsl:stylesheet>
