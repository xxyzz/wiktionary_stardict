from sqlite3 import Connection


def init_db(lemma_lang: str) -> Connection:
    import sqlite3
    from pathlib import Path

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
    """)
    return conn


def create_indexes(conn: Connection):
    conn.executescript("""
    CREATE INDEX entry_index ON entry (title);
    CREATE INDEX form_index ON form (entry_id);
    CREATE INDEX form_of_index ON form_of (entry_id);
    CREATE INDEX image_index ON image (entry_id);
    PRAGMA optimize;
    """)
    conn.commit()


def check_def_len(conn: Connection) -> bool:
    for (use_64_bits,) in conn.execute("""
    SELECT sum(octet_length(e.definition)) > 0xFFFF_FFFF
    FROM entry e
    WHERE e.form_of_only = 0 OR (e.form_of_only = 1 AND (
      NOT EXISTS (
        SELECT 1 FROM form_of fo JOIN entry e2
        WHERE fo.entry_id = e.id AND fo.target = e2.title
      )))
    """):
        return bool(use_64_bits)
    return False


def iter_entries(conn: Connection):
    for index, (entry_id, definition, title, images) in enumerate(
        conn.execute("""
    SELECT e.id, e.definition, e.title, group_concat(i.url, '<sep>')
    FROM entry e
    LEFT JOIN image i on i.entry_id = e.id
    WHERE e.form_of_only = 0 OR (e.form_of_only = 1 AND (
      NOT EXISTS (
        SELECT 1 FROM form_of fo JOIN entry e2
        WHERE fo.entry_id = e.id AND fo.target = e2.title
      )
    )) GROUP BY e.id ORDER BY e.title_lower, e.title
    """)
    ):
        conn.execute("UPDATE entry SET index_num = ? WHERE id = ?", (index, entry_id))
        yield (definition, title, images.split("<sep>") if images is not None else [])
    conn.commit()


def iter_forms(conn: Connection):
    for form, index in conn.execute("""
    WITH form_only_forms AS MATERIALIZED (
      SELECT e.title_lower, e.title, f.form_lower, f.form, t_e.index_num
      FROM entry e
      JOIN form_of fo ON fo.entry_id = e.id
      JOIN entry t_e ON t_e.title = fo.target
      LEFT JOIN form f ON f.entry_id = e.id
      WHERE e.index_num IS NULL AND t_e.index_num IS NOT NULL
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


def insert_data(
    conn: Connection,
    definition: str,
    forms: list[str],
    form_of_only: bool,
    form_of_targets: list[str],
    images: list[str],
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
