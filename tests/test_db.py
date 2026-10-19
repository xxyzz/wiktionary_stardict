from collections import defaultdict
from pathlib import Path
from unittest import TestCase

from wiktionary_stardict.db import (
    FORMS_LIMIT,
    combine_links,
    create_indexes,
    delete_problematic_forms,
    init_db,
    insert_data,
    insert_fragment_forms,
    iter_entries,
    iter_forms,
    update_index_num,
)


class DBTest(TestCase):
    maxDiff = None

    def setUp(self):
        import random
        import string

        db_name = "".join(random.choices(string.ascii_letters, k=20))
        self.db_path = Path(f"build/{db_name}.db")
        self.conn = init_db(db_name)
        self.all_links_path = Path(f"build/{db_name}_links.db")

    def tearDown(self):
        self.conn.close()
        self.db_path.unlink()
        self.all_links_path.unlink(True)

    def get_titles(self):
        return [title for _, title, *_ in iter_entries(self.conn)]

    def test_form_of_same_forms(self):
        insert_data(
            self.conn,
            "maldizer",
            "maldizer def",
            ["maldizer", "maldito", "malditos", "maldita", "malditas"],
        )
        insert_data(
            self.conn,
            "maldito",
            "maldito def",
            ["maldito", "maldita", "malditos", "malditas"],
            True,
            ["maldizer"],
        )
        create_indexes(self.conn, "en")
        update_index_num(self.conn)
        self.assertEqual(self.get_titles(), ["maldizer"])
        self.assertEqual(
            list(iter_forms(self.conn)),
            [("maldita", 0), ("malditas", 0), ("maldito", 0), ("malditos", 0)],
        )

    def test_form_of_differen_forms(self):
        insert_data(self.conn, "dyke", "dyke def", ["dyke", "dykes", "dike"])
        insert_data(self.conn, "dyke", "dike def", ["dike", "dikes"], True, ["dyke"])
        create_indexes(self.conn, "en")
        update_index_num(self.conn)
        self.assertEqual(self.get_titles(), ["dyke"])
        self.assertEqual(
            list(iter_forms(self.conn)), [("dike", 0), ("dikes", 0), ("dykes", 0)]
        )

    def test_form_of_target_not_exist(self):
        insert_data(
            self.conn, "TACO", "TACO def", ["TACO"], True, ["Trump always chickens out"]
        )
        create_indexes(self.conn, "en")
        update_index_num(self.conn)
        self.assertEqual(self.get_titles(), ["TACO"])

    def test_word_sort_order(self):
        insert_data(self.conn, "Book", "Book", ["Book", "Books"])
        insert_data(self.conn, "book", "book", ["book", "books", "booking", "booked"])
        insert_data(self.conn, "apple", "apple", ["apple", "apples"])
        update_index_num(self.conn)
        self.assertEqual(self.get_titles(), ["apple", "Book", "book"])
        self.assertEqual(
            list(iter_forms(self.conn)),
            [("apples", 0), ("booked", 2), ("booking", 2), ("Books", 1), ("books", 2)],
        )

    def test_title_not_in_target_forms(self):
        insert_data(
            self.conn,
            "flying colors",
            "flying colors",
            ["flying colors"],
            True,
            ["flying colours"],
        )
        insert_data(self.conn, "flying colours", "flying colours", ["flying colours"])
        update_index_num(self.conn)
        self.assertEqual(self.get_titles(), ["flying colours"])
        self.assertEqual(list(iter_forms(self.conn)), [("flying colors", 0)])

    def test_rm_bad_forms(self):
        insert_data(self.conn, "-isieren", "-isieren", ["-isieren", "-isierend", "ich"])
        for num in range(FORMS_LIMIT):
            insert_data(self.conn, str(num), str(num), [str(num), "ich"])
        update_index_num(self.conn)
        delete_problematic_forms(self.conn)
        form_count = defaultdict(int)
        for form, _ in iter_forms(self.conn):
            form_count[form] += 1
        self.assertEqual(form_count["-isierend"], 1)
        self.assertEqual(form_count["ich"], FORMS_LIMIT)

    def test_form_of_target_fragment(self):
        insert_data(
            self.conn, "ír", "ír verb", ["ír"], ids=["Hungarian", "Hungarian:_to_write"]
        )
        insert_data(self.conn, "ír", "ír adj", ["ír"])
        insert_data(
            self.conn,
            "írhat",
            "írhat",
            ["írhat", "írhatok"],
            True,
            ["ír#Hungarian:_to_write"],
            links=["ír#Hungarian:_to_write"],
        )
        self.conn.commit()
        update_index_num(self.conn)
        combine_links([self.db_path], self.all_links_path)
        insert_fragment_forms(self.conn, "en", self.all_links_path)
        self.assertEqual(self.get_titles(), ["ír", "ír"])
        self.assertEqual(list(iter_forms(self.conn)), [("írhat", 0), ("írhatok", 0)])

    def test_link_id_form(self):
        with self.conn:
            insert_data(
                self.conn,
                "order",
                "order",
                ["order"],
                links=["scale#English:_size_or_scope"],
            )
            insert_data(
                self.conn,
                "scale",
                "scale",
                ["scale"],
                ids=["English", "English:_size_or_scope"],
            )
        update_index_num(self.conn)
        combine_links([self.db_path], self.all_links_path)
        insert_fragment_forms(self.conn, "en", self.all_links_path)
        self.assertEqual(
            list(iter_forms(self.conn)), [("scale#English:_size_or_scope", 1)]
        )
