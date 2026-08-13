from utils import XMLTestCase


class ElPronTestCase(XMLTestCase):
    edition = "el"

    def test_pron_sections(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>日本</title></head>
<body>
<section><h2><span>Ιαπωνικά (ja)</span></h2>
<section><h3><span class="pronunciation">Προφορά</span></h3>
<dl><dd><a title="ΔΦΑ"><span>ΔΦΑ</span></a><span> </span>: /<a><span>ɲ̟iˈhõ̞ɴ</span></a>/ <span class="ext-phonos" typeof="mw:Extension/phonos"></span></dd></dl>
</section>
<section><h3><span class="partofspeech">Κύριο όνομα</span></h3>
<p><b>日本</b></p>
<ul><li>gloss 1</li></ul>
</section>
<section><h3><span class="pronunciation">Προφορά</span></h3>
<dl><dd><a title="ΔΦΑ"><span>ΔΦΑ</span></a><span> </span>: /<a><span>ɲ̟ipˈpõ̞ɴ</span></a>/</dd></dl>
</section>
<section><h3><span class="partofspeech">Κύριο όνομα</span></h3>
<p><b>日本</b></p>
<ul><li>gloss 2</li></ul>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="el">
<h4><span class="partofspeech">Κύριο όνομα</span></h4>
<dl><dd><span>ΔΦΑ</span><span> </span>: /<span>ɲ̟iˈhõ̞ɴ</span>/ </dd></dl>
<p><b>日本</b></p>
<ul><li>gloss 1</li></ul>
</section>"""
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="el">
<h4><span class="partofspeech">Κύριο όνομα</span></h4>
<dl><dd><span>ΔΦΑ</span><span> </span>: /<span>ɲ̟ipˈpõ̞ɴ</span>/</dd></dl>
<p><b>日本</b></p>
<ul><li>gloss 2</li></ul>
</section>"""
                },
            ],
        )

    def test_parent_pron_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>φούντια</title></head>
<body>
<section><h2><span>Νέα ελληνικά (el)</span></h2>
<section><h3><span class="pronunciation">Προφορά</span> 1</h3>
<dl><dd><a title="ΔΦΑ"><span>ΔΦΑ</span></a><span> </span>: /<a><span>ˈfun.dʝa</span></a>/</dd></dl>
<section><h3><span class="partofspeech">Κλιτικός τύπος ουσιαστικού</span></h3>
<p><b>φούντια</b></p>
<ul><li>gloss 1</li></ul>
</section></section>
<section><h3><span class="pronunciation">Προφορά</span></h3>
<dl><dd><a title="ΔΦΑ"><span>ΔΦΑ</span></a><span> </span>: /<a><span>ˈfun.di.a</span></a>/</dd></dl>
<section><h3><span class="partofspeech">Κλιτικός τύπος ουσιαστικού</span></h3>
<p><b>φούντια</b></p>
<ul><li>gloss 2</li></ul>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="el">
<h4><span class="partofspeech">Κλιτικός τύπος ουσιαστικού</span></h4>
<dl><dd><span>ΔΦΑ</span><span> </span>: /<span>ˈfun.dʝa</span>/ </dd></dl>
<p><b>φούντια</b></p>
<ul><li>gloss 1</li></ul>
</section>"""
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="el">
<h4><span class="partofspeech">Κλιτικός τύπος ουσιαστικού</span></h4>
<dl><dd><span>ΔΦΑ</span><span> </span>: /<span>ˈfun.di.a</span>/</dd></dl>
<p><b>φούντια</b></p>
<ul><li>gloss 2</li></ul>
</section>"""
                },
            ],
        )
