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
        <meta name="description" content="Wiktionary StarDict dictionaries for KOReader and other e-readers."/>
        <meta property="og:title" content="Wiktionary StarDict"/>
        <meta property="og:type" content="website"/>
        <meta name="color-scheme" content="light dark"/>
        <link href="./style.css" rel="stylesheet"/>
      </head>
      <body>
        <h1>Wiktionary StarDict</h1>
        <p>Wiktionary StarDict dictionaries for KOReader and other e-readers. Download from here or KOReader dictionary settings menu. Source code: <a href="https://github.com/xxyzz/wiktionary_stardict">xxyzz/wiktionary_stardict</a></p>
        <p>Read the <a href="./fonts.html">fonts document</a> of how to install required fonts.</p>
        <p>Creation date: {$json-data?date}</p>
        <p>Please donate via <a role="button" class="liberapay btn" href="https://liberapay.com/xxyzz/donate"><svg viewBox="0 0 80 80" height="16" width="16"><g transform="translate(-78.37-208.06)" fill="#1a171b"><path d="m104.28 271.1c-3.571 0-6.373-.466-8.41-1.396-2.037-.93-3.495-2.199-4.375-3.809-.88-1.609-1.308-3.457-1.282-5.544.025-2.086.313-4.311.868-6.675l9.579-40.05 11.69-1.81-10.484 43.44c-.202.905-.314 1.735-.339 2.489-.026.754.113 1.421.415 1.999.302.579.817 1.044 1.546 1.395.729.353 1.747.579 3.055.679l-2.263 9.278"></path><path d="m146.52 246.14c0 3.671-.604 7.03-1.811 10.07-1.207 3.043-2.879 5.669-5.01 7.881-2.138 2.213-4.702 3.935-7.693 5.167-2.992 1.231-6.248 1.848-9.767 1.848-1.71 0-3.42-.151-5.129-.453l-3.394 13.651h-11.162l12.52-52.19c2.01-.603 4.311-1.143 6.901-1.622 2.589-.477 5.393-.716 8.41-.716 2.815 0 5.242.428 7.278 1.282 2.037.855 3.708 2.024 5.02 3.507 1.307 1.484 2.274 3.219 2.904 5.205.627 1.987.942 4.11.942 6.373m-27.378 15.461c.854.202 1.91.302 3.167.302 1.961 0 3.746-.364 5.355-1.094 1.609-.728 2.979-1.747 4.111-3.055 1.131-1.307 2.01-2.877 2.64-4.714.628-1.835.943-3.858.943-6.071 0-2.161-.479-3.998-1.433-5.506-.956-1.508-2.615-2.263-4.978-2.263-1.61 0-3.118.151-4.525.453l-5.28 21.948"></path></g></svg><span>Liberapay</span></a> or <a role="button" class="paypal btn" href="https://paypal.me/worddumb"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16"><path d="M14.06 3.713c.12-1.071-.093-1.832-.702-2.526C12.628.356 11.312 0 9.626 0H4.734a.7.7 0 0 0-.691.59L2.005 13.509a.42.42 0 0 0 .415.486h2.756l-.202 1.28a.628.628 0 0 0 .62.726H8.14c.429 0 .793-.31.862-.731l.025-.13.48-3.043.03-.164.001-.007a.35.35 0 0 1 .348-.297h.38c1.266 0 2.425-.256 3.345-.91q.57-.403.993-1.005a4.94 4.94 0 0 0 .88-2.195c.242-1.246.13-2.356-.57-3.154a2.7 2.7 0 0 0-.76-.59l-.094-.061ZM6.543 8.82a.7.7 0 0 1 .321-.079H8.3c2.82 0 5.027-1.144 5.672-4.456l.003-.016q.326.186.548.438c.546.623.679 1.535.45 2.71-.272 1.397-.866 2.307-1.663 2.874-.802.57-1.842.815-3.043.815h-.38a.87.87 0 0 0-.863.734l-.03.164-.48 3.043-.024.13-.001.004a.35.35 0 0 1-.348.296H5.595a.106.106 0 0 1-.105-.123l.208-1.32z"/></svg> <span>PayPal</span></a> to support this project.</p>
        <p>
          <label for="edition">Choose Wiktionary edition: </label>
          <select autocomplete="off" id="edition">
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
        </p>

        <xsl:for-each select="map:keys($assets)">
          <xsl:variable name="lang" select="."/>
          <xsl:variable name="files" select="$assets($lang)"/>
          <xsl:variable name="lang_code" select="$json-data?gloss_codes($lang)"/>

          <div id="{$lang}"
               class="{if ($lang = 'English') then 'files active grid' else 'files grid'}">
            <picture class="screenshot">
              <source srcset="{$lang_code}.avif" type="image/avif"/>
              <img loading="lazy" src="{$lang_code}.png" alt="KOReader screenshot"/>
            </picture>
            <ul class="list">
              <xsl:for-each select="$files?*">
                <xsl:sort select="?name"/>
                <li>
                  <a lang="{$lang_code}" href="{?url}">{?name}</a>
                  <span> {?entries} entries, {?size}</span>
                </li>
              </xsl:for-each>
            </ul>
          </div>
        </xsl:for-each>

        <p><a href="./statistics.html">Statistics</a></p>
        <xsl:element name="script" expand-text="no">
          window.addEventListener("pageshow", () => {
            document.querySelector("#edition").value = "English";
          });

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
