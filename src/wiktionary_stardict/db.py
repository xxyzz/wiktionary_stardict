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
      index_num    INTEGER
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


def create_indexes(conn: Connection, edition: str):
    sql = """
    CREATE INDEX entry_index ON entry (title);
    CREATE INDEX form_index ON form (entry_id, form);
    CREATE INDEX form_of_index ON form_of (entry_id);
    CREATE INDEX image_index ON image (entry_id);
    CREATE INDEX fragment_index ON title_fragment (entry_id, text);
    """
    if edition == "simple":
        sql += "CREATE INDEX link_index ON link (entry_id, href);"
    else:
        sql += "CREATE INDEX link_index ON link (entry_id);"
    sql += "PRAGMA optimize;"
    conn.executescript(sql)
    conn.commit()


def check_def_len(conn: Connection) -> bool:
    for (use_64_bits,) in conn.execute("""
    SELECT sum(octet_length(e.definition)) > 0xFFFFFFFF
    FROM entry e
    WHERE e.form_of_only = 0 OR (e.form_of_only = 1 AND (
      NOT EXISTS (
        SELECT 1 FROM form_of fo
        JOIN entry e2 ON fo.target = e2.title
        WHERE fo.entry_id = e.id
        UNION ALL
        SELECT 1 FROM form_of fo
        JOIN title_fragment tf ON fo.target = tf.text
        WHERE fo.entry_id = e.id
      )))
    """):
        return bool(use_64_bits)
    return False


def iter_entries(conn: Connection):
    for index, (entry_id, definition, title, images) in enumerate(
        conn.execute("""
    SELECT e.id, e.definition, e.title, group_concat(i.url, '<sep>')
    FROM entry e
    LEFT JOIN image i ON i.entry_id = e.id
    WHERE e.form_of_only = 0 OR (e.form_of_only = 1 AND (
      NOT EXISTS (
        SELECT 1 FROM form_of fo
        JOIN entry e2 ON fo.target = e2.title
        WHERE fo.entry_id = e.id
        UNION ALL
        SELECT 1 FROM form_of fo
        JOIN title_fragment tf ON fo.target = tf.text
        WHERE fo.entry_id = e.id
      )
    )) GROUP BY e.id ORDER BY e.title_lower, e.title
    """)
    ):
        conn.execute("UPDATE entry SET index_num = ? WHERE id = ?", (index, entry_id))
        yield (definition, title, images.split("<sep>") if images is not None else [])

    delete_problematic_forms(conn)
    conn.commit()


def iter_forms(conn: Connection):
    for form, index in conn.execute("""
    WITH form_only_forms AS MATERIALIZED (
      SELECT e.title_lower, e.title, f.form_lower, f.form, te.index_num
      FROM entry e
      JOIN form_of fo ON fo.entry_id = e.id
      JOIN entry te ON te.title = fo.target
      LEFT JOIN form f ON f.entry_id = e.id
      WHERE e.index_num IS NULL AND te.index_num IS NOT NULL
      UNION ALL
      SELECT e.title_lower, e.title, f.form_lower, f.form, te.index_num
      FROM entry e
      JOIN form_of fo ON fo.entry_id = e.id
      JOIN title_fragment tf ON tf.text = fo.target
      JOIN entry te ON tf.entry_id = te.id
      LEFT JOIN form f ON f.entry_id = e.id
      WHERE e.index_num IS NULL AND te.index_num IS NOT NULL
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
        INSERT INTO entry (title, title_lower, definition, form_of_only)
        VALUES(?, ?, ?, ?) RETURNING id
        """,
        (forms[0], forms[0].lower(), definition, form_of_only),
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


def combine_links(db_paths: list[Path], all_links_path: Path):
    import sqlite3

    if all_links_path.exists():
        all_links_path.unlink()
    conn = sqlite3.connect(all_links_path)
    conn.execute("CREATE TABLE link (href TEXT PRIMARY KEY)")
    for db_path in db_paths:
        conn.execute("ATTACH DATABASE ? AS lang_db", (str(db_path),))
        conn.executescript(
            """
            INSERT OR IGNORE INTO main.link (href)
            SELECT l.href
            FROM lang_db.entry e
            JOIN lang_db.link l ON e.id = l.entry_id
            WHERE e.index_num IS NOT NULL;
            DETACH DATABASE lang_db;
            """
        )
    conn.execute("PRAGMA optimize;")
    conn.commit()
    conn.close()


def insert_fragment_forms(conn: Connection, edition: str, all_links_path: Path):
    if edition == "simple":
        conn.execute(
            """
            INSERT INTO form (entry_id, form, form_lower)
            SELECT DISTINCT tf.entry_id, text, py_lower(text)
            FROM title_fragment tf JOIN link l ON l.href = tf.text
            """
        )
    else:
        conn.execute("ATTACH DATABASE ? AS all_links", (str(all_links_path),))
        conn.executescript(
            """
            INSERT INTO form (entry_id, form, form_lower)
            SELECT DISTINCT entry_id, text, py_lower(text)
            FROM title_fragment tf JOIN all_links.link l ON l.href = tf.text;
            DETACH DATABASE all_links;
            """
        )
