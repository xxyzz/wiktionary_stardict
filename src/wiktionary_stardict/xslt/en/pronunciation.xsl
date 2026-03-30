<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">

  <xsl:template match="section" mode="pron">
    <xsl:param name="language"/>
    <xsl:choose>
      <xsl:when test="$language = 'Japanese'">
        <xsl:apply-templates
            select="span[@data-mw and myfn:is-template(@data-mw,
                    ('ja-pron', 'ja-accent-dialectal'))]/following-sibling::ul[1]"
            mode="clean-content"/>
      </xsl:when>
      <xsl:when test="$language = 'Chinese'">
        <xsl:apply-templates
            select="div[@data-mw and myfn:is-template(@data-mw, 'zh-pron')]//ul[1]"
            mode="zh-pron"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:apply-templates select="ul" mode="pron-ul"/>
      </xsl:otherwise>
    </xsl:choose>
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
    <xsl:if test="not(table[contains-token(@class, 'audiotable')]) and
                  (.//a[@title = 'Wiktionary:International Phonetic Alphabet'] or
                  .//text()[normalize-space() = 'Syllabification:'] or
                  .//span[normalize-space() = 'Hyphenation:'])">
      <li>
        <xsl:apply-templates mode="pron-ul"/>
      </li>
    </xsl:if>
  </xsl:template>

  <xsl:template match="*" mode="pron-ul">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>

  <xsl:template match="ul" mode="zh-pron">
    <xsl:variable
        name="list"
        select="subsequence(.//dd[small/i/a[text() = ('Pinyin', 'Zhuyin')]], 1, 2)"/>
    <xsl:if test="$list/*">
      <dl>
        <xsl:apply-templates select="$list" mode="clean-content"/>
      </dl>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
