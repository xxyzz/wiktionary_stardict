from utils import XMLTestCase


class EnFormsTestCase(XMLTestCase):
    def test_alt_forms_under_pos(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>berserker</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">berserker</strong> (<i>plural</i> <b class="Latn form-of lang-en p-form-of" lang="en"><a title="berserkers">berserkers</a></b>)</span></p>
<ol><li><span>gloss</span></li></ol>
<section><h4>Alternative forms</h4>
<ul><li><span class="Latn" lang="en">berserkar</span></li></ul>
</section>
</section>
</section>
</body>
</html>""",
            [{"forms": ["berserker", "berserkar", "berserkers"]}],
        )

    def test_zh_forms_under_pron(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>大家</title></head>
<body>
<section><h2>Chinese</h2>
<section><h3>Pronunciation 3</h3>
<span data-mw='{"parts":[{"template":{"target":{"wt":"zh-forms","href":"./Template:zh-forms"},"params":{"alt":{"wt":"乾家-Min Nan,唐家-Min Nan,臺家-Eastern Min"}},"i":0}}]}'>
</span><table>
<tbody><tr>
<th colspan="2"></th>
<th></th>
<th></th></tr>
<tr>
<th>simp. and trad.<br/><span style="font-size:140%">(<span lang="zh-Hani" class="Hani">大家</span>)</span></th>
<td lang="zh-Hani" class="Hani">大</td>
<td lang="zh-Hani" class="Hani">家</td></tr>
<tr>
<th colspan="2">alternative forms</th>
<td colspan="2"><span style="white-space:nowrap;"><span class="Hant" lang="zh-Hant">乾家</span><span class="Hani" lang="zh">／</span><span class="Hans" lang="zh-Hans"><a>干家</a></span> <span style="font-size:80%"><i>Min Nan</i></span></span></td></tr>
</tbody></table>
<section><h4>Noun</h4>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">大家</strong></span></p>
<ol><li><span>gloss</span></li></ol>
</section>
</section>
</section>
</body>
</html>""",
            [{"forms": ["大家", "乾家", "干家"]}],
        )

    def test_zh_forms_sup(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>白麵</title></head>
<body>
<section><h2>Chinese</h2>
<span typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"zh-forms","href":"./Template:zh-forms"},"params":{"s":{"wt":"白面"}},"i":0}}]}'>
</span><table class="floatright">
<tbody><tr>
<th colspan="2"></th>
<th colspan="1"></th>
<th colspan="1">flour; noodles</th></tr>
<tr>
<th colspan="2"><a>trad.</a> <span style="font-size:140%">(<span lang="zh-Hant" class="Hant"><a>白麵</a>/<a>白麪</a></span>)</span></th>
<td lang="zh-Hant" class="Hant"><a>白</a></td>
<td lang="zh-Hant" class="Hant"><a>麵</a>/<a>麪</a></td></tr>
<tr>
<th colspan="2"><a>simp.</a> <span style="font-size:140%">(<span lang="zh-Hans" class="Hans"><a>白面</a><sup><span class="explain" title="This form has one or more other meanings.">*</span></sup></span>)</span></th>
<td lang="zh-Hans" class="Hans"><a>白</a></td>
<td lang="zh-Hans" class="Hans"><a>面</a></td></tr>
</tbody></table>
<section><h3>Pronunciation 1</h3>
<section><h4>Noun</h4>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">白麵</strong></span></p>
<ol><li><span>gloss</span></li></ol>
</section>
</section>
</section>
</body>
</html>""",
            [{"forms": ["白麵", "白麪", "白面"]}],
        )

    def test_zh_forms_anagram(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>門閥</title></head>
<body>
<section><h2>Chinese</h2>
<span typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"zh-forms","href":"./Template:zh-forms"},"params":{"s":{"wt":"门阀"}},"i":0}}]}'>
</span><table>
<tbody><tr>
<th colspan="2"></th>
<th colspan="1"></th>
<th colspan="1">clique; valve</th></tr>
<tr>
<th colspan="2"><a>trad.</a> <span style="font-size:140%">(<span lang="zh-Hant" class="Hant"><a>門閥</a></span>)</span></th>
<td lang="zh-Hant" class="Hant"><a>門</a></td>
<td lang="zh-Hant" class="Hant"><a>閥</a></td></tr>
<tr>
<th colspan="2"><a>simp.</a> <span style="font-size:140%">(<span lang="zh-Hans" class="Hans"><a>门阀</a></span>)</span></th>
<td lang="zh-Hans" class="Hans"><a>门</a></td>
<td lang="zh-Hans" class="Hans"><a>阀</a></td></tr>
<tr>
<th colspan="2">anagram</th>
<td colspan="2"><span style="white-space:nowrap;"><span class="Hant" lang="zh-Hant"><a>閥門</a></span><span class="Hani" lang="zh">／</span><span class="Hans" lang="zh-Hans"><a>阀门</a></span></span></td></tr>
</tbody></table>
<section><h3>Pronunciation</h3></section>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">門閥</strong></span></p>
<ol><li><span>gloss</span></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["門閥", "门阀"],
                }
            ],
        )

    def test_ja_kanjitab(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>痛い</title></head>
<body>
<section><h2>Japanese</h2>
<table class="wikitable floatright">
<tbody><tr><th style="font-weight:normal">Alternative spellings</th></tr>
<tr>
<td style="text-align:center;font-size:108%"><span class="Jpan" lang="ja" style="font-size:140%"><a>甚い</a></span><br/><span class="Jpan" lang="ja" style="font-size:140%"><a>イタい</a></span> <small><span class="usage-label-sense"><span class="ib-brac label-brac">(</span><span class="ib-content label-content">particularly<span typeof="mw:Entity"> </span>the<span typeof="mw:Entity"> </span>"cringy"<span typeof="mw:Entity"> </span>sense</span><span class="ib-brac label-brac">)</span></span></small></td></tr>
</tbody></table>
<section><h3>Adjective</h3>
<p><span class="headword-line"><strong class="Jpan headword" lang="ja"><ruby>痛<rp>(</rp><rt><a>いた</a></rt><rp>)</rp></ruby>い</strong> <a>•</a> (<span class="headword-tr tr" dir="ltr"><span class="Latn" lang="ja"><a>itai</a></span></span>)<span typeof="mw:Entity"> </span><i><abbr title="-i (type I) inflection">-i</abbr></i> (<i>adverbial</i> <b class="Jpan" lang="ja"><a><ruby>痛<rp>(</rp><rt>いた</rt><rp>)</rp></ruby>く</a></b> <span class="mention-gloss-paren annotation-paren">(</span><span class="tr">itaku</span><span class="mention-gloss-paren annotation-paren">)</span>)</span></p>
<ol><li><span>gloss</span></li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["痛い", "甚い", "イタい", "痛く"]}],
        )

    def test_russian_forms(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>бегать</title></head>
<body>
<section><h2>Russian</h2>
<section><h3>Alternative forms</h3>
<ul><li><span class="Cyrl" lang="ru"><a rel="mw:WikiLink" href="./бѣгать#Russian" title="бѣгать">бѣ́гать</a></span><span> </span><span class="mention-gloss-paren annotation-paren">(</span><span lang="ru-Latn" class="tr Latn">bě́gatʹ</span><span class="mention-gloss-paren annotation-paren">)</span><span> </span><span>—</span><span> </span><span class="ib-content label-content"><a>pre-1918 spelling</a></span></li></ul>
</section>
<section><h3>Verb</h3>
<p><span class="headword-line"><strong class="Cyrl headword" lang="ru">бе́гать</strong> <b class="Cyrl form-of lang-ru verbal_noun-form-of pos-noun target-бе́гание origin-бе́гать origin_transliteration-" lang="ru"><a rel="mw:WikiLink" title="бегание" class="new" typeof="mw:LocalizedAttrs">бе́гание</a></b></span></p>
<ol><li><span>gloss</span></li></ol>
<section><h4>Conjugation</h4>
<div><table><tbody>
<tr>
<th>passive</th>
<td><span>—</span></td><td><span>—</span></td></tr>
<tr>
<th>adverbial</th>
<td><span class="Cyrl form-of lang-ru past|adv|part-form-of origin-бе́гать" lang="ru"><a rel="mw:WikiLink" href="./бегав#Russian" title="бегав">бе́гав</a></span><br/><span lang="ru-Latn" class="tr Latn" style="color:var(--wikt-palette-grey-8,#888);">bégav</span>,<br/><span class="Cyrl form-of lang-ru past|adv|part-form-of origin-бе́гать" lang="ru"><a rel="mw:WikiLink" href="./бегавши#Russian" title="бегавши">бе́гавши</a></span><br/><span lang="ru-Latn" class="tr Latn" style="color:var(--wikt-palette-grey-8,#888);">bégavši</span></td></tr>
<tr class="rowgroup">
<th></th>
<th>present tense</th>
<th>future tense</th></tr>
<tr>
<th><a rel="mw:WikiLink" href="./первое_лицо" title="первое лицо">1st</a> <a rel="mw:WikiLink" href="./единственное_число" title="единственное число">singular</a> (<span lang="ru" class="Cyrl">я</span>)</th>
<td><span class="Cyrl form-of lang-ru 1|s|pres|ind-form-of origin-бе́гать" lang="ru"><a rel="mw:WikiLink" href="./бегаю#Russian" title="бегаю">бе́гаю</a></span><br/><span lang="ru-Latn" class="tr Latn" style="color:var(--wikt-palette-grey-8,#888);">bégaju</span></td><td><span class="Cyrl" lang="ru"><a rel="mw:WikiLink" href="./буду#Russian" title="буду">бу́ду</a></span><span lang="ru" class="Cyrl"> бе́гать</span><br/><span lang="ru-Latn" class="tr Latn" style="color:var(--wikt-palette-grey-8,#888);">búdu bégatʹ</span></td></tr>
</tbody></table></div>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": [
                        "бе́гать",  # headword strong
                        "бегать",
                        "бѣ́гать",  # alternative forms section
                        "бѣгать",
                        "бе́гание",  # headword b
                        "бегание",
                        "бе́гав",  # conjugation section table
                        "бегав",
                        "бе́гавши",
                        "бегавши",
                        "бе́гаю",
                        "бегаю",
                    ]
                }
            ],
        )

    def test_greek_forms(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>τρέχω</title></head>
<body>
<section><h2>Greek</h2>
<section><h3>Verb</h3>
<p><span class="headword-line"><strong class="Grek headword" lang="el">τρέχω</strong>
</span></p>
<ol><li><span>gloss</span></li></ol>
<section><h4>Conjugation</h4>
<div><table><tbody>
<tr><th>3 <span class="gender"><abbr title="plural number">pl</abbr></span></th>
<td><a rel="mw:WikiLink" title="τρέχουν" class="new">τρέχουν</a>(<a rel="mw:WikiLink" title="τρέχουνε" class="new">ε</a>)</td></tr>
<tr>
<th><span><b>Subjunctive mood</b></span></th>
<td colspan="2">Formed using <i>present</i>, <i>dependent</i> (for <i>simple past</i>) or <i>present perfect</i> from above with a particle (<a rel="mw:WikiLink" href="./να" title="να">να</a>, <a rel="mw:WikiLink" href="./ας" title="ας">ας</a>).</td></tr>
</tbody></table></div>
</section>
</section>
</section>
</body>
</html>""",
            [{"forms": ["τρέχω", "τρέχουν", "τρέχουνε"]}],
        )
