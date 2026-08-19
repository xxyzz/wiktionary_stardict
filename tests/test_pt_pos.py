from utils import XMLTestCase


class PtPOSTestCase(XMLTestCase):
    edition = "pt"

    def test_short_example(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>palavra</title></head>
<body>
<section></section>
<section><h1><style data-mw='{"parts":[{"template":{"target":{"wt":"-pt-"}}}]}'>.mw-parser-output</style><span class="cabecalhoIdioma"><span><span><span><a>Português</a></span></span></span></span></h1>
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
                },
            ],
        )

    def test_b_form_of(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>ajisonbyō</title></head>
<body>
<section><h1>Japonês</h1>
<section><h2>Transliteração</h2>
<p><b>ajisonbyō</b></p>
<ol><li><a>transliteração</a> de <b><a>アジソン病</a></b></li></ol>
</section></section></body></html>""",
            [{"form_of_only": True, "form_of_targets": ["アジソン病"]}],
        )

    def test_a_form_of(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>ganbatte</title></head>
<body>
<section><h1>Japonês</h1>
<section><h2>Transliteração</h2>
<p><b>ganbatte</b></p>
<ol><li>transliteração de <a>がんばって</a></li></ol>
</section></section></body></html>""",
            [{"form_of_only": True, "form_of_targets": ["がんばって"]}],
        )

    def test_split_lang_name(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>april</title></head>
<body>
<section><h1><span><span class="lnklng"><a>Holandês</a>/<a>Neerlandês</a></span></span></h1>
<section><h2>Substantivo</h2>
<p><b>april</b></p>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [{"lang": "Holandês"}],
        )
