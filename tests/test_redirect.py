import sqlite3
from unittest import TestCase

from wiktionary_stardict.db import (
    init_db,
    insert_data,
    iter_entries,
    iter_forms,
)
from wiktionary_stardict.redirect import add_redirects


class RedirectTest(TestCase):
    maxDiff = None

    def setUp(self):
        import random
        import string
        from pathlib import Path

        db_name = "".join(random.choices(string.ascii_letters, k=20))
        self.rdb_path = Path(f"build/{db_name}_redirect.db")
        with sqlite3.connect(self.rdb_path) as conn:
            conn.executescript("""
            CREATE TABLE redirect (
            source   TEXT PRIMARY KEY,
            target   TEXT,
            fragment TEXT);
            CREATE INDEX target_idx ON redirect (target);""")
        self.db_path = Path(f"build/{db_name}.db")
        self.conn = init_db(db_name)

    def tearDown(self):
        self.conn.close()
        self.db_path.unlink()
        self.rdb_path.unlink()

    def test_add_redirect(self):
        with sqlite3.connect(self.rdb_path) as r_conn:
            r_conn.executemany(
                "INSERT INTO redirect VALUES(?, ?, ?)",
                [
                    ("get that bag", "bag", "English:_money"),
                    ("get the bag", "bag", "English:_money"),
                    ("no match id", "bag", "id"),
                    ("no id", "bag", ""),
                ],
            )
        insert_data(
            self.conn,
            "bag",
            "bag noun",
            ["bag"],
            ids=["English", "Noun", "English:_money"],
        )
        insert_data(self.conn, "bag", "bag verb", ["bag"], ids=["English", "Verb"])
        list(iter_entries(self.conn))
        add_redirects(self.conn, self.rdb_path)
        self.assertEqual(
            list(iter_forms(self.conn)),
            [
                ("get that bag", 0),
                ("get the bag", 0),
                ("no id", 0),
                ("no id", 1),
                ("no match id", 0),
                ("no match id", 1),
            ],
        )
