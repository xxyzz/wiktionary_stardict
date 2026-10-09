<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="pron">
    <xsl:param name="use-h5" select="false()" as="xs:boolean"/>
    <xsl:variable name="contents">
      <xsl:apply-templates mode="pron-content"/>
    </xsl:variable>
    <xsl:if test="$contents//ul">
      <section>
        <xsl:apply-templates select="h2 | h3 | h4 | h5 | h6" mode="section-heading">
          <xsl:with-param name="use-h5" select="$use-h5"/>
        </xsl:apply-templates>
        <xsl:apply-templates
            select="$contents/*[self::ul or .//ul]" mode="clean-content"/>
      </section>
    </xsl:if>
  </xsl:template>

  <xsl:mode name="pron-content" on-no-match="shallow-copy"/>

  <xsl:template match="ul" mode="pron-content">
    <xsl:variable name="lists">
      <xsl:apply-templates select="li" mode="pron-content"/>
    </xsl:variable>
    <xsl:if test="$lists/*">
      <xsl:copy>
        <xsl:copy-of select="@*"/>
        <xsl:sequence select="$lists"/>
      </xsl:copy>
    </xsl:if>
  </xsl:template>

  <xsl:template match="li" mode="pron-content">
    <xsl:if
        test="exists(a[@title = ('AFI', 'SAMPA', 'X-SAMPA')] or
              text()[some $text in ('AFI:', 'X-SAMPA:')
              satisfies contains(., $text)])">
      <li>
        <xsl:apply-templates mode="pron-content"/>
      </li>
    </xsl:if>
  </xsl:template>

  <xsl:template match="section" mode="pron-content">
    <xsl:apply-templates select="." mode="pron">
      <xsl:with-param name="use-h5" select="true()"/>
    </xsl:apply-templates>
  </xsl:template>

  <xsl:template match="*[contains-token(@typeof, 'mw:File')]" mode="pron-content"/>
  <xsl:template match="*[contains-token(@rel, 'mw:MediaLink')]" mode="pron-content"/>
  <xsl:template match="sup" mode="pron-content"/>
</xsl:stylesheet>
