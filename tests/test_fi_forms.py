from utils import XMLTestCase


class FiFormsTestCase(XMLTestCase):
    edition = "fi"

    def test_ru_verbi(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>бросить</title></head>
<body>
<section><h2>Venäjä</h2>
<section><h3>Verbi</h3>
<p><b lang="ru" class="hakusana Cyrl">бро́сить</b> <span>(</span><a>II</a><span>)</span> <span>(</span><i><a>perfektiivinen</a></i><span>)</span> (<i>imperfektiivinen</i> <b><a title="бросать">броса́ть</a></b>)</p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["бро́сить", "бросить", "броса́ть", "бросать"]}],
        )

    def test_en_verbi(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>run</title></head>
<body>
<section><h2>Englanti</h2>
<section><h3>Verbi</h3>
<span data-mw='{"parts":[{"template":{"target":{"wt":"en-verbi"}}}]}'></span>
<table class="wikitable">
<tbody><tr>
<th colspan="2">Taivutus</th></tr>
<tr>
<th><a>ind.</a> <a>prees.</a> <a>y.</a> <a>3.</a> <a>p.</a></th>
<td><b><span class="Zzzz linkki" lang="en" data-kuvaus="tm/--/v/ind.p.y3p"><a>runs</a></span></b></td></tr>
</tbody></table><p><b lang="en" class="hakusana Zzzz">run</b></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["run", "runs"]}],
        )

    def test_de_verbi_heik(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>run</title></head>
<body>
<section><h2>Englanti</h2>
<section><h3>Verbi</h3>
<span data-mw='{"parts":[{"template":{"target":{"wt":"en-verbi"}}}]}'></span>
<table class="wikitable">
<tbody><tr>
<th colspan="2">Taivutus</th></tr>
<tr>
<th><a>ind.</a> <a>prees.</a> <a>y.</a> <a>3.</a> <a>p.</a></th>
<td><b><span class="Zzzz linkki" lang="en" data-kuvaus="tm/--/v/ind.p.y3p"><a>runs</a></span></b></td></tr>
</tbody></table><p><b lang="en" class="hakusana Zzzz">run</b></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["run", "runs"]}],
        )

    def test_fi_subs_kala(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>kirja</title></head>
<body>
<section><h2>Suomi</h2>
<section><h3>Substantiivi</h3>
<p id="mwCQ"><b lang="fi" class="hakusana Zzzz">kirja</b><span> </span></p>
<ol><li>gloss</li></ol>
<section><h4>Taivutus</h4>
<span class="mw-empty-elt" data-mw='{"parts":[{"template":{"target":{"wt":"fi-subs-kala"}}}]}'></span><table class="wikitable mw-collapsible">
<tbody>
<tr>
<th><a rel="mw:WikiLink" href="./genetiivi" title="genetiivi">genetiivi</a></th>
<td><span class="Zzzz linkki" lang="fi"><a>kirjan</a></span></td>
<td><span class="Zzzz linkki" lang="fi"><a>kirjojen</a></span><br/>(<span class="Zzzz linkki" lang="fi"><a>kirjain</a></span>)</td></tr>
</tbody></table>
</section>
</section>
</section>
</body>
</html>""",
            [{"forms": ["kirja", "kirjan", "kirjojen", "kirjain"]}],
        )

    def test_ven_verbi(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>бросить</title></head>
<body>
<section><h2>Venäjä</h2>
<section><h3>Verbi</h3>
<p><b lang="ru" class="hakusana Cyrl">бро́сить</b></p>
<ol><li>gloss</li></ol>
<section><h4>Taivutus</h4>
<table class="wikitable" data-mw='{"parts":[{"template":{"target":{"wt":"ven-verbi\n"}}}]}'>
<tbody><tr>
<th><span> </span></th><th>Preesens</th><th>Preteriti</th><th>Imperatiivi</th></tr>
<tr>
<th>yks. 1</th>
<td>бро́шу</td>
<td rowspan="3">бро́сил<br/>бро́сила<br/>бро́сило</td><td>-</td></tr>
</tbody></table>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": [
                        "бро́сить",
                        "бросить",
                        "бро́шу",
                        "бро́сил",
                        "бро́сила",
                        "бро́сило",
                    ]
                }
            ],
        )
