from utils import XMLTestCase


class JaFormsTestCase(XMLTestCase):
    edition = "ja"

    def test_de_noun(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Montag</title></head>
<body>
<section><h2>ドイツ語</h2>
<section><h3>名詞</h3>
<p><span lang="de"><b>Montag</b></span> <span class="gender m" title="masculine gender"><span>男性</span></span> (<span class="form-of genitive-form-of lang-de">属格<b><span lang="de">Montages</span></b><span class="form-of genitive-form-of lang-de"> 又は <b><span lang="de">Montags</span></b></span></span>, <span class="form-of plural-form-of lang-de">複数形 <b><span lang="de">Montage</span></b></span>)</p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["Montag", "Montages", "Montags", "Montage"]}],
        )

    def test_alt_forms(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>スペイン語</title></head>
<body>
<section><h2>日本語</h2>
<section><h3>異表記・別形</h3>
<ul><li><span class="Jpan" lang="ja"><a>イスパニア語</a></span><span>, </span><span class="Jpan" lang="ja"><a>西語</a></span></li></ul>
</section>
<section><h3>名詞</h3>
<p><strong class="Jpan headword" lang="ja"><a>スペイン</a><a>語</a></strong><span> (</span><span class="headword-tr manual-tr tr" dir="ltr">すぺいんご</span><span>)</span><span class="headword-kanji">【<b class="Jpan" lang="ja"><a>西班牙語</a></b>】</span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["スペイン語", "イスパニア語", "西語", "西班牙語"]}],
        )
