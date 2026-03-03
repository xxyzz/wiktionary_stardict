import logging
from pathlib import Path

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
    html = data["article_body"]["html"]
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


def write_dict_info(f, lemma_lang: str, gloss_lang: str, snapshot_date: str):
    from datetime import date

    f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<stardict>
<info>
    <version>3.0.0</version>
    <bookname>Wiktionary {lemma_lang}-{gloss_lang}</bookname>
    <author>xxyzz</author>
    <website>https://github.com/xxyzz/wiktionary_stardict</website>
    <description>Snapshot {snapshot_date}. Wiktionary license CC BY-SA 4.0</description>
    <date>{date.today().isoformat()}</date>
</info>
<contents>""")


def create_stardict(input_path: Path, output_path: Path):
    import os
    import shutil
    import tarfile
    from compression import zstd

    from pyglossary.glossary_v2 import ConvertArgs, Glossary

    Glossary.init()
    glos = Glossary()
    glos.convert(
        ConvertArgs(
            inputFilename=str(input_path),
            outputFilename=str(output_path),
            inputFormat="StardictTextual",
            outputFormat="StardictMergeSyns",
        )
    )
    with tarfile.open(
        name=output_path.with_suffix(".tar.zst"),
        mode="x:zst",
        options={
            zstd.CompressionParameter.compression_level: 19,
            zstd.CompressionParameter.nb_workers: os.process_cpu_count(),
        },
    ) as tar:
        tar.add(output_path, arcname=".")
    input_path.unlink()
    shutil.rmtree(output_path)


def main():
    import argparse
    from concurrent.futures import ProcessPoolExecutor

    from .snapshot import (
        decompress_chunk,
        download_chunk,
        get_access_token,
        get_chunk_ndjson_path,
        get_chunk_tar_path,
        get_snapshot_chunks,
    )

    parser = argparse.ArgumentParser()
    parser.add_argument("edition", choices=EDITIONS.keys())
    args = parser.parse_args()
    xsl_path = get_xsl_path(args.edition)
    edition_lang = EDITIONS[args.edition]
    snapshot_identifier = f"{args.edition}wiktionary_namespace_0"
    access_token = get_access_token()
    snapshot_date, chunk_identifiers = get_snapshot_chunks(
        access_token, snapshot_identifier
    )
    out_files = {}
    out_paths = []
    for chunk_identifier in chunk_identifiers:
        chunk_tar_path = get_chunk_tar_path(chunk_identifier)
        if not chunk_tar_path.exists():
            download_chunk(
                access_token, snapshot_identifier, chunk_identifier, chunk_tar_path
            )
        decompress_chunk(chunk_tar_path)
        ndjson_path = get_chunk_ndjson_path(chunk_identifier)
        logger.info(f"start chunk {chunk_identifier}")
        with ndjson_path.open() as f:
            with ProcessPoolExecutor(
                initializer=init_worker, initargs=(xsl_path,)
            ) as executor:
                for results in executor.map(transform, f, chunksize=100):
                    for lemma_lang, article in results:
                        if lemma_lang not in out_files:
                            out_path = Path(f"build/{lemma_lang}-{edition_lang}.xml")
                            out_files[lemma_lang] = out_path.open("w")
                            write_dict_info(
                                out_files[lemma_lang],
                                lemma_lang,
                                edition_lang,
                                snapshot_date,
                            )
                            out_paths.append(out_path)
                        else:
                            out_files[lemma_lang].write(article)
        chunk_tar_path.unlink()
        ndjson_path.unlink()
        logger.info(f"chunk {chunk_identifier} done")

    for f in out_files.values():
        f.write("</contents>\n</stardict>")
        f.close()
    for out_path in out_paths:
        out_path.with_suffix("").mkdir(exist_ok=True)
        create_stardict(out_path, out_path.with_suffix(""))
