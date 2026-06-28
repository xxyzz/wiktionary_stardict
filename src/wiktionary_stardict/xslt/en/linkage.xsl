<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="linkage">
    <xsl:variable name="lists" select=".//ul"/>
    <xsl:if test="$lists">
      <section>
        <xsl:apply-templates select="h3 | h4 | h5 | h6" mode="section-heading"/>
        <xsl:apply-templates select="$lists" mode="linkage"/>
      </section>
    </xsl:if>
  </xsl:template>

  <xsl:template match="ul" mode="linkage">
    <ul>
      <xsl:apply-templates select="li[position() lt 7]" mode="clean-content"/>
    </ul>
  </xsl:template>

  <xsl:function name="myfn:get-linkage-section" as="element(section)*">
    <xsl:param name="pos-section" as="element(section)"/>
    <xsl:param name="titles" as="xs:string*"/>
    <xsl:variable
        name="sections"
        select="$pos-section/(section | following-sibling::section)
                [normalize-space(h3|h4|h5|h6) = $titles]"/>
    <xsl:for-each-group select="$sections" group-by="normalize-space(h3|h4|h5|h6)">
      <xsl:sequence select="current-group()[1]"/>
    </xsl:for-each-group>
  </xsl:function>
</xsl:stylesheet>
