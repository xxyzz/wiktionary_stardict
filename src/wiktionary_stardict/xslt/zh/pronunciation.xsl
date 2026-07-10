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
      <xsl:when test="$language = '日語'">
        <xsl:apply-templates
            select="span[@data-mw and myfn:is-template(@data-mw,
                    ('ja-pron', 'ja-IPA', 'ja-accent-dialectal'))]/
                    following-sibling::ul[1]"
            mode="ja-pron"/>
      </xsl:when>
      <xsl:when test="$language = '漢語'">
        <xsl:apply-templates
            select="(div[contains-token(@class, 'zhpron')]//ul)[1]"
            mode="zh-pron"/>
      </xsl:when>
      <xsl:when test="$language = '藏語'">
        <xsl:apply-templates
            select="div[@data-mw and
                    myfn:is-template(@data-mw, ('bo-IPA', 'bo-pron'))]/ul[1]"
            mode="ja-pron"/>
      </xsl:when>
      <xsl:when test="$language = '泰語'">
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

  <xsl:template match="li" mode="pron-ul">
    <xsl:if
        test="not(table[contains-token(@class, 'audiotable')]) and
              (.//a[@title = 'Wiktionary:國際音標'] or
              .//text()[normalize-space() = ('音節化：', '聲調數字：')])">
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

  <xsl:template match="ul" mode="zh-pron">
    <xsl:variable name="li">
      <xsl:apply-templates select="li[1]" mode="zh-pron-li"/>
    </xsl:variable>
    <ul>
      <xsl:apply-templates select="$li" mode="clean-content"/>
    </ul>
  </xsl:template>
  <xsl:mode name="zh-pron-li" on-no-match="shallow-copy"/>
  <xsl:template match="dd[span[contains-token(@typeof, 'mw:File')]]" mode="zh-pron-li"/>

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
    <xsl:variable name="output">
      <xsl:apply-templates select="." mode="th-pron-tr"/>
    </xsl:variable>
    <xsl:apply-templates select="$output" mode="clean-content"/>
  </xsl:template>
  <xsl:mode name="th-pron-tr" on-no-match="shallow-copy"/>
  <xsl:template match="tr[normalize-space(th[1]) = '音頻']" mode="th-pron-tr"/>
  <xsl:template match="th/div[normalize-space(.) = 'edit']" mode="th-pron-tr"/>
  <xsl:template match="th/sup[normalize-space(.) = '(說明)']" mode="th-pron-tr"/>
  <xsl:template match="td/sup[normalize-space(.) = '(R)']" mode="th-pron-tr"/>
</xsl:stylesheet>
