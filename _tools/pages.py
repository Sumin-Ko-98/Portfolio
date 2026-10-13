"""상세페이지 내용. 사실 기준 = LS 포트폴리오 _시안/인수인계.md 7절 + portfolio.html (2026-10 최종).
lede / text 문단은 HTML 그대로 들어간다(<b> 사용 가능, & 는 &amp; 로).

블록 종류
  ("text", 라벨, 리드문 또는 None, [문단...])
  ("row", [(파일, 캡션), ...])           한 줄 이미지, 높이 맞춤·줄 폭 꽉
  ("grid", 열수, [(파일, 캡션), ...], (MORE 제목, 설명) 또는 None)
  ("items", [(번호, 제목, 설명), ...])
  ("facts", [(라벨, 값, 메모), ...])
  ("part", 번호, 제목)                    큰 구분 제목
  ("role", [역할, ...])
캡션은 "English · 한국어 설명" 형태면 앞부분이 작은 라벨로 표시된다.
"""

# 상세페이지 이전/다음 순서 (wade 는 손으로 관리하는 페이지지만 순서에는 포함)
ORDER = ["threespin", "ts700", "h500", "odm-cmf", "wade", "inclusive", "seuv", "ev-sedan"]

PAGES = {}

PAGES["threespin"] = dict(
    dir="ts450", cat_key="product",
    title="Threespin Slim", year="2024 — 2025", category="Robot Mop · Everybot",
    desc="쓰리스핀 슬림 TS450 물걸레 로봇청소기 제품디자인",
    lede="에브리봇이 10년 이상 축적한 ROBO-SPIN 기술을 바탕으로 <b>브랜드 역사상 가장 슬림하게</b> 완성한 "
         "물걸레 로봇청소기입니다. 낮은 바디로 소파·침대 아래까지 청소 범위를 넓히고, 오프 화이트 매트 마감과 "
         "심리스한 곡면으로 거실의 오브제처럼 자리하도록 디자인했습니다.",
    hero="cover.jpg",
    meta=[("Term", "2024.07 — 2025.12"), ("Client", "에브리봇"), ("Product", "쓰리스핀 슬림 TS450"),
          ("Category", "물걸레 로봇청소기"), ("Output", "양산 출시")],
    awards=[("if", "2026.04", "iF Design Award 2026 · Gold"), ("reddot", "2026.04", "Red Dot Design Award · Winner"),
            ("gd", "2026.09", "Good Design (GD) · 선정")],
    blocks=[
        ("text", "Overview", "공간에 스며드는 미니멀 오브제",
         ["낮은 높이와 단순한 형태, 끊김 없는 곡면으로 가전보다 오브제에 가까운 인상을 만들었습니다."]),
        ("facts", [("Height", "83mm", "쓰리스핀 시리즈 최저 높이"), ("Pads", "3", "ROBO-SPIN 회전 패드"),
                   ("Buttons", "2", "시작·정지 / 물 공급량")]),
        ("row", [("overview_life.jpg", "")]),
        ("text", "Form", "낮음 · 단순함 · 심리스",
         ["세 가지 조형 원칙 아래 형태를 정리했습니다."]),
        ("items", [
            ("01", "Triangle Form",
             "ROBO-SPIN 구조의 세 회전 패드 배치가 그대로 삼각형 외형으로 이어졌습니다. 다양한 R값으로 모서리를 다듬어 "
             "원형 로봇청소기와 다른 조형 언어를 만들었고, 본체를 360도로 두르는 블랙 센서창 라인이 시선을 가로로 이끕니다. "
             "센서가 없는 양옆은 하이글로시 블랙 파트로 이어 끊김 없는 띠로 보이게 했습니다."),
            ("02", "Low Proportion",
             "상단부 두께를 최소화하고 측면 라인이 바닥으로 흘러내리도록 처리해 바닥에 밀착된 인상을 줍니다. "
             "개발 중 IR 센서가 측후면으로 이동한 뒤에도 손잡이·상면 곡률·센서창 비율을 함께 조정해 이 라인을 유지했습니다."),
        ]),
        ("row", [("form_pers.jpg", "Perspective"), ("form_side.jpg", "Side")]),
        ("text", "Sensor Protection", "센서창 스크래치 VOC를 바디 형상으로 해결",
         ["이전 모델에서 접수된 센서창·가구 스크래치 VOC를 바디 형상으로 해결했습니다."]),
        ("items", [
            ("01", "센서창 보호 단차",
             "이전 모델은 센서창이 바디와 같은 면에 있어 가구에 직접 부딪혔고, 센서창과 가구에 스크래치가 생겼습니다. "
             "상·하단 바디를 센서창보다 바깥으로 내밀어 단차를 주어 부딪혀도 바디가 먼저 닿게 했습니다."),
            ("02", "크래들 비접촉 거치",
             "크래들에 거치할 때도 센서창이 크래들에 직접 닿는 면을 없애 스크래치를 막았습니다."),
        ]),
        ("row", [("sensor_before.jpg", "Before · 이전 모델 — 센서창과 바디가 같은 면"),
                 ("sensor_after.jpg", "After · TS450 — 상·하단 바디가 센서창보다 돌출")]),
        ("row", [("sensor_cradle.jpg", "Cradle · 거치 시 센서창이 크래들에 닿지 않는 구조")]),
        ("text", "Technology & UI", None,
         ["구동 바퀴 없이 세 개의 회전 패드만으로 이동과 청소를 동시에 수행합니다. 본체 무게가 세 패드에 실려 바닥을 눌러 닦습니다."]),
        ("items", [
            ("01", "ROBO-SPIN", "구동 바퀴 없이 세 개의 회전 패드로 이동과 청소를 동시에 수행합니다."),
            ("02", "Simple UI", "시작·정지와 물 공급량 버튼 2개, 작동 상태를 알리는 라이트 라인, 음성 안내만으로 매뉴얼 없이 조작합니다."),
            ("03", "Mop Pads", "세 개의 회전 패드는 손쉽게 탈착·세탁할 수 있고, 세탁 후 반복 사용합니다."),
        ]),
        ("row", [("robospin.jpg", "ROBO-SPIN"), ("ui.jpg", "Simple UI")]),
        ("row", [("mop_pads.jpg", "Mop Pads")]),
        ("text", "Storage & CMF", None,
         ["본체를 세워 결합하는 수직형 거치대로 보관 면적을 줄였습니다. 거치대도 본체와 같은 곡면·컬러·마감으로 통일해 "
          "보관 중에도 하나의 오브제로 읽힙니다.",
          "도장 없이 착색 레진으로 사출해 색과 표면을 완성하는 <b>원착(무도장) 사출</b>로 마감했습니다."]),
        ("row", [("cradle_shelf.jpg", "Vertical Cradle"), ("exploded_pad.jpg", "Exploded View")]),
        ("text", "Mock-up", None,
         ["1:1 목업과 샘플로 비율·센서창 라인·CMF를 확인하고, 기구설계팀과 구조를 함께 검토했습니다."]),
        ("row", [("mockup_1201.jpg", ""), ("mockup_5465.jpg", ""), ("mockup_5981.jpg", "")]),
        ("role", ["시장·트렌드·경쟁 제품 리서치", "컨셉·제품디자인", "UX 디자인", "스케치·2D 렌더링", "3D 모델링·렌더링",
                  "CMF", "목업 제작 감리", "디자인 사양서", "양산 지원", "마케팅 이미지 소스 지원", "어워드 출품"]),
    ],
)

