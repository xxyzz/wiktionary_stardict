from utils import XMLTestCase


class FiPronTestCase(XMLTestCase):
    edition = "fi"

    def test_pron_list(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>kirja</title></head>
<body>
<section><h2>Suomi</h2>
<section><h3>Substantiivi</h3>
<p><b lang="fi" class="hakusana Zzzz">kirja</b><span> </span><span> (</span>9<span>)</span></p>
<ol><li>gloss</li></ol>
<section><h4>Ääntäminen</h4>
<ul><li><a title="Liite:Ääntäminen">IPA</a>: <span class="IPA explain" style="text-decoration: none; font-size:115%; font-family: 'Gentium', sans-serif;">/ˈkirjɑ/</span></li>
<li>tavutus: kir‧ja</li></ul>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="fi">
<h4>Substantiivi</h4>
<ul><li>IPA: <span class="IPA explain" style="text-decoration: none; font-size:115%; font-family: 'Gentium', sans-serif;">/ˈkirjɑ/</span></li>
<li>tavutus: kir‧ja</li></ul>
<p><b lang="fi" class="hakusana Zzzz">kirja</b><span> </span><span> (</span>9<span>)</span></p>
<ol><li>gloss</li></ol>
</section>"""
                }
            ],
        )

    def test_ipa2(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>aquae</title></head>
<body>
<section><h2>Latina</h2>
<section><h3>Substantiivi</h3>
<p><b>aquae</b></p>
<ol><li>gloss</li></ol>
<section><h4>Ääntäminen</h4>
<ul><li>(<i>klassinen</i>) <span class="IPA explain">[ˈäkʷäe̯]</span></li></ul>
</section>
<section><h5>Ääntäminen</h5>
<ul><li>tavutus: a‧quae</li></ul>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="fi">
<h4>Substantiivi</h4>
<ul><li>(<i>klassinen</i>) <span class="IPA explain">[ˈäkʷäe̯]</span></li></ul>
<ul><li>tavutus: a‧quae</li></ul>
<p><b>aquae</b></p>
<ol><li>gloss</li></ol>
</section>"""
                }
            ],
        )
