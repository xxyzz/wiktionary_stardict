from utils import XMLTestCase


class FrLinkageTestCase(XMLTestCase):
    edition = "fr"

    def test_lists(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>autrice</title></head>
<body>
<section><h2>Français</h2>
<section><h3>Nom commun</h3>
<p><b>autrice</b></p>
<ol><li>gloss</li></ol>
<section><h4>Synonymes</h4>
<div class="boite">
<div class="NavFrame">
<div class="NavHead"><span class="nav-head-title"><b>Celle qui est à l’origine de quelque chose</b></span><span> </span><span class="nav-head-number">(1)</span></div>
<div class="NavContent">
<div style="column-width:  26em; -webkit-column-width: 26em; -moz-column-width:  26em;  vertical-align: top; text-align: left;">
<ul><li>artisane</li>
<li>conceptrice</li>
<li>constructrice</li>
<li>créatrice</li>
<li>faiseuse</li>
<li>fondatrice</li>
<li>formulatrice</li></ul>
</div></div><div style="clear:both"></div></div></div>
</section>
<section><h4>Quasi-synonymes</h4>
<ul><li>auteur</li></ul>
</section>
</section>
</section>
</body>
</html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="fr">
<h4>Nom commun</h4>
<p><b>autrice</b></p>
<ol><li>gloss</li></ol>
<section><h4>Synonymes</h4>
<div class="boite">
<div class="NavFrame">
<div class="NavHead"><span class="nav-head-title"><b>Celle qui est à l’origine de quelque chose</b></span><span> </span><span class="nav-head-number">(1)</span></div>
<div class="NavContent">
<div style="column-width:  26em; -webkit-column-width: 26em; -moz-column-width:  26em;  vertical-align: top; text-align: left;">
<ul><li>artisane</li>
<li>conceptrice</li>
<li>constructrice</li>
<li>créatrice</li>
<li>faiseuse</li>
<li>fondatrice</li></ul>
</div></div><div style="clear:both"></div></div></div>
</section>
<section><h4>Quasi-synonymes</h4>
<ul><li>auteur</li></ul>
</section>
</section>""",
                },
            ],
        )
