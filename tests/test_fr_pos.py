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
<li><span class="example"><q><bdi lang="fr" class="lang-fr"><i>Le Rhône <b>court</b> du nord au sud.</i></bdi></q></span></li>
<li><span class="example"><q><bdi lang="fr" class="lang-fr"><i><b>court</b></i></bdi></q><span class="sources"></span></span></li></ul>
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
<ol><li>Variante de <i><a rel="mw:WikiLink" href="./ouïghour">ouïghour</a>.</i></li></ol>
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

    def test_variante_pos(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>à coeur perdu</title></head>
<body>
<section><h2>Français</h2>
<section><h3>Variante par contrainte typographique</h3>
<p><b>à coeur perdu</b></p>
<ol><li><i>Variante par contrainte typographique d’</i> <a rel="mw:WikiLink" href="./à_cœur_perdu" title="à cœur perdu">à cœur perdu</a>.</li></ol>
</section></section></body></html>""",
            [{"form_of_only": True, "form_of_targets": ["à cœur perdu"]}],
        )

    def test_form_of_fragment(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>bout</title></head>
<body>
<section><h2>Anglais</h2>
<section><h3>Préposition</h3>
<p><b>bout</b></p>
<ol><li><i typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"variante de"}}}]}'>Variante<span typeof="mw:Entity"> </span>de</i><span> </span><bdi lang="en" class="lang-en"><a rel="mw:WikiLink" href="./about#en-prép" title="about">about</a></bdi>.</li></ol>
</section></section></body></html>""",
            [{"form_of_only": True, "form_of_targets": ["about#en-prép"]}],
        )

    def test_ignore_score_not_in_def(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>gamme mineure harmonique</title></head>
<body>
<section><h2>Français</h2>
<section><h3>Locution nominale</h3>
<div class="thumb tright" about="#mwt6" id="mwDw">
<div class="thumbinner">
<div class="illustration-musique">
<div class="mw-ext-score noresize mw-ext-score-svg skin-invert" data-mw-midi="//upload.wikimedia.org/score/m/y/myjko5dskhtkls9bs0hs8gjl0xsdqng/myjko5ds.midi" typeof="mw:Extension/score" about="#mwt8" data-mw='{"name":"score","attrs":{"lang":"lilypond","note-language":"english","sound":"1"},"body":{"extsrc":"{\n\\override Score.TimeSignature #&apos;stencil = ##f\n\\relative c&apos; { \n  \\clef treble \\time 7/4\n  a4 b c d e f gs a2 }\n}"}}'><img src="//upload.wikimedia.org/score/m/y/myjko5dskhtkls9bs0hs8gjl0xsdqng/myjko5ds.svg" width="230" height="59" alt="{
\\override Score.TimeSignature #'stencil = ##f
\relative c' {
  \\clef treble \time 7/4
  a4 b c d e f gs a2 }
}"/></div></div></div></div>
<p><b>gamme mineure harmonique</b></p>
<ol><li>Gamme, en musique occidentale</li></ol>
</section></section></body></html>""",
            [{"svg": [], "images": []}],
        )

    def test_forme_de_verbe_sections(self):
        # https://fr.wiktionary.org/wiki/fue
        input_html = """<!DOCTYPE html>
