from pathlib import Path
from sqlite3 import Connection


def download_redirect_db(edition: str) -> Path:
    import shutil
    import subprocess
    from compression import zstd

    db_path = Path("build") / f"{edition}_redirect.db"
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
        with zstd.open(db_zst_path, "rb") as f_in, db_path.open("wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
        db_zst_path.unlink()
    return db_path


def get_redirect_pages(conn: Connection, target: str) -> list[tuple[str, str]]:
    results = []
    for title, fragment in conn.execute(
        "SELECT source, fragment FROM redirect WHERE target = ?", (target,)
    ):
        results.append((title, fragment))
    return results


def add_redirects(
    conn: Connection, page_title: str, page_data_list: list[dict[str, list[str]]]
):
    redirects = get_redirect_pages(conn, page_title)
    if len(redirects) > 0:
        for redirect_title, fragment in redirects:
            if fragment != "":
                added = False
                for page_data in page_data_list:
                    if fragment in page_data.get("ids", []):
                        add_redirect(redirect_title, page_data)
                        added = True
                        break
                if added:
                    break
            for page_data in page_data_list:
                add_redirect(redirect_title, page_data)


def add_redirect(title: str, page_data):
    page_data["forms"] = list(dict.fromkeys(page_data["forms"] + [title]))
