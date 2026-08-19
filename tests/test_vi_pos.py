from utils import XMLTestCase


class ViPOSTestCase(XMLTestCase):
    edition = "vi"

    def test_short_example(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>nước</title></head>
<body>
<section><h2 id="Tiếng_Việt">Tiếng Việt</h2>
<section><h3 id="Danh_từ">Danh từ</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="vi">nước</strong></span></p>
<ol><li>gloss
<dl><dd><div class="h-usage-example"><i class="Latn mention e-example" lang="vi"><b>Nước</b> mưa.</i></div></dd>
<dd><div class="h-usage-example"><i class="Latn mention e-example" lang="vi"><b>Nước</b> lũ.</i></div></dd></dl></li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="vi">
<h4>Danh từ</h4>
<p><span class="headword-line"><strong class="Latn headword" lang="vi">nước</strong></span></p>
<ol><li>gloss
<dl><dd><div class="h-usage-example"><i class="Latn mention e-example" lang="vi"><b>Nước</b> lũ.</i></div></span></dd></li></ol>
</section>""",
                    "forms": ["nước"],
                    "lang": "Tiếng Việt",
                    "ids": ["Tiếng_Việt", "Danh_từ"],
                },
            ],
        )

    def test_p_infl_inline(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>dog</title></head>
<body>
<section><h2>Tiếng Anh</h2>
<section><h3>Danh từ</h3>
<p><span class="infl-inline"><b>dog</b> (<i>số nhiều</i><span> </span><span class="form-of plural-form-of lang-en"><b><a>dogs</a></b></span>)</span></p>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="vi">
<h4>Danh từ</h4>
<p><span class="infl-inline"><b>dog</b> (<i>số nhiều</i><span> </span><span class="form-of plural-form-of lang-en"><b>dogs</b></span>)</span></p>
<ol><li>gloss</li></ol>
</section>""",
                    "forms": ["dog", "dogs"],
                },
            ],
        )

    def test_third_person_singular_of(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>books</title></head>
<body>
<section><h2>Tiếng Anh</h2>
<section><h3>Danh từ</h3>
<p><b>books</b></p>
<ol><li><span class="use-with-mention" data-mw='{"parts":[{"template":{"target":{"wt":"third-person singular of"},"params":{"1":{"wt":"[[book]]"}},"i":0}}]}'><a>Động từ</a> chia ở <a>ngôi thứ ba</a> <a>số ít</a><span> </span>của<span> </span><span class="mention"><a>book</a></span></span></li></ol>
</section></section></body></html>""",
            [{"form_of_only": True, "form_of_targets": ["book"]}],
        )
