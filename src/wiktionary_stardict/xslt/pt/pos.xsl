<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:include href="../image.xsl"/>
  <xsl:include href="conjugation.xsl"/>
  <xsl:include href="etymology.xsl"/>
  <xsl:include href="../en/linkage.xsl"/>
  <xsl:include href="pronunciation.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:param name="language" as="xs:string"/>

    <xsl:variable
        name="headword-b-forms" select="p/b ! normalize-space(replace(., '.', ''))"
        as="xs:string*"/>
    <xsl:variable
        name="table-forms"
        select="myfn:get-element-forms(
                for $td in table//td[not(contains-token(@class, 'genero'))]
                return if ($td/span[contains-token(@class, 'lnkprt')]) then
                $td/span[contains-token(@class, 'lnkprt')] else $td)"
        as="xs:string*"/>
    <xsl:variable
        name="conj-forms"
        select="myfn:get-conj-forms((section|following-sibling::section)
                [normalize-space((h2|h3)[1]) = 'Conjugação'][1])"
        as="xs:string*"/>
    <xsl:variable
        name="alt-form-titles"
        select="('Sigla', 'Abreviatura', 'Símbolo',
                'Ordinal Equivalente', 'Forma alternativa', 'Variante', 'Variantes',
                'Variação', 'Grafias alternativas', 'Grafia alternativa',
                'Forma(s) alternativa(s)', 'Formas alternativas', 'Graus')"
        as="xs:string*"/>
    <xsl:variable
        name="alt-forms"
        select="myfn:get-alt-forms((section|following-sibling::section)
                [normalize-space((h2|h3)[1]) = $alt-form-titles][1])"
        as="xs:string*"/>
    <xsl:variable
        name="unique-forms"
        select="distinct-values(($headword-b-forms, $title, $table-forms, $conj-forms,
                $alt-forms)[not(. = ('', '-'))])"
        as="xs:string*"/>

    <xsl:variable name="definition">
      <section class="mw-parser-output" dir="ltr" lang="pt">
        <xsl:apply-templates
            select="h2[1]" mode="section-heading"/>
        <xsl:apply-templates select="p[b] | ol" mode="pos-li"/>
        <xsl:apply-templates
            select="(section|following-sibling::section)
                    [normalize-space((h2|h3)[1]) = 'Pronúncia'][1]"
            mode="pron"/>
        <xsl:apply-templates
            select="(section|following-sibling::section)
                    [normalize-space((h2|h3)[1]) = ($alt-form-titles, 'Nota', 'Uso',
                    'Notas', 'Graus', 'Fraseologia')][1]"
            mode="etymology"/>
        <xsl:apply-templates
            select="(section|following-sibling::section)
                    [normalize-space((h2|h3)[1]) = ('Sinônimos', 'Sinônimo',
                    'Sinónimos/Sinônimos', 'Sinónimos', 'Sinónimo',
                    'Sinônimos e variantes', 'Antônimos', 'Antônimo', 'Antónimo',
                    'Antónimos', 'Antónimos/Antônimos', 'Expressões', 'Expressão')][1]"
            mode="linkage"/>
        <xsl:apply-templates
            select="(section|following-sibling::section)
                    [normalize-space((h2|h3)[1]) = 'Etimologia'][1]"
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
        select="boolean(let $pos := normalize-space(h2[1])
                return starts-with($pos, 'Forma ') or $pos = 'Transliteração')"/>

    <xsl:sequence
        select="map{'lang': $language,
                'forms': array{$unique-forms},
                'def': serialize(
                  $final-definition, map{'method': 'html', 'indent': false()}),
                'images': array{$images},
                'form_of_targets': array{if ($form-of-only) then
                  myfn:form-of-targets(ol/li) else ()},
                'form_of_only': $form-of-only}"/>
  </xsl:template>

  <xsl:template match="h2 | h3 | h4 | h5 | h6" mode="section-heading">
    <h4><xsl:apply-templates mode="clean-content"/></h4>
  </xsl:template>

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
        select="distinct-values((if ($li/b) then $li/b else $li/a[last()]) !
                normalize-space(.))[. != '']"/>
  </xsl:function>

  <!-- Predefinição:proparoxítona aparente -->
  <xsl:template match="sup[normalize-space(.) = 'nota']" mode="clean-content"/>
</xsl:stylesheet>
