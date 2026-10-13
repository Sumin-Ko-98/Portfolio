"""2026-10-13 WADE 상세 정리 (1회성): 임시 수상 마크·빈 이미지 칸·자율주행 표현 제거, 실제 사진 채움.
사실 기준: LS 포트폴리오 인수인계 7절 (원격 조종 주행 + 자동 드로잉, 팀 5인, HCI 최우수상, 특허·디자인 등록)."""
import re, sys, os

P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "work", "wade.html")
s = open(P, encoding="utf-8").read()


def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n != count:
        sys.exit(f"expected {count} got {n}: {old[:70]!r}")
    s = s.replace(old, new)


def cut(start_marker, end_marker):
    """start_marker 부터 end_marker 직전까지 삭제"""
    global s
    a = s.index(start_marker)
    b = s.index(end_marker, a)
    s = s[:a] + s[b:]


IMG = lambda f, extra="": f'<img src="../assets/works/wade/{f}" alt="" loading="lazy"{extra}>'

# ---- head / hero / meta
rep('<div class="work-head__cat"><span class="num">2023</span>service robot</div>',
    '<div class="work-head__cat"><span class="num">2023</span>Service Robot · KIRO</div>')
rep("""    사용자가 터치 패널에 그린 그림을 <b>물로 바닥에 출력하는</b> 자율주행 서비스 로봇입니다.
    물로 그린 그림은 시간이 지나면 증발하기 때문에 따로 지울 필요가 없습니다.""",
    """    관람객이 터치 디스플레이에 그린 그림을 <b>물로 바닥에 출력하는</b> 놀이공원 서비스 로봇입니다.
    물로 그린 그림은 시간이 지나면 증발하기 때문에 따로 지울 필요가 없습니다.""")
rep('<img src="../assets/works/wade_cover.jpg" alt="Wade · product hero">',
    '<img src="../assets/works/wade/cover.jpg" alt="WADE 워터 드로잉 서비스 로봇">')
rep("""  <div class="meta__item"><span class="k">Year</span><span class="v">2023</span></div>
  <div class="meta__item"><span class="k">Client</span><span class="v">KIRO 한국로봇융합연구원 × 서울로봇아카데미</span></div>
  <div class="meta__item"><span class="k">Category</span><span class="v">Service Robot</span></div>
  <div class="meta__item"><span class="k">Role</span><span class="v">Product &amp; Service Design (디자인 100%)</span></div>
  <div class="meta__item"><span class="k">Output</span><span class="v">워킹 프로토타입</span></div>""",
    """  <div class="meta__item"><span class="k">Term</span><span class="v">2023.07 — 2023.08</span></div>
  <div class="meta__item"><span class="k">Client</span><span class="v">KIRO 서울로봇아카데미</span></div>
  <div class="meta__item"><span class="k">Team</span><span class="v">5인 (엔지니어 4 · 디자이너 1)</span></div>
  <div class="meta__item"><span class="k">Role</span><span class="v">외관 디자인 · 구조 설계 · 워킹 프로토타입 (디자인 기여도 100%)</span></div>
  <div class="meta__item"><span class="k">Output</span><span class="v">워킹 프로토타입 · 특허 · 디자인 등록</span></div>""")

# ---- awards: HCI + 특허 + 디자인 등록 (임시 IDEA / Red Dot 마크 삭제)
a = s.index("      <!-- ▼ 레이아웃 검증용 더미 2건")
b = s.index("    </ul>", a)
s = s[:a] + """      <li class="wd-award">
        <span class="wd-award__symbol wd-award__symbol--text">PAT</span>
        <span class="wd-award__body">
          <span class="wd-award__year">2026.03</span>
          <span class="wd-award__name">Patent</span>
          <span class="wd-award__note">특허 제10-2942532호 · 워터 드로잉을 위한 로봇 장치</span>
        </span>
      </li>
      <li class="wd-award">
        <span class="wd-award__symbol wd-award__symbol--text">DES</span>
        <span class="wd-award__body">
          <span class="wd-award__year">2024.10</span>
          <span class="wd-award__name">Design Reg.</span>
          <span class="wd-award__note">디자인 등록 제30-1280754호 · 지능형 서비스 로봇</span>
        </span>
      </li>
""" + s[b:]
rep('<span class="wd-award__note">Creative Award, Grand Prize</span>',
    '<span class="wd-award__note">Creative Award · Excellence Award (최우수상)</span>')

