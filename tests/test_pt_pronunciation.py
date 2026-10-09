from utils import XMLTestCase


class PtPronTestCase(XMLTestCase):
    edition = "pt"

    def test_direct_list_child(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>brasilianista</title></head>
<body>
<section><h1>Português</h1>
<section><h2>Adjetivo</h2>
<p><b>brasilianista</b></p>
<ol><li>gloss</li></ol>
</section>
<section><h2>Pronúncia</h2>
<ul><li><a title="AFI">AFI</a>: <span class="ipa">/bɾa.zi.li.ã.'nis.tə/</span></li>
<li><a title="SAMPA">SAMPA</a>: /bra.zi.lj6."nis.ta/</li></ul>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pt">
<h4>Adjetivo</h4>
<p><b>brasilianista</b></p>
<ol><li>gloss</li></ol>
<section><h4>Pronúncia</h4>
<ul><li>AFI: <span class="ipa">/bɾa.zi.li.ã.'nis.tə/</span></li>
<li>SAMPA: /bra.zi.lj6."nis.ta/</li></ul>
</section></section>"""
                }
            ],
        )

    def test_child_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>tupi</title></head>
<body>
<section><h1>Português</h1>
<section><h2>Adjetivo</h2>
<p><b>tupi</b></p>
<ol><li>gloss</li></ol>
</section>
<section><h2>Pronúncia</h2>
<section><h3>Brasil</h3>
<ul><li><span> </span><a title="AFI">AFI</a><span>: </span><span>/tuˈpi/</span><span>  </span></li></ul>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pt">
<h4>Adjetivo</h4>
<p><b>tupi</b></p>
<ol><li>gloss</li></ol>
<section><h4>Pronúncia</h4>
<section><h5>Brasil</h5>
<ul><li><span> </span>AFI<span>: </span><span>/tuˈpi/</span><span>  </span></li></ul>
</section></section></section>"""
                }
            ],
        )

    def test_remove_audio_file(self):
        self.assertTransformEqual(
            r"""<!DOCTYPE html>
<html>
<head><title>dictionary</title></head>
<body>
<section><h1>Inglês</h1>
<section><h2>Substantivo</h2>
<p><b>dic.tion.a.ry</b></p>
<ol><li>gloss</li></ol>
</section>
<section><h2>Pronúncia</h2>
<section><h3>Estados Unidos</h3>
<ul><li>AFI: /ˈdɪk.ʃən.<i>ɛ</i>.ɹɪ/ <span typeof="mw:Transclusion mw:File"><a href="./Ficheiro:En-us-dictionary.ogg" title="Ficheiro:En-us-dictionary.ogg"><img resource="./Ficheiro:Loudspeaker.svg" src="//thumb.wikimedia.org/wikipedia/commons/thumb/8/8a/Loudspeaker.svg/20px-Loudspeaker.svg.png"/></a></span><span> </span><a rel="mw:MediaLink">ouvir</a><span> </span><sup><a rel="mw:WikiLink" href="./Ficheiro:En-us-dictionary.ogg" title="Ficheiro:En-us-dictionary.ogg">fonte</a> <a>?</a></sup><span> </span><span typeof="mw:File"><span title="noicon"><audio></audio></span></span></li>
<li>X-SAMPA: /"dIk.S@n.<i>E</i>.r\I/</li></ul>
</section></section></section></body></html>""",
            [
                {
                    "def": r"""<section class="mw-parser-output" dir="ltr" lang="pt">
<h4>Substantivo</h4>
<p><b>dic.tion.a.ry</b></p>
<ol><li>gloss</li></ol>
<section><h4>Pronúncia</h4>
<section><h5>Estados Unidos</h5>
<ul><li>AFI: /ˈdɪk.ʃən.<i>ɛ</i>.ɹɪ/ <span> </span><span> </span><span> </span></li>
<li>X-SAMPA: /"dIk.S@n.<i>E</i>.r\I/</li></ul>
</section></section></section>"""
                }
            ],
        )

    def test_nested_ipa_lists(self):
        self.assertTransformEqual(
            r"""<!DOCTYPE html>
<html>
<head><title>pelúcia</title></head>
<body>
<section><h1>Português</h1>
<section><h2>Substantivo</h2>
<p><b>pelúcia</b></p>
<ol><li>gloss</li></ol>
</section>
<section><h2>Pronúncia</h2>
<section><h3>Brasil</h3>
<ul><li><a title="AFI">AFI</a>: <a title="Ajuda:Guia de pronúncia"><span class="ipa">/pe.ˈlu.sjə/</span></a></li>
<li><a title="X-SAMPA">X-SAMPA</a>: /pe."lu.sj@/
<ul><li>AFI: /pe.'lu.sja/ <span>(</span><span class="escopo">Região Sul</span><span>)</span></li>
<li>X-SAMPA: /pe."lu.sja/ <span>(</span><span class="escopo">Região Sul</span><span>)</span></li></ul></li></ul>
</section></section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="pt">
<h4>Substantivo</h4>
<p><b>pelúcia</b></p>
<ol><li>gloss</li></ol>
<section><h4>Pronúncia</h4>
<section><h5>Brasil</h5>
<ul><li>AFI: <span class="ipa">/pe.ˈlu.sjə/</span></li>
<li>X-SAMPA: /pe."lu.sj@/
<ul><li>AFI: /pe.'lu.sja/ <span>(</span><span class="escopo">Região Sul</span><span>)</span></li>
<li>X-SAMPA: /pe."lu.sja/ <span>(</span><span class="escopo">Região Sul</span><span>)</span></li></ul></li></ul>
</section></section></section>"""
                }
            ],
        )