PAGES["ts700"] = dict(
    dir="ts700", cat_key="product",
    title="Threespin Steam", year="2025 — 2026", category="Robot Mop · Everybot",
    desc="쓰리스핀 스팀 TS700 제품디자인 · 양산 지원",
    lede="스팀 모듈을 탑재한 쓰리스핀 로봇청소기입니다. 높아진 전고를 <b>슬림한 실루엣</b>으로 보이게 하고, "
         "<b>서비스성을 높인 하우징 분할 구조</b>를 설계하는 데 집중했습니다.",
    hero="cover.jpg",
    meta=[("Term", "2025.11 — 2026.10"), ("Client", "에브리봇"), ("Product", "쓰리스핀 스팀 TS700"),
          ("Category", "스팀 물걸레 로봇청소기"), ("Status", "양산 지원 진행 중")],
    blocks=[
        ("text", "Overview", "높아진 전고와 서비스성, 두 가지 문제",
         ["스팀 모듈 탑재로 높아진 전고와 하우징의 서비스성 문제를 디자인으로 해결했습니다."]),
        ("items", [
            ("01", "Slim Look", "대형 챔퍼와 다크 하단으로 높아진 전고를 슬림하게"),
            ("02", "3-Part Body", "바텀·미들·탑 3분할로 하단 모듈 서비스성 개선"),
            ("03", "Steam Module", "쓰리스핀 구동부 위 스팀 모듈 · 세워 보관하는 거치대"),
        ]),
        ("row", [("overview_main.jpg", "")]),
        ("row", [("view_front.jpg", "Front"), ("view_side.jpg", "Side"), ("view_bottom.jpg", "Bottom"),
                 ("view_cradle.jpg", "Cradle")]),
        ("text", "Slim Look", None,
         ["로봇청소기 시장에서는 전고가 낮을수록 제품 가치가 높게 평가되지만, 스팀 모듈 탑재로 전고가 크게 높아졌습니다.",
          "바텀 하우징 엣지에 <b>대형 챔퍼</b>를 적용해 측면 볼륨을 덜어내고, 바텀 파트에 <b>다크 톤 CMF</b>를 적용해 "
          "하단부가 시각적으로 후퇴하도록 했습니다. 이를 통해 사용자의 시선 각도에서 실제 전고 대비 슬림한 실루엣으로 "
          "인지되도록 디자인했습니다."]),
        ("row", [("eye_angle.png", "")], "narrow"),
        ("text", "3-Part Body", None,
         ["기존 자사 제품은 깊은 바텀 하우징과 얕은 탑 하우징의 2분할 구조로 원가는 절감했지만, A/S 시 하단 모듈에 "
          "접근하려면 상단 모듈을 모두 분해해야 해 서비스성이 낮았습니다.",
          "바디를 <b>바텀·미들·탑 3분할 구조</b>로 재구성해, 상단 전체를 해체하지 않고도 하단 모듈에 접근할 수 있도록 "
          "서비스성을 개선했습니다."]),
        ("row", [("three_part_body.png", "")], "narrow"),
        ("text", "Product Details", None,
         ["디자인 이후 UI·음성, CMF, 양산 단계까지 이어서 맡아 제품 완성도를 관리했습니다."]),
        ("row", [("detail_top_cover.jpg", "Top Cover · 상단 커버를 열어 물통·스팀 모듈에 접근"),
                 ("detail_storage.jpg", "Storage · 거치대에 세워 보관")]),
        ("items", [
            ("UI · Sound", "표시 UI · 음성 안내", "동작 사양에 따른 표시 UI, 음성 안내, 효과음·TTS 제작"),
            ("CMF", "컬러 · 마감 확정", "컬러칩 · 한도견본으로 확정, 실크 · 레이저 마킹 검수"),
            ("Mass Production", "양산 지원", "디자인 사양서 · 시사출 검토 · 금형 수정 요청 · 마케팅 렌더링"),
        ]),
        ("text", "Mock-up", None, ["목업으로 외관과 내부 구조를 확인하고, 시사출 외관을 검토했습니다."]),
        ("row", [("mockup_1109.jpg", ""), ("mockup_2325.jpg", ""), ("mockup_1665.jpg", "")]),
        ("role", ["시장·트렌드·경쟁 제품 리서치", "컨셉·제품디자인", "UX 디자인", "스케치·2D 렌더링", "3D 모델링·렌더링",
                  "UI·음성 안내 설계(효과음·TTS)", "CMF", "목업 제작 감리", "디자인 사양서", "양산 지원",
                  "마케팅 이미지 소스 지원"]),
    ],
)

