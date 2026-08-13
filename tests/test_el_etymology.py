from utils import XMLTestCase


class ElEtymologyTestCase(XMLTestCase):
    edition = "el"

    def test_parent_etymology_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>ήλιο</title></head>
<body>
<section><h2><span>Νέα ελληνικά (el)</span></h2>
<section><h3><span data-mw='{"parts":[{"template":{"target":{"wt":"ετυμολογία"}}}]}'><span><span></span></span> Ετυμολογία </span> 1</h3>
<dl><dd>etymology 1</dd></dl>
<section><h4><span class="pronunciation">Προφορά</span></h4>
<dl><dd><a title="ΔΦΑ"><span>ΔΦΑ</span></a><span> </span>: /<span>ˈi.li.o</span>/</dd></dl>
</section>
<section><h4><span class="partofspeech">Ουσιαστικό</span></h4>
<p><b>ήλιο</b></p>
<ul><li>gloss 1</li></ul>
</section></section>
<section><h3><span data-mw='{"parts":[{"template":{"target":{"wt":"ετυμολογία"}}}]}'><span><span></span></span> Ετυμολογία </span> 2</h3>
<dl><dd>etymology 2</dd></dl>
<section><h4><span class="pronunciation">Προφορά</span></h4>
<dl><dd><a title="ΔΦΑ"><span>ΔΦΑ</span></a><span> </span>: /<span>ˈi.ʎo</span>/</dd></dl>
</section>
<section><h4><span class="partofspeech">Κλιτικός τύπος ουσιαστικού</span></h4>
<p><b>ήλιο</b></p>
<ul><li>gloss 2</li></ul>
</section></section>
</section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="el">
<h4><span class="partofspeech">Ουσιαστικό</span></h4>
<dl><dd><span>ΔΦΑ</span><span> </span>: /<span>ˈi.li.o</span>/</dd></dl>
<p><b>ήλιο</b></p>
<ul><li>gloss 1</li></ul>
<section><h4><span><span><span></span></span> Ετυμολογία </span> 1</h4>
<dl><dd>etymology 1</dd></dl>
</section></section>"""
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="el">
<h4><span class="partofspeech">Κλιτικός τύπος ουσιαστικού</span></h4>
<dl><dd><span>ΔΦΑ</span><span> </span>: /<span>ˈi.ʎo</span>/</dd></dl>
<p><b>ήλιο</b></p>
<ul><li>gloss 2</li></ul>
<section><h4><span><span><span></span></span> Ετυμολογία </span> 2</h4>
<dl><dd>etymology 2</dd></dl>
</section></section>"""
                },
            ],
        )

    def test_preceding_etymology_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>ίδιος</title></head>
<body>
<section><h2><span>Νέα ελληνικά (el)</span></h2>
<section><h3><span data-mw='{"parts":[{"template":{"target":{"wt":"ετυμολογία"}}}]}'><span><span></span></span> Ετυμολογία </span> 1</h3>
<dl><dd>etymology 1</dd></dl>
</section>
<section><h3><span class="pronunciation">Προφορά 1</span></h3>
<dl><dd><a title="ΔΦΑ"><span>ΔΦΑ</span></a><span> </span>: /<span>ˈi.ðʝos</span>/</dd></dl>
</section>
<section><h3><span class="partofspeech">Επίθετο</span></h3>
<p><b>ίδιος</b></p>
<ul><li>gloss 1</li></ul>
</section>
<section><h3><span data-mw='{"parts":[{"template":{"target":{"wt":"ετυμολογία"}}}]}'><span><span></span></span> Ετυμολογία </span> 2</h3>
<dl><dd>etymology 2</dd></dl>
</section>
<section><h3><span class="pronunciation">Προφορά 2</span></h3>
<dl><dd><a title="ΔΦΑ"><span>ΔΦΑ</span></a><span> </span>: /<span>ˈi.ði.os</span>/</dd></dl>
</section>
<section><h3><span class="partofspeech">Επίθετο</span></h3>
<p><b>ίδιος</b></p>
<ul><li>gloss 2</li></ul>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="el">
<h4><span class="partofspeech">Επίθετο</span></h4>
<dl><dd><span>ΔΦΑ</span><span> </span>: /<span>ˈi.ðʝos</span>/</dd></dl>
<p><b>ίδιος</b></p>
<ul><li>gloss 1</li></ul>
<section><h4><span><span><span></span></span> Ετυμολογία </span> 1</h4>
<dl><dd>etymology 1</dd></dl>
</section></section>"""
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="el">
<h4><span class="partofspeech">Επίθετο</span></h4>
<dl><dd><span>ΔΦΑ</span><span> </span>: /<span>ˈi.ði.os</span>/</dd></dl>
<p><b>ίδιος</b></p>
<ul><li>gloss 2</li></ul>
<section><h4><span><span><span></span></span> Ετυμολογία </span> 2</h4>
<dl><dd>etymology 2</dd></dl>
</section></section>"""
                },
            ],
        )
