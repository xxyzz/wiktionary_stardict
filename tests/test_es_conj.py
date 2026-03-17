from utils import XMLTestCase


class EsConjTestCase(XMLTestCase):
    edition = "es"

    def test_add_conj_to_verb_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>acontecer</title></head>
<body>
<section><h2><a>Español</a></h2>
<section><h4>Verbo intransitivo y terciopersonal</h4>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>
<section><h4>Sustantivo masculino</h4>
<dl><dt>2</dt><dd>gloss</dd></dl>
</section>
<section><h4>Conjugación</h4>
<table><tbody><tr>
<td><a>hubiera</a><a> acontecido</a>, <a>hubiese</a><a> acontecido</a></td>
<td><a>aconteciera</a>, <a>aconteciese</a></td>
</tr></tbody></table>
</section>
</section>
</body>
</html>""",
            [
                [
                    ["acontecer", "acontecido", "aconteciera", "aconteciese"],
                    """<section>
<h4>Verbo intransitivo y terciopersonal</h4>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>""",
                    [],
                ],
                [
                    ["acontecer"],
                    """<section>
<h4>Sustantivo masculino</h4>
<dl><dt>2</dt><dd>gloss</dd></dl>
</section>""",
                    [],
                ],
            ],
        )

    def test_inconformarse(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>inconformarse</title></head>
<body>
<section><h2><a>Español</a></h2>
<section><h4>Verbo pronominal</h4>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>
<section><h3>Conjugación</h3>
<table><tbody><tr>
<td><span class="movil">que tú<span> </span></span>te <a>inconformaras</a>, te <a>inconformases</a></td>
<td><span class="movil">que tú<span> </span></span>te <a>hubieras</a><a> inconformado</a>, te <a>hubieses</a><a> inconformado</a></td>
</tr></tbody></table>
</section>
</section>
</body>
</html>""",
            [
                [
                    ["inconformarse", "inconformaras", "inconformases", "inconformado"],
                    """<section>
<h4>Verbo pronominal</h4>
<dl><dt>1</dt><dd>gloss</dd></dl>
</section>""",
                    [],
                ],
            ],
        )