PAGES["h500"] = dict(
    dir="h500", cat_key="product",
    title="H500", year="2025 — 2026", category="Wheelchair · Everybot Mobility",
    desc="에브리봇모빌리티 H500 수전동휠체어 컨트롤러 · 인휠모터 휠 디자인",
    lede="수전동휠체어 H500의 <b>컨트롤러</b>와 <b>인휠모터 휠</b>을 디자인했습니다. 손 힘이 약한 사용자도 정확하게 "
         "조작할 수 있는 컨트롤러와, 구동부를 허브에 담고 컬러 커스텀을 고려한 휠입니다.",
    hero="ctrl_cover.jpg",
    meta=[("Term", "2025.12 — 2026.04"), ("Client", "에브리봇모빌리티"), ("Product", "H500 수전동휠체어"),
          ("Scope", "컨트롤러 · 인휠모터 휠"), ("Output", "3D 프린팅 목업 · CMF 목업")],
    blocks=[
        ("part", "01", "Controller"),
        ("text", "Controller", "손을 받친 채 쓰는 컨트롤러",
         ["손 힘이 약한 사용자도 놓치지 않고 정확하게 조작할 수 있도록, 손을 받친 채 쓰는 컨트롤러를 디자인했습니다."]),
        ("row", [("ctrl_living.jpg", "In Use · 팔걸이에 장착해 사용하는 모습"),
                 ("ctrl_mockup.jpg", "Mock-up · 3D 프린팅 목업으로 쥐고 조작하며 검증")]),
        ("items", [
            ("01", "Joystick & Palm Rest", "벨로즈로 감싼 조이스틱 옆 텍스처 팜레스트로 손을 받친 채 조작"),
            ("02", "Button Grouping", "레드 전원 버튼을 중앙에, 방향 버튼을 주위에 모아 기능별로 묶음"),
            ("03", "Display", "표시부를 버튼 위에 두어 누르는 손에 가려지지 않게 함"),
            ("04", "Mock-up", "3D 프린팅 목업으로 직접 쥐고 조작하며 형상과 배치를 다듬음"),
        ]),
        ("text", "Final Design", None, ["레드 전원 버튼을 중심으로 라이트·비상등·경적 버튼을 배치하고, 측면에 벨로즈 조이스틱과 팜레스트를 두었습니다."]),
        ("row", [("ctrl_pers.jpg", "Perspective"), ("ctrl_top.jpg", "Top"), ("ctrl_side.jpg", "Side · 벨로즈 조이스틱 · 팜레스트")]),
        ("role", ["컨트롤러 디자인", "UX 디자인 (조작 형상·버튼 배치·오조작 방지·표시부 가독성)", "3D 프린팅 목업 검증"]),
        ("part", "02", "In-wheel Motor Wheel"),
        ("text", "Wheel", "휠 하나로 완결한 구동부",
         ["인휠모터를 허브에 담아 휠 하나로 구동부를 완결했습니다. 원하는 컬러로 커스텀할 수 있도록 확장성을 고려해 디자인했습니다."]),
        ("row", [("wheel_chair_side.jpg", "Mounted · 휠체어에 장착한 모습"),
                 ("wheel_rim_hand.jpg", "Hand Rim · 핸드림을 잡고 수동 주행")]),
        ("items", [
            ("Hub", "인휠모터 허브", "인휠모터를 허브에 담아 휠 하나로 구동부를 완결"),
            ("Spoke", "3-스포크 · 컬러 커스텀", "스포크 인서트를 원하는 컬러로 커스텀할 수 있도록 확장성을 고려한 디자인"),
            ("Hand Rim", "메탈 핸드림", "손으로 수동 주행할 때를 고려해 핸드림의 두께와 휠과의 간격을 설정"),
        ]),
        ("row", [("wheel_render_24.jpg", "")], "narrow"),
        ("text", "Mock-up & CMF", None, ["스포크 커버 컬러와 핸드림 마감을 실물 목업과 컬러칩으로 비교했습니다."]),
        ("row", [("wheel_cmf_mockup.jpg", "CMF Mock-up · 스포크 커버 컬러 비교 · 핸드림 블랙 / 실버"),
                 ("wheel_color_chips.jpg", "Color Chips · 5종"), ("wheel_white_mockup.jpg", "White Spoke · 목업")]),
        ("role", ["인휠모터 휠 디자인", "3D 모델링", "CMF"]),
    ],
)

