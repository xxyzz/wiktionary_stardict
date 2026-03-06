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
      <h4>Adjective</h4>
      <ul>
        <li>
          <span class="ib-brac qualifier-brac">(</span>
          <span class="ib-content qualifier-content">
            <span class="usage-label-accent">Received Pronunciation</span>
          </span>
          <span class="ib-brac qualifier-brac">)</span>
          <span> </span>IPA<span>:</span><span> </span>
          <span class="IPA nowrap">/bəˈzɜːk/</span>
       </li>
      </ul>
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

    def test_remove_audio_file_table(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>languid</title></head>
<body>
<section><h2>English</h2>
<section><h3>Pronunciation</h3>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">Received Pronunciation<span class="ib-comma label-comma">,</span><span> </span>General American<span class="ib-comma label-comma">,</span><span> </span>weak vowel distinction</span></span><span class="ib-brac qualifier-brac">)</span><span> </span><a title="Wiktionary:International Phonetic Alphabet">IPA</a><sup>(<a title="Appendix:English pronunciation">key</a>)</sup><span>:</span><span> </span><span class="IPA nowrap">/ˈlæŋɡwɪd/</span>
<ul><li><style data-mw-deduplicate="TemplateStyles:r50165410">.mw-parser-output .k-player .k-attribution{visibility:hidden}</style><table class="audiotable"></table>
<ul><li><span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">US<span class="ib-comma label-comma">,</span><span> </span>Canada<span class="ib-comma label-comma">,</span><span> </span>weak vowel distinction</span></span><span class="ib-brac qualifier-brac">)</span><span> </span><a title="Wiktionary:International Phonetic Alphabet">IPA</a><sup>(<a>key</a>)</sup><span>:</span><span> </span><span class="IPA nowrap">/ˈleɪ̯ŋɡwɪd/</span><span>, </span><span class="IPA nowrap">/ˈlɛ̃ŋɡwɪd/</span></li></ul></li></ul></li></ul>
</section>
<section><h3>Adjective</h3>
<p><span class="headword-line"><strong class="Latn headword" lang="en">languid</strong></span></p>
<ol><li>gloss</li></ol>
</section>
</section>
</body>
</html>""",
            [
                [
                    ["languid"],
                    """<section>
      <h4>Adjective</h4>
      <ul>
        <li>
          <span class="ib-brac qualifier-brac">(</span><span class="ib-content qualifier-content"><span class="usage-label-accent">Received Pronunciation<span class="ib-comma label-comma">,</span><span> </span>General American<span class="ib-comma label-comma">,</span><span> </span>weak vowel distinction</span></span><span class="ib-brac qualifier-brac">)</span><span> </span>IPA<span>:</span><span> </span><span class="IPA nowrap">/ˈlæŋɡwɪd/</span>
       </li>
      </ul>
      <p>
        <span class="headword-line">
          <strong class="Latn headword" lang="en">languid</strong>
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
