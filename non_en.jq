select(
  .lang_code == $lang_code and
  has("senses") and
  has("pos") and .pos != "num" and
  (.tags // [] | index("form-of") or index("alt-of") | not)) |
  ([.word] + [(.forms//[])[].form] | unique) as $forms |
  (.senses | map(select(has("glosses") and (.tags // [] | index("form-of") or index("alt-of") | not)) |
    {glosses, example: (.examples // [] | map(select(has("ref") | not) | .text) | sort_by(length) | first)})) as $senses |
  (.sounds // [] | map(select(.ipa or .zh_pron)) | first | if . then .ipa // .zh_pron else null end) as $ipa |
  if $senses | length > 0 then
    {word, pos: .pos_title, forms: $forms[1:], $ipa, $senses}
  else empty end