# ---- intro (자율주행 → 원격 조종 주행 + 자동 드로잉)
rep('<h2 class="wd-intro__h">물로 그림을 그리는 자율주행 서비스 로봇</h2>',
    '<h2 class="wd-intro__h">기다리는 시간을 볼거리로 바꾸는 워터 드로잉 로봇</h2>')
rep('<p class="wd-intro__h-en">An autonomous service robot that draws with water</p>',
    '<p class="wd-intro__h-en">A service robot that turns waiting time into a show, drawn in water</p>')
rep("""        WADE는 야외 바닥에 <b>물로 그림을 그리는</b> 자율주행 서비스 로봇입니다.
        사용자가 상단 터치 패널에 그림을 그리면 로봇이 이동하면서 그 형태를 바닥에 출력합니다.
        사람이 없는 구간에서는 스스로 워터드로잉을 실행해 방문객의 시선을 모읍니다.
        캐리커처와 캐릭터 드로잉, 상점 홍보 문구 출력, 물 도면을 이용한 길 안내와 대기열 안내를 제공합니다.
        물은 증발하기 때문에 청소가 필요하지 않고, 놀이공원과 페스티벌, 박람회처럼
        사람이 오래 머무는 장소에서 활용도가 높습니다.""",
    """        WADE는 야외 바닥에 <b>물로 그림을 그리는</b> 서비스 로봇입니다.
        놀이공원에서 가장 불편한 점으로 꼽힌 긴 대기줄(47.9%, 메타베이 2023.06)에서 출발해,
        대기 시간을 줄이는 대신 줄 옆 바닥에 그림을 그려 기다리는 시간을 볼거리로 바꾸는 컨셉입니다.
        관람객이 머리 위 터치 디스플레이에 그림을 그리면 그림을 20×12개의 점으로 바꾸고,
        로봇이 직진하는 동안 12개의 노즐이 한 줄씩 바닥에 물을 뿌려 출력합니다.
        물 그림은 소음 속에서도 눈에 띄고, 마르면 흔적 없이 사라집니다.""")
rep("""      WADE is an autonomous service robot that draws on outdoor ground surfaces with water.
      When a user draws on the upper touch panel, the robot moves forward and prints that
      shape onto the ground. In areas where no one is present, it runs a water-drawing
      routine on its own to attract visitors. The service covers caricature and character
      drawing, printed store promotions, and wayfinding or queue information drawn in water.
      Because the water evaporates, no cleaning is required, which makes the robot suitable
      for amusement parks, festivals, and expos where visitors stay for long periods.""",
    """      WADE is a service robot that draws on outdoor ground surfaces with water.
      It started from the long queues that visitors named as the biggest discomfort at
      amusement parks (47.9%, Metabay, June 2023): instead of shortening the wait, the robot
      draws next to the line and turns waiting time into something to watch. A visitor draws
      on the overhead touch display, the drawing is converted into a 20×12 dot grid, and
      twelve nozzles print it row by row while the robot drives straight. Water drawings stand
      out even in a noisy crowd and disappear without a trace once they dry.""")

# ---- image slots
rep('<div class="wd-dark-img reveal" data-label="Fig. 01 · Overview Scene"></div>',
    f'<div class="wd-dark-img reveal">{IMG("scene_print.jpg")}</div>')
cut("  <!-- 원형 이미지 슬롯 3개", '  <div class="wd-dark-row reveal">\n    <div class="wd-dark-row__mark">APPROACH</div>')
rep('<div class="wd-dark-img reveal" data-label="Fig. 05 · Context Scene" style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;"></div>',
    f'<div class="wd-dark-img reveal" style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;">{IMG("step_print.jpg")}</div>')
