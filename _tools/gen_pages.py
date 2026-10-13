"""케이스 스터디 상세페이지 생성기.

실행 (사이트 루트에서):  python _tools/gen_pages.py
- 내용은 _tools/pages.py 의 PAGES 에서 고친다. work/*.html 을 직접 고치면 다음 실행 때 덮어써진다.
- work/wade.html 은 이 생성기 대상이 아니다(손으로 관리).
- 이미지 크기(비율)는 파일에서 읽어서 줄 높이를 맞춘다 → pymupdf 필요.
"""
import os, sys, html
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pages import PAGES, ORDER  # noqa: E402

E = html.escape
_size_cache = {}


def size(rel):
    if rel not in _size_cache:
        p = os.path.join(ROOT, rel)
        try:
            pix = pymupdf.Pixmap(p)
            _size_cache[rel] = (pix.width, pix.height)
        except Exception:
            raise SystemExit(f"이미지 없음/열기 실패: {rel}")
    return _size_cache[rel]


def img_src(slug, f):
    return f"assets/works/{slug}/{f}"


def fig(slug, f, cap, grow=True):
    rel = img_src(slug, f)
    w, h = size(rel)
    style = f' style="flex:{w / h:.4f} 1 0"' if grow else ""
    capt = ""
    if cap:
        if " · " in cap and cap.split(" · ", 1)[0].isascii():
            k, v = cap.split(" · ", 1)
            capt = f"<figcaption><b>{E(k)}</b>{E(v)}</figcaption>"
        else:
            capt = f"<figcaption>{E(cap)}</figcaption>"
    return (f'<figure class="cs-cell reveal"{style}><div class="ph" style="aspect-ratio:{w}/{h}">'
            f'<img src="../{rel}" alt="{E(cap or f)}" loading="lazy" width="{w}" height="{h}"></div>{capt}</figure>')


def render_block(slug, b, last):
    kind = b[0]
    if kind == "text":
        _, label, lead, paras = b
        body = (f'<p class="lead">{lead}</p>' if lead else "") + "".join(f"<p>{p}</p>" for p in paras)
        return f'<section class="sec"><div class="sec__label reveal">{E(label)}</div><div class="sec__body reveal delay-1">{body}</div></section>'
    if kind == "row":
        cls = "cs-row cs-row--last" if last else "cs-row"
        if len(b) > 2 and b[2] == "narrow":
            cls += " cs-row--narrow"
        return f'<div class="{cls}">' + "".join(fig(slug, f, c) for f, c in b[1]) + "</div>"
    if kind == "grid":
        _, cols, items, more = b
        cells = "".join(fig(slug, f, c, grow=False) for f, c in items)
        if more:
            cells += f'<div class="cs-more reveal"><b>{E(more[0])}</b><span>{E(more[1])}</span></div>'
        return f'<div class="cs-grid" style="--cols:{cols}">{cells}</div>'
    if kind == "items":
        items = b[1]
        cells = "".join(
            f'<div class="cs-item reveal"><span class="cs-item__n">{E(n)}</span>'
            f'<h3 class="cs-item__t">{E(t)}</h3><p class="cs-item__d">{d}</p></div>' for n, t, d in items)
        return f'<div class="cs-items" style="--cols:{len(items)}">{cells}</div>'
    if kind == "facts":
        cells = "".join(
            f'<div class="fact reveal"><span class="fact__k">{E(k)}</span><span class="fact__v">{E(v)}</span>'
            f'<span class="fact__note">{E(n)}</span></div>' for k, v, n in b[1])
        return f'<section class="facts" style="grid-template-columns:repeat({len(b[1])},1fr)">{cells}</section>'
    if kind == "part":
        _, n, t = b
        return f'<div class="cs-part reveal"><span class="cs-part__n">{E(n)}</span><h2 class="cs-part__t">{E(t)}</h2></div>'
    if kind == "role":
        chips = "".join(f"<span>{E(r)}</span>" for r in b[1])
        return (f'<section class="sec"><div class="sec__label reveal">Role</div>'
                f'<div class="sec__body reveal delay-1"><div class="cs-role">{chips}</div></div></section>')
    raise ValueError(kind)


AWARD_LOGO = {"if": "if-gold.png", "reddot": "reddot.png", "gd": "gooddesign.png", "hci": "hci.png",
              "idea": "idea.png", "spark": "spark.png"}


