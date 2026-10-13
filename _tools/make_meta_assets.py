"""공유 미리보기(OG) 이미지 · 파비콘 · 큰 이미지 압축.

실행 (레포 루트):  python _tools/make_meta_assets.py
- assets/og/<slug>.jpg  1200×630 (상세 = 히어로 컷, 정적 4페이지 = site.jpg)
- favicon.svg · apple-touch-icon.png(180)
상세 히어로가 바뀌면 다시 실행할 것.
"""
import os, sys
import pymupdf

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import story_pages as SP  # noqa: E402

OG_W, OG_H = 1200, 630
PAPER = (0xf6 / 255, 0xf5 / 255, 0xf2 / 255)
INK = (0x0b / 255, 0x0b / 255, 0x0f / 255)


def save_jpg(pix, path, q):
    with open(path, "wb") as fh:
        fh.write(pix.tobytes("jpg", jpg_quality=q))


def cover_page(src, w, h, pos=(0.5, 0.5)):
    """src 를 w×h 에 cover 로 채운 페이지 반환"""
    pix = pymupdf.Pixmap(src)
    if pix.alpha:
        pix = pymupdf.Pixmap(pix, 0)
    s = max(w / pix.width, h / pix.height)
    iw, ih = pix.width * s, pix.height * s
    x0 = (w - iw) * pos[0]
    y0 = (h - ih) * pos[1]
    doc = pymupdf.open()
    pg = doc.new_page(width=w, height=h)
    pg.insert_image(pymupdf.Rect(x0, y0, x0 + iw, y0 + ih), pixmap=pix)
    return doc, pg


def og_for_page(slug, p):
    hero = p["hero"]["f"] if isinstance(p["hero"], dict) else p["hero"]
    src = os.path.join(ROOT, "assets", "works", p["dir"], hero)
    doc, pg = cover_page(src, OG_W, OG_H)
    out = os.path.join(ROOT, "assets", "og", slug + ".jpg")
    save_jpg(pg.get_pixmap(), out, 78)
    return out


def og_site():
    src = os.path.join(ROOT, "assets", "works", "ts450", "cover_src.jpg")
    doc, pg = cover_page(src, OG_W, OG_H, pos=(0.5, 0.5))
    # 아래쪽 띠 + 이름
    pg.draw_rect(pymupdf.Rect(0, OG_H - 120, OG_W, OG_H), color=None, fill=PAPER, fill_opacity=0.92)
    pg.insert_text((56, OG_H - 50), "Sumin Ko  ·  Product Designer", fontsize=40, fontname="hebo", color=INK)
    out = os.path.join(ROOT, "assets", "og", "site.jpg")
    save_jpg(pg.get_pixmap(), out, 80)
    return out


def favicons():
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
           '<rect width="64" height="64" rx="14" fill="#f6f5f2"/>'
           '<circle cx="32" cy="32" r="14" fill="#0b0b0f"/></svg>\n')
    open(os.path.join(ROOT, "favicon.svg"), "w", encoding="utf-8").write(svg)
    doc = pymupdf.open()
    pg = doc.new_page(width=180, height=180)
    pg.draw_rect(pg.rect, color=None, fill=PAPER)
    pg.draw_circle((90, 90), 40, color=None, fill=INK)
    pg.get_pixmap(alpha=False).save(os.path.join(ROOT, "apple-touch-icon.png"))


def shrink(rel, q=80, maxside=1800, bg=None, out_rel=None):
    path = os.path.join(ROOT, rel)
    before = os.path.getsize(path)
    pix = pymupdf.Pixmap(path)
    if pix.alpha or bg:
        doc = pymupdf.open()
        pg = doc.new_page(width=pix.width, height=pix.height)
        pg.draw_rect(pg.rect, color=None, fill=bg or (1, 1, 1))
        pg.insert_image(pg.rect, filename=path)
        pix = pg.get_pixmap()
    s = min(1.0, maxside / max(pix.width, pix.height))
    if s < 1:
        pix = pymupdf.Pixmap(pix, round(pix.width * s), round(pix.height * s))
    out = os.path.join(ROOT, out_rel or rel)
    save_jpg(pix, out, q)
    print(f"  {rel} {before // 1024}KB -> {out_rel or rel} {os.path.getsize(out) // 1024}KB ({pix.width}x{pix.height})")


if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "assets", "og"), exist_ok=True)
    for slug, p in SP.PAGES.items():
        out = og_for_page(slug, p)
        print("og", slug, os.path.getsize(out) // 1024, "KB")
    out = og_site()
    print("og site", os.path.getsize(out) // 1024, "KB")
    favicons()
    print("favicons ok")
    if "--shrink" in sys.argv:
        shrink("assets/about-portrait.jpg", q=80, maxside=1600)
        shrink("assets/works/ts700/cradle2.jpg", q=80, maxside=1400)
        shrink("assets/works/ts700/three_part_body.png", q=82, bg=(245 / 255, 245 / 255, 245 / 255),
               out_rel="assets/works/ts700/three_part_body.jpg")
