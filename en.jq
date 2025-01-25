# https://github.com/tatuylonen/wiktextract/blob/master/src/wiktextract/extractor/en/section_titles.py
def pos_str:
  if . == "abbrev" then "Abbreviation"
  elif . == "adj_noun" then "Adjectival noun"
  elif . == "adj_verb" then "Adjectival verb"
  elif . == "adj" then "Adjective"
  elif . == "adv" then "Adverb"
  elif . == "adv_phrase" then "Adverbial phrase"
  elif . == "combining_form" then "Combining form"
  elif . == "conj" then "Conjunction"
  elif . == "det" then "Determiner"
  elif . == "intj" then "Interjection"
  elif . == "postp" then "Postposition"
  elif . == "prep" then "Preposition"
  elif . == "prep_phrase" then "Prepositional phrase"
  elif . == "pron" then "Pronoun"
  elif . == "name" then "Proper noun"
  elif . == "punct" then "Punctuation mark"
  else . | (.[0:1] | ascii_upcase) + .[1:]
  end;

select(.lang_code == $lang_code and has("senses") and has("pos") and .pos != "num") |
  ([.word] + [(.forms//[])[].form] | unique) as $forms |
  ([.senses[] | select(.tags | index("form-of") | not) |
    .glosses[-1] as $gloss |
      "<li>" + $gloss +
        (if .examples | length > 0 then
          "<dl><dd><i>" + (.examples[0].text) + "</i></dd></dl>"
         else "" end) +
      "</li>"] | join("")) as $list |
  (.sounds // [] | map(select(has("ipa") or has("zh_pron"))) | first |
    if .ipa then "<span>" + .ipa + "</span>"
    elif .zh_pron then "<span>" + .zh_pron + "</span>"
    else "" end) as $ipa |
  if $list | length > 0 then
    ($forms | join("|")) + "\n<h3>" + (.pos | pos_str) + "</h3>" + $ipa + "<ol>" + $list + "</ol>\n"
  else "" end
