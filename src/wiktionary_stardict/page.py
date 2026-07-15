def convert_release_data(tag: str):
    import json
    import shutil
    import subprocess
    import tarfile
    from collections import defaultdict
    from pathlib import Path

    from .koreader import koreader_file

    with open("build/release.json", "w") as f:
        subprocess.run(
            ["gh", "release", "view", tag, "--json", "assets,publishedAt"],
            check=True,
            text=True,
            stdout=f,
        )
    with open("build/release.json") as f:
        release_data = json.load(f)
    assets = defaultdict(list)
    gloss_codes = {}
    all_ko_data = []
    for asset in release_data["assets"]:
        if not asset["name"].endswith(".tar.zst") or asset["name"].endswith(
            "_images.tar.zst"
        ):
            continue
        subprocess.run(
            ["gh", "release", "download", tag, "-D", "build", "-p", asset["name"]],
            check=True,
        )
        zst_path = Path("build") / asset["name"]
        zst_name = asset["name"].removesuffix(".tar.zst")
        zst_size = zst_path.stat().st_size
        dict_folder = Path("build") / zst_name
        dict_folder.mkdir(exist_ok=True)
        with tarfile.open(name=zst_path, mode="r") as tar_f:
            tar_f.extractall(path=dict_folder)
        zst_path.unlink()
        with open(dict_folder / f"{dict_folder.name}.ifo") as f:
            ko_data = {"codes": zst_name}
            book_name = ""
            for line in f:
                if line.startswith("bookname="):
                    book_name = line.removeprefix("bookname=").strip()
                    ko_data["name"] = book_name
                elif line.startswith("wordcount="):
                    ko_data["entries"] = int(line.removeprefix("wordcount="))
            all_ko_data.append(ko_data)
            gloss_code = zst_name.rsplit("-", 1)[-1]
            gloss_name = book_name.rsplit("-", 1)[-1]
            assets[gloss_name].append(
                {
                    "name": book_name,
                    "url": asset["url"],
                    "entries": ko_data["entries"],
                    "size": convert_size(zst_size),
                }
            )
            gloss_codes[gloss_name] = gloss_code
        shutil.rmtree(dict_folder)
    date = release_data["publishedAt"]
    koreader_file(all_ko_data)
    return json.dumps(
        {"date": date[: date.index("T")], "assets": assets, "gloss_codes": gloss_codes}
    )


def convert_size(size: int) -> str:
    kb = size / 1000
    if kb < 1000:
        return f"{int(kb)} KB"
    return f"{int(kb / 1000)} MB"


def download_screenshots():
    import subprocess

    subprocess.run(
        ["gh", "release", "download", "20260329", "-D", "_site", "-p", "*.png"],
        check=True,
    )


def create_github_page(args):
    from importlib.resources import files
    from pathlib import Path

    from saxonche import PySaxonProcessor

    from .main import config_proc

    proc = PySaxonProcessor(license=False)
    config_proc(proc)
    xsltproc = proc.new_xslt30_processor()
    xsltproc.set_parameter(
        "data", proc.make_string_value(convert_release_data(args.tag))
    )
    executable = xsltproc.compile_stylesheet(
        stylesheet_file=str(files("wiktionary_stardict") / "xslt" / "github_page.xsl")
    )
    out_path = Path("_site/index.html")
    out_path.parent.mkdir(exist_ok=True)
    Path("docs/fonts.html").copy_into(out_path.parent)
    download_screenshots()
    with out_path.open("w") as f:
        doc = proc.parse_xml(xml_text="<root/>")
        f.write(executable.transform_to_string(xdm_node=doc))
