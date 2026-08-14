from utils import XMLTestCase


class ThPOSTestCase(XMLTestCase):
    edition = "th"

    def test_th_page(self):
        self.assertTransformEqual(
            """<!DOCTYPE html>
<html>
<head><title>หนังสือ</title></head>
<body>
<section><h2 id="ภาษาไทย">ภาษาไทย</h2>
<section><h3 id="คำนาม">คำนาม</h3>
<p><span class="headword-line" data-mw='{"parts":[{"template":{"target":{"wt":"th-noun"}}}]}'><strong class="Thai headword" lang="th">หนังสือ</strong> (<i>คำลักษณนาม</i> <b class="Thai" lang="th"><a>เล่ม</a></b> <i>หรือ</i> <b class="Thai" lang="th"><a>ฉบับ</a></b>)</span></p>
<ol><li>เครื่องหมายใช้ขีดเขียนแทนเสียงหรือคำพูด
<dl><dd><div class="h-usage-example"><i class="Thai mention e-example" lang="th">อ่าน<b>หนังสือ</b></i></div><span class="mw-empty-elt"></span></dd>
<dd><div class="h-usage-example"><i class="Thai mention e-example" lang="th">เขียน<b>หนังสือ</b></i></div></dd></dl></li></ol>
</section></section></body></html>""",
            [
                {
                    "def": """<section class="mw-parser-output" dir="ltr" lang="th">
<h4>คำนาม</h4>
<p><span class="headword-line"><strong class="Thai headword" lang="th">หนังสือ</strong> (<i>คำลักษณนาม</i> <b class="Thai" lang="th">เล่ม</b> <i>หรือ</i> <b class="Thai" lang="th">ฉบับ</b>)</span></p>
<ol><li>เครื่องหมายใช้ขีดเขียนแทนเสียงหรือคำพูด
<dl><dd><div class="h-usage-example"><i class="Thai mention e-example" lang="th">อ่าน<b>หนังสือ</b></i></div><span class="mw-empty-elt"></span></dd></dl></li></ol>
</section>""",
                    "forms": ["หนังสือ"],
                    "ids": ["ภาษาไทย", "คำนาม"],
                    "lang": "ภาษาไทย",
                }
            ],
        )
