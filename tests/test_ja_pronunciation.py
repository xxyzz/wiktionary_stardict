from utils import XMLTestCase


class JaPronTestCase(XMLTestCase):
    edition = "ja"

    def test_ja_pron(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>日本語</title></head>
<body>
<section><h2>日本語</h2>
<section><h3>発音</h3>
<span data-mw='{"parts":[{"template":{"target":{"wt":"ja-pron"}}}]}'></span>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><a title="w:東京式アクセント" class="extiw">東京式</a></span><span class="ib-brac qualifier-brac">)</span> <span lang="ja" class="Jpan">に<span style="border-top:1px solid">ほんご</span></span> <span class="Latn"><samp>[nìhóńgó]</samp></span> (<a>平板型</a> – [0])</li>
<li><a title="w:国際音声記号" class="extiw">IPA</a><sup>(<a>?</a>)</sup>:<span> </span><span class="IPA">[ɲ̟ihõ̞ŋɡo̞]</span></li>
<li><table class="audiotable"><tbody></tbody></table><span class="mw-empty-elt"></span></li></ul>
<span data-mw='{"parts":[{"template":{"target":{"wt":"ja-pron"}}}]}'></span>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><a>東京式</a></span><span class="ib-brac qualifier-brac">)</span> <span lang="ja" class="Jpan">に<span style="border-top:1px solid">っぽんご</span></span> <span class="Latn"><samp>[nìppóńgó]</samp></span> (<a>平板型</a> – [0])</li>
<li><a title="w:国際音声記号">IPA</a><sup>(<a>?</a>)</sup>:<span> </span><span class="IPA">[ɲ̟ip̚põ̞ŋɡo̞]</span></li></ul>
</section>
<section><h3>名詞</h3>
<p><strong class="Jpan headword" lang="ja">日本語</strong></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ja">
<h4 class="Jpan">名詞</h4>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content">東京式</span><span class="ib-brac qualifier-brac">)</span> <span lang="ja" class="Jpan">に<span style="border-top:1px solid">ほんご</span></span> <span class="Latn"><samp>[nìhóńgó]</samp></span> (平板型 – [0])</li>
<li>IPA:<span> </span><span class="IPA">[ɲ̟ihõ̞ŋɡo̞]</span></li></ul>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content">東京式</span><span class="ib-brac qualifier-brac">)</span> <span lang="ja" class="Jpan">に<span style="border-top:1px solid">っぽんご</span></span> <span class="Latn"><samp>[nìppóńgó]</samp></span> (平板型 – [0])</li>
<li>IPA:<span> </span><span class="IPA">[ɲ̟ip̚põ̞ŋɡo̞]</span></li></ul>
<p><strong class="Jpan headword" lang="ja">日本語</strong></p>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )

    def test_cmn_pron(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>中国</title></head>
<body>
<section><h2>中国語</h2>
<section><h3>発音</h3>
<span data-mw='{"parts":[{"template":{"target":{"wt":"cmn-pron"}}},"\n"]}'>
</span><ul><li>官話:
<ul><li>標準中国語:</li></ul>
<dl><dd><a>拼音</a>: Zhōngguó</dd>
<dd><a>ウェード式</a>: chung<sup>1</sup> kuo<sup>2</sup></dd>
<dd><a>IPA</a><small style="vertical-align: super; font-size: 75%;">(<a>?</a>)</small>: <span class="IPA">/ʈ͡ʂʊŋ⁵⁵ kwɔ³⁵/</span></dd>
<dd><table class="audiotable"></table></dd></dl>
<ul><li>四川語:</li></ul>
</li></ul>
</section>
<section><h3>固有名詞</h3>
<p><strong class="Jpan headword" lang="zh">中国</strong></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ja">
<h4 class="Jpan">固有名詞</h4>
<ul><li>官話:
<ul><li>標準中国語:</li></ul>
<dl><dd>拼音: Zhōngguó</dd>
<dd>ウェード式: chung<sup>1</sup> kuo<sup>2</sup></dd>
<dd>IPA: <span class="IPA">/ʈ͡ʂʊŋ⁵⁵ kwɔ³⁵/</span></dd></dl>
</li></ul>
<p><strong class="Jpan headword" lang="zh">中国</strong></p>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )

    def test_ipa(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>puppy</title></head>
<body>
<section><h2>英語</h2>
<section><h3>発音</h3>
<ul><li><a title="w:国際音声記号">IPA</a><span>: </span><span class="IPA">/ˈpə.pi/</span><span>, </span><span class="IPA">/ˈpʌp.i/</span></li></ul>
</section>
<section><h3>名詞</h3>
<p><strong class="Latn headword" lang="en">puppy</strong></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ja">
<h4 class="Jpan">名詞</h4>
<ul><li>IPA<span>: </span><span class="IPA">/ˈpə.pi/</span><span>, </span><span class="IPA">/ˈpʌp.i/</span></li></ul>
<p><strong class="Latn headword" lang="en">puppy</strong></p>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )
