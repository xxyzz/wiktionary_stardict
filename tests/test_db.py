from unittest import TestCase

from wiktionary_stardict.db import create_indexes, init_db, insert_data, iter_entries


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
        for e_def, e_forms, *_ in iter_entries("Portuguese"):
            self.assertEqual(e_def, "maldizer def")
            self.assertCountEqual(
                e_forms, ["maldizer", "maldito", "malditos", "maldita", "malditas"]
            )

    def test_form_of_differen_forms(self):
        conn = init_db("English_1")
        insert_data(conn, "dyke def", ["dyke", "dykes", "dike"], False, [], [])
        insert_data(conn, "dike def", ["dike", "dikes"], True, ["dyke"], [])
        create_indexes(conn)
        entry_data = []
        for e_def, *_ in iter_entries("English_1"):
            entry_data.append(e_def)
        self.assertCountEqual(entry_data, ["dyke def", "dike def"])

    def test_form_of_target_not_exist(self):
        conn = init_db("English_2")
        insert_data(conn, "TACO def", ["TACO"], True, ["Trump always chickens out"], [])
        create_indexes(conn)
        for e_def, *_ in iter_entries("English_2"):
            self.assertEqual(e_def, "TACO def")
