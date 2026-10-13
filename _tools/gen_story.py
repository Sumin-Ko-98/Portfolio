"""상세페이지 생성기 (Story 레이아웃 = 원래 WADE 상세페이지 리듬).

실행 (레포 루트에서):  python _tools/gen_story.py            # 전체
                       python _tools/gen_story.py ts700      # 한 페이지만
- 내용: _tools/story_pages.py  (work/*.html 을 직접 고치면 다음 실행 때 덮어써짐)
- 스타일: css/story.css (원래 WADE 인라인 스타일을 뽑은 것) + css/main.css + css/work.css
- 이미지: assets/works/<dir>/<이름>. 파일이 없으면 story_pages.SOURCES 의 원본에서 웹용(긴 변 1800px, JPG)으로 만든다.

섹션 (story_pages.py 에서 쓰는 튜플)
  ("hero", img)                                  머리 아래 16:9 풀블리드
  ("intro", awards, h, h_en, kor, eng)           수상/특허 목록 + 한·영 소개
  ("dark", [블록...])                            블랙 패널. 블록:
       ("img", img) · ("row", MARK, kor, eng) · ("dots", [img,img,img]) · ("grid", [img x6])
       ("mosaic", [img x4]) · ("facts", [(값, 설명)...]) · ("roles", [역할...])
  ("scene", img)                                 블랙 패널 바로 뒤 풀블리드(위쪽 검정 그라데이션)
  ("text", 라벨, kor, eng)                        라벨 + 한·영 문단
  ("split", (라벨, kor, eng), (라벨, kor, eng))   좌우 캡션
  ("square", img) · ("scenario", img)            여백 있는 정사각
  ("tri", [img x3])                              풀블리드 3열 정사각
  ("duo", [img, img])                            풀블리드 2칸 (정사각 + 3:4)
  ("pair", [img, img])                           여백 있는 2칸 (3:4)
  ("bleed", img, kind)                           풀블리드. kind = tall|macro|strap|related|final|natural
  ("lineup", [(img, 캡션)...], (MORE 제목, 설명))  제품 라인업 4열 그리드
  ("band",)                                      검은 띠
img = "파일.jpg" 또는 dict(f="파일.jpg", pos="50% 40%", fit="contain", bg="#fff", r="natural")
"""
import os, sys, html, re

import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import story_pages as SP  # noqa: E402

E = html.escape
MAX = 1800
BASE = "https://sumin-ko-98.github.io/Portfolio/"
CTX = {"title": "", "label": ""}  # 이미지 alt 자동 생성용 (프로젝트명 · 섹션 라벨)


def _plain(x):
    return re.sub(r"<[^>]+>", " ", html.unescape(x or "")).replace("  ", " ").strip()


# ---------------------------------------------------------------- assets
def _load_source(src):
    """SOURCES 값 → Pixmap. 값은 경로 문자열 또는 dict:
       {"src": 경로, "rot": 90|180|270, "crop": (x0, y0, x1, y1) 비율, "trim": 0.06 (빈 배경 자르고 여백 비율)}
       {"pdf": 경로, "page": 0부터, "rect": (x0, y0, x1, y1) PDF 좌표, "scale": 1.5}"""
    if isinstance(src, str):
        src = {"src": src}
    if "pdf" in src:
        doc = pymupdf.open(src["pdf"])
        s = src.get("scale", 1.5)
        return doc[src["page"]].get_pixmap(matrix=pymupdf.Matrix(s, s), clip=pymupdf.Rect(*src["rect"]))
    path = src["src"]
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        raise SystemExit(f"원본 없음/동기화 중: {path}")
    pix = pymupdf.Pixmap(path)
    rot = src.get("rot", 0)
    crop = src.get("crop")
    if pix.alpha or pix.n > 3 or rot or crop:
        # 흰 바탕 페이지에 그려서 투명 합성 · 회전 · 크롭을 한 번에
        w, h = (pix.height, pix.width) if rot in (90, 270) else (pix.width, pix.height)
        doc = pymupdf.open()
        pg = doc.new_page(width=w, height=h)
        pg.draw_rect(pg.rect, color=None, fill=(1, 1, 1))
        pg.insert_image(pg.rect, filename=path, rotate=rot)
        clip = None
        if crop:
            x0, y0, x1, y1 = crop
            clip = pymupdf.Rect(w * x0, h * y0, w * x1, h * y1)
        pix = pg.get_pixmap(clip=clip)
    if src.get("trim") is not None:
        pix = _trim(pix, src["trim"])
    if src.get("square"):
        pix = _square(pix)
    return pix


