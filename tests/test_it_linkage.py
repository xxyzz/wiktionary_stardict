from utils import XMLTestCase


class ItLinkageTestCase(XMLTestCase):
    edition = "it"

    def test_linkage_list(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>cane</title></head>
<body>
<section><h2><a>Italiano</a></h2>
<section><h3>Sostantivo</h3>
<p><b>cane</b></p>
<ol><li>gloss</li></ol>
</section>
<section><h3>Sinonimi</h3>
<ul><li>list 1</li><li>list 2</li><li>list 3</li><li>list 4</li><li>list 5</li>
<li>list 6</li><li>list 7</li></ul>
</section>
<section><h3>Contrari</h3>
<ul><li>list 1</li></ul>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="it">
<h4>Sostantivo</h4>
<p><b>cane</b></p>
<ol><li>gloss</li></ol>
<section><h4>Sinonimi</h4>
<ul><li>list 1</li><li>list 2</li><li>list 3</li><li>list 4</li><li>list 5</li>
<li>list 6</li></ul>
</section>
<section><h4>Contrari</h4>
<ul><li>list 1</li></ul>
</section></section>""",
                }
            ],
        )
