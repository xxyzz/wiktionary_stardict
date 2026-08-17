<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="pron">
    <xsl:variable name="contents" select="(.//li|p)[a[@title = 'Aiuto:IPA')]]"/>
    <xsl:if test="$contents">
      <ul>
        <xsl:for-each select="$contents">
          <xsl:choose>
            <xsl:when test="self::p">
              <li>
                <xsl:apply-templates select="node()" mode="clean-content"/>
              </li>
            </xsl:when>
            <xsl:otherwise>
              <xsl:apply-templates mode="clean-content"/>
            </xsl:otherwise>
          </xsl:choose>
        </xsl:for-each>
      </ul>
    </xsl:if>
  </xsl:template>

  <xsl:template
      match="span[@data-mw and myfn:is-template(@data-mw, 'Audio')]"
      mode="clean-content"/>
</xsl:stylesheet>
