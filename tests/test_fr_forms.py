from utils import XMLTestCase


class FrFormsTestCase(XMLTestCase):
    edition = "fr"

    def test_table_forms(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>autrice</title></head>
<body>
<section><h2>Français</h2>
<section><h3><span>Nom commun</span></h3>
<table class="wikitable flextable flextable-fr-mfsp">
<tbody><tr><th>Singulier</th><th>Pluriel</th></tr>
<tr>
<td><b><span lang="fr" class="lang-fr"><bdi>autrice</bdi></span></b></td>
<td><bdi lang="fr" class="lang-fr"><a>autrices</a></bdi></td></tr>
</tbody></table>
<p><b>autrice</b></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["autrice", "autrices"]}],
        )

    def test_lien_pronominal(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>prendre</title></head>
<body>
<section><h2>Français</h2>
<section><h3>Verbe</h3>
<p><b>prendre</b> <a><span class="API" title="Prononciation API">\\pʁɑ̃dʁ\\</span></a> <span class="ligne-de-forme"><i><a>transitif</a></i></span> <a>3<sup style="font-size:83.33%;line-height:1">e</sup> groupe</a><span> (</span><a><span style="font-size: 100%; font-weight: bold; font-variant: small-caps">voir la conjugaison</span></a><span>)</span> <span>(</span><i>pronominal</i><span><span> </span>: </span><b><bdi lang="fr" class="lang-fr"><a>se<span> </span>prendre</a></bdi></b><span>)</span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["prendre", "se prendre"]}],
        )

    def test_équiv_pour(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>manchot</title></head>
<body>
<section><h2>Français</h2>
<section><h3>Nom commun 1</h3>
<p><b>manchot</b> <a><span class="API" title="Prononciation API">\\mɑ̃.ʃo\\</span></a> <span class="ligne-de-forme"><i>masculin</i></span> <i>(pour une femme, on dit</i><span><span> </span>: </span><bdi lang="fr" class="lang-fr"><a>manchote</a></bdi><i>)</i></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["manchot", "manchote"]}],
        )

    def test_ru_table_forms(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>собака</title></head>
<body>
<section><h2>Russe</h2>
<section><h3>Nom commun</h3>
<table class="wikitable flextable"><tbody>
<tr>
<th>Nominatif</th>
<td><b><span lang="ru" class="lang-ru"><bdi>соба́ка</bdi></span></b></td>
<td><bdi lang="ru" class="lang-ru"><a rel="mw:WikiLink" href="./собаки#ru" title="собаки">соба́ки</a></bdi></td></tr>
</tbody></table>
<p><b>соба́ка</b></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["соба́ка", "собака", "соба́ки", "собаки"]}],
        )
