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
    <xsl:param name="language"/>

    <xsl:variable
        name="table-forms"
        select="(table[contains-token(@class, 'inflection-table')]//
                td/a/normalize-space())[not(. = ('sein', 'haben'))]"
        as="xs:string*"/>
    <xsl:variable
        name="unique-forms"
        select="distinct-values(($title, $table-forms)[. != ''])"
        as="xs:string*"/>
    <xsl:variable
        name="flexion-links"
        select="table[contains-token(@class, 'inflection-table')]//th//a
                [starts-with(@title, 'Flexion:')]/@title"
        as="xs:string*"/>

    <xsl:variable name="definition">
      <section lang="de" dir="ltr">
        <xsl:apply-templates select="h3" mode="pos"/>
        <xsl:apply-templates
            select="p[@data-mw and myfn:is-template(@data-mw, 'Worttrennung')]"
            mode="hyphenation"/>
        <xsl:apply-templates
            select="p[@data-mw and myfn:is-template(@data-mw, 'Aussprache')]"
            mode="pronunciation"/>
        <xsl:apply-templates
            select="p[@data-mw and myfn:is-template(@data-mw, 'Bedeutungen')]"
            mode="meaning"/>
        <xsl:apply-templates
            select="p[@data-mw and myfn:is-template(@data-mw, 'Herkunft')]"
            mode="etymology"/>
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
                          'zim_pages': array{$flexion-links}}"/>
  </xsl:template>

  <xsl:template match="h3" mode="pos">
    <h4><xsl:apply-templates mode="clean-content"/></h4>
  </xsl:template>

  <xsl:template match="p" mode="hyphenation">
    <section>
      <xsl:apply-templates select="following-sibling::dl[1]" mode="clean-content"/>
    </section>
  </xsl:template>

  <xsl:template match="p" mode="meaning">
    <section>
      <h4>Bedeutungen:</h4>
      <xsl:apply-templates select="following-sibling::dl[1]" mode="clean-content"/>
    </section>
  </xsl:template>

  <xsl:template match="p" mode="etymology">
    <section>
      <h4>Herkunft:</h4>
      <xsl:apply-templates select="following-sibling::dl[1]" mode="clean-content"/>
    </section>
  </xsl:template>
</xsl:stylesheet>
