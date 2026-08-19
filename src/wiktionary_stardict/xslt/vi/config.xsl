<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:myfn="https://github.com/xxyzz">
  <xsl:variable
      name="allowed-languages"
      select="('Tiếng Anh',
              'Tiếng Pháp',
              'Tiếng Việt',
              'Tiếng Nga',
              'Tiếng Na Uy',
              'Tiếng Nhật',
              'Tiếng Tây Ban Nha',
              'Tiếng Trung Quốc',
              'Tiếng Hà Lan',
              'Tiếng Tày',
              'Tiếng Đức',
              'Tiếng Hungary',
              'Tiếng Uzbek',
              'Tiếng Bồ Đào Nha')"/>

  <xsl:function name="myfn:convert-lang" as="xs:string">
    <xsl:param name="lang" as="xs:string"/>
    <xsl:sequence
        select="if ($lang = 'Tiếng Quan Thoại') then 'Tiếng Trung Quốc' else $lang"/>
  </xsl:function>
</xsl:stylesheet>
