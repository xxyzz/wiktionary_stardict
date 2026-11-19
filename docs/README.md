# How to add a new Wiktionary edition

## Assess Wiktionary quality

First make sure the new edition is actively edited and has acceptable data quality, check the following links and search some words in the wiki.

- [active editors](https://stats.wikimedia.org/#/en.wiktionary.org/contributing/active-editors/normal|line|2-year|~total|monthly)
- [user edits](https://stats.wikimedia.org/#/en.wiktionary.org/contributing/user-edits/normal|bar|2-year|(page_type)~content*non-content|monthly)
- [recent changes](https://en.wiktionary.org/wiki/Special:RecentChanges?hidebots=1&hidecategorization=1&hideWikibase=1&limit=500&days=30&enhanced=1&urlversion=2)
- [lemmas count](https://en.wiktionary.org/wiki/Category:English_lemmas)

## Find new edition's wikitext layout

Every edition's layout is different, [here](https://en.wiktionary.org/wiki/Wiktionary:Entry_layout) is the English Wiktionary entry layout.

## Download snapshot

Add [some data](https://github.com/xxyzz/snapshot/blob/master/src/snapshot/edition.py) and [enable](https://github.com/xxyzz/snapshot/blob/master/.github/workflows/snapshot.yml) new edition in the [snapshot](https://github.com/xxyzz/snapshot/) repo.

## Add language data

Add language names and codes used in the new edition to [mediawiki_langcodes](https://github.com/xxyzz/mediawiki_langcodes/tree/master/build_script).

## Choose languages

Enable languages that have sufficient lemmas in [config.xsl](https://github.com/xxyzz/wiktionary_stardict/blob/master/src/wiktionary_stardict/xslt/en/config.xsl) file.

## Install dependencies

```console
pacman -Syu --needed uv bubblewrap python-libseccomp lilypond nodejs npm github-cli
npm install
uv sync
```

Because `libseccomp` doesn't have PyPI package, run this command to use the system package or build the wheel file from source then run `uv pip install`:

```console
python -m venv --system-site-packages .venv
```

## Implement XSLT templates

New template starts from the [main.xsl](https://github.com/xxyzz/wiktionary_stardict/blob/master/src/wiktionary_stardict/xslt/en/main.xsl) file and should return a JSON data for each part of speech section. Each section heading should use `<h4>`.

```json
{
  "lang": "English",
  "forms": ["booked"],
  "def": '<section class="mw-parser-output" dir="ltr" lang="en"></section>'
  "images": [],
  "form_of_targets": ["book#English"],
  "form_of_only": true,
  "ids": ["English", "Verb"],
  "links": ["book#English"],
  "svg": [],
}
```

## Add tests

Add test files for each extracted section and template change, for example: [tests/test_en_pos.py](https://github.com/xxyzz/wiktionary_stardict/blob/master/tests/test_en_pos.py).

```python
from utils import XMLTestCase


class EnPOSTestCase(XMLTestCase):
    def test_something(self):
        self.assertTransformEqual(
            "input_html", [{"forms": ["tee", "tees"], "def": "output_html"}]
        )
```

```console
uv tool run ruff check
uv tool run ruff format --fix
uv run -m unittest discover -b -s tests
```

## Add CSS

Add CSS file to the [src/wiktionary_stardict/css](https://github.com/xxyzz/wiktionary_stardict/tree/master/src/wiktionary_stardict/css) folder. If a new font is used, also add the font to [src/wiktionary_stardict/github_pages/fonts.html](https://github.com/xxyzz/wiktionary_stardict/blob/master/src/wiktionary_stardict/github_pages/fonts.html).

## Test pages

StarDict files will be created inside the "build" folder.

```console
uv run dict build en --page="book" --page="books"
```

## More documentations

* [XSL Transformations (XSLT) Version 3.0 ](https://www.w3.org/TR/xslt-30)
* [XML Path Language (XPath) 3.1](https://www.w3.org/TR/xpath-31)
* [XPath and XQuery Functions and Operators 3.1](https://www.w3.org/TR/xpath-functions)
* [MediaWiki DOM Spec](https://www.mediawiki.org/wiki/Specs/HTML)
* [Wikimedia Enterprise API](https://enterprise.wikimedia.com/docs)
* [Wikimedia REST API](https://en.wiktionary.org/w/index.php?api=wmf-rest%2Fv1&title=Special%3ARestSandbox)
* [Parsoid API](https://www.mediawiki.org/wiki/Parsoid/API)
* Parsoid HTML https://en.wiktionary.org/w/rest.php/v1/page/tee/html
* [Saxon 13 documentation](https://www.saxonica.com/documentation13/documentation.xml)
* [StarDict file format](https://github.com/huzheng001/stardict-3/blob/master/dict/doc/StarDictFileFormat)
* [CirrusSearch](https://www.mediawiki.org/wiki/Help:CirrusSearch)
