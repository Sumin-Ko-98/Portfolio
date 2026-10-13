"""2026-10-13 Work 인덱스(work.html) 정리 (1회성): 상세페이지 연결, 잘못된 설명·연도 수정, 상세 없는 프로젝트는 링크 없는 Archive 카드로."""
import os, sys, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "work.html")
s = open(P, encoding="utf-8").read()


def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        sys.exit(f"expected {count} got {n}: {old[:80]!r}")
    s = s.replace(old, new)


def foot(title, sub, year):
    return f"""      <div class="card__foot">
        <div>
          <h3 class="card__title">{title}</h3>
          <p class="card__sub">{sub}</p>
        </div>
        <span class="card__year">{year}</span>
      </div>"""


def laurel(key):
    return f'\n        <span class="card__laurel"><img src="assets/awards/{key}.png" alt=""></span>' if key else ""


def linked(href, img, alt, title, sub, year, award=None, delay=0):
    d = f" delay-{delay}" if delay else ""
    return f"""    <a class="card reveal{d}" href="{href}">
      <div class="card__media">
        <img src="{img}" alt="{alt}">{laurel(award)}
        <span class="card__view">View project →</span>
      </div>
{foot(title, sub, year)}
    </a>
"""


def archive(title, sub, year, cover, award=None, delay=0, img=None):
    """상세페이지 없는 프로젝트 — 링크 없음"""
    d = f" delay-{delay}" if delay else ""
    if img:
        media = f'<img src="{img}" alt="{title}">'
    else:
        tone, kicker, name = cover
        media = f"""<div class="tp-cover tp-cover--{tone}">
          <div class="tp-cover__inner">
            <span class="tp-cover__kicker">{kicker}</span>
            <span class="tp-cover__name">{name}</span>
          </div>
        </div>"""
    return f"""    <div class="card card--wip reveal{d}">
      <div class="card__media">
        {media}{laurel(award)}
      </div>
{foot(title, sub, year + ' · Archive')}
    </div>
"""


PRODUCT = [
    linked("work/ts700.html", "assets/works/ts700/cover.jpg", "쓰리스핀 스팀 TS700", "Threespin Steam",
           "쓰리스핀 스팀(TS700) · 스팀 물걸레 로봇청소기", "2026"),
    linked("work/h500.html", "assets/works/h500/ctrl_cover.jpg", "H500 컨트롤러", "H500",
           "수전동휠체어 컨트롤러 · 인휠모터 휠", "2026", delay=1),
    linked("work/odm-cmf.html", "assets/works/odm/q3_turbo.jpg", "ODM CMF", "ODM CMF",
           "양산 제품 CMF 디자인 16종", "2026", delay=2),
    linked("work/threespin.html", "assets/works/threespin_cover.jpg", "쓰리스핀 슬림 TS450", "Threespin Slim",
           "쓰리스핀 슬림(TS450) · 물걸레 로봇청소기", "2025", award="if-gold"),
    linked("work/wade.html", "assets/works/wade/cover.jpg", "WADE 워터 드로잉 서비스 로봇", "WADE",
           "Water-Drawing Service Robot", "2023", award="hci", delay=1),
    archive("ARO", "Classroom Arrangement Robot · IDEA Finalist", "2023", ("slate", "Service Robot", "ARO"),
            award="idea", delay=2),
    archive("FODI", "Spark Design Awards Finalist", "2023", ("rose", "Spark Finalist", "FODI"), award="spark"),
    archive("MobiLink", "Mobile Console for Future Mobility", "2022", ("indigo", "Mobility", "MobiLink"), award="idea", delay=1),
    archive("Flever", "Smart Home Screen for Family", "2022", ("amber", "Smart Home", "Flever"), delay=2),
    archive("NOBLE", "COWAY · 프리미엄 정수기 UX", "2023", ("charcoal", "Home Appliance", "NOBLE")),
]
UX = [
    archive("SDV Pace Car", "현대자동차 × 마크로밀엠브레인 · 소비자 조사", "2024", ("indigo", "Consumer Research", "SDV<br>Pace")),
    linked("work/inclusive.html", "assets/works/inclusive/door_ramp.jpg", "Inclusive PBV 도어스텝", "Inclusive Mobility",
           "Universal Boarding &amp; Interior UX for PBV", "2023", delay=1),
    linked("work/seuv.html", "assets/works/seuv/clamshell_crop.jpg", "SeUV 클램쉘 테일게이트 목업", "SeUV UX",
           "Cabin Space &amp; Wellness Concept", "2023", delay=2),
    archive("GlowOne", "글로우원 · 인간중심 스마트조명 디자인", "2023", ("sage", "Smart Lighting", "GlowOne")),
    archive("Seamless Cabin", "서연이화 · 미래 모빌리티 내장디자인 연구", "2023", ("slate", "Automotive Interior", "Seamless<br>Cabin"),
            delay=1),
    linked("work/ev-sedan.html", "assets/works/ev-sedan/ev_scene_console.jpg", "전기세단 확장형 센터콘솔", "EV Sedan UX",
           "UX Concepts for a Mid-size EV Sedan", "2022", delay=2),
]


def replace_grid(nth, cards):
    global s
    starts = [m.end() for m in re.finditer(r'<div class="wcat__grid">\n', s)]
    a = starts[nth]
    b = s.index("  </div>\n</section>", a)
    s = s[:a] + "    <!-- 최신순. Archive = 상세페이지 없음(링크 없음) -->\n\n" + "\n".join(cards) + s[b:]


replace_grid(0, PRODUCT)
replace_grid(1, UX)
rep("<span><b>13</b> Projects</span>", f"<span><b>{len(PRODUCT) + len(UX)}</b> Projects</span>")
rep("""      <a href="assets/portfolio.pdf" target="_blank" rel="noopener">PDF · 40 MB</a>
""", "")
rep("Portfolio v. 2026.08 — Industrial Design", "Portfolio v. 2026.10 — Industrial Design")
open(P, "w", encoding="utf-8", newline="\n").write(s)
print("work ok; '#' links:", s.count('href="#"'), "| projects:", len(PRODUCT) + len(UX))
