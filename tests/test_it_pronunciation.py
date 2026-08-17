from utils import XMLTestCase


class ItPronunciationTestCase(XMLTestCase):
    edition = "it"

    def test_audio(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>cane</title></head>
<body>
<section><h2><a>Italiano</a></h2>
<section><h3>Sostantivo</h3>
<p><b>cane</b></p>
<ol><li>gloss</li></ol>
</section>
<section><h3>Pronuncia</h3>
<p><a title="Aiuto:IPA">AFI</a><span>: </span><span class="IPA">/ˈkaːne/</span>
<span data-mw='{"parts":[{"template":{"target":{"wt":"Audio"}}}]}'>Ascolta la pronuncia<span> </span>: </span><span typeof="mw:File"><span><audio></audio></span></span></p>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="it">
<h4>Sostantivo</h4>
<ul><li>AFI<span>: </span><span class="IPA">/ˈkaːne/</span><span><span></span></span></li></ul>
<p><b>cane</b></p>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )
