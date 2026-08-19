from utils import XMLTestCase


class PtFormsTestCase(XMLTestCase):
    edition = "pt"

    def test_flex_pt_subst_completa(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>parvo</title></head>
<body>
<section><h1>Português</h1>
<section><h2>Substantivo</h2>
<table><tbody><tr>
<td><span class="lnkprt"><a>parva</a></span>/<span class="lnkprt"><a>párvoa</a></span></td><td><span class="lnkprt"><a>-</a></span></td></tr>
</tbody></table>
<p><b>par.vo</b></p>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [{"forms": ["parvo", "parva", "párvoa"]}],
        )

    def test_conj_pt(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>ababalhar</title></head>
<body>
<section><h1>Português</h1>
<section><h2>Verbo</h2>
<p><b>a.ba.ba.<u>lhar</u></b></p>
<ol><li>gloss</li></ol>
<section><h3>Conjugação</h3>
<div><table><tbody><tr><td><a>ababalhando</a></td>
<th style="background-color: #DDD;"><b>Particípio</b></th>
<td>ababalhado</td></tr></tbody></table>
<table><tbody><tr><td><a>ababalhamos</a><sup>1</sup> /<br/><a>ababalhámos</a><sup>2</sup></td></tr></tbody></table>
</div>
</section></section></section></body></html>""",
            [
                {
                    "forms": [
                        "ababalhar",
                        "ababalhando",
                        "ababalhado",
                        "ababalhamos",
                        "ababalhámos",
                    ]
                }
            ],
        )

    def test_conj_en(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>rede</title></head>
<body>
<section><h1>Inglês</h1>
<section><h2>Verbo</h2>
<p><b>rede</b></p>
<ol><li>gloss</li></ol>
<section><h3>Conjugação</h3>
<table><tbody><tr><td><sup>Passado simples:</sup>
<dl><dd><b><a>red</a></b>/<b><a>redd</a></b></dd></dl></td></tr></tbody></table>
</section></section></section></body></html>""",
            [{"forms": ["rede", "red", "redd"]}],
        )

    def test_alt_form(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Costa de Ivor</title></head>
<body>
<section><h1>Língua Franca Nova</h1>
<section><h2>Locução substantiva</h2>
<p><b>Costa de Ivor</b></p>
<ol><li>gloss</li></ol></section>
<section><h2>Variante</h2>
<table><tbody><tr><td><ul><li><a>Коста де Ивор</a> <i>(Em cirílico)</i></li></ul></td></tr></tbody></table>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pt">
<h4>Locução substantiva</h4>
<p><b>Costa de Ivor</b></p>
<ol><li>gloss</li></ol>
<section><h4>Variante</h4>
<ul><li>Коста де Ивор <i>(Em cirílico)</i></li></ul>
</section></section>""",
                    "forms": ["Costa de Ivor", "Коста де Ивор"],
                }
            ],
        )

    def test_degree_forms(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>grande</title></head>
<body>
<section><h1>Português</h1>
<section><h2>Adjetivo</h2>
<p><b>grande</b></p>
<ol><li>gloss</li></ol>
<section><h3>Graus</h3>
<ul><li><b>comparativo de superioridade</b>: <a>maior</a> do que</li>
<li><b>superlativo absoluto sintético</b>: <a>grandíssimo</a></li>
<li><b>superlativo relativo de superioridade</b>: maior</li></ul>
</section></section></section></body></html>""",
            [{"forms": ["grande", "maior", "grandíssimo"]}],
        )
