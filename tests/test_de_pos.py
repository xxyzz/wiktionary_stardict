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
                    "def": """<section class="mw-parser-output" dir="ltr" lang="de">
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

    def test_examples(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Buch</title></head>
<body>
<section><h2>Buch (<a>Deutsch</a>)</h2>
<section><h3><a>Substantiv</a>, <em>n</em></h3>
<p data-mw='{"parts":[{"template":{"target":{"wt":"Bedeutungen"}}}]}'>Bedeutungen:</p>
<dl><dd>[1] gloss</dd></dl>
<p data-mw='{"parts":[{"template":{"target":{"wt":"Beispiele"}}}]}'>Beispiele:</p>
<dl><dd>[1] „Das <i id="mwAfA">Buch</i> bleibt bis tief ins Hochmittelalter hinein ein Gegenstand der Verehrung und des Respekts, ein Numinosum als Wort- und Zeichenträger, ganz abgesehen von der Kostbarkeit im materiellen Sinn.“<sup class="mw-ref reference"></sup></dd>
<dd>[1] <i>Bücher</i> staubt man am besten mit einem speziellen Besen ab, der aus sehr feinem Ziegenhaar besteht.</dd>
<dd>[6–9] <span class="mw-empty-elt"></span></dd></dl>
</section></section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="de">
<h4>Substantiv, <em>n</em></h4>
<section><h4>Bedeutungen:</h4>
<dl><dd>[1] gloss</dd></dl>
</section><section>
<h4>Beispiele:</h4>
<dl><dd>[1] <i>Bücher</i> staubt man am besten mit einem speziellen Besen ab, der aus sehr feinem Ziegenhaar besteht.</dd></dl>
</section></section>""",
                },
            ],
        )

    def test_example_ul(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>schade</title></head>
<body>
<section><h2>schade (<a>Niederländisch</a>)</h2>
<section><h3><a>Substantiv</a>, <em>f</em></h3>
<p data-mw='{"parts":[{"template":{"target":{"wt":"Bedeutungen"}}}]}'>Bedeutungen:</p>
<dl><dd>[1] gloss</dd></dl>
<p data-mw='{"parts":[{"template":{"target":{"wt":"Beispiele"}}}]}'>Beispiele:</p>
<ul><li><i><a rel="mw:WikiLink" href="./Belgien" title="Belgien">Belgien</a>:</i></li></ul>
<dl><dd>[1] “De ingenieurs moeten de precieze <i>schade</i> nog opmeten.”<sup class="mw-ref reference"></sup>
<dl><dd>„Die Ingenieure müssen den genauen <i>Schaden</i> noch begutachten.“</dd></dl></dd></dl>
<ul><li><i><a rel="mw:WikiLink" href="./Niederlande" title="Niederlande">Niederlande</a>:</i></li></ul>
<dl><dd>[1] “Door de brand ontstond aan en in de woning flinke <i>schade.</i>”<sup class="mw-ref reference"></sup>
<dl><dd>„Durch den Brand entstand an und in der Wohnung erheblicher <i>Schaden.</i>“</dd></dl></dd></dl>
<p title="Parömien" data-mw='{"parts":[{"template":{"target":{"wt":"Sprichwörter"}}}]}'>Sprichwörter:</p>
<dl><dd>[1] <a rel="mw:WikiLink" href="./door_schade_en_schande_wijs_worden?action=edit&amp;redlink=1" title="door schade en schande wijs worden" class="new">door <i>schade</i> en schande wordt men wijs</a></dd></dl>
</section></section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="de">
<h4>Substantiv, <em>f</em></h4>
<section><h4>Bedeutungen:</h4>
<dl><dd>[1] gloss</dd></dl>
</section><section>
<h4>Beispiele:</h4>
<ul><li><i><a href="bword://Belgien" title="Belgien">Belgien</a>:</i></li></ul>
<dl><dd>[1] “De ingenieurs moeten de precieze <i>schade</i> nog opmeten.”
<dl><dd>„Die Ingenieure müssen den genauen <i>Schaden</i> noch begutachten.“</dd></dl></dd></dl>
<ul><li><i><a href="bword://Niederlande" title="Niederlande">Niederlande</a>:</i></li></ul>
<dl><dd>[1] “Door de brand ontstond aan en in de woning flinke <i>schade.</i>”
<dl><dd>„Durch den Brand entstand an und in der Wohnung erheblicher <i>Schaden.</i>“</dd></dl></dd></dl>
</section></section>""",
                },
            ],
        )
