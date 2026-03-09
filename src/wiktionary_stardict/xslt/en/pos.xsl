<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:include href="utils.xsl"/>
  <xsl:include href="alt_forms.xsl"/>
  <xsl:include href="pronunciation.xsl"/>
  <xsl:include href="conjugation.xsl"/>

  <xsl:template match="section" mode="pos">
    <xsl:param name="language"/>
    <xsl:variable
        name="headword-span"
        select="p/span[@class='headword-line']"/>
    <xsl:variable
        name="headword-strong"
        select="for $b in $headword-span/strong[contains(@class, 'headword')] return myfn:ruby_text($b)"
	as="xs:string*"/>
    <xsl:variable
        name="headword-forms"
        select="for $b in $headword-span//b[contains(@class, 'form-of')] return myfn:ruby_text($b)"
        as="xs:string*"/>
    <xsl:variable
	name="pos" select="(h3 | h4 | h5 | h6)[1]/text()" as="xs:string"/>

    <xsl:if test="ol/li[myfn:is_gloss_li(.)]">
      <xsl:variable name="alt-forms" as="xs:string*" select="myfn:get-alt-forms(., $language)"/>
      <xsl:variable name="conj-forms" as="xs:string*">
        <xsl:apply-templates
            select="section[(h4 | h5 | h6)//text() = ('Conjugation', 'Declension')]"
            mode="conj"/>
      </xsl:variable>
      <xsl:variable
          name="unique-forms"
          select="distinct-values(
                  ($headword-strong, $title, $alt-forms, $headword-forms, $conj-forms)[. != ''])"
          as="xs:string*"/>

      <xsl:variable name="definition">
        <section>
	  <xsl:apply-templates
	      select="h3 | h4 | h5 | h6" mode="pos-li"/>
	  <xsl:apply-templates
              select="preceding-sibling::section[starts-with((h3|h4|h5|h6)/text(), 'Pronunciation')] | ancestor::section/section[starts-with((h3|h4|h5|h6)/text(), 'Pronunciation')]"
              mode="pron">
	    <xsl:with-param name="pos" select="$pos"/>
	    <xsl:with-param name="language" select="$language"/>
	  </xsl:apply-templates>
	  <xsl:apply-templates select="p | ol" mode="pos-li"/>
        </section>
      </xsl:variable>

      <xsl:variable name="images" as="xs:string*">
	<xsl:sequence select="$definition//img/@src"/>
      </xsl:variable>

      <xsl:variable name="final-definition">
	<xsl:apply-templates select="$definition" mode="convert-img"/>
      </xsl:variable>

      <xsl:sequence select="array{$language, array{$unique-forms}, $final-definition, array{$images}}"/>
    </xsl:if>
  </xsl:template>

  <xsl:template match="h3 | h4 | h5 | h6" mode="pos-li">
    <h4><xsl:apply-templates mode="clean-content"/></h4>
  </xsl:template>

  <xsl:template match="ol" mode="pos-li">
    <xsl:variable name="lists">
      <xsl:apply-templates select="li" mode="pos-li"/>
    </xsl:variable>
    <xsl:if test="$lists/*">
      <ol><xsl:copy-of select="$lists"/></ol>
    </xsl:if>
  </xsl:template>

  <xsl:template match="li" mode="pos-li">
    <xsl:if test="myfn:is_gloss_li(.)">
      <li><xsl:apply-templates mode="pos-li"/></li>
    </xsl:if>
  </xsl:template>

  <!-- Remove quote examples -->
  <xsl:template match="ul" mode="pos-li"/>

  <!-- Find the shortest usage example -->
  <xsl:template match="dl" mode="pos-li">
    <xsl:variable
        name="examples"
        select="dd[div[contains(@class, 'h-usage-example')] or
                span[contains(@class, 'e-example') or contains(@class, 'affixusex')] or
                dl[contains(@class, 'zhusex')]]"/>
    <xsl:variable
        name="color-panel"
        select="dd[div[contains(@class, 'color-panel')]]"/>
    <xsl:if test="$examples/* or $color-panel/*">
      <dl>
	<xsl:apply-templates select="$color-panel" mode="clean-content"/>
	<xsl:apply-templates
            select="($examples[string-length() = min($examples/string-length())])[1]"
            mode="clean-content"/>
      </dl>
    </xsl:if>
  </xsl:template>

  <xsl:template match="*" mode="pos-li">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>

  <xsl:function name="myfn:is_gloss_li" as="xs:boolean">
    <xsl:param name="n" as="node()"/>
    <xsl:sequence
	select="($n/* or $n/text()) and not($n/span[contains(@class, 'form-of-definition')])"/>
  </xsl:function>

  <xsl:template match="img" mode="convert-img">
    <img>
      <xsl:copy-of select="@*[not(local-name() = 'src')]"/>
      <xsl:attribute name="src">
	<xsl:choose>
	  <xsl:when test="contains(@src, 'math/render/svg/')">
	    <xsl:value-of select="substring-after(@src, 'math/render/svg/')"/>
	    <xsl:text>.svg</xsl:text>
	  </xsl:when>
	  <xsl:otherwise>
	    <xsl:value-of select="substring-before(tokenize(@src, '/')[last()], '?')"/>
	  </xsl:otherwise>
	</xsl:choose>
      </xsl:attribute>
    </img>
  </xsl:template>

  <xsl:template match="*" mode="convert-img">
    <xsl:element name="{local-name()}">
      <xsl:copy-of select="@*"/>
      <xsl:apply-templates mode="convert-img"/>
    </xsl:element>
  </xsl:template>
</xsl:stylesheet>
