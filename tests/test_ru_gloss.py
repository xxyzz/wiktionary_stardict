from utils import XMLTestCase


class RuGlossTestCase(XMLTestCase):
    edition = "ru"

    def test_examples(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>keep</title></head>
<body>
<section><h1><span></span><span>Английский</span></h1>
<section><h3>Семантические свойства</h3>
<section><h4><span></span>Значение</h4>
<ol><li>иметь, хранить <span class="example-fullblock"><span>◆</span><span> </span><span class="example-block">to <b class="example-select">keep</b> smb. in prison<span class="example-translate"><span> </span>—<span> </span><b class="example-select">держать</b> кого-л. в тюрьме</span> <span class="example-details"> <i><span class="citation-source"> </span></i></span></span></span> <span class="example-fullblock "><span>◆</span><span> </span><span class="example-block">to <b class="example-select">keep</b> money in the savings-bank<span class="example-translate"><span> </span>—<span> </span><b class="example-select">хранить</b> деньги в сбербанке</span> <span class="example-details"> <i><span class="citation-source"> </span></i></span></span></span></li>
<li><a>держать</a>, <a>содержать</a>
<ol><li>Иметь (кого-л.) в услужении</li></ol></li>
<li class="mw-empty-elt" id="mwLA"></li>
</ol>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="ru">
<h4>Значение</h4>
<ol><li>иметь, хранить <span class="example-fullblock"><span>◆</span><span> </span><span class="example-block">to <b class="example-select">keep</b> smb. in prison<span class="example-translate"><span> </span>—<span> </span><b class="example-select">держать</b> кого-л. в тюрьме</span> <span class="example-details"> <i><span class="citation-source"> </span></i></span></span></span> </li>
<li>держать, содержать
<ol><li>Иметь (кого-л.) в услужении</li></ol></li>
</ol>
</section>""",
                },
            ],
        )

    def test_missing_example(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Фемиксира</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Семантические свойства</h3>
<section><h4>Значение</h4>
<ol><li>gloss <span class="example-fullblock example-absent-block"><span>◆</span><span> </span><span class="example-block"><span class="example-absent">Отсутствует пример употребления (см. <span class="example-recommendations">рекомендации</span>).</span> <span class="example-details"> <i><span class="citation-source"> </span></i></span></span></span></li></ol>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="ru">
<h4>Значение</h4>
<ol><li>gloss </li></ol>
</section>""",
                },
            ],
        )
