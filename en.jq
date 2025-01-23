select(.lang_code == $lang_code and has("senses") and has("pos") and .pos != "number") |
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
    ($forms | join("|")) + "\n<h3>" + .pos + "</h3>" + $ipa + "<ol>" + $list + "</ol>\n"
  else "" end