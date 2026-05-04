from utils import XMLTestCase


class JaEtymologyTestCase(XMLTestCase):
    edition = "ja"

    def test_above_pos(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>うつる</title></head>
<body>
<section><h2>日本語</h2>
<section><h3>語源</h3>
<p><a>古典日本語</a>「<a>うつる</a>」 &lt; 「<a>うつす</a>」の自動詞形</p>
</section>
<section><h3>動詞：移</h3>
<p><strong class="Jpan headword" lang="ja">うつる</strong></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ja">
<h4 class="Jpan">動詞：移</h4>
<p><strong class="Jpan headword" lang="ja">うつる</strong></p>
<ol><li>gloss</li></ol>
<section>
<h4 class="Jpan">語源</h4>
<p>古典日本語「うつる」 &lt; 「うつす」の自動詞形</p>
</section>
</section>""",
                }
            ],
        )

    def test_under_pos(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>東京</title></head>
<body>
<section><h2>日本語</h2>
<section><h3>固有名詞</h3>
<p><strong class="Jpan headword" lang="ja">東京</strong></p>
<ol><li>gloss</li></ol>
<section><h4>語源</h4>
<ul><li><a>京都</a>に対して<a>東</a>にある<a>京</a>（<a>都</a>）であることから</li></ul>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ja">
<h4 class="Jpan">固有名詞</h4>
<p><strong class="Jpan headword" lang="ja">東京</strong></p>
<ol><li>gloss</li></ol>
<section>
<h4 class="Jpan">語源</h4>
<ul><li>京都に対して東にある京（都）であることから</li></ul>
</section>
</section>""",
                }
            ],
        )
