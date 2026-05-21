from utils import XMLTestCase


class SvPOSTestCase(XMLTestCase):
    edition = "sv"

    def test_ordbok(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>ordbok</title></head>
<body>
<section><h2 id="Svenska">Svenska</h2>
<section><h3 id="Substantiv">Substantiv</h3>
<p id="mwBw"><b id="mwCA"><a>ord</a><a>bok</a></b></p>
<ol><li>bok med
<dl><dd><i>Slå upp det i en <b>ordbok</b>!</i></dd>
<dd><i>Den fransk-svenska <b>ordboken</b> var oundgänglig när jag läste franska.</i></dd>
<dd></dd><dd class="semantic-relation template-etymologi"><em title="Ordets ursprung">Etymologi:</em> Belagt i språket sedan 1690.<sup class="mw-ref reference"></sup></dd>
<dd class="semantic-relation template-jämför"><em title="Andra liknande begrepp">Jämför:</em> <a>encyklopedi</a></dd></dl></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="sv">
<h4>Substantiv</h4>
<p><b>ordbok</b></p>
<ol><li>bok med
<dl><dd><i>Slå upp det i en <b>ordbok</b>!</i></dd>
<dd class="semantic-relation template-etymologi"><em title="Ordets ursprung">Etymologi:</em> Belagt i språket sedan 1690.</dd>
</li></ol>
</section>""",
                    "forms": ["ordbok"],
                    "ids": ["Svenska", "Substantiv"],
                }
            ],
        )

    def test_ul_dl(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>vatten</title></head>
<body>
<section><h2>Svenska</h2>
<section><h3>Substantiv</h3>
<p><b>vatten</b></p>
<ul><li><b><a title="Wiktionary:Stilguide/Uttal">uttal</a>:</b><span> </span><span><span class="ipa">ˈvatː.ɛn</span></span></li></ul>
<ol><li>gloss</li></ol>
<dl><dd><span typeof="mw:Transclusion mw:File"><span title="Indragna rader ovanför strecket gäller en särskild definition. Eventuella rader närmast nedan kan gälla en eller flera av definitionerna ovan."><img src="//upload.wikimedia.org/wikipedia/commons/8/83/Hor_barileto_avgraensare_i_222_18_px_trans.png?utm_source=sv.wiktionary.org&amp;utm_campaign=parser&amp;utm_content=thumbnail_unscaled"/></span></span></dd>
<dd class="semantic-relation template-etymologi"><em title="Ordets ursprung">Etymologi:</em> Av fornsvenska</dd></dl>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="sv">
<h4>Substantiv</h4>
<p><b>vatten</b></p>
<ul><li><b>uttal: </b><span class="ipa">ˈvatː.ɛn</span></li></ul>
<ol><li>gloss</li></ol>
<dl><dd class="semantic-relation template-etymologi"><em title="Ordets ursprung">Etymologi:</em> Av fornsvenska</dd></dl>
</section>""",
                }
            ],
        )

    def test_form_of(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>boks</title></head>
<body>
<section><h2>Bokmål</h2>
<section><h3>Substantiv</h3>
<p><b>boks</b></p>
<ul><li><b><a title="Wiktionary:Stilguide/Uttal">uttal</a>:</b><span> </span><span><span class="ipa">ˈvatː.ɛn</span></span></li></ul>
<ol><li>box, låda, fack, bås</li>
<li>bjälke, bom, balk (av trä), fyrkantigt virke</li>
<li><i>böjningsform av</i><span> </span><a>bok</a><link rel="mw:PageProp/Category" href="./Kategori:Bokmål/Substantivformer#boks"/></li></ol>
</section>
<section><h3>Verb</h3>
<p><b>boks</b></p>
<ol><li><i>böjningsform av</i><span> </span><a>bokse</a><link rel="mw:PageProp/Category" href="./Kategori:Bokmål/Verbformer#boks"/></li></ol>
</section>
</section>
</body>
</html>""",
            [
                {
                    "form_of_only": False,
                    "form_of_targets": ["bok"],
                },
                {
                    "form_of_only": True,
                    "form_of_targets": ["bokse"],
                },
            ],
        )
