<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <!-- https://sv.wiktionary.org/wiki/Wiktionary:Alla_språk_och_koder_med_antal_huvuduppslag -->
  <!-- https://sv.wiktionary.org/wiki/Mall:språkindex -->
  <xsl:variable
      name="allowed-languages"
      select="('Svenska',
              'Engelska',
              'Tyska',
              'Bokmål',
              'Danska',
              'Finska',
              'Franska',
              'Spanska',
              'Isländska',
              'Katalanska',
              'Nederländska',
              'Polska',
              'Ryska',
              'Albanska',
              'Esperanto',
              'Frisiska',
              'Italienska',
              'Japanska',
              'Jiddisch',
              'Nynorska',
              'Portugisiska',
              'Ukrainska')"/>
</xsl:stylesheet>
