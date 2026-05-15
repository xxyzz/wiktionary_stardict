from utils import XMLTestCase


class FiPOSTestCase(XMLTestCase):
    edition = "fi"

    def test_taivm_mon(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>lehmät</title></head>
<body>
<section><h2>Suomi</h2>
<section><h3>Substantiivi</h3>
<p id="mwBA"><b lang="fi" class="hakusana Zzzz">lehmät</b><span about="#mwt1"> </span></p>

<ol><li><span> </span><i>monikkomuoto</i><span> </span><i>sanasta</i><span> </span><b><span class="Zzzz linkki" lang="fi"><a>lehmä</a></span></b></li></ol>

<link rel="mw:PageProp/Category" href="./Luokka:Suomen_substantiivien_taivutusmuodot#lehmät" id="mwCg"/>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="fi">
<h4>Substantiivi</h4>
<p><b lang="fi" class="hakusana Zzzz">lehmät</b><span> </span></p>
<ol><li><span> </span><i>monikkomuoto</i><span> </span><i>sanasta</i><span> </span><b><span class="Zzzz linkki" lang="fi">lehmä</span></b></li></ol>
</section>""",
                    "forms": ["lehmät"],
                    "form_of_only": True,
                    "form_of_targets": ["lehmä"],
                }
            ],
        )

    def test_en_monikko(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>books</title></head>
<body>
<section><h2>Englanti</h2>
<section><h3>Substantiivi</h3>
<p><b>books</b></p>
<ol><li><i>monikkomuoto</i><span> </span><i>sanasta</i><span> </span><b><span class="Zzzz linkki" lang="en"><a>book</a></span></b><link rel="mw:PageProp/Category" href="./Luokka:Englannin_substantiivien_taivutusmuodot#BOOKS"/></li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["books"], "form_of_only": True, "form_of_targets": ["book"]}],
        )

    def test_example_list(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>kirja</title></head>
<body>
<section><h2>Suomi</h2>
<section><h3>Substantiivi</h3>
<p><b lang="fi" class="hakusana Zzzz">kirja</b><span> </span><span> (</span><a>9</a><span>)</span></p>
<ol><li>gloss
<dl><dd><i>Luin kiinnostavaa <b>kirjaa</b> aamuyölle asti.</i></dd>
<dd><i>Teidän tulee lukea tämä <b>kirja</b> läpi lokakuun aikana.</i></dd>
</dl></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="fi">
<h4>Substantiivi</h4>
<p><b lang="fi" class="hakusana Zzzz">kirja</b><span> </span><span> (</span>9<span>)</span></p>
<ol><li>gloss
<dl><dd><i>Luin kiinnostavaa <b>kirjaa</b> aamuyölle asti.</i></dd></dl></li></ol>
</section>"""
                }
            ],
        )

    def test_notes(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>nainen</title></head>
<body>
<section><h2>Suomi</h2>
<section><h3>Substantiivi</h3>
<p><b lang="fi" class="hakusana Zzzz">nainen</b><span> </span><span> (</span><a>38</a><span>)</span></p>
<ol><li>gloss</li></ol>
<section><h4>Huomautukset</h4>
<ul><li>Yhdyssanojen alkuosana sana esiintyy muodossa <i>nais-.</i></li></ul>
<dl><dd><i><b>Nais</b>kansanedustajien määrä nousi eduskuntavaaleissa 93:een.</i> (yle.fi)</dd></dl>
</section>
<section><h4>Etymologia</h4>
<p>samasta vartalosta kuin<sup class="mw-ref reference"></sup></p>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="fi">
<h4>Substantiivi</h4>
<p><b lang="fi" class="hakusana Zzzz">nainen</b><span> </span><span> (</span>38<span>)</span></p>
<ol><li>gloss</li></ol>
<section><h4>Huomautukset</h4>
<ul><li>Yhdyssanojen alkuosana sana esiintyy muodossa <i>nais-.</i></li></ul>
<dl><dd><i><b>Nais</b>kansanedustajien määrä nousi eduskuntavaaleissa 93:een.</i> (yle.fi)</dd></dl>
</section>
<section><h4>Etymologia</h4>
<p>samasta vartalosta kuin</p>
</section>
</section>"""
                }
            ],
        )
