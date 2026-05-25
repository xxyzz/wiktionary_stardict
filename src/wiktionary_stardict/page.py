def convert_release_data(tag: str):
    import json
    import subprocess
    from collections import defaultdict

    from mediawiki_langcodes import code_to_name

    from .edition import EDITIONS, ZH_CODE_TO_NAME

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
    screenshots = {}
    for asset in release_data["assets"]:
        if not asset["name"].endswith(".tar.zst"):
            continue
        name = asset["name"].removesuffix(".tar.zst")
        lemma_code, gloss_code = name.split("-", 1)
        gloss_lang = EDITIONS[gloss_code]["lang"]
        if gloss_code == "zh" and lemma_code in ZH_CODE_TO_NAME:
            lemma_lang = ZH_CODE_TO_NAME[lemma_code]
        else:
            lemma_lang = code_to_name(lemma_code, gloss_code)
        lemma_lang = lemma_lang[0].upper() + lemma_lang[1:]
        assets[gloss_lang].append(
            {"name": f"{lemma_lang}-{gloss_lang}", "url": asset["url"]}
        )
        screenshots[gloss_lang] = f"{gloss_code}.png"
    date = release_data["publishedAt"]
    return json.dumps(
        {"date": date[: date.index("T")], "assets": assets, "screenshots": screenshots}
    )


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

    from .koreader import koreader_file
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
    koreader_file(args.tag)
