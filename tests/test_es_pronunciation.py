from utils import XMLTestCase


class EsPronunciationTestCase(XMLTestCase):
    edition = "es"

    def test_pron_graf(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>acontecer</title></head>
<body>
<section><h2>Español</h2>
<table class="pron-graf toccolours" data-mw='{"parts":[{"template":{"target":{"wt":"pron-graf"}}}]}'>
<tbody><tr><td>acontecer</td></tr>
<tr>
<td><a><b>seseante</b></a> (<a title="Alfabeto Fonético Internacional">AFI</a>)</td>
<td>[akõn̪t̪eˈseɾ]<br/></td></tr>
<tr>
<td><b>silabación</b></td>
<td>a-con-te-cer</td></tr>
<tr>
<td><b>acentuación</b></td>
<td>aguda</td></tr>
</tbody></table>
<section><h3>Verbo intransitivo y terciopersonal</h3>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["acontecer"],
                    "def": """<section dir="ltr" lang="es">
<h4>Verbo intransitivo y terciopersonal</h4>
<ul>
<li><b>seseante</b> (AFI): [akõn̪t̪eˈseɾ]</li>
<li><b>silabación</b>: a-con-te-cer</li>
</ul>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>""",
                }
            ],
        )

    def test_pron_in_different_lang_sections(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>livre</title></head>
<body>
<section><h2>Francés</h2>
<table class="pron-graf toccolours" style="float: right;" typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"pron-graf"}}}]}'>
<tbody><tr><td colspan="2"><span>livre</span></td></tr>
<tr>
<td><a title="Wikcionario:Referencia/FR/Pronunciación"><b>pronunciación</b></a> (<a title="Alfabeto Fonético Internacional">AFI</a>)</td>
<td>[(ˈ)li(ː.)vʁ(ə)] <span class="ext-phonos" typeof="mw:Extension/phonos">phonos</span><br/></td></tr>
</tbody></table>
<section><h3>Sustantivo masculino</h3>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>
</section>

<section><h2>Portugués</h2>
<table class="pron-graf toccolours" style="float: right;" typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"pron-graf"}}}]}'>
<tbody><tr><td colspan="2"><span>livre</span></td></tr>
<tr>
<td><a><b>Portugal</b></a> (<a title="Alfabeto Fonético Internacional">AFI</a>)</td>
<td>[ˈli.vɾɨ] </td></tr>
</tbody></table>
<section><h3>Adjetivo</h3>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="es">
<h4>Sustantivo masculino</h4>
<ul>
<li><b>pronunciación</b> (AFI): [(ˈ)li(ː.)vʁ(ə)]</li>
</ul>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>""",
                },
                {
                    "def": """<section dir="ltr" lang="es">
<h4>Adjetivo</h4>
<ul>
<li><b>Portugal</b> (AFI): [ˈli.vɾɨ]</li>
</ul>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>""",
                },
            ],
        )

    def test_two_ipa(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Shintoismus</title></head>
<body>
<section><h2>Alemán</h2>
<table class="pron-graf toccolours" data-mw='{"parts":[{"template":{"target":{"wt":"pron-graf"}}}]}'>
<tbody><tr><td>Shintoismus</td></tr>
<tr>
<td><b>pronunciación</b> (<a title="Alfabeto Fonético Internacional">AFI</a>)</td>
<td>[ʃɪntoˈɪsmʊs]<br/>[ʃɪntoˈʔɪsmʊs]<br/></td></tr>
</tbody></table>
<section><h3>Sustantivo</h3>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="es">
<h4>Sustantivo</h4>
<ul>
<li><b>pronunciación</b> (AFI): [ʃɪntoˈɪsmʊs], [ʃɪntoˈʔɪsmʊs]</li>
</ul>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>""",
                }
            ],
        )
