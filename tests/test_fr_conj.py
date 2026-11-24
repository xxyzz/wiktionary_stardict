from utils import XMLTestCase


class FrConjTestCase(XMLTestCase):
    edition = "fr"
    xsl_file = "conjugaison.xsl"

    def test_fr_conj(self):
        data = self.transform_zim(
            """<!DOCTYPE html>
<html>
<head><title>Conjugaison:français/courir</title></head>
<body>
<section><h3>Modes impersonnels</h3>
<table><tbody>
<tr align="center" valign="top" id="mwFg">
<td width="8%"><span> </span><b><a>Infinitif</a></b><span> </span></td>
<td width="4.5%" align="right"><span> </span><span> </span></td>
<td width="12.5%" align="left"><a>courir</a></td>
<td width="25%"><span> </span><a><span class="API">\\ku.ʁiʁ\\</span></a></td>
<td width="15%" align="right"><span> </span>avoir<span> </span></td>
<td width="10%" align="left"><a>couru</a></td>
<td width="25%"><span> </span><a><span class="API">\\a.vwaʁ<span> </span>ku.ʁy\\</span></a></td></tr>
</tbody></table>
</section>
<section><h3> Indicatif </h3>
<table>
<tbody><tr align="center" valign="top">
<td width="50%">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tbody><tr bgcolor="#DDDDDD" style="border:1px solid #AAAAAA;">
    <th colspan="4">Présent</th>
</tr>
<tr>
    <td width="20%" align="right">je<span> </span></td>
    <td width="30%" align="left"><a>cours</a></td>
    <td width="20%" align="right" class="API">\\<a><span class="API" title="prononciation API">ʒə<span> </span></span></a></td>
    <td width="30%" align="left" class="API"><a><span class="API" title="prononciation API">kuʁ</span></a>\\</td>
</tr>
</tbody></table></td></tr></tbody></table>
</section>
<section><h3> Impératif </h3>
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tbody><tr align="center" valign="top">
<td width="50%">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
<tbody><tr align="center">
<th colspan="3">Présent</th></tr>
<tr align="center" valign="top">
<td width="25%" align="right"><span> </span></td>
<td width="25%" align="left"><a>cours</a><span> </span></td>
<td width="50%"><a><span class="API" title="Prononciation API">\\kuʁ\\</span></a></td></tr>
</tbody></table></td></tr></tbody></table>
</section>
</body>
</html>"""
        )
        self.assertEqual(data, ["courir", "couru", "cours"])

    def test_es_conj(self):
        data = self.transform_zim(
            r"""<!DOCTYPE html>
<html>
<head><title>Conjugaison:espagnol/casar</title></head>
<body>
<section><h3>Modes impersonnels</h3>
<table><tbody><tr>
<td width="17%"><span> </span><a rel="mw:WikiLink" href="./casar#es" title="casar">casar</a></td>
<td width="18%"><a><span class="API" title="Prononciation API">\kaˈθaɾ\</span></a></td>
<td width="15%" align="right"><span> </span>haber<span> </span></td>
<td width="17%"><span> </span><a rel="mw:WikiLink" href="./casado#es" title="casado">casado</a></td>
<td width="18%"><span> </span><a><span class="API" title="Prononciation API">\aˈβeɾ kaˈθa.ðo\</span></a></td></tr>
</tbody></table>
</section>
<section><h3>Indicatif</h3><table><tbody><tr><td><table><tbody><tr>
<td width="30%" align="right">(yo)<span> </span></td>
<td width="34%"><span> </span><a rel="mw:WikiLink" href="./caso#es" title="caso">caso</a></td>
<td width="36%"><a><span class="API" title="Prononciation API">\ˈka.θo\</span></a></td>
</tr></tbody></table></td></tr></tbody></table></section></body></html>"""
        )
        self.assertEqual(data, ["casar", "casado", "caso"])

    def test_it_conj(self):
        self.assertEqual(
            self.transform_zim(
                r"""<!DOCTYPE html>
<html>
<head><title>Conjugaison:italien/avere</title></head>
<body>
<section><h3>Modes impersonnels</h3>
<table><tbody><tr>
<td style="width:17%;"><span> </span><a>avere</a></td>
<td style="width:18%;"><a><span class="API" title="Prononciation API">\a.ˈve.re\</span></a></td>
<td><span> </span>avere</td>
<td style="width:17%;"><span> </span>avuto</td>
</tr></tbody></table>
</section>
<section><h3>Indicatif</h3><table><tbody><tr><td><table><tbody><tr>
<td>(io)<span> </span></td>
<td><span> </span><b><a rel="mw:WikiLink" href="./ho#it" title="ho">ho</a></b></td>
</tr></tbody></table></td></tr></tbody></table></section></body></html>"""
            ),
            ["avere", "ho"],
        )

    def test_ja_adj_conj(self):
        self.assertEqual(
            self.transform_zim(
                """<!DOCTYPE html>
<html><head><title>Conjugaison:japonais/格好だ</title></head><body>
<section><table><tbody><tr>
<th scope="row">Neutre négatif</th>
<td><span lang="ja" class="lang-ja"><bdi><a>格好ではない</a><br/><a>格好じゃない</a></bdi></span></td>
<td>kakkou dewa nai<br/>kakkou ja nai</td></tr>
<tr>
<th scope="row">Conditionnel</th>
<td><span lang="ja" class="lang-ja"><bdi><a>格好なら</a>(ば)</bdi></span></td>
<td><span lang="ja" class="lang-ja"><bdi><a>かっこうなら</a>(ば)</bdi></span></td>
<td>kakkou nara(ba)</td>
</tr></tbody></table></section></body></html>"""
            ),
            [
                "格好ではない",
                "格好じゃない",
                "格好なら",
                "格好ならば",
                "かっこうなら",
                "かっこうならば",
            ],
        )

    def test_ja_verb_conj(self):
        self.assertEqual(
            self.transform_zim(
                """<!DOCTYPE html>
<html><head><title>Conjugaison:japonais/在る</title></head><body>
<section><table><tbody><tr>
<td><bdi lang="ja" class="lang-ja"><a>在る</a></bdi></td>
<td><bdi lang="ja" class="lang-ja"><a>ある</a></bdi></td>
<td><i>aru</i><p><i></i></p></td>
</tr></tbody></table></section></body></html>"""
            ),
            ["在る", "ある"],
        )

    def test_de_adj_annexe(self):
        self.assertEqual(
            self.transform_zim(
                """<!DOCTYPE html>
<html><head><title>Annexe:Déclinaison en allemand/herrlich</title></head><body>
<section><table><tbody><tr>
<td>der</td>
<td><bdi lang="de" class="lang-de"><a>herrliche</a></bdi></td>
</tr></tbody></table></section></body></html>"""
            ),
            ["herrliche"],
        )

    def test_ko_conj(self):
        self.assertEqual(
            self.transform_zim(
                """<!DOCTYPE html>
<html><head><title>Conjugaison:coréen/깨닫다</title></head><body>
<section><table><tbody><tr>
<td colspan="2"><span lang="ko" class="lang-ko"><bdi>깨닫-</bdi></span></td>
<td><table class="wikitable"><tbody><tr>
<td><span lang="ko" class="lang-ko"><bdi>깨달았</bdi></span>-</td>
</tr></tbody></table></td></tr></tbody></table>
<table class="wikitable"><tbody><tr>
<td><span lang="ko" class="lang-ko"><bdi>깨닫는다</bdi></span><br/>kkaedanneunda<br/><a><span class="API" title="Prononciation API">[ˀke̞.dan.nɯn.da]</span></a></td>
</tr></tbody></table></section></body></html>"""
            ),
            ["깨닫는다"],
        )

    def test_cs_conj(self):
        self.assertEqual(
            self.transform_zim(
                """<!DOCTYPE html>
<html><head><title>Conjugaison:tchèque/plavat</title></head><body>
<section><table><tbody><tr>
<td><bdi lang="cs" class="lang-cs"><a>plavu</a></bdi></td><td><bdi lang="cs" class="lang-cs"><a>plaval</a></bdi> <bdi lang="cs" class="lang-cs"><a>jsem</a></bdi> <span class="ligne-de-forme"><i>masculin</i></span><br/><bdi lang="cs" class="lang-cs"><a>plavala</a></bdi> <bdi lang="cs" class="lang-cs"><a>jsem</a></bdi> <span class="ligne-de-forme"><i>féminin</i></span></td><td><bdi lang="cs" class="lang-cs"><a>budu</a></bdi> <bdi lang="cs" class="lang-cs"><a>plavat</a></bdi></td><td><bdi lang="cs" class="lang-cs"><a>plaval</a></bdi> <bdi lang="cs" class="lang-cs"><a>bych</a></bdi> <span class="ligne-de-forme"><i>masculin</i></span><br/><bdi lang="cs" class="lang-cs"><a>plavala</a></bdi> <bdi lang="cs" class="lang-cs"><a>bych</a></bdi> <span class="ligne-de-forme"><i>féminin</i></span></td><td>—</td>
</tr></tbody></table></section></body></html>"""
            ),
            ["plavu", "plaval", "plavala", "plavat"],
        )

    def test_pt_conj(self):
        self.assertEqual(
            self.transform_zim(
                """<!DOCTYPE html>
<html><head><title>Conjugaison:portugais/tombar</title></head><body>
<section><table><tbody><tr>
<td><bdi lang="pt" class="lang-pt"><a>tombámos</a></bdi> / <br/> <small>brésilien:</small> <bdi lang="pt" class="lang-pt"><a>tombamos</a></bdi></td>
</tr></tbody></table></section></body></html>"""
            ),
            ["tombámos", "tombamos"],
        )
        self.assertEqual(
            self.transform_zim(
                """<!DOCTYPE html>
<html><head><title>Conjugaison:portugais/dizer</title></head><body>
<section><table><tbody><tr>
<td>-</td>
<td><a>diz</a><br/><a>dize</a></td>
</tr></tbody></table></section></body></html>"""
            ),
            ["diz", "dize"],
        )
