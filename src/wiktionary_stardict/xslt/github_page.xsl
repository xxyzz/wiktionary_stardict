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
        <title>Wiktionary StarDict</title>
        <xsl:element name="style" expand-text="no">
          .files {display: none;}
          .active {display: initial;}
          .screenshot {float: right; width: 30%;}
        </xsl:element>
      </head>
      <body>
        <h1>Wiktionary StarDict</h1>
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
            <img class="screenshot" loading="lazy"
                 src="{$json-data?screenshots($lang)}"/>
            <ul>
              <xsl:for-each select="$files?*">
                <xsl:sort select="?name"/>
                <li>
                  <a href="{?url}">
                    <xsl:value-of select="?name"/>
                  </a>
                </li>
              </xsl:for-each>
            </ul>
          </div>
        </xsl:for-each>

        <p>Creation date: {$json-data?date}</p>
        <p>Source code: <a href="https://github.com/xxyzz/wiktionary_stardict">wiktionary_stardict</a></p>
        <p>Please donate via <a href="https://liberapay.com/xxyzz/donate">Liberapay</a> or <a href="https://paypal.me/worddumb">PayPal</a> to support this project.</p>

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

        <h2>Install fonts</h2>
        <h3>Pronunciation fonts</h3>
        <p>Download <a href="https://fonts.google.com/specimen/Gentium+Plus">Gentium Plus</a> font file <code>GentiumPlus-Regular.ttf</code> to <code>koreader/fonts</code> folder</p>
        <p>Download <a href="https://fonts.google.com/noto/specimen/Noto+Sans+Mono">Noto Sans Mono</a> font file <code>NotoSansMono-Regular.ttf</code> to <code>koreader/fonts</code> folder</p>
        <h3>CJK fonts</h3>
        <p>Download these <a href="https://github.com/notofonts/noto-cjk/releases">Noto Sans CJK</a> font files to <code>koreader/fonts</code> folder:</p>
        <ul>
          <li><code>NotoSansCJKtc-Regular.otf</code></li>
          <li><code>NotoSansCJKtc-Bold.otf</code></li>
          <li><code>NotoSansCJKsc-Regular.otf</code></li>
          <li><code>NotoSansCJKsc-Bold.otf</code></li>
          <li><code>NotoSansCJKjp-Regular.otf</code></li>
          <li><code>NotoSansCJKjp-Bold.otf</code></li>
          <li><code>NotoSansCJKkr-Regular.otf</code></li>
          <li><code>NotoSansCJKkr-Bold.otf</code></li>
        </ul>
        <h3>Tibetan fonts</h3>
        <p>Download these <a href="https://fonts.google.com/noto/specimen/Noto+Serif+Tibetan">Noto Serif Tibetan</a> font files to <code>koreader/fonts</code> folder:</p>
        <ul>
          <li><code>NotoSerifTibetan-Regular.ttf</code></li>
          <li><code>NotoSerifTibetan-Bold.ttf</code></li>
        </ul>
        <h3>Mongolian, Manchu fonts</h3>
        <p>Download <a href="https://fonts.google.com/noto/specimen/Noto+Sans+Mongolian">Noto Sans Mongolian</a> font file <code>NotoSansMongolian-Regular.ttf</code> to <code>koreader/fonts</code> folder</p>
        <h3>Devanagari fonts</h3>
        <p>Download these <a href="https://fonts.google.com/noto/specimen/Noto+Serif+Devanagari"> Noto Serif Devanagari</a> font files to <code>koreader/fonts</code> folder:</p>
        <ul>
          <li><code>NotoSerifDevanagari-Regular.ttf</code></li>
          <li><code>NotoSerifDevanagari-Bold.ttf</code></li>
        </ul>
        <h3>Arabic font</h3>
        <p>Download <a href="https://fonts.google.com/noto/specimen/Noto+Naskh+Arabic">Noto Naskh Arabic</a> font file <code>NotoNaskhArabic-Regular.ttf</code> to <code>koreader/fonts</code> folder</p>
        <h3>Hebrew font</h3>
        <p>Download <a href="https://fonts.google.com/noto/specimen/Noto+Sans+Hebrew"> Noto Sans Hebrew</a> font file <code>NotoSansHebrew-Regular.ttf</code> to <code>koreader/fonts</code> folder</p>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
