from utils import XMLTestCase


class SvFormsTestCase(XMLTestCase):
    edition = "sv"

    def test_sv_verb_er(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>sträcka</title></head>
<body>
<section><h2>Svenska</h2>
<section><h3>Verb</h3>
<table class="grammar template-sv-verb-er"><tbody>
<tr><td><span class="b-"><a>sträcks</a> (<span class="b-"><a>sträckes</a></span>)</span></td></tr>
<tr>
<th>Presens</th>
<td colspan="2" class="min"><span class="prespart-"><a>sträckande</a>, <a>sträckandes</a></span></td></tr>
</tbody></table>
<p><b>sträcka</b></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": [
                        "sträcka",
                        "sträcks",
                        "sträckes",
                        "sträckande",
                        "sträckandes",
                    ],
                }
            ],
        )

    def test_double_headword_lines(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>búa</title></head>
<body>
<section><h2>Isländska</h2>
<section><h3>Verb</h3>
<p><b>búa</b></p>
<ol><li>gloss</li></ol>
<p><b>búast við</b></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["búa", "búast við"]}],
        )