def _square(pix):
    """가장자리 픽셀을 늘려 정사각형으로 (그라데이션 배경 렌더를 정사각 칸에 꽉 채울 때)"""
    import numpy as np
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)[:, :, :3]
    h, w = a.shape[:2]
    if w > h:
        t = (w - h) // 2
        a = np.pad(a, ((t, w - h - t), (0, 0), (0, 0)), mode="edge")
    elif h > w:
        t = (h - w) // 2
        a = np.pad(a, ((0, 0), (t, h - w - t), (0, 0)), mode="edge")
    a = np.ascontiguousarray(a)
    return pymupdf.Pixmap(pymupdf.csRGB, a.shape[1], a.shape[0], a.tobytes(), False)


def _trim(pix, margin):
    """렌더 바깥의 빈 배경을 잘라 제품 둘레에 margin(긴 변 비율)만 남긴다."""
    import numpy as np
    if pix.alpha:
        pix = pymupdf.Pixmap(pix, 0)
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)[:, :, :3].astype(int)
    corners = np.array([a[2, 2], a[2, -3], a[-3, 2], a[-3, -3]])
    bg = np.median(corners, axis=0)
    mask = np.abs(a - bg).sum(axis=2) > 36
    ys, xs = np.where(mask)
    if len(xs) == 0:
        return pix
    m = int(max(pix.width, pix.height) * margin)
    x0, x1 = max(0, xs.min() - m), min(pix.width, xs.max() + m)
    y0, y1 = max(0, ys.min() - m), min(pix.height, ys.max() + m)
    doc = pymupdf.open(); pg = doc.new_page(width=pix.width, height=pix.height)
    pg.insert_image(pg.rect, pixmap=pix)
    return pg.get_pixmap(clip=pymupdf.Rect(x0, y0, x1, y1))


def ensure_asset(d, name):
    """assets/works/d/name 이 없으면 SOURCES 원본에서 만든다. (w, h) 반환."""
    rel = f"assets/works/{d}/{name}"
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        src = SP.SOURCES.get(d, {}).get(name)
        if not src:
            raise SystemExit(f"이미지 없음, SOURCES에도 없음: {rel}")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        pix = _load_source(src)
        s = min(1.0, MAX / max(pix.width, pix.height))
        if s < 1:
            pix = pymupdf.Pixmap(pix, round(pix.width * s), round(pix.height * s))
        with open(path, "wb") as fh:
            fh.write(pix.tobytes("jpg", jpg_quality=84))
        print("  + asset", rel, f"{pix.width}x{pix.height}")
    pix = pymupdf.Pixmap(path)
    return pix.width, pix.height, pix


