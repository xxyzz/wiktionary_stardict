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
