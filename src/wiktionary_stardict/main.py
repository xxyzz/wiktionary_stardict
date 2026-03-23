import logging
from pathlib import Path

logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


def get_xsl_path(edition: str, file: str) -> str:
    from importlib.resources import files

    return str(files("wiktionary_stardict") / "xslt" / edition / file)


def init_worker(xsl_path: str, zim_path: Path | None, zim_xsl_path: Path | None):
    from saxonche import PySaxonProcessor

    from .zim import open_zim

    global proc, executable, zim, zim_xsl_exec
    proc = PySaxonProcessor(license=False)
    xsltproc = proc.new_xslt30_processor()
    executable = xsltproc.compile_stylesheet(stylesheet_file=xsl_path)
    if zim_path is not None:
        zim = open_zim(zim_path)
        zim_xsl_exec = xsltproc.compile_stylesheet(stylesheet_file=zim_xsl_path)
    else:
        zim = None
        zim_xsl_exec = None


def transform(line: str) -> list[list[str]]:
    import json

    from saxonche import PySaxonApiError

    from .zim import get_zim_page

    data = json.loads(line)
    html = data["html"]
    try:
        document = proc.parse_xml(xml_text=html)
        result = executable.transform_to_string(xdm_node=document)
    except PySaxonApiError as err:
        logger.error(f"Error in page: {data['name']} {err}")
        return []
    json_result = json.loads(result)
    if json_result is None:
        logger.info(f"None result in page {data['name']}")
        return []
    for data in json_result:
        data["forms"] = list({f.strip() for f in data["forms"] if f.strip() != ""})
    if zim is not None:
        for data in json_result:
            extra_forms = set()
            for zim_page in data["zim_pages"]:
                page_text = get_zim_page(zim, zim_page)
                if page_text != "":
                    try:
                        zim_doc = proc.parse_xml(xml_text=page_text)
                        zim_result = zim_xsl_exec.transform_to_string(xdm_node=zim_doc)
                        extra_forms |= set(json.loads(zim_result))
                    except PySaxonApiError as err:
                        logger.error(f"Error in page: {zim_page} {err}")
            extra_forms = {f.strip() for f in extra_forms if f.strip() != ""}
            data["forms"] = list(set(data["forms"]) | extra_forms)
    return json_result


def main():
    import argparse
    from concurrent.futures import ProcessPoolExecutor

    from pyglossary.glossary_v2 import Glossary

    from .edition import EDITIONS
    from .snapshot import (
        decompress_chunk,
        download_chunk,
        get_chunk_zst_path,
        get_snapshot_chunks,
    )
    from .stardict import add_entry, create_glossary, create_stardict
    from .zim import download_zim, open_zim

    parser = argparse.ArgumentParser()
    parser.add_argument("edition", choices=EDITIONS.keys())
    args = parser.parse_args()
    xsl_path = get_xsl_path(args.edition, "main.xsl")
    edition_lang = EDITIONS[args.edition]["lang"]
    snapshot_identifier = f"{args.edition}wiktionary_namespace_0"
    snapshot_date, chunk_num = get_snapshot_chunks(snapshot_identifier)
    glos_dict = {}
    add_files = {}
    Glossary.init()
    zim = None
    zim_path = None
    zim_xsl_path = None
    if "zim_xsl" in EDITIONS[args.edition]:
        zim_path = download_zim(args.edition)
        zim = open_zim(zim_path)
        zim_xsl_path = get_xsl_path(args.edition, EDITIONS[args.edition]["zim_xsl"])

    for chunk_idx in range(chunk_num):
        chunk_identifier = f"{snapshot_identifier}_chunk_{chunk_idx}"
        chunk_zst_path = get_chunk_zst_path(chunk_identifier)
        if not chunk_zst_path.exists():
            download_chunk(chunk_identifier, chunk_zst_path)
        ndjson_path = decompress_chunk(chunk_zst_path)
        logger.info(f"start chunk {chunk_identifier}")
        with ndjson_path.open() as f:
            with ProcessPoolExecutor(
                initializer=init_worker, initargs=(xsl_path, zim_path, zim_xsl_path)
            ) as executor:
                for results in executor.map(transform, f, chunksize=100):
                    for data in results:
                        if data["lang"] not in glos_dict:
                            add_files[data["lang"]] = set()
                            glos = create_glossary(
                                data["lang"], edition_lang, snapshot_date
                            )
                            glos_dict[data["lang"]] = glos
                        add_entry(
                            glos_dict[data["lang"]],
                            args.edition,
                            data["forms"],
                            data["def"],
                            data["images"],
                            add_files[data["lang"]],
                            zim,
                        )
        chunk_zst_path.unlink()
        ndjson_path.unlink()
        logger.info(f"chunk {chunk_identifier} done")
    if zim_path is not None:
        zim_path.unlink()

    for lemma_lang, glos in glos_dict.items():
        create_stardict(glos, lemma_lang, edition_lang, args.edition)
