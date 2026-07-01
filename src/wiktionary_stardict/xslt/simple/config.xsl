<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:map="http://www.w3.org/2005/xpath-functions/map">
  <xsl:variable
      name="unsupported-titles"
      select="map {
              'Unsupported titles/`lt`': '&lt;',
              'Unsupported titles/`gt`': '&gt;'}"/>
</xsl:stylesheet>
