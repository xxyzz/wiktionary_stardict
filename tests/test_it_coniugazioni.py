from utils import XMLTestCase


class ItConjTestCase(XMLTestCase):
    edition = "it"
    xsl_file = "coniugazioni.xsl"

    def test_it_conj(self):
        data = self.transform(
            """<!DOCTYPE html>
<html>
<head><title>Appendice:Coniugazioni/Italiano/correre</title></head>
<body><section><table><tbody>
<tr><td>avere, se intr. essere</td><td><a>correndo</a></td></tr>
<tr><td><div><table><tbody>
<tr><td><a>abbiamo</a> <a>corso</a><br/><a>siamo</a> <a>corsi</a></td></tr>
</tbody></table></div></td></tr>
</tbody></table></section></body></html>"""
        )
        self.assertEqual(data, ["correndo", "corso", "corsi"])