PAGES["odm-cmf"] = dict(
    dir="odm", cat_key="product",
    title="ODM CMF", year="2024 — 2026", category="CMF Design · 16 Models",
    desc="에브리봇 · 맥스젠 · 에브리봇모빌리티 ODM 양산 제품 CMF 디자인 16종",
    lede="중국 ODM 제조사가 설계·디자인한 제품의 <b>색상·소재·마감·실크</b>를 담당했습니다. 브랜드 톤을 유지하면서 "
         "모델마다 차이가 드러나도록 정리했고, Q7 PLUS는 물통 커버 금형 수정, Q9은 스테이션 커버 신규 제작까지 맡았습니다.",
    hero=None,
    meta=[("Term", "2024.05 — 2026.10"), ("Client", "에브리봇 · 맥스젠 · 에브리봇모빌리티"), ("Partner", "중국 ODM 제조사"),
          ("Scope", "CMF · 금형 수정 · 신규 커버"), ("Output", "양산 제품 16종")],
    blocks=[
        ("row", [("q9.jpg", "Q9 · 스테이션 커버 신규 제작"), ("q7_plus.jpg", "Q7 PLUS · 물통 커버 금형 수정"), ("b1.jpg", "B1 · 욕실로봇청소기")]),
        ("facts", [("Everybot", "13", "에브리봇"), ("Maxzen", "2", "맥스젠"), ("Everybot Mobility", "1", "에브리봇모빌리티")]),
        ("text", "CMF Line-up", None,
         ["디자인 사양서와 CMF 가이드를 제조사에 전달하고, 도장 목업 제작을 감리하고, 양산 샘플을 검수했습니다."]),
        ("grid", 4, [
            ("q3_turbo.jpg", "Q3 Turbo"), ("q3_turbo_s.jpg", "Q3 Turbo S"),
            ("q7_plus.jpg", "Q7 PLUS · 물통 커버 금형 수정"), ("q9.jpg", "Q9 · 스테이션 커버 신규 제작"),
            ("q9_plus.jpg", "Q9 PLUS"), ("q11.jpg", "Q11"), ("q13.jpg", "Q13"), ("q7.jpg", "Q7"),
            ("ts402m.jpg", "TS402M"), ("b1.jpg", "B1 · 욕실로봇청소기"), ("x1.jpg", "X1"), ("x2.jpg", "X2"),
            ("sr13w.jpg", "SR13W · 맥스젠 흡입스팀다리미"),
        ], ("+ MORE", "TS800 · SR15W(맥스젠) · H300(에브리봇모빌리티)")),
        ("role", ["CMF 디자인", "금형 수정·신규 커버 디자인", "도장 목업 제작 감리", "디자인 사양서·CMF 가이드 전달",
                  "샘플 검수", "마케팅 이미지 소스 지원"]),
    ],
)

