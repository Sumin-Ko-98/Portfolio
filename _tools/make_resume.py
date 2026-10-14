"""공개용 이력서 PDF: 최종 포트폴리오 PDF 2쪽(About Me)에서 생년월일 · 쪽번호를 실제로 삭제.

실행:  python _tools/make_resume.py <최종 포트폴리오 PDF 경로>
출력:  assets/Sumin_Ko_Resume.pdf  (전화번호는 원래 2쪽에 없음 · 이메일만 남음)
"""
import os, sys
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = pymupdf.open(sys.argv[1])
doc = pymupdf.open()
doc.insert_pdf(src, from_page=1, to_page=1)
page = doc[0]

targets = []
for x0, y0, x1, y1, text, *_ in page.get_text("blocks"):
    t = text.strip()
    if t.startswith("Birth date") or "1998" in t:
        targets.append(pymupdf.Rect(x0, y0, x1, y1))
    elif t == "02":  # 쪽번호
        targets.append(pymupdf.Rect(x0, y0, x1, y1))
if not targets:
    sys.exit("생년월일 블록을 찾지 못함")
for r in targets:
    page.add_redact_annot(r + (-2, -2, 2, 2), fill=False)
page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE, graphics=pymupdf.PDF_REDACT_LINE_ART_NONE)

doc.set_metadata({"title": "Sumin Ko — Resume", "author": "Sumin Ko", "subject": "Product Designer",
                  "creator": "", "producer": "", "keywords": ""})
out = os.path.join(ROOT, "assets", "Sumin_Ko_Resume.pdf")
doc.save(out, garbage=4, deflate=True, clean=True)

check = pymupdf.open(out)
txt = "".join(p.get_text() for p in check)
meta = " ".join(str(v) for v in check.metadata.values())
print("pages:", len(check), "| size:", os.path.getsize(out) // 1024, "KB")
print("'1998' in text:", "1998" in txt, "| 'Birth' in text:", "Birth" in txt, "| '1998' in metadata:", "1998" in meta)
print("phone in text:", any(k in txt for k in ("010", "5660", "+82")), "| email in text:", "ssom98@naver.com" in txt)
raw = open(out, "rb").read()
print("'1998' bytes in file:", b"1998" in raw)
