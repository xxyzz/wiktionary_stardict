from utils import XMLTestCase


class EnPronunciationTestCase(XMLTestCase):
    def test_pos_list_in_pron_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>berserk</title></head>
<body>
<section><h2>English</h2>
<section><h3>Pronunciation</h3>
<ul><li><a>Noun</a>:
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent"><a title="w:Received Pronunciation" class="extiw">Received Pronunciation</a></span></span><span class="ib-brac qualifier-brac">)</span><span> </span><a title="Wiktionary:International Phonetic Alphabet">IPA</a><sup>(<a title="Appendix:English pronunciation">key</a>)</sup><span>:</span><span> </span><span class="IPA nowrap">/ˈbɜːsɜːk/</span></li>
</ul></li>
<li><a title="Appendix:Glossary">Adjective</a>:
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent"><a title="w:Received Pronunciation" class="extiw">Received Pronunciation</a></span></span><span class="ib-brac qualifier-brac">)</span><span> </span><a title="Wiktionary:International Phonetic Alphabet">IPA</a><sup>(<a title="Appendix:English pronunciation">key</a>)</sup><span>:</span><span> </span><span class="IPA nowrap">/bəˈzɜːk/</span></li></ul></li>
<li><span>Hyphenation: </span><span class="Latn" lang="en">ber‧serk</span></li></ul></section>

