<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:map="http://www.w3.org/2005/xpath-functions/map"
    xmlns:array="http://www.w3.org/2005/xpath-functions/array"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output method="html" html-version="5" indent="yes" encoding="UTF-8"/>
  <xsl:param name="data"/>

  <xsl:template match="/">
    <xsl:variable name="json-data" select="parse-json($data)"/>
    <xsl:variable name="assets" select="$json-data?assets"/>

    <html lang="en" dir="ltr">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>Statistics</title>
        <meta name="color-scheme" content="light dark"/>
        <link href="./style.css" rel="stylesheet"/>
      </head>
      <body>
        <h1>Statistics</h1>
        <p>Creation date: <span id="date">{$json-data?date}</span></p>
        <p>
          <label for="edition">Choose Wiktionary edition: </label>
          <select autocomplete="off" id="edition">
            <xsl:for-each select="map:keys($assets)">
              <xsl:sort select="."/>
              <option value="{$json-data?gloss_codes(.)}">
                <xsl:if test=". = 'English'">
                  <xsl:attribute name="selected"/>
                </xsl:if>
                <xsl:value-of select="."/>
              </option>
            </xsl:for-each>
          </select>
        </p>
        <xsl:for-each select="map:keys($assets)">
          <xsl:variable name="gloss-code" select="$json-data?gloss_codes(.)"/>
          <p id="{$gloss-code}-options"
             class="{if ($gloss-code = 'en') then 'files active-option' else 'files'}">
            <label for="{$gloss-code}-select">Choose language: </label>
            <select
                autocomplete="off" class="language-options" id="{$gloss-code}-select">
              <xsl:for-each select="$assets(.)?*">
                <xsl:sort select="?name"/>
                <xsl:variable
                    name="lemma-code" select="$json-data?lemma_codes(?name)"/>
                <option value="{$lemma-code}">
                  <xsl:value-of select="?name"/>
                </option>
              </xsl:for-each>
            </select>
          </p>
        </xsl:for-each>
        <div style="width: 80%;margin: auto"><canvas id="chart"></canvas></div>
        <script defer="defer" type="module" src="./statistics.js"/>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
