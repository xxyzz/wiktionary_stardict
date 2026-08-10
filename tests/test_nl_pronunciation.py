from utils import XMLTestCase


class NlPronunciationTestCase(XMLTestCase):
    edition = "nl"

    def test_pos_index_li(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>weed</title></head>
<body>
<section><h2><i>Duits</i></h2>
<section><h5><i>Uitspraak</i></h5>
<ul><li>[A] <a>Geluid</a>: <span class="IPA unicode audiolink"><span> </span><a>weed</a></span><span> </span><span> </span><span> </span><span> </span><small>(<a>hulp</a>, <a>bestand</a>)</small>
<ul><li><a title="WikiWoordenboek:IPA">IPA</a>: <a><span style="font-size: 110%;">/<span> </span>wet<span> </span>/</span></a><span> (1 lettergreep)</span></li></ul></li>
<li>[B] <a>Geluid</a>: <span class="IPA unicode audiolink"><span> </span><a>weed</a></span><span> </span><span> </span><span> </span><span> </span><small>(<a>hulp</a>, <a>bestand</a>)</small>
<ul><li><a title="WikiWoordenboek:IPA">IPA</a>: <a><span style="font-size: 110%;">/<span> </span>wit<span> </span>/</span></a><span> (1 lettergreep)</span></li></ul></li></ul>
</section>
<section><h4><i>Zelfstandig naamwoord</i></h4>
<p><b>[A]</b><span> </span><span>de</span><span> </span><b>weed</b><span> </span><span>m</span></p>
<ol><li>gloss a</li></ol>
</section>
<section><h4><i>Zelfstandig naamwoord</i></h4>
<p><b>[B]</b><span> </span><span>de</span><span> </span><b>weed</b><span> </span><span>m</span></p>
<ol><li>gloss b</li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="nl">
<h4><i>Zelfstandig naamwoord</i></h4>
<ul><li>IPA: <span style="font-size: 110%;">/<span> </span>wet<span> </span>/</span><span> (1 lettergreep)</span></li></ul>
<p><b>[A]</b><span> </span><span>de</span><span> </span><b>weed</b><span> </span><span>m</span></p>
<ol><li>gloss a</li></ol>
</section>"""
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="nl">
<h4><i>Zelfstandig naamwoord</i></h4>
<ul><li>IPA: <span style="font-size: 110%;">/<span> </span>wit<span> </span>/</span><span> (1 lettergreep)</span></li></ul>
<p><b>[B]</b><span> </span><span>de</span><span> </span><b>weed</b><span> </span><span>m</span></p>
<ol><li>gloss b</li></ol>
</section>"""
                },
            ],
        )

    def test_no_pos_index(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>rennen</title></head>
<body>
<section><h2><i>Nederlands</i></h2>
<section><h5><i>Uitspraak</i></h5>
<ul><li><a title="WikiWoordenboek:IPA">IPA</a>: <span style="font-size: 110%;">/<span> </span>ˈrɛŋə(n)<span> </span>/</span><span> (2 lettergrepen)</span></li></ul>
</section>
<section><h4><i>Werkwoord</i></h4>
<p><b>rennen</b></p>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="nl">
<h4><i>Werkwoord</i></h4>
<ul><li>IPA: <span style="font-size: 110%;">/<span> </span>ˈrɛŋə(n)<span> </span>/</span><span> (2 lettergrepen)</span></li></ul>
<p><b>rennen</b></p>
<ol><li>gloss</li></ol>
</section>"""
                }
            ],
        )
