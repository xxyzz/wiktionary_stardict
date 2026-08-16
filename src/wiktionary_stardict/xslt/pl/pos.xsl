<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:fn="http://www.w3.org/2005/xpath-functions"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:include href="../utils.xsl"/>
  <xsl:include href="../image.xsl"/>
  <xsl:include href="inflection.xsl"/>
  <xsl:include href="pronunciation.xsl"/>

  <xsl:template match="p" mode="pos">
    <xsl:param name="language" as="xs:string"/>
    <xsl:param name="ids" as="xs:string*"/>

    <xsl:variable name="pos-index" select="position()"/>
    <xsl:variable
        name="unique-forms"
        select="distinct-values((
                $title,
                myfn:get-inflection-forms(
                  following-sibling::dl[dt[span[@data-field = 'odmiana']]][1],
                  $pos-index),
                myfn:get-alt-forms(
                  preceding-sibling::dl[dt[span[@data-field =
                  ('ortografie', 'warianty')]]][1])
                ))[. != '']"
        as="xs:string*"/>

    <xsl:variable name="definition">
      <section class="mw-parser-output" dir="ltr" lang="pl">
        <xsl:apply-templates select="." mode="clean-content"/>
        <xsl:apply-templates
            select="preceding-sibling::dl[dt[span[@data-field = 'wymowa']]][1]"
            mode="pron">
          <xsl:with-param name="pos-index" select="$pos-index"/>
        </xsl:apply-templates>
        <xsl:apply-templates select="following-sibling::dl[1]" mode="clean-content"/>
        <xsl:apply-templates
            select="following-sibling::dl[dt[span[@data-field = 'przyklady']]][1]"
            mode="example">
          <xsl:with-param name="pos-index" select="$pos-index"/>
        </xsl:apply-templates>
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
                'images': array{$images},
                'ids': array{$ids}}"/>
  </xsl:template>

  <xsl:template match="dl" mode="example">
    <xsl:param name="pos-index" as="xs:integer"/>
    <xsl:variable name="examples" select="myfn:match-dd(dd, $pos-index)"/>
    <xsl:if test="$examples">
      <dl>
        <xsl:apply-templates select="dt" mode="clean-content"/>
        <xsl:for-each-group
            select="$examples"
            group-by="(text()/analyze-string(., '\(([\d\s,.-]+)\)')//fn:group)[1]">
          <xsl:apply-templates
              select="current-group()[string-length() =
                      min(current-group()/string-length())][1]"
              mode="clean-content"/>
        </xsl:for-each-group>
      </dl>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
