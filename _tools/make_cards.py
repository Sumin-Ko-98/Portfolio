"""홈·Work 카드 썸네일(4:3)을 한 규칙으로 만든다.

규칙: 최종 PDF 표지와 같은 대표 컷 · 제품을 정중앙 · 제품 높이(또는 폭)를 카드의 일정 비율로 맞춤
      · 원본이 모자라는 쪽은 원본 가장자리 색으로 채움(잘림·띠 없음)

실행:  python _tools/make_cards.py            → assets/cards/<slug>.jpg (1200×900)
       python _tools/make_cards.py --debug    → 찾은 제품 영역을 빨간 박스로 표시한 확인용 이미지
"""
import os, sys
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(ROOT, "assets", "works")
OUT = os.path.join(ROOT, "assets", "cards")
CW, CH = 1200, 900

# slug: (원본, 제품 영역 bbox 원본 px 또는 None=자동, 카드에서 제품이 차지할 비율)
#   fill = 제품 bbox가 카드 높이(가로로 긴 제품이면 폭)에서 차지하는 비율
#   fill=None  → 장면 컷: bbox 중심 기준으로 카드를 꽉 채움(cover)
#   bbox는 그라데이션 배경에서 자동 탐지가 안 돼 원본을 보고 지정(2026-10-14)
CARDS = {
    "ts450":     ("ts450/cover_src.jpg",       (570, 140, 1255, 915),  0.80),
    "ts700":     ("ts700/cover_src.jpg",       (567, 134, 1282, 887),  0.80),
    "h500":      ("h500/ctrl_cover_src.jpg",   None,                   0.74),
    "wade":      ("wade/cover.jpg",            (929, 251, 1621, 1012), 0.80),
    "mobilink":  ("mobilink/render_sq.jpg",    (105, 119, 767, 966),   0.86),
    "flever":    ("flever/bh_hero.jpg",        (256, 185, 1414, 1182), 0.80),
    "inclusive": ("inclusive/door_ramp.jpg",   (360, 0, 1800, 1012),   None),
    "seuv":      ("seuv/s_mood.jpg",           None,                   None),
    "ev-sedan":  ("ev-sedan/ev_scene_console.jpg", None,               None),
}
# CMF는 최종 PDF 06 표지처럼 제품 4종 2×2
CMF_GRID = ["odm/q9_plus.jpg", "odm/q13.jpg", "odm/x1.jpg", "odm/sr13w.jpg"]


