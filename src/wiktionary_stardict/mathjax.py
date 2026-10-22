# https://www.mediawiki.org/wiki/Extension:Math/Syntax
# https://github.com/wikimedia/mediawiki-extensions-Math/blob/master/src/MathRenderer.php
def get_math_svg(session, data: dict) -> str:
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

    subprocess.Popen(["node", "src/wiktionary_stardict/mathjax.js"])


def shutdown_node():
    import requests

    requests.get("http://127.0.0.1:8080/shutdown")
