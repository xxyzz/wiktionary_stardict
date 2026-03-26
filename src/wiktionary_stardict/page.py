def convert_release_data(tag: str):
    import json
    import subprocess
    from collections import defaultdict

    p = subprocess.run(
        ["gh", "release", "view", tag, "--json", "assets,publishedAt"],
        check=True,
        text=True,
        capture_output=True,
    )
    gh_data = json.loads(p.stdout)

    assets = defaultdict(list)
    for asset in gh_data["assets"]:
        if not asset["name"].endswith(".tar.zst"):
            continue
        name = asset["name"].removesuffix(".tar.zst").replace("_", " ")
        edition = name.split("-", 1)[-1]
        assets[edition].append({"name": name, "url": asset["url"]})
    date = gh_data["publishedAt"]
    return json.dumps({"date": date[: date.index("T")], "assets": assets})


def create_github_page(args):
    from importlib.resources import files
    from pathlib import Path

    from saxonche import PySaxonProcessor

    proc = PySaxonProcessor(license=False)
    xsltproc = proc.new_xslt30_processor()
    xsltproc.set_parameter(
        "data", proc.make_string_value(convert_release_data(args.tag))
    )
    executable = xsltproc.compile_stylesheet(
        stylesheet_file=str(files("wiktionary_stardict") / "xslt" / "github_page.xsl")
    )
    out_path = Path("_site/index.html")
    out_path.parent.mkdir(exist_ok=True)
    with out_path.open("w") as f:
        doc = proc.parse_xml(xml_text="<root/>")
        f.write(executable.transform_to_string(xdm_node=doc))
