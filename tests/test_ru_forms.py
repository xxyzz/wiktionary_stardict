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
                    "def": """<section dir="ltr" lang="ru">
<section><h4>Тип и синтаксические свойства сочетания</h4>
<p><b>Кра́с<span class="hyph" style="color:lightgreen;">-</span>на<span class="hyph-dot" style="color:red;">·</span>я Ша́<span class="hyph" style="color:lightgreen;">-</span>поч<span class="hyph" style="color:lightgreen;">-</span>ка</b></p>
<p><span>Корень: </span><b>-хорош-</b></p>
</section>
<h4>Значение</h4>
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
                    "def": """<section dir="ltr" lang="ru">
<section><h4>Тип и синтаксические свойства сочетания</h4>
<p><b>бе<span class="hyph" style="color:lightgreen;">-</span>жа́ть</b><span> </span>(<span title="написание в дореформенной орфографии" style="border-bottom: 1px dotted; cursor: help">дореформ.</span> <span style="font-family:'Palatino Linotype'">бѣжа́ть</span>)</p>
</section>
<h4>Значение</h4>
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
