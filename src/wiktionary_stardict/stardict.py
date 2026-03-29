from pathlib import Path


def create_glossary(lemma_lang: str, gloss_lang: str, snapshot_date: str):
    from datetime import date

    from pyglossary.glossary_v2 import Glossary

    return Glossary(
        {
            "version": "3.0.0",
            "bookname": f"Wiktionary {lemma_lang}-{gloss_lang}",
            "author": "xxyzz",
            "website": "https://github.com/xxyzz/wiktionary_stardict",
            "description": f"Snapshot {snapshot_date}. Wiktionary license CC BY-SA 4.0",
            "date": date.today().isoformat(),
        }
    )


def add_entry(
    glos,
    edition: str,
    forms: list[str],
    definition: str,
    images: str[str],
    added_files: set[str],
    zim,
):
    glos.addEntry(glos.newEntry(forms, definition, defiFormat="h"))
    for image in images:
        download_image(glos, image, edition, added_files, zim)


def download_image(glos, url: str, edition: str, added_files: set[str], zim):
    import re

    import requests

    from .zim import get_zim_asset

    filename = url.rsplit("/", maxsplit=1)[-1]
    if "?" in filename:
        filename = filename[: filename.index("?")]
    if "math/render/svg/" in url:
        filename += ".svg"
    filename = re.sub(r"\..*\.", ".", filename)
    if url.startswith("//"):
        url = "https:" + url
    elif url.startswith("/"):
        url = f"https://{edition}.wiktionary.org/{url.lstrip('/')}"
    if filename not in added_files:
        if zim is not None:
            data = get_zim_asset(zim, filename)
            if data is not None:
                glos.addEntry(glos.newDataEntry(filename, data))
                added_files.add(filename)
                return
        r = requests.get(
            url,
            headers={"user-agent": get_user_agent()},
        )
        if r.ok:
            glos.addEntry(glos.newDataEntry(filename, r.content))
            added_files.add(filename)


def get_user_agent() -> str:
    from importlib.metadata import version

    return f"wikitionary_stardict/{version('wiktionary_stardict')} (https://github.com/xxyzz/wiktionary_stardict)"


def create_stardict(glos, lemma_lang: str, edition: str):
    import shutil
    import tarfile
    from pathlib import Path

    from mediawiki_langcodes import name_to_code

    folder_name = f"{name_to_code(lemma_lang, edition)}-{edition}"
    out_path = Path("build") / folder_name
    if out_path.exists():
        shutil.rmtree(out_path)
    out_path.mkdir(exist_ok=True)
    glos.write(
        f"build/{folder_name}/{folder_name}.ifo",
        formatName="Stardict",
        dictzip=True,
        sametypesequence="h",
    )
    css_path = get_css_path(edition)
    if css_path.exists():
        css_path.copy(out_path / f"{folder_name}.css")
    tar_path = out_path.with_suffix(".tar.zst")
    if tar_path.exists():
        tar_path.unlink()
    with tarfile.open(name=tar_path, mode="x:zst") as tar:
        tar.add(out_path, arcname=".")
    shutil.rmtree(out_path)


def get_css_path(edition: str) -> Path:
    from importlib.resources import files

    return files("wiktionary_stardict") / "css" / edition / "style.css"
