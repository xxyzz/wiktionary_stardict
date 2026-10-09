from utils import XMLTestCase


class DePronTestCase(XMLTestCase):
    edition = "de"

    def test_empty_ipa(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>adhere</title></head>
<body>
<section><h2>adhere (<a>Englisch</a>)</h2>
<section><h3><a>Verb</a></h3>
<p data-mw='{"parts":[{"template":{"target":{"wt":"Worttrennung"}}}]}'>Worttrennung:</p>
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
                    "images": [],
                },
            ],
        )

    def test_nested_ipa(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Garage</title></head>
<body>
<section><h2>Garage (<a>Deutsch</a>)</h2>
<section><h3><a>Substantiv</a></h3>
<p data-mw='{"parts":[{"template":{"target":{"wt":"Aussprache"}}}]}'>Aussprache:</p>
<dl><dd><a title="Hilfe:IPA">IPA</a><span>:</span>
<dl><dd><i><a>Deutschland</a>:</i> <span>[</span><span class="ipa">ɡaˈʁaːʒə</span><span>]</span><sup class="mw-ref reference"></sup></dd>
<dd><i><a>Österreich</a>:</i> <span>[</span><span class="ipa">ɡaˈʁaːʃ</span><span>]</span><sup></sup>, <span>[</span><span class="ipa">ɡaˈʁaːʃə</span><span>]</span></dd></dl></dd></dl>
<p data-mw='{"parts":[{"template":{"target":{"wt":"Bedeutungen"}}}]}'>Bedeutungen:</p>
<dl><dd>[1] gloss</dd></dl>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="de">
<h4>Substantiv</h4>
<dl><dd>IPA<span>:</span>
<dl><dd><i>Deutschland:</i> <span>[</span><span class="ipa">ɡaˈʁaːʒə</span><span>]</span></dd>
<dd><i>Österreich:</i> <span>[</span><span class="ipa">ɡaˈʁaːʃ</span><span>]</span><sup></sup>, <span>[</span><span class="ipa">ɡaˈʁaːʃə</span><span>]</span></dd></dl></dd></dl>
<section><h4>Bedeutungen:</h4>
<dl><dd>[1] gloss</dd></dl>
</section></section>""",
                },
            ],
        )
