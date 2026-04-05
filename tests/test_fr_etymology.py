from utils import XMLTestCase


class FrEtymologyTestCase(XMLTestCase):
    edition = "fr"

    def test_pos_ids(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>dame</title></head>
<body>
<section><h2>Français</h2>
<section><h3>Étymologie</h3>
<dl><dd><i>(<a rel="mw:WikiLink" href="./dame#fr-nom-1" class="mw-selflink-fragment">Nom commun 1</a>)</i> Du <span>latin </span><i><bdi lang="la" class="lang-la">domina</bdi></i><span> («</span><span> </span>aîtresse<span> de </span>maison<span> </span><span>»)</span>.</dd>
<dd><i>(<a rel="mw:WikiLink" href="./dame#fr-nom-2" class="mw-selflink-fragment">Nom commun 2</a>)</i> Du <span>moyen néerlandais </span><i><bdi lang="dum" class="lang-dum">dam</bdi></i><span> («</span><span> </span>digue<span> </span><span>»)</span>.</dd></dl>
</section>
<section><h3><span class="titredef" id="fr-nom-1">Nom commun 1</span></h3>
<p><b>dame</b> <span class="API" title="Prononciation API">\\dam\\</span> <span class="ligne-de-forme"><i>féminin</i></span></p>
<ol><li>Femme qui appartient à la noblesse.</li></ol>
</section>
<section><h3><span class="titredef" id="fr-nom-2">Nom commun 2</span></h3>
<p><b>dame</b> <span class="API" title="Prononciation API">\\dam\\</span> <span class="ligne-de-forme"><i>féminin</i></span></p>
<ol><li>Digue, ou pièce de maçonnerie, installée sur un cours d’eau pour permettre la construction d’un ouvrage.</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="fr">
<h4><span class="titredef">Nom commun 1</span></h4>
<p><b>dame</b> <span class="API" title="Prononciation API">\\dam\\</span> <span class="ligne-de-forme"><i>féminin</i></span></p>
<ol><li>Femme qui appartient à la noblesse.</li></ol>
<section>
<h4>Etymology</h4>
<dl><dd> Du <span>latin </span><i><bdi lang="la" class="lang-la">domina</bdi></i><span> («</span><span> </span>aîtresse<span> de </span>maison<span> </span><span>»)</span>.</dd></dl>
</section>
</section>""",
                },
                {
                    "def": """<section dir="ltr" lang="fr">
<h4><span class="titredef">Nom commun 2</span></h4>
<p><b>dame</b> <span class="API" title="Prononciation API">\\dam\\</span> <span class="ligne-de-forme"><i>féminin</i></span></p>
<ol><li>Digue, ou pièce de maçonnerie, installée sur un cours d’eau pour permettre la construction d’un ouvrage.</li></ol>
<section>
<h4>Etymology</h4>
<dl><dd> Du <span>moyen néerlandais </span><i><bdi lang="dum" class="lang-dum">dam</bdi></i><span> («</span><span> </span>digue<span> </span><span>»)</span>.</dd></dl>
</section>
</section>""",
                },
            ],
        )

    def test_missing_etymology(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Hörsaal</title></head>
<body>
<section><h2>Allemand</h2>
<section><h3>Étymologie</h3>
<dl><dd>text<link rel="mw:PageProp/Category" href="./Catégorie:Wiktionnaire:Étymologies_manquantes_en_allemand"/></dd></dl>
</section>
<section><h3>Nom commun</h3>
<p><b>Hörsaal</b></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="fr">
<h4>Nom commun</h4>
<p><b>Hörsaal</b></p>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )
