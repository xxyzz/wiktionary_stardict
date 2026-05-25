def koreader_file(tag):
    # https://github.com/koreader/koreader/blob/master/frontend/ui/data/dictionaries.lua
    import json
    import shutil
    import tarfile
    from pathlib import Path
    from subprocess import run

    import pycountry

    with open("build/release.json") as f:
        release_data = json.load(f)
    with open("build/koreader", "w") as out_f:
        all_data = []
        for asset in release_data["assets"]:
            if not asset["name"].endswith(".tar.zst"):
                continue
            run(
                ["gh", "release", "download", tag, "-p", asset["name"]],
                check=True,
            )
            zst_path = Path("build") / asset["name"]
            dict_folder = Path("build") / zst_path.name.removesuffix(".tar.zst")
            dict_folder.mkdir(exist_ok=True)
            with tarfile.open(name=zst_path, mode="r") as tar_f:
                tar_f.extractall(path=dict_folder)
            zst_path.unlink()
            with open(dict_folder / f"{dict_folder.name}.ifo") as f:
                lang_in, lang_out = dict_folder.name.split("-")
                lang_in_code = (
                    pycountry.languages.get(alpha_2=lang_in).alpha_3
                    if len(lang_in) == 2
                    else lang_in
                )
                dict_data = {
                    "license": "GPLv3+ and CC BY-SA 4.0",
                    "url": f"https://github.com/xxyzz/wiktionary_stardict/releases/latest/download/{asset['name']}",
                    "lang_in": lang_in_code,
                    "lang_out": pycountry.languages.get(alpha_2=lang_out).alpha_3,
                }
                for line in f:
                    if line.startswith("bookname="):
                        dict_data["name"] = line.removeprefix("bookname=").strip()
                    elif line.startswith("wordcount="):
                        dict_data["entries"] = int(line.removeprefix("wordcount="))
                all_data.append(dict_data)
            shutil.rmtree(dict_folder)
        for data in sorted(all_data, key=lambda data: data["name"]):
            out_f.write("    {\n")
            for key in ["name", "lang_in", "lang_out", "entries", "license", "url"]:
                if key != "entries":
                    out_f.write(f'        {key} = "{data[key]}",\n')
                else:
                    out_f.write(f"        {key} = {data[key]},\n")
            out_f.write("    },\n")
