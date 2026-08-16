def convert_release_data(tag: str):
    import json
    import subprocess
    from collections import defaultdict
    from pathlib import Path

    from .edition import EDITIONS
    from .koreader import koreader_file

    subprocess.run(
        ["gh", "release", "download", tag, "-D", "build", "-p", "*.json"],
        check=True,
    )
    assets = defaultdict(list)
    gloss_codes = {}
    ko_data = []
    for json_path in Path("build").glob("*.json"):
        with json_path.open() as f:
            data = json.load(f)
            gloss_code = json_path.stem
            gloss_name = EDITIONS[gloss_code]["lang"]
            for dict_info in data:
                assets[gloss_name].append(
                    {
                        "name": dict_info["bookname"],
                        "url": f"https://github.com/xxyzz/wiktionary_stardict/releases/download/{tag}/{dict_info['filename']}",
                        "entries": dict_info["wordcount"],
                        "size": convert_size(dict_info["filesize"]),
                    }
                )
                gloss_codes[gloss_name] = gloss_code
            ko_data.extend(data)
    koreader_file(ko_data)
    return json.dumps({"date": tag, "assets": assets, "gloss_codes": gloss_codes})


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
