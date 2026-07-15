from utils import XMLTestCase


class FiConjTestCase(XMLTestCase):
    edition = "fi"
    xsl_file = "liite.xsl"

    def test_fi_liite(self):
        data = self.transform(
            """<!DOCTYPE html>
<html>
<head><title>Liite:Verbitaivutus/suomi/kirjata</title></head>
<body>
<section><h2>Persoonamuodot</h2><table class="wikitable">
<tbody><tr>
<td>minä</td>
<td><span class="Zzzz linkki" lang="fi" data-kuvaus="tm/*/v/ind.p.y1p"><a rel="mw:WikiLink" href="./kirjaan#Suomi" title="kirjaan">kirjaan</a></span></td>
<td>en <span class="Zzzz linkki" lang="fi" data-kuvaus="tm/*/v/imp.y2p imp.y2p.kon ind.kon ind.p.y3p"><a rel="mw:WikiLink" href="./kirjaa#Suomi" title="kirjaa">kirjaa</a></span></td>
</tr></tbody></table></section></body></html>"""
        )
        self.assertEqual(data, ["kirjaan", "kirjaa"])
