from utils import XMLTestCase


class NlVervoegingTestCase(XMLTestCase):
    edition = "nl"
    xsl_file = "vervoeging.xsl"

    def test_nlverb(self):
        data = self.transform(
            """<!DOCTYPE html>
<html>
<head><title>rennen/vervoeging</title></head>
<body>
<section><table class="infoboxlinks" data-mw='{"parts":[{"template":{"target":{"wt":"-nlverb-"}}}]}'><tbody>
<tr>
<td colspan="1" rowspan="2" class="infoboxrijhoofding">onvoltooid</td>
<td colspan="2" class="infoboxrijhoofding">tegenwoordig</td>
<td colspan="3">rennen</td>
<td colspan="3">te rennen</td></tr>
<tr>
<td class="infoboxrijhoofding"></td><td colspan="2"><a>rennend</a></td><td colspan="3"><a>gerend</a></td><td>ev.<br/> <a>ren</a></td><td>mv. <small>verouderd</small><br/><a>rent</a></td><td colspan="2"><a>renne</a></td></tr>
</tbody></table></section></body></html>"""
        )
        self.assertEqual(
            data, ["rennen", "te rennen", "rennend", "gerend", "ren", "rent", "renne"]
        )

    def test_deadjc_decl(self):
        data = self.transform(
            """<!DOCTYPE html>
<html>
<head><title>angstfrei/verbuiging</title></head>
<body>
<section data-mw='{"parts":[{"template":{"target":{"wt":"-deadjc-decl\n"}}}]}'>
<h2>Overtreffende trap</h2>
<section><h3>Sterke verbuiging (zonder lidwoord)</h3>
<table class="infoboxlinks"><tbody>
<tr>
<th bgcolor="#F4F4F4"><a>nominatief</a></th>
<td bgcolor="#CAE1FF">—</td>
<td bgcolor="#CAE1FF">angstfrei(e)ster</td>
<td bgcolor="#CAE1FF">—</td>
<td bgcolor="#CAE1FF">angstfrei(e)ste</td>
</tr></tbody></table></section></section></body></html>"""
        )
        self.assertEqual(
            data, ["angstfreister", "angstfreiester", "angstfreiste", "angstfreieste"]
        )
