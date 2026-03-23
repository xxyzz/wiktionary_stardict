from pathlib import Path


def download_zim(edition: str) -> Path:
    import subprocess

    from .main import logger

    zim_path = get_zim_path(edition)
    logger.info("Downloading zim")
    subprocess.run(
        [
            "curl",
            "-L",
            "-o",
            f"build/{edition}.zim",
            f"https://github.com/xxyzz/snapshot/releases/latest/download/{edition}.zim",
        ],
        check=True,
    )
    logger.info("Download zim done")
    return zim_path


def open_zim(path: Path):
    from libzim.reader import Archive

    return Archive(path)


def get_zim_path(edition: str) -> Path:
    return Path(f"build/{edition}.zim")


def get_zim_page(zim, title: str) -> str:
    if not zim.has_entry_by_title(title):
        return ""
    entry = zim.get_entry_by_title(title)
    item = entry.get_item()
    return bytes(item.content).decode("UTF-8")


def get_zim_asset(zim, filename: str) -> bytes | None:
    path = f"_assets_/{filename}"
    if not zim.has_entry_by_path(path):
        return None
    entry = zim.get_entry_by_path(path)
    item = entry.get_item()
    return bytes(item.content)
