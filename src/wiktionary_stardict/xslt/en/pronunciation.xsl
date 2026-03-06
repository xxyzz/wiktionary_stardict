<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="pron">
    <xsl:param name="pos"/>
    <xsl:variable name="pron-list">
      <xsl:apply-templates select="ul" mode="pron-ul"/>
    </xsl:variable>
    <xsl:variable name="pos-pron">
      <xsl:sequence
	  select="$pron-list//li[replace(string-join(text(), ''), ':\s*$', '') = $pos]/ul"/>
    </xsl:variable>
    <xsl:copy-of select="if ($pos-pron/*) then $pos-pron else $pron-list "/>
  </xsl:template>

  <xsl:template match="ul" mode="pron-ul">
    <xsl:variable name="lists">
      <xsl:apply-templates select="li" mode="pron-ul"/>
    </xsl:variable>
    <xsl:if test="$lists/*">
      <ul><xsl:copy-of select="$lists"/></ul>
    </xsl:if>
  </xsl:template>

  <xsl:template match="li" mode="pron-ul">
    <xsl:if test=".//a[@title='Wiktionary:International Phonetic Alphabet'] and not(table[contains(@class, 'audiotable')])">
      <li>
	<xsl:apply-templates mode="pron-ul"/>
      </li>
    </xsl:if>
  </xsl:template>

  <xsl:template match="sup[normalize-space(.) = '(key)']" mode="pron-ul"/>

  <xsl:template match="*" mode="pron-ul">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>
</xsl:stylesheet>
