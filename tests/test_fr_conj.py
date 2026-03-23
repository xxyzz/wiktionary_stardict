from utils import XMLTestCase


class FrConjTestCase(XMLTestCase):
    edition = "fr"
    xsl_file = "conjugaison.xsl"

    def test_fr_conj(self):
        data = self.transform(
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
