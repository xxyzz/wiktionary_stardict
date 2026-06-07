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

    def test_form_of_same_forms(self):
        conn = init_db("Portuguese")
        insert_data(
            conn,
            "maldizer def",
            ["maldizer", "maldito", "malditos", "maldita", "malditas"],
            False,
            [],
            [],
        )
        insert_data(
            conn,
            "maldito def",
            ["maldito", "maldita", "malditos", "malditas"],
            True,
            ["maldizer"],
            [],
        )
        create_indexes(conn)
        for index, e_def, title, *_ in iter_entries(conn):
            self.assertEqual(index, 0)
            self.assertEqual(e_def, "maldizer def")
            self.assertEqual(title, "maldizer")
        forms = []
        for form_data in iter_forms(conn):
            forms.append(form_data)
        self.assertCountEqual(
            forms, [("maldito", 0), ("malditos", 0), ("maldita", 0), ("malditas", 0)]
        )
        conn.close()
        Path("build/Portuguese.db").unlink()

    def test_form_of_differen_forms(self):
        conn = init_db("English_1")
        insert_data(conn, "dyke def", ["dyke", "dykes", "dike"], False, [], [])
        insert_data(conn, "dike def", ["dike", "dikes"], True, ["dyke"], [])
        create_indexes(conn)
        entry_data = []
        for _, e_def, *_ in iter_entries(conn):
            entry_data.append(e_def)
        self.assertCountEqual(entry_data, ["dyke def", "dike def"])
        conn.close()
        Path("build/English_1.db").unlink()

    def test_form_of_target_not_exist(self):
        conn = init_db("English_2")
        insert_data(conn, "TACO def", ["TACO"], True, ["Trump always chickens out"], [])
        create_indexes(conn)
        for _, e_def, *_ in iter_entries(conn):
            self.assertEqual(e_def, "TACO def")
        conn.close()
        Path("build/English_2.db").unlink()
