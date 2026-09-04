def convert_release_data(tag: str):
    import json
    import subprocess
    from collections import defaultdict
    from pathlib import Path

    from ..edition import EDITIONS
    from .koreader import koreader_file

    subprocess.run(
        ["gh", "release", "download", tag, "-D", "build", "-p", "*.json"],
        check=True,
    )
    assets = defaultdict(list)
    gloss_codes = {}
    lemma_codes = {}
    ko_data = []
    for json_path in Path("build").glob("*.json"):
        with json_path.open() as f:
            data = json.load(f)
            gloss_code = json_path.stem
            gloss_name = EDITIONS[gloss_code]["lang"]
            for dict_info in data:
                filename = dict_info["filename"].replace(" ", ".")
                lemma_name = (
                    dict_info["bookname"]
                    .removeprefix(EDITIONS[gloss_code]["wiki_name"])
                    .removesuffix(f"-{gloss_name}")
                    .strip()
                )
                assets[gloss_name].append(
                    {
                        "name": lemma_name,
                        "url": f"https://github.com/xxyzz/wiktionary_stardict/releases/download/{tag}/{filename}",
                        "entries": dict_info["wordcount"],
                        "size": convert_size(dict_info["filesize"]),
                        "bytes": dict_info["filesize"],
                    }
                )
                gloss_codes[gloss_name] = gloss_code
                lemma_codes[lemma_name] = dict_info["filename"].removesuffix(
                    f"-{gloss_code}.tar.zst"
                )
            ko_data.extend(data)
    koreader_file(ko_data)
    return json.dumps(
        {
            "date": tag,
            "assets": assets,
            "gloss_codes": gloss_codes,
            "lemma_codes": lemma_codes,
        }
    )


def convert_size(size: int) -> str:
    kb = size / 1000
    if kb < 1000:
        return f"{int(kb)} KB"
    return f"{int(kb / 1000)} MB"


def download_screenshots():
    import subprocess

    subprocess.run(
        [
            "gh",
            "release",
            "download",
            "20260329",
            "-D",
            "_site",
            "-p",
            "*.png",
            "-p",
            "*.avif",
        ],
        check=True,
    )


def create_github_pages(args):
    from importlib.resources import files
    from pathlib import Path

    from saxonche import PySaxonProcessor

    from ..main import config_proc
    from .statistics import create_statistics

    proc = PySaxonProcessor(license=False)
    config_proc(proc)
    xsltproc = proc.new_xslt30_processor()
    xsltproc.set_parameter(
        "data", proc.make_string_value(convert_release_data(args.tag))
    )
    executable = xsltproc.compile_stylesheet(
        stylesheet_file=str(files("wiktionary_stardict") / "github_pages" / "index.xsl")
    )
    index_path = Path("_site/index.html")
    index_path.parent.mkdir(exist_ok=True)
    for ext in ("html", "css", "js"):
        for file in (files("wiktionary_stardict") / "github_pages").glob(f"*.{ext}"):
            file.copy_into(index_path.parent)
    download_screenshots()
    with open(index_path, "w") as f:
        doc = proc.parse_xml(xml_text="<root/>")
        f.write(executable.transform_to_string(xdm_node=doc))
    with open("_site/statistics.html", "w") as f:
        executable = xsltproc.compile_stylesheet(
            stylesheet_file=str(
                files("wiktionary_stardict") / "github_pages" / "statistics.xsl"
            )
        )
        doc = proc.parse_xml(xml_text="<root/>")
        f.write(executable.transform_to_string(xdm_node=doc))
    create_statistics(args.tag)
