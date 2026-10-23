# https://www.mediawiki.org/wiki/Extension:Math/Syntax
# https://github.com/wikimedia/mediawiki-extensions-Math/blob/master/src/MathRenderer.php
def tex2svg(session, data: dict) -> str:
    body = data.get("body", {}).get("extsrc", "")
    attrs = data.get("attrs", {})
    if data.get("name", "") == "chem" or "chem" in attrs:
        body = r"\ce{ " + body + " }"
    layout_mode = attrs.get("display", "")
    match layout_mode:
        case "" | "block":
            body = r"{\displaystyle " + body + "}"
        case "inline":
            body = r"{\textstyle " + body + "}"
        case "linebreak":
            body = r"\[" + body + r"\]"

    r = session.post(
        "http://127.0.0.1:8080/tex2svg",
        json={"display": layout_mode == "block", "body": body},
    )
    if r.ok:
        return r.text
    return ""


def start_node():
    import subprocess
    import time

    import requests

    p = subprocess.Popen(["node", "src/wiktionary_stardict/mathjax.js"])
    for i in range(5):
        try:
            r = requests.get("http://127.0.0.1:8080/health")
            if r.ok:
                break
        except requests.exceptions.ConnectionError:
            time.sleep(0.1)
    return p


def shutdown_node(p):
    import requests

    requests.get("http://127.0.0.1:8080/shutdown")
    p.wait()
