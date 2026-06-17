<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:map="http://www.w3.org/2005/xpath-functions/map"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:mode name="clean-content" on-no-match="shallow-copy"/>

  <xsl:template
      match="@typeof | @about | @id | @rel | @srcset | @resource |
             @*[starts-with(name(), 'data-')]"
      mode="clean-content"/>

  <!-- KOReader doesn't support `var()` CSS function -->
  <xsl:template match="@style" mode="clean-content">
    <xsl:attribute name="style"
                   select="replace(., 'var\([^,]+,\s*([^)]+)\s*\)', '$1')"/>
  </xsl:template>

  <!-- Remove category links -->
  <xsl:template match="link | audio | comment() | script" mode="clean-content"/>

  <!-- Remove a elements but keep their text content -->
  <xsl:template match="a" mode="clean-content">
    <xsl:apply-templates mode="clean-content"/>
  </xsl:template>

  <!-- Remove hidden elements -->
  <xsl:template match="*[contains(@style, 'display: none;')]" mode="clean-content"/>

  <xsl:template match="sup[contains(@class, 'mw-ref')]" mode="clean-content"/>
  <xsl:template match="figure[@typeof = 'mw:File/Thumb']" mode="clean-content"/>

  <!-- Remove <gallery> image list
       https://www.mediawiki.org/wiki/Help:Images#Rendering_a_gallery_of_images-->
  <xsl:template
      match="ul[contains-token(@class, 'gallery')]" mode="clean-content"/>

  <xsl:template
      match="li[contains-token(@class, 'mw-empty-elt')]" mode="clean-content"/>
</xsl:stylesheet>
