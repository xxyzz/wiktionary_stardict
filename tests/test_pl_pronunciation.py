from utils import XMLTestCase


class PlPronunciationTestCase(XMLTestCase):
    edition = "pl"

    def test_ipa_dd_no_pos_index(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>książka</title></head>
<body>
<section><h2>książka (<span class="lang-code primary-lang-code lang-code-pl" id="pl"><a>język polski</a></span>)</h2>
<dl><dt><span data-field="wymowa">wymowa<span>:</span></span></dt>
<dd><span class="ext-phonos" typeof="mw:Extension/phonos"></span>, <a title="Aneks:IPA">IPA</a>:<span> </span><span title="To jest wymowa w zapisie IPA; zobacz hasło IPA w Wikipedii" class="ipa">[ˈcɕɔ̃w̃ʃka]</span></dd></dl>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>rzeczownik, rodzaj żeński</i></p>
<dl><dd>(1.1) gloss</dd></dl>
</section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>rzeczownik, rodzaj żeński</i></p>
<dl><dd>IPA:<span> </span><span title="To jest wymowa w zapisie IPA; zobacz hasło IPA w Wikipedii" class="ipa">[ˈcɕɔ̃w̃ʃka]</span></dd></dl>
<dl><dd>(1.1) gloss</dd></dl>
</section>"""
                }
            ],
        )

    def test_pos_index_nested_dl(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>read</title></head>
<body>
<section><h2>read (<span class="lang-code primary-lang-code lang-code-en" id="en"><a>język angielski</a></span>)</h2>
<dl><dt><span data-field="wymowa">wymowa<span>:</span></span></dt>
<dd>(1.1-6, 2.1)
<dl><dd><a title="Aneks:IPA">IPA</a>:<span> </span><span>/riːd/</span></dd></dl></dd>
<dd>(3.1-2)
<dl><dd><a title="Aneks:IPA">IPA</a>:<span> </span>/red/</dd></dl></dd></dl>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>czasownik</i></p>
<dl><dd>(1.1) gloss 1</dd></dl>
<p><i>rzeczownik</i></p>
<dl><dd>(2.1) gloss 2</dd></dl>
<p><i>czasownik, forma fleksyjna</i></p>
<dl><dd>(3.1) gloss 3</dd></dl>
</section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik</i></p>
<dl><dd>IPA:<span> </span><span>/riːd/</span></dd></dl>
<dl><dd>(1.1) gloss 1</dd></dl>
</section>"""
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>rzeczownik</i></p>
<dl><dd>IPA:<span> </span><span>/riːd/</span></dd></dl>
<dl><dd>(2.1) gloss 2</dd></dl>
</section>"""
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik, forma fleksyjna</i></p>
<dl><dd>IPA:<span> </span>/red/</dd></dl>
<dl><dd>(3.1) gloss 3</dd></dl>
</section>"""
                },
            ],
        )

    def test_pos_index_dl(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>palić</title></head>
<body>
<section><h2>palić (<span class="lang-code primary-lang-code lang-code-hsb" id="hsb"><a>język górnołużycki</a></span>)</h2>
<dl><dt><span data-field="wymowa">wymowa<span>:</span></span></dt>
<dd>(1.1) <a title="Aneks:IPA">IPA</a>:<span> </span><span class="ipa">/ˈpalit͡ʃ/</span></dd>
<dd>(2.1) <a title="Aneks:IPA">IPA</a>:<span> </span><span class="ipa">/ˈpalit͡ʃ sɔ/</span></dd></dl>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>czasownik</i></p>
<dl><dd>(1.1) gloss 1</dd></dl>
<p><i>czasownik</i></p>
<dl><dd>(2.1) gloss 2</dd></dl>
</section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik</i></p>
<dl><dd>(1.1) IPA:<span> </span><span class="ipa">/ˈpalit͡ʃ/</span></dd></dl>
<dl><dd>(1.1) gloss 1</dd></dl>
</section>"""
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik</i></p>
<dl><dd>(2.1) IPA:<span> </span><span class="ipa">/ˈpalit͡ʃ sɔ/</span></dd></dl>
<dl><dd>(2.1) gloss 2</dd></dl>
</section>"""
                },
            ],
        )
