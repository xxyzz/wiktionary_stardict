from unittest import TestCase


class LanguageTest(TestCase):
    def test_languages(self):
        import json
        from pathlib import Path

        from mediawiki_langcodes import name_to_code
        from saxonche import PySaxonProcessor

        proc = PySaxonProcessor(license=False)
        xsltproc = proc.new_xslt30_processor()
        xslt = """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
    version="3.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:array="http://www.w3.org/2005/xpath-functions/array"
    expand-text="yes"
    exclude-result-prefixes="#all">
  <xsl:output method="json" indent="no" encoding="UTF-8"/>
  <xsl:template match="/">
    <xsl:variable name="var"
                  select="doc('{0}')//xsl:variable[@name = 'allowed-languages']"/>
    <xsl:choose>
      <xsl:when test="$var">
        <xsl:variable name="languages" as="item()*">
          <xsl:evaluate xpath="string($var/@select)"/>
        </xsl:variable>
        <xsl:sequence select="array{{$languages}}"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:sequence select="array{{()}}"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>
</xsl:stylesheet>"""

        for config in Path("src/wiktionary_stardict/xslt").glob("**/config.xsl"):
            executable = xsltproc.compile_stylesheet(
                stylesheet_text=xslt.format(config.absolute().as_uri())
            )
            result = executable.transform_to_string(
                xdm_node=proc.parse_xml(xml_text="<root/>")
            )
            languages = json.loads(result)
            name_sets = set()
            code_sets = set()
            edition = config.parent.name
            for language_name in languages:
                if language_name in name_sets:
                    self.assertEqual(
                        f"Duplicated {edition} language: {language_name}", ""
                    )
                else:
                    name_sets.add(language_name)
                    lemma_code = name_to_code(language_name, edition)
                    if lemma_code == "":
                        self.assertEqual(f"No {edition} language: {language_name}", "")
                    elif lemma_code in code_sets:
                        self.assertEqual(
                            f"Conflict code {edition=} {language_name=} {lemma_code=}",
                            "",
                        )
                    else:
                        code_sets.add(lemma_code)
