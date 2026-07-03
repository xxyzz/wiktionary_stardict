from unittest import TestCase

from wiktionary_stardict.redirect import add_redirects


class RedirectTest(TestCase):
    maxDiff = None

    def setUp(self):
        import sqlite3

        self.conn = sqlite3.connect(":memory:")
        self.conn.executescript("""
        CREATE TABLE redirect (
        source   TEXT PRIMARY KEY,
        target   TEXT,
        fragment TEXT);
        CREATE INDEX target_idx ON redirect (target);""")

    def tearDown(self):
        self.conn.close()

    def test_add_redirect(self):
        self.conn.executemany(
            "INSERT INTO redirect VALUES(?, ?, ?)",
            [
                ("get that bag", "bag", "English:_money"),
                ("get the bag", "bag", "English:_money"),
            ],
        )
        page_data = [
            {"forms": ["bag"], "ids": ["English", "Noun", "English:_money"]},
            {"forms": ["bag"], "ids": ["English", "Verb"]},
        ]
        add_redirects(self.conn, "bag", page_data)
        self.assertEqual(page_data[0]["forms"], ["bag", "get that bag", "get the bag"])
        self.assertEqual(page_data[1]["forms"], ["bag"])