<html>
<head><title>fue</title></head>
<body>
<section><h2 id="Espagnol"><span class="sectionlangue" id="es"><a rel="mw:WikiLink" href="./Portail:Espagnol" title="Portail:Espagnol">Espagnol</a></span></h2>
<section><h3 id="Forme_de_verbe_1"><span class="titredef" id="es-flex-verb-1">Forme de verbe 1</span><span id="es-flex-verb" style="font-size:0;"></span></h3>
<table class="wikitable flextable">
<tbody><tr><th colspan="3"><small><a rel="mw:WikiLink" href="./Conjugaison:espagnol/ir" title="Conjugaison:espagnol/ir">Voir la conjugaison du verbe <i><span lang="es" class="lang-es"><bdi>ir</bdi></span></i></a></small></th></tr>
<tr style="vertical-align:top"><td>(él/ella/ello/usted) fue</td></tr>
</tbody></table>
<p><b>fue</b> <a rel="mw:WikiLink" href="./Annexe:Prononciation/espagnol" title="Annexe:Prononciation/espagnol"><span class="API" title="Prononciation API">\\fwe\\</span></a></p>
<ol><li><i>Troisième personne du singulier du passé simple de l’indicatif du verbe irrégulier</i> <bdi lang="es" class="lang-es"><a rel="mw:WikiLink" href="./ir#es-verb" title="ir">ir</a></bdi><span> («</span><span typeof="mw:Entity"> </span><a rel="mw:WikiLink" href="./aller" title="aller">aller</a><span typeof="mw:Entity"> </span><span>»)</span>.</li></ol>
</section>
<section><h3 id="Forme_de_verbe_2"><span class="titredef" id="es-flex-verb-2">Forme de verbe 2</span></h3>
<p><b>fue</b> <a rel="mw:WikiLink" href="./Annexe:Prononciation/espagnol" title="Annexe:Prononciation/espagnol"><span class="API" title="Prononciation API">\\fwe\\</span></a></p>
<ol><li><i>Troisième personne du singulier du passé simple de l’indicatif du verbe irrégulier</i> <bdi lang="es" class="lang-es"><a rel="mw:WikiLink" href="./ser#es-verb" title="ser">ser</a></bdi><span> («</span><span typeof="mw:Entity"> </span><a rel="mw:WikiLink" href="./%C3%AAtre" title="être">être</a><span typeof="mw:Entity"> </span><span>»)</span>.</li></ol>
</section>
</section>
</body>
</html>"""
        self.assertEqual(len(self.transform_input(input_html)), 2)
        self.assertTransformEqual(
            input_html,
            [
                {
                    "forms": ["fue"],
                    "form_of_only": True,
                    "form_of_targets": ["ir#es-verb"],
                    "ids": [
                        "Espagnol",
                        "Forme_de_verbe_1",
                        "es",
                        "es-flex-verb-1",
                        "es-flex-verb",
                    ],
                },
                {
                    "forms": ["fue"],
                    "form_of_only": True,
                    "form_of_targets": ["ser#es-verb"],
                },
            ],
        )

    def test_forme_section_ignore_table_forms(self):
        # https://fr.wiktionary.org/wiki/casas
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>casas</title></head>
<body>
<section><h2>Espagnol</h2>
<section><h3 id="Forme_de_nom_commun"><span class="titredef" id="es-flex-nom-1">Forme de nom commun</span></h3>
<table class="wikitable flextable flextable-es-mfsp">
<tbody><tr><th>Singulier</th><th>Pluriel</th></tr>
<tr>
<td><bdi lang="es" class="lang-es"><a rel="mw:WikiLink" href="./casa#es" title="casa">casa</a></bdi></td>
<td><b><span lang="es" class="lang-es"><bdi>casas</bdi></span></b></td></tr>
</tbody></table>
<p><b>casas</b> <span class="ligne-de-forme"><i>féminin</i></span></p>
<ol><li><i>Pluriel de</i> <a rel="mw:WikiLink" href="./casa#es-nom" title="casa">casa</a>.</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["casas"],
                    "form_of_only": True,
                    "form_of_targets": ["casa#es-nom"],
                }
            ],
        )

    def test_lemma_and_forme_sections(self):
        # https://fr.wiktionary.org/wiki/casa
        input_html = """<!DOCTYPE html>
