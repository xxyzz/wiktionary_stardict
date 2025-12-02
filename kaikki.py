import sys

if __name__ == "__main__":
    import requests
    from datetime import datetime

    gloss_lang = sys.argv[1]
    url = (
        "https://kaikki.org/dictionary/raw-wiktextract-data.jsonl.gz"
        if gloss_lang == "en"
        else f"https://kaikki.org/{gloss_lang}wiktionary/raw-wiktextract-data.jsonl.gz"
    )
    r = requests.head(url)
    date = datetime.strptime(r.headers["Last-Modified"], "%a, %d %b %Y %H:%M:%S %Z")
    print(date.strftime("%Y-%m-%d"))