# ---------------- UX (현대자동차 산학 3건) ----------------
# 인수인계 8절 3번: 옛 포트폴리오에 근거 없는 수치(도어 폭 mm, 인원수, 모드 수, 인치, 살균 시간 등)는 넣지 않는다.

PAGES["inclusive"] = dict(
    dir="inclusive", cat_key="ux",
    title="Inclusive Mobility", year="2023", category="UX Research · Hyundai",
    desc="현대자동차 Inclusive 기반 미래 모빌리티 UX디자인 및 편의장치 개발",
    lede="시각·청각 장애인부터 노약자, 어린이까지 <b>누구나 안전하게 타고 내릴 수 있는 PBV</b>의 UX 요소와 편의장치를 "
         "설계하고, 3D 프린팅과 1:1 폼보드 목업으로 검증했습니다.",
    hero="door_ramp.jpg",
    meta=[("Term", "2023.02 — 2023.05"), ("Client", "현대디자인센터 퓨처모빌리티디자인팀"),
          ("Team", "석사연구원 4 · 학부연구원 3"), ("Method", "애자일 · 1:1 프로토타입"),
          ("Role", "선행 연구 · UX 아이템 발굴 · 프로토타입 · 검증")],
    blocks=[
        ("text", "Boarding", "Door &amp; Door Step",
         ["이중 개폐 도어로 출입구를 넓게 열고, 도어스텝이 계단 또는 경사판으로 내려와 휠체어 이용자도 바로 탈 수 있게 했습니다. "
          "보조도어의 투명 디스플레이로 승하차 방향을 안내하고, 탑승 가능 여부를 빛으로 알립니다.",
          "도어와 도어스텝은 1:1 목업으로 만들어 휠체어로 직접 진입하며 폭과 경사를 확인했습니다."]),
        ("row", [("door_wheelchair_test.jpg", "Mock-up · 1:1 도어 목업 진입 테스트"),
                 ("doorstep_led_test.jpg", "Mock-up · LED 도어스텝 목업")]),
        ("text", "Interior", None, ["실내에서는 일어서고 앉는 동작, 휠체어 고정, 좌석 배치를 다뤘습니다."]),
        ("items", [
            ("01", "Assist Seat", "팔걸이를 짚고 일어나면 시트가 따라 올라와 일어서는 동작을 돕습니다."),
            ("02", "Wheelchair Lock", "바퀴가 버튼을 누르면 고리가 나와 휠체어를 고정합니다."),
            ("03", "Seat Layout", "휠체어 탑승 공간을 고려해 좌석 배치를 구성했습니다."),
        ]),
        ("row", [("assist_pair.jpg", "Assist Seat"), ("s_wc_lock.jpg", "Wheelchair Lock")]),
        ("row", [("s_seat_layout.jpg", "Seat Layout · 좌석 배치")], "narrow"),
        ("text", "More", None, ["바닥·외부 커뮤니케이션 요소도 함께 제안하고 일부는 실물로 만들어 확인했습니다."]),
        ("row", [("nonslip_pattern.jpg", "Non-slip · 논슬립 이중 그래픽"), ("wheelchair_fold.jpg", "Mock-up · 휠체어 목업")]),
        ("row", [("s_laser.jpg", "Guide · 레이저 진입 가이드"), ("s_ehmi_front.jpg", "eHMI · 횡단 안내"),
                 ("s_tdisplay.jpg", "Display · 실내 디스플레이")]),
        ("role", ["선행 연구", "UX 아이템 발굴", "프로토타입 제작", "UX 리서치 및 검증"]),
    ],
)