<html>
<head><title>casa</title></head>
<body>
<section><h2>Espagnol</h2>
<section><h3 id="Nom_commun"><span class="titredef" id="es-nom-1">Nom commun</span></h3>
<p><b>casa</b> <span class="ligne-de-forme"><i>féminin</i></span></p>
<ol><li><a rel="mw:WikiLink" href="./maison#Nom_commun" title="maison">Maison</a>.</li></ol>
</section>
<section><h3 id="Forme_de_verbe"><span class="titredef" id="es-flex-verb-1">Forme de verbe</span></h3>
<p><b>casa</b></p>
<ol><li><i>Troisième personne du singulier du présent de l’indicatif de </i><bdi lang="es" class="lang-es"><a rel="mw:WikiLink" href="./casar#es" title="casar">casar</a></bdi><i>.</i></li>
<li><i>Deuxième personne du singulier de l’impératif de </i><bdi lang="es" class="lang-es"><a rel="mw:WikiLink" href="./casar#es" title="casar">casar</a></bdi><i>.</i></li></ol>
</section>
</section>
</body>
</html>"""
        self.assertEqual(len(self.transform_input(input_html)), 2)
        self.assertTransformEqual(
            input_html,
            [
                {"forms": ["casa"], "form_of_only": False, "form_of_targets": []},
                {
                    "forms": ["casa"],
                    "form_of_only": True,
                    "form_of_targets": ["casar#es"],
                },
            ],
        )

    def test_forme_de_verbe_french(self):
        # https://fr.wiktionary.org/wiki/mangeons
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>mangeons</title></head>
<body>
<section><h2>Français</h2>
<section><h3 id="Forme_de_verbe"><span class="titredef" id="fr-flex-verb-1">Forme de verbe</span></h3>
<p><b>mangeons</b></p>
<ol><li><i>Première personne du pluriel du présent de l’indicatif de</i> <a rel="mw:WikiLink" href="./manger" title="manger">manger</a>.</li>
<li><i>Première personne du pluriel de l’impératif de</i> <a rel="mw:WikiLink" href="./manger" title="manger">manger</a>.</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["mangeons"],
                    "form_of_only": True,
                    "form_of_targets": ["manger"],
                }
            ],
        )

    def test_forme_section_italic_link_is_not_target(self):
        # https://fr.wiktionary.org/wiki/trat
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>trat</title></head>
<body>
<section><h2>Allemand</h2>
<section><h3 id="Forme_de_verbe"><span class="titredef" id="de-flex-verb-1">Forme de verbe</span></h3>
<p><b>trat</b></p>
<ol><li><i>Première personne du singulier du <a rel="mw:WikiLink" href="./pr%C3%A9t%C3%A9rit" title="prétérit">prétérit</a> de</i> <a rel="mw:WikiLink" href="./treten" title="treten">treten</a>.</li>
<li><i>Troisième personne du singulier du <a rel="mw:WikiLink" href="./pr%C3%A9t%C3%A9rit" title="prétérit">prétérit</a> de</i> <a rel="mw:WikiLink" href="./treten" title="treten">treten</a>.</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["trat"], "form_of_only": True, "form_of_targets": ["treten"]}],
        )

    def test_forme_section_without_link(self):
        # https://fr.wiktionary.org/wiki/Abesias
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Abesias</title></head>
<body>
<section><h2>Gaulois</h2>
<section><h3 id="Forme_de_prénom"><span class="titredef">Forme de prénom</span></h3>
<p><b>Abesias</b></p>
<ol><li><i>Génitif singulier d'un prénom féminin gaulois</i>.</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["Abesias"], "form_of_only": False, "form_of_targets": []}],
        )

    def test_forme_section_with_plain_definitions(self):
        # https://fr.wiktionary.org/wiki/nineties
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>nineties</title></head>
<body>
<section><h2>Anglais</h2>
<section><h3 id="Forme_de_nom_commun"><span class="titredef" id="en-flex-nom-1">Forme de nom commun</span></h3>
<p><b>nineties</b></p>
<ol><li><i>Pluriel de</i> <a rel="mw:WikiLink" href="./ninety#en" title="ninety">ninety</a>.</li>
<li><span class="term" id="en-calendrier"><i>(<span class="texte">Chronologie</span>)</i></span> Années 90, en particulier la <a rel="mw:WikiLink" href="./d%C3%A9cennie" title="décennie">décennie</a> 1990-1999.</li>
<li><span class="term"><i>(<span class="texte">Avec un adjectif possessif</span>)</i></span> Âges de 90 à 99 ans.</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["nineties"], "form_of_only": False, "form_of_targets": []}],
        )

    def test_forme_section_link_without_label(self):
        # https://fr.wiktionary.org/wiki/2èmes
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>2èmes</title></head>
<body>
<section><h2>Français</h2>
<section><h3 id="Forme_d’adjectif"><span class="titredef" id="fr-flex-adj-1">Forme d’adjectif</span></h3>
<p><b>2èmes</b></p>
<ol><li><a rel="mw:WikiLink" href="./deuxi%C3%A8mes" title="deuxièmes">Deuxièmes</a>.</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["2èmes"], "form_of_only": False, "form_of_targets": []}],
        )
