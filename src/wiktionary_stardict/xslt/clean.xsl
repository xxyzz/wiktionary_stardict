<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:map="http://www.w3.org/2005/xpath-functions/map"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <!-- Remove attributes except class and style -->
  <xsl:template match="*" mode="clean-content">
    <xsl:element name="{name()}">
      <xsl:copy-of
          select="@*[not(name() = ('typeof', 'about', 'id', 'rel', 'srcset', 'resource')
                  or starts-with(name(), 'data-'))]"/>
      <xsl:apply-templates mode="clean-content"/>
    </xsl:element>
  </xsl:template>

  <!-- Remove category links -->
  <xsl:template match="link" mode="clean-content"/>

  <!-- Remove a elements but keep their text content -->
  <xsl:template match="a" mode="clean-content">
    <xsl:apply-templates mode="clean-content"/>
  </xsl:template>

  <!-- Copy text nodes as-is -->
  <xsl:template match="text()" mode="clean-content">
    <xsl:copy/>
  </xsl:template>

  <!-- Remove hidden elements -->
  <xsl:template match="*[contains(@style, 'display: none;')]" mode="clean-content"/>

  <xsl:template match="sup[contains(@class, 'mw-ref')]" mode="clean-content"/>
  <xsl:template match="figure[@typeof = 'mw:File/Thumb']" mode="clean-content"/>
  <xsl:template match="audio" mode="clean-content"/>

  <!-- Remove "audio" element expanded from <score>
       https://www.mediawiki.org/wiki/Extension:Score -->
  <xsl:template
      match="div[contains-token(@class, 'mw-ext-score')]/div[audio]"
      mode="clean-content"/>

  <!-- Remove <gallery> image list
       https://www.mediawiki.org/wiki/Help:Images#Rendering_a_gallery_of_images-->
  <xsl:template
      match="ul[contains-token(@class, 'gallery')]" mode="clean-content"/>

  <xsl:template
      match="li[contains-token(@class, 'mw-empty-elt')]" mode="clean-content"/>
</xsl:stylesheet>
