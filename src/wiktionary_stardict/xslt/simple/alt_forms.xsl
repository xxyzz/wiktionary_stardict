<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

 <xsl:function name="myfn:get-alt-form-section" as="element(section)*">
    <xsl:param name="section" as="element(section)"/>
    <xsl:sequence
        select="$section/preceding-sibling::section
                [normalize-space(h3) = 'Other spellings']"/>
 </xsl:function>

 <xsl:template match="section" mode="alt-form">
   <xsl:if test="ul">
     <section>
       <xsl:apply-templates select="h3" mode="section-heading"/>
       <xsl:apply-templates select="ul" mode="clean-content"/>
     </section>
   </xsl:if>
 </xsl:template>
</xsl:stylesheet>
