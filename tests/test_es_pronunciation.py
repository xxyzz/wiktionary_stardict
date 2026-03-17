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
                [
                    ["acontecer"],
                    """<section>
<h4>Verbo intransitivo y terciopersonal</h4>
<ul>
<li><b>seseante</b> (AFI): [akõn̪t̪eˈseɾ]</li>
<li><b>silabación</b>: a-con-te-cer</li>
</ul>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>""",
                    [],
                ]
            ],
        )
