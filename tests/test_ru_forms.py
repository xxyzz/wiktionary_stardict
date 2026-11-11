from utils import XMLTestCase


class RuFormsTestCase(XMLTestCase):
    edition = "ru"

    def test_stress_form(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>Красная Шапочка</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Тип и синтаксические свойства сочетания</h3>
<p><b><a>Кра́с<span class="hyph" style="color:lightgreen;">-</span>на<span class="hyph-dot" style="color:red;">·</span>я</a> <a>Ша́<span class="hyph" style="color:lightgreen;">-</span>поч<span class="hyph" style="color:lightgreen;">-</span>ка</a></b></p>
<p><span>Корень: </span><b>-хорош-</b></p>
</section>
<section><h3>Семантические свойства</h3>
<section><h4><span></span>Значение</h4>
<ol><li>gloss</li></ol>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section dir="ltr" lang="ru" class="mw-parser-output">
<section><h4>Тип и синтаксические свойства сочетания</h4>
<p><b>Кра́с<span class="hyph" style="color:lightgreen;">-</span>на<span class="hyph-dot" style="color:red;">·</span>я Ша́<span class="hyph" style="color:lightgreen;">-</span>поч<span class="hyph" style="color:lightgreen;">-</span>ка</b></p>
<p><span>Корень: </span><b>-хорош-</b></p>
</section>
<h4><span></span>Значение</h4>
<ol><li>gloss</li></ol>
</section>""",
                    "forms": ["Красная Шапочка", "Кра́сная Ша́почка"],
                },
            ],
        )

    def test_double_slash(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>собака</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Морфологические и синтаксические свойства</h3>
<table class="morfotable ru" cellpadding="3" rules="all" about="#mwt12">
<tbody><tr><th><a>падеж</a></th>
<th>ед.<span> </span>ч.</th>
<th>мн.<span> </span>ч.</th></tr>
<tr><th><a>В.</a></th>
<td>соба́ку</td>
<td>соба́к<span> </span>//<br/>соба́ки</td></tr>
</tbody>
</table>
<p><b>со<span class="hyph" style="color:lightgreen;">-</span>ба́<span class="hyph" style="color:lightgreen;">-</span>ка</b></p>
</section>
<section><h3>Семантические свойства</h3>
<section><h4><span></span>Значение</h4>
<ol><li>gloss</li></ol>
</section>
</section>
</section>
</body>
</html>""",
            [{"forms": ["собака", "соба́ка", "соба́ку", "соба́к", "соба́ки"]}],
        )

    def test_a_link_form(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>бежать</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Морфологические и синтаксические свойства</h3>
<table class="morfotable ru" cellpadding="2" rules="all">
<tbody><tr>
<th colspan="3">Настоящее/будущее время</th>
</tr><tr>
<th></th>
<th align="center">ед. число</th>
<th align="center">мн. число</th>
</tr>
<tr>
<th>1-е лицо</th>
<td>бегу́</td>
</tr>
<tr>
<th colspan="3">Деепричастия</th>
</tr>
<tr>
<th align="right">прош. вр.</th>
<td colspan="2"><a rel="mw:WikiLink" href="./бежав#бежа́в" title="бежав">бежа́в</a>, <a rel="mw:WikiLink" href="./бежавши#бежа́вши" title="бежавши">бежа́вши</a></td>
</tr>
</tbody></table>
<p><b>бе<span class="hyph" style="color:lightgreen;">-</span>жа́ть</b><span> </span>(<span title="написание в дореформенной орфографии" style="border-bottom: 1px dotted; cursor: help">дореформ.</span> <span style="font-family:'Palatino Linotype'">бѣжа́ть</span>)</p>
</section>
<section><h3>Семантические свойства</h3>
<section><h4><span></span>Значение</h4>
<p>(Во всех значениях, кроме указанных особо, глагол <span class="label mark" title="несовершенный вид">несов.</span> вида и <span class="label mark" title="непереходный глагол">неперех.</span>)</p>
<ol><li>gloss</li></ol>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ru">
<section><h4>Морфологические и синтаксические свойства</h4>
<p><b>бе<span class="hyph" style="color:lightgreen;">-</span>жа́ть</b><span> </span>(<span title="написание в дореформенной орфографии" style="border-bottom: 1px dotted; cursor: help">дореформ.</span> <span style="font-family:'Palatino Linotype'">бѣжа́ть</span>)</p>
</section>
<h4><span></span>Значение</h4>
<p>(Во всех значениях, кроме указанных особо, глагол <span class="label mark" title="несовершенный вид">несов.</span> вида и <span class="label mark" title="непереходный глагол">неперех.</span>)</p>
<ol><li>gloss</li></ol>
</section>""",
                    "forms": [
                        "бежать",
                        "бежа́ть",
                        "бегу́",
                        "бежа́в",
                        "бежа́вши",
                        "бежав",
                        "бежавши",
                    ],
                }
            ],
        )

    def test_comparative_forms_tag(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>здоровый</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Морфологические и синтаксические свойства</h3>
<p><a>Прилагательное</a>, <a>качественное</a>, тип склонения по <a>классификации А.<span> </span>Зализняка</a><span> </span>— 1a.<span> </span>Сравнительная степень<span> </span>— <i><a title="здоровее">здорове́е</a><sup><abbr title="нерегулярная форма">△</abbr></sup>, <a><span class="label mark" title="устаревшее">устар.</span></a>: <a title="здоровее">здоро́вее</a></i>.</p>
</section>
<section><h3>Семантические свойства</h3>
<section><h4><span></span>Значение</h4>
<ol><li>gloss</li></ol>
</section></section></section></body></html>""",
            [{"forms": ["здоровый", "здорове́е", "здоровее", "здоро́вее"]}],
        )

    def test_comparative_forms_multiple_i(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>дешёвый</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Морфологические и синтаксические свойства</h3>
<p><a>Прилагательное</a>, <a>качественное</a>, тип склонения по <a>классификации А.<span> </span>Зализняка</a><span> </span>— 1a/c-ё.<span> </span>Сравнительная степень<span> </span>— <i><a title="дешевле">деше́вле</a> </i>и<i> <a title="подешевле">подеше́вле</a> </i>(в значении цены)<i>, <a title="дешевее" class="new">дешеве́е</a> </i>(в перен. знач.)<i>.</i></p>
</section>
<section><h3>Семантические свойства</h3>
<section><h4><span></span>Значение</h4>
<ol><li>gloss</li></ol>
</section></section></section></body></html>""",
            [
                {
                    "forms": [
                        "дешёвый",
                        "деше́вле",
                        "дешевле",
                        "подеше́вле",
                        "подешевле",
                        "дешеве́е",
                        "дешевее",
                    ]
                }
            ],
        )

    def test_comparative_forms_более(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>мудной</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Морфологические и синтаксические свойства</h3>
<p><a>Прилагательное</a>, <a>качественное</a>, тип склонения по <a>классификации А.<span> </span>Зализняка</a><span> </span>— 1b.<span> </span>Сравнительная степень<span> </span>— <i><a title="муднее">муднее</a>, <a title="более">более</a> <a class="mw-selflink-fragment">мудной</a></i>.</p>
</section>
<section><h3>Семантические свойства</h3>
<section><h4><span></span>Значение</h4>
<ol><li>gloss</li></ol>
</section></section></section></body></html>""",
            [{"forms": ["мудной", "муднее"]}],
        )

    def test_superlative_forms_a(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>новый</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Морфологические и синтаксические свойства</h3>
<p><a>Прилагательное</a>, <a>качественное</a>, тип склонения по <a>классификации А.<span> </span>Зализняка</a><span> </span>— 1a/c'.<span> </span>Сравнительная степень<span> </span>— <i><a title="новее">нове́е</a></i>.
Превосходная степень — <a title="новейший">новейший</a>, <a title="наиновейший">наиновейший</a>.</p>
</section>
<section><h3>Семантические свойства</h3>
<section><h4><span></span>Значение</h4>
<ol><li>gloss</li></ol>
</section></section></section></body></html>""",
            [{"forms": ["новый", "нове́е", "новее", "новейший", "наиновейший"]}],
        )

    def test_superlative_forms_i(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>сладкий</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Морфологические и синтаксические свойства</h3>
<p>Превосходная степень — <i><a title="сладчайший">сладча́йший</a></i>.</p>
</section>
<section><h3>Семантические свойства</h3>
<section><h4><span></span>Значение</h4>
<ol><li>gloss</li></ol>
</section></section></section></body></html>""",
            [{"forms": ["сладкий", "сладча́йший", "сладчайший"]}],
        )
