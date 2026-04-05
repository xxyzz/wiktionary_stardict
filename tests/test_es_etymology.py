from utils import XMLTestCase


class EsEtymologyTestCase(XMLTestCase):
    edition = "es"

    def test_etymology_sections(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>livre</title></head>
<body>
<section><h2>Francés</h2>
<section><h3>Etimología 1</h3>
<p>etymology 1<sup class="mw-ref reference">ref</sup></p>
<section><h3>Sustantivo masculino</h3>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>
</section>

<section><h3>Etimología 2</h3>
<p>etymology 2</p>
<section><h3>Sustantivo femenino</h3>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="es">
<h4>Sustantivo masculino</h4>
<dl><dt>1</dt><dd>gloss</dd></dl>
<section><h4>Etimología</h4>
<p>etymology 1</p>
</section>
</section>""",
                },
                {
                    "def": """<section dir="ltr" lang="es">
<h4>Sustantivo femenino</h4>
<dl><dt>1</dt><dd>gloss</dd></dl>
<section><h4>Etimología</h4>
<p>etymology 2</p>
</section>
</section>""",
                },
            ],
        )

    def test_missing_etymology(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Schreck</title></head>
<body>
<section><h2>Alemán</h2>
<section><h3>Etimología 1</h3>
<p><span class="notheme"><i>Si puedes, incorpórala: ver cómo</i><link rel="mw:PageProp/Category" href="./Categoría:DE:Palabras_de_etimología_sin_precisar"/></span>.</p>
<section><h3>Sustantivo masculino</h3>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="es">
<h4>Sustantivo masculino</h4>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>""",
                }
            ],
        )
