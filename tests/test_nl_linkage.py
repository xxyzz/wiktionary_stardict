from utils import XMLTestCase


class NlLinkageTestCase(XMLTestCase):
    edition = "nl"

    def test_normal_list(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>goed</title></head>
<body>
<section><h2><i>Nederlands</i></h2>
<section><h4><i>Bijvoeglijk naamwoord</i></h4>
<p><b>goed</b></p>
<ol><li>gloss</li></ol>
<section><h5><i>Synoniemen</i></h5>
<ul><li>geschikt</li></ul>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="nl">
<h4><i>Bijvoeglijk naamwoord</i></h4>
<p><b>goed</b></p>
<ol><li>gloss</li></ol>
<section><h4><i>Synoniemen</i></h4>
<ul><li>geschikt</li></ul>
</section></section>"""
                }
            ],
        )

    def test_list_in_table(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Adjektiv</title></head>
<body>
<section><h2><i>Duits</i></h2>
<section><h4><i>Zelfstandig naamwoord</i></h4>
<p><b>Adjektiv</b></p>
<ol><li>gloss</li></ol>
<section><h5><i>Synoniemen</i></h5>
<table><tbody><tr>
<td><ul><li><a>Beiwort</a></li></ul></td>
<td><ul><li><a>Eigenschaftswort</a></li></ul></td>
</tr></tbody></table>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="nl">
<h4><i>Zelfstandig naamwoord</i></h4>
<p><b>Adjektiv</b></p>
<ol><li>gloss</li></ol>
<section><h4><i>Synoniemen</i></h4>
<ul><li>Beiwort</li><li>Eigenschaftswort</li></ul>
</section></section>"""
                }
            ],
        )
