from utils import XMLTestCase


class RuLinkageTestCase(XMLTestCase):
    edition = "ru"

    def test_child_ol_lists(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>книга</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Семантические свойства</h3>
<section><h4>Значение</h4>
<ol><li>gloss</li></ol>
</section>
<section><h4>Синонимы</h4>
<ol><li>том</li>
<li>книжка</li>
<li>—</li>
<li>—</li></ol>
</section>
<section><h4>Антонимы</h4>
<ol><li>—</li>
<li>—</li>
<li>—</li>
<li>—</li></ol>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ru">
<h4>Значение</h4>
<ol><li>gloss</li></ol>
<section><h4>Синонимы</h4>
<ol><li>том</li>
<li>книжка</li>
<li>—</li>
<li>—</li></ol>
</section></section>""",
                },
            ],
        )

    def test_ref_list(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>красный</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Семантические свойства</h3>
<section><h4>Значение</h4>
<ol><li>gloss</li></ol>
<h4>Синонимы</h4>
<div class="mw-references-wrap">
<ol class="mw-references references"><li><span class="mw-cite-backlink"><span class="mw-linkback-text">↑</span></span> <span class="mw-reference-text reference-text">алый, червонный, червлёный</span></li></ol></div>
<h4> Антонимы </h4>
<div class="mw-references-wrap">
<ol class="mw-references references"><li><span class="mw-cite-backlink"><span class="mw-linkback-text">↑</span></span> <span class="mw-reference-text reference-text"><span> </span>—<span> </span></span></li></ol></div>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="ru">
<h4>Значение</h4>
<ol><li>gloss</li></ol>
<section><h4>Синонимы</h4>
<ol class="mw-references references"><li> <span class="mw-reference-text reference-text">алый, червонный, червлёный</span></li></ol>
</section></section>""",
                },
            ],
        )
