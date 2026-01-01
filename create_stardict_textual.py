import sys
import json
from datetime import date
from pathlib import Path

from lxml import etree
from lxml.builder import E


if __name__ == "__main__":
    # https://github.com/huzheng001/stardict-3/blob/master/dict/doc/TextualDictionaryFileFormat
    # https://github.com/huzheng001/stardict-3/blob/master/dict/doc/stardict-textual-dict-example.xml
    input_path = Path(sys.argv[1])
    with input_path.open() as f:
        root = etree.Element("stardict")
        info = etree.SubElement(root, "info")
        version = etree.SubElement(info, "version")
        version.text = "3.0.0"
        bookname = etree.SubElement(info, "bookname")
        bookname.text = "Wiktionary " + input_path.stem
        date_ele = etree.SubElement(info, "date")
        date_ele.text = date.today().isoformat()
        desc = etree.SubElement(info, "description")
        desc.text = "Data source: https://kaikki.org, Wiktionary license: CC BY-SA 4.0 https://creativecommons.org/licenses/by-sa/4.0/"
        website = etree.SubElement(info, "website")
        website.text = "https://github.com/xxyzz/wiktionary_stardict"
        contents = etree.SubElement(root, "contents")
        for line in f:
            line = line.strip()
            if line == "":
                continue
            data = json.loads(line)
            article = etree.SubElement(contents, "article")
            key = etree.SubElement(article, "key")
            key.text = data["word"]
            for syn in data["forms"]:
                syn_ele = etree.SubElement(article, "synonym")
                syn_ele.text = syn
            def_ele = etree.SubElement(article, "definition", type="h")
            def_ele.text = f"<h3>{data['pos']}</h3>"
            if data["ipa"] is not None:
                def_ele.text += f"<span>{data['ipa']}</span>"
            top_ol_ele = etree.Element("ol")
            gloss_li_dict = {}
            for sense in data["senses"]:
                current_ol = top_ol_ele
                for index, gloss in enumerate(sense["glosses"]):
                    if gloss not in gloss_li_dict:
                        if index == 0:
                            gloss_li_dict.clear()
                        li_ele = etree.SubElement(current_ol, "li")
                        li_ele.text = gloss
                        gloss_li_dict[gloss] = li_ele
                        current_ol = etree.SubElement(li_ele, "ol")
                    else:
                        current_ol = gloss_li_dict[gloss].find("ol")
                if sense["example"] is not None:
                    offsets = sense["example"].get("bold_text_offsets")
                    if offsets is None:
                        gloss_li_dict[gloss].insert(
                            0, E.dl(E.dd(E.i(sense["example"]["text"])))
                        )
                    else:
                        i_ele = E.i("")
                        last_pos = 0
                        last_b = None
                        for start, end in offsets:
                            if last_b is None:
                                i_ele.text += sense["example"]["text"][last_pos:start]
                            else:
                                last_b.tail += sense["example"]["text"][last_pos:start]
                            b_ele = etree.SubElement(i_ele, "b")
                            b_ele.text = sense["example"]["text"][start:end]
                            b_ele.tail = ""
                            last_pos = end
                            last_b = b_ele
                        last_b.tail += sense["example"]["text"][last_pos:]
                        gloss_li_dict[gloss].insert(0, E.dl(E.dd(i_ele)))

            for ol_ele in top_ol_ele.xpath(".//ol"):
                if len(ol_ele) == 0:
                    ol_ele.getparent().remove(ol_ele)
            def_ele.text += etree.tostring(top_ol_ele, encoding="unicode")

        with open(f"{input_path.stem}.xml", "wb") as out_f:
            etree.ElementTree(root).write(
                out_f, pretty_print=True, xml_declaration=True, encoding="UTF-8"
            )
