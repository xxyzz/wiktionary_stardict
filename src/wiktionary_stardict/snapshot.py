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

    from .main import logger

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
        with (
            open(zst_path.with_suffix(".ndjson"), "w") as f,
            init_requests_session() as session,
        ):
            for test_page in test_pages:
                r = session.get(
                    f"https://{edition}.wiktionary.org/w/rest.php/v1/page/{test_page}/html",
                )
                if r.ok:
                    json.dump(
                        {"name": test_page, "html": r.text},
                        f,
                        ensure_ascii=False,
                        separators=(",", ":"),
                    )
                    f.write("\n")
                else:
                    logger.warning(
                        f'Download page "{test_page}" failed: {r.status_code=}'
                        f" {r.reason=} {r.text=}"
                    )


def decompress_chunk(zst_path: Path):
    import shutil
    from compression import zstd

    ndjson_path = zst_path.with_suffix(".ndjson")
    with zstd.open(zst_path, "rb") as f_in, ndjson_path.open("wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
    zst_path.unlink()


def get_chunk_zst_path(chunk_identifier: str) -> Path:
    return Path("build").joinpath(chunk_identifier).with_suffix(".zst")


def get_user_agent() -> str:
    from importlib.metadata import version

    return f"wiktionary_stardict/{version('wiktionary_stardict')} (https://github.com/xxyzz/wiktionary_stardict)"


def init_requests_session():
    from requests import Session
    from requests.adapters import HTTPAdapter
    from urllib3.util import Retry

    s = Session()
    s.mount(
        "https://",
        HTTPAdapter(
            max_retries=Retry(total=5, backoff_factor=0.1, status_forcelist=[429])
        ),
    )
    s.headers.update({"user-agent": get_user_agent()})
    return s
