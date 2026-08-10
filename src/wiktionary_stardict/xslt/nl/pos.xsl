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
  <xsl:include href="pronunciation.xsl"/>
  <xsl:include href="etymology.xsl"/>
  <xsl:include href="linkage.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:param name="language"/>
    <xsl:if test="ol/li[myfn:is-gloss-li(.)]">
      <xsl:variable
          name="headword-b"
          select="p/b[not(matches(., '^\[[A-Z]\]$'))] ! normalize-space(.)"
          as="xs:string*"/>
      <xsl:variable
          name="pos-index"
          select="normalize-space(p/(b|text())[matches(., '\[[A-Z]\]')][1])"
          as="xs:string"/>
      <xsl:variable
          name="forms-table"
          select="(./table|preceding-sibling::section//table|preceding-sibling::table)
                  [contains-token(@class, 'infobox') and
                  not(.//th/a[text() = ('Rangtelwoord', 'Telwoord')])][last()]"
          as="element(table)?"/>
      <xsl:variable
          name="table-td"
          select="$forms-table//td[not(contains-token(@class, 'infoboxrijhoofding'))]"
          as="element(td)*"/>
      <xsl:variable name="filtered-table-td" as="element(td)*">
        <xsl:apply-templates select="$table-td" mode="filter-td-ipa"/>
      </xsl:variable>
      <xsl:variable
          name="table-forms"
          select="myfn:get-element-forms(for $td in $filtered-table-td return
                  if ($td/a) then $td/a else $td)"
          as="xs:string*"/>
      <!-- Sjabloon:-conjug- Sjabloon:-decl- -->
      <xsl:variable
          name="inflection-section-forms"
          select="section[normalize-space(h5) = ('Vervoeging', 'Verbuiging')]/table//
                  td[not(contains-token(@class, 'infoboxrijhoofding'))]/
                  myfn:get-element-forms(.)"
          as="xs:string*"/>
      <xsl:variable
          name="unique-forms"
          select="distinct-values(($headword-b, $title, $table-forms,
                  $inflection-section-forms)[not(. = ('', '-', '—', '*'))])"
          as="xs:string*"/>
      <xsl:variable
          name="vervoeging-links"
          select="distinct-values($forms-table//
                  td[contains-token(@class, 'infoboxrijhoofding')]/
                  a[some $suffix in ('/vervoeging', '/verbuiging')
                  satisfies ends-with(@title, $suffix)]/@title)"
          as="xs:string*"/>

      <xsl:variable name="definition">
        <section class="mw-parser-output" dir="ltr" lang="nl">
          <xsl:apply-templates select="h4" mode="section-heading"/>
          <xsl:apply-templates
              select="preceding-sibling::section
                      [normalize-space(h5) = 'Uitspraak'][last()]"
              mode="pron">
            <xsl:with-param name="pos-index" select="$pos-index"/>
          </xsl:apply-templates>
          <xsl:apply-templates select="p | ol" mode="pos-li"/>
          <xsl:apply-templates
              select="section[normalize-space(h5) = 'Opmerkingen']"
              mode="usage-notes"/>
          <xsl:apply-templates
              select="section[normalize-space(h5) = ('Synoniemen', 'Antoniemen',
                      'Schrijfwijzen', 'Spreekwoorden', 'Uitdrukkingen en gezegden')]"
              mode="linkage"/>
          <xsl:apply-templates
              select="preceding-sibling::section
                      [normalize-space(h4) = 'Woordherkomst en -opbouw']"
              mode="etymology">
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

      <xsl:variable name="form-of-only" as="xs:boolean">
        <xsl:sequence
            select="boolean(every $li in ol/li[myfn:is-gloss-li(.)]
                    satisfies myfn:li-is-form-of($li))"/>
      </xsl:variable>

      <xsl:sequence
          select="map{'lang': $language,
                  'forms': array{$unique-forms},
                  'def': serialize(
                    $final-definition, map{'method': 'html', 'indent': false()}),
                  'images': array{$images},
                  'form_of_targets': array{if ($form-of-only) then
                    myfn:form-of-targets(ol/li[myfn:is-gloss-li(.)]) else ()},
                  'form_of_only': $form-of-only,
                  'zim_pages': array{$vervoeging-links}}"/>
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

  <!-- shortest usage example -->
  <xsl:template match="dl" mode="pos-li">
    <xsl:variable name="ul-examples" select="dd/ul/li"/>
    <xsl:variable name="dd-examples" select="dd[not(ul or span[text() = '▸'])]"/>
    <xsl:if test="$ul-examples">
      <ul>
        <xsl:apply-templates
            select="($ul-examples[string-length() =
                    min($ul-examples/string-length())])[1]"
            mode="clean-content"/>
      </ul>
    </xsl:if>
    <xsl:if test="$dd-examples">
      <dl>
        <xsl:apply-templates
            select="($dd-examples[string-length() =
                    min($dd-examples/string-length())])[1]"
            mode="clean-content"/>
      </dl>
    </xsl:if>
  </xsl:template>

  <xsl:template match="*" mode="pos-li">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>

  <xsl:function name="myfn:is-gloss-li" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean($li/node() and
                not(contains-token($li/@class, 'mw-empty-elt')))"/>
  </xsl:function>

  <xsl:function name="myfn:li-is-form-of" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean($li//link[contains-token(@rel, 'mw:PageProp/Category') and
                (some $prefix in ('Zelfstandignaamwoordsvorm', 'Werkwoordsvorm',
                'Oude_spelling', 'Bijvoeglijknaamwoordsvorm', 'Deelwoord',
                'Verbogen_vorm', 'Hoofdtelwoord_vorm', 'Rangtelwoordsvorm',
                'Voorzetselvorm', 'Aanwijzend-voornaamwoordsvorm',
                'Bezittelijk-voornaamwoordsvorm', 'Voornaamwoordsvorm',
                'Betrekkelijk-naamwoordsvorm', 'Bijwoordsvorm', 'Eigennaamsvorm',
                'Onvoltooid_deelwoord')
                satisfies starts-with(@href, './Categorie:' || $prefix))])"/>
  </xsl:function>

  <xsl:function name="myfn:form-of-targets" as="xs:string*">
    <xsl:param name="li" as="element(li)*"/>
    <xsl:sequence select="distinct-values($li/a[1] ! normalize-space(.))"/>
  </xsl:function>

  <xsl:template match="section" mode="usage-notes">
    <xsl:variable name="content" select="p | ul"/>
    <xsl:if test="$content">
      <section>
        <xsl:apply-templates select="h4" mode="section-heading"/>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>

  <xsl:mode name="filter-td-ipa" on-no-match="shallow-copy"/>
  <xsl:template match="span[contains-token(@class, 'IPAtekst')]" mode="filter-td-ipa"/>
</xsl:stylesheet>
