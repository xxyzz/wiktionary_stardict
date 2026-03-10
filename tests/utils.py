import unittest


class XMLTestCase(unittest.TestCase):
    maxDiff = None
    edition = "en"

    def setUp(self):
        from saxonche import PySaxonProcessor

        from wiktionary_stardict.main import get_xsl_path

        self.proc = PySaxonProcessor(license=False)
        xsltproc = self.proc.new_xslt30_processor()
        self.executable = xsltproc.compile_stylesheet(
            stylesheet_file=get_xsl_path(self.edition)
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
            for (_, output_forms, output_xml, output_images), (
                expected_forms,
                expected_xml,
                expected_images,
            ) in zip(output, expected_list):
                self.assertEqual(output_forms, expected_forms)
                self.assertXMLEqual(output_xml, expected_xml)
                self.assertEqual(output_images, expected_images)
