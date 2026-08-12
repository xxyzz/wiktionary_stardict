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