def render_awards(awards):
    if not awards:
        return ""
    out = []
    for key, year, name in awards:
        if key in AWARD_LOGO:
            mark = f'<img src="../assets/awards/{AWARD_LOGO[key]}" alt="">'
        else:
            mark = f'<span class="cs-award__mark">{E(key)}</span>'
        out.append(f'<div class="cs-award">{mark}<span class="cs-award__t"><span class="cs-award__y">{E(year)}</span>'
                   f'<span class="cs-award__n">{E(name)}</span></span></div>')
    return '<section class="cs-awards reveal">' + "".join(out) + "</section>"


FOOTER = """<footer class="footer">
  <div class="footer__grid">
    <div>
      <h4>Contact</h4>
      <a href="mailto:ssom98@naver.com">ssom98@naver.com</a>
      <span>+82 10 5660 5032</span>
    </div>
    <div>
      <h4>Index</h4>
      <a href="../work.html">Work</a>
      <a href="../about.html">About</a>
      <a href="../contact.html">Contact</a>
    </div>
    <div>
      <h4>CV</h4>
      <a href="../about.html#resume">View resume</a>
    </div>
  </div>
  <div class="footer__meta">
    <span>© 2026 Su-min Ko. All rights reserved.</span>
    <span>Portfolio v. 2026.10 — Industrial Design</span>
  </div>
</footer>"""


def render(slug, p):
    i = ORDER.index(slug)
    prev_s, next_s = ORDER[i - 1], ORDER[(i + 1) % len(ORDER)]
    fixed = {"wade": "WADE"}
    title_of = lambda s: PAGES[s]["title"] if s in PAGES else fixed[s]
    meta = "".join(f'<div class="meta__item"><span class="k">{E(k)}</span><span class="v">{E(v)}</span></div>'
                   for k, v in p["meta"])
    d = p.get("dir", slug)
    blocks = p["blocks"]
    body = []
    for j, b in enumerate(blocks):
        nxt = blocks[j + 1][0] if j + 1 < len(blocks) else None
        body.append(render_block(d, b, last=(b[0] == "row" and nxt != "row")))
    d = p.get("dir", slug)
    hero = ""
    if p.get("hero"):
        hw, hh = size(img_src(d, p["hero"]))
        hero = f'<section class="cs-hero reveal"><img src="../{img_src(d, p["hero"])}" alt="{E(p["title"])}" width="{hw}" height="{hh}"></section>'
    back = "ux" if p["cat_key"] == "ux" else "product"
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(p["title"])} — Su-min Ko</title>
<meta name="description" content="{E(p["desc"])}">
<link rel="stylesheet" href="../css/main.css">
<link rel="stylesheet" href="../css/work.css">
<link rel="stylesheet" href="../css/case.css">
</head>
<body data-page="work-detail">
<!-- 생성 파일: _tools/gen_pages.py · 내용은 _tools/pages.py 에서 고칠 것 -->

<nav class="nav" aria-label="Primary">
  <a class="nav__brand" href="../index.html">
    <span class="dot" aria-hidden="true"></span>
    <span>Su-min Ko</span>
  </a>
  <ul class="nav__menu">
    <li><a href="../work.html" aria-current="page">Work</a></li>
    <li><a href="../about.html">About</a></li>
    <li><a href="../contact.html">Contact</a></li>
  </ul>
</nav>

<main>
<div class="back"><a href="../work.html#{back}">← Back</a></div>

<header class="work-head work-head--compact">
  <div class="reveal">
    <div class="work-head__cat"><span class="num">{E(p["year"])}</span>{E(p["category"])}</div>
    <h1 class="work-head__title">{E(p["title"])}</h1>
  </div>
  <p class="work-head__lede reveal delay-1">{p["lede"]}</p>
</header>

{hero}

<section class="meta">{meta}</section>

{render_awards(p.get("awards"))}

{chr(10).join(body)}

<nav class="pager" aria-label="Project navigation">
  <a href="{prev_s}.html" class="left">
    <span class="pager__label">Previous</span>
    <span class="pager__title">← {E(title_of(prev_s))}</span>
  </a>
  <a href="{next_s}.html" class="right">
    <span class="pager__label">Next Project</span>
    <span class="pager__title">{E(title_of(next_s))} →</span>
  </a>
</nav>
</main>

{FOOTER}

<script src="../js/main.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    for slug, p in PAGES.items():
        out = os.path.join(ROOT, "work", slug + ".html")
        with open(out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(render(slug, p))
        print("wrote", os.path.relpath(out, ROOT))
