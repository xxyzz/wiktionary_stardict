from utils import XMLTestCase


class ZhPronTestCase(XMLTestCase):
    edition = "zh"

    def test_zh_pron(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>慥慥</title></head>
<body>
<section><h2>漢語</h2>
<section><h3>發音</h3>
<div class="standard-box zhpron"><div class="vsSwitcher" data-toggle-category="發音">
<ul><li><a>官話</a>
<dl><dd><small>(<a>拼音</a>)</small>：<span class="zhpron-monospace" lang="cmn"><a>zàozào</a></span></dd>
<dd><small>(<a>注音</a>)</small>：<span lang="cmn-Bopo" class="Bopo">ㄗㄠˋ ㄗㄠˋ</span></dd></dl></li>
<li><a>粵語</a> <small>(<a>粵拼</a>)</small>：<span style="font-family: Consolas, monospace;">cou<sup>3</sup> cou<sup>3</sup></span><span class="vsToggleElement" style="float: right;"></span></li></ul></div></div>
</section>
<section><h3>形容詞</h3>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">慥慥</strong>
</span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="zh">
<h4 class="Hant">形容詞</h4>
<ul><li>官話
<dl><dd><small>(拼音)</small>：<span class="zhpron-monospace" lang="cmn">zàozào</span></dd>
<dd><small>(注音)</small>：<span lang="cmn-Bopo" class="Bopo">ㄗㄠˋ ㄗㄠˋ</span></dd></dl></li></ul>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">慥慥</strong>
</span></p>
<ol><li>gloss</li></ol>
</section>"""
                }
            ],
        )