PAGES["seuv"] = dict(
    dir="seuv", cat_key="ux",
    title="SeUV UX", year="2022 — 2023", category="UX Research · Hyundai",
    desc="현대자동차 대형 SeUV 공간 및 웰니스 컨셉 USP 항목 UX디자인",
    lede="대형 SeUV의 <b>실내 공간과 웰니스 경험</b>을 위한 컨셉을 항목별로 발굴하고, PoC 목업으로 만들어 사용성 테스트에 "
         "썼습니다.",
    hero="clamshell_crop.jpg",
    meta=[("Term", "2022.12 — 2023.01"), ("Client", "현대자동차 제품UX팀 × 마크로밀엠브레인"),
          ("Team", "석사연구원 4 · 학부연구원 4"), ("Output", "PoC 목업 · 사용성 테스트"),
          ("Role", "선행 연구 · UX 리서치 · 아이템 발굴 · 프로토타이핑")],
    blocks=[
        ("text", "Space", "Clamshell Tailgate",
         ["테일게이트를 펼쳐 앉고 쉬는 공간으로 쓰도록, 그 위에서 쓰는 액세서리를 1:1 폼보드로 만들어 직접 시연했습니다."]),
        ("row", [("clamshell_step.jpg", "Step · 베드 끝에 수납되는 발걸이"), ("s_cupholder.jpg", "Cup Holder · 컵홀더 목업"),
                 ("s_luggage.jpg", "Board · 테일게이트 보드 목업")]),
        ("text", "Wellness & Comfort", None,
         ["원격 시트 베리에이션, 후석 엔터테인먼트, 캐빈 살균, 무드 큐레이터 등 웰니스 항목을 시나리오와 목업으로 구체화했습니다."]),
        ("row", [("seat_modes.jpg", "Seat Variation · 앱으로 시트를 원격 조절")]),
        ("row", [("rear_display_test.jpg", "Rear Entertainment · 실차 검증"),
                 ("s_ott_popup.jpg", "OTT Display · 팝업형")]),
        ("row", [("s_mood.jpg", "Mood Curator · 무드 큐레이터"), ("s_ambient.jpg", "Ambient Light · 감응형 엠비언트 라이트"),
                 ("s_tray.jpg", "Tray · 트레이 목업")]),
        ("role", ["선행 연구", "UX 리서치 및 아이템 발굴", "프로토타이핑", "검증"]),
    ],
)

