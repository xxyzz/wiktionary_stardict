from unittest import TestCase

from wiktionary_stardict.score import get_score_svg


class ScoreTestCase(TestCase):
    maxDiff = None

    def test_score_svg(self):
        self.assertIn(
            "<path ",
            get_score_svg(
                "major scale",
                {
                    "name": "score",
                    "attrs": {},
                    "body": {"extsrc": "{c' d' e' f' g' a' b' c''}"},
                },
            ),
        )

    def test_raw_score(self):
        self.assertIn(
            "<path ",
            get_score_svg(
                "sensitive female chord progression",
                {
                    "name": "score",
                    "attrs": {"raw": "1", "sound": "1"},
                    "body": {
                        "extsrc": r"""\header { tagline = "" }
\score {
  \new Staff \with { \remove "Time_signature_engraver" }
  \repeat volta 2 {<c' e' a'>2 <c' f' a'> <c' e' g'> <b d' g'>}
  \layout { }
}
\score { % "unfold" this score copy so MIDI plays the repeated section twice
  \unfoldRepeats {
    \repeat volta 2 {<c' e' a'>2 <c' f' a'> <c' e' g'> <b d' g'>}
  }
  \midi { }
}"""
                    },
                },
            ),
        )

    def test_note_language(self):
        self.assertIn(
            "<path ",
            get_score_svg(
                "gamme mineure harmonique",
                {
                    "name": "score",
                    "attrs": {
                        "lang": "lilypond",
                        "note-language": "english",
                        "sound": "1",
                    },
                    "body": {
                        "extsrc": r"""{
\override Score.TimeSignature #'stencil = ##f
\relative c' {
  \clef treble \time 7/4
  a4 b c d e f gs a2 }
}"""
                    },
                },
            ),
        )
