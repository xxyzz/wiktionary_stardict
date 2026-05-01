from utils import XMLTestCase


class ZhFormsTestCase(XMLTestCase):
    edition = "zh"

    def test_zh_forms_th_sup(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>白麵</title></head>
<body>
<section><h2>漢語</h2>
<span data-mw='{"parts":[{"template":{"target":{"wt":"zh-forms"}}}]}'>
</span><table>
<tbody><tr>
<th colspan="2"></th></tr>
<tr>
<th style="padding: 0.5em;border: 1px solid var(--border-color-base,#aaa);background: var(--wikt-palette-cyan, #eaffff);color: inherit;font-weight: normal;font-size: smaller;" colspan="2"><a rel="mw:WikiLink" href="./正體" title="正體">正體</a>/<a rel="mw:WikiLink" href="./繁體" title="繁體">繁體</a> <span typeof="mw:LanguageVariant" data-mw-variant='{"disabled":{"t":"&lt;span>(&lt;span lang=\\"zh-Hant\\" class=\\"Hant\\">&lt;!-- -->&lt;a>&lt;span typeof=\\"mw:LanguageVariant\\" data-mw-variant=&apos;{\\"disabled\\":{\\"t\\":\\"白麵\\"}}&apos;>&lt;/span>&lt;/a>/&lt;!-- -->&lt;a>&lt;span typeof=\\"mw:LanguageVariant\\" data-mw-variant=&apos;{\\"disabled\\":{\\"t\\":\\"白麪\\"}}&apos;>&lt;/span>&lt;/a>&lt;/span>)&lt;/span>\n| lang=\\"zh-Hant\\" class=\\"Hant\\" | &lt;!-- -->&lt;a>&lt;span typeof=\\"mw:LanguageVariant\\" data-mw-variant=&apos;{\\"disabled\\":{\\"t\\":\\"白\\"}}&apos;>&lt;/span>&lt;/a>\n| lang=\\"zh-Hant\\" class=\\"Hant\\" | &lt;!-- -->&lt;a>&lt;span typeof=\\"mw:LanguageVariant\\" data-mw-variant=&apos;{\\"disabled\\":{\\"t\\":\\"麵\\"}}&apos;>&lt;/span>&lt;/a>/&lt;!-- -->&lt;a>&lt;span typeof=\\"mw:LanguageVariant\\" data-mw-variant=&apos;{\\"disabled\\":{\\"t\\":\\"麪\\"}}&apos;>&lt;/span>&lt;/a>"}}'></span></th></tr>
<tr>
<th colspan="2"><a>簡體</a> <span typeof="mw:LanguageVariant" data-mw-variant='{"disabled":{"t":"&lt;span>(&lt;span lang=\\"zh-Hans\\" class=\\"Hans\\">&lt;!-- -->&lt;a>&lt;span typeof=\\"mw:LanguageVariant\\" data-mw-variant=&apos;{\\"disabled\\":{\\"t\\":\\"白面\\"}}&apos;>&lt;/span>&lt;/a>&lt;sup>&lt;span class=\\"explain\\" title=\\"此形式還有其他意義。\\">*&lt;/span>&lt;/sup>&lt;/span>)&lt;/span>\n| lang=\\"zh-Hans\\" class=\\"Hans\\" | &lt;!-- -->&lt;a>&lt;span typeof=\\"mw:LanguageVariant\\" data-mw-variant=&apos;{\\"disabled\\":{\\"t\\":\\"白\\"}}&apos;>&lt;/span>&lt;/a>\n| lang=\\"zh-Hans\\" class=\\"Hans\\" | &lt;!-- -->&lt;a>&lt;span typeof=\\"mw:LanguageVariant\\" data-mw-variant=&apos;{\\"disabled\\":{\\"t\\":\\"面\\"}}&apos;>&lt;/span>&lt;/a>"}}'></span></th></tr>
</tbody></table>
<section><h3>名詞</h3>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">白麵</strong>
</span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["白麵", "白麪", "白面"]}],
        )

    def test_zh_forms_alt_forms(self):
        self.assertTransformEqual(
            r"""<!DOCTYPE html>
<html>
<head><title>司奶</title></head>
<body>
<section><h2>漢語</h2>
<span data-mw='{"parts":[{"template":{"target":{"wt":"zh-forms"}}}]}'></span><table>
<tbody><tr>
<th colspan="2">異體</th>
<td colspan="2"><div typeof="mw:LanguageVariant" data-mw-variant='{"disabled":{"t":"&lt;div class=\"vsSwitcher\" data-toggle-category=\"異體字\">&lt;div class=\"vsShow\">&lt;span style=\"white-space:nowrap;\">&lt;span class=\"Hani\" lang=\"zh\">&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"&amp;lt;!---->&amp;lt;a>司乃&amp;lt;/a>&amp;lt;!---->\"}}&apos;>&lt;/span>&lt;/span>&lt;/span>&lt;span style=\"white-space:nowrap;\">&lt;span class=\"Hant\" lang=\"zh-Hant\">&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"&amp;lt;!---->&amp;lt;a>獅奈&amp;lt;/a>&amp;lt;!---->\"}}&apos;>&lt;/span>&lt;/span>&lt;span class=\"Hani\" lang=\"zh\">&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"&amp;lt;!---->／&amp;lt;!---->\"}}&apos; id=\"mwJg\">&lt;/span>&lt;/span>&lt;span class=\"Hans\" lang=\"zh-Hans\">&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"&amp;lt;!---->&amp;lt;a>狮奈&amp;lt;/a>&amp;lt;!---->\"}}&apos;>&lt;/span>&lt;/span>&lt;/span>&lt;/div>&lt;div class=\"vsHide\">&lt;span style=\"white-space:nowrap;\">&lt;span class=\"Hani\" lang=\"zh\">&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"&amp;lt;!---->&amp;lt;a>西乃&amp;lt;/a>&amp;lt;!---->\"}}&apos; id=\"mwYA\">&lt;/span>&lt;/span>&lt;/span>&lt;/div>&lt;span class=\"vsToggleElement\">&lt;span typeof=\"mw:Entity\"> &lt;/span>&lt;/span>&lt;/div>"}}'></div></td></tr>
</tbody></table>
<section><h3>名詞</h3>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">司奶</strong>
</span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["司奶", "司乃", "獅奈", "狮奈", "西乃"]}],
        )

    def test_ja_verb_suru(self):
        self.assertTransformEqual(
            r"""<!DOCTYPE html>
<html>
<head><title>加速</title></head>
<body>
<section><h2>日語</h2>
<section><h3>名詞</h3>
<p><span class="headword-line"><strong class="Jpan headword" lang="ja"><span typeof="mw:LanguageVariant" data-mw-variant='{"disabled":{"t":"&lt;ruby>加&lt;rp id=\"mwAXM\">(&lt;/rp>&lt;rt>&lt;!-- -->&lt;a>&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"か\"}}&apos;>&lt;/span>&lt;/a>&lt;/rt>&lt;rp>)&lt;/rp>&lt;/ruby>&lt;ruby>速&lt;rp>(&lt;/rp>&lt;rt>&lt;!-- -->&lt;a>&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"そく\"}}&apos;>&lt;/span>&lt;/a>&lt;/rt>&lt;rp>)&lt;/rp>&lt;/ruby>&lt;!-- -->&lt;a>&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"する\"}}&apos;>&lt;/span>&lt;/a>"}}'></span></strong> <a>•</a> (<span class="headword-tr tr" dir="ltr"><span typeof="mw:LanguageVariant" data-mw-variant='{"disabled":{"t":"&lt;!---->&lt;span class=\"Latn\" lang=\"ja\">&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"&amp;lt;!-- -->&amp;lt;a>&amp;lt;span typeof=\\\"mw:LanguageVariant\\\" data-mw-variant=&amp;apos;{\\\"disabled\\\":{\\\"t\\\":\\\"kasoku\\\"}}&amp;apos;>&amp;lt;/span>&amp;lt;/a> &amp;lt;!-- -->&amp;lt;a>&amp;lt;span typeof=\\\"mw:LanguageVariant\\\" data-mw-variant=&amp;apos;{\\\"disabled\\\":{\\\"t\\\":\\\"suru\\\"}}&amp;apos;>&amp;lt;/span>&amp;lt;/a>\"}}&apos;>&lt;/span>&lt;/span>&lt;!---->"}}'></span></span>)<span> </span><i>自動詞<span> </span><abbr title="サ行活用">サ行</abbr></i> (連用形<span typeof="mw:LanguageVariant" data-mw-variant='{"disabled":{"t":" &lt;b class=\"Jpan\" lang=\"ja\">&lt;ruby>加&lt;rp>(&lt;/rp>&lt;rt>か&lt;/rt>&lt;rp>)&lt;/rp>&lt;/ruby>&lt;ruby>速&lt;rp>(&lt;/rp>&lt;rt>そく&lt;/rt>&lt;rp>)&lt;/rp>&lt;/ruby>&lt;!-- -->&lt;a>&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"し\"}}&apos;>&lt;/span>&lt;/a>&lt;/b> &lt;span class=\"mention-gloss-paren annotation-paren\">(&lt;/span>&lt;span class=\"tr\">&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"&amp;lt;!---->kasoku &amp;lt;a>shi&amp;lt;/a>&amp;lt;!---->\"}}&apos;>&lt;/span>&lt;/span>&lt;span class=\"mention-gloss-paren annotation-paren\">)&lt;/span>"}}'></span>，過去式<span typeof="mw:LanguageVariant" data-mw-variant='{"disabled":{"t":" &lt;b class=\"Jpan\" lang=\"ja\">&lt;ruby>加&lt;rp>(&lt;/rp>&lt;rt>か&lt;/rt>&lt;rp>)&lt;/rp>&lt;/ruby>&lt;ruby>速&lt;rp>(&lt;/rp>&lt;rt>そく&lt;/rt>&lt;rp>)&lt;/rp>&lt;/ruby>&lt;!-- -->&lt;a>&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"した\"}}&apos;>&lt;/span>&lt;/a>&lt;/b> &lt;span class=\"mention-gloss-paren annotation-paren\">(&lt;/span>&lt;span class=\"tr\">&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"&amp;lt;!---->kasoku &amp;lt;a>shita&amp;lt;/a>&amp;lt;!---->\"}}&apos;>&lt;/span>&lt;/span>&lt;span class=\"mention-gloss-paren annotation-paren\">)&lt;/span>"}}'></span>)</span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["加速する", "加速", "加速し", "加速した"]}],
        )

    def test_ja_suru(self):
        self.assertTransformEqual(
            r"""<!DOCTYPE html>
<html>
<head><title>加速</title></head>
<body>
<section><h2>日語</h2>
<section><h3>名詞</h3>
<p><span class="headword-line"><strong class="Jpan headword" lang="ja">加速</strong>
</span></p>
<ol><li>gloss</li></ol>
<section><h4>活用</h4>
<div><table class="inflection-table"><tbody><tr>
<th><span class="Jpan" lang="ja"><span typeof="mw:LanguageVariant" data-mw-variant='{"disabled":{"t":"&lt;!-- -->&lt;a>&lt;span typeof=\"mw:LanguageVariant\" data-mw-variant=&apos;{\"disabled\":{\"t\":\"命令形\"}}&apos;>&lt;/span>&lt;/a>"}}'></span></span></th>
<td><span class="Jpan" lang="ja-Jpan">加速せよ<span>¹</span><br/>加速しろ<span>²</span></span></td>
<td><span class="Jpan" lang="ja-Jpan">かそくせよ<span>¹</span><br/>かそくしろ<span>²</span></span></td>
<td><span class="Latn" lang="ja-Latn">kasoku seyo<span>¹</span><br/>kasoku shiro<span>²</span></span></td>
</tr></tbody></table></div>
</section>
</section>
</section>
</body>
</html>""",
            [{"forms": ["加速", "加速せよ", "加速しろ", "かそくせよ", "かそくしろ"]}],
        )