PAGES["ev-sedan"] = dict(
    dir="ev-sedan", cat_key="ux",
    title="EV Sedan UX", year="2022", category="UX Research · Hyundai",
    desc="현대자동차 준대형 전기세단 UX 디자인 컨셉 솔루션 발굴",
    lede="UX 아이템 10가지를 발굴해 시나리오는 영상으로, 실내 아이템은 <b>폼보드 PoC</b>로 만들어 직접 써 보며 검증했습니다. "
         "PoC는 마크로밀엠브레인의 실사용자 사용성 테스트에 쓰였습니다.",
    hero="ev_scene_console.jpg",
    meta=[("Term", "2022.09 — 2022.11"), ("Client", "현대자동차 제품UX팀 × 마크로밀엠브레인"),
          ("Team", "석사연구원 3 · 학부연구원 3"), ("Output", "폼보드 PoC · 시나리오 영상"),
          ("Role", "선행 연구 · UX 리서치 · 아이템 발굴 · 프로토타이핑")],
    blocks=[
        ("text", "Key Item", "Expandable Center Console",
         ["1열·2열 수납과 컵홀더를 하나의 콘솔에 모으고, 탑승 상황에 따라 콘솔이 앞뒤로 확장되는 구조를 제안했습니다. "
          "폼보드 PoC로 1·2열 배치를 재현해 직접 사용해 보며 확인했습니다."]),
        ("row", [("ev_console_poc.jpg", "PoC · 콘솔 폼보드 모델"), ("ev_console_test.jpg", "Test · 2열 수납 사용")]),
        ("items", [
            ("01", "Table", "여러 방식의 테이블 안을 실차에 펼쳐 검증"),
            ("02", "Cup Holder", "콘솔 하단 트레이에 접어 넣는 폴딩 컵홀더"),
            ("03", "Trunk Luggage Box", "덮개는 컵홀더, 세우면 칸막이가 되는 수납함"),
        ]),
        ("row", [("ev_table_ioniq6.jpg", "Table · 실차 검증"), ("ev_cupholder_poc.jpg", "Cup Holder · PoC"),
                 ("ev_trunk_poc.jpg", "Trunk Luggage Box · PoC")]),
        ("text", "Scenario Items", None, ["공조, 주행, 감시모드, 커스텀 모드 등은 시나리오 영상으로 표현했습니다."]),
        ("row", [("s_aircon.jpg", "Climate · 자동 공조"), ("s_hud.jpg", "Driving · HUD 주행 가이드")]),
        ("row", [("s_relax.jpg", "Custom Mode · 인테리어 커스텀 모드"), ("s_cinema.jpg", "Custom Mode · 인테리어 커스텀 모드")]),
        ("role", ["선행 연구", "UX 리서치 및 아이템 발굴", "프로토타이핑", "검증"]),
    ],
)
