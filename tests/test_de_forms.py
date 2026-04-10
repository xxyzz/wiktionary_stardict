from utils import XMLTestCase


class DeFormsTestCase(XMLTestCase):
    edition = "de"

    def test_verb_table(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>sehen</title></head>
<body>
<section><h2>sehen (<a>Deutsch</a>)</h2>
<section><h3>Verb, <i>unregelmäßig</i></h3>
<table class="wikitable inflection-table float-right flexbox">
<tbody>
<tr>
<th rowspan="2">Imperativ</th>
<td><small>Singular</small></td><td colspan="3"><a rel="mw:WikiLink" href="./siehe" title="siehe">siehe</a>!<br/><a rel="mw:WikiLink" href="./sieh" title="sieh">sieh</a>!</td></tr>
<th rowspan="2"><a rel="mw:WikiLink" href="./Hilfe:Perfekt" title="Hilfe:Perfekt">Perfekt</a></th><th colspan="3"><a rel="mw:WikiLink" href="./Hilfe:Partizip" title="Hilfe:Partizip">Partizip<span typeof="mw:Entity"> </span>II</a></th><th style="width: 90px;"><a rel="mw:WikiLink" href="./Hilfe:Hilfsverb" title="Hilfe:Hilfsverb">Hilfsverb</a></th>
<tr>
<td style="text-align:right" colspan="3"><a rel="mw:WikiLink" href="./gesehen" title="gesehen">gesehen</a><br/>sehen</td>
<td><a rel="mw:WikiLink" href="./haben" title="haben">haben</a></td></tr>
<tr>
<th style="font-weight:normal;" colspan="5"><div style="text-align: center;"><i>Alle weiteren Formen:</i> <a rel="mw:WikiLink" href="./Flexion:sehen" title="Flexion:sehen">Flexion:sehen</a></div></th></tr>
</tbody></table>

<p data-mw='{"parts":[{"template":{"target":{"wt":"Bedeutungen"}}}]}'>Bedeutungen:</p>
<dl><dd>[1] gloss</dd></dl>
</section></section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="de">
<h4>Verb, <i>unregelmäßig</i></h4>
<section><h4>Bedeutungen:</h4>
<dl><dd>[1] gloss</dd></dl>
</section></section>""",
                    "forms": ["sehen", "siehe", "sieh", "gesehen"],
                },
            ],
        )
