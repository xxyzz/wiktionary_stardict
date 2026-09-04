import json
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import TypedDict


class ReleaseData(TypedDict):
    date: str
    wordcount: int
    synwordcount: int
    filesize: int


def download_previous_data(edition: str, new_tag: str) -> dict[str, list[ReleaseData]]:
    import gzip

    import requests

    r = requests.get(f"https://xxyzz.github.io/wiktionary_stardict/{edition}.gz")
    if r.ok:
        return json.loads(gzip.decompress(r.content))
    else:
        return download_data_from_releases(edition, new_tag)


def download_data_from_releases(
    edition: str, new_tag: str
) -> dict[str, list[ReleaseData]]:
    import re

    if not Path("build/20260815").exists():
        releases_json = Path("build/releases.json")
        with open(releases_json, "w") as f:
            subprocess.run(
                ["gh", "release", "list", "--json", "tagName"],
                check=True,
                text=True,
                stdout=f,
            )
        with open(releases_json) as f:
            for release in json.load(f):
                if release["tagName"] == new_tag:
                    continue
                json_folder = Path("build") / release["tagName"]
                json_folder.mkdir(exist_ok=True)
                subprocess.run(
                    [
                        "gh",
                        "release",
                        "download",
                        release["tagName"],
                        "-D",
                        str(json_folder),
                        "-p",
                        "*.json",
                    ],
                    check=True,
                )
                if release["tagName"] == "20260815":
                    break
        releases_json.unlink()

    all_data = defaultdict(list)
    for folder in Path("build").iterdir():
        if folder.is_dir() and re.match(r"\d{8}", folder.name):
            json_path = folder / f"{edition}.json"
            if json_path.exists():
                with open(json_path) as f:
                    add_edition_data(all_data, edition, folder.name, json.load(f))
    return all_data


def add_edition_data(
    all_data: dict[str, list[ReleaseData]],
    edition: str,
    release_date: str,
    new_data: list[dict[str, int]],
):
    for lang_data in new_data:
        lemma_code = lang_data["filename"].removesuffix(f"-{edition}.tar.zst")
        all_data[lemma_code].append(
            {
                "date": release_date,
                "wordcount": lang_data["wordcount"],
                "synwordcount": lang_data["synwordcount"],
                "filesize": lang_data["filesize"],
            }
        )


def create_statistics(new_tag: str):
    import gzip

    for new_json in Path("build").glob("*.json"):
        edition = new_json.stem
        all_data = download_previous_data(edition, new_tag)
        with open(new_json) as f:
            add_edition_data(all_data, edition, new_tag, json.load(f))
        gz_path = Path(f"_site/{edition}.gz")
        gz_path.unlink(True)
        for lang_data in all_data.values():
            lang_data.sort(key=lambda d: int(d["date"]))

        with gzip.open(gz_path, "wt", encoding="utf-8") as f:
            json.dump(all_data, f, ensure_ascii=False, separators=(",", ":"))
