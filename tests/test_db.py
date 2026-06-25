from pathlib import Path
from unittest import TestCase

from wiktionary_stardict.db import (
    create_indexes,
    init_db,
    insert_data,
    iter_entries,
    iter_forms,
)


class DBTest(TestCase):
    maxDiff = None

    def setUp(self):
        import random
        import string

        db_name = "".join(random.choices(string.ascii_letters, k=20))
        self.db_path = Path(f"build/{db_name}.db")
        self.conn = init_db(db_name)

    def tearDown(self):
        self.conn.close()
        self.db_path.unlink()

    def get_titles(self):
        return [title for _, title, *_ in iter_entries(self.conn)]

    def test_form_of_same_forms(self):
        insert_data(
            self.conn,
            "maldizer def",
            ["maldizer", "maldito", "malditos", "maldita", "malditas"],
            False,
            [],
            [],
        )
        insert_data(
            self.conn,
            "maldito def",
            ["maldito", "maldita", "malditos", "malditas"],
            True,
            ["maldizer"],
            [],
        )
        create_indexes(self.conn)
        self.assertEqual(self.get_titles(), ["maldizer"])
        self.assertEqual(
            list(iter_forms(self.conn)),
            [("maldita", 0), ("malditas", 0), ("maldito", 0), ("malditos", 0)],
        )

    def test_form_of_differen_forms(self):
        insert_data(self.conn, "dyke def", ["dyke", "dykes", "dike"], False, [], [])
        insert_data(self.conn, "dike def", ["dike", "dikes"], True, ["dyke"], [])
        create_indexes(self.conn)
        self.assertEqual(self.get_titles(), ["dyke"])
        self.assertEqual(
            list(iter_forms(self.conn)), [("dike", 0), ("dikes", 0), ("dykes", 0)]
        )

    def test_form_of_target_not_exist(self):
        insert_data(
            self.conn, "TACO def", ["TACO"], True, ["Trump always chickens out"], []
        )
        create_indexes(self.conn)
        self.assertEqual(self.get_titles(), ["TACO"])

    def test_word_sort_order(self):
        insert_data(self.conn, "Book", ["Book", "Books"], False, [], [])
        insert_data(
            self.conn, "book", ["book", "books", "booking", "booked"], False, [], []
        )
        insert_data(self.conn, "apple", ["apple", "apples"], False, [], [])
        self.assertEqual(self.get_titles(), ["apple", "Book", "book"])
        self.assertEqual(
            list(iter_forms(self.conn)),
            [("apples", 0), ("booked", 2), ("booking", 2), ("Books", 1), ("books", 2)],
        )

    def test_title_not_in_target_forms(self):
        insert_data(
            self.conn, "flying colors", ["flying colors"], True, ["flying colours"], []
        )
        insert_data(self.conn, "flying colours", ["flying colours"], False, [], [])
        self.assertEqual(self.get_titles(), ["flying colours"])
        self.assertEqual(list(iter_forms(self.conn)), [("flying colors", 0)])
