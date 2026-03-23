from pathlib import Path

RELEASE_URL = "https://github.com/xxyzz/snapshot/releases/latest/download/"


def get_snapshot_chunks(identifier: str) -> tuple[str, int]:
    import requests

    r = requests.get(f"{RELEASE_URL}{identifier}.json")
    data = r.json()
    return data["date"], data["chunks"]


def download_chunk(chunk: str, path: Path):
    import subprocess

    path.parent.mkdir(exist_ok=True)
    subprocess.run(
        ["curl", "-L", "-o", str(path), f"{RELEASE_URL}{chunk}.zst"], check=True
    )


def decompress_chunk(zst_path: Path) -> Path:
    import shutil
    from compression import zstd

    ndjson_path = zst_path.with_suffix(".ndjson")
    with zstd.open(zst_path, "rb") as f_in, ndjson_path.open("wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
    return ndjson_path


def get_chunk_zst_path(chunk_identifier: str) -> Path:
    return Path("build").joinpath(chunk_identifier).with_suffix(".zst")
