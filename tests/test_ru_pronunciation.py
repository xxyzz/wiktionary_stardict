from utils import XMLTestCase


class RuPronunciationTestCase(XMLTestCase):
    edition = "ru"

    def test_audio_table(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>book</title></head>
<body>
<section><h1>Английский</h1>
<section><h2><span>book I</span></h2>
<section><h3>Произношение</h3>
<ul style="margin-left:0; list-style:none;" class="transcription" about="#mwt9" typeof="mw:Transclusion"><li><a rel="mw:WikiLink/Interwiki" href="https://ru.wikipedia.org/wiki/Международный%20фонетический%20алфавит" title="w:Международный фонетический алфавит" class="extiw">МФА</a><span typeof="mw:Entity"> </span>(Великобритания): ед.<span> </span>ч.<span typeof="mw:Entity"> </span><span typeof="mw:Entity">[</span><span class="IPA" style="white-space: nowrap;">bʊk</span><span>]</span><span> </span><table class="audiotable"></table> мн.<span> </span>ч.<span> </span><span>[</span><span class="IPA" style="white-space: nowrap;">bʊks</span><span>]</span></li></ul>
</section>
<section><h3>Семантические свойства</h3>
<section><h4>Значение</h4>
<ol><li>gloss</li></ol>
</section></section></section></section>
</body></html>""",
            [
                {
                    "def": """<section dir="ltr" lang="ru">
<section><h4>Произношение</h4>
<ul style="margin-left:0; list-style:none;" class="transcription"><li>МФА<span> </span>(Великобритания): ед.<span> </span>ч.<span> </span><span>[</span><span class="IPA" style="white-space: nowrap;">bʊk</span><span>]</span><span> </span> мн.<span> </span>ч.<span> </span><span>[</span><span class="IPA" style="white-space: nowrap;">bʊks</span><span>]</span></li></ul>
</section>
<h4>Значение</h4>
<ol><li>gloss</li></ol>
</section>""",
                },
            ],
        )

    def test_ul_under_span(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>книга</title></head>
<body>
<section><h1>Русский</h1>
<section><h3>Произношение</h3>
<span class="rutr"><ul><li><a rel="mw:WikiLink" href="./Справка:МФА_для_русского_языка" title="Справка:МФА для русского языка">МФА</a>: ед.<span> </span>ч.<span> </span><span>[</span><span class="IPA" style="white-space: nowrap;">ˈknʲiɡə</span><span>]</span><span> </span><table class="audiotable"></table></li></ul></span>
</section>
<section><h3>Семантические свойства</h3>
<section><h4>Значение</h4>
<ol><li>gloss</li></ol>
</section></section></section>
</body></html>""",
            [
                {
                    "def": """<section dir="ltr" lang="ru">
<section><h4>Произношение</h4>
<ul><li>МФА: ед.<span> </span>ч.<span> </span><span>[</span><span class="IPA" style="white-space: nowrap;">ˈknʲiɡə</span><span>]</span><span> </span></li></ul>
</section>
<h4>Значение</h4>
<ol><li>gloss</li></ol>
</section>""",
                },
            ],
        )
