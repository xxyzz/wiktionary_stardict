from utils import XMLTestCase


class ItPOSTestCase(XMLTestCase):
    edition = "it"

    def test_h4_pos_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>run</title></head>
<body>
<section><h2 id="Inglese"><link rel="mw:PageProp/Category" data-mw='{"parts":[{"template":{"target":{"wt":"-en-"}}}]}'/><span data-mw='{}' typeof="mw:File"><a><img src="//upload.wikimedia.org/wikipedia/commons/thumb/8/83/Flag_of_the_United_Kingdom_%283-5%29.svg/40px-Flag_of_the_United_Kingdom_%283-5%29.svg.png"/></a></span><span> </span><a>Inglese</a></h2>
<section><h3 id="Verbo"><span typeof="mw:File"><a><img src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Open_book_01.svg/40px-Open_book_01.svg.png"/></a></span><i><a>Verbo</a></i></h3>
<section><h4 id="Transitivo"><a>Transitivo</a></h4>
<p><b>to</b> <b data-mw='{"parts":[{"template":{"target":{"wt":"Pn"}}}]}'>run</b><small></small> <small><i>(<a title="Appendice:Coniugazioni/Inglese/run" id="mwDw">vai alla coniugazione</a>)</i></small> <span>(</span><i><small>3ª persona sing. presente</small></i><span> </span><b><a>runs</a></b><span>, </span><i><small>participio presente</small></i><span> </span><b><a>running</a></b><span>, </span><i><small>passato semplice</small></i><span> </span><b><a >ran</a></b><span>, </span><i><small>participio passato</small></i><span> </span><b><a>run</a></b><span about="#mwt5">) </span></p>
<ol><li>amministrare, condurre (un'azienda)</li></ol></section>
<section><h4 id="Intransitivo"><a>Intransitivo</a></h4>
<p><b>run</b></p>
<ol><li>correre</li></ol>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="it">
<h4><i>Verbo</i></h4>
<h4>Transitivo</h4>
<p><b>to</b> <b>run</b> <span>(</span><i><small>3ª persona sing. presente</small></i><span> </span><b>runs</b><span>, </span><i><small>participio presente</small></i><span> </span><b>running</b><span>, </span><i><small>passato semplice</small></i><span> </span><b>ran</b><span>, </span><i><small>participio passato</small></i><span> </span><b>run</b><span>) </span></p>
<ol><li>amministrare, condurre (un'azienda)</li></ol>
</section>""",
                    "forms": ["run", "runs", "running", "ran"],
                    "ids": ["Inglese", "Verbo", "Transitivo"],
                    "lang": "Inglese",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="it">
<h4><i>Verbo</i></h4>
<h4>Intransitivo</h4>
<p><b>run</b></p>
<ol><li>correre</li></ol>
</section>""",
                    "forms": ["run"],
                    "ids": ["Inglese", "Verbo", "Intransitivo"],
                    "lang": "Inglese",
                },
            ],
        )

    def test_shortest_example(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>dog</title></head>
<body>
<section><h2><a>Inglese</a></h2>
<section><h3>Sostantivo, forma flessa</h3>
<p><b data-mw='{"parts":[{"template":{"target":{"wt":"Pn"}}}]}'>dog</b> <i>m sing</i></p>
<ol><li>mutazione per lenizione (t→d) di <a>tog</a><span> </span>; <a>cappello</a>.
<ul><li><i>Da <b>dog</b>, e <b>dog</b>.</i>
<dl><dd>Il tuo cappello, il suo cappello.</dd></dl></li>
<li><i>Daou <b>dog</b></i>
<dl><dd>Due cappelli.</dd></dl></li></ul></li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="it">
<h4>Sostantivo, forma flessa</h4>
<p><b>dog</b> <i>m sing</i></p>
<ol><li>mutazione per lenizione (t→d) di tog<span> </span>; cappello.
<ul><li><i>Daou <b>dog</b></i>
<dl><dd>Due cappelli.</dd></dl></li></ul></li></ol>
</section>""",
                    "form_of_only": True,
                    "form_of_targets": ["tog"],
                }
            ],
        )
