from utils import XMLTestCase


class NlPOSTestCase(XMLTestCase):
    edition = "nl"

    def test_form_of(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>grootje</title></head>
<body>
<section data-mw-section-id="-1" id="mwAw"><span about="#mwt1">
</span><h2 about="#mwt1" id="Nederlands"><i><a rel="mw:WikiLink" href="./WikiWoordenboek:Nederlands" title="WikiWoordenboek:Nederlands">Nederlands</a></i></h2>
<section data-mw-section-id="-1" id="mwHw"><h4><i><a rel="mw:WikiLink" href="./WikiWoordenboek:Zelfstandig_naamwoord" title="WikiWoordenboek:Zelfstandig naamwoord">Zelfstandig naamwoord</a></i></h4>
<p about="#mwt15">het<span> </span><b>grootje</b><span> </span><a><span>o</span></a></p>
<ol about="#mwt15"><li>verkleinwoord enkelvoud van het zelfstandig naamwoord <a rel="mw:WikiLink" href="./groot" title="groot">groot</a><link rel="mw:PageProp/Category" href="./Categorie:Zelfstandignaamwoordsvorm_in_het_Nederlands"/></li>
<li>gloss</li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="nl">
<h4><i>Zelfstandig naamwoord</i></h4>
<p>het<span> </span><b>grootje</b><span> </span><span>o</span></p>
<ol><li>verkleinwoord enkelvoud van het zelfstandig naamwoord groot</li>
<li>gloss</li></ol>
</section>""",
                    "form_of_only": False,
                    "forms": ["grootje"],
                }
            ],
        )
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>grootje</title></head>
<body>
<section><h2><i>Nederlands</i></h2>
<section><h4><i><a>Zelfstandig naamwoord</a></i></h4>
<p>het<span> </span><b>grootje</b><span> </span><a><span>o</span></a></p>
<ol><li>verkleinwoord enkelvoud van het zelfstandig naamwoord <a rel="mw:WikiLink" href="./groot" title="groot">groot</a><link rel="mw:PageProp/Category" href="./Categorie:Zelfstandignaamwoordsvorm_in_het_Nederlands"/></li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="nl">
<h4><i>Zelfstandig naamwoord</i></h4>
<p>het<span> </span><b>grootje</b><span> </span><span>o</span></p>
<ol><li>verkleinwoord enkelvoud van het zelfstandig naamwoord groot</li></ol>
</section>""",
                    "form_of_only": True,
                    "form_of_targets": ["groot"],
                }
            ],
        )

    def test_short_ul_example(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Nederlands</title></head>
<body>
<section><h2><i>Nederlands</i></h2>
<section><h4><i><a>Eigennaam</a></i></h4>
<p>het<span> </span><b>Nederlands</b><span> </span><a><span>o</span></a></p>
<ol><li>gloss
<dl><dd><ul><li>short example</li><li>very long example</li></ul></dd>
<dd><span>▸</span><i>quote example</i></dd>
</dl></li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="nl">
<h4><i>Eigennaam</i></h4>
<p>het<span> </span><b>Nederlands</b><span> </span><span>o</span></p>
<ol><li>gloss<ul><li>short example</li></ul></li></ol>
</section>"""
                }
            ],
        )

    def test_headword_b_index(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>weed</title></head>
<body>
<section><h2><i>Nederlands</i></h2>
<section><h4><i>Zelfstandig naamwoord</i></h4>
<p><b>[A]</b><span> </span><span>de</span><span> </span><b>weed</b></p>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="nl">
<h4><i>Zelfstandig naamwoord</i></h4>
<p><b>[A]</b><span> </span><span>de</span><span> </span><b>weed</b></p>
<ol><li>gloss</li></ol>
</section>""",
                    "forms": ["weed"],
                }
            ],
        )

    def test_short_bijv_2_example(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>ruotsi</title></head>
<body>
<section><h2><i>Fins</i></h2>
<section><h4><i>Zelfstandig naamwoord</i></h4>
<p><b>ruotsi</b></p>
<ol><li>gloss
<dl><dd>«Opiskelen <b>ruotsia</b>.»
<dl><dd><i>Ik studeer <b>Zweeds</b>.</i></dd></dl></dd>
<dd>«Puhutteko <b>ruotsia</b>?»
<dl><dd><i>Spreekt u <b>Zweeds</b>?</i></dd></dl></dd></dl></li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="nl">
<h4><i>Zelfstandig naamwoord</i></h4>
<p><b>ruotsi</b></p>
<ol><li>gloss
<dl><dd>«Puhutteko <b>ruotsia</b>?»
<dl><dd><i>Spreekt u <b>Zweeds</b>?</i></dd></dl></dd></dl></li></ol>
</section>""",
                }
            ],
        )
