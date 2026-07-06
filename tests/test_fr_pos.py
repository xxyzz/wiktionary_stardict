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
                    "def": """<section class="mw-parser-output" dir="ltr" lang="fr">
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
                    "def": """<section class="mw-parser-output" dir="ltr" lang="fr">
<h4><span>Nom commun</span></h4>
<p><b>book</b> <span class="API" title="Prononciation API">\\bʊk\\</span></p>
<ol><li>Cahier.</li></ol>
</section>""",
                },
            ],
        )

    def test_h6_notes(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>frigidaire</title></head>
<body>
<section><h2><span>Français</span></h2>
<section><h3><span>Nom commun</span></h3>
<p><b>frigidaire</b></p>
<ol><li>gloss</li></ol>
<section><h6><span>Notes</span></h6>
<dl><dd>notes</dd></dl>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="fr">
<h4><span>Nom commun</span></h4>
<p><b>frigidaire</b></p>
<ol><li>gloss</li></ol>
<section><h4>Notes</h4>
<dl><dd>notes</dd></dl>
</section>
</section>""",
                },
            ],
        )

    def test_section_ids(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>eat</title></head>
<body>
<section><h2 id="Anglais"><span id="en">Anglais</span></h2>
<section><h3 id="Verbe">
<span id="en-verb-1">Verbe</span><span id="en-verb"></span>
</h3>
<p><b>eat</b></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"ids": ["Anglais", "Verbe", "en", "en-verb-1", "en-verb"]}],
        )

    def test_rfdef(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>galet</title></head>
<body>
<section><h2>Catalan</h2>
<section><h3>Nom commun</h3>
<p><b>galet</b></p>
<ol><li><i data-mw='{"parts":[{"template":{"target":{"wt":"ébauche-déf"}}}]}'>Définition manquante ou à compléter.</i><span> </span><span class="plainlinks stubedit">(Ajouter)</span></li></ol>
</section></section></body></html>""",
            [],
        )

    def test_variante_hanja_de(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>地圖</title></head>
<body>
<section><h2>Coréen</h2>
<section><h3>Nom commun</h3>
<p><b>地圖</b></p>
<ol><li><span class="emploi" data-mw='{"parts":[{"template":{"target":{"wt":"variante hanja de"}}}]}'><span id="désuet"></span><i>(<span class="texte">Désuet</span>)</i></span><span> </span><i>Écriture en sinogrammes de</i><span> </span><bdi lang="ko" class="lang-ko">지도</bdi><span> («</span><span> </span><span>carte géographique</span><span> </span><span>»)</span>.</li></ol>
</section></section></body></html>""",
            [{"form_of_only": True, "form_of_targets": ["지도"]}],
        )

    def test_variante_de(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>contindre</title></head>
<body>
<section><h2>Catalan</h2>
<section><h3>Verb</h3>
<p><b>contindre</b></p>
<ol><li><span>(</span><i>Valencien</i><span>)</span> <i data-mw='{"parts":[{"template":{"target":{"wt":"variante de"}}}]}'>Variante<span> </span>de</i><span> </span><bdi lang="fr" class="lang-fr">contenir</bdi>.</li></ol>
</section></section></body></html>""",
            [{"form_of_only": True, "form_of_targets": ["contenir"]}],
        )

    def test_form_of_plain_text(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>ouighour</title></head>
<body>
<section><h2>Français</h2>
<section><h3>Adjectif</h3>
<p><b>ouighour</b></p>
<ol><li>Variante de <i><a>ouïghour</a>.</i></li></ol>
</section></section></body></html>""",
            [{"form_of_only": True, "form_of_targets": ["ouïghour"]}],
        )

    def test_form_of_i(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>donner</title></head>
<body>
<section><h2>Ancien français</h2>
<section><h3>Verbe</h3>
<p><b>donner</b></p>
<ol><li><i>Variante tardive de</i> <bdi lang="fro" class="lang-fro">doner</bdi>.</li></ol>
</section></section></body></html>""",
            [{"form_of_only": True, "form_of_targets": ["doner"]}],
        )

    def test_préciser(self):
        self.assertTransformEqual(
            r"""<!DOCTYPE html>
<html>
<head><title>à cropton</title></head>
<body>
<section><h2>Français</h2>
<section><h3>Locution adverbiale</h3>
<p><b>à cropton</b> <span title="Prononciation à préciser">\<small><span class="plainlinks stubedit">Prononciation<span> </span>?</span></small>\</span> <span class="ligne-de-forme"><i>invariable</i></span></p>
<ol><li><span><i>(Canton de Vaud)</i></span> Être baissé, proche du sol. <small title="Cette information devrait être précisée ou vérifiée."><span> </span>(information<span> </span><i>à préciser ou à vérifier</i>)</small></li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="fr">
<h4>Locution adverbiale</h4>
<p><b>à cropton</b>  <span class="ligne-de-forme"><i>invariable</i></span></p>
<ol><li><span><i>(Canton de Vaud)</i></span> Être baissé, proche du sol. </li></ol>
</section>"""
                }
            ],
        )

    def test_notes_ol(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>社會</title></head>
<body>
<section><h2>Chinois</h2>
<section><h3>Nom commun</h3>
<p><b>社會</b></p>
<ol><li>gloss</li></ol>
<section><h4>Notes</h4>
<ul><li>classificateur<span> </span>: <span class="Hani" lang="zh">個</span><span>／</span><span class="Hani" lang="zh">个</span><span> (</span><i><span class="tr Latn">gè</span></i><span>)</span></li></ul>
<ol><li><ul><li class="mw-empty-elt"></li><li><span class="example"><q><bdi lang="zh" class="lang-zh">一個社會</bdi></q></span><br/><bdi lang="zh-Latn" class="lang-zh-Latn"><i>yī gè shèhuì</i></bdi>
<dl><dd>une société</dd></dl></li></ul></li></ol>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="fr">
<h4>Nom commun</h4>
<p><b>社會</b></p>
<ol><li>gloss</li></ol>
<section><h4>Notes</h4>
<ul><li>classificateur<span> </span>: <span class="Hani" lang="zh">個</span><span>／</span><span class="Hani" lang="zh">个</span><span> (</span><i><span class="tr Latn">gè</span></i><span>)</span></li></ul>
<ol><li><ul><li><span class="example"><q><bdi lang="zh" class="lang-zh">一個社會</bdi></q></span><br/><bdi lang="zh-Latn" class="lang-zh-Latn"><i>yī gè shèhuì</i></bdi>
<dl><dd>une société</dd></dl></li></ul></li></ol>
</section></section>"""
                }
            ],
        )
