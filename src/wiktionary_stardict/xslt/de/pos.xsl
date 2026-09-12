<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:fn="http://www.w3.org/2005/xpath-functions"
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
        name="alternative-forms"
        select="p[@data-mw and myfn:is-template(@data-mw, 'Alternative Schreibweisen')]/
                following-sibling::dl[1] => myfn:get-alt-forms()"
        as="xs:string*"/>
    <xsl:variable
        name="unique-forms"
        select="distinct-values(($title, $table-forms, $alternative-forms)[. != ''])"
        as="xs:string*"/>
    <xsl:variable
        name="flexion-links"
        select="table[contains-token(@class, 'inflection-table')]//th//a
                [starts-with(@title, 'Flexion:')]/@title"
        as="xs:string*"/>

    <xsl:variable name="definition">
      <section class="mw-parser-output" dir="ltr" lang="de">
        <xsl:apply-templates select="h3" mode="pos"/>
        <xsl:apply-templates
            select="p[@data-mw and myfn:is-template(@data-mw, 'Worttrennung')]"
            mode="hyphenation"/>
        <xsl:apply-templates
            select="p[@data-mw and myfn:is-template(@data-mw, 'Aussprache')]"
            mode="pronunciation"/>
        <xsl:apply-templates
            select="p[@data-mw and myfn:is-template(@data-mw, ('Bedeutungen',
                    'Herkunft', 'Synonyme', 'Sinnverwandte Redewendungen',
                    'Gegenwörter', 'Beispiele'))]"
            mode="p-section"/>
      </section>
    </xsl:variable>

    <xsl:variable name="images" as="xs:string*">
      <xsl:sequence select="$definition//img/@src"/>
    </xsl:variable>

    <xsl:variable name="final-definition">
      <xsl:apply-templates select="$definition" mode="convert-img"/>
    </xsl:variable>

    <xsl:variable name="math" select="myfn:get-math-tex(.)"/>

    <xsl:sequence
        select="map{'lang': $language,
                'forms': array{$unique-forms},
                'def': if (exists($math)) then serialize($final-definition) else
                  serialize($final-definition, map{'method': 'html',
                  'indent': false(), 'escape-uri-attributes': false()}),
                'images': array{$images},
                'zim_pages': array{$flexion-links},
                'ids': array{myfn:get-ancestor-section-ids(.)},
                'math': array{$math}}"/>
  </xsl:template>

  <xsl:template match="h3" mode="pos">
    <h4><xsl:apply-templates mode="clean-content"/></h4>
  </xsl:template>

  <xsl:template match="p" mode="hyphenation">
    <section>
      <xsl:apply-templates select="following-sibling::dl[1]" mode="clean-content"/>
    </section>
  </xsl:template>

  <xsl:template match="p" mode="p-section">
    <section>
      <xsl:choose>
        <xsl:when test="@data-mw and myfn:is-template(@data-mw, 'Beispiele')">
          <xsl:apply-templates select="." mode="examples"/>
        </xsl:when>
        <xsl:otherwise>
          <h4>{normalize-space(.)}</h4>
          <xsl:apply-templates select="following-sibling::dl[1]" mode="clean-content"/>
        </xsl:otherwise>
      </xsl:choose>
    </section>
  </xsl:template>

  <xsl:function name="myfn:get-alt-forms" as="xs:string*">
    <xsl:param name="dl" as="element(dl)*"/>
    <xsl:sequence select="$dl/dd/a[not(ends-with(string(), ':'))]/@title"/>
  </xsl:function>

  <xsl:template match="p" mode="examples">
    <xsl:variable name="content">
      <xsl:choose>
        <xsl:when test="following-sibling::*[1][self::ul]">
          <xsl:variable name="next-p" select="following-sibling::p[1]"/>
          <xsl:apply-templates
              select="following-sibling::*[self::ul or self::dl]
                      [empty($next-p) or . &lt;&lt; $next-p]"
              mode="examples-content"/>
        </xsl:when>
        <xsl:otherwise>
          <xsl:apply-templates
              select="following-sibling::dl[1]" mode="examples-content"/>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:variable>
    <xsl:if test="exists($content)">
      <h4>{normalize-space(.)}</h4>
      <xsl:apply-templates select="$content" mode="clean-content"/>
    </xsl:if>
  </xsl:template>

  <xsl:mode name="examples-content" on-no-match="shallow-copy"/>
  <xsl:template match="dl" mode="examples-content">
    <xsl:variable
        name="dd-nodes" select="dd[not(span[contains-token(@class, 'mw-empty-elt')])]"/>
    <xsl:if test="exists($dd-nodes)">
      <dl>
        <!-- [1], [1-2], [1, 2], [1.1], [1a] -->
        <xsl:for-each-group
            select="$dd-nodes"
            group-by="(text()/analyze-string(., '\[([\d\sa-z,.\-–?]+)\]')//fn:group)[1]">
          <xsl:sequence
              select="current-group()[string-length() =
                      min(current-group()/string-length())][1]"/>
        </xsl:for-each-group>
      </dl>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