def border_color(pix):
    s, n, w, h = pix.samples, pix.n, pix.width, pix.height
    pts = []
    for x in range(0, w, max(1, w // 60)):
        for y in (1, h - 2):
            i = (y * w + x) * n; pts.append(s[i:i + 3])
    for y in range(0, h, max(1, h // 60)):
        for x in (1, w - 2):
            i = (y * w + x) * n; pts.append(s[i:i + 3])
    return tuple(sorted(p[c] for p in pts)[len(pts) // 2] for c in range(3))


def auto_bbox(path, thr=28):
    full = pymupdf.Pixmap(path)
    if full.alpha: full = pymupdf.Pixmap(full, 0)
    k = max(1, full.width // 300)
    small = pymupdf.Pixmap(full, 0) if False else full
    # 축소본으로 마스크
    sw, sh = full.width // k, full.height // k
    doc = pymupdf.open(); pg = doc.new_page(width=sw, height=sh)
    pg.insert_image(pg.rect, filename=path)
    pix = pg.get_pixmap(colorspace=pymupdf.csRGB)
    bg = border_color(pix)
    s, n, w, h = pix.samples, pix.n, pix.width, pix.height
    cols, rows = [0] * w, [0] * h
    for y in range(h):
        base = y * w * n
        for x in range(w):
            i = base + x * n
            if abs(s[i] - bg[0]) + abs(s[i + 1] - bg[1]) + abs(s[i + 2] - bg[2]) > thr:
                cols[x] += 1; rows[y] += 1
    cx = [x for x in range(w) if cols[x] > h * 0.02]
    ry = [y for y in range(h) if rows[y] > w * 0.02]
    if not cx or not ry:
        return (0, 0, full.width, full.height), bg
    sx, sy = full.width / w, full.height / h
    return (cx[0] * sx, ry[0] * sy, (cx[-1] + 1) * sx, (ry[-1] + 1) * sy), bg


def strip(path, iw, ih, r):
    """원본의 r 영역(px)만 잘라낸 픽스맵 — 가장자리 띠 늘이기용"""
    d = pymupdf.open(); pg = d.new_page(width=iw, height=ih)
    pg.insert_image(pg.rect, filename=path)
    return pg.get_pixmap(clip=r, colorspace=pymupdf.csRGB)


ANCHOR_BOTTOM = {"wade/cover.jpg"}   # 원본 아래가 잘린 컷 → 카드 아래에 붙임


def compose(path, bbox, fill, bg):
    img = pymupdf.Pixmap(path); iw, ih = img.width, img.height
    rel = os.path.relpath(path, W).replace(os.sep, "/")
    x0, y0, x1, y1 = bbox; bw, bh = x1 - x0, y1 - y0
    if fill is None:          # 장면 컷: 카드를 꽉 채움
        scale = max(CW / iw, CH / ih)
    elif bw / bh > CW / CH:   # 가로로 긴 제품 → 폭 기준
        scale = (CW * fill) / bw
    else:                     # 세로로 긴 제품 → 높이 기준
        scale = (CH * fill) / bh
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    left = CW / 2 - cx * scale; top = CH / 2 - cy * scale
    if fill is None:          # 장면은 틈 없이
        left = min(0, max(CW - iw * scale, left)); top = min(0, max(CH - ih * scale, top))
    if rel in ANCHOR_BOTTOM:
        top = CH - ih * scale
    right, bottom = left + iw * scale, top + ih * scale
    doc = pymupdf.open(); pg = doc.new_page(width=CW, height=CH)
    pg.draw_rect(pg.rect, color=None, fill=[c / 255 for c in bg])
    e = 4  # 원본 가장자리 4px 띠를 늘려 틈을 채움 → 배경 그라데이션이 자연스럽게 이어짐
    if left > 0:
        pg.insert_image(pymupdf.Rect(0, top, left + 1, bottom), pixmap=strip(path, iw, ih, pymupdf.Rect(0, 0, e, ih)), keep_proportion=False)
    if right < CW:
        pg.insert_image(pymupdf.Rect(right - 1, top, CW, bottom), pixmap=strip(path, iw, ih, pymupdf.Rect(iw - e, 0, iw, ih)), keep_proportion=False)
    if top > 0:
        pg.insert_image(pymupdf.Rect(min(left, 0), 0, max(right, CW), top + 1), pixmap=strip(path, iw, ih, pymupdf.Rect(0, 0, iw, e)), keep_proportion=False)
    if bottom < CH:
        pg.insert_image(pymupdf.Rect(min(left, 0), bottom - 1, max(right, CW), CH), pixmap=strip(path, iw, ih, pymupdf.Rect(0, ih - e, iw, ih)), keep_proportion=False)
    pg.insert_image(pymupdf.Rect(left, top, right, bottom), filename=path)
    return pg.get_pixmap(colorspace=pymupdf.csRGB), (left, top, scale)


def cmf_grid():
    first = pymupdf.Pixmap(os.path.join(W, CMF_GRID[0]))
    bg = first.pixel(5, 5)[:3]
    doc = pymupdf.open(); pg = doc.new_page(width=CW, height=CH)
    pg.draw_rect(pg.rect, color=None, fill=[c / 255 for c in bg])
    gw, gh = CW / 2, CH / 2
    for i, rel in enumerate(CMF_GRID):
        p = os.path.join(W, rel)
        img = pymupdf.Pixmap(p)
        s = min(gw / img.width, gh / img.height) * 0.98
        cx, cy = (i % 2 + 0.5) * gw, (i // 2 + 0.5) * gh
        r = pymupdf.Rect(cx - img.width * s / 2, cy - img.height * s / 2, cx + img.width * s / 2, cy + img.height * s / 2)
        pg.insert_image(r, filename=p)
    return pg.get_pixmap(colorspace=pymupdf.csRGB)


def main():
    debug = "--debug" in sys.argv
    os.makedirs(OUT, exist_ok=True)
    for slug, (rel, bbox, fill) in CARDS.items():
        p = os.path.join(W, rel)
        found, bg = auto_bbox(p)
        bbox = bbox or found
        pix, (l, t, s) = compose(p, bbox, fill, bg)
        if debug:
            d = pymupdf.open(); pg = d.new_page(width=CW, height=CH)
            pg.insert_image(pg.rect, pixmap=pix)
            x0, y0, x1, y1 = bbox
            pg.draw_rect(pymupdf.Rect(l + x0 * s, t + y0 * s, l + x1 * s, t + y1 * s), color=(1, 0, 0), width=3)
            pix = pg.get_pixmap()
        pix.save(os.path.join(OUT, f"{slug}.jpg"), jpg_quality=86)
        print(slug, [round(v) for v in bbox], "bg", bg)
    cmf_grid().save(os.path.join(OUT, "odm-cmf.jpg"), jpg_quality=86)
    print("odm-cmf grid")


if __name__ == "__main__":
    main()
