from utils import XMLTestCase


class EsPOSTestCase(XMLTestCase):
    edition = "es"

    def test_dl_list(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>correr</title></head>
<body>
<section data-mw-section-id="1" id="mwAw"><h2 id="Español"><span id="Espa.C3.B1ol" typeof="mw:FallbackId"></span><span id="es" class="headline-lang" about="#mwt1" typeof="mw:Transclusion" data-mw='{"parts":[]}'></span><a rel="mw:WikiLink">Español</a><link/></h2>

<section><h3><span></span>Etimología 1</h3>
<section><h4><span>Verbo intransitivo</span></h4>
<dl><dt>1</dt><dd>Desplazarse rápidamente sobre el suelo mediante el movimiento alternado de las piernas o de las patas.</dd>
<dt>2</dt><dd>Desplazarse rápidamente de cualquier otra forma, un vehículo, cosa o ser.
<ul><li><b>Ejemplo:</b> Mi auto corre a 290 km por hora.</li>
<li><b>Ejemplo:</b> Unas nubecillas corrían por el cielo.</li></ul></dd>
<dt id="mwGw">4</dt><dd id="mwHA">Tener prisa, estar muy ocupado en una actividad.
<ul><li><b>Sinónimos:</b> <span><a>ajetrearse</a></span>, <span><a>darse prisa</a></span>.</li>
<li><b>Antónimo:</b> <span><a>relajarse</a></span>.</li>
<li><b>Ejemplo:</b><span> </span><div class="mw-collapsible mw-collapsed"></div></li></ul></dd></dl>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["correr"],
                    "def": """<section class="mw-parser-output" dir="ltr" lang="es">
<h4><span>Verbo intransitivo</span></h4>
<dl><dt>1</dt><dd>Desplazarse rápidamente sobre el suelo mediante el movimiento alternado de las piernas o de las patas.</dd>
<dt>2</dt><dd>Desplazarse rápidamente de cualquier otra forma, un vehículo, cosa o ser.
<ul><li><b>Ejemplo:</b> Mi auto corre a 290 km por hora.</li></ul></dd>
<dt>4</dt><dd>Tener prisa, estar muy ocupado en una actividad.
<ul><li><b>Sinónimos:</b> <span>ajetrearse</span>, <span>darse prisa</span>.</li>
<li><b>Antónimo:</b> <span>relajarse</span>.</li>
</ul></dd></dl>
</section>""",
                },
            ],
        )

    def test_es_sust_space(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>arco iris</title></head>
<body>
<section><h2><a>Español</a></h2>
<section><h3><span>Locución sustantiva masculina</span></h3>
<p><b typeof="mw:Transclusion">arc<span>o</span> iri<span>s</span></b><span> (</span><i>copulativa</i><span>)</span><span> </span><span>¦</span><span> </span><span>plural: </span><a>arc<span>os</span></a><span> </span><a>iri<span>s</span></a></p>

<dl><dt>1</dt><dd>gloss</dd></dl>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["arco iris", "arcos iris"],
                    "def": """<section class="mw-parser-output" dir="ltr" lang="es">
<h4><span>Locución sustantiva masculina</span></h4>
<p><b>arc<span>o</span> iri<span>s</span></b><span> (</span><i>copulativa</i><span>)</span><span> </span><span>¦</span><span> </span><span>plural: </span>arc<span>os</span><span> </span>iri<span>s</span></p>

<dl><dt>1</dt><dd>gloss</dd></dl>
</section>""",
                },
            ],
        )

    def test_es_sust_comma(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>gurú</title></head>
<body>
<section><h2><a>Español</a></h2>
<section><h3><span>Sustantivo femenino y masculino</span></h3>
<p><b typeof="mw:Transclusion">gur<span>ú</span></b><span> (</span><i>sin género</i><span>)</span><span> </span><span>¦</span><span> </span><span>plural: </span><a>gur<span>ús</span></a><span>, </span><a>gur<span>úes</span></a></p>

<dl><dt>1</dt><dd>gloss</dd></dl>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["gurú", "gurús", "gurúes"],
                    "def": """<section class="mw-parser-output" dir="ltr" lang="es">
<h4><span>Sustantivo femenino y masculino</span></h4>
<p><b>gur<span>ú</span></b><span> (</span><i>sin género</i><span>)</span><span> </span><span>¦</span><span> </span><span>plural: </span>gur<span>ús</span><span>, </span>gur<span>úes</span></p>

<dl><dt>1</dt><dd>gloss</dd></dl>
</section>""",
                }
            ],
        )

    def test_ja_lang_name(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>世界</title></head>
<body>
<section><h2><a>Japonés</a><span> </span><small>(Kanji)</small></h2>
<section><h3>Sustantivo</h3>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>
</section>
</body>
</html>""",
            [
                {
                    "lang": "Japonés",
                    "forms": ["世界"],
                    "def": """<section class="mw-parser-output" dir="ltr" lang="es">
<h4>Sustantivo</h4>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>""",
                }
            ],
        )

    def test_redundant_p(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>audino</title></head>
<body>
<section><h2>Español</h2>
<section><h3>Adjetivo</h3>
<p><b typeof="mw:Transclusion">audin<span>o</span></b><span> </span><span>¦</span><span> </span><span>plural: </span><a>audin<span>os</span></a></p>
<dl><dt>1</dt><dd>gloss</dd></dl>
<p><br/></p>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["audino", "audinos"],
                    "def": """<section class="mw-parser-output" dir="ltr" lang="es">
<h4>Adjetivo</h4>
<p><b>audin<span>o</span></b><span> </span><span>¦</span><span> </span><span>plural: </span>audin<span>os</span></p>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>""",
                },
            ],
        )

    def test_facebook_p(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Facebook</title></head>
<body>
<section><h2>Español</h2>
<section><h3>Etimología 1</h3>
<p><span>Del inglés </span><i>facebook</i> ("directorio de fotos"), compuesto de <span>face</span><span> </span><span>('</span>rostro<span>')</span> y <span>book</span><span> </span><span>('</span>libro<span>')</span>.
<b typeof="mw:Transclusion">Facebook</b><span> (</span><i>singularia tantum</i><span>)</span></p>
<dl><dt>1 <span>Internet</span></dt><dd>gloss</dd></dl>
</section>
</section>
</body>
</html>""",
            [
                {
                    "forms": ["Facebook"],
                    "def": """<section class="mw-parser-output" dir="ltr" lang="es">
<h4>Etimología 1</h4>
<dl><dt>1 <span>Internet</span></dt><dd>gloss</dd></dl>
</section>""",
                },
            ],
        )
