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

  <xsl:template match="section" mode="pos">
    <xsl:param name="language"/>

    <xsl:variable name="headword-forms" as="xs:string*"
        select="p/(b|bdi)/myfn:get-element-forms(.)"/>
    <xsl:variable
        name="table-forms"
        select="table[contains-token(@class, 'wikitable')]//td/bdi/
                myfn:get-element-forms(.)"
        as="xs:string*"/>
    <xsl:variable
        name="unique-forms"
        select="distinct-values(($headword-forms, $title, $table-forms)[. != ''])"
        as="xs:string*"/>
    <xsl:variable
        name="conj-links"
        select="p/a[starts-with(@title, 'Conjugaison:') and
                not(some $v in ('Premier groupe', 'Deuxième groupe', 'Troisième groupe')
                satisfies ends-with(@title, $v))]/@title"
        as="xs:string*"/>

    <xsl:variable name="definition">
      <section lang="fr" dir="ltr">
        <xsl:apply-templates
            select="h3 | h4 | h5 | h6" mode="pos-li"/>
        <xsl:apply-templates
            select="p | ol | section[normalize-space(h4|h5|h6) = 'Notes']"
            mode="pos-li"/>
        <xsl:apply-templates
            select="preceding-sibling::section[normalize-space(h3[1]) = 'Étymologie']
                    [last()]"
            mode="etymology">
          <xsl:with-param
              name="pos-id"
              select="(h3|h4|h5|h6)/span[contains-token(@class, 'titredef')]/@id"/>
        </xsl:apply-templates>
      </section>
    </xsl:variable>

    <xsl:variable name="images" as="xs:string*">
      <xsl:sequence select="$definition//img/@src"/>
    </xsl:variable>

    <xsl:variable name="final-definition">
      <xsl:apply-templates select="$definition" mode="convert-img"/>
    </xsl:variable>

    <xsl:sequence select="map{'lang': $language,
                          'forms': array{$unique-forms},
                          'def': $final-definition,
                          'images': array{$images},
                          'zim_pages': array{$conj-links}}"/>
  </xsl:template>

  <xsl:template match="h3 | h4 | h5 | h6" mode="pos-li">
    <h4><xsl:apply-templates mode="clean-content"/></h4>
  </xsl:template>

  <xsl:template match="ol" mode="pos-li">
    <ol><xsl:apply-templates mode="pos-li"/></ol>
  </xsl:template>

  <xsl:template match="li" mode="pos-li">
    <xsl:if test="node()">
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
</xsl:stylesheet>
