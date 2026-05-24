<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:map="http://www.w3.org/2005/xpath-functions/map"
    xmlns:myfn="https://github.com/xxyzz">
  <xsl:variable
      name="allowed-languages"
      select="('漢語',
              '朝鮮語',
              '意大利語',
              '拉丁語',
              '西班牙語',
              '德語',
              '英語',
              '葡萄牙語',
              '俄語',
              '瑞典語',
              '日語',
              '法語',
              '越南語',
              '波蘭語',
              '芬蘭語',
              '羅馬尼亞語',
              '土耳其語',
              '希臘語',
              '烏克蘭語',
              '匈牙利語',
              '馬其頓語',
              '荷蘭語',
              '拉脫維亞語',
              '阿塞拜疆語',
              '阿拉伯語',
              '冰島語',
              '立陶宛語',
              '泰盧固語',
              '印地語',
              '書面挪威語',
              '滿語',
              '壯語',
              '新挪威語',
              '波斯語',
              '丹麥語',
              '藏語',
              '印尼語',
              '蒙古語',
              '泰語',
              '希伯來語',
              '緬甸語',
              '孟加拉語')"/>

  <xsl:variable
      name="lang-map"
      select="map {
              '汉语': '漢語',
              '朝鲜语': '朝鮮語',
              '意大利语': '意大利語',
              '拉丁语': '拉丁語',
              '西班牙语': '西班牙語',
              '德语': '德語',
              '英语': '英語',
              '葡萄牙语': '葡萄牙語',
              '俄语': '俄語',
              '瑞典语': '瑞典语',
              '日语': '日語',
              '法语': '法語',
              '越南语': '越南語',
              '波兰语': '波蘭語',
              '芬兰语': '芬蘭語',
              '荷兰语': '荷蘭語',
              '书面挪威语': '書面挪威語',
              '新挪威语': '新挪威語',
              '泰语': '泰語',
              '希伯来语': '希伯來語'}"/>

  <xsl:function name="myfn:combine-lang" as="xs:string">
    <xsl:param name="lang" as="xs:string"/>
    <xsl:sequence select="if (map:contains($lang-map, $lang))
                          then $lang-map($lang) else $lang"/>
  </xsl:function>
</xsl:stylesheet>
