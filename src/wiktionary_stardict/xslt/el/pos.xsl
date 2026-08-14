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
  <xsl:include href="inflection.xsl"/>
  <xsl:include href="pronunciation.xsl"/>
  <xsl:include href="etymology.xsl"/>
  <xsl:include href="linkage.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:param name="language"/>
    <xsl:variable
        name="headword-forms" as="xs:string*"
        select="myfn:get-element-forms(for $b in p/b
                return if ($b/span) then $b/span else $b)"/>
    <xsl:variable name="table-forms" as="xs:string*" select="myfn:get-table-forms(.)"/>
    <xsl:variable
        name="inf-forms" as="xs:string*"
        select="myfn:get-inf-section-forms(section[
                normalize-space((h4|h5|h6)[1]) = 'Κλίση'])"/>
    <xsl:variable
        name="alt-forms" as="xs:string*"
        select="myfn:get-alt-forms(section[
                normalize-space((h4|h5|h6)[1]) = 'Άλλες μορφές'])"/>
    <xsl:variable
        name="unique-forms"
        select="distinct-values(($headword-forms, $title, $table-forms, $inf-forms,
                $alt-forms)[not(. = ('', '-'))])"
        as="xs:string*"/>
    <xsl:variable name="definition">
      <section class="mw-parser-output" dir="ltr" lang="el">
        <xsl:apply-templates
            select="h3 | h4 | h5 | h6" mode="section-heading"/>
        <xsl:apply-templates
            select="(preceding-sibling::section | ancestor::section)
                    [(h3|h4)[span[contains-token(@class, 'pronunciation')]]][last()]"
            mode="pron"/>
        <xsl:apply-templates select="p | ol | ul" mode="pos-li"/>
        <xsl:apply-templates
            select="section[normalize-space((h4|h5|h6)[1]) = 'Σημειώσεις']"
            mode="notes"/>
        <xsl:apply-templates
            select="section[normalize-space((h4|h5|h6)[1]) =
                    ('Άλλες μορφές', 'Συνώνυμα', 'Αντώνυμα', 'Εκφράσεις')]"
            mode="linkage"/>
        <xsl:apply-templates
            select="(preceding-sibling::section | ancestor::section)
                    [h3[span[@data-mw and myfn:is-template(@data-mw, 'ετυμολογία')]]]
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

    <xsl:variable
        name="form-of-only" as="xs:boolean"
        select="boolean(every $li in (ol|ul)/li[myfn:is-gloss-li(.)]
                satisfies myfn:is-form-of($li))"/>

    <xsl:sequence
        select="map{'lang': $language,
                'forms': array{$unique-forms},
                'def': serialize(
                  $final-definition, map{'method': 'html', 'indent': false()}),
                'images': array{$images},
                'form_of_targets': array{if ($form-of-only) then
                  myfn:form-of-targets((ol|ul)/li) else ()},
                'form_of_only': $form-of-only,
                'ids': array{myfn:get-pos-section-ids(.)}}"/>
  </xsl:template>

  <xsl:mode name="section-heading" on-no-match="shallow-copy"/>
  <xsl:template match="img" mode="section-heading"/>
  <xsl:template match="h3 | h4 | h5 | h6" mode="section-heading">
    <xsl:variable name="content">
      <xsl:apply-templates mode="section-heading"/>
    </xsl:variable>
    <h4><xsl:apply-templates select="$content" mode="clean-content"/></h4>
  </xsl:template>

  <xsl:template match="ol" mode="pos-li">
    <ol><xsl:apply-templates mode="pos-li"/></ol>
  </xsl:template>

  <xsl:template match="ul" mode="pos-li">
    <ul><xsl:apply-templates mode="pos-li"/></ul>
  </xsl:template>

  <xsl:template match="li" mode="pos-li">
    <xsl:if test="myfn:is-gloss-li(.)">
      <li><xsl:apply-templates mode="pos-li"/></li>
    </xsl:if>
  </xsl:template>

  <!-- shortest usage example -->
  <xsl:template match="dl" mode="pos-li">
    <xsl:variable
        name="examples"
        select="dd[span[@data-mw and
                myfn:is-template(@data-mw, ('πχ', 'eg', 'ιαπ'))]]"/>
    <xsl:variable
        name="color-panel"
        select="dd[table[@data-mw and
                myfn:is-template(@data-mw, ('χρωμ', 'colour panel', 'χρώμ'))]]"/>
    <!-- Κατηγορία:Πρότυπα για ετικέτες -->
    <xsl:variable
        name="nyms"
        select="dd[span[@data-mw and myfn:is-template(@data-mw, ('συν', 'syn', 'αντ',
                'ant', 'συνων', 'συνών', 'συνυπ', 'συνυπων', 'συνυπών', 'αντων',
                'αντών', 'αρχελλ', 'λατ', 'μορφ', 'ταυτ', 'υπ', 'υπων', 'υπών', 'υπερ',
                'υπερων', 'υπερών', 'βλ', 'cf', 'go'))]]"/>
    <xsl:if test="$examples or $color-panel or $nyms">
      <dl>
        <xsl:apply-templates
            select="($examples[string-length() = min($examples/string-length())])[1]"
            mode="clean-content"/>
        <xsl:apply-templates select="$color-panel" mode="clean-content"/>
        <xsl:apply-templates select="$nyms" mode="clean-content"/>
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

  <!-- Κατηγορία:Πρότυπα για κλιτικούς τύπους -->
  <xsl:function name="myfn:is-form-of" as="xs:boolean">
    <xsl:param name="li" as="element(li)"/>
    <xsl:sequence
        select="boolean($li/(span|a|i)[@data-mw and (myfn:is-template(@data-mw, ('κλ',
                'infl', 'acc eo', 'αιτ του', 'αιτιατική πληθυντικού του', 'πλ',
                'plur', 'πληθ του', 'αιτιατική του', 'αορ', 'aor', 'αρσ του',
                'γερουνδιακ', 'ενεστώτας του', 'θηλ του', 'ουδ του', 'πτΓπλ',
                'ρημ τύπος', 'σνρ', 'γρ', 'γραφή του', 'alter', 'βλ', 'cf', 'go')) or
                myfn:is-template-prefix(@data-mw, ('αρσ του-', 'θηλ του-', 'ουδ του-',
                'πτώσεις', 'πτώση')))])"/>
  </xsl:function>

  <xsl:function name="myfn:form-of-targets" as="xs:string*">
    <xsl:param name="li-nodes" as="element(li)*"/>
    <xsl:sequence
        select="distinct-values(
                for $li in $li-nodes return
                let $σνρ-a := $li/a[@data-mw and myfn:is-template(@data-mw, 'σνρ')],
                    $βλ-span := $li/span[@data-mw and
                      myfn:is-template(@data-mw, ('βλ', 'cf', 'go'))]
                return if ($σνρ-a) then
                  normalize-space(myfn:get-template-arg($σνρ-a[1]/@data-mw, 'σνρ', '1'))
                else if ($βλ-span) then
                  normalize-space(myfn:get-template-arg(
                    $βλ-span[1]/@data-mw, ('βλ', 'cf', 'go'), '1'))
                else $li//b ! normalize-space())[. != '']"/>
  </xsl:function>

  <xsl:template
      match="p/small[sup[a[@rel='mw:WikiLink/Interwiki']]]" mode="clean-content"/>

  <xsl:template match="section" mode="notes">
    <xsl:variable name="content" select="p | ul | ol"/>
    <xsl:if test="$content">
      <section>
        <xsl:apply-templates select="h4|h5|h6" mode="section-heading"/>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
