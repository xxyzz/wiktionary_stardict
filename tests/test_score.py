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
                }
            ),
        )
