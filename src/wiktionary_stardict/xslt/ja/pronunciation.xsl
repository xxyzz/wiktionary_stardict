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
      <xsl:when test="$language = ('日本語', '古典日本語')">
        <xsl:apply-templates
            select="span[@data-mw and myfn:is-template(@data-mw,
                    ('ja-pron', 'ja-accent-common'))]/following-sibling::ul[1]"
            mode="ja-pron"/>
      </xsl:when>
      <xsl:when test="$language = '中国語'">
        <xsl:apply-templates
            select="span[@data-mw and myfn:is-template(@data-mw, 'cmn-pron')]/
                    following-sibling::ul[1]/li[1]"
            mode="zh-pron"/>
      </xsl:when>
      <xsl:when test="$language = 'タイ語'">
        <xsl:apply-templates
            select="table[@data-mw and myfn:is-template(@data-mw, 'th-pron')]"
            mode="th-pron"/>
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

  <!-- '分綴:' from Template:es-pr Template:hyphenation -->
  <xsl:template match="li" mode="pron-ul">
    <xsl:if
        test="not(table[contains-token(@class, 'audiotable')]) and
              (.//a[@title = 'w:国際音声記号'] or
              .//text()[normalize-space() = '分綴:'] or
              .//span[starts-with(normalize-space(), '分綴:')])">
      <li>
        <xsl:apply-templates mode="pron-ul"/>
      </li>
    </xsl:if>
  </xsl:template>

  <xsl:template match="dl" mode="pron-ul">
    <xsl:variable name="lists">
      <xsl:apply-templates select="dd" mode="pron-ul"/>
    </xsl:variable>
    <xsl:if test="$lists/*">
      <dl><xsl:copy-of select="$lists"/></dl>
    </xsl:if>
  </xsl:template>

  <xsl:template match="dd" mode="pron-ul">
    <xsl:if test="not(table[contains-token(@class, 'audiotable')])">
      <dd><xsl:apply-templates mode="pron-ul"/></dd>
    </xsl:if>
  </xsl:template>

  <xsl:template match="*" mode="pron-ul">
    <xsl:apply-templates select="." mode="clean-content"/>
  </xsl:template>

  <xsl:template match="li" mode="zh-pron">
    <xsl:variable name="nodes">
      <xsl:apply-templates select="text() | ul[1] | dl[1]" mode="zh-pron-li"/>
    </xsl:variable>
    <ul>
      <li>
        <xsl:apply-templates select="$nodes" mode="clean-content"/>
      </li>
    </ul>
  </xsl:template>
  <xsl:mode name="zh-pron-li" on-no-match="shallow-copy"/>
  <xsl:template
      match="dd[table[contains-token(@class, 'audiotable')]]" mode="zh-pron-li"/>

  <xsl:template match="ul" mode="ja-pron">
    <xsl:variable name="li">
      <xsl:apply-templates select="li" mode="ja-pron-li"/>
    </xsl:variable>
    <ul>
      <xsl:apply-templates select="$li" mode="clean-content"/>
    </ul>
  </xsl:template>
  <xsl:mode name="ja-pron-li" on-no-match="shallow-copy"/>
  <xsl:template
      match="li[table[contains-token(@class, 'audiotable')]]" mode="ja-pron-li"/>

  <xsl:template match="table" mode="th-pron">
    <xsl:variable name="ipa-th" select=".//tr/th[a[@title = 'w:国際音声記号']]"/>
    <xsl:if test="$ipa-th">
      <ul><li>IPA: <xsl:apply-templates
      select="$ipa-th/following-sibling::td/span[contains-token(@class, 'IPA')]"
      mode="clean-content"/>
      </li></ul>
    </xsl:if>
  </xsl:template>
</xsl:stylesheet>
