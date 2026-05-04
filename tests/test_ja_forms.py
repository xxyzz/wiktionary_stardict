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

    def test_ja_auxiliary_verb_conj(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>させる</title></head>
<body>
<section><h2>日本語</h2>
<section><h3>助動詞</h3>
<p><strong class="Jpan headword" lang="ja">させる</strong></p>
<ul><li>接続:</li></ul>
<ol><li>gloss</li></ol>
<section><h4>活用</h4>
<table class="wikitable" data-mw='{"parts":[{"template":{"target":{"wt":"日本語助動詞活用"}}}]}'>
<tbody><tr><th>未然形</th><th>連用形</th><th>終止形</th><th>連体形</th><th>仮定形</th><th>命令形</th><th>活用型</th></tr>
<tr align="center">
<td>させ</td><td>させ</td><td>させる</td><td>させる</td><td>させれ</td><td>させろ<br/>させよ</td><td>動詞下一段型</td></tr>
</tbody></table>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ja">
<h4 class="Jpan">助動詞</h4>
<p><strong class="Jpan headword" lang="ja">させる</strong></p>
<ul><li>接続:</li></ul>
<ol><li>gloss</li></ol>
</section>""",
                    "forms": ["させる", "させ", "させれ", "させろ", "させよ"],
                }
            ],
        )

    def test_ja_classical_conj(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>とし</title></head>
<body>
<section><h2>古典日本語</h2>
<section><h3>形容詞</h3>
<p><strong class="Jpan headword" lang="ja">とし</strong></p>
<ol><li>gloss</li></ol>
<section><h4>活用</h4>
<table class="wikitable" data-mw='{"parts":[{"template":{"target":{"wt":"古典日本語ク活用"}}}]}'>
<tbody><tr>
<th>基本形</th><th>語幹</th><th>未然形</th><th>連用形</th><th>終止形</th><th>連体形</th><th>已然形</th><th>命令形</th><th>活用の種類</th></tr>
<tr>
<td rowspan="2">とし</td>
<td rowspan="2">と</td>
<td>(-く)</td>
<td>-く</td>
<td>-し</td>
<td>-き</td>
<td>-けれ</td>
<td>○</td>
<td rowspan="2">ク活用</td></tr>
<tr>
<td>-から</td>
<td>-かり</td>
<td>○</td>
<td>-かる</td>
<td>○</td>
<td>-かれ</td></tr>
</tbody></table>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": [
                        "とし",
                        "とく",
                        "とき",
                        "とけれ",
                        "とから",
                        "とかり",
                        "とかる",
                        "とかれ",
                    ]
                }
            ],
        )

    def test_ja_combine_form_br(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>まぜる</title></head>
<body>
<section><h2>日本語</h2>
<section><h3>動詞</h3>
<p><strong class="Jpan headword" lang="ja">まぜる</strong></p>
<ol><li>gloss</li></ol>
<section><h4>活用</h4>
<div data-mw='{"parts":[{"template":{"target":{"wt":"日本語下一段活用"}}}]}'>
<div class="NavHead" align="left">活用と結合例</div>
<div class="NavContent">
<table class="wikitable" style="text-align:center">
<caption>ま-ぜる 動詞活用表<small>（<a>日本語の活用</a>）</small></caption>
<tbody><tr><th colspan="7"><a>ザ行下一段活用</a></th></tr>
<tr>
<th><a>語幹</a></th><th><a>未然形</a></th><th><a>連用形</a></th><th><a>終止形</a></th><th><a>連体形</a></th><th><a>仮定形</a></th><th><a>命令形</a></th></tr>
<tr>
<td>ま</td><td>ぜろ<br/>ぜよ</td></tr>
</tbody></table>
<table class="wikitable" style="text-align:center">
<caption>各活用形の基礎的な結合例</caption>
<tbody><tr><th>意味</th><th>語形</th><th>結合</th></tr>
<tr>
<td>仮定条件</td><td>まぜれば</td><td>仮定形 + <a>ば</a></td></tr>
<tr>
<td>命令</td><td>まぜろ<br/>まぜよ</td><td>命令形のみ</td></tr>
</tbody></table>
</div></div>
</section>
</section>
</section>
</body>
</html>""",
            [{"forms": ["まぜる", "まぜろ", "まぜよ", "まぜれば"]}],
        )

    def test_ja_combine_form_no_conj_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>全然</title></head>
<body>
<section><h2>日本語</h2>
<section><h3>副詞</h3>
<p><strong class="Jpan headword" lang="ja">全然</strong></p>
<ol><li>gloss</li></ol>
<div class="NavFrame" data-mw='{"parts":[{"template":{"target":{"wt":"日本語タルト活用"}}}]}'>
<div class="NavHead" align="left">活用と結合例</div>
<div class="NavContent">
<table class="wikitable" style="text-align:center">
<caption>全然 形容動詞活用表<small>（<a>日本語の活用</a>）</small></caption>
<tbody><tr><th colspan="7"><a>タルト活用</a></th></tr>
<tr>
<td>全然</td><td>(無し)</td><td>と</td><td>(たり)</td><td>たる</td><td>(無し)</td><td>(たれ)</td></tr>
</tbody></table>
<table class="wikitable" style="text-align:center">
<caption>各活用形の基礎的な結合例</caption>
<tbody><tr><th>意味</th><th>語形</th><th>結合</th></tr>
<tr>
<td>自動詞化</td><td>全然とする</td><td>連用形 + <a>する</a></td></tr>
</tbody></table>
</div></div>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": [
                        "全然",
                        "全然と",
                        "全然たり",
                        "全然たる",
                        "全然たれ",
                        "全然とする",
                    ]
                }
            ],
        )
