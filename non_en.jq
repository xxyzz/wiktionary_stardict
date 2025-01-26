select(
  .lang_code == $lang_code and
  has("senses") and
  has("pos") and .pos != "num" and
  (.tags // [] | index("form-of") | not)) |
  ([.word] + [(.forms//[])[].form] | unique) as $forms |
  ([.senses[] | select(has("glosses") and (.tags // [] | index("form-of") | not)) |
    "<li>" + (.glosses | join(" ")) +
        (if .examples | length > 0 then
          "<dl><dd><i>" + (.examples | map(.text) | sort_by(length) | first) + "</i></dd></dl>"
         else "" end) + "</li>"] | join("")) as $list |
  (.sounds // [] | map(select(.ipa or .zh_pron)) | first | if . then "<span>" + (.ipa // .zh_pron) + "</span>" else "" end) as $ipa |
  if $list | length > 0 then
    {word, forms: $forms[1:], content: ("<h3>" + .pos_title + "</h3>" + $ipa + "<ol>" + $list + "</ol>")}
  else empty end
