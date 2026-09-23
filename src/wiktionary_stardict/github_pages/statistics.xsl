<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:map="http://www.w3.org/2005/xpath-functions/map"
    xmlns:array="http://www.w3.org/2005/xpath-functions/array"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output method="html" html-version="5" indent="no" encoding="UTF-8"/>
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
        <link rel="icon" href="./favicon.ico"/>
        <link rel="apple-touch-icon" sizes="180x180" href="./apple-touch-icon.png"/>
      </head>
      <body>
        <h1>Statistics</h1>
        <p>Creation date: <span id="date"><a href="https://github.com/xxyzz/wiktionary_stardict/releases/tag/{$json-data?date}">{$json-data?date}</a></span></p>
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
          <p id="{$gloss-code}-options" class="files">
            <xsl:if test="$gloss-code != 'en'">
              <xsl:attribute name="hidden"/>
            </xsl:if>
            <label for="{$gloss-code}-select">Choose language: </label>
            <select
                autocomplete="off" class="language-options" id="{$gloss-code}-select">
              <xsl:for-each select="$assets(.)?*">
                <xsl:sort select="?name"/>
                <xsl:variable
                    name="lemma-code" select="$json-data?lemma_codes(?name)"/>
                <option value="{$lemma-code}">
                  <xsl:if test="$gloss-code = 'en' and $lemma-code = 'en'">
                    <xsl:attribute name="selected"/>
                  </xsl:if>
                  <xsl:value-of select="?name"/>
                </option>
              </xsl:for-each>
            </select>
          </p>
        </xsl:for-each>
        <div style="width: 80%;margin: auto"><canvas id="chart"></canvas></div>
        <script type="module" src="./statistics.js"/>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
