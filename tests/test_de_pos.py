from utils import XMLTestCase


class DePosTestCase(XMLTestCase):
    edition = "de"

    def test_gloss_list(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Keim</title></head>
<body>
<section><h2>Keim (<a>Deutsch</a>)</h2>
<section><h3><a>Substantiv</a>, <em>m</em></h3>
<p data-mw='{"parts":[{"template":{"target":{"wt":"Worttrennung"}}}]}'>Worttrennung:</p>
<dl><dd>Keim, <span style="font-size:95%;" about="#mwt8" typeof="mw:Transclusion">Plural:</span> Kei·me</dd></dl>

<p style="margin-bottom:-0.5em; font-weight:bold; " title="Phonetik" about="#mwt9" typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"Aussprache"}}}]}'>Aussprache:</p>
<dl><dd><a title="Hilfe:IPA">IPA</a><span>:</span> <span>[</span><span>kaɪ̯m</span><span>]</span></dd>
<dd><a title="Hilfe:Reime">Reime:</a> <span><a>-aɪ̯m</a></span></dd></dl>

<p data-mw='{"parts":[{"template":{"target":{"wt":"Bedeutungen"}}}]}'>Bedeutungen:</p>
<dl><dd>[2] das erste <a>Entwicklungsstadium</a> eines sich neu bildenden Lebens
<dl><dd>[a] <i>Botanik<span>:</span></i> erster Trieb einer Pflanze</dd></dl></dd></dl>
</section></section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="de">
<h4>Substantiv, <em>m</em></h4>
<section>
<dl><dd>Keim, <span style="font-size:95%;">Plural:</span> Kei·me</dd></dl>
</section>
<section>
<dl><dd>IPA<span>:</span> <span>[</span><span>kaɪ̯m</span><span>]</span></dd></dl>
</section>
<section><h4>Bedeutungen:</h4>
<dl><dd>[2] das erste Entwicklungsstadium eines sich neu bildenden Lebens
<dl><dd>[a] <i>Botanik<span>:</span></i> erster Trieb einer Pflanze</dd></dl></dd></dl>
</section>
</section>""",
                },
            ],
        )
