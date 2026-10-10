def get_math_svg(session, tex: str) -> str:
    r = session.post("http://127.0.0.1:8080/tex2svg", data=tex)
    if r.ok:
        return r.text
    return ""


def start_node():
    import subprocess

    subprocess.Popen(["node", "src/wiktionary_stardict/mathjax.js"])


def shutdown_node():
    import requests

    requests.get("http://127.0.0.1:8080/shutdown")