cut("<!-- 06.5 · FULL-BLEED PRODUCT SCENE", '<section data-om-id="731addee:om-section-7"')
rep('<div class="wd-bigsquare__frame reveal" data-label="Fig. 07 · Product Portrait"></div>',
    f'<div class="wd-bigsquare__frame wd-bigsquare__frame--portrait reveal">{IMG("scene_wait.jpg")}</div>')
rep('<div class="wd-trirow__cell reveal" data-label="Fig. 08"></div>',
    f'<div class="wd-trirow__cell reveal">{IMG("step_detect.jpg", chr(32) + "style=" + chr(34) + "object-position:72% 50%" + chr(34))}</div>')
rep('<div class="wd-trirow__cell reveal delay-1" data-label="Fig. 09"></div>',
    f'<div class="wd-trirow__cell reveal delay-1">{IMG("step_draw.jpg")}</div>')
rep('<div class="wd-trirow__cell reveal delay-2" data-label="Fig. 10"></div>',
    f'<div class="wd-trirow__cell reveal delay-2">{IMG("step_pixelate.jpg")}</div>')
cut("<!-- 10 · ASYMMETRIC DUO", '<section class="wd-textrow">\n  <div class="wd-textrow__label">Reach for Everyone</div>')
cut("<!-- 11 · TALL CLOSE-UP", "<!-- 11b · CAPTION")
cut("<!-- 12 · TWO-HAND SCENARIO", "<!-- 13b · CAPTION")
rep("""<section class="wd-detailduo">
  <div class="reveal" data-label="Fig. 16 · Camera"></div>
  <div class="reveal delay-1" data-label="Fig. 17 · USB-C"></div>
</section>""",
    f"""<section class="wd-detailduo wd-detailduo--wide">
  <div class="reveal">{IMG("inner_front.jpg")}</div>
  <div class="reveal delay-1">{IMG("inner_rear.jpg")}</div>
</section>""")
cut("<!-- 15 · STRAP TALL", "<!-- 17 · DARK PANEL #2 -->")
rep("""    <div data-label="Fig. 20"></div><div data-label="Fig. 21"></div><div data-label="Fig. 22"></div>
    <div data-label="Fig. 23"></div><div data-label="Fig. 24"></div><div data-label="Fig. 25"></div>""",
    "    " + "".join(f'<div title="{t}">{IMG(f)}</div>' for f, t in [
        ("build_paint.jpg", "01 외장 3D 프린팅·도장"), ("build_chassis.jpg", "02 플랫폼·배선"),
        ("build_head.jpg", "03 헤드 프로토타입 제작"), ("build_valves.jpg", "04 방수 설계"),
        ("test_print.jpg", "05 출력 테스트"), ("build_assembly.jpg", "06 조립")]))
cut("  <!-- BW people mosaic", '  <div class="wd-dark-row reveal">\n    <div class="wd-dark-row__mark">IN THE FIELD</div>')
rep("""<section class="wd-bleed wd-bleed--final">
  <div class="wd-bleed__frame reveal" data-label="Fig. 30 · Final Lifestyle"></div>
</section>""",
    f"""<section class="wd-bleed wd-bleed--final">
  <div class="wd-bleed__frame wd-bleed__frame--photo reveal" style="aspect-ratio: 1800 / 638;">{IMG("print_field.jpg")}</div>
</section>""")

# ---- text facts
rep("""변화를 더해 사용자가 로봇의 상태를 확인하면서 조작하도록 했습니다. 감정
        의인화 표현을 다룬 연구는 IDEA 2024 국제디자인학회에 논문으로 발표했습니다.""",
    """변화를 더해 사용자가 로봇의 상태를 확인하면서 조작하도록 했습니다. 캐릭터성은
        절제하고 직선을 줄인 유선형으로 다듬어 불쾌한 골짜기를 피했습니다.""")
rep("""        status while operating it. The study on emotional personification was published
        at IDEA 2024, the International Design Conference.""",
    """        status while operating it. The character was kept restrained, with a streamlined
        form and fewer straight lines, to avoid the uncanny valley.""")
