from utils import XMLTestCase


class RuEtymologyTestCase(XMLTestCase):
    edition = "ru"

    def test_etymology_p(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>бежать</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Семантические свойства</h3>
<section><h4>Значение</h4>
<ol><li>gloss</li></ol>
</section></section>
<section><h3>Этимология</h3>
<p>etymology text</p>
</section></section>
</body></html>""",
            [
                {
                    "def": """<section dir="ltr" lang="ru">
<h4>Значение</h4>
<ol><li>gloss</li></ol>
<section><h4>Этимология</h4>
<p>etymology text</p>
</section>
</section>""",
                },
            ],
        )

    def test_missing_etymology(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Фемиксира</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Семантические свойства</h3>
<section><h4>Значение</h4>
<ol><li>gloss</li></ol>
</section></section>
<section><h3>Этимология</h3>
<p>От <span>??</span><link rel="mw:PageProp/Category" href="./Категория:Нужна_этимология"/></p>
</section></section>
</body></html>""",
            [
                {
                    "def": """<section dir="ltr" lang="ru">
<h4>Значение</h4>
<ol><li>gloss</li></ol>
</section>""",
                },
            ],
        )
