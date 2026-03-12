import logging

EDITIONS = {"en": "English"}
logging.basicConfig(format="%(asctime)s %(levelname)s: %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)


def get_xsl_path(edition: str) -> str:
    from importlib.resources import files

    return str(files("wiktionary_stardict") / "xslt" / edition / "main.xsl")


def init_worker(xsl_path: str):
    from saxonche import PySaxonProcessor

    global proc, executable
    proc = PySaxonProcessor(license=False)
    xsltproc = proc.new_xslt30_processor()
    executable = xsltproc.compile_stylesheet(stylesheet_file=xsl_path)


def transform(line: str) -> list[list[str]]:
    import json

    from saxonche import PySaxonApiError

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
    return json_result


def main():
    import argparse
    from concurrent.futures import ProcessPoolExecutor

    from pyglossary.glossary_v2 import Glossary

    from .snapshot import (
        decompress_chunk,
        download_chunk,
        get_chunk_zst_path,
        get_snapshot_chunks,
    )
    from .stardict import add_entry, create_glossary, create_stardict

    parser = argparse.ArgumentParser()
    parser.add_argument("edition", choices=EDITIONS.keys())
    args = parser.parse_args()
    xsl_path = get_xsl_path(args.edition)
    edition_lang = EDITIONS[args.edition]
    snapshot_identifier = f"{args.edition}wiktionary_namespace_0"
    snapshot_date, chunk_identifiers = get_snapshot_chunks(snapshot_identifier)
    glos_dict = {}
    add_files = {}
    Glossary.init()
    for chunk_identifier in chunk_identifiers:
        chunk_zst_path = get_chunk_zst_path(chunk_identifier)
        if not chunk_zst_path.exists():
            download_chunk(chunk_identifier, chunk_zst_path)
        ndjson_path = decompress_chunk(chunk_zst_path)
        logger.info(f"start chunk {chunk_identifier}")
        with ndjson_path.open() as f:
            with ProcessPoolExecutor(
                initializer=init_worker, initargs=(xsl_path,)
            ) as executor:
                for results in executor.map(transform, f, chunksize=100):
                    for lemma_lang, forms, definition, images in results:
                        if lemma_lang not in glos_dict:
                            add_files[lemma_lang] = set()
                            glos = create_glossary(
                                lemma_lang, edition_lang, snapshot_date
                            )
                            glos_dict[lemma_lang] = glos
                        add_entry(
                            glos_dict[lemma_lang],
                            args.edition,
                            forms,
                            definition,
                            images,
                            add_files[lemma_lang],
                        )
        chunk_zst_path.unlink()
        ndjson_path.unlink()
        logger.info(f"chunk {chunk_identifier} done")

    for lemma_lang, glos in glos_dict.items():
        create_stardict(glos, lemma_lang, edition_lang, args.edition)
