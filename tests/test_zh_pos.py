from utils import XMLTestCase


class ZhPOSTestCase(XMLTestCase):
    edition = "zh"

    def test_shortest_example(self):
        self.assertTransformEqual(
            r"""<!DOCTYPE html>
<html>
<head><title>詞典</title></head>
<body>
<section><h2>漢語</h2>
<section><h3>名詞</h3>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">詞典</strong>
</span></p>
<ol><li>gloss
<dl><dd><span lang="zh-Hant" class="Hant" data-mw='{"parts":[{"template":{"target":{"wt":"zh-x"}}}]}' id="mwNQ"><span typeof="mw:LanguageVariant" data-mw-variant='{"disabled":{"t":"&lt;!-- -->&lt;a>牛津&lt;/a>&lt;a>英語&lt;/a>&lt;b>詞典&lt;/b>&lt;!-- -->"}}'></span></span><span lang="zh-Hani" class="Hani">／</span><span lang="zh-Hans" class="Hans"><span typeof="mw:LanguageVariant" data-mw-variant='{"disabled":{"t":"&lt;!-- -->&lt;a>牛津&lt;/a>&lt;a>英语&lt;/a>&lt;b>词典&lt;/b>&lt;!-- -->"}}'></span></span><span typeof="mw:Entity" about="#mwt7"> </span><span> ―</span><span> </span><span> </span><span lang="zh-Latn" style="color:#404D52" class="skin-nightmode-reset-color"><i>Niújīn Yīngyǔ <b>Cídiǎn</b></i></span><link rel="mw:PageProp/Category" href="./Category:有使用例的官話詞" about="#mwt7" id="mwPA"/></dd>
<dd><span lang="zh-Hant" class="Hant" data-mw='{"parts":[{"template":{"target":{"wt":"zh-x"}}}]}'><span typeof="mw:LanguageVariant" data-mw-variant='{"disabled":{"t":"&lt;!-- -->&lt;a>英&lt;/a>&lt;a>漢&lt;/a>&lt;b>詞典&lt;/b>&lt;!-- -->"}}'></span></span><span lang="zh-Hani" class="Hani">／</span><span lang="zh-Hans" class="Hans"><span typeof="mw:LanguageVariant" data-mw-variant='{"disabled":{"t":"&lt;!-- -->&lt;a>英&lt;/a>&lt;a>汉&lt;/a>&lt;b>词典&lt;/b>&lt;!-- -->"}}'></span></span><span> </span><span> ―</span><span> </span><span> </span><span lang="zh-Latn" style="color:#404D52" class="skin-nightmode-reset-color"><i>Yīng–Hàn <b>cídiǎn</b></i></span></dd></dl>
</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="zh">
<h4>名詞</h4>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">詞典</strong>
</span></p>
<ol><li>gloss
<dl><dd><span lang="zh-Hant" class="Hant">英漢<b>詞典</b></span><span lang="zh-Hani" class="Hani">／</span><span lang="zh-Hans" class="Hans">英汉<b>词典</b></span><span> </span><span> ―</span><span> </span><span> </span><span lang="zh-Latn" style="color:#404D52" class="skin-nightmode-reset-color"><i>Yīng–Hàn <b>cídiǎn</b></i></span></dd></dl>
</li></ol></li></ol>
</section>"""
                }
            ],
        )
