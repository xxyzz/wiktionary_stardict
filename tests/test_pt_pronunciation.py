from utils import XMLTestCase


class PtPronTestCase(XMLTestCase):
    edition = "pt"

    def test_direct_list_child(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>brasilianista</title></head>
<body>
<section><h1>Português</h1>
<section><h2>Adjetivo</h2>
<p><b>brasilianista</b></p>
<ol><li>gloss</li></ol>
</section>
<section><h2>Pronúncia</h2>
<ul><li><a title="AFI">AFI</a>: <span class="ipa">/bɾa.zi.li.ã.'nis.tə/</span></li>
<li><a title="SAMPA">SAMPA</a>: /bra.zi.lj6."nis.ta/</li></ul>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pt">
<h4>Adjetivo</h4>
<p><b>brasilianista</b></p>
<ol><li>gloss</li></ol>
<section><h4>Pronúncia</h4>
<ul><li>AFI: <span class="ipa">/bɾa.zi.li.ã.'nis.tə/</span></li>
<li>SAMPA: /bra.zi.lj6."nis.ta/</li></ul>
</section></section>"""
                }
            ],
        )

    def test_child_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>tupi</title></head>
<body>
<section><h1>Português</h1>
<section><h2>Adjetivo</h2>
<p><b>tupi</b></p>
<ol><li>gloss</li></ol>
</section>
<section><h2>Pronúncia</h2>
<section><h3>Brasil</h3>
<ul><li><span> </span><a title="AFI">AFI</a><span>: </span><span>/tuˈpi/</span><span>  </span></li></ul>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pt">
<h4>Adjetivo</h4>
<p><b>tupi</b></p>
<ol><li>gloss</li></ol>
<section><h4>Pronúncia</h4>
<section><h5>Brasil</h5>
<ul><li><span> </span>AFI<span>: </span><span>/tuˈpi/</span><span>  </span></li></ul>
</section></section></section>"""
                }
            ],
        )
