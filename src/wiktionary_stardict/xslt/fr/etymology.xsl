<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="etymology">
    <xsl:param name="pos-ids" as="xs:string*"/>
    <xsl:variable
        name="dl-elements"
        select="dl[not(.//link[contains-token(@rel, 'mw:PageProp/Category') and
                starts-with(@href,
                './Catégorie:Wiktionnaire:Étymologies_manquantes_en')])]"/>
    <xsl:if test="$dl-elements">
      <xsl:variable
          name="matched-dd"
          select="($dl-elements/dd[some $id in $pos-ids satisfies
                  i/a[contains-token(@class, 'mw-selflink-fragment') and
                      ends-with(@href, '#' || $id)]])[1]"/>
      <xsl:variable name="content">
        <xsl:choose>
          <xsl:when test="$matched-dd">
            <dl>
              <xsl:copy-of select="$matched-dd"/>
            </dl>
          </xsl:when>
          <xsl:otherwise>
            <xsl:copy-of select="$dl-elements"/>
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
