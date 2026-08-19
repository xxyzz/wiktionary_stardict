from utils import XMLTestCase


class ViPronTestCase(XMLTestCase):
    edition = "vi"

    def test_vi_pron(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>nước</title></head>
<body>
<section><h2>Tiếng Việt</h2>
<section><h3>Cách phát âm</h3>
<span data-mw='{"parts":[{"template":{"target":{"wt":"vie-pron"}}}]}'></span><table class="wiktvi-vie-pron wikitable" style="text-align: center;" about="#mwt20">
<caption><a>IPA</a> theo giọng</caption>
<tbody><tr>
<th class="wiktvi-vie-pron-hn-th"><a>Hà Nội</a></th><th class="wiktvi-vie-pron-h-th" colspan="2"><a>Huế</a></th><th class="wiktvi-vie-pron-sg-th"><a>Sài Gòn</a></th></tr>
</tbody></table></section>
<section><h3>Danh từ</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="vi">nước</strong></span></p>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="vi">
<h4>Danh từ</h4>
<table class="wiktvi-vie-pron wikitable" style="text-align: center;"><tbody><tr>
<th class="wiktvi-vie-pron-hn-th">Hà Nội</th><th class="wiktvi-vie-pron-h-th" colspan="2">Huế</th><th class="wiktvi-vie-pron-sg-th">Sài Gòn</th></tr>
</tbody></table>
<p><span class="headword-line"><strong class="Latn headword" lang="vi">nước</strong></span></p>
<ol><li>gloss</li></ol>
</section>"""
                },
            ],
        )
