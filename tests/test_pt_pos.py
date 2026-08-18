from utils import XMLTestCase


class PtPOSTestCase(XMLTestCase):
    edition = "pt"

    def test_short_example(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>palavra</title></head>
<body>
<section><h1><style data-mw='{"parts":[{"template":{"target":{"wt":"-pt-"}}}]}'></style><span><span><span><span><a>Português</a></span></span></span></span></h1>
<section><h2><span>Substantivo</span></h2>
<p><b>pa.<u>la</u>.vra</b>, <i>feminino</i>, <span>(</span><span class="escopo"><i>Datação:</i></span><span> século XIII)</span></p>
<ol><li>gloss<ul><li><i>Com a <b>palavra</b>, o ilustre senador do Maranhão!</i></li>
<li><i>Só você fala, os outros também querem ter a <b>palavra</b>.</i></li></ul></li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pt">
<h4><span>Substantivo</span></h4>
<p><b>pa.<u>la</u>.vra</b>, <i>feminino</i>, <span>(</span><span class="escopo"><i>Datação:</i></span><span> século XIII)</span></p>
<ol><li>gloss<ul><li><i>Com a <b>palavra</b>, o ilustre senador do Maranhão!</i></li></ul></li></ol>
</section>""",
                    "forms": ["palavra"],
                    "lang": "Português",
                    "lemma_code": "pt",
                },
            ],
        )
