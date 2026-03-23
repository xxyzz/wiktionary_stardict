import unittest


class XMLTestCase(unittest.TestCase):
    maxDiff = None
    edition = "en"
    xsl_file = "main.xsl"

    def setUp(self):
        from saxonche import PySaxonProcessor

        from wiktionary_stardict.main import get_xsl_path

        self.proc = PySaxonProcessor(license=False)
        xsltproc = self.proc.new_xslt30_processor()
        self.executable = xsltproc.compile_stylesheet(
            stylesheet_file=get_xsl_path(self.edition, self.xsl_file)
        )

    def assertXMLEqual(self, output, expected):
        from bs4 import BeautifulSoup

        self.assertEqual(
            BeautifulSoup(output, "html.parser").prettify(),
            BeautifulSoup(expected, "html.parser").prettify(),
        )

    def transform(self, input_html):
        import json

        document = self.proc.parse_xml(xml_text=input_html)
        return json.loads(self.executable.transform_to_string(xdm_node=document))

    def assertTransformEqual(self, input_html, expected_list):
        output = self.transform(input_html)
        if len(expected_list) == 0:
            self.assertTrue(len(output) == 0)
        elif len(output) == 0:
            self.assertTrue(False)
        else:
            for result_data, expected_data in zip(output, expected_list):
                for key in expected_data.keys():
                    if key == "def":
                        self.assertXMLEqual(result_data["def"], expected_data["def"])
                    else:
                        self.assertEqual(result_data[key], expected_data[key])
