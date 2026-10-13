"""2026-10-13 About / Contact 정리 (1회성).
근거: LS 포트폴리오 p2(About Me), 학위수여증명서(2021.09 입학 · 2024.02 학위수여), 수상 증명서(iF 2026.03, GD 2026.08.21),
HCI KOREA 2024 수상 페이지(최우수상 = 대상 아래 2등급 → Grand Prize 아님), IEA 2024 논문은 저자 아님 → 삭제."""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def fix(name, pairs):
    p = os.path.join(ROOT, name)
    s = open(p, encoding="utf-8").read()
    for old, new in pairs:
        n = s.count(old)
        if n != 1:
            sys.exit(f"{name}: expected 1 got {n}: {old[:80]!r}")
        s = s.replace(old, new)
    open(p, "w", encoding="utf-8", newline="\n").write(s)
    print(name, "ok")


FOOTER_PDF = '      <a href="assets/portfolio.pdf" target="_blank" rel="noopener">PDF · 40 MB</a>\n'
VERSION = ("Portfolio v. 2026.08 — Industrial Design", "Portfolio v. 2026.10 — Industrial Design")

fix("about.html", [
    ("    자율주행 로봇의 외형에서부터 공유 셔틀의 내부 경험까지,\n",
     "    로봇청소기와 전동휠체어부터 미래 모빌리티의 실내 경험까지,\n"),
    ("""    <h3>Biography</h3>
    <p>
      홍익대학교 산업디자인전공에서 <b>석사 학위</b>를 마쳤습니다.""",
     """    <h3>Biography</h3>
    <p>
      에브리봇 디자인 R&amp;D 센터에서 <b>로봇청소기, 소형가전, 전동휠체어</b>를 디자인합니다.
      스케치·3D 모델링부터 CMF, 목업, 양산 지원까지 출시 전 과정을 맡고,
      팀의 UI·CMF·사양서 기준도 만들어 운영합니다.
    </p>
    <p>
      홍익대학교 대학원 산업디자인전공에서 <b>석사 학위</b>를 마쳤습니다."""),
    ("""      <b>모빌리티·로보틱스·제품</b> 분야를 중점적으로 다루며,
      2024년 HCI KOREA에서 <b>Creative Award 최우수상</b>을,
      IDEA International Design Excellence Awards와 SPARK Design Award에서
      <b>Finalist</b>에 선정되었습니다.""",
     """      쓰리스핀 슬림(TS450)으로 <b>iF 디자인 어워드 2026 Gold</b>, 레드닷 디자인 어워드,
      굿디자인(GD) 선정을 받았고, 대학원에서는 HCI KOREA 2024 <b>Creative Award 최우수상</b>을 받았으며
      IDEA와 Spark Design Awards에서 Finalist에 선정되었습니다."""),
    ("""      <time>2022 — 2024</time>
      <div>
        <h4>홍익대학교 대학원 · 산업디자인전공 석사</h4>
        <p>Thesis · Water Drawing Entertainment Robot Using Appropriate Technology Based on Design Thinking</p>""",
     """      <time>2021.09 — 2024.02</time>
      <div>
        <h4>홍익대학교 대학원 · 산업디자인전공 석사</h4>
        <p>미술학석사 · 디자인학부 산업디자인</p>"""),
    ("""      <time>2017 — 2021</time>""", """      <time>2017 — 2021.02</time>"""),
    ("""    <div class="tl-item">
      <time>2024.04 — 2024.04</time>""",
     """    <div class="tl-item">
      <time>2025.11 — 2026.10</time>
      <div><h4>에브리봇 · TS700 쓰리스핀 스팀</h4><p>제품디자인 · 양산 지원</p></div>
    </div>
    <div class="tl-item">
      <time>2025.12 — 2026.04</time>
      <div><h4>에브리봇모빌리티 · H500 수전동휠체어</h4><p>컨트롤러 · 인휠모터 휠 디자인</p></div>
    </div>
    <div class="tl-item">
      <time>2024.05 — 2026.10</time>
      <div><h4>에브리봇 · 맥스젠 · 에브리봇모빌리티</h4><p>ODM 양산 제품 CMF 디자인 16종</p></div>
    </div>
    <div class="tl-item">
      <time>2024.07 — 2025.12</time>
      <div><h4>에브리봇 · TS450 쓰리스핀 슬림</h4><p>물걸레 로봇청소기 제품디자인</p></div>
    </div>
    <div class="tl-item">
      <time>2024.04</time>"""),
    ("""      <div><h4>KIRO · 서울로봇아카데미</h4><p>모바일 로봇 디자인 엔지니어</p></div>""",
     """      <div><h4>KIRO · 서울로봇아카데미</h4><p>모바일 로봇 디자인 엔지니어 과정 수료 · WADE</p></div>"""),
    ("""      <time>2022.09 — 2022.10</time>""", """      <time>2022.09 — 2022.11</time>"""),
    ("""      <time>2024.01</time>
      <div><h4>HCI KOREA 학술대회</h4><p>Creative Award 논문 투고 및 전시</p></div>""",
     """      <time>2023.12 — 2024.01</time>
      <div><h4>HCI KOREA 학술대회</h4><p>Creative Award 작품 발표 · 전시</p></div>"""),
    ("""    <div class="skill reveal delay-2"><h4>Auto CAD</h4><div class="bar" style="--v:50%"></div><span class="val">50 · Working</span></div>""",
     """    <div class="skill reveal delay-2"><h4>AI Tools</h4><span class="val">VIZCOM · Claude Code</span></div>"""),
    ("""      <time>2026.04</time>
      <span class="award-logo"><img src="assets/awards/if-gold.png" alt="iF Design Award Gold"></span>
      <h4>iF Design Award — 2026 Gold Winner</h4>""",
     """      <time>2026.03</time>
      <span class="award-logo"><img src="assets/awards/if-gold.png" alt="iF Design Award Gold"></span>
      <h4>iF Design Award 2026 — Gold</h4>"""),
    ("""      <h4>Red Dot Design Award — Winner</h4>""", """      <h4>Red Dot Award: Product Design 2026</h4>"""),
    ("""      <time>2026</time>
      <span class="award-logo"><img src="assets/awards/gooddesign.png" alt="Good Design Award"></span>
      <h4>Good Design Award — Winner</h4>""",
     """      <time>2026.08</time>
      <span class="award-logo"><img src="assets/awards/gooddesign.png" alt="Good Design Korea"></span>
      <h4>Good Design Korea 2026 — GD 선정</h4>"""),
    ("""      <h4>HCI Korea · Creative Award, 최우수상</h4>""",
     """      <h4>HCI KOREA 2024 · Creative Award, Excellence Award (최우수상)</h4>"""),
    ("""    <h2 class="h-2 reveal">Thesis.</h2>
    <span class="mono reveal delay-1">Published research</span>
  </header>
  <ul class="honors__list honors__list--nosymbol">
    <li class="reveal">
      <time>2024.04</time>
      <h4>Water Drawing Entertainment Robot Using Appropriate Technology Based on Design Thinking — Emotional personification expression</h4>
      <p>국제인간공학회 (IEA 2024) · Proposal No. 419</p>
    </li>
""",
     """    <h2 class="h-2 reveal">Publications.</h2>
    <span class="mono reveal delay-1">Papers · Patents</span>
  </header>
  <ul class="honors__list honors__list--nosymbol">
    <li class="reveal">
      <time>2026.03</time>
      <h4>특허 등록 — 워터 드로잉을 위한 로봇 장치 및 이를 포함하는 로봇 시스템</h4>
      <p>제10-2942532호 · 고수민 외 3인</p>
    </li>
    <li class="reveal">
      <time>2024.10</time>
      <h4>디자인 등록 — 지능형 서비스 로봇</h4>
      <p>제30-1280754호 · 고수민 외 3인</p>
    </li>
"""),
    ("""      <p>기초조형학연구 25권 1호 (통권 121호) · KCI 등재</p>""",
     """      <p>기초조형학연구 25권 1호 (통권 121호) · KCI 등재 · 고수민, 김은영</p>"""),
    ("""      <p>기초조형학연구 24권 6호 (통권 120호) · KCI 등재</p>""",
     """      <p>기초조형학연구 24권 6호 (통권 120호) · KCI 등재 · 고수민 외 4인</p>"""),
    (FOOTER_PDF, ""),
    VERSION,
])

fix("contact.html", [
    ("""    <a class="row__value" href="assets/portfolio.pdf" target="_blank" rel="noopener" data-hover>Portfolio.pdf</a>
    <span class="row__aside">40 MB · Updated 2024.04</span>""",
     """    <a class="row__value" href="about.html#resume" data-hover>About · Resume</a>
    <span class="row__aside">Updated 2026.10</span>"""),
    ("""      <a href="assets/portfolio.pdf" target="_blank" rel="noopener">PDF · 40 MB</a>\n""", ""),
    VERSION,
])