rep("컨셉과 시나리오를 함께 정한 뒤 서비스 로봇과 자율주행, LabVIEW 교육을 이수하고",
    "컨셉과 시나리오를 함께 정한 뒤 서비스 로봇과 LabVIEW 교육을 이수하고")
rep("the team completed coursework in service robotics, autonomous driving, and LabVIEW,",
    "the team completed coursework in service robotics and LabVIEW,")
rep("운용 시나리오는 GPS 기반 자율주행, 사람을 인식해 정지하고 그림을 받는 단계, 0.5m/s로 직진하며 출력하는 단계로 구성했습니다.",
    "프로토타입은 원격 조종으로 주행하고, 사람을 인식해 정지한 뒤 그림을 받고, 0.5m/s로 직진하며 12개 노즐로 출력합니다. 34°C에서도 물 그림이 5분 이상 유지됐습니다.")
rep("The operating scenario consisted of GPS-based autonomous driving, detecting a person and stopping to receive a drawing, and printing while advancing straight at 0.5 m/s.",
    "The prototype is driven by remote control; it detects a person, stops to receive a drawing, and prints with twelve nozzles while advancing straight at 0.5 m/s. At 34°C the water drawings stayed visible for more than five minutes.")
rep("이 프로젝트로 HCI KOREA 2024 Creative Award 최우수상을 받았습니다.",
    "이 프로젝트로 HCI KOREA 2024 Creative Award 최우수상을 받았고, 특허(제10-2942532호)와 디자인(제30-1280754호)을 등록했습니다.")
rep("The project received the Creative Award, Grand Prize, at HCI KOREA 2024.",
    "The project received the Excellence Award (최우수상) at the HCI KOREA 2024 Creative Award and was granted a patent (No. 10-2942532) and a design registration (No. 30-1280754).")

# ---- pager / footer
rep("""  <a href="../work.html" class="left">
    <span class="pager__label">All Works</span>
    <span class="pager__title">← Index</span>
  </a>
  <a href="#" class="right">
    <span class="pager__label">Next Project</span>
    <span class="pager__title">Threespin →</span>
  </a>""",
    """  <a href="odm-cmf.html" class="left">
    <span class="pager__label">Previous</span>
    <span class="pager__title">← ODM CMF</span>
  </a>
  <a href="inclusive.html" class="right">
    <span class="pager__label">Next Project</span>
    <span class="pager__title">Inclusive Mobility →</span>
  </a>""")
rep('<a href="mailto:hello@sumin.co">hello@sumin.co</a>', '<a href="mailto:ssom98@naver.com">ssom98@naver.com</a>')
rep("Portfolio v. 2026.09 — Industrial Design", "Portfolio v. 2026.10 — Industrial Design")
rep("<title>", "<title>", 1)

# ---- CSS for filled slots
rep("</style>\n</head>", """/* 2026.10 — 실제 사진이 들어간 칸 */
[data-label]:has(img)::after, .wd-trirow__cell:has(img)::after, .wd-bigsquare__frame:has(img)::after,
.wd-detailduo > div:has(img)::after { content: none; }
.wd-trirow__cell img, .wd-detailduo > div img, .wd-protogrid > div img, .wd-dark-img img {
  display: block; width: 100%; height: 100%; object-fit: cover;
}
.wd-bigsquare__frame--portrait { aspect-ratio: 1648 / 2208; max-width: 760px; margin: 0 auto; background: #ececec; }
.wd-bigsquare__frame--portrait img { display: block; width: 100%; height: 100%; object-fit: cover; }
.wd-detailduo--wide > div { aspect-ratio: 16 / 9; }
.wd-award__symbol--text {
  display: grid; place-items: center; border: 1px solid var(--hair); border-radius: 50%;
  font-family: var(--f-mono); font-size: 11px; letter-spacing: 0.08em; color: var(--ink);
}
</style>
</head>""")

open(P, "w", encoding="utf-8", newline="\n").write(s)
left = re.findall(r'data-label="Fig[^"]*"', s)
print("done; remaining placeholder slots:", left)
print("autonomous/자율주행 left:", [m.start() for m in re.finditer("자율주행|[Aa]utonomous|IDEA 2024|hello@", s)])
