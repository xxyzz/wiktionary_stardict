<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:include href="../image.xsl"/>
  <xsl:include href="pronunciation.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:param name="language" as="xs:string"/>
    <xsl:param name="lemma-code" as="xs:string"/>

    <xsl:variable
        name="headword-first-b" select="(p/b[@data-mw])[1]"/>
    <xsl:variable
        name="headword-rest-b" select="$headword-first-b/following-sibling::b"/>
    <xsl:variable
        name="headword-b-forms"
        select="myfn:get-element-forms(($headword-first-b, $headword-rest-b))"
        as="xs:string*"/>
    <xsl:variable
        name="headword-big-forms" select="myfn:get-element-forms(div//big)"
        as="xs:string*"/>
    <xsl:variable
        name="headword-linkp-forms"
        as="xs:string*"
        select="myfn:get-template-arg(
                (p/span[@data-mw and myfn:is-template(@data-mw, 'Linkp')]/@data-mw)[1],
                'Linkp', '1')"/>
    <xsl:variable
        name="table-forms"
        select="myfn:get-element-forms(table[not(preceding-sibling::div
                [@data-mw and myfn:is-template(@data-mw, 'ja-kanjitab')])]//td)"
        as="xs:string*"/>
    <xsl:variable
        name="alt-forms"
        select="myfn:get-element-forms((following-sibling::section |
                parent::section[h3]/following-sibling::section)
                [normalize-space(h3[1]) = ('Varianti', 'Variazione', 'Forme flesse',
                'Variazioni', 'Variante')]//li/a)"
        as="xs:string*"/>
    <xsl:variable
        name="unique-forms"
        select="distinct-values(($title, $headword-b-forms, $headword-linkp-forms,
                $headword-big-forms, $table-forms, $alt-forms))
                [. != '']"
        as="xs:string*"/>

    <xsl:variable name="definition">
      <section class="mw-parser-output" dir="ltr" lang="it">
        <xsl:apply-templates
            select="preceding-sibling::h3" mode="section-heading"/>
        <xsl:apply-templates
            select="h3 | h4 | h5 | h6" mode="section-heading"/>
        <xsl:apply-templates
            select="(following-sibling::section |
                    parent::section[h3]/following-sibling::section)
                    [normalize-space(h3[1]) = 'Pronuncia']"
            mode="pron"/>
        <xsl:apply-templates select="p | div[.//big] | ol" mode="pos-li"/>
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
        select="boolean(let $pos := normalize-space(if (preceding-sibling::h3) then
                preceding-sibling::h3[1] else h3[1])
                return (ends-with($pos, ', forma flessa') or $pos = 'Voce verbale'))"/>

    <xsl:sequence
        select="map{'lang': $language,
                'forms': array{$unique-forms},
                'def': serialize(
                  $final-definition, map{'method': 'html', 'indent': false()}),
                'images': array{$images},
                'ids': array{myfn:get-pos-section-ids(.)},
                'lemma_code': $lemma-code,
                'form_of_targets': array{if ($form-of-only) then
                  myfn:form-of-targets(ol/li) else ()},
                'form_of_only': $form-of-only}"/>
  </xsl:template>

  <xsl:template match="h3 | h4 | h5 | h6" mode="section-heading">
    <xsl:variable name="content">
      <xsl:apply-templates mode="section-heading-nodes"/>
    </xsl:variable>
    <h4><xsl:apply-templates select="$content" mode="clean-content"/></h4>
  </xsl:template>
   <xsl:mode name="section-heading-nodes" on-no-match="shallow-copy"/>
  <xsl:template
      match="span[contains-token(@typeof, 'mw:File')]" mode="section-heading-nodes"/>

  <!-- rm Wikipedia link in headword line -->
  <xsl:template
      match="small[preceding-sibling::b[@data-mw and myfn:is-template(@data-mw, 'Pn')]]"
      mode="clean-content"/>

  <xsl:template match="ol" mode="pos-li">
    <ol><xsl:apply-templates mode="pos-li"/></ol>
  </xsl:template>

  <xsl:template match="li" mode="pos-li">
    <xsl:if test="myfn:is-not-empty-li(.)">
      <li><xsl:apply-templates mode="pos-li"/></li>
    </xsl:if>
  </xsl:template>

  <xsl:template match="ul" mode="pos-li">
    <xsl:variable name="examples" select="li[myfn:is-not-empty-li(.)]"/>
    <xsl:if test="$examples">
      <ul>
        <xsl:apply-templates
            select="($examples[string-length() = min($examples/string-length())])[1]"
            mode="clean-content"/>
      </ul>
    </xsl:if>
  </xsl:template>

  <xsl:template match="*" mode="pos-li">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>

  <xsl:function name="myfn:is-not-empty-li" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean($li/node() and
                not(contains-token($li/@class, 'mw-empty-elt')))"/>
  </xsl:function>

  <xsl:function name="myfn:form-of-targets" as="xs:string*">
    <xsl:param name="li" as="element(li)*"/>
    <xsl:sequence
        select="distinct-values($li/a
                [ends-with(normalize-space(preceding-sibling::text()[1]), ' di')] !
                normalize-space(.))[. != '']"/>
  </xsl:function>
</xsl:stylesheet>
