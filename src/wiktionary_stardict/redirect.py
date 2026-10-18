from pathlib import Path
from sqlite3 import Connection


def download_redirect_db(edition: str) -> Path:
    import shutil
    import subprocess
    from compression import zstd

    db_path = Path(f"build/{edition}_redirect.db")
    db_path.parent.mkdir(exist_ok=True)
    db_zst_path = db_path.with_suffix(db_path.suffix + ".zst")
    if not db_path.exists() and not db_zst_path.exists():
        subprocess.run(
            [
                "gh",
                "release",
                "download",
                "-D",
                "build",
                "-p",
                db_path.name + ".zst",
                "-R",
                "xxyzz/snapshot",
            ],
            check=True,
        )
        with zstd.open(db_zst_path, "rb") as f_in, open(db_path, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
        db_zst_path.unlink()
    return db_path


def add_redirects(conn: Connection, rdb_path: Path):
    conn.execute("ATTACH DATABASE ? AS rdb", (str(rdb_path),))
    conn.executescript("""
    INSERT INTO form (entry_id, form, form_lower)
    SELECT DISTINCT e.id, r.source, py_lower(r.source)
    FROM rdb.redirect r
    JOIN entry e ON r.target = e.origin_title AND r.source != e.title
    WHERE NOT EXISTS (
      SELECT 1
      FROM form f
      WHERE f.entry_id = e.id AND f.form = r.source
    ) AND (EXISTS (
      SELECT 1
      FROM title_fragment tf
      WHERE tf.entry_id = e.id AND
        tf.text = concat(replace(e.origin_title, ' ', '_'), '#', r.fragment)
    ) OR NOT EXISTS (
      SELECT 1
      FROM entry e2
      JOIN title_fragment tf2 ON e2.id = tf2.entry_id
      WHERE e2.origin_title = r.target AND
        tf2.text = concat(replace(e2.origin_title, ' ', '_'), '#', r.fragment)
    ));
    DETACH DATABASE rdb;""")
