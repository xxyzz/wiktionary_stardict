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
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ru">
<h4><span></span>Значение</h4>
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
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ru">
<h4>Значение</h4>
<ol><li>gloss </li></ol>
</section>""",
                },
            ],
        )

    def test_form_of(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>адекватно</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Семантические свойства</h3>
<section><h4>Значение</h4>
<ol><li><a data-mw='{"parts":[{"template":{"target":{"wt":"наречие","href":"./Шаблон:наречие"},"params":{"1":{"wt":"адекватный"}},"i":0}}]}'>наречие</a><span> к </span><i><a rel="mw:WikiLink" href="./адекватный" title="адекватный">адекватный</a></i>; в соответствии с чем-либо</li>
<li class="mw-empty-elt"></li></ol>
</section></section></section></body></html>""",
            [{"form_of_only": True, "form_of_targets": ["адекватный"]}],
        )
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>меньше</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Семантические свойства</h3>
<section><h4>Значение</h4>
<ol><li><span class="label mark" data-mw='{"parts":[{"template":{"target":{"wt":"помета","href":"./Шаблон:помета"},"params":{"1":{"wt":"нареч."}},"i":0}}]}'>нареч.</span> <a data-mw='{"parts":[{"template":{"target":{"wt":"сравн.","href":"./Шаблон:сравн."},"params":{"к":{"wt":"нареч"},"1":{"wt":"мало"}},"i":0}}]}'><span class="label " title="сравнительная степень">сравн. ст.</span></a><span> </span><span>к </span><a rel="mw:WikiLink" href="./наречие" title="наречие">нареч.</a><span> </span><a rel="mw:WikiLink" href="./мало" title="мало">мало</a></li></ol>
</section></section></section></body></html>""",
            [{"form_of_only": True, "form_of_targets": ["наречие"]}],
        )

    def test_form_of_id(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>связанный</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Семантические свойства</h3>
<section><h4>Значение</h4>
<ol><li><i data-mw='{"parts":[{"template":{"target":{"wt":"прич.","href":"./Шаблон:прич."},"params":{"1":{"wt":"[[связать#связать I|связать I]]"},"2":{"wt":"прош"},"3":{"wt":"страд"}},"i":0}}]}'><a>страд. прич.</a> <a>прош. вр.</a></i><span> от </span><a rel="mw:WikiLink" href="./связать#связать_I" title="связать">связать I</a>; изготовленный вязанием</li>
<li><i data-mw='{"parts":[{"template":{"target":{"wt":"прич.","href":"./Шаблон:прич."},"params":{"1":{"wt":"[[связать#связать I|связать I]]"},"2":{"wt":"прош"},"3":{"wt":"страд"}},"i":0}}]}'><a>страд. прич.</a> <a>прош. вр.</a></i><span> от </span><a rel="mw:WikiLink" href="./связать#связать_I" title="связать">связать I</a>; <a rel="mw:WikiLink" href="./соединённый" title="соединённый" id="mwmA">соединённый</a>, <a rel="mw:WikiLink" href="./скреплённый" title="скреплённый" id="mwmQ">скреплённый</a> верёвками; <a rel="mw:WikiLink" href="./привязанный" title="привязанный" id="mwmg">привязанный</a></li>
<li><i data-mw='{"parts":[{"template":{"target":{"wt":"прич.","href":"./Шаблон:прич."},"params":{"1":{"wt":"[[связать#связать II|связать II]]"},"2":{"wt":"прош"},"3":{"wt":"страд"}},"i":0}}]}'><a>страд. прич.</a> <a>прош. вр.</a></i><span> от </span><a rel="mw:WikiLink" href="./связать#связать_II" title="связать">связать II</a>; находящийся во <a rel="mw:WikiLink" href="./взаимосвязь" title="взаимосвязь">взаимосвязи</a> с кем-либо, чем-либо, <a rel="mw:WikiLink" href="./обусловленный" title="обусловленный">обусловленный</a> чем-либо</li></ol>
</section></section></section></body></html>""",
            [
                {
                    "form_of_only": True,
                    "form_of_targets": ["связать#связать_I", "связать#связать_II"],
                }
            ],
        )