<section><h3>Adjective</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">berserk</strong></span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="en">
<h4>Adjective</h4>
<ul>
<li>Noun:
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">Received Pronunciation</span></span><span class="ib-brac qualifier-brac">)</span><span> </span>IPA<span>:</span><span> </span><span class="IPA nowrap">/ˈbɜːsɜːk/</span></li>
</ul></li>
<li>Adjective:
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">Received Pronunciation</span></span><span class="ib-brac qualifier-brac">)</span><span> </span>IPA<span>:</span><span> </span><span class="IPA nowrap">/bəˈzɜːk/</span></li></ul></li>
<li><span>Hyphenation: </span><span class="Latn" lang="en">ber‧serk</span></li>
</ul>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">berserk</strong>
</span></p>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )

    def test_remove_audio_file_table(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>languid</title></head>
<body>
<section><h2>English</h2>
<section><h3>Pronunciation</h3>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">Received Pronunciation<span class="ib-comma label-comma">,</span><span> </span>General American<span class="ib-comma label-comma">,</span><span> </span>weak vowel distinction</span></span><span class="ib-brac qualifier-brac">)</span><span> </span><a title="Wiktionary:International Phonetic Alphabet">IPA</a><sup>(<a title="Appendix:English pronunciation">key</a>)</sup><span>:</span><span> </span><span class="IPA nowrap">/ˈlæŋɡwɪd/</span>
<ul><li><style data-mw-deduplicate="TemplateStyles:r50165410">.mw-parser-output .k-player .k-attribution{visibility:hidden}</style><table class="audiotable"></table>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">US<span class="ib-comma label-comma">,</span><span> </span>Canada<span class="ib-comma label-comma">,</span><span> </span>weak vowel distinction</span></span><span class="ib-brac qualifier-brac">)</span><span> </span><a title="Wiktionary:International Phonetic Alphabet">IPA</a><sup>(<a>key</a>)</sup><span>:</span><span> </span><span class="IPA nowrap">/ˈleɪ̯ŋɡwɪd/</span><span>, </span><span class="IPA nowrap">/ˈlɛ̃ŋɡwɪd/</span></li></ul></li></ul></li></ul>
</section>
<section><h3>Adjective</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">languid</strong></span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="en">
      <h4>Adjective</h4>
      <ul>
        <li>
          <span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">Received Pronunciation<span class="ib-comma label-comma">,</span><span> </span>General American<span class="ib-comma label-comma">,</span><span> </span>weak vowel distinction</span></span><span class="ib-brac qualifier-brac">)</span><span> </span>IPA<span>:</span><span> </span><span class="IPA nowrap">/ˈlæŋɡwɪd/</span>
       </li>
      </ul>
      <p>
        <span class="headword-line">
          <strong class="Latn headword" lang="en">languid</strong>
        </span>
      </p>
      <ol>
        <li>gloss</li>
      </ol>
    </section>""",
                }
            ],
        )

    def test_ja_pron(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>痛い</title></head>
<body>
<section><h2>Japanese</h2>
<section><h3>Pronunciation</h3>
<span data-mw='{"parts":[{"template":{"target":{"wt":"ja-pron","href":"./Template:ja-pron"},"params":{"1":{"wt":"いたい"},"acc":{"wt":"2"},"acc_ref":{"wt":"SMK2"}},"i":0}}]}'>
</span><ul><li><span class="usage-label-accent"><span class="ib-brac label-brac">(</span><span class="ib-content label-content"><a>Tokyo</a></span><span class="ib-brac label-brac">)</span></span> <span lang="ja" class="Jpan">い<span style="border-top:1px solid;position:relative;padding:1px;">た<span style="position:absolute;top:0;bottom:67%;right:0%;border-right:1px solid;"></span></span>い</span> <span class="Latn"><samp>[ìtáꜜì]</samp></span> (<a>Nakadaka</a> – [2])<sup class="mw-ref reference"><a><span class="mw-reflink-text"><span class="cite-bracket">[</span>5<span class="cite-bracket">]</span></span></a></sup></li><li><a title="Wiktionary:International Phonetic Alphabet">IPA</a><sup>(<a>key</a>)</sup>:<span> </span><span class="IPA nowrap">[ita̠i]</span></li></ul>
</section>
<section><h3>Adjective</h3>
<p><span class="headword-line"><strong class="Japn headword" lang="ja">痛い</strong></span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="en">
<h4>Adjective</h4>
<ul>
  <li><span class="usage-label-accent"><span class="ib-brac label-brac">(</span><span class="ib-content label-content">Tokyo</span><span class="ib-brac label-brac">)</span></span> <span lang="ja" class="Jpan">い<span style="border-top:1px solid;position:relative;padding:1px;">た<span style="position:absolute;top:0;bottom:67%;right:0%;border-right:1px solid;"></span></span>い</span> <span class="Latn"><samp>[ìtáꜜì]</samp></span> (Nakadaka – [2])</li>
  <li>IPA:<span> </span><span class="IPA nowrap">[ita̠i]</span></li></ul>
<p>
  <span class="headword-line">
    <strong class="Japn headword" lang="ja">痛い</strong>
  </span>
</p>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )

    def test_zh_pron(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>大家</title></head>
<body>
<section><h2>Chinese</h2>
<section><h3>Pronunciation 1</h3>
<div class="standard-box zhpron" style="overflow:auto; max-width:500px; font-size:100%" about="#mwt2" typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"zh-pron\n","href":"./Template:zh-pron"},"i":0}}]}'><div class="vsSwitcher" data-toggle-category="pronunciations">
<ul><li><a class="extiw">Mandarin</a>
<dl><dd><small>(<i><a>Standard</a></i>)</small>
<dl><dd><small>(<i><a>Pinyin</a></i>)</small>: <span class="zhpron-monospace form-of pinyin-ts-form-of" lang="cmn"><span class="Latn" lang="cmn"><a>dàjiā</a></span>, <span class="Latn" lang="cmn"><a>dà'ā</a></span></span></dd>
<dd><small>(<i><a>Zhuyin</a></i>)</small>: <span lang="cmn-Bopo" class="Bopo">ㄉㄚˋ ㄐㄧㄚ, ㄉㄚˋ ㄚ</span></dd>
<dd><span class="mw-default-size mw-default-audio-height" typeof="mw:File"><span><audio><source/></audio></span></span></dd></dl></dd>
<dd><small>(<i>Chengdu, Sichuanese Pinyin</i>)</small>: <span class="zhpron-monospace">da<sup>4</sup> jia<sup>1</sup></span></dd>
</dl></li></ul>
<div class="vsHide" style="clear:right;">
<hr/>
<ul><li>Mandarin
<ul><li><small>(<i>Standard Chinese</i>)</small><sup><small><abbr title="Add Mandarin homophones"><span class="plainlinks">+</span></abbr></small></sup>
<ul><li><small><i>Hanyu Pinyin</i></small>: <span class="zhpron-monospace" lang="cmn"><span class="Latn" lang="cmn">dàjiā</span></span></li></ul></li></ul></li></ul>
</div></div></div>
<section><h4>Pronoun</h4>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">大家</strong></span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="en">
<h4>Pronoun</h4>
<ul><li>Mandarin
<dl><dd><small>(<i>Standard</i>)</small>
<dl><dd><small>(<i>Pinyin</i>)</small>: <span class="zhpron-monospace form-of pinyin-ts-form-of" lang="cmn"><span class="Latn" lang="cmn">dàjiā</span>, <span class="Latn" lang="cmn">dà'ā</span></span></dd>
<dd><small>(<i>Zhuyin</i>)</small>: <span lang="cmn-Bopo" class="Bopo">ㄉㄚˋ ㄐㄧㄚ, ㄉㄚˋ ㄚ</span></dd></dl></dd>
<dd><small>(<i>Chengdu, Sichuanese Pinyin</i>)</small>: <span class="zhpron-monospace">da<sup>4</sup> jia<sup>1</sup></span></dd>
</dl></li></ul>
<p>
  <span class="headword-line">
    <strong class="Hani headword" lang="zh">大家</strong>
  </span>
</p>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )

    def test_non_map_value_data_mw(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>寝椅子</title></head>
<body>
<section><h2>Japanese</h2>
<section><h3>Pronunciation</h3>
<span data-mw='{"parts":[{"template":{"target":{"wt":"ja-pron"}}}]}'>
</span><ul><li><span class="usage-label-accent"><span class="ib-brac label-brac">(</span><span class="ib-content label-content">Tokyo</span><span class="ib-brac label-brac">)</span></span> <span lang="ja" class="Jpan">ね<span style="border-top:1px;">いす</span></span> <span class="Latn"><samp>[nèísú]</samp></span> (<a>Heiban</a> – [0])<sup class="mw-ref reference"></sup></li></ul>
<span typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"ja-accent-dialectal"}}},"&lt;ref name=\\"KDJ2O\\"/>"]}'>
</span><ul><li><span class="usage-label-accent"><span class="ib-brac label-brac">(</span><span class="ib-content label-content"><a>Kyōto</a></span><span class="ib-brac label-brac">)</span></span> <span class="Jpan" lang="ja"><span style="border-top:1px;">ね<span style="position:absolute;">​</span></span>いす</span><span> </span><span class="Latn"><samp>[néꜜìsù]</samp></span> (<a>Kōki</a>)<sup class="mw-ref reference"></sup></li></ul>
</section>
<section><h3>Pronoun</h3>
<p><span class="headword-line"><strong class="Jpan headword" lang="ja">寝椅子</strong></span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="en">
<h4>Pronoun</h4>
<ul><li><span class="usage-label-accent"><span class="ib-brac label-brac">(</span><span class="ib-content label-content">Tokyo</span><span class="ib-brac label-brac">)</span></span> <span lang="ja" class="Jpan">ね<span style="border-top:1px;">いす</span></span> <span class="Latn"><samp>[nèísú]</samp></span> (Heiban – [0])</li></ul>
<ul><li><span class="usage-label-accent"><span class="ib-brac label-brac">(</span><span class="ib-content label-content">Kyōto</span><span class="ib-brac label-brac">)</span></span> <span class="Jpan" lang="ja"><span style="border-top:1px;">ね<span style="position:absolute;">​</span></span>いす</span><span> </span><span class="Latn"><samp>[néꜜìsù]</samp></span> (Kōki)</li></ul>
<p>
  <span class="headword-line">
    <strong class="Jpan headword" lang="ja">寝椅子</strong>
  </span>
</p>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )

    def test_syllabification(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>diccionario</title></head>
<body>
<section><h2>Spanish</h2>
<section><h3>Pronunciation</h3>
<ul><li>Syllabification: <span class="Latn" lang="es">dic‧cio‧na‧rio</span></li></ul>
</section>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="es">diccionario</strong></span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="en">
<h4>Noun</h4>
<ul><li>Syllabification: <span class="Latn" lang="es">dic‧cio‧na‧rio</span></li></ul>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="es">diccionario</strong>
  </span>
</p>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )

    def test_zh_pron_no_mandarin(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>仆街</title></head>
<body>
<section><h2>Chinese</h2>
<section><h3>Pronunciation</h3>
<div class="standard-box zhpron">
<div class="vsSwitcher" data-toggle-category="pronunciations">
<ul><li>Cantonese <small>(<i>Jyutping</i>)</small>: <span class="zhpron-monospace">puk<sup>1</sup> gaai<sup>1</sup></span></li></ul>
</div></div>
</section>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Hans headword" lang="zh">仆街</strong></span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="en">
<h4>Noun</h4>
<ul><li>Cantonese <small>(<i>Jyutping</i>)</small>: <span class="zhpron-monospace">puk<sup>1</sup> gaai<sup>1</sup></span></li></ul>
<p><span class="headword-line"><strong class="Hans headword" lang="zh">仆街</strong>
</span></p>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )

    def test_parent_preceding_pron(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>tee</title></head>
<body>
<section><h2>English</h2>
<section><h3>Pronunciation</h3>
<ul><li><a title="Wiktionary:International Phonetic Alphabet">IPA</a><sup>(key)</sup><span>:</span><span> </span><span class="IPA nowrap">/ˈtiː/</span></li></ul></section>
<section><h3>Etymology 1</h3>
<section><h4>Noun</h4>
<p><span class="headword-line"><strong class="Latn headword" lang="en">tee</strong></span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="en">
<h4>Noun</h4>
<ul><li>IPA<span>:</span><span> </span><span class="IPA nowrap">/ˈtiː/</span></li></ul>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">tee</strong>
</span></p>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )

    def test_dl_audio(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>severe</title></head>
<body>
<section><h2>English</h2>
<section><h3>Pronunciation</h3>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">UK</span></span><span class="ib-brac qualifier-brac">)</span><span> </span><a rel="mw:WikiLink" href="./Wiktionary:International_Phonetic_Alphabet" title="Wiktionary:International Phonetic Alphabet">IPA</a><span>:</span><span> </span><span class="IPA nowrap">/sɪˈvɪə/</span>
<dl><dd><table class="audiotable"></table></dd></dl></li>
</ul></section>
<section><h3>Adjective</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">severe</strong>
</span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="en">
<h4>Adjective</h4>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">UK</span></span><span class="ib-brac qualifier-brac">)</span><span> </span>IPA<span>:</span><span> </span><span class="IPA nowrap">/sɪˈvɪə/</span></li></ul>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">severe</strong>
</span></p>
<ol><li>gloss</li></ol>
</section>""",
                }
            ],
        )
