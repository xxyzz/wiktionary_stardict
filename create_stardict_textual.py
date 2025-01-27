import sys
import json
from datetime import date
from pathlib import Path

from lxml import etree


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
            def_ele.text = data["content"]

        with open(f"{input_path.stem}.xml", "wb") as out_f:
            etree.ElementTree(root).write(
                out_f, pretty_print=True, xml_declaration=True, encoding="UTF-8"
            )
