<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    expand-text="yes"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="conj" as="xs:string*">
    <xsl:sequence select="for $span in .//span[contains-token(@class, 'form-of')]
                          return myfn:ruby_text($span)"/>
  </xsl:template>
</xsl:stylesheet>
