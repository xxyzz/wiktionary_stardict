from utils import XMLTestCase


class PlFormsTestCase(XMLTestCase):
    edition = "pl"

    def test_odmiana_czasownik_polski(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>biec</title></head>
<body>
<section><h2>biec (<span class="lang-code primary-lang-code lang-code-pl" id="pl"><a>język polski</a></span>)</h2>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>czasownik nieprzechodni niedokonany</i></p>
<dl><dd>(1.1) gloss 1</dd><dd>(1.2) gloss 2</dd><dd>(1.3) gloss 3</dd></dl>
<dl><dt><span data-field="odmiana">odmiana<span>:</span></span></dt>
<dd>(1.1-3) <div><div><table><tbody>
<tr><td><span class="potential-form"><a>będę</a>  biegło,<br/><a>będę</a>  biec</span></td></tr>
<tr><td>biegnąca, niebiegnąca</td></tr>
<tr><td>biegnąc, <a>nie</a> biegnąc </td></tr></tbody></table></div></div></dd></dl>
</section></body></html>""",
            [{"forms": ["biec", "biegło", "biegnąca", "niebiegnąca", "biegnąc"]}],
        )

    def test_odmiana_rzeczownik_polski(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>durian</title></head>
<body>
<section><h2>durian (<span class="lang-code primary-lang-code lang-code-pl" id="pl"><a>język polski</a></span>)</h2>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>rzeczownik, rodzaj męskozwierzęcy lub męskorzeczowy</i></p>
<dl><dd>(1.1) gloss 1</dd><dd>(1.2) gloss 2</dd></dl>
<dl><dt><span data-field="odmiana">odmiana<span>:</span></span></dt>
<dd>(1.1-2) <div><div><table><tbody>
<tr><td>durian / <span class="short-container"><a><span class="short-content">pot.</span></a></span> duriana</td><td>duriany</td></tr></tbody></table></div></div></dd></dl>
</section></body></html>""",
            [{"forms": ["durian", "duriana", "duriany"]}],
        )

    def test_alt_form_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>styczeń</title></head>
<body>
<section><h2>styczeń (<span class="lang-code primary-lang-code lang-code-pl" id="pl"><a>język wilamowski</a></span>)</h2>
<dl><dt><span class="field field-title fld-ortografie field-foreign" data-field="ortografie">zapisy w ortografiach alternatywnych<span>:</span></span></dt><dd></dd>
<dd><a>styćyń</a></dd></dl>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>rzeczownik, rodzaj męski</i></p>
<dl><dd>(1.1) styczeń</dd></dl>
</section></body></html>""",
            [{"forms": ["styczeń", "styćyń"]}],
        )

    def test_zh_forms(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>电车</title></head>
<body>
<section><h2>电车 (<span class="lang-code primary-lang-code lang-code-zh"><a>język chiński standardowy</a></span>)</h2>
<dl><dt><span class="field field-title fld-zapis field-keep" data-field="zapis" data-section-links="keep">zapis<span>:</span></span></dt>
<dd><span class="short-container"><span><span class="short-content">uproszcz.</span></span></span><span lang="zh"> 电车</span>, <a><span><span class="short-content">trad.</span></span></a><span lang="zh"> 電車</span></dd></dl>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>rzeczownik</i></p>
<dl><dd>(1.1) tramwaj</dd></dl>
</section></body></html>""",
            [{"forms": ["电车", "電車"]}],
        )
