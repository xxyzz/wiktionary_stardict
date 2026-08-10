from utils import XMLTestCase


class NlEtymologyTestCase(XMLTestCase):
    edition = "nl"

    def test_etymology_plain_text_pos_index(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>hond</title></head>
<body>
<section><h2><i>Nederlands</i></h2>
<section><h5><i>Woordherkomst en -opbouw</i></h5>
<ul><li>[A] etymology a</li><li>[B] etymology b</li></ul>
</section>
<section><h4><i>Zelfstandig naamwoord</i></h4>
<p>[A] <b>hond</b></p>
<ol><li>gloss a</li></ol>
</section>
<section><h4><i>Zelfstandig naamwoord</i></h4>
<p>[B] <b>hond</b></p>
<ol><li>gloss b</li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="nl">
<h4><i>Zelfstandig naamwoord</i></h4>
<p>[A] <b>hond</b></p>
<ol><li>gloss a</li></ol>
<section><h4><i>Woordherkomst en -opbouw</i></h4>
<ul><li>[A] etymology a</li></ul>
</section></section>"""
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="nl">
<h4><i>Zelfstandig naamwoord</i></h4>
<p>[B] <b>hond</b></p>
<ol><li>gloss b</li></ol>
<section><h4><i>Woordherkomst en -opbouw</i></h4>
<ul><li>[B] etymology b</li></ul>
</section></section>"""
                },
            ],
        )
