<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:include href="../image.xsl"/>
  <xsl:include href="../utils.xsl"/>
  <xsl:include href="conjugation.xsl"/>
  <xsl:include href="pronunciation.xsl"/>
  <xsl:include href="etymology.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:param name="language"/>
    <xsl:variable
        name="pos" select="normalize-space((h3 | h4 | h5 | h6)[1])" as="xs:string"/>
    <xsl:if test="not(starts-with($pos, 'Forma '))">
      <xsl:variable
          name="headword-forms"
          select="for $p in p[child::*[1][self::b[@typeof='mw:Transclusion']]]
                  return myfn:headword-forms($p)"
          as="xs:string*"/>
      <xsl:variable
          name="conj-section"
          select="(section | following-sibling::section)
                  [normalize-space(h3|h4|h5|h6) = 'Conjugación'][1]"/>
      <xsl:variable
          name="conj-forms"
          select="if (starts-with($pos, 'Verbo') and $conj-section)
                  then myfn:conj-forms($conj-section) else ()"
          as="xs:string*"/>

      <xsl:variable
          name="unique-forms"
          select="distinct-values(($title, $headword-forms, $conj-forms)[. != ''])"
          as="xs:string*"/>

      <xsl:variable name="definition">
        <section class="mw-parser-output" dir="ltr" lang="es">
          <xsl:apply-templates select="h3 | h4 | h5 | h6" mode="pos"/>
          <xsl:apply-templates
              select="ancestor::section/table[@data-mw]
                      [myfn:is-template(@data-mw, 'pron-graf')][last()]" mode="pron"/>
          <xsl:apply-templates
              select="p[child::*[1][self::b[@typeof='mw:Transclusion']]] | dl"
              mode="pos"/>
          <xsl:apply-templates
              select="(parent::section | preceding-sibling::section)
                      [starts-with(normalize-space((h3|h4|h5|h6)[1]), 'Etimología')]
                      [last()]"
              mode="etymology"/>
        </section>
      </xsl:variable>

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
                  'images': array{$images}}"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="h3 | h4 | h5 | h6" mode="pos">
    <h4><xsl:apply-templates mode="clean-content"/></h4>
  </xsl:template>

  <xsl:template match="dl" mode="pos">
    <dl><xsl:apply-templates mode="pos"/></dl>
  </xsl:template>

  <xsl:template match="dd" mode="pos">
    <dd><xsl:apply-templates mode="pos"/></dd>
  </xsl:template>

  <xsl:template match="ul" mode="pos">
    <xsl:variable
        name="linkages"
        select="li[b/text() = ('Sinónimos:', 'Sinónimo:', 'Antónimos', 'Antónimo:',
                'Uso:', 'Ámbito')]"/>
    <xsl:variable
        name="examples"
        select="li[b/text() = 'Ejemplo:' and
                not(div[contains-token(@class, 'mw-collapsed')])]"/>
    <xsl:if test="$linkages/* or $examples/*">
      <ul>
        <xsl:apply-templates select="$linkages" mode="clean-content"/>
        <xsl:apply-templates
            select="($examples[string-length() = min($examples/string-length())])[1]"
            mode="clean-content"/>
      </ul>
    </xsl:if>
  </xsl:template>

  <xsl:template match="*" mode="pos">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>

  <xsl:function name="myfn:headword-forms" as="xs:string*">
    <xsl:param name="node" as="node()"/>
    <xsl:for-each-group
        select="$node/a"
        group-starting-with="a[preceding-sibling::*[1][normalize-space() != '']]">
      <xsl:sequence select="string-join(current-group(), ' ')"/>
    </xsl:for-each-group>
  </xsl:function>
</xsl:stylesheet>
