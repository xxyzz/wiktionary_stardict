from pathlib import Path


def get_snapshot_chunks(identifier: str, test_pages: list[str]) -> tuple[str, int]:
    from datetime import datetime, timezone

    import requests

    if len(test_pages) > 0:
        return datetime.now(timezone.utc).isoformat().split("T")[0], 1
    r = requests.get(
        f"https://github.com/xxyzz/snapshot/releases/latest/download/{identifier}.json"
    )
    data = r.json()
    return data["date"], data["chunks"]


def download_chunk(edition: str, chunk: str, zst_path: Path, test_pages: list[str]):
    import json
    import subprocess
    from importlib.metadata import version

    import requests

    zst_path.parent.mkdir(exist_ok=True)
    if len(test_pages) == 0:
        subprocess.run(
            [
                "gh",
                "release",
                "download",
                "-D",
                "build",
                "-p",
                f"{chunk}.zst",
                "-R",
                "xxyzz/snapshot",
            ],
            check=True,
        )
        decompress_chunk(zst_path)
    else:
        with open(zst_path.with_suffix(".ndjson"), "w") as f:
            user_agent = f"wiktionary_stardict/{version('wiktionary_stardict')} (https://github.com/xxyzz/wiktionary_stardict)"
            for test_page in test_pages:
                r = requests.get(
                    f"https://{edition}.wiktionary.org/w/rest.php/v1/page/{test_page}/html",
                    headers={"user-agent": user_agent},
                )
                if r.ok:
                    json.dump(
                        {"name": test_page, "html": r.text},
                        f,
                        ensure_ascii=False,
                        separators=(",", ":"),
                    )
                    f.write("\n")


def decompress_chunk(zst_path: Path):
    import shutil
    from compression import zstd

    ndjson_path = zst_path.with_suffix(".ndjson")
    with zstd.open(zst_path, "rb") as f_in, ndjson_path.open("wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
    zst_path.unlink()


def get_chunk_zst_path(chunk_identifier: str) -> Path:
    return Path("build").joinpath(chunk_identifier).with_suffix(".zst")
