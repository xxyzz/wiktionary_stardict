from utils import XMLTestCase


class SimplePOSTestCase(XMLTestCase):
    edition = "simple"

    def test_shortest_example(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>book</title></head>
<body>
<section><h2 id="Verb">Verb</h2>
<table border="0" width="100%" class="notheme inflection-table">
<tbody><tr>
<td bgcolor="#e2e2ff" valign="top" width="20%" style="padding: 0 1em;">
<p>Plain form<br/>
<b>book</b></p></td>
<td bgcolor="#e2e2ff" valign="top" width="20%" style="padding: 0 1em;">
<p>Third-person singular<br/>
<span class="form-of third-person_singular-form-of-book"><b>books</b></span></p></td>
</tr></tbody></table>
<ol><li><span>(</span><i><span class="skin-nightmode-reset-color" style="color:green;">transitive</span></i><span>)</span><link rel="mw:PageProp/Category" href="./Category:Transitive_verbs"/> If you book something or someone, you <a>reserve</a> them for a certain time. <ul class="onyms-collapse onyms-collapse-synonyms"><li><b>Synonyms:</b> engage, order <i>and</i> reserve</li></ul>
<dl><dd><i>I want to <b>book</b> a hotel room for tomorrow night.</i></dd>
<dd><i>I can <b>book</b> tickets for the concert next week.</i></dd></dl></li></ol>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Verb</h4>
<ol><li><span>(</span><i><span class="skin-nightmode-reset-color" style="color:green;">transitive</span></i><span>)</span> If you book something or someone, you reserve them for a certain time. <ul class="onyms-collapse onyms-collapse-synonyms"><li><b>Synonyms:</b> engage, order <i>and</i> reserve</li></ul>
<dl><dd><i>I can <b>book</b> tickets for the concert next week.</i></dd></dl></li></ol>
</section>""",
                    "forms": ["book", "books"],
                    "ids": ["Verb"],
                }
            ],
        )

    def test_form_of_only(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>books</title></head>
<body>
<section><h2>None</h2>
<ol><li><span>The </span>third-person<span> </span>singular<span> form of </span><i>book</i><span>.</span><link rel="mw:PageProp/Category" href="./Category:Third-person_singular_forms"/></li></ol>
</section>
</body>
</html>""",
            [{"form_of_only": True, "form_of_targets": ["book"]}],
        )

    def test_other_spellings(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>practise</title></head>
<body>
<section><h3>Other spellings</h3>
<ul><li><a>practice</a> <span>(</span><i>US</i><span>)</span></li></ul>
</section>
<section><h2>Verb</h2>
<ol><li>gloss</li></ol>
<section><h3>Usage notes</h3>
<p>notes</p>
</section></section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Verb</h4>
<ol><li>gloss</li></ol>
<section><h4>Usage notes</h4>
<p>notes</p>
</section>
<section><h4>Other spellings</h4>
<ul><li>practice <span>(</span><i>US</i><span>)</span></li></ul>
</section></section>""",
                    "forms": ["practise"],
                }
            ],
        )

    def test_pron(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>book</title></head>
<body>
<section><h3>Pronunciation</h3>
<ul><li>enPR<span>: </span><span title="English phonemic representation" class="AHD enPR">bo͝ok</span>, <a title="w:en:IPA chart for English">IPA</a><span> </span><sup>(key)</sup><span>: </span><span class="IPA">/bʊk/</span></li></ul></section>
<section><h2>Noun</h2>
<ol><li>gloss</li></ol></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<ul><li>enPR<span>: </span><span title="English phonemic representation" class="AHD enPR">bo͝ok</span>, IPA<span> </span><span>: </span><span class="IPA">/bʊk/</span></li></ul>
<ol><li>gloss</li></ol></section>""",
                }
            ],
        )
