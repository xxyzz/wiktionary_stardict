from utils import XMLTestCase


class EnPOSTestCase(XMLTestCase):
    def test_remove_cat_link_and_anchor(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>tee</title></head>
<body>
<section data-mw-section-id="4" id="mwEQ"><h2 id="English">English</h2>

<section data-mw-section-id="7" id="mwLA"><h4 id="Noun">Noun</h4>
<p id="mwLQ"><span class="headword-line" about="#mwt16" typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"en-noun","href":"./Template:en-noun"},"params":{},"i":0}}]}' id="mwLg"><strong class="Latn headword" lang="en">tee</strong> (<i>plural</i> <b class="Latn form-of lang-en p-form-of" lang="en"><a rel="mw:WikiLink" href="./tees#English" title="tees">tees</a></b>)</span><link rel="mw:PageProp/Category" href="./Category:English_lemmas#TEE" about="#mwt16"/></p>

<ol id="mwMA"><li id="mwMQ"><span class="use-with-mention" about="#mwt17" typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"Latn-def","href":"./Template:Latn-def"},"params":{"1":{"wt":"en"},"2":{"wt":"name"},"3":{"wt":"T"},"4":{"wt":"t"}},"i":0}}]}' id="mwMg">The name of the <a rel="mw:WikiLink" href="./Appendix:Latin_script" title="Appendix:Latin script">Latin script</a> letter <i class="Latn mention" lang="en"><a rel="mw:WikiLink" href="./T#English" title="T">T</a></i>/<i class="Latn mention" lang="en"><a rel="mw:WikiLink" href="./t#English" title="t">t</a></i>.</span><link rel="mw:PageProp/Category" href="./Category:en:Latin_letter_names#TEE" about="#mwt17" id="mwMw"/></li>
<li class="mw-empty-elt"></li><li class="senseid"> <span class="usage-label-sense"><span class="ib-brac label-brac">(</span><span class="ib-content label-content"><a>clothing</a><span class="ib-comma label-comma">,</span><span> </span><a>informal</a></span><span class="ib-brac label-brac">)</span></span> <span class="form-of-definition use-with-mention"><a>Ellipsis</a> of <span class="form-of-definition-link"><i class="Latn mention" lang="en"><a>tee-shirt</a></i></span></span>.</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["tee", "tees"],
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
      <h4>Noun</h4>
      <p>
        <span class="headword-line">
          <strong class="Latn headword" lang="en">tee</strong> (<i>plural</i>
          <b class="Latn form-of lang-en p-form-of" lang="en">tees</b>)</span>
      </p>
      <ol>
        <li>
          <span class="use-with-mention">The name of the Latin script letter <i class="Latn mention" lang="en">T</i>/<i class="Latn mention" lang="en">t</i>.</span>
        </li>
        <li> <span class="usage-label-sense"><span class="ib-brac label-brac">(</span><span class="ib-content label-content">clothing<span class="ib-comma label-comma">,</span><span> </span>informal</span><span class="ib-brac label-brac">)</span></span> <span class="form-of-definition use-with-mention">Ellipsis of <span class="form-of-definition-link"><i class="Latn mention" lang="en">tee-shirt</i></span></span>.</li>
      </ol>
    </section>""",
                    "form_of_only": False,
                },
            ],
        )

    def test_double_headword_one_ol(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>-ego</title></head>
<body>
<section><h2>English</h2>
<section><h3>Suffix</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">-ego</strong></span></p>
<p><span class="headword-line"><strong class="Latn headword" lang="en">-ego</strong><span> </span><span class="gender"><abbr title="masculine gender">m</abbr></span></span></p>
<ol><li><span class="use-with-mention">forms adjectives</span></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["-ego"],
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
      <h4>Suffix</h4>
      <p>
        <span class="headword-line">
          <strong class="Latn headword" lang="en">-ego</strong>
        </span>
      </p>
      <p>
        <span class="headword-line">
          <strong class="Latn headword" lang="en">-ego</strong>
          <span> </span>
          <span class="gender"><abbr title="masculine gender">m</abbr></span>
        </span>
      </p>
      <ol>
        <li>
          <span class="use-with-mention">forms adjectives</span>
        </li>
      </ol>
    </section>""",
                },
            ],
        )

    def test_two_headword_two_ol(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>-άρης</title></head>
<body>
<section><h2>Greek</h2>
<section><h3>Suffix</h3>
<p><span class="headword-line"><strong class="Grek headword" lang="el">-άρης</strong></span></p>
<ol><li><span>gloss 1</span></li></ol>
<p><span class="headword-line"><strong class="Grek headword" lang="el">-άρης</strong></span></p>
<ol><li><span>gloss 2</span></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["-άρης"],
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
      <h4>Suffix</h4>
      <p>
        <span class="headword-line">
          <strong class="Grek headword" lang="el">-άρης</strong>
        </span>
      </p>
      <ol>
        <li>
          <span>gloss 1</span>
        </li>
      </ol>
      <p>
        <span class="headword-line">
          <strong class="Grek headword" lang="el">-άρης</strong>
        </span>
      </p>
      <ol>
        <li>
          <span>gloss 2</span>
        </li>
      </ol>
    </section>""",
                },
            ],
        )

    def test_empty_def_list(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>wind down</title></head>
<body>
<section><h2>English</h2>
<section><h3>Verb</h3>
<p><span class="headword-line">
<strong class="Latn headword" lang="en">wind down</strong></span></p>
<ol>
   <li>gloss 1</li>
   <li class="mw-empty-elt"><link/></li>
</ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
      <h4>Verb</h4>
      <p>
        <span class="headword-line">
          <strong class="Latn headword" lang="en">wind down</strong>
        </span>
      </p>
      <ol>
        <li>gloss 1</li>
      </ol>
    </section>""",
                },
            ],
        )

    def test_math_svg(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>binomial series</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">binomial series</strong>
  </span>
</p>
<ol>
   <li>The Maclaurin series expansion <span class="mwe-math-element mwe-math-element-inline" ><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math></math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/d253b87bf18d329bd2d1c12ee1ebba5071003ca8" class="mwe-math-fallback-image-inline mw-invert skin-invert" aria-hidden="true" style="vertical-align: -1.005ex; width:11.63ex; height:3.176ex;"/></span></li>
</ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">binomial series</strong>
  </span>
</p>
<ol>
   <li>The Maclaurin series expansion <span class="mwe-math-element mwe-math-element-inline" ><img src="d253b87bf18d329bd2d1c12ee1ebba5071003ca8.svg" class="mwe-math-fallback-image-inline mw-invert skin-invert" aria-hidden="true" style="vertical-align: -1.005ex; width:11.63ex; height:3.176ex;"/></span></li>
</ol>
</section>""",
                    "images": [
                        "https://wikimedia.org/api/rest_v1/media/math/render/svg/d253b87bf18d329bd2d1c12ee1ebba5071003ca8"
                    ],
                }
            ],
        )

    def test_egyptian_png(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>ꜣḫt-jtn</title></head>
<body>
<section><h2>English</h2>
<section><h3>Proper noun</h3>
<p>
  <span class="headword-line">
    <strong class="None headword" lang="egy">
      <img class="skin-invert" style="margin: 1px;" src="/w/extensions/wikihiero/img/hiero_N27.png?fee08" height="22" title="N27 [Axt]" alt="Axt"/>
    </strong>
  </span>
</p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Proper noun</h4>
<p>
  <span class="headword-line">
    <strong class="None headword" lang="egy">
      <img class="skin-invert" style="margin: 1px;" src="hiero_N27.png" height="22" title="N27 [Axt]" alt="Axt"/>
    </strong>
  </span>
</p>
<ol><li>gloss</li></ol>
</section>""",
                    "images": ["/w/extensions/wikihiero/img/hiero_N27.png?fee08"],
                }
            ],
        )

    def test_remove_sup_ref_and_figure(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>säteri</title></head>
<body>
<section><h2>Finnish</h2>
<section><h3>Noun</h3>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="fi">säteri</strong>
  </span>
</p>
<ol><li>gloss<sup class="mw-ref reference">[1]</sup><figure class="mw-default-size" typeof="mw:File/Thumb" id="mwHw"><a href="./File:Valsta_säteri.jpg" class="mw-file-description" id="mwIA"><img resource="./File:Valsta_säteri.jpg" src="//upload.wikimedia.org/wikipedia/commons/thumb/1/13/Valsta_s%C3%A4teri.jpg/250px-Valsta_s%C3%A4teri.jpg" decoding="async" data-file-width="3288" data-file-height="2239" data-file-type="bitmap" height="170" width="250" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/1/13/Valsta_s%C3%A4teri.jpg/500px-Valsta_s%C3%A4teri.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/1/13/Valsta_s%C3%A4teri.jpg/500px-Valsta_s%C3%A4teri.jpg 2x" class="mw-file-element" id="mwIQ"/></a><figcaption id="mwIg">Valsta säteri, a sateri roof form</figcaption></figure></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="fi">säteri</strong>
  </span>
</p>
<ol><li>gloss</li></ol>
</section>""",
                },
            ],
        )

    def test_color_panel(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Nile blue</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">Nile blue</strong>
  </span>
</p>
<ol><li>A pale <a>greenish</a> <a>blue</a> colour.
<dl><dd><div class="color-panel mw-no-invert" about="#mwt4" typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"color panel","href":"./Template:color_panel"},"params":{"1":{"wt":"006F7C"}},"i":0}}]}' id="mwDw">Nile blue: <span style="background-color:#006F7C;  display:inline-block; width:80px"><span typeof="mw:Entity"> </span></span></div></dd></dl></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">Nile blue</strong>
  </span>
</p>
<ol><li>A pale greenish blue colour.
<dl><dd><div class="color-panel mw-no-invert">Nile blue: <span style="background-color:#006F7C;  display:inline-block; width:80px"><span> </span></span></div></dd></dl></li></ol>
</section>""",
                },
            ],
        )

    def test_image_src_without_question_mark(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>rhombus</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">rhombus</strong>
  </span>
</p>
<ol><li class="mw-empty-elt"></li><li class="senseid"><span class="usage-label-sense"><span class="ib-brac label-brac">(</span><span class="ib-content label-content"><a>geometry</a></span><span class="ib-brac label-brac">)</span></span> A <a>parallelogram</a> having all sides of equal length. <style>.mw-parser-output .defdate{font-size:smaller}</style><span class="defdate">[from 16th c.]</span>
<ol><li>The rhombus diamond, as one of the <a class="extiw">suits</a> seen in a deck of playing cards (<span><a href="./File:SuitDiamonds.svg" class="mw-file-description" title="♦"><img alt="♦" resource="./File:SuitDiamonds.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/db/SuitDiamonds.svg/20px-SuitDiamonds.svg.png" decoding="async" data-file-width="240" data-file-height="260" data-file-type="drawing" height="22" width="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/db/SuitDiamonds.svg/40px-SuitDiamonds.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/d/db/SuitDiamonds.svg/40px-SuitDiamonds.svg.png 2x" class="mw-file-element"/></a></span> or <span><a href="./File:SuitDiamonds4colors.svg" class="mw-file-description" title="♦"><img alt="♦" resource="./File:SuitDiamonds4colors.svg" src="//upload.wikimedia.org/wikipedia/commons/thumb/7/79/SuitDiamonds4colors.svg/20px-SuitDiamonds4colors.svg.png" decoding="async" data-file-width="240" data-file-height="260" data-file-type="drawing" height="22" width="20" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/7/79/SuitDiamonds4colors.svg/40px-SuitDiamonds4colors.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/7/79/SuitDiamonds4colors.svg/40px-SuitDiamonds4colors.svg.png 2x" class="mw-file-element"/></a></span>).</li></ol></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">rhombus</strong>
  </span>
</p>
<ol><li><span class="usage-label-sense"><span class="ib-brac label-brac">(</span><span class="ib-content label-content">geometry</span><span class="ib-brac label-brac">)</span></span> A parallelogram having all sides of equal length. <style>.mw-parser-output .defdate{font-size:smaller}</style><span class="defdate">[from 16th c.]</span>
<ol><li>The rhombus diamond, as one of the suits seen in a deck of playing cards (<span><img alt="♦" src="20px-SuitDiamonds.png" decoding="async" height="22" width="20" class="mw-file-element"/></span> or <span><img alt="♦" src="20px-SuitDiamonds4colors.png" decoding="async" height="22" width="20" class="mw-file-element"/></span>).</li></ol></li>
</section>""",
                    "images": [
                        "//upload.wikimedia.org/wikipedia/commons/thumb/d/db/SuitDiamonds.svg/20px-SuitDiamonds.svg.png",
                        "//upload.wikimedia.org/wikipedia/commons/thumb/7/79/SuitDiamonds4colors.svg/20px-SuitDiamonds4colors.svg.png",
                    ],
                },
            ],
        )

    def test_score_sound(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Italian augmented sixth chord</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">Italian augmented sixth chord</strong>
  </span>
</p>
<ol><li><span class="usage-label-sense"><span class="ib-brac label-brac">(</span><span class="ib-content label-content">music</span><span class="ib-brac label-brac">)</span></span> a chord with the tonic, lowered submediant, and raised subdominant scale degrees
<dl><dd><div class="h-usage-example"><i class="Latn mention e-example" lang="en">C <b>Italian augmented sixth chord</b><span>:</span><br/><div class="mw-ext-score noresize" data-midi="//upload.wikimedia.org/score/r/a/rai5gcag11ug70nkzqlrjaxl0zvsfyv/rai5gcag.midi" typeof="mw:Extension/score" about="#mwt6" data-mw='{"name":"score","attrs":{"sound":""},"body":{"extsrc":"&lt;c&apos;aes fis&apos;>1"}}'><img src="//upload.wikimedia.org/score/r/a/rai5gcag11ug70nkzqlrjaxl0zvsfyv/rai5gcag.png" width="115" height="60" alt="&lt;c'aes fis'>1"/><div style="margin-top: 3px;"><audio controls=""><source src="//upload.wikimedia.org/score/r/a/rai5gcag11ug70nkzqlrjaxl0zvsfyv/rai5gcag.mp3" type="audio/mpeg"/><div>Audio playback is not supported in your browser. You can <a href="//upload.wikimedia.org/score/r/a/rai5gcag11ug70nkzqlrjaxl0zvsfyv/rai5gcag.mp3">download the audio file</a>.</div></audio></div></div></i></div></dd></dl></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">Italian augmented sixth chord</strong>
  </span>
</p>
<ol><li><span class="usage-label-sense"><span class="ib-brac label-brac">(</span><span class="ib-content label-content">music</span><span class="ib-brac label-brac">)</span></span> a chord with the tonic, lowered submediant, and raised subdominant scale degrees
<dl><dd><div class="h-usage-example"><i class="Latn mention e-example" lang="en">C <b>Italian augmented sixth chord</b><span>:</span><br/><div class="mw-ext-score noresize"><img src="rai5gcag.png" width="115" height="60" alt="&lt;c'aes fis'>1"/></div></i></div></dd></dl></li></ol>
</section>""",
                    "images": [
                        "//upload.wikimedia.org/score/r/a/rai5gcag11ug70nkzqlrjaxl0zvsfyv/rai5gcag.png"
                    ],
                },
            ],
        )

    def test_math_example(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>binomial theorem</title></head>
<body>
<section><h2>English</h2>
<section><h3>Proper noun</h3>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">the binomial theorem</strong>
  </span>
</p>
<ol><li>gloss<dl><dd>
<span class="mwe-math-element mwe-math-element-inline">
<img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/79b6d531a4481eeb1be6fd20769cfcc0da365062"/>
</span>
</dd></dl></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["the binomial theorem", "binomial theorem"],
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Proper noun</h4>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">the binomial theorem</strong>
  </span>
</p>
<ol><li>gloss<dl><dd>
<span class="mwe-math-element mwe-math-element-inline">
<img src="79b6d531a4481eeb1be6fd20769cfcc0da365062.svg"/>
</span>
</dd></dl></li></ol>
</section>""",
                    "images": [
                        "https://wikimedia.org/api/rest_v1/media/math/render/svg/79b6d531a4481eeb1be6fd20769cfcc0da365062"
                    ],
                },
            ],
        )

    def test_li_synonyms(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>hypocrite</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">hypocrite</strong>
  </span>
</p>
<ol><li>gloss<dl>
<dd><span class="nyms synonym"><span style="font-size: smaller">Synonyms:</span> <span class="Latn" lang="en"><a>flip-flopper</a></span>, <span class="Latn" lang="en"><a>pretender</a></span>; <i>see also</i> <a>Thesaurus:<span class="Latn" lang="en">deceiver</span></a></span></dd>
<dd><span class="nyms synonym"><span style="font-size: smaller">Synonyms:</span> <i>see</i> <a>Thesaurus:<span class="Latn" lang="en">dictionary</span></a></span></dd>
<dd><span class="nyms hypernym"><span style="font-size: smaller">Hypernym:</span> <span class="Latn" lang="en"><a>wordbook</a></span></span></dd>
</dl></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">hypocrite</strong>
  </span>
</p>
<ol><li>gloss<dl>
<dd><span class="nyms synonym"><span style="font-size: smaller">Synonyms:</span> <span class="Latn" lang="en">flip-flopper</span>, <span class="Latn" lang="en">pretender</span>; <i>see also</i> Thesaurus:<span class="Latn" lang="en">deceiver</span></span></dd>
<dd><span class="nyms synonym"><span style="font-size: smaller">Synonyms:</span> <i>see</i> Thesaurus:<span class="Latn" lang="en">dictionary</span></span></dd>
</dl></li></ol>
</section>""",
                },
            ],
        )

    def test_li_alt_forms(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>portmanteau</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">portmanteau</strong>
  </span>
</p>
<ol><li>gloss
<dl><dd><span class="nyms alternative-form"><span style="font-size: smaller">Alternative forms:</span> <span class="Latn" lang="en"><a>portemanteau</a></span>, <span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content">obsolete</span><span class="ib-brac qualifier-brac">)</span> <span class="Latn" lang="en"><a>portmantua</a></span></span></dd></dl></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["portmanteau", "portemanteau", "portmantua"],
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">portmanteau</strong>
  </span>
</p>
<ol><li>gloss
<dl><dd><span class="nyms alternative-form"><span style="font-size: smaller">Alternative forms:</span> <span class="Latn" lang="en">portemanteau</span>, <span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content">obsolete</span><span class="ib-brac qualifier-brac">)</span> <span class="Latn" lang="en">portmantua</span></span></dd></dl></li></ol>
</section>""",
                },
            ],
        )

    def test_rm_rfdef(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>intrigued</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">intrigued</strong>
  </span>
</p>
<ol><li><i typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"rfdef"}}}]}'>This term needs a definition. Please help out and <b>add a definition</b>, then remove the text <code style="white-space:pre-wrap"><span>{</span><span>{</span><a>rfdef</a><span>}</span><span>}</span></code></i><span>.</span></li></ol>
</section>
</section>
</body>
</html>""",
            [],
        )

    def test_rm_maintenance_line(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>hinge</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">hinge</strong>
  </span>
</p>
<ol><li><span class="maintenance-line">(<span id="rfm-sense-notice-en-"></span>Should we <a >move, merge or split</a><sup class="plainlinks">(<a class="external text">+</a>)</sup> this sense?)</span> <span class="usage-label-sense"><span class="ib-brac label-brac">(</span><span class="ib-content label-content"><a>intransitive</a><span class="ib-comma label-comma">,</span><span> </span>with <i class="Latn mention" lang="en"><a>on</a></i> or <i class="Latn mention" lang="en"><a>upon</a></i></span><span class="ib-brac label-brac">)</span></span> To <a>depend</a> on something.</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">hinge</strong>
  </span>
</p>
<ol><li> <span class="usage-label-sense"><span class="ib-brac label-brac">(</span><span class="ib-content label-content">intransitive<span class="ib-comma label-comma">,</span><span> </span>with <i class="Latn mention" lang="en">on</i> or <i class="Latn mention" lang="en">upon</i></span><span class="ib-brac label-brac">)</span></span> To depend on something.</li></ol>
</section>""",
                },
            ],
        )

    def test_zh_also_zh_co(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>底</title></head>
<body>
<section><h2>Chinese</h2>
<section><h3>Noun</h3>
<p>
  <span class="headword-line">
    <strong class="Hani headword" lang="zh">底</strong>
  </span>
</p>
<ol><li>gloss<dl><dd><span data-mw='{"parts":[{"template":{"target":{"wt":"zh-also"}}}]}'>See also: </span><span class="Hani" lang="zh">年底</span><span>, </span><span class="Hani" lang="zh">月底</span></dd>
<dd><span lang="zh-Hant" class="Hant" data-mw='{"parts":[{"template":{"target":{"wt":"zh-co"}}}]}'>六月<b>底</b></span><span> </span><span><span>[</span>Cantonese<span>]</span></span><span> </span><span> ―</span><span> </span><span> </span><span lang="zh-Latn"><i>luk<sup>6</sup> jyut<sup>6</sup> <b>dai<sup>2</sup></b> </i></span><span> </span><span><span>[</span>Jyutping<span>]</span></span><span> </span><span> ―</span><span> </span><span> </span><b>end</b><span> of June</span></dd></dl></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p>
  <span class="headword-line">
    <strong class="Hani headword" lang="zh">底</strong>
  </span>
</p>
<ol><li>gloss<dl><dd><span>See also: </span><span class="Hani" lang="zh">年底</span><span>, </span><span class="Hani" lang="zh">月底</span></dd>
<dd><span lang="zh-Hant" class="Hant">六月<b>底</b></span><span> </span><span><span>[</span>Cantonese<span>]</span></span><span> </span><span> ―</span><span> </span><span> </span><span lang="zh-Latn"><i>luk<sup>6</sup> jyut<sup>6</sup> <b>dai<sup>2</sup></b> </i></span><span> </span><span><span>[</span>Jyutping<span>]</span></span><span> </span><span> ―</span><span> </span><span> </span><b>end</b><span> of June</span></dd></dl></li></ol>
</section>""",
                },
            ],
        )

    def test_alt_of_with_forms(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>dike</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">dike</strong> (<i>plural</i> <b class="Latn form-of lang-en p-form-of" lang="en">dikes</b>)</span></p>
<ol><li><span class="usage-label-sense"><span class="ib-brac label-brac">(</span><span class="ib-content label-content">chiefly<span> </span>US</span><span class="ib-brac label-brac">)</span></span> <span class="form-of-definition use-with-mention">Alternative spelling of <span class="form-of-definition-link"><i class="Latn mention" lang="en">dyke</i></span></span>: ditch; embankment; waterway; etc.</li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p><span class="headword-line"><strong class="Latn headword" lang="en">dike</strong> (<i>plural</i> <b class="Latn form-of lang-en p-form-of" lang="en">dikes</b>)</span></p>
<ol><li><span class="usage-label-sense"><span class="ib-brac label-brac">(</span><span class="ib-content label-content">chiefly<span> </span>US</span><span class="ib-brac label-brac">)</span></span> <span class="form-of-definition use-with-mention">Alternative spelling of <span class="form-of-definition-link"><i class="Latn mention" lang="en">dyke</i></span></span>: ditch; embankment; waterway; etc.</li></ol>
</section>""",
                    "forms": ["dike", "dikes"],
                    "form_of_targets": ["dyke"],
                    "form_of_only": True,
                },
            ],
        )

    def test_chinese_alt_form_of(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>琴瑟合鳴</title></head>
<body>
<section><h2>Chinese</h2>
<section><h3>Idiom</h3>
<p><span class="headword-line"><strong class="Hant headword" lang="zh">琴瑟合鳴</strong></span></p>
<ol><li><span class="form-of-definition use-with-mention">alternative form of <span class="form-of-definition-link"><i class="Hant mention" lang="zh">琴瑟和鳴</i><span class="Zsym mention" style="font-size:100%;"><span> </span>/ </span><i class="Hans mention" lang="zh">琴瑟和鸣</i> <span class="mention-gloss-paren annotation-paren">(</span><span lang="zh-Latn" class="mention-tr tr Latn">qínsèhémíng</span><span class="mention-gloss-paren annotation-paren">)</span></span></span></li></ol>
</section>
</section>
</body>
</html>""",
            [{"form_of_targets": ["琴瑟和鳴", "琴瑟和鸣"], "form_of_only": True}],
        )

    def test_usage_notes(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>serendipity</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">serendipity</strong></span></p>
<ol><li>gloss</li></ol>
<section><h5>Usage notes</h5>
<ul><li>usage notes text</li></ul>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p><span class="headword-line"><strong class="Latn headword" lang="en">serendipity</strong></span></p>
<ol><li>gloss</li></ol>
<section><h4>Usage notes</h4>
<ul><li>usage notes text</li></ul>
</section>
</section>""",
                },
            ],
        )

    def test_zh_x_single_line(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>大家</title></head>
<body>
<section><h2>Chinese</h2>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">大家</strong>
</span></p>
<ol><li>gloss
<dl><dd><span lang="zh-Hant" class="Hant" data-mw='{"parts":[{"template":{"target":{"wt":"zh-x"}}}]}'><b>大家</b>閨秀</span><span lang="zh-Hani" class="Hani">／</span><span lang="zh-Hans" class="Hans"><b>大家</b>闺秀</span><span> </span><span> ―</span><span> </span><span> </span><span lang="zh-Latn"><i><b>dàjiā</b>guīxiù</i></span><span> </span><span> ―</span><span> </span><span> unmarried daughter of a noble house</span></dd></dl></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p><span class="headword-line"><strong class="Hani headword" lang="zh">大家</strong>
</span></p>
<ol><li>gloss
<dl><dd><span lang="zh-Hant" class="Hant"><b>大家</b>閨秀</span><span lang="zh-Hani" class="Hani">／</span><span lang="zh-Hans" class="Hans"><b>大家</b>闺秀</span><span> </span><span> ―</span><span> </span><span> </span><span lang="zh-Latn"><i><b>dàjiā</b>guīxiù</i></span><span> </span><span> ―</span><span> </span><span> unmarried daughter of a noble house</span></dd></dl></li></ol>
</section>""",
                },
            ],
        )

    def test_only_check_li_under_ol(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>tore</title></head>
<body>
<section><h2>English</h2>
<section><h3>Verb</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">tore</strong></span></p>
<ol><li><span class="form-of-definition use-with-mention">simple past of <span class="form-of-definition-link"><i class="Latn mention" lang="en"><a rel="mw:WikiLink" href="./tear#English" title="tear">tear</a></i> <span class="mention-gloss-paren annotation-paren">(</span><span class="mention-gloss-double-quote">“</span><span class="mention-gloss">rip, rend, speed</span><span class="mention-gloss-double-quote">”</span><span class="mention-gloss-paren annotation-paren">)</span></span></span>.</li>
<li><span class="form-of-definition use-with-mention">past participle of <span class="form-of-definition-link"><i class="Latn mention" lang="en"><a rel="mw:WikiLink" href="./tear#English" title="tear">tear</a></i> <span class="mention-gloss-paren annotation-paren">(</span><span class="mention-gloss-double-quote">“</span><span class="mention-gloss">rip, rend, speed</span><span class="mention-gloss-double-quote">”</span><span class="mention-gloss-paren annotation-paren">)</span></span></span>
<ul><li><div class="citation-whole"></div></li></ul>
</li><li></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {"form_of_only": True, "form_of_targets": ["tear"]},
            ],
        )

    def test_rm_inter_project_class(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>shin</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">shin</strong></span></p>
<ol><li>gloss<span class="interProject">Wikipedia</span></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="en">
<h4>Noun</h4>
<p><span class="headword-line"><strong class="Latn headword" lang="en">shin</strong></p>
<ol><li>gloss</li></ol>
</section>"""
                }
            ],
        )
