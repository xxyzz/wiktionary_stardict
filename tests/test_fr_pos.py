from utils import XMLTestCase


class FrPOSTestCase(XMLTestCase):
    edition = "fr"

    def test_example_list(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>courir</title></head>
<body>
<section><h2 id="Français"><span id="Fran.C3.A7ais" typeof="mw:FallbackId"></span><span class="sectionlangue" id="fr" about="#mwt1" typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"langue","href":"./Modèle:langue"},"params":{"1":{"wt":"fr"}},"i":0}}]}'><a rel="mw:WikiLink" href="./Portail:Français" title="Portail:Français">Français</a></span><link rel="mw:PageProp/Category" href="./Catégorie:français" about="#mwt1" id="mwBA"/></h2>

<section><h3 id="Verbe"><span>Verbe</span></h3>
<p id="mwIg"><b id="mwIw">courir</b> <a><span class="API" title="Prononciation API">\\ku.ʁiʁ\\</span></a> <span class="ligne-de-forme"><i><a>transitif</a></i></span><link rel="mw:PageProp/Category" href="./Catégorie:Verbes_transitifs_en_français" about="#mwt12" id="mwJg"/> ou <span class="ligne-de-forme"><i><a>intransitif</a></i></span> <a rel="mw:WikiLink" href="./Conjugaison:français/Troisième_groupe" title="Conjugaison:français/Troisième groupe">3<sup style="font-size:83.33%;line-height:1">e</sup> groupe</a><span> (</span><a rel="mw:WikiLink" href="./Conjugaison:français/courir" title="Conjugaison:français/courir"><span style="font-size: 100%; font-weight: bold; font-variant: small-caps">voir la conjugaison</span></a><span>)</span></p>
<ol>
<li>Couler, s’écouler.
<ul><li><span class="example"><q><bdi lang="fr" class="lang-fr"><i>Le ruisseau qui <b>court</b> dans la prairie.</i></bdi></q></span></li>
<li><span class="example"><q><bdi lang="fr" class="lang-fr"><i>Le Rhône <b>court</b> du nord au sud.</i></bdi></q></span></li></ul>
<ol><li>Se dit figurément du Temps.
<ul><li><span class="example"><q><bdi lang="fr" class="lang-fr"><i>Le temps court insensiblement.</i></bdi></q></span></li>
<li><i>Par les temps qui <b>courent</b>,</i> dans le temps présent, dans les circonstances actuelles.</li></ul></li></ol></li>
</ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="fr">
<h4><span>Verbe</span></h4>
<p><b>courir</b> <span class="API" title="Prononciation API">\\ku.ʁiʁ\\</span> <span class="ligne-de-forme"><i>transitif</i></span> ou <span class="ligne-de-forme"><i>intransitif</i></span> 3<sup style="font-size:83.33%;line-height:1">e</sup> groupe</p>
<ol>
<li>Couler, s’écouler.
<ul><li><span class="example"><q><bdi lang="fr" class="lang-fr"><i>Le Rhône <b>court</b> du nord au sud.</i></bdi></q></span></li></ul>
<ol><li>Se dit figurément du Temps.
<ul><li><span class="example"><q><bdi lang="fr" class="lang-fr"><i>Le temps court insensiblement.</i></bdi></q></span></li></ul></ol></li>
</ol>
</section>""",
                    "zim_pages": ["Conjugaison:français/courir"],
                },
            ],
        )

    def test_ignore_missing_example(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>book</title></head>
<body>
<section><h2><span>Anglais</span></h2>
<section><h3><span>Nom commun</span></h3>
<p><b>book</b> <span class="API" title="Prononciation API">\\bʊk\\</span></p>
<ol>
<li>Cahier.
<ul><li><span class="example"><i>Exemple d’utilisation manquant.</i> <span class="plainlinks stubedit">(Ajouter)</span><bdi lang="en" style="display: none"></bdi></span></li></ul></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="fr">
<h4><span>Nom commun</span></h4>
<p><b>book</b> <span class="API" title="Prononciation API">\\bʊk\\</span></p>
<ol><li>Cahier.</li></ol>
</section>""",
                },
            ],
        )

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
