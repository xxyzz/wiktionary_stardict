from utils import XMLTestCase


class ItEtymologyTestCase(XMLTestCase):
    edition = "it"

    def test_p_etymology(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>comprare</title></head>
<body>
<section><h2><a>Italiano</a></h2>
<section><h3>Sostantivo</h3>
<section><h4>Transitivo</h4>
<p><b data-mw='{"parts":[{"template":{"target":{"wt":"Pn"}}}]}'>comprare</b></p>
<ol><li>gloss</li></ol>
</section></section>
<section><h3><span typeof="mw:File"><a><img/></a></span><a>Etimologia</a> / <a>Derivazione</a></h3>
<p>etymology text</p>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="it">
<h4>Sostantivo</h4>
<h4>Transitivo</h4>
<p><b>comprare</b></p>
<ol><li>gloss</li></ol>
<section>
<h4>Etimologia / Derivazione</h4>
<p>etymology text</p>
</section></section>""",
                }
            ],
        )
