def koreader_file(all_data: list[dict[str, str]]):
    # https://github.com/koreader/koreader/blob/master/frontend/ui/data/dictionaries.lua
    import pycountry

    with open("build/koreader", "w") as out_f:
        data_list = []
        for data in all_data:
            lang_in, lang_out = data["codes"].rsplit("-", 1)
            lang_in_code = (
                pycountry.languages.get(alpha_2=lang_in).alpha_3
                if len(lang_in) == 2
                else lang_in
            )
            lang_out_code = (
                "eng"
                if lang_out == "simple"
                else pycountry.languages.get(alpha_2=lang_out).alpha_3
            )
            data_list.append(
                {
                    "license": "GPLv3+ and CC BY-SA 4.0",
                    "url": f"https://github.com/xxyzz/wiktionary_stardict/releases/latest/download/{data['codes']}.tar.zst",
                    "lang_in": lang_in_code,
                    "lang_out": lang_out_code,
                    "name": data["name"],
                    "entries": data["entries"],
                }
            )
        for data in sorted(data_list, key=lambda data: data["name"]):
            out_f.write("    {\n")
            for key in ["name", "lang_in", "lang_out", "entries", "license", "url"]:
                if key != "entries":
                    out_f.write(f'        {key} = "{data[key]}",\n')
                else:
                    out_f.write(f"        {key} = {data[key]},\n")
            out_f.write("    },\n")
