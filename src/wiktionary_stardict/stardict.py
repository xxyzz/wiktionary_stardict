from pathlib import Path
from sqlite3 import Connection


def download_image(res_path: Path, url: str, edition: str, zim):
    import re
    import urllib.parse

    import requests

    from .zim import get_zim_asset

    filename = url.rsplit("/", maxsplit=1)[-1]
    if "?" in filename:
        filename = filename[: filename.index("?")]
    if "math/render/svg/" in url:
        filename += ".svg"
    filename = urllib.parse.unquote(re.sub(r"\..*\.", ".", filename))
    if url.startswith("//"):
        url = "https:" + url
    elif url.startswith("/"):
        url = f"https://{edition}.wiktionary.org/{url.lstrip('/')}"
    if not res_path.is_dir():
        res_path.mkdir()
    file_path = res_path / filename
    if not file_path.is_file():
        if zim is not None:
            data = get_zim_asset(zim, filename)
            if data is not None:
                with file_path.open("wb") as f:
                    f.write(data)
                return
        cache_path = Path(f"build/{edition}_images/{filename}")
        if cache_path.is_file():
            cache_path.copy(file_path)
        else:
            r = requests.get(url, headers={"user-agent": get_user_agent()})
            if r.ok:
                with file_path.open("wb") as f:
                    f.write(r.content)


def get_user_agent() -> str:
    from importlib.metadata import version

    return f"wikitionary_stardict/{version('wiktionary_stardict')} (https://github.com/xxyzz/wiktionary_stardict)"


def create_stardict(
    edition: str, snapshot_date: str, zim_path: Path | None, lemma_lang: str
):
    import shutil
    import sqlite3
    import tarfile
    from pathlib import Path

    from mediawiki_langcodes import name_to_code

    from .edition import EDITIONS
    from .main import logger
    from .zim import open_zim

    zim = None
    if zim_path is not None:
        zim = open_zim(zim_path)
    lemma_code = name_to_code(lemma_lang, edition)
    folder_name = f"{lemma_code}-{edition}"
    out_path = Path("build") / folder_name
    if out_path.exists():
        shutil.rmtree(out_path)
    out_path.mkdir()
    db_path = Path(f"build/{lemma_lang}.db")
    with sqlite3.connect(db_path) as conn:
        logger.info(f"start creating {folder_name} dict and idx files")
        wordcount, idxfilesize, use_64_bits_offset = create_dict_idx_file(
            out_path, conn, edition, zim
        )
        logger.info(f"{folder_name} dict and idx files created")
        synwordcount = create_syn_file(out_path, conn)
        logger.info(f"{folder_name} syn file created")
    create_ifo_file(
        out_path,
        f"{EDITIONS[edition]['wiki_name']} {lemma_lang}-{EDITIONS[edition]['lang']}",
        wordcount,
        synwordcount,
        idxfilesize,
        snapshot_date,
        64 if use_64_bits_offset else 32,
    )
    css_path = get_css_path(edition)
    if css_path.exists():
        css_path.copy(out_path / f"{folder_name}.css")
    tar_path = out_path.with_suffix(".tar.zst")
    if tar_path.exists():
        tar_path.unlink()
    with tarfile.open(name=tar_path, mode="x:zst") as tar:
        tar.add(out_path, arcname=".")
    res_path = out_path / "res"
    res_dst_path = Path(f"build/{lemma_lang}_res_images")
    if res_dst_path.is_dir():
        shutil.rmtree(res_dst_path)
    if res_path.is_dir():
        shutil.move(res_path, res_dst_path)
    shutil.rmtree(out_path)
    db_path.unlink()


def get_css_path(edition: str) -> Path:
    from importlib.resources import files

    return files("wiktionary_stardict") / "css" / edition / "style.css"


def convert_number(number: int, use_64_bits: bool = False) -> bytes:
    import struct

    return struct.pack("!Q" if use_64_bits else "!I", number)


def create_dict_idx_file(
    folder: Path, conn: Connection, edition: str, zim
) -> tuple[int, int, bool]:
    from idzip import IdzipFile

    from .db import check_def_len, iter_entries

    dict_path = folder / (folder.name + ".dict.dz")
    idx_path = folder / (folder.name + ".idx")
    res_path = folder / "res"
    use_64_bits_offset = check_def_len(conn)
    with IdzipFile(str(dict_path), "wb") as dict_f, idx_path.open("wb") as idx_f:
        offset = 0
        wordcount = 0
        for definition, title, images in iter_entries(conn):
            def_bytes = definition.encode("utf-8")
            dict_f.write(def_bytes)
            def_len = len(def_bytes)
            idx_f.write(
                title.encode("utf-8")
                + b"\0"
                + convert_number(offset, use_64_bits_offset)
                + convert_number(def_len)
            )
            offset += def_len
            wordcount += 1
            for image in images:
                download_image(res_path, image, edition, zim)

    return wordcount, idx_path.stat().st_size, use_64_bits_offset


def create_syn_file(folder: Path, conn: Connection) -> int:
    from .db import iter_forms

    syn_path = folder / (folder.name + ".syn")
    synwordcount = 0
    with syn_path.open("wb") as f:
        for form, index in iter_forms(conn):
            f.write(form.encode("utf-8") + b"\0" + convert_number(index))
            synwordcount += 1
    return synwordcount


def create_ifo_file(
    folder: Path,
    bookname: str,
    wordcount: int,
    synwordcount: int,
    idxfilesize: int,
    snapshot_date: str,
    idxoffsetbits: int,
):
    from datetime import date

    with (folder / (folder.name + ".ifo")).open("w") as f:
        f.write(f"""StarDict's dict ifo file
version=3.0.0
bookname={bookname}
wordcount={wordcount}
synwordcount={synwordcount}
idxfilesize={idxfilesize}
idxoffsetbits={idxoffsetbits}
author=xxyzz
website=https://github.com/xxyzz/wiktionary_stardict
description=Snapshot {snapshot_date}, Wiktionary license CC BY-SA 4.0
date={date.today().isoformat()}
sametypesequence=h
""")


def download_last_release_images(edition: str):
    import shutil
    import subprocess
    import tarfile

    zst_name = f"{edition}_images.tar.zst"
    subprocess.run(["gh", "release", "download", "-D", "build", "-p", zst_name])
    zst_path = Path("build") / zst_name
    if zst_path.is_file():
        archive_folder = Path(f"build/{edition}_images")
        if archive_folder.is_dir():
            shutil.rmtree(archive_folder)
        with tarfile.open(name=zst_path, mode="r") as tar:
            tar.extractall("build")
        zst_path.unlink()


def archive_images(edition: str):
    import shutil
    import tarfile

    archive_folder = Path(f"build/{edition}_images")
    if archive_folder.is_dir():
        shutil.rmtree(archive_folder)
    archive_folder.mkdir()
    has_file = False
    for images_dir in Path("build").glob("*_res_images"):
        for image in images_dir.iterdir():
            image.move(archive_folder / image.name)
            has_file = True
        shutil.rmtree(images_dir)
    if has_file:
        tar_path = archive_folder.with_suffix(".tar.zst")
        with tarfile.open(name=tar_path, mode="x:zst") as tar:
            tar.add(archive_folder, arcname=".")
