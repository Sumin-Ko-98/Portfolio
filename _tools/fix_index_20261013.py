"""2026-10-13 홈(index.html) 정리 (1회성)."""
import os, sys, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "index.html")
s = open(P, encoding="utf-8").read()


def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        sys.exit(f"expected {count} got {n}: {old[:80]!r}")
    s = s.replace(old, new)


def card(href, img, alt, badge, title, sub, year, delay=""):
    d = f" {delay}" if delay else ""
    return f"""    <a class="card reveal{d}" data-magnetic href="{href}">
      <div class="card__media">
        <img src="{img}" alt="{alt}">
        <span class="card__badge">{badge}</span>
        <span class="card__view">View project →</span>
      </div>
      <div class="card__foot">
        <div>
          <h3 class="card__title">{title}</h3>
          <p class="card__sub">{sub}</p>
        </div>
        <span class="card__year">{year}</span>
      </div>
    </a>
"""


def replace_grid(nth, cards):
    """nth 번째 <div class="work__grid"> 의 내용을 통째로 교체"""
    global s
    starts = [m.end() for m in re.finditer(r'<div class="work__grid">\n', s)]
    a = starts[nth]
    b = s.index("  </div>\n\n  <div class=\"work__viewall", a)
    s = s[:a] + "\n".join(cards) + s[b:]


rep('content="Product & UX designer based in Seoul. Portfolio 2022–2024."',
    'content="Product & UX designer based in Seoul. Portfolio 2022–2026."')
rep("<span>Portfolio · 2022 — 2024</span>", "<span>Portfolio · 2022 — 2026</span>")
rep("Selected works, 2022&mdash;2024.", "Selected works, 2022&mdash;2026.")
rep('<span class="eyebrow">Selected Works · 2022–2024</span>', '<span class="eyebrow">Selected Works · 2022–2026</span>')

replace_grid(0, [
    card("work/threespin.html", "assets/works/threespin_cover.jpg", "쓰리스핀 슬림 TS450", "iF Gold · Red Dot · GD",
         "Threespin Slim", "쓰리스핀 슬림(TS450) · 물걸레 로봇청소기", "2025"),
    card("work/ts700.html", "assets/works/ts700/cover.jpg", "쓰리스핀 스팀 TS700", "Everybot · 양산 지원",
         "Threespin Steam", "쓰리스핀 스팀(TS700) · 스팀 물걸레 로봇청소기", "2026", "delay-1"),
    card("work/wade.html", "assets/works/wade/cover.jpg", "WADE 워터 드로잉 서비스 로봇", "HCI Korea 2024 · Excellence",
         "WADE", "Water-Drawing Service Robot", "2023", "delay-2"),
])
replace_grid(1, [
    card("work/inclusive.html", "assets/works/inclusive/door_ramp.jpg", "Inclusive PBV 도어스텝", "Hyundai · 2023",
         "Inclusive Mobility", "Universal Boarding &amp; Interior UX for PBV", "2023"),
    card("work/seuv.html", "assets/works/seuv/clamshell_crop.jpg", "SeUV 클램쉘 테일게이트 목업", "Hyundai · 2023",
         "SeUV UX", "Cabin Space &amp; Wellness Concept", "2023", "delay-1"),
    card("work/ev-sedan.html", "assets/works/ev-sedan/ev_scene_console.jpg", "전기세단 확장형 센터콘솔", "Hyundai · 2022",
         "EV Sedan UX", "UX Concepts for a Mid-size EV Sedan", "2022", "delay-2"),
])

# Recognitions
rep("""        <span class="award__year">2026.04</span>
        <span class="award__name">iF Design Award</span>
        <span class="award__note">2026 Gold Winner — 쓰리스핀 슬림 (TS450)</span>""",
    """        <span class="award__year">2026.03</span>
        <span class="award__name">iF Design Award</span>
        <span class="award__note">2026 Gold — 쓰리스핀 슬림 (TS450)</span>""")
rep("""        <span class="award__note">Winner — 쓰리스핀 슬림 (TS450)</span>
      </span>
    </li>
    <li class="award reveal delay-2">
      <span class="award__symbol"><img src="assets/awards/gooddesign.png" alt="Good Design Award"></span>
      <span class="award__body">
        <span class="award__year">2026</span>
        <span class="award__name">Good Design Award</span>
        <span class="award__note">Winner — 쓰리스핀 슬림 (TS450)</span>""",
    """        <span class="award__note">Product Design 2026 — 쓰리스핀 슬림 (TS450)</span>
      </span>
    </li>
    <li class="award reveal delay-2">
      <span class="award__symbol"><img src="assets/awards/gooddesign.png" alt="Good Design Korea"></span>
      <span class="award__body">
        <span class="award__year">2026.08</span>
        <span class="award__name">Good Design Korea</span>
        <span class="award__note">GD 선정 — 쓰리스핀 슬림 (TS450)</span>""")
rep("<span class=\"award__note\">Creative Award, Grand Prize — WADE</span>",
    "<span class=\"award__note\">Creative Award · Excellence Award (최우수상) — WADE</span>")

# footer: 공개 PDF 없음 → 링크 삭제, 버전
rep("""      <a href="assets/portfolio.pdf" target="_blank" rel="noopener">PDF · 40 MB</a>
""", "")
rep("Portfolio v. 2026.08 — Industrial Design", "Portfolio v. 2026.10 — Industrial Design")

open(P, "w", encoding="utf-8", newline="\n").write(s)
print("index ok; '#' links left:", s.count('href="#"'))
