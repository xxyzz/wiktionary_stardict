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

<ol id="mwMA"><li id="mwMQ"><span class="use-with-mention" about="#mwt17" typeof="mw:Transclusion" data-mw='{"parts":[{"template":{"target":{"wt":"Latn-def","href":"./Template:Latn-def"},"params":{"1":{"wt":"en"},"2":{"wt":"name"},"3":{"wt":"T"},"4":{"wt":"t"}},"i":0}}]}' id="mwMg">The name of the <a rel="mw:WikiLink" href="./Appendix:Latin_script" title="Appendix:Latin script">Latin script</a> letter <i class="Latn mention" lang="en"><a rel="mw:WikiLink" href="./T#English" title="T">T</a></i>/<i class="Latn mention" lang="en"><a rel="mw:WikiLink" href="./t#English" title="t">t</a></i>.</span><link rel="mw:PageProp/Category" href="./Category:en:Latin_letter_names#TEE" about="#mwt17" id="mwMw"/></li></ol>
</section>
</section>
</body>
</html>""",
            [
                [
                    ["tee", "tees"],
                    """<section>
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
      </ol>
    </section>""",
                    [],
                ],
            ],
        )

    def test_remove_form_of_gloss(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>books</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">books</strong></span></p>
<ol><li><span class="form-of-definition use-with-mention">plural of <span class="form-of-definition-link"><i class="Latn mention" lang="en">book</i></span></span></li></ol>
</section>
</section>
</body>
</html>""",
            [],
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
                [
                    ["-ego"],
                    """<section>
      <h3>Suffix</h3>
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
                    [],
                ],
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
                [
                    ["-άρης"],
                    """<section>
      <h3>Suffix</h3>
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
                    [],
                ],
            ],
        )

    def test_empty_def_list(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>tee</title></head>
<body>
<section><h2>English</h2>
<section><h3>Noun</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">tee</strong></span></p>
<ol>
   <li>gloss 1</li>
   <li class="mw-empty-elt" id="mwRg"></li>
</ol>
</section>
</section>
</body>
</html>""",
            [
                [
                    ["tee"],
                    """<section>
      <h3>Noun</h3>
      <p>
        <span class="headword-line">
          <strong class="Latn headword" lang="en">tee</strong>
        </span>
      </p>
      <ol>
        <li>gloss 1</li>
      </ol>
    </section>""",
                    [],
                ],
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
                [
                    ["binomial series"],
                    """<section><h3>Noun</h3>
<p>
  <span class="headword-line">
    <strong class="Latn headword" lang="en">binomial series</strong>
  </span>
</p>
<ol>
   <li>The Maclaurin series expansion <span class="mwe-math-element mwe-math-element-inline" ><img src="d253b87bf18d329bd2d1c12ee1ebba5071003ca8.svg" class="mwe-math-fallback-image-inline mw-invert skin-invert" aria-hidden="true" style="vertical-align: -1.005ex; width:11.63ex; height:3.176ex;"/></span></li>
</ol>
</section>""",
                    [
                        "https://wikimedia.org/api/rest_v1/media/math/render/svg/d253b87bf18d329bd2d1c12ee1ebba5071003ca8"
                    ],
                ]
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
                [
                    ["ꜣḫt-jtn"],
                    """<section><h3>Proper noun</h3>
<p>
  <span class="headword-line">
    <strong class="None headword" lang="egy">
      <img class="skin-invert" style="margin: 1px;" src="hiero_N27.png" height="22" title="N27 [Axt]" alt="Axt"/>
    </strong>
  </span>
</p>
<ol><li>gloss</li></ol>
</section>""",
                    ["/w/extensions/wikihiero/img/hiero_N27.png?fee08"],
                ]
            ],
        )
