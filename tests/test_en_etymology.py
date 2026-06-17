from utils import XMLTestCase


class EnEtymologyTestCase(XMLTestCase):
    def test_missing_etymology(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>prickle</title></head>
<body>
<section><h2>English</h2>
<section><h3>Etymology</h3>
<p><style>.mw-parser-output</style>
<span class="maintenance-line">This etymology is missing</span>
<link rel="mw:PageProp/Category"/></p>
</section>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">prickle</strong>
</span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">prickle</strong>
</span></p>
<ol><li>gloss</li></ol>
</section>"""
                }
            ],
        )

    def test_parent_etymology(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>tee</title></head>
<body>
<section><h2 id="English">English</h2>
<section><h3 id="Etymology_1">Etymology 1</h3>
<ul><li>From <span class="etyl">Middle English</span><span> </span><small>[Term?]</small>, from <span class="etyl">Old English</span><span> </span><i class="Latn mention" lang="ang">te</i>, from <span class="etyl">Latin</span><span> </span><i class="Latn mention" lang="la">tē</i><span> </span><span class="mention-gloss-paren annotation-paren">(</span><span class="ann-pos">the name of the letter T</span><span class="mention-gloss-paren annotation-paren">)</span>.</li></ul>
<section><h3 id="Noun">Noun</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">tee</strong></span></p>
<ol><li id="English:_T-shirt">gloss</li></ol>
</section>
</section>

<section><h3 id="Etymology_2">Etymology 2</h3>
<p>First attested in the 17th century as <i class="Latn mention" lang="en">teaz</i>, back-formation from obsolete <span class="etyl">Scots</span><span> </span><i class="Latn mention" lang="sco">teaz</i>, later reanalyzed as a plural.<sup class="mw-ref reference"><span class="mw-reflink-text"><span class="cite-bracket">[</span>1<span class="cite-bracket">]</span></span></sup> <span class="maintenance-line"><i>This etymology is incomplete. You can help Wiktionary by elaborating on the origins of this term. </i></span></p>
<section><h4 id="Noun_2">Noun</h4>
<p><span class="headword-line"><strong class="Latn headword" lang="en">tee</strong></span></p>
<ol><li id="mwdA">gloss</li></ol>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">tee</strong>
</span></p>
<ol><li>gloss</li></ol>
<section>
<h4>Etymology</h4>
<ul><li>From <span class="etyl">Middle English</span><span> </span><small>[Term?]</small>, from <span class="etyl">Old English</span><span> </span><i class="Latn mention" lang="ang">te</i>, from <span class="etyl">Latin</span><span> </span><i class="Latn mention" lang="la">tē</i><span> </span><span class="mention-gloss-paren annotation-paren">(</span><span class="ann-pos">the name of the letter T</span><span class="mention-gloss-paren annotation-paren">)</span>.</li></ul>
</section>
</section>""",
                    "ids": ["English", "Etymology_1", "Noun", "English:_T-shirt"],
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">tee</strong>
</span></p>
<ol><li>gloss</li></ol>
<section>
<h4>Etymology</h4>
<p>First attested in the 17th century as <i class="Latn mention" lang="en">teaz</i>, back-formation from obsolete <span class="etyl">Scots</span><span> </span><i class="Latn mention" lang="sco">teaz</i>, later reanalyzed as a plural. </p>
</section>
</section>""",
                    "ids": ["English", "Etymology_2", "Noun_2"],
                },
            ],
        )

    def test_zh_x_chengyu_etymology(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>月明星稀</title></head>
<body>
<section><h2>Chinese</h2>
<section><h3>Etymology</h3>
<p>From <i>Duan Ge Xing</i> by <span class="Hani" lang="zh">曹操</span> (Cao Cao):</p>
<dl><dd><div class="vsSwitcher" data-toggle-category="usage examples"><dl class="zhusex"><span lang="zh-Hant" class="Hant"><b>月明星稀</b>，烏鵲南飛。繞樹三匝，何枝可依？</span><span class="vsHide"> <span style="color:var(--wikt-palette-forestgreen, #235923); font-size:80%;"><span>[</span>Classical Chinese, <i>trad.</i><span>]</span></span></span><span class="vsToggleElement" style="color:var(--wikt-palette-forestgreen, #235923);padding-left:10px"></span><hr/><span class="vsHide"><span lang="zh-Hans" class="Hans"><b>月明星稀</b></span></span><dd><span class="vsHide"><small><i>From:</i></small></span></dd><dd><b>The moon is bright and the stars are few</b>, and southward the crows flew. Circling the tree thrice, on which branch can they perch?</dd></dl></div></dd></dl>
</section>
<section><h3>Idiom</h3>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">月明星稀</strong></span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Idiom</h4>
<p><span class="headword-line">
<strong class="Hani headword" lang="zh">月明星稀</strong>
</span></p>
<ol><li>gloss</li></ol>
<section>
<h4>Etymology</h4>
<p>From <i>Duan Ge Xing</i> by <span class="Hani" lang="zh">曹操</span> (Cao Cao):</p>
<dl><dd><div class="vsSwitcher"><dl class="zhusex"><span lang="zh-Hant" class="Hant"><b>月明星稀</b>，烏鵲南飛。繞樹三匝，何枝可依？</span><span class="vsToggleElement" style="color:#235923;padding-left:10px"></span><hr/><dd></dd><dd><b>The moon is bright and the stars are few</b>, and southward the crows flew. Circling the tree thrice, on which branch can they perch?</dd></dl></div></dd></dl>
</section>
</section>"""
                }
            ],
        )

    def test_ancestor_ety(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>compound</title></head>
<body>
<section><h2>English</h2>
<section><h3>Etymology 1</h3>
<p>etymology 1</p>
<section><h4>Pronunciation</h4>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">Received Pronunciation</span></span><span class="ib-brac qualifier-brac">)</span><span> </span><a title="Wiktionary:International Phonetic Alphabet">IPA</a><span>:</span><span> </span><span class="IPA nowrap">/ˈkɒmpaʊnd/</span></li></ul>
</section>
<section><h4>Noun</h4>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">compound</strong>
</span></p>
<ol><li>noun gloss</li></ol>
</section>
</section>

<section><h3>Etymology 2</h3>
<p>etymology 2</p>
<section><h4>Pronunciation 1</h4>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">UK</span></span><span class="ib-brac qualifier-brac">)</span><span> </span><a title="Wiktionary:International Phonetic Alphabet">IPA</a><span>:</span><span> </span><span class="IPA nowrap">/ˈkɒmpaʊnd/</span></li></ul>
<section><h5>Adjective</h5>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">compound</strong>
</span></p>
<ol><li>adj gloss</li></ol>
</section>
<section><h5>Noun</h5>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">compound</strong>
</span></p>
<ol><li>noun gloss</li></ol>
</section>
</section>

<section><h4>Pronunciation 2</h4>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">UK</span><span class="ib-brac qualifier-brac">)</span><span> </span><a title="Wiktionary:International Phonetic Alphabet">IPA</a><span>:</span><span> </span><span class="IPA nowrap">/kəmˈpaʊnd/</span></span></li></ul>
<section><h5>Verb</h5>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">compound</strong>
</span></p>
<ol><li>verb gloss</li></ol>
</section>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">Received Pronunciation</span></span><span class="ib-brac qualifier-brac">)</span><span> </span>IPA<span>:</span><span> </span><span class="IPA nowrap">/ˈkɒmpaʊnd/</span></li></ul>
<p><span class="headword-line"><strong class="Latn headword" lang="en">compound</strong>
</span></p>
<ol><li>noun gloss</li></ol>
<section><h4>Etymology</h4>
<p>etymology 1</p>
</section></section>"""
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Adjective</h4>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">UK</span></span><span class="ib-brac qualifier-brac">)</span><span> </span>IPA<span>:</span><span> </span><span class="IPA nowrap">/ˈkɒmpaʊnd/</span></li></ul>
<p><span class="headword-line"><strong class="Latn headword" lang="en">compound</strong>
</span></p>
<ol><li>adj gloss</li></ol>
<section><h4>Etymology</h4>
<p>etymology 2</p>
</section></section>"""
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">UK</span></span><span class="ib-brac qualifier-brac">)</span><span> </span>IPA<span>:</span><span> </span><span class="IPA nowrap">/ˈkɒmpaʊnd/</span></li></ul>
<p><span class="headword-line"><strong class="Latn headword" lang="en">compound</strong>
</span></p>
<ol><li>noun gloss</li></ol>
<section><h4>Etymology</h4>
<p>etymology 2</p>
</section></section>"""
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Verb</h4>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">UK</span><span class="ib-brac qualifier-brac">)</span><span> </span>IPA<span>:</span><span> </span><span class="IPA nowrap">/kəmˈpaʊnd/</span></span></li></ul>
<p><span class="headword-line"><strong class="Latn headword" lang="en">compound</strong>
</span></p>
<ol><li>verb gloss</li></ol>
<section><h4>Etymology</h4>
<p>etymology 2</p>
</section></section>"""
                },
            ],
        )
