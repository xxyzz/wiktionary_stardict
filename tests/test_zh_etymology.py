from utils import XMLTestCase


class ZhEtymologyTestCase(XMLTestCase):
    edition = "zh"

    def test_zh_x(self):
        self.assertTransformEqual(
            r"""<!DOCTYPE html>
<html>
<head><title>目不識丁</title></head>
<body>
<section><h2>漢語</h2>
<section><h3>詞源</h3>
<p>出自《舊唐書．卷一二九．張延賞列傳》中<a>張弘靖</a>對士兵說的話：</p>
<dl><dd><div><dl class="zhusex"><span lang="zh-Hant" class="Hant"><span typeof="mw:LanguageVariant" data-mw-variant='{"disabled":{"t":"&lt;!-- -->「……&lt;a>今&lt;/a>&lt;a>天下&lt;/a>&lt;a>無事&lt;/a>，&lt;a>汝輩&lt;/a>&lt;a>挽&lt;/a>&lt;a>得&lt;/a>&lt;a>兩&lt;/a>&lt;a>石&lt;/a>&lt;a>力&lt;/a>&lt;a>弓&lt;/a>，&lt;a>&lt;b>不&lt;/b>如&lt;/a>&lt;a>&lt;b>識&lt;/b>&lt;/a>&lt;a>一&lt;/a>&lt;a>&lt;b>丁&lt;/b>&lt;/a>&lt;a>字&lt;/a>。」&lt;!-- -->"}}'></span></span><span class="vsHide"> <span class="skin-nightmode-reset-color" style="color:darkgreen; font-size:x-small;"><span typeof="mw:Entity">[</span><a>文言文</a>，<a>繁體</a><span typeof="mw:Entity">]</span></span></span><span class="vsToggleElement" style="color:darkgreen; font-size:x-small;padding-left:10px"></span><hr/><dd>「……現在天下太平，你們雖然能拉兩石力氣的弓，還不如去認識一個『丁』字來得有用。</dd></dl></div></dd></dl>
</section>
<section><h3>成語</h3>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">目不識丁</strong>
</span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="zh">
<h4 class="Hant">成語</h4>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">目不識丁</strong>
</span></p>
<ol><li>gloss</li></ol>
<section><h4 class="Hant">詞源</h4>
<p>出自《舊唐書．卷一二九．張延賞列傳》中張弘靖對士兵說的話：</p>
<dl><dd><div><dl class="zhusex"><span lang="zh-Hant" class="Hant">「……今天下無事，汝輩挽得兩石力弓，<b>不</b>如<b>識</b>一<b>丁</b>字。」</span><span class="vsToggleElement" style="color:darkgreen; font-size:x-small;padding-left:10px"></span><hr/><dd>「……現在天下太平，你們雖然能拉兩石力氣的弓，還不如去認識一個『丁』字來得有用。</dd></dl></div></dd></dl>
</section>
</section>"""
                }
            ],
        )
