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
