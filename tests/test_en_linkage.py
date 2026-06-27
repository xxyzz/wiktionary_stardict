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
<ul><li>1</li><li>2</li><li>3</li><li>4</li><li>5</li><li>6</li></ul>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content">post</span><span class="ib-brac qualifier-brac">)</span><span class="ib-colon sense-qualifier-colon">:</span></li></ul>
<ul><li><span class="Hani" lang="zh">位子</span> <span class="mention-gloss-paren annotation-paren">(</span><span lang="zh-Latn" class="tr Latn">wèizi</span><span class="mention-gloss-paren annotation-paren">)</span></li></ul></section></section></section>""",
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
