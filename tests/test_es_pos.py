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
                [
                    ["correr"],
                    """<section>
<h4><span>Verbo intransitivo</span></h4>
<dl><dt>1</dt><dd>Desplazarse rápidamente sobre el suelo mediante el movimiento alternado de las piernas o de las patas.</dd>
<dt>2</dt><dd>Desplazarse rápidamente de cualquier otra forma, un vehículo, cosa o ser.
<ul><li><b>Ejemplo:</b> Mi auto corre a 290 km por hora.</li></ul></dd>
<dt>4</dt><dd>Tener prisa, estar muy ocupado en una actividad.
<ul><li><b>Sinónimos:</b> <span>ajetrearse</span>, <span>darse prisa</span>.</li>
<li><b>Antónimo:</b> <span>relajarse</span>.</li>
</ul></dd></dl>
</section>""",
                    [],
                ],
            ],
        )
