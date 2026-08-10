from utils import XMLTestCase


class NlFormsTestCase(XMLTestCase):
    edition = "nl"

    def test_deadjc(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>angstfrei</title></head>
<body>
<section><h2><i>Duits</i></h2>
<section><h5><i>Woordafbreking</i></h5>
<ul><li>angst·frei</li></ul>
<table class="infobox">
<tbody><tr>
<td>am angstfreiesten<br/>am angstfreisten <br/> <span class="IPAtekst">/am ˈaŋstfʀaɪ̯əstn̩/<br/>/am ˈaŋstfʀaɪ̯stn̩/</span></td></tr>
<tr>
<td colspan="3" class="infoboxrijhoofding"><a rel="mw:WikiLink" href="./angstfrei/verbuiging" title="angstfrei/verbuiging">alle verbuigingsvormen</a></td></tr>
</tbody></table>
</section>
<section><h4><i>Bijvoeglijk naamwoord</i></h4>
<p><b>angstfrei</b></p>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [
                {
                    "forms": ["angstfrei", "am angstfreiesten", "am angstfreisten"],
                    "zim_pages": ["angstfrei/verbuiging"],
                }
            ],
        )

    def test_headword_stress_form(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>бобр</title></head>
<body>
<section><h2><i>Russisch</i></h2>
<table class="infobox">
<tbody>
<tr>
<td class="infoboxrijhoofding"><i>nominatief</i></td>
<td>бо́бр</td><td>бобры́</td></tr></tbody></table>
<section><h4><i>Zelfstandig naamwoord</i></h4>
<p><b>бо́бр</b></p>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [{"forms": ["бо́бр", "бобр", "бобры́"]}],
        )

    def test_preceding_section_table(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>weed</title></head>
<body>
<section><h2><i>Nederlands</i></h2>
<section><h5>Woordherkomst en -opbouw</h5>
<table class="infobox"><tbody><tr>
<td class="infoboxrijhoofding">naamwoord</td>
<td>weed</td>
<td>-</td></tr></tbody></table>
</section>
<section><h4><i>Zelfstandig naamwoord</i></h4>
<p><b>weed</b></p>
<ol><li>gloss</li></ol>
<section><h5>Afgeleide begrippen</h5>
<table class="infobox">
<tbody><tr>
<td class="infoboxrijhoofding">naamwoord</td>
<td>weed</td>
<td>-</td></tr>
<tr>
<td class="infoboxrijhoofding">verkleinwoord</td>
<td><a>weedje</a></td>
<td><a>weedjes</a></td></tr>
</tbody></table>
</section></section>
<section><h4><i>Zelfstandig naamwoord</i></h4>
<p><b>weed</b></p>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [{"forms": ["weed"]}, {"forms": ["weed", "weedje", "weedjes"]}],
        )

    def test_conj_section_table_forms(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>albánský</title></head>
<body>
<section><h2><i>Tsjechisch</i></h2>
<section><h4><i>Bijvoeglijk naamwoord</i></h4>
<p><b>albánský</b></p>
<ol><li>gloss</li></ol>
<section><h5><i>Vervoeging</i></h5>
<table><tbody><tr><th>stellend</th>
<td><a>albánský</a></td></tr>
<tr>
<th>vergrotend</th>
<td><a>albánštější</a></td></tr>
<tr>
<th>overtreffend</th>
<td><a>nejalbánštější</a></td></tr>
</tbody></table>
</section></section></section></body></html>""",
            [{"forms": ["albánský", "albánštější", "nejalbánštější"]}],
        )

    def test_parenthesis_in_td(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>dood</title></head>
<body>
<section><h2><i>Nederlands</i></h2>
<section><h4><i>Woordherkomst en -opbouwx</i></h4>
<table class="infobox" data-mw='{"parts":[{"template":{"target":{"wt":"-nlnoun-"}}}]}'>
<tbody><tr>
<td class="infoboxrijhoofding">naamwoord</td>
<td>dood</td>
<td>(<a>doden</a>) <a><span title="zie Opmerkingen">*</span></a></td></tr>
</tbody></table></section>
<section><h4><i>Zelfstandig naamwoord</i></h4>
<p><b>dood</b></p>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [{"forms": ["dood", "doden"]}],
        )

    def test_ignore_number_tables(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>drie</title></head>
<body>
<section><h2><i>Nederlands</i></h2>
<table class="infobox">
<tbody><tr><th><a>Telwoord</a> (nl)</th></tr>
<tr><td><a>0</a></td></tr></tbody></table>
<section><h4><i>Hoofdtelwoord</i></h4>
<p><b>drie</b></p>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [{"forms": ["drie"]}],
        )
