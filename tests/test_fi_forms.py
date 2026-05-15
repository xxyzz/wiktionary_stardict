from utils import XMLTestCase


class FiFormsTestCase(XMLTestCase):
    edition = "fi"

    def test_ru_verbi(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>бросить</title></head>
<body>
<section><h2>Venäjä</h2>
<section><h3>Verbi</h3>
<p><b lang="ru" class="hakusana Cyrl">бро́сить</b> <span>(</span><a>II</a><span>)</span> <span>(</span><i><a>perfektiivinen</a></i><span>)</span> (<i>imperfektiivinen</i> <b><a title="бросать">броса́ть</a></b>)</p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [{"forms": ["бро́сить", "бросить", "броса́ть", "бросать"]}],
        )
