from utils import XMLTestCase


class ElFromsTestCase(XMLTestCase):
    edition = "el"

    def test_el_table(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>θελξίνοος</title></head>
<body>
<section><h2><span>Αρχαία ελληνικά (grc)</span></h2>
<span data-mw='{"parts":[{"template":{"target":{"wt":"grc-κλίση-&apos;εύνους&apos;"}}}]}'></span>
<table><tbody><tr>
<td style="background:#e3e5e8;"><span><i><b>ονομαστική</b></i></span></td>
<td align="center"><span>ὁ</span>/<span>ἡ</span></td>
<td align="left"><a><span>θελξίν</span><span>ο</span><span>ος</span></a> <span> </span> > <a><span>θελξίν</span><span>ους</span></a></td></tr></tbody></table>
<section><h3><span class="partofspeech">Επίθετο</span></h3>
<p><b>θελξίνοος</b></p>
<ul><li>gloss</li></ul>
</section></section></body></html>""",
            [{"forms": ["θελξίνοος", "θελξίνους"]}],
        )

    def test_en_table(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>book</title></head>
<body>
<section><h2><span>Αγγλικά (en)</span></h2>
<section><h3><span class="partofspeech">Ρήμα</span></h3>
<span data-mw='{"parts":[{"template":{"target":{"wt":"en-verb-&apos;ask&apos;"}}}]}'></span><table><tbody><tr>
<td style="background:#a1bdea" align="center"><span><i>γ΄<span> </span>ενικό<span> </span>ενεστώτα</i></span></td>
<td align="center"><a><span>books</span></a></td></tr></tbody></table>
<p><b>book</b></p>
<ul><li>gloss</li></ul>
</section></section></body></html>""",
            [{"forms": ["book", "books"]}],
        )

    def test_el_inf_section_table(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>κρατώ</title></head>
<body>
<section><h2><span>Νέα ελληνικά (el)</span></h2>
<section><h3><span class="partofspeech">Ρήμα</span></h3>
<p><b>κρατώ</b></p>
<ul><li>gloss</li></ul>
<section><h4>Κλίση</h4>
<div data-mw='{"parts":[{"template":{"target":{"wt":"el-κλίσ-&apos;ζητώ&apos;"},"params":{"1":{"wt":"κρατ"},"2":{"wt":"κράτ"},"πρ1":{"wt":"[[κράτα]] - [[κράτει]]"}}}}]}'>
<div><span> </span> <span> </span> Ενεργητική φωνή</div>
<div class="NavContent">
<table><tbody><tr>
<td style="background:#c0c0c0">γ' πληθ.</td>
<td>θα κρατάν(ε) - κρατούν(ε)</td></tr></tbody></table></div></div>
</section></section></section></body></html>""",
            [{"forms": ["κρατώ", "κρατάν", "κρατάνε", "κρατούν", "κρατούνε"]}],
        )

    def test_alt_form_bg_color_tag(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>πίνω</title></head>
<body>
<section><h2><span>Αρχαία ελληνικά (grc)</span></h2>
<section><h3><span class="partofspeech">Ρήμα</span></h3>
<p><b>πίνω</b></p>
<ul><li>gloss</li></ul>
<section><h4>Άλλες μορφές</h4>
<ul><li><a><span style="background:#ffffff"><i>αιολικός τύπος</i></span></a><span> </span>: <a data-mw='{"parts":[{"template":{"target":{"wt":"l"},"params":{"1":{"wt":"πώνω"},"2":{"wt":"grc"}}}}]}'>πώνω</a></li></ul>
</section></section></section></body></html>""",
            [{"forms": ["πίνω", "πώνω"]}],
        )

    def test_alt_form_parenthesis_tag(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>αρσενικός</title></head>
<body>
<section><h2><span>Νέα ελληνικά (el)</span></h2>
<section><h3><span class="partofspeech">Επίθετο</span></h3>
<p><b>αρσενικός</b></p>
<ul><li>gloss</li></ul>
<section><h4>Άλλες μορφές</h4>
<ul><li><a>σερνικός</a> <span data-mw='{"parts":[{"template":{"target":{"wt":"ετ"}}}]}'>(</span><a><i>λαϊκότροπο</i></a><span>)</span></li></ul>
</section></section></section></body></html>""",
            [{"forms": ["αρσενικός", "σερνικός"]}],
        )
