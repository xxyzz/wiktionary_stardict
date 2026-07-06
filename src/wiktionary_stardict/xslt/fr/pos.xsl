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
  <xsl:include href="etymology.xsl"/>
  <xsl:include href="linkage.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:param name="language"/>
    <xsl:if test="ol/li[myfn:is-gloss-li(.)]">
      <xsl:variable name="headword-forms" as="xs:string*"
                    select="p/(b|bdi)/myfn:get-element-forms(.)"/>
      <xsl:variable
          name="table-forms"
          select="table[contains-token(@class, 'flextable')]//td/bdi/
                  myfn:get-element-forms(.)"
          as="xs:string*"/>
      <xsl:variable
          name="title-form"
          select="if (not(starts-with($title, 'Titres non pris en charge/')))
                  then $title else ''"/>
      <xsl:variable
          name="unique-forms"
          select="distinct-values(($headword-forms, $title-form, $table-forms)[. != ''])"
          as="xs:string*"/>
      <xsl:variable
          name="conj-links"
          select="p/a[starts-with(@title, 'Conjugaison:') and not(
                  some $v in ('Premier groupe', 'Deuxième groupe', 'Troisième groupe')
                  satisfies ends-with(@title, $v))]/@title"
          as="xs:string*"/>

      <xsl:variable name="definition">
        <section class="mw-parser-output" lang="fr" dir="ltr">
          <xsl:apply-templates select="h3 | h4 | h5 | h6" mode="section-heading"/>
          <xsl:apply-templates select="p | ol" mode="pos-li"/>
          <xsl:apply-templates
              select="section[normalize-space(h4|h5|h6) = 'Notes']" mode="notes"/>
          <xsl:apply-templates
              select="section[normalize-space(h4|h5|h6) =
                      ('Synonymes', 'Quasi-synonymes', 'Antonymes', 'Variantes',
                      'Variantes dialectales', 'Variantes orthographiques')]"
              mode="linkage"/>
          <xsl:apply-templates
              select="preceding-sibling::section[normalize-space(h3[1]) = 'Étymologie']
                      [last()]"
              mode="etymology">
            <xsl:with-param name="pos-ids" select="(h3|h4|h5|h6)/span/@id"/>
          </xsl:apply-templates>
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
                  'def': serialize(
                    $final-definition, map{'method': 'html', 'indent': false()}),
                  'images': array{$images},
                  'zim_pages': array{$conj-links},
                  'ids': array{myfn:fr-pos-section-ids(.)},
                  'form_of_targets': array{if ($form-of-only) then
                    myfn:form-of-targets(ol/li[myfn:is-gloss-li(.)]) else ()},
                  'form_of_only': $form-of-only}"/>
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

  <!-- Find the shortest usage example -->
  <xsl:template match="ul" mode="pos-li">
    <xsl:variable name="examples" select="li[span[q]]"/>
    <xsl:if test="$examples">
      <ul>
        <xsl:apply-templates
            select="($examples[string-length() = min($examples/string-length())])[1]"
            mode="clean-content"/>
      </ul>
    </xsl:if>
  </xsl:template>

  <xsl:template match="p" mode="pos-li">
    <p><xsl:apply-templates mode="pos-li"/></p>
  </xsl:template>

  <xsl:template
      match="a[normalize-space() = 'voir la conjugaison'] |
             span[following-sibling::a[1][normalize-space() = 'voir la conjugaison']] |
             span[preceding-sibling::a[1][normalize-space() = 'voir la conjugaison']]"
      mode="pos-li"/>

  <xsl:template match="*" mode="pos-li">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>

  <xsl:template match="section" mode="notes">
    <xsl:variable name="content" select="p | dl | ul | ol"/>
    <xsl:if test="$content">
      <section>
        <h4>Notes</h4>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>

  <xsl:function name="myfn:fr-pos-section-ids" as="xs:string*">
    <xsl:param name="section" as="element(section)"/>
    <xsl:sequence select="myfn:get-heading-ids(
                          ($section | $section/ancestor::section)/(h2|h3|h4))"/>
  </xsl:function>

  <xsl:function name="myfn:get-heading-ids" as="xs:string*">
    <xsl:param name="heading" as="element()*"/>
    <xsl:variable
        name="span-ids" select="$heading/span/@id[not(starts-with(., 'mw'))]"/>
    <xsl:sequence
        select="$heading/@id[not(starts-with(., 'mw'))], $span-ids"/>
  </xsl:function>

  <xsl:function name="myfn:is-gloss-li" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean($li/node() and
                not(contains-token($li/@class, 'mw-empty-elt')) and
                not($li/i[@data-mw and myfn:is-template(@data-mw, 'ébauche-déf')]))"/>
  </xsl:function>

  <xsl:function name="myfn:is-form-of" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean(($li/i|$li/span)[@data-mw and myfn:is-template(@data-mw,
                ('variante ateji de', 'variante de', 'variante hanja de',
                'variante hiragana de', 'variante kanji de', 'variante katakana de',
                'variante kyujitai de', 'variante ortho de', 'variante romaji de'))] or
                $li/text()[starts-with(normalize-space(), 'Variante ')] or
                $li/i[starts-with(normalize-space(), 'Variante ')])"/>
  </xsl:function>

  <xsl:function name="myfn:form-of-targets" as="xs:string*">
    <xsl:param name="li" as="element(li)*"/>
    <xsl:sequence
        select="distinct-values((if ($li/bdi) then $li/bdi else $li/i/a) !
                normalize-space(.))"/>
  </xsl:function>
</xsl:stylesheet>
