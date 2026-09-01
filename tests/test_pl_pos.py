from utils import XMLTestCase


class PlPOSTestCase(XMLTestCase):
    edition = "pl"

    def test_pos_index_dot(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>book</title></head>
<body>
<section><h2 id="book_(język_angielski)">book (<span class="lang-code primary-lang-code lang-code-en" id="en"><a>język angielski</a></span>)</h2>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) <a>książka</a></dd>
<dd>(1.2) <a>księga</a></dd></dl>
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) <a>rezerwować</a></dd>
<dd>(2.2) rejestrować</dd>
<dd>(2.3) <span class="short-container"><span class="short-wrapper"><span class="short-content">księg.</span></span></span> księgować</dd></dl>
<p><i>czasownik nieprzechodni</i></p>
<dl><dd>(3.1) meldować się</dd></dl>
<dl><dt><span data-field="przyklady">przykłady<span>:</span></span></dt><dd></dd>
<dd>(1.1) <i>I've read this <a class="mw-selflink">book</a>.</i> → Przeczytałem tę <b>książkę</b>.</dd>
<dd>(1.1) <i>The more money donated, the more books purchased, and the more happy children.</i></dd>
<dd>(1.2) <i>The Book of Exodus is the second book of the Old Testament.</i></dd>
<dd>(2.1) <i>I will book a room for a night.</i></dd></dl>
</section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) książka</dd>
<dd>(1.2) księga</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(1.1) <i>I've read this <strong>book</strong>.</i> → Przeczytałem tę <b>książkę</b>.</dd>
<dd>(1.2) <i>The Book of Exodus is the second book of the Old Testament.</i></dd></dl>
</section>""",
                    "forms": ["book"],
                    "ids": ["book_(język_angielski)", "en"],
                    "lang": "język angielski",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) rezerwować</dd>
<dd>(2.2) rejestrować</dd>
<dd>(2.3) <span class="short-container"><span class="short-wrapper"><span class="short-content">księg.</span></span></span> księgować</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(2.1) <i>I will book a room for a night.</i></dd></dl>
</section>""",
                    "forms": ["book"],
                    "ids": ["book_(język_angielski)", "en"],
                    "lang": "język angielski",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik nieprzechodni</i></p>
