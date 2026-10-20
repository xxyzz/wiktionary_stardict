from unittest import TestCase


class XMLTestCase(TestCase):
    maxDiff = None
    edition = "en"
    xsl_file = "main.xsl"

    @classmethod
    def setUpClass(cls):
        from saxonche import PySaxonProcessor

        from wiktionary_stardict.main import config_proc, get_xsl_path

        cls.proc = PySaxonProcessor(license=False)
        config_proc(cls.proc)
        xsltproc = cls.proc.new_xslt30_processor()
        cls.executable = xsltproc.compile_stylesheet(
            stylesheet_file=get_xsl_path(cls.edition, cls.xsl_file)
        )
        cls.math_xsl_exec = xsltproc.compile_stylesheet(
            stylesheet_file=get_xsl_path("", "math_svg.xsl")
        )
        cls.link_xsl_exec = xsltproc.compile_stylesheet(
            stylesheet_file=get_xsl_path("", "mod_link.xsl")
        )

    def assertXMLEqual(self, output, expected):
        from bs4 import BeautifulSoup

        self.assertEqual(
            BeautifulSoup(output, "html.parser").prettify(),
            BeautifulSoup(expected, "html.parser").prettify(),
        )

    def transform_zim(self, input_html: str):
        import json

        zim_doc = self.proc.parse_xml(xml_text=input_html)
        zim_result = self.executable.transform_to_string(xdm_node=zim_doc)
        return json.loads(zim_result)

    def transform_input(self, input_html: str):
        import json

        from wiktionary_stardict.main import transform

        list_data = transform(
            {"name": "test", "html": input_html},
            self.proc,
            self.executable,
            self.math_xsl_exec,
            None,
        )
        for data in list_data:
            if "def" in data:
                doc = self.proc.parse_xml(xml_text=data["def"])
                self.link_xsl_exec.set_parameter(
                    "data",
                    self.proc.make_string_value(
                        json.dumps(data["links"], ensure_ascii=False)
                    ),
                )
                data["def"] = self.link_xsl_exec.transform_to_string(xdm_node=doc)
        return list_data

    def assertTransformEqual(self, input_html, expected_list, prettify=True):
        output = self.transform_input(input_html)
        if len(expected_list) == 0:
            self.assertTrue(len(output) == 0, "Shouldn't have output data")
        else:
            self.assertTrue(len(output) > 0, "No output data")
            for result_data, expected_data in zip(output, expected_list):
                for key in expected_data.keys():
                    if key == "def" and prettify:
                        self.assertXMLEqual(result_data["def"], expected_data["def"])
                    else:
                        self.assertEqual(result_data[key], expected_data[key])
