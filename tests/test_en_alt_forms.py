from utils import XMLTestCase


class EnAltFormsTestCase(XMLTestCase):
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
            [
                [
                    ["berserker", "berserkar", "berserkers"],
                    """<section>
      <h4>Noun</h4>
      <p>
        <span class="headword-line">
          <strong class="Latn headword" lang="en">berserker</strong> (<i>plural</i> <b class="Latn form-of lang-en p-form-of" lang="en">berserkers</b>)
        </span>
      </p>
      <ol>
        <li>
          <span>gloss</span>
        </li>
      </ol>
    </section>""",
                    [],
                ],
            ],
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
            [
                [
                    ["大家", "乾家", "干家"],
                    """<section>
      <h4>Noun</h4>
      <p>
        <span class="headword-line">
          <strong class="Hani headword" lang="zh">大家</strong></b>
        </span>
      </p>
      <ol>
        <li>
          <span>gloss</span>
        </li>
      </ol>
    </section>""",
                    [],
                ],
            ],
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
            [
                [
                    ["白麵", "白麪", "白面"],
                    """<section>
      <h4>Noun</h4>
      <p>
        <span class="headword-line">
          <strong class="Hani headword" lang="zh">白麵</strong></b>
        </span>
      </p>
      <ol>
        <li>
          <span>gloss</span>
        </li>
      </ol>
    </section>""",
                    [],
                ],
            ],
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
                [
                    ["門閥", "门阀"],
                    """<section>
      <h4>Noun</h4>
      <p>
        <span class="headword-line">
          <strong class="Hani headword" lang="zh">門閥</strong></b>
        </span>
      </p>
      <ol>
        <li>
          <span>gloss</span>
        </li>
      </ol>
    </section>""",
                    [],
                ],
            ],
        )
