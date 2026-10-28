from pathlib import Path
from sqlite3 import Connection


def init_db(lemma_lang: str) -> Connection:
    import sqlite3

    db_path = Path(f"build/{lemma_lang}.db")
    if db_path.exists():
        db_path.unlink()
    conn = sqlite3.connect(db_path)
    conn.executescript("""
    PRAGMA foreign_keys = ON;
    CREATE TABLE entry (
      id           INTEGER PRIMARY KEY,
      title        TEXT,
      title_lower  TEXT,
      definition   TEXT,
      form_of_only INTEGER,
      index_num    INTEGER,
      origin_title TEXT
    );

    CREATE TABLE form (
      id         INTEGER PRIMARY KEY,
      entry_id   INTEGER,
      form       TEXT,
      form_lower TEXT,
      FOREIGN KEY(entry_id) REFERENCES entry(id)
    );

    CREATE TABLE form_of (
      id       INTEGER PRIMARY KEY,
      entry_id INTEGER,
      target   TEXT,
      FOREIGN KEY(entry_id) REFERENCES entry(id)
    );

    CREATE TABLE image (
      id  INTEGER PRIMARY KEY,
      entry_id INTEGER,
      url TEXT,
      FOREIGN KEY(entry_id) REFERENCES entry(id)
    );

    CREATE TABLE title_fragment (
      id       INTEGER PRIMARY KEY,
      entry_id INTEGER,
      text     TEXT,
      FOREIGN KEY(entry_id) REFERENCES entry(id)
    );

    CREATE TABLE link (
      id       INTEGER PRIMARY KEY,
      entry_id INTEGER,
      href     TEXT,
      FOREIGN KEY(entry_id) REFERENCES entry(id)
    );
    """)
    create_sql_function(conn)
    return conn


def create_sql_function(conn: Connection):
    conn.create_function("py_lower", 1, str.lower, deterministic=True)


def create_indexes(conn: Connection):
    conn.executescript("""
    CREATE INDEX entry_index ON entry (origin_title);
    CREATE INDEX form_index ON form (entry_id, form);
    CREATE INDEX form_of_index ON form_of (entry_id);
    CREATE INDEX image_index ON image (entry_id);
    CREATE INDEX fragment_index ON title_fragment (text, entry_id);
    CREATE INDEX link_index ON link (href, entry_id);
    PRAGMA optimize;""")


def update_index_num(conn: Connection):
    conn.execute("""
    WITH rn AS (
      SELECT e.id, row_number() OVER (ORDER BY e.title_lower, e.title) - 1 AS index_num
      FROM entry e
      WHERE e.form_of_only = 0 OR (e.form_of_only = 1 AND (
      NOT EXISTS (
        SELECT 1 FROM form_of fo
        JOIN entry e2 ON fo.target = e2.origin_title
        WHERE fo.entry_id = e.id
        UNION ALL
        SELECT 1 FROM form_of fo
        JOIN title_fragment tf ON fo.target = tf.text
        WHERE fo.entry_id = e.id
    ))))
    UPDATE entry AS e
    SET index_num = rn.index_num
    FROM rn
    WHERE e.id = rn.id""")


def check_def_len(conn: Connection) -> bool:
    for (use_64_bits,) in conn.execute("""
    SELECT sum(octet_length(e.definition)) > 0xFFFFFFFF
    FROM entry e WHERE e.index_num IS NOT NULL"""):
        return bool(use_64_bits)
    return False


def iter_entries(conn: Connection):
    for definition, title, images in conn.execute("""
        SELECT e.definition, e.title, group_concat(i.url, '<sep>')
        FROM entry e
        LEFT JOIN image i ON i.entry_id = e.id
        WHERE e.index_num IS NOT NULL
        GROUP BY e.id ORDER BY e.title_lower, e.title"""):
        yield (definition, title, images.split("<sep>") if images is not None else [])


def iter_forms(conn: Connection):
    for form, index in conn.execute("""
    WITH form_only_forms AS MATERIALIZED (
      SELECT e.title_lower, e.title, f.form_lower, f.form, te.index_num
      FROM entry e
      JOIN form_of fo ON fo.entry_id = e.id
      JOIN entry te ON fo.target = te.origin_title
      LEFT JOIN form f ON f.entry_id = e.id AND f.form != te.title
      WHERE e.index_num IS NULL AND te.index_num IS NOT NULL AND NOT EXISTS (
        SELECT 1
        FROM entry te2
        JOIN form te2f ON te2f.entry_id = te2.id
        WHERE te2.origin_title = te.origin_title AND te2f.form = e.title AND
        NOT EXISTS (SELECT 1 FROM form ef WHERE ef.entry_id = e.id)
      )
      UNION ALL
      SELECT e.title_lower, e.title, f.form_lower, f.form, te.index_num
      FROM entry e
      JOIN form_of fo ON fo.entry_id = e.id
      JOIN title_fragment tf ON tf.text = fo.target
      JOIN entry te ON tf.entry_id = te.id
      LEFT JOIN form f ON f.entry_id = e.id AND f.form != te.title
      WHERE e.index_num IS NULL AND te.index_num IS NOT NULL AND NOT EXISTS (
        SELECT 1
        FROM entry te2
        JOIN form te2f ON te2f.entry_id = te2.id
        WHERE te2.origin_title = te.origin_title AND te2f.form = e.title AND
        NOT EXISTS (SELECT 1 FROM form ef WHERE ef.entry_id = e.id)
      )
    )
    SELECT DISTINCT form, index_num FROM (
      SELECT f.form_lower, f.form, e.index_num
      FROM form f
      JOIN entry e ON f.entry_id = e.id
      WHERE e.index_num IS NOT NULL
      UNION ALL
      SELECT title_lower AS form_lower, title AS form, index_num
      FROM form_only_forms
      UNION ALL
      SELECT form_lower, form, index_num
      FROM form_only_forms
      WHERE form IS NOT NULL
    )
    ORDER BY form_lower, form
    """):
        yield form, index


