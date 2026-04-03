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
        data["forms"] = list(
            dict.fromkeys(f.strip() for f in data["forms"] if f.strip() != "")
        )
    if zim is not None:
        for data in json_result:
            extra_forms = []
            for zim_page in data["zim_pages"]:
                page_text = get_zim_page(zim, zim_page)
                if page_text != "":
                    try:
                        zim_doc = proc.parse_xml(xml_text=page_text)
                        zim_result = zim_xsl_exec.transform_to_string(xdm_node=zim_doc)
                        extra_forms.extend(json.loads(zim_result))
                    except PySaxonApiError as err:
                        logger.error(f"Error in page: {zim_page} {err}")
            extra_forms = [f.strip() for f in extra_forms if f.strip() != ""]
            data["forms"] = list(dict.fromkeys(data["forms"] + extra_forms))
    return json_result


def build(args):
    from concurrent.futures import ProcessPoolExecutor
    from functools import partial
    from os import process_cpu_count

    from .db import create_indexes, init_db, insert_data
    from .edition import EDITIONS
    from .snapshot import (
        decompress_chunk,
        download_chunk,
        get_chunk_zst_path,
        get_snapshot_chunks,
    )
    from .stardict import create_stardict
    from .zim import download_zim

    xsl_path = get_xsl_path(args.edition, "main.xsl")
    edition_lang = EDITIONS[args.edition]["lang"]
    snapshot_identifier = f"{args.edition}wiktionary_namespace_0"
    snapshot_date, chunk_num = get_snapshot_chunks(snapshot_identifier)
    conn_dict = {}
    zim_path = None
    zim_xsl_path = None
    if "zim_xsl" in EDITIONS[args.edition]:
        zim_path = download_zim(args.edition)
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
                        if data["lang"] not in conn_dict:
                            conn_dict[data["lang"]] = init_db(data["lang"])
                        insert_data(
                            conn_dict[data["lang"]],
                            data["def"],
                            data["forms"],
                            data.get("form_of_only", False),
                            data.get("form_of_targets", []),
                            data.get("images", []),
                        )
        ndjson_path.unlink()
        logger.info(f"chunk {chunk_identifier} done")

    for conn in conn_dict.values():
        create_indexes(conn)
    with ProcessPoolExecutor(
        max_workers=min(len(conn_dict), process_cpu_count())
    ) as executor:
        list(
            executor.map(
                partial(
                    create_stardict, edition_lang, args.edition, snapshot_date, zim_path
                ),
                conn_dict.keys(),
            )
        )
    if zim_path is not None:
        zim_path.unlink()


def main():
    import argparse

    from .edition import EDITIONS
    from .page import create_github_page

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(required=True)
    build_parser = subparsers.add_parser("build")
    build_parser.add_argument("edition", choices=EDITIONS.keys())
    build_parser.set_defaults(func=build)
    page_parser = subparsers.add_parser("page")
    page_parser.add_argument("tag")
    page_parser.set_defaults(func=create_github_page)
    args = parser.parse_args()
    args.func(args)
