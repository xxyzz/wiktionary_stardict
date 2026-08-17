from utils import XMLTestCase


class ItFormsTestCase(XMLTestCase):
    edition = "it"

    def test_linkp(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>run</title></head>
<body>
<section><h2><a>Inglese</a></h2>
<section><h3>Sostantivo</h3>
<p><b data-mw='{"parts":[{"template":{"target":{"wt":"Pn"}}}]}'>run</b><small></small> <span data-mw='{"parts":[{"template":{"target":{"wt":"Linkp"},"params":{"1":{"wt":"runs"}}}}]}'>(</span><i>pl.</i><span>: </span><a>runs</a><span>)</span></p>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [{"forms": ["run", "runs"]}],
        )

    def test_zh_big(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>幼虫</title></head>
<body>
<section><h2><a>Cinese</a></h2>
<section><h3>Sostantivo</h3>
<div><div><big><big><b>幼虫</b><small></small></big></big> (<a>cinese semplificato</a>, variante tradizionale: <big><a>幼蟲</a></big>; <a>pinyin</a>: <b>yòuchóng</b>)<br/></div></div>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [{"forms": ["幼虫", "幼蟲"]}],
        )

    def test_tabs_table_template(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>cane</title></head>
<body>
<section><h2><a>Italiano</a></h2>
<section><h3>Sostantivo</h3>
<p><b data-mw='{"parts":[{"template":{"target":{"wt":"Pn"}}}]}'>cane</b></p>
<span data-mw='{"parts":[{"template":{"target":{"wt":"Tabs"},"params":{"1":{"wt":"cane"},"2":{"wt":"cani"},"3":{"wt":"cagna"},"4":{"wt":"cagne"}}}}]}'></span><table>
<tbody><tr align="center">
<th bgcolor="#FFFFE0"><span> </span><i><a>maschile</a></i><span> </span></th>
<td><span> </span> <a>cane</a><span> </span></td>
<td><span> </span> <a>cani</a><span> </span></td></tr>
</tbody></table>
<ol><li>gloss</li></ol>
</section></section></body></html>""",
            [{"forms": ["cane", "cani"]}],
        )

    def test_alt_form_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>comprare</title></head>
<body>
<section><h2><a>Italiano</a></h2>
<section><h3>Sostantivo</h3>
<section><h4>Transitivo</h4>
<p><b data-mw='{"parts":[{"template":{"target":{"wt":"Pn"}}}]}'>comprare</b></p>
<ol><li>gloss</li></ol>
</section></section>
<section><h3><span typeof="mw:File"><a><img/></a></span><span typeof="mw:File"><a><img/></a></span> <a>Varianti</a></h3>
<ul><li><a>comperare</a></li></ul>
</section></section></body></html>""",
            [
                {
                    "forms": ["comprare", "comperare"],
                    "def": """<section class="mw-parser-output" dir="ltr" lang="it">
<h4>Sostantivo</h4>
<h4>Transitivo</h4>
<p><b>comprare</b></p>
<ol><li>gloss</li></ol>
<section>
<h4> Varianti</h4>
<ul><li>comperare</li></ul>
</section></section>""",
                }
            ],
        )
