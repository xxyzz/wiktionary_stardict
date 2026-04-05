<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="etymology">
    <xsl:param name="pos-id" as="xs:string?"/>
    <xsl:variable
        name="dl-element"
        select="dl[not(.//link[@rel = 'mw:PageProp/Category' and starts-with(@href,
                './Catégorie:Wiktionnaire:Étymologies_manquantes_en')])][1]"/>
    <xsl:if test="$dl-element">
      <xsl:variable
          name="matched-dd"
          select="$dl-element/dd[i/a[ends-with(@href, '#' || $pos-id)]]"/>
      <xsl:variable name="content">
        <xsl:choose>
          <xsl:when test="$matched-dd">
            <dl>
              <dd>
                <xsl:copy-of
                    select="$matched-dd/node()
                            [not(self::i and not(preceding-sibling::i))]"/>
              </dd>
            </dl>
          </xsl:when>
          <xsl:otherwise>
            <xsl:copy-of select="$dl-element"/>
          </xsl:otherwise>
        </xsl:choose>
      </xsl:variable>

      <section>
        <h4>Etymology</h4>
        <xsl:apply-templates select="$content" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
