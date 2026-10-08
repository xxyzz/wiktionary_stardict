from utils import XMLTestCase


class EnLinkageTestCase(XMLTestCase):
    def test_child_section_list(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>radical</title></head>
<body>
<section><h2>English</h2>
<section><h3>Adjective</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">radical</strong>
</span></p>
<ol><li>gloss</li></ol>
<section><h4>Synonyms</h4>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content">linguistics, in reference to words</span><span class="ib-brac qualifier-brac">)</span><span class="ib-colon sense-qualifier-colon">:</span> <span class="Latn" lang="en">primitive</span></li></ul>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Adjective</h4>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">radical</strong></span></p>
<ol><li>gloss</li></ol>
<section><h4>Synonyms</h4>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content">linguistics, in reference to words</span><span class="ib-brac qualifier-brac">)</span><span class="ib-colon sense-qualifier-colon">:</span> <span class="Latn" lang="en">primitive</span></li></ul></section></section></section>""",
                }
            ],
        )

    def test_syn_saurus(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>位置</title></head>
<body>
<section><h2>Chinese</h2>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">位置</strong>
</span></p>
<ol><li>gloss</li></ol>
<section><h4>Synonyms</h4>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content">location</span><span class="ib-brac qualifier-brac">)</span><span class="ib-colon sense-qualifier-colon">:</span></li></ul>
<div class="list-switcher-wrapper"><div class="list-switcher" data-toggle-category="derived terms"><div class="term-list columns-bg ul-column-count" data-column-count="3"><ul><li>1</li><li>2</li><li>3</li><li>4</li><li>5</li><li>6</li><li>7</li></ul></div></div></div>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content">post</span><span class="ib-brac qualifier-brac">)</span><span class="ib-colon sense-qualifier-colon">:</span></li></ul>
<div class="list-switcher-wrapper"><div class="term-list columns-bg"><ul><li><span class="Hani" lang="zh">位子</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="zh-Latn" class="tr Latn">wèizi</span><span class="mention-gloss-paren annotation-paren">)</span></li></ul></div></div>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p><span class="headword-line">
<strong class="Hani headword" lang="zh">位置</strong></span></p>
<ol><li>gloss</li></ol>
<section><h4>Synonyms</h4>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content">location</span><span class="ib-brac qualifier-brac">)</span><span class="ib-colon sense-qualifier-colon">:</span></li></ul>
<div class="list-switcher-wrapper"><div class="list-switcher"><div class="term-list columns-bg ul-column-count"><ul><li>1</li><li>2</li><li>3</li><li>4</li><li>5</li><li>6</li></ul></div></div></div>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content">post</span><span class="ib-brac qualifier-brac">)</span><span class="ib-colon sense-qualifier-colon">:</span></li></ul>
<div class="list-switcher-wrapper"><div class="term-list columns-bg"><ul><li><span class="Hani" lang="zh">位子</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="zh-Latn" class="tr Latn">wèizi</span><span class="mention-gloss-paren annotation-paren">)</span></li></ul></div></div></section></section></section>""",
                }
            ],
        )

    def test_level_3_syn(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>cardinal</title></head>
<body>
<section><h2>English</h2>
<section><h3>Adjective</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">cardinal</strong>
</span></p>
<ol><li>gloss</li></ol></section>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">cardinal</strong>
</span></p>
<ol><li>gloss</li></ol></section>
<section><h3>Synonyms</h3>
<ul><li>syn</li></ul>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Adjective</h4>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">cardinal</strong></span></p>
<ol><li>gloss</li></ol>
<section><h4>Synonyms</h4>
<ul><li>syn</li></ul></section></section></section>""",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">cardinal</strong></span></p>
<ol><li>gloss</li></ol>
<section><h4>Synonyms</h4>
<ul><li>syn</li></ul></section></section></section>""",
                },
            ],
        )

    def test_col(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>homosexual</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">homosexual</strong>
</span></p>
<ol><li>gloss</li></ol>
<section><h4>Synonyms</h4>
<div class="NavFrame">
<div class="NavHead" style="text-align: left;">non-derogatory synonyms</div>
<div class="NavContent columns-bg ul-column-count" data-column-count="3" style="text-align: left;">
<dl><dt>of either sex</dt><dd></dd></dl>
<ul><li><span class="Latn" lang="en">gay</span> <span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content">but see usage notes at <i>gay</i> (n)</span><span class="ib-brac qualifier-brac">)</span></li></ul></div></div>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">homosexual</strong></span></p>
<ol><li>gloss</li></ol>
<section><h4>Synonyms</h4>
<div class="NavFrame">
<div class="NavHead" style="text-align: left;">non-derogatory synonyms</div>
<div class="NavContent columns-bg ul-column-count" style="text-align: left;">
<dl><dt>of either sex</dt><dd></dd></dl>
<ul><li><span class="Latn" lang="en">gay</span> <span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content">but see usage notes at <i>gay</i> (n)</span><span class="ib-brac qualifier-brac">)</span></li></ul></div></div></section></section></section>""",
                },
            ],
        )

    def test_rm_gallery(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Austria-Hungary</title></head>
<body>
<section><h2>English</h2>
<section><h3>Proper noun</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">Austria-Hungary
</strong></span></p>
<ol><li>gloss</li></ol>
<section><h4>Synonyms</h4>
<ul><li><span class="Latn" lang="en">Austro-Hungary</span></li></ul>
<ul class="gallery mw-gallery-traditional"><li class="gallerybox"></li></ul>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Proper noun</h4>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">Austria-Hungary</strong></span></p>
<ol><li>gloss</li></ol>
<section><h4>Synonyms</h4>
<ul><li><span class="Latn" lang="en">Austro-Hungary</span></li></ul>
</section></section></section>""",
                },
            ],
        )

    def test_rm_zh_dial(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>攪絞</title></head>
<body>
<section><h2>Chinese</h2>
<section><h3>Verb</h3>
<p><span class="headword-line"><strong class="Hant headword" lang="zh">攪絞</strong></span></p>
<ol><li>gloss</li></ol>
<section><h4>Synonyms</h4>
<span data-mw='{"parts":[{"template":{"target":{"wt":"zh-dial"}}}]}'>	</span><div class="NavFrame">
	<div class="NavHead">Dialectal synonyms of <span class="Hant" lang="zh"><a>腹瀉</a></span> (“to have diarrhea”) <a><small><span>[</span>map<span>]</span></small></a>
</div>
	<div class="NavContent">
	<table class="wikitable">
	<tbody><tr></tr></tbody></table></div></div>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Verb</h4>
<p><span class="headword-line">
<strong class="Hant headword" lang="zh">攪絞</strong></span></p>
<ol><li>gloss</li></ol></section></section>""",
                },
            ],
        )
