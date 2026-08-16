<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz"
    exclude-result-prefixes="#all">
  <xsl:template match="dl" mode="pron">
    <xsl:param name="pos-index" as="xs:integer"/>
    <xsl:variable
        name="ipa-dd"
        select="(let $matched-dd := myfn:match-dd(dd, $pos-index)
                return if ($matched-dd/dl) then $matched-dd//dd else $matched-dd)
                [a[@title = ('Aneks:IPA', 'Aneks:pinyin')]]"/>
    <xsl:if test="$ipa-dd">
      <dl>
        <xsl:apply-templates select="$ipa-dd" mode="clean-content"/>
      </dl>
    </xsl:if>
  </xsl:template>

  <!-- remove sound file -->
  <xsl:template match="span[contains-token(@typeof, 'mw:Extension/phonos')]"
                mode="clean-content"/>
  <xsl:template
      match="text()[normalize-space() = ',' and
             preceding-sibling::*[1]
             [self::span[contains-token(@typeof, 'mw:Extension/phonos')]]]"
      mode="clean-content"/>
</xsl:stylesheet>
