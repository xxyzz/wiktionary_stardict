import unittest


class XMLTestCase(unittest.TestCase):
    maxDiff = None
    edition = "en"

    def setUp(self):
        from saxonche import PySaxonProcessor

        from wiktionary_stardict.main import get_xsl_path

        self.proc = PySaxonProcessor(license=False)
        self.xsltproc = self.proc.new_xslt30_processor()
        self.xsl_path = get_xsl_path(self.edition)

    def pretty_output(self, xml):
        import html

        from bs4 import BeautifulSoup

        soup = BeautifulSoup(xml, "xml")
        def_node = soup.find("definition")
        html_soup = BeautifulSoup(html.unescape(def_node.string), "html.parser")
        def_node.clear()
        def_node.append(html_soup)
        return soup.prettify()

    def assertXMLEqual(self, actual, expected):
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(expected, "xml")
        self.assertEqual(self.pretty_output(actual), soup.prettify())

    def assertTransformEqual(self, input_html, expected_list):
        import json

        document = self.proc.parse_xml(xml_text=input_html)
        executable = self.xsltproc.compile_stylesheet(stylesheet_file=self.xsl_path)
        output = json.loads(executable.transform_to_string(xdm_node=document))
        if len(expected_list) == 0:
            self.assertTrue(len(output) == 0)
        else:
            for (_, output_xml), expected_xml in zip(output, expected_list):
                self.assertXMLEqual(output_xml, expected_xml)
