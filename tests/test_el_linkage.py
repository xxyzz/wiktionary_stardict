from utils import XMLTestCase


class ElLinkageTestCase(XMLTestCase):
    edition = "el"

    def test_syn_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>συντομογραφία</title></head>
<body>
<section><h2><span>Νέα ελληνικά (el)</span></h2>
<section><h3><span class="partofspeech">Ουσιαστικό</span></h3>
<p><b>συντομογραφία</b></p>
<ul><li>gloss</li></ul>
<section><h4>Συνώνυμα</h4>
<ul><li><a>βραχυγραφία</a></li></ul>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="el">
<h4><span class="partofspeech">Ουσιαστικό</span></h4>
<p><b>συντομογραφία</b></p>
<ul><li>gloss</li></ul>
<section><h4>Συνώνυμα</h4>
<ul><li>βραχυγραφία</li></ul>
</section></section>"""
                }
            ],
        )