<dl><dd>(3.1) meldować się</dd></dl>
</section>""",
                    "forms": ["book"],
                    "ids": ["book_(język_angielski)", "en"],
                    "lang": "język angielski",
                },
            ],
        )

    def test_pos_index_dot_hyphen(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>book</title></head>
<body>
<section><h2>book (<span class="lang-code primary-lang-code lang-code-en" id="en"><a>język angielski</a></span>)</h2>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) <a>książka</a></dd>
<dd>(1.2) <a>księga</a></dd></dl>
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) <a>rezerwować</a></dd>
<dd>(2.2) rejestrować</dd></dl>
<dl><dt><span data-field="przyklady">przykłady<span>:</span></span></dt><dd></dd>
<dd>(1.1-2) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd>
<dd>(1.1-2) <i>The more money donated, the more books purchased, and the more happy children.</i></dd></dl>
</section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) książka</dd>
<dd>(1.2) księga</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(1.1-2) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd></dl>
</section>""",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) rezerwować</dd>
<dd>(2.2) rejestrować</dd></dl>
</section>"""
                },
            ],
        )

    def test_pos_index_dot_comma(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>book</title></head>
<body>
<section><h2>book (<span class="lang-code primary-lang-code lang-code-en" id="en"><a>język angielski</a></span>)</h2>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) <a>książka</a></dd>
<dd>(1.2) <a>księga</a></dd></dl>
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) <a>rezerwować</a></dd>
<dd>(2.2) rejestrować</dd></dl>
<dl><dt><span data-field="przyklady">przykłady<span>:</span></span></dt><dd></dd>
<dd>(1.1,2) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd>
<dd>(1.1,2) <i>The more money donated, the more books purchased, and the more happy children.</i></dd></dl>
</section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) książka</dd>
<dd>(1.2) księga</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(1.1,2) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd></dl>
</section>""",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) rezerwować</dd>
<dd>(2.2) rejestrować</dd></dl>
</section>"""
                },
            ],
        )

    def test_pos_index_hyphen(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>book</title></head>
<body>
<section><h2>book (<span class="lang-code primary-lang-code lang-code-en" id="en"><a>język angielski</a></span>)</h2>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) <a>książka</a></dd>
<dd>(1.2) <a>księga</a></dd></dl>
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) <a>rezerwować</a></dd>
<dd>(2.2) rejestrować</dd></dl>
<p><i>czasownik nieprzechodni</i></p>
<dl><dd>(3.1) meldować się</dd></dl>
<dl><dt><span data-field="przyklady">przykłady<span>:</span></span></dt><dd></dd>
<dd>(1-3) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd>
<dd>(1-3) <i>The more money donated, the more books purchased, and the more happy children.</i></dd></dl>
</section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) książka</dd>
<dd>(1.2) księga</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(1-3) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd></dl>
</section>""",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) rezerwować</dd>
<dd>(2.2) rejestrować</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(1-3) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd></dl>
</section>""",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik nieprzechodni</i></p>
<dl><dd>(3.1) meldować się</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(1-3) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd></dl>
</section>""",
                },
            ],
        )

    def test_pos_index_comma(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>book</title></head>
<body>
<section><h2>book (<span class="lang-code primary-lang-code lang-code-en" id="en"><a>język angielski</a></span>)</h2>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) <a>książka</a></dd>
<dd>(1.2) <a>księga</a></dd></dl>
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) <a>rezerwować</a></dd>
<dd>(2.2) rejestrować</dd></dl>
<p><i>czasownik nieprzechodni</i></p>
<dl><dd>(3.1) meldować się</dd></dl>
<dl><dt><span data-field="przyklady">przykłady<span>:</span></span></dt><dd></dd>
<dd>(1,3) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd>
<dd>(1,3) <i>The more money donated, the more books purchased, and the more happy children.</i></dd></dl>
</section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) książka</dd>
<dd>(1.2) księga</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(1,3) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd></dl>
</section>""",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) rezerwować</dd>
<dd>(2.2) rejestrować</dd></dl>
</section>""",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik nieprzechodni</i></p>
<dl><dd>(3.1) meldować się</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(1,3) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd></dl>
</section>""",
                },
            ],
        )

    def test_pos_index_dot_comma_dot(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>book</title></head>
<body>
<section><h2>book (<span class="lang-code primary-lang-code lang-code-en" id="en"><a>język angielski</a></span>)</h2>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) <a>książka</a></dd>
<dd>(1.2) <a>księga</a></dd></dl>
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) <a>rezerwować</a></dd>
<dd>(2.2) rejestrować</dd></dl>
<p><i>czasownik nieprzechodni</i></p>
<dl><dd>(3.1) meldować się</dd></dl>
<dl><dt><span data-field="przyklady">przykłady<span>:</span></span></dt><dd></dd>
<dd>(1.1, 2.2) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd>
<dd>(1.1, 2.2) <i>The more money donated, the more books purchased, and the more happy children.</i></dd></dl>
</section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) książka</dd>
<dd>(1.2) księga</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(1.1, 2.2) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd></dl>
</section>""",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) rezerwować</dd>
<dd>(2.2) rejestrować</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(1.1, 2.2) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd></dl>
</section>""",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik nieprzechodni</i></p>
<dl><dd>(3.1) meldować się</dd></dl>
</section>""",
                },
            ],
        )

    def test_pos_index_hyhen_comma_dot(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>book</title></head>
<body>
<section><h2>book (<span class="lang-code primary-lang-code lang-code-en" id="en"><a>język angielski</a></span>)</h2>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) <a>książka</a></dd>
<dd>(1.2) <a>księga</a></dd></dl>
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) <a>rezerwować</a></dd>
<dd>(2.2) rejestrować</dd></dl>
<p><i>czasownik nieprzechodni</i></p>
<dl><dd>(3.1) meldować się</dd></dl>
<dl><dt><span data-field="przyklady">przykłady<span>:</span></span></dt><dd></dd>
<dd>(1-2, 3.1) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd>
<dd>(1-2, 3.1) <i>The more money donated, the more books purchased, and the more happy children.</i></dd></dl>
</section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>rzeczownik policzalny</i></p>
<dl><dd>(1.1) książka</dd>
<dd>(1.2) księga</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(1-2, 3.1) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd></dl>
</section>""",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik przechodni</i></p>
<dl><dd>(2.1) rezerwować</dd>
<dd>(2.2) rejestrować</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(1-2, 3.1) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd></dl>
</section>""",
                },
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pl">
<p><i>czasownik nieprzechodni</i></p>
<dl><dd>(3.1) meldować się</dd></dl>
<dl><dt><span>przykłady<span>:</span></span></dt>
<dd>(1-2, 3.1) <i>I've read this book.</i> → Przeczytałem tę <b>książkę</b>.</dd></dl>
</section>""",
                },
            ],
        )

    def test_form_of(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>gorzej</title></head>
<body>
<section><h2>gorzej (<span class="lang-code primary-lang-code"><a>język polski</a></span>)</h2>
<dl><dt><span data-field="znaczenia">znaczenia<span>:</span></span></dt><dd></dd></dl>
<p><i>przysłówek, forma fleksyjna</i></p>
<dl><dd>(1.1) <i>stopień wyższy przysłówka</i> <a>źle</a></dd></dl>
</section></body></html>""",
            [{"form_of_only": True, "form_of_targets": ["źle"]}],
        )
