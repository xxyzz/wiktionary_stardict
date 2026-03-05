from utils import XMLTestCase


class EnPronunciationTestCase(XMLTestCase):
    def test_pos_list_in_pron_section(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>berserk</title></head>
<body>
<section><h2>English</h2>
<section><h3>Pronunciation</h3>
<ul><li><a>Noun</a>:
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent"><a title="w:Received Pronunciation" class="extiw">Received Pronunciation</a></span></span><span class="ib-brac qualifier-brac">)</span><span> </span><a title="Wiktionary:International Phonetic Alphabet">IPA</a><sup>(<a title="Appendix:English pronunciation">key</a>)</sup><span>:</span><span> </span><span class="IPA nowrap">/ˈbɜːsɜːk/</span></li>
</ul></li>
<li><a title="Appendix:Glossary">Adjective</a>:
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent"><a title="w:Received Pronunciation" class="extiw">Received Pronunciation</a></span></span><span class="ib-brac qualifier-brac">)</span><span> </span><a title="Wiktionary:International Phonetic Alphabet">IPA</a><sup>(<a title="Appendix:English pronunciation">key</a>)</sup><span>:</span><span> </span><span class="IPA nowrap">/bəˈzɜːk/</span></li></ul></li></ul></section>

<section><h3>Adjective</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">berserk</strong></span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                [
                    ["berserk"],
                    """<section>
      <h3>Pronunciation</h3>
      <ul>
        <li>
          <span class="ib-brac qualifier-brac">(</span>
          <span class="ib-content qualifier-content">
            <span class="usage-label-accent">Received Pronunciation</span>
          </span>
          <span class="ib-brac qualifier-brac">)</span>
          <span> </span>IPA<sup>(key)</sup><span>:</span><span> </span>
          <span class="IPA nowrap">/bəˈzɜːk/</span>
       </li>
      </ul>
    </section>
    <section>
      <h3>Adjective</h3>
      <p>
        <span class="headword-line">
          <strong class="Latn headword" lang="en">berserk</strong>
        </span>
      </p>
      <ol>
        <li>gloss</li>
      </ol>
    </section>""",
                    [],
                ]
            ],
        )
