from unittest import TestCase

from requests import Session

from wiktionary_stardict.mathjax import shutdown_node, start_node, tex2svg


class MathJaxTestCase(TestCase):
    maxDiff = None

    @classmethod
    def setUpClass(cls):
        cls.session = Session()
        cls.node_process = start_node()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        shutdown_node(cls.node_process)

    def test_chem(self):
        # en page "adipic acid"
        svg1 = tex2svg(
            self.session,
            {"name": "chem", "attrs": {}, "body": {"extsrc": "C4H8(COOH)2"}},
        )
        # en page "Michaelis-Menten equation"
        svg2 = tex2svg(
            self.session,
            {"name": "math", "attrs": {"chem": ""}, "body": {"extsrc": "C4H8(COOH)2"}},
        )
        self.assertEqual(svg1, svg2)
        self.assertIn(r"\mathrm", svg1)
        self.assertStartsWith(
            svg1, '<mjx-container class="MathJax" jax="SVG" overflow="overflow">'
        )

    def test_block_display(self):
        # en page "Mahler measure"
        self.assertStartsWith(
            tex2svg(
                self.session,
                {
                    "name": "math",
                    "attrs": {"display": "block"},
                    "body": {"extsrc": "M(p)"},
                },
            ),
            '<mjx-container class="MathJax" jax="SVG" overflow="overflow" display="true">',
        )
