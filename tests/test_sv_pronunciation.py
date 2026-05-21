from utils import XMLTestCase


class SvPronunciationTestCase(XMLTestCase):
    edition = "sv"

    def test_sound_file(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>bok</title></head>
<body>
<section><h2>Svenska</h2>
<section><h3>Substantiv</h3>
<p><b>bok</b></p>
<ul><li><b><a title="Wiktionary:Stilguide/Uttal">uttal</a>:</b><span> </span><span class="ext-phonos"><span class="oo-ui-labelElement-label">buːk</span></span></li></ul>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="sv">
<h4>Substantiv</h4>
<p><b>bok</b></p>
<ul><li><b>uttal: </b><span class="ipa">buːk</span></li></ul>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )
