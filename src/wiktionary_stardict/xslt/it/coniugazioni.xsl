<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output method="json" indent="no" encoding="UTF-8"/>

  <xsl:include href="../utils.xsl"/>

  <xsl:template match="/">
    <xsl:variable name="forms" as="xs:string*">
      <xsl:for-each select=".//td">
        <xsl:for-each-group select="node()" group-adjacent="boolean(self::br)">
          <xsl:if test="not(current-grouping-key())">
            <xsl:variable name="new-e">
              <xsl:copy-of select="current-group()"/>
            </xsl:variable>
            <xsl:sequence select="myfn:get-element-forms($new-e/a[last()])"/>
          </xsl:if>
        </xsl:for-each-group>
      </xsl:for-each>
    </xsl:variable>
    <xsl:sequence select="array{distinct-values($forms[. != ''])}"/>
  </xsl:template>
</xsl:stylesheet>
