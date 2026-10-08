from utils import XMLTestCase


class DePronTestCase(XMLTestCase):
    edition = "de"

    def test_empty_ipa(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>adhere</title></head>
<body>
<section><h2>adhere (<a>Deutsch</a>)</h2>
<section><h3><a>Verb</a></h3>
<p data-mw='{"parts":[{"template":{"target":{"wt":"Aussprache"}}}]}'>Aussprache:</p>
<dl><dd><a title="Hilfe:IPA">IPA</a><span>:</span> <span>[</span><span class="ipa">…</span><span>]</span></dd>
<dd><a title="Hilfe:Hörbeispiele">Hörbeispiele:</a> <span><span title="Lautsprecherbild"><img resource="./Datei:Loudspeaker.svg" src="//thumb.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/20px-Loudspeaker.svg.png?utm_source=de.wiktionary.org&amp;utm_campaign=parser&amp;utm_content=thumbnail"/></span></span><span><span> </span></span><a href="//upload.wikimedia.org/wikipedia/commons/9/9e/En-us-adhere.ogg?utm_source=de.wiktionary.org&amp;utm_campaign=rest&amp;utm_content=original">adhere<span> </span>(US-amerikanisch)</a><sup><span> </span>(<a title="Datei:En-us-adhere.ogg">Info</a>)</sup></dd></dl>
<p data-mw='{"parts":[{"template":{"target":{"wt":"Bedeutungen"}}}]}'>Bedeutungen:</p>
<dl><dd>[1] gloss</dd></dl>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="de">
<h4>Verb</h4>
<section><h4>Bedeutungen:</h4>
<dl><dd>[1] gloss</dd></dl>
</section></section>""",
                },
            ],
        )