FORMS_LIMIT = 100


def delete_problematic_forms(conn: Connection):
    # some unexpected forms like pronoun link to too many entries,
    # keep 100 and delete the rest
    conn.execute(
        """
    WITH bad_form AS (
      SELECT form
      FROM form
      GROUP BY form
      HAVING COUNT(DISTINCT entry_id) > :limit
    ),
    delete_id AS (
      SELECT f.id, row_number() OVER (PARTITION BY f.form ORDER BY f.id) AS rn
      FROM form AS f
      JOIN bad_form AS b ON f.form = b.form
    )
    DELETE FROM form
    WHERE id IN (
     SELECT id
     FROM delete_id
     WHERE rn > :limit
    )
    """,
        {"limit": FORMS_LIMIT},
    )


def insert_data(
    conn: Connection,
    page_name: str,
    definition: str,
    forms: list[str],
    form_of_only: bool = False,
    form_of_targets: list[str] = [],
    images: list[str] = [],
    ids: list[str] = [],
    links: list[str] = [],
):
    for (entry_id,) in conn.execute(
        """
        INSERT INTO entry (title, title_lower, definition, form_of_only, origin_title)
        VALUES(?, ?, ?, ?, ?) RETURNING id
        """,
        (forms[0], forms[0].lower(), definition, form_of_only, page_name),
    ):
        conn.executemany(
            "INSERT INTO form (entry_id, form, form_lower) VALUES(?, ?, ?)",
            ((entry_id, form, form.lower()) for form in forms[1:]),
        )
        conn.executemany(
            "INSERT INTO form_of (entry_id, target) VALUES(?, ?)",
            ((entry_id, target) for target in form_of_targets),
        )
        conn.executemany(
            "INSERT INTO image (entry_id, url) VALUES(?, ?)",
            ((entry_id, url) for url in images),
        )
        conn.executemany(
            "INSERT INTO title_fragment (entry_id, text) VALUES(?, ?)",
            ((entry_id, f"{page_name.replace(' ', '_')}#{id}") for id in ids),
        )
        conn.executemany(
            "INSERT INTO link (entry_id, href) VALUES(?, ?)",
            ((entry_id, href) for href in links),
        )


def insert_fragment_forms(conn: Connection):
    conn.execute("""
    INSERT INTO form (entry_id, form, form_lower)
    SELECT DISTINCT tf.entry_id, text, py_lower(text)
    FROM title_fragment tf
    JOIN link l ON l.href = tf.text
    JOIN entry e ON e.id = tf.entry_id
    WHERE e.index_num IS NOT NULL""")


def delete_links(conn: Connection):
    conn.execute("""
    DELETE FROM link
    WHERE EXISTS (
      SELECT 1
      FROM entry e
      WHERE e.id = link.entry_id AND e.index_num IS NULL
    ) OR (
      NOT EXISTS (
        SELECT 1
        FROM title_fragment tf
        JOIN entry e ON e.id = tf.entry_id
        WHERE tf.text = link.href AND e.index_num IS NOT NULL
    ) OR (
      SELECT count(DISTINCT tf.entry_id)
      FROM title_fragment tf
      JOIN entry e ON e.id = tf.entry_id
      WHERE tf.text = link.href AND e.index_num IS NOT NULL
    ) = (
      SELECT count(DISTINCT e.id)
      FROM entry e
      WHERE e.origin_title =
        replace(substr(link.href, 0, instr(link.href, '#')), '_', ' ') AND
        e.index_num IS NOT NULL
    ))""")


def iter_entry_with_links(conn: Connection):
    for id, definition, links in conn.execute("""
    SELECT e.id, e.definition, group_concat(l.href, '<sep>')
    FROM entry e
    LEFT JOIN link l ON e.id = l.entry_id
    WHERE e.index_num IS NOT NULL
    GROUP BY e.id, e.definition"""):
        yield id, definition, [] if links is None else links.split("<sep>")


def update_entry_links(conn: Connection, id: str, html: str):
    conn.execute("UPDATE entry SET definition = ? WHERE id = ?", (html, id))
