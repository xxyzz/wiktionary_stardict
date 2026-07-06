<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output method="json" indent="no" encoding="UTF-8"/>

  <xsl:include href="../clean.xsl"/>
  <xsl:include href="config.xsl"/>
  <xsl:include href="pos.xsl"/>

  <xsl:variable
      name="title" select="html/head/title/text()" as="xs:string"/>

  <!-- https://fr.wiktionary.org/wiki/Convention:Structure_des_pages -->
  <!-- https://fr.wiktionary.org/wiki/Modèle:S -->
  <!-- https://fr.wiktionary.org/wiki/Wiktionnaire:Liste_des_sections -->
  <!-- https://fr.wiktionary.org/wiki/Wiktionnaire:Liste_des_sections_de_types_de_mots -->
  <!-- https://fr.wiktionary.org/wiki/Module:types_de_mots/data -->
  <xsl:template match="/">
    <xsl:variable name="results" as="map(*)*">
      <xsl:apply-templates
          select="html/body/section[normalize-space(h2) = $allowed-languages]"
          mode="language"/>
    </xsl:variable>
    <xsl:sequence select="array{$results}"/>
  </xsl:template>

  <!-- Language section -->
  <xsl:template match="section" mode="language">
    <xsl:variable name="language" select="normalize-space(h2)"/>
    <xsl:apply-templates
        select=".//section[p and ol and
                not(some $prefix in ('Forme ', 'Variante ') satisfies
                starts-with(normalize-space(h3|h4|h5|h6), $prefix))]"
        mode="pos">
      <xsl:with-param name="language" select="$language"/>
    </xsl:apply-templates>
  </xsl:template>

  <!-- Modèle:référence nécessaire -->
  <xsl:template match="span[@title='Cette information a besoin d’être sourcée']"
                mode="clean-content"/>
  <!-- Modèle:référence souhaitée -->
  <xsl:template
      match="div[@title = 'Cette information n’est pas remise en cause, mais une référence serait un plus.']"
      mode="clean-content"/>
  <!-- Modèle:préciser -->
  <xsl:template
      match="small[@title = 'Cette information devrait être précisée ou vérifiée.']"
      mode="clean-content"/>
  <!-- Modèle:pron-recons -->
  <xsl:template match="abbr[@title = 'Prononciation théorique']" mode="clean-content"/>
  <xsl:template match="span[@title = 'Prononciation à préciser']" mode="clean-content"/>
</xsl:stylesheet>
