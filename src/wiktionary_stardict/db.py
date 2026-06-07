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
      definition   TEXT,
      form_of_only INTEGER,
      index_num    INTEGER
    );

    CREATE TABLE form (
      id       INTEGER PRIMARY KEY,
      entry_id INTEGER,
      form     TEXT,
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


def iter_entries(conn: Connection):
    for index, (entry_id, definition, title, images) in enumerate(
        conn.execute("""
    SELECT e.id, e.definition, e.title, group_concat(i.url, '<sep>')
    FROM entry e
    LEFT JOIN form f ON f.entry_id = e.id
    LEFT JOIN image i on i.entry_id = e.id
    WHERE e.form_of_only = 0 OR (e.form_of_only = 1 AND (
      NOT EXISTS (
        SELECT 1 FROM form_of fo
        WHERE fo.entry_id = e.id AND fo.target IN (SELECT title FROM entry)
      )
      OR EXISTS (
        SELECT 1 FROM form f2
        WHERE f2.entry_id = e.id AND f2.form NOT IN (
          SELECT f3.form FROM form f3 JOIN entry e2 ON f3.entry_id = e2.id
          WHERE e2.title IN (
            SELECT fo.target FROM form_of fo WHERE fo.entry_id = e.id
          )
        )
      )
    )) GROUP by e.id ORDER BY e.title
    """)
    ):
        conn.execute("UPDATE entry SET index_num = ? WHERE id = ?", (index, entry_id))
        yield (
            index,
            definition,
            title,
            images.split("<sep>") if images is not None else [],
        )
    conn.commit()


def iter_forms(conn: Connection):
    for form, index in conn.execute("""
    SELECT f.form, e.index_num
    FROM form f
    LEFT JOIN entry e ON f.entry_id = e.id
    WHERE e.index_num IS NOT NULL
    ORDER BY f.form
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
        INSERT INTO entry (title, definition, form_of_only)
        VALUES(?, ?, ?) RETURNING id
        """,
        (forms[0], definition, form_of_only),
    ):
        conn.executemany(
            "INSERT INTO form (entry_id, form) VALUES(?, ?)",
            ((entry_id, form) for form in forms[1:]),
        )
        conn.executemany(
            "INSERT INTO form_of (entry_id, target) VALUES(?, ?)",
            ((entry_id, target) for target in form_of_targets),
        )
        conn.executemany(
            "INSERT INTO image (entry_id, url) VALUES(?, ?)",
            ((entry_id, url) for url in images),
        )
