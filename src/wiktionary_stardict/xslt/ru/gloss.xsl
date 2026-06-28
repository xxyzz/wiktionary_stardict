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

      <xsl:sequence
          select="map{'lang': $language,
                  'forms': array{$unique-forms},
                  'def': serialize(
                    $final-definition, map{'method': 'html', 'indent': false()}),
                  'images': array{$images},
                  'ids': array{myfn:get-ancestor-section-ids(.)}}"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="section" mode="meaning">
    <xsl:apply-templates select="h4[1]" mode="section-title"/>
    <xsl:apply-templates select="p | ol" mode="gloss-li"/>
  </xsl:template>

  <xsl:template match="ol" mode="gloss-li">
    <ol><xsl:apply-templates mode="gloss-li"/></ol>
  </xsl:template>

  <xsl:template match="li" mode="gloss-li">
    <xsl:if test="node() and not(contains-token(@class, 'mw-empty-elt'))">
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

  <xsl:template match="h3 | h4 | h5 | h6" mode="section-title">
    <h4><xsl:apply-templates mode="clean-content"/></h4>
  </xsl:template>
</xsl:stylesheet>
