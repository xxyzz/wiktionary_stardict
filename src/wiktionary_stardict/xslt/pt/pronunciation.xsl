<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="pron">
    <xsl:variable
        name="ipa-lists"
        select="ul/li[myfn:is-ipa-li(.)]"/>
    <xsl:variable
        name="child-sections"
        select="section[ul/li[myfn:is-ipa-li(.)]]"/>
    <xsl:if test="$ipa-lists or $child-sections">
      <section>
        <h4>Pronúncia</h4>
        <xsl:if test="$ipa-lists">
          <ul>
            <xsl:apply-templates select="$ipa-lists" mode="clean-content"/>
          </ul>
        </xsl:if>
        <xsl:for-each select="$child-sections">
          <section>
            <h5><xsl:apply-templates select="(h3|h4)/node()" mode="clean-content"/></h5>
            <xsl:variable name="content">
              <xsl:apply-templates
                  select="ul/li[myfn:is-ipa-li(.)]" mode="pron-li"/>
            </xsl:variable>
            <ul>
              <xsl:apply-templates select="$content" mode="clean-content"/>
            </ul>
          </section>
        </xsl:for-each>
      </section>
    </xsl:if>
  </xsl:template>

  <xsl:function name="myfn:is-ipa-li" as="xs:boolean">
    <xsl:param name="li" as="element(li)*"/>
    <xsl:sequence
        select="exists($li[a[@title = ('AFI', 'SAMPA', 'X-SAMPA')] or
                text()[some $text in ('AFI:', 'X-SAMPA:')
                satisfies contains(., $text)]])"/>
  </xsl:function>

  <xsl:template match="*[contains-token(@typeof, 'mw:File')]" mode="pron-li"/>
  <xsl:template match="*[contains-token(@rel, 'mw:MediaLink')]" mode="pron-li"/>
  <xsl:template match="sup" mode="pron-li"/>
  <xsl:mode name="pron-li" on-no-match="shallow-copy"/>
</xsl:stylesheet>
