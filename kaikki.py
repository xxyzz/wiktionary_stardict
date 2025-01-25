import sys

if __name__ == "__main__":
    import re

    import requests
    from lxml import etree

    gloss_lang = sys.argv[1]
    url = (
        "https://kaikki.org/dictionary/rawdata.html"
        if gloss_lang == "en"
        else f"https://kaikki.org/{gloss_lang}wiktionary/rawdata.html"
    )
    r = requests.get(url)
    root = etree.HTML(r.text)
    text = root.xpath("body/div[last()]/p[1]/text()")[0]
    m = re.search(r"(\d{4}-\d{2}-\d{2})", text)
    print(m.group(1))
