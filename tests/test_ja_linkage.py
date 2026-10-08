from utils import XMLTestCase


class JaLinkageTestCase(XMLTestCase):
    edition = "ja"

    def test_remove_no_ul_element(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>abandonment</title></head>
<body>
<section><h2>英語</h2>
<section><h3>名詞</h3>
<p><strong class="Latn headword" lang="en">abandonment</strong></p>
<ol><li>gloss</li></ol>
<section><h4>対義語</h4>
<ul><li><a>acquisition</a>（獲得）</li></ul>
<div class="boilerplate noprint plainlinks">
<p><span><a><img src="//thumb.wikimedia.org/wikipedia/commons/thumb/c/ce/Stubico.svg/40px-Stubico.svg.png"/></a></span>
このページは<a>スタブ（書きかけ）</a>です。<a>このページを加筆して下さる</a>協力者を求めています。</p>
</div>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ja">
<h4 class="Jpan">名詞</h4>
<p><strong class="Latn headword" lang="en">abandonment</strong></p>
<ol><li>gloss</li></ol>
<section>
<h4 class="Jpan">対義語</h4>
<ul><li>acquisition（獲得）</li></ul>
</section></section>""",
                }
            ],
        )
