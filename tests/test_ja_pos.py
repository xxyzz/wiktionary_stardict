from utils import XMLTestCase


class JaPOSTestCase(XMLTestCase):
    edition = "ja"

    def test_shortest_example(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>良好</title></head>
<body>
<section><h2><span>日本語</span></h2>
<section><h3><span>形容動詞</span></h3>
<p><strong class="Jpan headword" lang="ja"><a>良</a><a>好</a></strong><span> (</span><span class="headword-tr manual-tr tr" dir="ltr"><a>りょうこう</a></span><span>)</span></p>
<ol><li><a>状態</a>や<a>結果</a>、<a>成績</a>が良く、<a>このましい</a>こと。
<dl><dd><span data-mw='{"parts":[{"template":{"target":{"wt":"ant"}}}]}'>対義語: </span><span class="Jpan" lang="ja">劣悪</span><span>, </span><span class="Jpan" lang="ja" about="#mwt9">険悪</span><span>, </span><span class="Jpan" lang="ja">不良</span></dd></dl>
<ul><li><div class="h-usage-example"><i class="Jpan mention e-example" lang="ja">治療の結果、体調は<b>良好</b>だ。</i></div></li>
<li><div class="h-usage-example">経過<b>良好</b></div></li></ul></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ja">
<h4 class="Jpan"><span>形容動詞</span></h4>
<p><strong class="Jpan headword" lang="ja">良好</strong><span> (</span><span class="headword-tr manual-tr tr" dir="ltr">りょうこう</span><span>)</span></p>
<ol><li>状態や結果、成績が良く、このましいこと。
<dl><dd><span>対義語: </span><span class="Jpan" lang="ja">劣悪</span><span>, </span><span class="Jpan" lang="ja">険悪</span><span>, </span><span class="Jpan" lang="ja">不良</span></dd></dl>
<ul><li><div class="h-usage-example">経過<b>良好</b></div></li></ul></li></ol>
</section>""",
                    "forms": ["良好"],
                }
            ],
        )

    def test_form_of(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>天麩羅</title></head>
<body>
<section><h2>日本語</h2>
<section><h3>和語の漢字表記</h3>
<link rel="mw:PageProp/Category" href="./カテゴリ:日本語_和語の漢字表記"/>
<p><span lang="ja" data-mw='{"parts":[{"template":{"target":{"wt":"jachars"}}}]}'><b><a>天</a> <a>麩</a> <a>羅</a></b></span></p>
<ol><li>「<a>てんぷら</a>」参照。</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ja">
<h4 class="Jpan">和語の漢字表記</h4>
<p><span lang="ja"><b>天 麩 羅</b></span></p>
<ol><li>「てんぷら」参照。</li></ol>
</section>""",
                    "forms": ["天麩羅"],
                    "form_of_only": True,
                    "form_of_targets": ["てんぷら"],
                }
            ],
        )
