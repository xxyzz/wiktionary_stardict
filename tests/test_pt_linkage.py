from utils import XMLTestCase


class PtLinkageTestCase(XMLTestCase):
    edition = "pt"

    def test_nested_linkage_list(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>cão</title></head>
<body><section><h1>Português</h1>
<section><h2>Adjetivo</h2>
<p><b>cão</b></p>
<ol><li>gloss</li></ol>
<section><h3>Sinônimos</h3>
<ul><li>De <b>1</b> (animal mamífero, carnívoro e quadrúpede):
<ul><li>cachorro</li>
<li>perro</li>
<li><span>(</span><span class="escopo">Brasil, RS</span><span>)</span> cusco</li></ul></li>
<li>De <b>2</b> (parte da arma de fogo):
<ul><li>percussor</li></ul></li></ul>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pt">
<h4>Adjetivo</h4>
<p><b>cão</b></p>
<ol><li>gloss</li></ol>
<section><h4>Sinônimos</h4>
<ul><li>De <b>1</b> (animal mamífero, carnívoro e quadrúpede):
<ul><li>cachorro</li>
<li>perro</li>
<li><span>(</span><span class="escopo">Brasil, RS</span><span>)</span> cusco</li></ul></li>
<li>De <b>2</b> (parte da arma de fogo):
<ul><li>percussor</li></ul></li></ul>
</section></section>"""
                }
            ],
        )

    def test_p_table_in_linkage_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>dicionário</title></head>
<body><section><h1>Português</h1>
<section><h2>Substantivo</h2>
<p><b>dicionário</b></p>
<ol><li>gloss</li></ol>
<section><h3>Sinónimos/Sinônimos</h3>
<p>De <b>1</b> (coleção terminológica):</p>
<table><tbody><tr><td class="vtbm">
<ul><li><a>aurélio</a> (<span class="escopo">Brasil, informal</span>)</li></ul></td>
<td class="vtbm" align="left">
<ul><li><a>glossário</a></li></ul></td>
<td class="vtbm" align="left">
<ul><li><a>léxico</a></li></ul></td>
<td class="vtbm" align="left">
<ul><li><a>pai dos burros</a> (<span class="escopo">jocoso</span>)</li></ul></td></tr>
</tbody></table>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pt">
<h4>Substantivo</h4>
<p><b>dicionário</b></p>
<ol><li>gloss</li></ol>
<section><h4>Sinónimos/Sinônimos</h4>
<p>De <b>1</b> (coleção terminológica):</p>
<ul><li>aurélio (<span class="escopo">Brasil, informal</span>)</li></ul>
<ul><li>glossário</li></ul>
<ul><li>léxico</li></ul>
<ul><li>pai dos burros (<span class="escopo">jocoso</span>)</li></ul>
</section></section>"""
                }
            ],
        )

    def test_sub_linkage_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>pelúcia</title></head>
<body><section><h1>Português</h1>
<section><h2>Substantivo</h2>
<p><b>pelúcia</b></p>
<ol><li>gloss</li></ol>
<section><h3>Sinónimos/Sinônimos</h3>
<section><h4>De 1</h4>
<ul><li><span>(</span><span class="escopo">Portugal</span><span>)</span> peluche</li></ul>
</section></section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pt">
<h4>Substantivo</h4>
<p><b>pelúcia</b></p>
<ol><li>gloss</li></ol>
<section><h4>Sinónimos/Sinônimos</h4>
<section><h5>De 1</h5>
<ul><li><span>(</span><span class="escopo">Portugal</span><span>)</span> peluche</li></ul>
</section></section></section>"""
                }
            ],
        )
