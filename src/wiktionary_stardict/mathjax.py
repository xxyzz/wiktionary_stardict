def get_math_svg(tex: str) -> str:
    import requests

    r = requests.post("http://127.0.0.1:8080/tex2svg", data=tex)
    if r.ok:
        return r.text
    return ""


def start_deno():
    import subprocess

    subprocess.Popen(
        ["deno", "--allow-net=127.0.0.1", "src/wiktionary_stardict/mathjax.ts"]
    )


def shutdown_deno():
    import requests

    requests.get("http://127.0.0.1:8080/shutdown")