class Img:
    def __init__(self, d, spec):
        if isinstance(spec, str):
            spec = {"f": spec}
        self.f = spec["f"]
        self.pos = spec.get("pos")
        self.fit = spec.get("fit")
        self.bg = spec.get("bg")
        self.r = spec.get("r")
        self.pad = spec.get("pad")      # contain 일 때 제품 둘레 여백 (예: "6%")
        cap = _plain(spec.get("cap", ""))
        parts = [CTX["title"], CTX["label"], cap]
        self.alt = spec.get("alt") or " · ".join(dict.fromkeys(x for x in parts if x))
        self.w, self.h, pix = ensure_asset(d, self.f)
        if self.bg == "auto":           # 렌더 배경색에 맞춘 판 (가장자리 픽셀 평균)
            # 위쪽 가장자리 + 좌우 중간 (아래쪽은 제품 그림자 때문에 어두워서 제외), 중앙값
            px = [pix.pixel(x, y)[:3] for x, y in ((3, 3), (pix.width - 4, 3), (pix.width // 4, 3),
                                                     (pix.width // 2, 3), (3 * pix.width // 4, 3),
                                                     (3, pix.height // 3), (pix.width - 4, pix.height // 3))]
            r, g, b = (sorted(c[i] for c in px)[len(px) // 2] for i in range(3))
            self.bg = f"#{r:02x}{g:02x}{b:02x}"
        self.src = f"../assets/works/{d}/{self.f}"

    def tag(self):
        style = []
        if self.pos:
            style.append(f"object-position:{self.pos}")
        if self.bg:
            style.append(f"background:{self.bg}")
        if self.pad:
            style.append(f"padding:{self.pad}")
        cls = ' class="st-contain"' if self.fit == "contain" else ""
        st = f' style="{";".join(style)}"' if style else ""
        return f'<img src="{self.src}" alt="{E(self.alt)}" loading="lazy" width="{self.w}" height="{self.h}"{cls}{st}>'

    def ratio_css(self):
        return f"aspect-ratio:{self.w}/{self.h}" if self.r == "natural" else ""

    def ratio_style(self, extra=""):
        css = ";".join(x for x in (self.ratio_css(), extra) if x)
        if self.bg and self.fit == "contain":
            css = ";".join(x for x in (css, f"background:{self.bg}") if x)
        return f' style="{css}"' if css else ""

# ---------------------------------------------------------------- blocks
def kor_eng(kor, eng, cls_k, cls_e, kor_style=""):
    out = f'<p class="{cls_k}"{kor_style}>{kor}</p>'
    if eng:
        out += f'\n      <p class="{cls_e}">{eng}</p>'
    return out


def dark_block(d, b, label=""):
    k = b[0]
    if label:
        CTX["label"] = label
    if k == "img":
        im = Img(d, b[1])
        extra = b[2] if len(b) > 2 else ""
        extra = extra.strip()
        if extra.startswith('style="'):
            extra = extra[7:-1]
        return f'  <div class="wd-dark-img reveal"{im.ratio_style(extra)}>{im.tag()}</div>'
    if k == "row":
        _, mark, kor, eng = b
        body = kor_eng(kor, eng, "wd-dark-row__kor", "wd-dark-row__eng", ' style="color: rgb(246, 245, 242)"')
        return f"""  <div class="wd-dark-row reveal">
    <div class="wd-dark-row__mark">{mark}</div>
    <div class="wd-dark-row__body">
      {body}
    </div>
  </div>"""
    if k == "dots":
        cells = "\n".join(f'    <div class="wd-dot">{Img(d, s).tag()}</div>' for s in b[1])
        two = " wd-dots--2" if len(b[1]) == 2 else ""
        return f'  <div class="wd-dots{two} reveal delay-1">\n{cells}\n  </div>'
    if k == "grid":
        cells = "".join(f"<div>{Img(d, s).tag()}</div>" for s in b[1])
        return f'  <div class="wd-protogrid reveal">\n    {cells}\n  </div>'
    if k == "mosaic":
        a, bb, c, dd = [Img(d, s).tag() for s in b[1]]
        return f"""  <div class="wd-mosaic reveal delay-1">
    <div class="wd-mosaic__row wd-mosaic__row--a"><div>{a}</div><div>{bb}</div></div>
    <div class="wd-mosaic__row wd-mosaic__row--b"><div>{c}</div><div>{dd}</div></div>
  </div>"""
    if k == "facts":
        cells = "".join(f'<div class="st-fact"><span class="st-fact__v">{E(v)}</span><span class="st-fact__k">{E(t)}</span></div>'
                        for v, t in b[1])
        return f'  <div class="st-facts reveal" style="--n:{len(b[1])}">{cells}</div>'
    if k == "roles":
        chips = "".join(f"<span>{E(r)}</span>" for r in b[1])
        return f"""  <div class="wd-dark-row reveal">
    <div class="wd-dark-row__mark">ROLE</div>
    <div class="wd-dark-row__body"><div class="st-role">{chips}</div></div>
  </div>"""
    raise ValueError(k)


def section(d, s):
    k = s[0]
    if k == "dark":
        blocks = s[1]
        marks = [_plain(b[1]) if b[0] == "row" else None for b in blocks]

        def label_for(i):
            nxt = next((m for m in marks[i + 1:] if m), None)
            prv = next((m for m in reversed(marks[:i]) if m), None)
            return (nxt or prv or CTX["label"]).title()
        inner = "\n\n".join(dark_block(d, b, label_for(i)) for i, b in enumerate(blocks))
        return f'<section class="wd-dark">\n{inner}\n</section>'
    if k == "scene":
        im = Img(d, s[1])
        return f'<section class="wd-scene-bleed">\n  <div class="wd-scene-bleed__frame"{im.ratio_style()}>{im.tag()}</div>\n</section>'
    if k == "text":
        _, label, kor, eng = s
        return f"""<section class="wd-textrow">
  <div class="wd-textrow__label">{label}</div>
  <div class="wd-textrow__body">
    {kor_eng(kor, eng, "wd-textrow__kor", "wd-textrow__eng")}
  </div>
</section>"""
    if k == "split":
        cols = []
        for side, (label, kor, eng) in zip(("left", "right"), s[1:]):
            cols.append(f"""  <div class="wd-textrow__col wd-textrow__col--{side}">
    <h3 class="wd-textrow__caplabel">{label}</h3>
    {kor_eng(kor, eng, "wd-textrow__kor", "wd-textrow__eng")}
  </div>""")
        return '<section class="wd-textrow wd-textrow--split">\n' + "\n".join(cols) + "\n</section>"
    if k == "square":
        im = Img(d, s[1])
        return f'<section class="wd-bigsquare">\n  <div class="wd-bigsquare__frame reveal"{im.ratio_style()}>{im.tag()}</div>\n</section>'
    if k == "scenario":
        im = Img(d, s[1])
        return f'<section class="wd-scenario">\n  <div class="wd-scenario__frame reveal"{im.ratio_style()}>{im.tag()}</div>\n</section>'
    if k == "single":
        # ("single", img, caption) — 여백 있는 단독 이미지(원래 비율) + 캡션
        im = Img(d, s[1])
        cap = s[2] if len(s) > 2 else ""
        out = (f'<section class="wd-detailduo" style="grid-template-columns:1fr">\n'
               f'  <div class="reveal" style="aspect-ratio:{im.w}/{im.h}">{im.tag()}</div>\n</section>')
        if cap:
            out += f'\n<div class="st-pair-caps" style="grid-template-columns:1fr"><span>{cap}</span></div>'
        return out
    if k == "tri":
        cells = "\n".join(f'  <div class="wd-trirow__cell reveal{" delay-" + str(i) if i else ""}">{Img(d, x).tag()}</div>'
                          for i, x in enumerate(s[1]))
        out = f'<section class="wd-trirow">\n{cells}\n</section>'
        caps = [x.get("cap") if isinstance(x, dict) else None for x in s[1]]
        if any(caps):
            out += ('\n<div class="st-pair-caps st-tri-caps">' + "".join(f"<span>{c or ''}</span>" for c in caps) + "</div>")
        return out
    if k == "duo":
        a, b = [Img(d, x) for x in s[1]]
        return (f'<section class="wd-bleed-duo wd-bleed-duo--sq-tall">\n  <div class="reveal">{a.tag()}</div>\n'
                f'  <div class="reveal delay-1">{b.tag()}</div>\n</section>')
    if k == "pair":
        a, b = [Img(d, x) for x in s[1]]
        ra = a.ratio_css()
        out = (f'<section class="wd-detailduo">\n  <div class="reveal"{a.ratio_style()}>{a.tag()}</div>\n'
               f'  <div class="reveal delay-1"{b.ratio_style(ra) if ra else b.ratio_style()}>{b.tag()}</div>\n</section>')
        caps = [x.get("cap") if isinstance(x, dict) else None for x in s[1]]
        if any(caps):
            out += ('\n<div class="st-pair-caps">' + "".join(f"<span>{c or ''}</span>" for c in caps) + "</div>")
        return out
    if k == "bleed":
        im = Img(d, s[1])
        kind = s[2] if len(s) > 2 else "natural"
        if kind == "natural":
            im.r = "natural"
            kind = "final"
        return (f'<section class="wd-bleed wd-bleed--{kind}">\n'
                f'  <div class="wd-bleed__frame wd-bleed__frame--photo reveal"{im.ratio_style()}>{im.tag()}</div>\n</section>')
    if k == "lineup":
        cells = []
        for spec, cap in s[1]:
            im = Img(d, spec)
            cells.append(f'<figure class="st-lineup__cell reveal">{im.tag()}<figcaption>{E(cap)}</figcaption></figure>')
        if len(s) > 2 and s[2]:
            cells.append(f'<div class="st-lineup__more"><b>{E(s[2][0])}</b><span>{E(s[2][1])}</span></div>')
        return '<section class="st-lineup">\n  ' + "\n  ".join(cells) + "\n</section>"
    if k == "video":
        # ("video", "anim.mp4", "anim_poster.jpg") — 풀블리드 자동재생 루프 (소리 없음)
        _, mp4, poster = s
        w, h, _p = ensure_asset(d, poster)
        return (f'<section class="wd-bleed wd-bleed--final">\n  <div class="wd-bleed__frame wd-bleed__frame--photo reveal" '
                f'style="aspect-ratio:{w}/{h}"><video src="../assets/works/{d}/{mp4}" poster="../assets/works/{d}/{poster}" '
                f'autoplay muted loop playsinline preload="metadata"></video></div>\n</section>')
    if k == "band":
        return '<div class="wd-band"></div>'
    raise ValueError(k)


AWARD_LOGO = {"if": "if-gold.png", "reddot": "reddot.png", "gd": "gooddesign.png", "hci": "hci.png",
              "idea": "idea.png", "spark": "spark.png"}


def intro(p):
    awards, h, h_en, kor, eng = p
    items = []
    for key, year, name, note in awards:
        if key in AWARD_LOGO:
            sym = f'<span class="wd-award__symbol"><img src="../assets/awards/{AWARD_LOGO[key]}" alt="{E(name)} logo"></span>'
        else:
            sym = f'<span class="wd-award__symbol wd-award__symbol--text">{E(key)}</span>'
        items.append(f"""      <li class="wd-award">
        {sym}
        <span class="wd-award__body">
          <span class="wd-award__year">{E(year)}</span>
          <span class="wd-award__name">{E(name)}</span>
          <span class="wd-award__note">{E(note)}</span>
        </span>
      </li>""")
    return f"""<section class="wd-intro">
  <div class="wd-intro__mark-wrap reveal">
    <ul class="wd-awards" aria-label="Awards">
{chr(10).join(items)}
    </ul>
  </div>
  <div class="wd-intro__body reveal delay-1">
    <div>
      <h2 class="wd-intro__h">{h}</h2>
      <p class="wd-intro__h-en">{h_en}</p>
      <p class="wd-intro__kor">{kor}</p>
    </div>
    <p class="wd-intro__eng">{eng}</p>
  </div>
</section>"""


FOOTER = """<footer class="footer">
  <div class="footer__grid">
    <div>
      <h4>Contact</h4>
      <a href="mailto:ssom98@naver.com">ssom98@naver.com</a>
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
    <span>© 2026 Sumin Ko. All rights reserved.</span>
    <span>Portfolio v. 2026.10 — Industrial Design</span>
  </div>
</footer>"""


def render(slug, p):
    order = SP.ORDER
    i = order.index(slug)
    prev_s, next_s = order[i - 1], order[(i + 1) % len(order)]
    d = p["dir"]
    CTX["title"], CTX["label"] = p["title"], "Hero"
    hero = Img(d, p["hero"])
    meta = "\n".join(f'  <div class="meta__item"><span class="k">{E(k)}</span><span class="v">{E(v)}</span></div>'
                     for k, v in p["meta"])
    CTX["title"] = p["title"]
    CTX["label"] = "Overview"
    secs = p["sections"]
    out = []
    for i, sec in enumerate(secs):
        k = sec[0]
        if k in ("text", "part"):
            CTX["label"] = _plain(sec[1] if k == "text" else sec[2])
        elif k not in ("dark", "band"):
            nxt = secs[i + 1] if i + 1 < len(secs) else None
            if nxt and nxt[0] == "split":
                CTX["label"] = " / ".join(_plain(c[0]) for c in nxt[1:])
        out.append(section(d, sec))
        if k == "split":
            CTX["label"] = " / ".join(_plain(c[0]) for c in sec[1:])
    body = "\n\n".join(out)
    back = "ux" if p.get("cat_key") == "ux" else "product"
    return f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(p["title"])} — Sumin Ko</title>
<meta name="description" content="{E(p["desc"])}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Sumin Ko Portfolio">
<meta property="og:title" content="{E(p["title"])} — Sumin Ko">
<meta property="og:description" content="{E(p["desc"])}">
<meta property="og:url" content="{BASE}work/{slug}.html">
<meta property="og:image" content="{BASE}assets/og/{slug}.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="../apple-touch-icon.png">
<link rel="stylesheet" href="../css/main.css">
<link rel="stylesheet" href="../css/work.css">
<link rel="stylesheet" href="../css/story.css">
</head>
<body data-page="work-detail">
<!-- 생성 파일: _tools/gen_story.py · 내용은 _tools/story_pages.py 에서 고칠 것 -->

<nav class="nav" aria-label="Primary">
  <a class="nav__brand" href="../index.html">
    <span class="dot" aria-hidden="true"></span>
    <span>Sumin Ko</span>
  </a>
  <ul class="nav__menu">
    <li><a href="../work.html" aria-current="page">Work</a></li>
    <li><a href="../about.html">About</a></li>
    <li><a href="../contact.html">Contact</a></li>
  </ul>
</nav>

<main>

<section class="v2-hero v2-hero--plain v2-hero--backonly">
  <div class="v2-back"><a href="../work.html#{back}">← Back</a></div>
</section>

<header class="work-head work-head--compact">
  <div class="reveal">
    <div class="work-head__cat"><span class="num">{E(p["year"])}</span>{E(p["category"])}</div>
    <h1 class="work-head__title">{E(p["title"])}.</h1>
  </div>
  <p class="work-head__lede reveal delay-1" style="font-size: 15px; color: rgb(11, 11, 15); letter-spacing: 0px">{p["lede"]}</p>
</header>

<section class="v2-hero v2-hero--plain v2-hero--after-head">
  <div class="v2-hero__media">{hero.tag()}</div>
</section>

<section class="meta">
{meta}
</section>

{intro(p["intro"])}

{body}

<nav class="pager" aria-label="Project navigation">
  <a href="{prev_s}.html" class="left">
    <span class="pager__label">Previous</span>
    <span class="pager__title">← {E(SP.PAGES[prev_s]["title"])}</span>
  </a>
  <a href="{next_s}.html" class="right">
    <span class="pager__label">Next Project</span>
    <span class="pager__title">{E(SP.PAGES[next_s]["title"])} →</span>
  </a>
</nav>

</main>

{FOOTER}

<script src="../js/main.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    only = sys.argv[1:]
    for slug in SP.ORDER:
        if only and slug not in only:
            continue
        print(slug)
        out = os.path.join(ROOT, "work", slug + ".html")
        txt = render(slug, SP.PAGES[slug])
        with open(out, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(txt)
        print("  wrote", os.path.relpath(out, ROOT))
