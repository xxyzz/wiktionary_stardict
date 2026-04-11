from utils import XMLTestCase


class DeFlexionTestCase(XMLTestCase):
    edition = "de"
    xsl_file = "flexion.xsl"

    def test_de_adj_flexion(self):
        data = self.transform(
            """<!DOCTYPE html>
<html>
<head><title>Flexion:arm</title></head>
<body>
<table class="wikitable inflection-table hintergrundfarbe2"><tbody>
<tr>
<th>Nominativ</th>
<td><div style="text-align: center;">—</div></td>
<td><a rel="mw:WikiLink" href="./armer" title="armer">armer</a></td>
</tr>
</tbody></table>
</body>
</html>"""
        )
        self.assertEqual(data, ["armer"])
