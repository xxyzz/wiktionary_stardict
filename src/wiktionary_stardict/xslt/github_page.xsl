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
        <title>Wiktionary Stardict</title>
        <xsl:element name="style" expand-text="no">
          .files {display: none;}
          .active {display: initial;}
        </xsl:element>
      </head>
      <body>
        <h1>Wiktionary Stardict</h1>
        <label for="edition">Choose Wiktionary edition:</label>
        <select id="edition">
          <xsl:for-each select="map:keys($assets)">
            <xsl:sort select="."/>
            <option value="{.}">
              <xsl:if test=". = 'English'">
                <xsl:attribute name="selected"/>
              </xsl:if>
              <xsl:value-of select="."/>
            </option>
          </xsl:for-each>
        </select>

        <xsl:for-each select="map:keys($assets)">
          <xsl:variable name="lang" select="."/>
          <xsl:variable name="files" select="$assets($lang)"/>

          <div id="{$lang}"
               class="{if ($lang = 'English') then 'files active' else 'files'}">
            <ul>
              <xsl:for-each select="1 to array:size($files)">
                <xsl:variable name="file" select="$files(.)"/>
                <li>
                  <a href="{$file?url}">
                    <xsl:value-of select="$file?name"/>
                  </a>
                </li>
              </xsl:for-each>
            </ul>
          </div>
        </xsl:for-each>

        <p>Create date: {$json-data?date}</p>
        <p>Source code: <a href="https://github.com/xxyzz/wiktionary_stardict">wiktionary_stardict</a></p>
        <p>Please donate on <a href="https://liberapay.com/xxyzz/donate">Liberapay</a> or <a href="https://paypal.me/worddumb">PayPal</a> to support this project.</p>

        <xsl:element name="script" expand-text="no">
            document.getElementById("edition").addEventListener(
              "change",
              function(event) {
                document.querySelectorAll(".files").forEach(l => {
                  if (l.id == event.target.value) {
                    l.classList.add("active");
                  } else {
                    l.classList.remove("active");
                  }
                });
              }
            );
        </xsl:element>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
