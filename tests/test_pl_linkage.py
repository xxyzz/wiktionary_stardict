from utils import XMLTestCase


class PlLinkageTestCase(XMLTestCase):
    edition = "pl"

    def test_linkage_pos_index(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>read</title></head>
<body>
<section><h2>read (<span class="lang-code primary-lang-code lang-code-en" id="en"><a>język angielski</a></span>)</h2>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>czasownik</i></p>
<dl><dd>(1.1) gloss 1</dd></dl>
<p><i>rzeczownik</i></p>
<dl><dd>(2.1) gloss 2</dd></dl>
<dl><dt><span data-field="skladnia">składnia<span>:</span></span></dt><dd></dd></dl>
<dl><dt><span data-field="synonimy">synonimy<span>:</span></span></dt><dd></dd>
<dd>(1.3) <a>say</a></dd>
<dd>(1.4) <a>hear</a></dd>
<dd>(1) <span class="short-container"><span><span>daw.</span></span></span> <a>rede</a></dd></dl>
<dl><dt><span data-field="antonimy">antonimy<span>:</span></span></dt><dd></dd>
<dd>(1.1) <a>write</a></dd></dl>
<dl><dt><span data-field="etymologia">etymologia<span>:</span></span></dt><dd></dd>
<dd>etymology text 1</dd><dd>etymology text 2</dd></dl>
</section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik</i></p>
<dl><dd>(1.1) gloss 1</dd></dl>
<dl><dt><span>synonimy<span>:</span></span></dt>
<dd>(1.3) say</dd>
<dd>(1.4) hear</dd>
<dd>(1) <span class="short-container"><span><span>daw.</span></span></span> rede</dd></dl>
<dl><dt><span>antonimy<span>:</span></span></dt>
<dd>(1.1) write</dd></dl>
<dl><dt><span>etymologia<span>:</span></span></dt>
<dd>etymology text 1</dd><dd>etymology text 2</dd></dl>
</section>"""
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>rzeczownik</i></p>
<dl><dd>(2.1) gloss 2</dd></dl>
<dl><dt><span>etymologia<span>:</span></span></dt>
<dd>etymology text 1</dd><dd>etymology text 2</dd></dl>
</section>"""
                },
            ],
        )
