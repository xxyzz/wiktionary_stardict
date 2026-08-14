from utils import XMLTestCase


class ElPOSTestCase(XMLTestCase):
    edition = "el"

    def test_ignore_headword_b_suffix(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>διασκεδαστικός</title></head>
<body>
<section></section>
<section><h2 id="Νέα_ελληνικά_(el)"><span>Νέα ελληνικά</span><span about="#mwt1"> (</span><a><span>el</span></a><span>)</span></h2>
<section><h3 id="Επίθετο"><span class="partofspeech"><img src="//upload.wikimedia.org/wikipedia/commons/thumb/d/d5/OOjs_UI-like_arrow_empty-ltr_progressive.svg/40px-OOjs_UI-like_arrow_empty-ltr_progressive.svg.png?utm_source=el.wiktionary.org&amp;utm_campaign=parser&amp;utm_content=thumbnail" decoding="async" data-file-width="27"/></span> Επίθετο</h3>
<p><b><span>διασκεδαστικός</span>, -ή, -ό</b></p>
<ul><li>gloss</li></ul>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="el">
<h4><span class="partofspeech"></span></span> Επίθετο</span></h4>
<p><b><span>διασκεδαστικός</span>, -ή, -ό</b></p>
<ul><li>gloss</li></ul>
</section>""",
                    "forms": ["διασκεδαστικός"],
                    "ids": ["Νέα_ελληνικά_(el)", "Επίθετο"],
                    "lang": "Νέα ελληνικά",
                }
            ],
        )

    def test_form_of(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>διασκεδαστικός</title></head>
<body>
<section><h2><span>Εσπεράντο (eo)</span></h2>
<section><h3><span class="partofspeech">Κλιτικός τύπος ουσιαστικού</span></h3>
<p><b>abakon</b><span> </span><small><sup><a rel="mw:WikiLink/Interwiki" class="extiw">(eo)</a></sup></small></p>
<ul><li><a data-mw='{"parts":[{"template":{"target":{"wt":"αιτ_του"}}}]}'><span><i>αιτιατική</i></span></a><span> </span><span>του</span><span> </span><span class="notheme"><b><a>abako</a></b></span></li></ul>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="el">
<h4><span class="partofspeech">Κλιτικός τύπος ουσιαστικού</span></h4>
<p><b>abakon</b><span> </span></p>
<ul><li><span><i>αιτιατική</i></span><span> </span><span>του</span><span> </span><span class="notheme"><b>abako</b></span></li></ul>
</section>""",
                    "form_of_only": True,
                    "form_of_targets": ["abako"],
                }
            ],
        )

    def test_form_of_βλ(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>διασκεδαστικός</title></head>
<body>
<section><h2><span>Νέα ελληνικά (el)</span></h2>
<section><h3><span class="partofspeech">Μετοχή</span></h3>
<p><b><span>αναμαλλιασμένος</span>, -η, -ο</b></p>
<ul><li><span data-mw='{"parts":[{"template":{"target":{"wt":"βλ"},"params":{"1":{"wt":"αναμαλλιάζω"}}}}]}'>→</span><span> </span><i>δείτε</i><span> </span><i>τη<span> </span>λέξη</i><span> </span><a>αναμαλλιάζω</a></li></ul>
</section></section></body></html>""",
            [{"form_of_only": True, "form_of_targets": ["αναμαλλιάζω"]}],
        )

    def test_shortest_example(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>book</title></head>
<body>
<section><h2><span>Αγγλικά (en)</span></h2>
<section><h3><span class="partofspeech">Ρήμα</span></h3>
<p><b>book</b></p>
<ol><li>gloss
<dl><dd><span data-mw='{"parts":[{"template":{"target":{"wt":"eg"}}}]}'></span><span> </span> <i><b>I am booking</b> a table at a restaurant.</i>
<dl><dd><b>Κρατώ</b> τραπέζι σ' ένα εστιατόριο.</dd></dl></dd>
<dd><span data-mw='{"parts":[{"template":{"target":{"wt":"eg"}}}]}'></span><span> </span> <i><b>We booked</b> our tickets yesterday.</i>
<dl><dd><b>Κλείσαμε</b> τα εισιτήριά μας χθες.</dd></dl></dd>
<dd><span data-mw='{"parts":[{"template":{"target":{"wt":"συνών"}}}]}'><span>≈</span></span><span> </span><a><span><i>συνώνυμα</i></span></a><i>:</i> <a>reserve</a></dd></dl>
</li></ol></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="el">
<h4><span class="partofspeech">Ρήμα</span></h4>
<p><b>book</b></p>
<ol><li>gloss
<dl><dd><span></span><span> </span> <i><b>We booked</b> our tickets yesterday.</i>
<dl><dd><b>Κλείσαμε</b> τα εισιτήριά μας χθες.</dd></dl></dd>
<dd><span><span>≈</span></span><span> </span><span><i>συνώνυμα</i></span><i>:</i> reserve</dd></dl></li></ol>
</section>"""
                }
            ],
        )
