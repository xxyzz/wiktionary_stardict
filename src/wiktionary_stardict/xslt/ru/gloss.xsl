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

  <xsl:template match="section" mode="gloss">
    <xsl:param name="language"/>

    <xsl:variable
        name="meaning-section"
        select="section[normalize-space(h4) = ('Значение', 'Значения',
                'Как самостоятельный глагол',
                'В значении вспомогательного глагола или связки') and ol]"/>

    <xsl:if test="$meaning-section/*">
      <xsl:variable
        name="morphology-section"
        select="preceding-sibling::section[normalize-space(h3) =
                ('Морфологические и синтаксические свойства',
                'Тип и синтаксические свойства сочетания',
                'Тип и свойства сочетания')]"/>

      <xsl:variable name="definition">
        <section lang="ru" dir="ltr">
          <xsl:apply-templates select="$morphology-section" mode="morphology"/>
          <xsl:apply-templates
              select="preceding-sibling::section[normalize-space(h3) = 'Произношение']"
              mode="pronunciation"/>
          <xsl:apply-templates select="$meaning-section" mode="meaning"/>
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

      <xsl:sequence select="map{'lang': $language,
                            'forms': array{$unique-forms},
                            'def': $final-definition,
                            'images': array{$images}}"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="section" mode="meaning">
    <h4>Значение</h4>
    <xsl:apply-templates select="p | ol" mode="gloss-li"/>
  </xsl:template>

  <xsl:template match="ol" mode="gloss-li">
    <ol><xsl:apply-templates mode="gloss-li"/></ol>
  </xsl:template>

  <xsl:template match="li" mode="gloss-li">
    <xsl:if test="node()">
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
</xsl:stylesheet>
