from pathlib import Path


def get_snapshot_chunks(identifier: str) -> tuple[str, list[str]]:
    import requests

    r = requests.get(
        f"https://github.com/xxyzz/snapshot/releases/latest/download/{identifier}.json"
    )
    data = r.json()
    return data["date"], data["chunks"]


def download_chunk(chunk_identifier: str, path: Path):
    import requests

    r = requests.get(
        f"https://github.com/xxyzz/snapshot/releases/latest/download/{chunk_identifier}.zst",
        stream=True,
    )
    path.parent.mkdir(exist_ok=True)
    with path.open("wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)


def decompress_chunk(zst_path: Path) -> Path:
    import shutil
    from compression import zstd

    ndjson_path = zst_path.with_suffix(".ndjson")
    with zstd.open(zst_path, "rb") as f_in, ndjson_path.open("wb") as f_out:
        shutil.copyfileobj(f_in, f_out)
    return ndjson_path


def get_chunk_zst_path(chunk_identifier: str) -> Path:
    return Path("build").joinpath(chunk_identifier).with_suffix(".zst")
