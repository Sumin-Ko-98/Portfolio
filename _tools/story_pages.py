"""상세페이지 내용 (gen_story.py 가 읽음). 사실 기준 = _tools/인수인계.md 3절.
문단은 HTML 그대로 들어간다(<b> 사용 가능, & 는 &amp;).
SOURCES: assets/works/<dir>/<이름> 이 없을 때만 쓰는 원본 경로(윈도우). 한 번 만들어지면 레포의 assets 를 쓴다.
"""
import os

LS = r"C:\Users\Hkyum\iCloudDrive\04_포트폴리오\261006 LS 포트폴리오"
HEIC = r"C:\Users\Hkyum\AppData\Local\Temp\claude\C--Users-Hkyum-iCloudDrive\1054dd20-8098-478f-a7d0-c5556a0bf222\scratchpad\heic"  # HEIC → JPG 변환본
J = os.path.join

ORDER = ["threespin", "ts700", "h500", "odm-cmf", "wade", "inclusive", "seuv", "ev-sedan"]

SOURCES = {
    "ts450": {
        "award_banner.jpg": J(LS, "TS450", "260416_TS450_Award ver_OR_v1.png"),
        "kv_shelf.jpg": J(LS, "TS450", "TS450_KeyVisual_01.png"),
        "kv_wall.jpg": J(LS, "TS450", "TS450_KeyVisual_02.png"),
        "kitchen.jpg": J(LS, "TS450", "TS450_Lifestyle_Kitchen.png"),
        "front_pers.jpg": J(LS, "TS450", "TS450_Front_Pers.png"),
        "side_view.jpg": J(LS, "TS450", "TS450_Side View_v1.png"),
        "bedroom.jpg": J(LS, "TS450", "genspark", "gs_ts450_bedroom_01.png"),
        "bedroom2.jpg": J(LS, "TS450", "genspark", "gs_ts450_bedroom_02.png"),
        "shelf_gs.jpg": J(LS, "TS450", "genspark", "gs_ts450_cradle_shelf_01.png"),
        "macro.jpg": J(LS, "TS450", "genspark", "gs_ts450_mop_macro_01.png"),
        "padchange_gs.jpg": J(LS, "TS450", "genspark", "gs_ts450_pad_change_01.png"),
        "topview.jpg": J(LS, "TS450", "genspark", "gs_ts450_topview_02.png"),
        "photo_1206.jpg": J(HEIC, "TS450_Photo_1206.jpg"),
        "photo_5363.jpg": J(HEIC, "TS450_Photo_5363.jpg"),
        "photo_5982.jpg": J(HEIC, "TS450_Photo_5982.jpg"),
    },
    "ts700": {
        "home2.jpg": J(LS, "TS700", "261002_TS700_Home2_v1.png"),
        "hero_gs.jpg": J(LS, "TS700", "genspark", "gs_ts700_hero_01.png"),
        "hero_gs2.jpg": J(LS, "TS700", "genspark", "gs_ts700_hero_02.png"),
        "steam_macro.jpg": J(LS, "TS700", "genspark", "gs_ts700_pads_macro_01.png"),
        "steam_macro2.jpg": J(LS, "TS700", "genspark", "gs_ts700_pads_macro_02.png"),
        "cutout_front.jpg": J(LS, "TS700", "260910_TS700_Cutout_.36.png"),
        "pers4.jpg": J(LS, "TS700", "260929_TS700_Pers4_v1.png"),
        "pers5.jpg": J(LS, "TS700", "260929_TS700_Pers5_v1.png"),
        "cradle2.jpg": J(LS, "TS700", "260929_TS700_Cradle2_v1.png"),
        "hand_cradle.jpg": J(LS, "TS700", "TS700_Hand_Cradle.png"),
        "lifestyle_hand.jpg": J(LS, "TS700", "TS700_Lifestyle_Hand.png"),
        "mop_exploded.jpg": J(LS, "TS700", "TS700_MopPad_Exploded.png"),
        "photo_2323.jpg": J(HEIC, "TS700_Photo_2323.jpg"),
        "photo_2324.jpg": J(HEIC, "TS700_Photo_2324.jpg"),
        "photo_0188.jpg": J(HEIC, "TS700_Photo_0188.jpg"),
    },
    "h500": {
        "concept.jpg": J(LS, "H500", "260506_H500 CONTROLLER_CON_P2_v3_Concept2_1.png"),
        "mock_ctrl1.jpg": J(LS, "H500", "H500_Mockup_Controller_01.jpg"),
        "mock_ctrl2.jpg": J(LS, "H500", "H500_Mockup_Controller_02.jpg"),
        "mock_ctrl3.jpg": J(LS, "H500", "H500_Mockup_Controller_03.jpg"),
        "mock_wheel1.jpg": J(LS, "H500", "H500_Mockup_Wheel_01.jpg"),
        "mock_wheel2.jpg": J(LS, "H500", "H500_Mockup_Wheel_02.jpg"),
        "mock_wheel3.jpg": J(LS, "H500", "H500_Mockup_Wheel_03.jpg"),
        "mock_wheel4.jpg": J(LS, "H500", "H500_Mockup_Wheel_04.jpg"),
        "mock_wheel5.jpg": J(LS, "H500", "H500_Mockup_Wheel_05.jpg"),
        "chair186.jpg": J(LS, "H500", "H500_Wheelchair_186.png"),
        "gs_wheel_side.jpg": J(LS, "H500", "genspark", "gs2_h500_view_wheel_side_01.png"),
        "gs_wheel_detail.jpg": J(LS, "H500", "genspark", "gs2_h500_wheel_detail_01.png"),
        "gs_cafe.jpg": J(LS, "H500", "genspark", "gs_h500_cafe_02.png"),
        "gs_door.jpg": J(LS, "H500", "genspark", "gs_h500_home_door_01.png"),
        "photo_8218.jpg": J(HEIC, "H500_Photo_8218.jpg"),
    },
    "odm": {
        "q7plus_main.jpg": J(LS, "ODM", "260526_Q7PLUS_Set_Main Pers_v3.png"),
        "q9plus_main.jpg": J(LS, "ODM", "260622_Q9 Plus_Cutout_Set_Main Pers_v1.png"),
        "q13_set.jpg": J(LS, "ODM", "260827_Q13_3D_Set_v2.png"),
        "x2_pers.jpg": J(LS, "ODM", "260907_X2_Pers2_v1.png"),
        "q3t_set.jpg": J(LS, "ODM", "260714_Q3 Turbo_Set_Pers R 20_v1.png"),
        "ts402m_tilt.jpg": J(LS, "ODM", "260319_TS402M_3DR_Set_Front Tilting_v1.png"),
        "q9_side.jpg": J(LS, "ODM", "Q9_Set_Side_R.png"),
        "q9_front.jpg": J(LS, "ODM", "Q9_Set_Front.png"),
        "cmf_book.jpg": J(LS, "Work_Photos", "CMF_Color_Book_6775.JPG"),
        "cmf_chips.jpg": J(HEIC, "CMF_Color_Chips_7998.jpg"),
        "cmf_sample.jpg": J(HEIC, "CMF_Sample_Check_0013.jpg"),
        "pantone1.jpg": J(HEIC, "CMF_Silk_Pantone_0954.jpg"),
        "pantone2.jpg": J(HEIC, "CMF_Silk_Pantone_0955.jpg"),
        "q9_topcover.jpg": J(HEIC, "Q9_TopCover_Photo.jpg"),
    },
    "wade": {
        "studio.jpg": J(LS, "WADE", "genspark", "gs_wade_studio_01.png"),
        "kid_draw.jpg": J(LS, "WADE", "genspark", "gs_wade_kid_draw_DtsenQa9.jpg"),
        "drone.jpg": J(LS, "WADE", "genspark", "gs_wade_drone_UFcdm34p.jpg"),
        "nozzle1.jpg": J(LS, "WADE", "genspark", "gs_wade_nozzle_6KZTCK5o.jpg"),
        "nozzle2.jpg": J(LS, "WADE", "genspark", "gs_wade_nozzle_It2CF2g5.jpg"),
        "result_heart.jpg": J(LS, "_시안", "assets", "wade", "result_heart.jpg"),
    },
    "inclusive": {
        "s_ehmi_side.jpg": J(LS, "_시안", "assets", "ux", "inclusive", "s_ehmi_side.jpg"),
    },
    "seuv": {
        "s_ott.jpg": J(LS, "_시안", "assets", "ux", "seuv", "s_ott.jpg"),
    },
    "ev-sedan": {
        "s_security.jpg": J(LS, "_시안", "assets", "ux", "ev_sedan", "s_security.jpg"),
    },
}

W = "#fff"  # 흰 배경 렌더용

PAGES = {}

# =====================================================================
PAGES["threespin"] = dict(
    dir="ts450", cat_key="product", title="Threespin Slim", year="2024 — 2025", category="Robot Mop · Everybot",
    desc="쓰리스핀 슬림 TS450 물걸레 로봇청소기 제품디자인",
    lede="에브리봇이 10년 이상 축적한 ROBO-SPIN 기술로 <b>브랜드 역사상 가장 슬림하게</b> 완성한 물걸레 로봇청소기입니다.",
    hero="cover.jpg",
    meta=[("Term", "2024.07 — 2025.12"), ("Client", "에브리봇"), ("Product", "쓰리스핀 슬림 TS450"),
          ("Role", "UX · 3D · CMF · 디자인 목업 · 양산 지원"), ("Output", "양산 출시")],
    intro=([("if", "2026.04", "iF Design Award", "2026 · Gold"),
            ("reddot", "2026.04", "Red Dot Award", "Product Design 2026"),
            ("gd", "2026.09", "Good Design Korea", "GD 선정")],
           "공간에 스며드는 미니멀 오브제",
           "A minimal object that settles into the room",
           "낮은 바디로 소파·침대 아래까지 청소 범위를 넓히고, <b>오프 화이트 매트 마감</b>과 심리스한 곡면으로 "
           "거실의 오브제처럼 자리하도록 디자인했습니다. 쓰리스핀 시리즈에서 가장 낮은 83mm 높이에, "
           "버튼 2개와 라이트 라인, 음성 안내만으로 매뉴얼 없이 쓰도록 정리했습니다.",
           "Built on the ROBO-SPIN technology Everybot has refined for more than ten years, Threespin Slim is the "
           "slimmest robot mop in the brand's history. Its low body reaches under sofas and beds, and an off-white "
           "matte finish with seamless curves lets it sit in the living room like an object rather than an appliance. "
           "At 83 mm it is the lowest model in the Threespin series, operated with two buttons, a light line and voice guidance."),
    sections=[
        ("dark", [
            ("img", {"f": "award_banner.jpg", "r": "natural"}),
            ("row", "FORM",
             "‘낮음 · 단순함 · 심리스’라는 세 가지 조형 원칙 아래 형태를 정리했습니다. ROBO-SPIN 구조의 세 회전 패드 배치가 "
             "그대로 삼각형 외형으로 이어졌고, 다양한 R값으로 모서리를 다듬어 원형 로봇청소기와 다른 조형 언어를 만들었습니다.",
             "The form follows three principles: low, simple and seamless. The layout of the three rotating pads in the "
             "ROBO-SPIN structure carries straight into a triangular silhouette, and corners finished with varied radii "
             "give it a form language distinct from round robot vacuums."),
            ("dots", ["macro.jpg", "padchange_gs.jpg", "shelf_gs.jpg"]),
            ("row", "PROTECTION",
             "이전 모델은 센서창이 하우징과 같은 면에 있어 가구에 직접 부딪혔고, 센서창과 가구에 스크래치가 생긴다는 VOC가 "
             "접수됐습니다. 상·하단 하우징을 센서창보다 바깥으로 내밀어 단차를 주어, 부딪혀도 하우징이 먼저 닿게 했습니다.",
             "On the previous model the sensor window sat flush with the housing and hit furniture directly, and customers "
             "reported scratches on both. The upper and lower housings now step out beyond the sensor window, so the "
             "housing touches first."),
            ("img", {"f": "kitchen.jpg", "pos": "50% 78%"}, ' style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;"'),
        ]),
        ("scene", {"f": "bedroom.jpg", "r": "natural"}),
        ("text", "Triangle Form",
         "본체를 360도로 두르는 블랙 센서창 라인이 시선을 가로로 이끕니다. 다양한 R값으로 다듬은 모서리가 원형 로봇청소기와 "
         "다른 인상을 만듭니다. #슬림 · #심리스 · #미니멀",
         "A black sensor-window line wraps the body through 360 degrees and leads the eye horizontally, while corners "
         "finished with varied radii set it apart from round robot vacuums."),
        ("square", "kv_shelf.jpg"),
        ("tri", ["topview.jpg", {"f": "mop_pads.jpg", "pos": "45% 50%"}, {"f": "front_pers.jpg", "pos": "50% 50%"}]),
        ("text", "Low Proportion",
         "상단부 두께를 최소화하고 측면 라인이 바닥으로 흘러내리도록 처리해 바닥에 밀착된 인상을 줍니다. 개발 중 IR 센서가 "
         "측후면으로 이동한 뒤에도 손잡이·상면 곡률·센서창 비율을 함께 조정해 이 라인을 유지했습니다.",
         "The top is kept as thin as possible and the side line flows down to the floor, so the robot looks pressed to "
         "the ground. When the IR sensor moved to the rear side during development, the handle, top curvature and "
         "sensor-window proportions were adjusted together to keep this line."),
        ("bleed", "side_view.jpg", "natural"),
        ("text", "Sensor Protection",
         "센서창 보호 단차와 함께, 크래들에 거치할 때도 센서창이 크래들에 직접 닿는 면을 없애 스크래치를 막았습니다. "
         "아래 왼쪽이 이전 모델, 오른쪽이 TS450입니다.",
         "Besides the protective step, the cradle was shaped so that no surface touches the sensor window when the robot "
         "is docked. Left: previous model. Right: TS450."),
        ("pair", [{"f": "sensor_before.jpg", "r": "natural"}, "sensor_after.jpg"]),
        ("bleed", "sensor_cradle.jpg", "natural"),
        ("split",
         ("Simple UI", "시작·정지와 물 공급량 버튼 2개, 작동 상태를 알리는 라이트 라인, 음성 안내만으로 매뉴얼 없이 조작합니다.",
          "Two buttons for start/stop and water flow, a light line for status and voice guidance: no manual needed."),
         ("Mop Pads", "세 개의 회전 패드는 손쉽게 탈착·세탁할 수 있고, 세탁 후 반복 사용합니다.",
          "The three rotating pads detach easily and can be washed and reused.")),
        ("duo", ["robospin.jpg", {"f": "ui.jpg", "pos": "62% 50%"}]),
        ("bleed", "kv_wall.jpg", "macro"),
        ("text", "Storage &amp; CMF",
         "본체를 세워 결합하는 수직형 거치대로 보관 면적을 줄였습니다. 거치대도 본체와 같은 곡면·컬러·마감으로 통일해 보관 중에도 "
         "하나의 오브제로 읽힙니다.",
         "A vertical cradle that holds the robot upright reduces the storage footprint. The cradle shares the body's "
         "curves, colour and finish, so the two read as one object even in storage."),
        ("scenario", {"f": "cradle_shelf.jpg", "pos": "50% 50%"}),
        ("bleed", "overview_life.jpg", "strap"),
        ("dark", [
            ("grid", ["mockup_1201.jpg", "photo_1206.jpg", "mockup_5465.jpg", "photo_5363.jpg", "photo_5982.jpg", "mockup_5981.jpg"]),
            ("row", "MOCK-UP",
             "1:1 디자인 목업을 제작해 비율 · 센서창 라인 · 다양한 CMF 시안을 검토했습니다. 시사출 단계에서는 플로우 마크 등의 "
             "품질 검수를 진행하고, 일부 금형 수정 등 양산 팔로우업을 진행했습니다.",
             "Full-scale design mock-ups were built to review proportion, the sensor-window line and a range of CMF options. "
             "At the trial-injection stage, quality issues such as flow marks were inspected and mass-production follow-up "
             "included partial mould changes."),
            ("facts", [("83mm", "쓰리스핀 시리즈 최저 높이"), ("3", "ROBO-SPIN 회전 패드"), ("2", "조작 버튼")]),
            ("row", "OUTCOME",
             "출시 후 iF 디자인 어워드 2026 Gold, 레드닷 디자인 어워드(Product Design 2026), 굿디자인(GD) 선정을 받았습니다.",
             "After launch the product received the iF Design Award 2026 Gold, the Red Dot Award: Product Design 2026 and "
             "Good Design Korea selection."),
            ("roles", ["시장·트렌드·경쟁 제품 리서치", "UX 디자인", "스케치·2D 렌더링", "3D 모델링·렌더링", "CMF",
                       "디자인 목업", "디자인 사양서", "양산 지원", "마케팅 이미지 소스 지원", "어워드 출품"]),
        ]),
        ("bleed", "bedroom2.jpg", "natural"),
        ("band",),
    ],
)

# =====================================================================
PAGES["ts700"] = dict(
    dir="ts700", cat_key="product", title="Threespin Steam", year="2025 — 2026", category="Robot Mop · Everybot",
    desc="쓰리스핀 스팀 TS700 제품디자인 · 양산 지원",
    lede="스팀 모듈을 탑재한 쓰리스핀 로봇청소기입니다. 높아진 전고를 <b>슬림한 실루엣</b>으로 보이게 하고, "
         "<b>A/S 효율성을 높인 하우징 분할 구조</b>를 설계했습니다.",
    hero="cover.jpg",
    meta=[("Term", "2025.11 — 2026.10"), ("Client", "에브리봇"), ("Product", "쓰리스핀 스팀 TS700"),
          ("Role", "UX · UI·음성 · CMF · 디자인 목업 · 양산 지원"), ("Status", "양산 지원 진행 중")],
    intro=([("01", "Slim Look", "대형 챔퍼 · 다크 하단", "높아진 전고를 슬림하게"),
            ("02", "3-Part Body", "바텀 · 미들 · 탑", "하단 모듈 서비스성 개선"),
            ("03", "Steam Module", "바닥면 중앙 스팀 모듈", "세워 보관하는 거치대")],
           "높아진 전고는 슬림하게, 하우징은 고치기 쉽게",
           "Slimmer to the eye, easier to service",
           "바닥면 중앙에 스팀 모듈을 탑재하면서 전고가 높아졌고, 기존 하우징 구조로는 A/S가 어려웠습니다. "
           "두 문제를 <b>형태와 CMF</b>, <b>파트 분할</b>로 풀고, 이후 UI·음성 안내와 CMF, 양산 단계까지 이어서 맡았습니다.",
           "Mounting a steam module at the centre of the underside raised the overall height, and the existing housing made "
           "after-sales service difficult. Both problems were solved through form and CMF, and through how the parts are "
           "split, followed by UI and voice guidance, CMF and mass-production support."),
    sections=[
        ("dark", [
            ("img", {"f": "steam_macro.jpg", "r": "natural"}),
            ("row", "PROBLEM",
             "로봇청소기 시장에서는 전고가 낮을수록 제품 가치가 높게 평가되지만, 스팀 모듈 탑재로 전고가 크게 높아졌습니다. "
             "또 기존 자사 제품은 깊은 바텀과 얕은 탑의 2분할 구조라, A/S 때 하단 모듈에 접근하려면 상단 모듈을 모두 분해해야 했습니다.",
             "In the robot vacuum market a lower height is read as higher value, but the steam module made the robot much "
             "taller. Existing models also used a two-part housing, a deep bottom and a shallow top, so reaching the lower "
             "module for service meant taking the whole upper module apart."),
            ("dots", [{"f": "pers4.jpg", "bg": W}, {"f": "mop_exploded.jpg", "pos": "50% 60%"}, {"f": "hand_cradle.jpg", "pos": "55% 50%"}]),
            ("row", "APPROACH",
             "바텀 하우징 엣지에 대형 챔퍼를, 바텀 파트에 다크 톤 CMF를 적용해 하단부가 시각적으로 후퇴하도록 했습니다. "
             "그리고 바디를 바텀·미들·탑 3분할로 재구성해, 상단 전체를 해체하지 않고도 하단 모듈에 접근할 수 있게 했습니다.",
             "A large chamfer on the bottom-housing edge and a dark-tone CMF on the bottom part make the lower body visually "
             "recede. The body was then rebuilt as bottom, middle and top, so the lower module can be reached without "
             "dismantling the entire top."),
            ("img", {"f": "home2.jpg", "r": "natural"}, ' style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;"'),
        ]),
        ("scene", {"f": "lifestyle_hand.jpg", "r": "natural"}),
        ("text", "Slim Look",
         "사용자가 서서 내려다보는 시선 각도에서는 챔퍼로 덜어낸 측면과 어두운 하단이 잘 보이지 않습니다. 그래서 실제 전고보다 "
         "얇은 바디로 인지됩니다.",
         "From the angle at which a standing user looks down, the chamfered side and the dark lower part barely register, "
         "so the body is perceived as thinner than its actual height."),
        ("bleed", "eye_angle.png", "natural"),
        ("tri", [{"f": "cutout_front.jpg", "fit": "contain", "bg": W}, {"f": "pers5.jpg", "fit": "contain", "bg": W},
                 {"f": "cradle2.jpg", "fit": "contain", "bg": W}]),
        ("text", "3-Part Body",
         "하우징을 바텀·미들·탑 3분할 구조로 재구성해, 상단 전체를 해체하지 않고도 하단 모듈에 접근할 수 있도록 "
         "서비스성을 개선했습니다.",
         "The housing was rebuilt in three parts (bottom, middle and top), so the lower module can be reached without "
         "dismantling the whole top."),
        ("bleed", "three_part_body.png", "natural"),
        ("duo", [{"f": "steam_macro2.jpg", "pos": "50% 60%"}, {"f": "hero_gs.jpg", "pos": "46% 50%"}]),
        ("text", "Product Details",
         "물통은 래치 방식으로 탈착하고, 사용하지 않을 때는 거치대에 세워 보관합니다.",
         "The water tank detaches with a latch, and the robot stands upright on its cradle when not in use."),
        ("pair", [{"f": "detail_top_cover.jpg", "r": "natural"}, "detail_storage.jpg"]),
        ("split",
         ("LED UI · Sound", "동작 사양에 따른 라이팅 UI와 음성 안내를 설계하고, 효과음·TTS를 제작했습니다.",
          "Lighting UI and voice guidance were designed from the operating specification, with sound effects and TTS produced in-house."),
         ("CMF", "다양한 컬러의 디자인 목업을 제작·검토한 뒤 CMF와 실크를 확정했습니다.",
          "Design mock-ups in a range of colours were built and reviewed before the CMF and silk-screen were fixed.")),
        ("dark", [
            ("grid", ["photo_2323.jpg", "photo_2324.jpg", "mockup_2325.jpg", "photo_0188.jpg", "mockup_1109.jpg", "mockup_1665.jpg"]),
            ("row", "MASS PRODUCTION",
             "디자인 목업과 시사출 외관을 검토하고, 디자인 사양서 · 시사출 검토 · 금형 수정 요청 · 마케팅 렌더링까지 양산 단계를 "
             "지원하고 있습니다.",
             "Design mock-ups and trial-injection parts were reviewed, and mass-production support continues with design "
             "specifications, trial-injection reviews, mould-change requests and marketing renderings."),
            ("roles", ["시장·트렌드·경쟁 제품 리서치", "UX 디자인", "스케치·2D 렌더링", "3D 모델링·렌더링",
                       "UI·음성 안내 설계 및 제작(효과음·TTS)", "CMF", "디자인 목업", "디자인 사양서", "양산 지원", "마케팅 이미지 소스 지원"]),
        ]),
        ("bleed", "overview_main.jpg", "natural"),
        ("band",),
    ],
)

# =====================================================================
PAGES["h500"] = dict(
    dir="h500", cat_key="product", title="H500", year="2025 — 2026", category="Wheelchair · Everybot Mobility",
    desc="에브리봇모빌리티 H500 수전동휠체어 컨트롤러 · 인휠모터 휠 디자인",
    lede="수전동휠체어 H500의 <b>컨트롤러</b>와 <b>인휠모터 휠</b>을 디자인했습니다.",
    hero="ctrl_cover.jpg",
    meta=[("Term", "2025.12 — 2026.06"), ("Client", "에브리봇모빌리티"), ("Product", "H500 수전동휠체어"),
          ("Scope", "컨트롤러 · 인휠모터 휠"), ("Output", "3D 프린팅 목업 · CMF 목업")],
    intro=([("CTRL", "Controller", "팜레스트 형상 · 버튼 배치", "오조작 방지 · 표시부 가독성"),
            ("WHEEL", "In-wheel Motor Wheel", "허브 일체형 구동부", "3-스포크 · 컬러 커스텀")],
           "손 힘이 약해도 정확하게, 구동부는 휠 하나에",
           "Precise control for a weak grip, a drive unit inside one wheel",
           "컨트롤러는 기존 일자형 컨트롤러보다 가시성을 높이도록 디스플레이와 조작부의 각도를 세우고, 손 힘이 약한 사용자도 "
           "놓치지 않고 정확하게 조작할 수 있도록 <b>손을 받친 채 쓰는</b> 형태로 만들었습니다. 휠은 구동부를 휠 안에 담은 "
           "인휠모터 휠로, 휠체어 시장에도 컬러 선택 니즈가 있음을 확인하고 <b>컬러 커스텀</b>이 가능한 컨셉으로 진행했습니다.",
           "Compared with conventional flat controllers, the display and controls are angled up for better visibility, and "
           "the controller is used with the hand resting on it so that users with a weak grip can operate it precisely. "
           "The wheel puts the drive unit inside the wheel itself; having confirmed that wheelchair users also want colour "
           "choice, it was developed as a colour-customisable concept."),
    sections=[
        ("dark", [
            ("img", {"f": "gs_cafe.jpg", "r": "natural"}),
            ("row", "CONTROLLER",
             "기존 일자형 컨트롤러에서 가시성을 높일 수 있도록 디스플레이와 조작부의 각도를 세웠습니다. 탈착·좌우 반전이 가능한 "
             "팜레스트로 손을 받친 채 조작하고, 레드 전원 버튼을 중앙에, 방향 버튼을 주위에 모아 기능별로 묶었습니다.",
             "The display and controls were angled up from the conventional flat layout for better visibility. A detachable, "
             "reversible palm rest supports the hand, and the red power button sits at the centre with the direction "
             "buttons grouped around it by function."),
            ("dots", ["mock_ctrl1.jpg", "ctrl_mockup.jpg", "wheel_white_mockup.jpg"]),
            ("row", "WHEEL",
             "인휠모터를 허브에 담아 휠 하나로 구동부를 완결했습니다. 스포크 인서트는 원하는 컬러로 커스텀할 수 있도록 확장성을 "
             "고려했고, 손으로 수동 주행할 때를 고려해 핸드림의 두께와 휠과의 간격을 설정했습니다.",
             "The in-wheel motor sits in the hub, so one wheel completes the drive unit. Spoke inserts were designed to be "
             "swapped for any colour, and the hand-rim thickness and its gap from the wheel were set for manual propulsion."),
            ("img", {"f": "wheel_rim_hand.jpg", "r": "natural"}, ' style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;"'),
        ]),
        ("scene", {"f": "ctrl_living.jpg", "r": "natural"}),
        ("text", "Palm Rest",
         "팜레스트는 탈착할 수 있고 좌우를 바꿔 달 수 있어 왼손잡이도 사용할 수 있습니다. 조이스틱은 기성품을 사용해 원가를 "
         "줄였습니다.",
         "The palm rest detaches and can be mounted on either side, so left-handed users can use it too. An off-the-shelf "
         "joystick keeps the cost down."),
        ("square", {"f": "ctrl_pers.jpg", "fit": "contain", "bg": W}),
        ("tri", [{"f": "ctrl_top.jpg", "fit": "contain", "bg": W}, {"f": "ctrl_side.jpg", "fit": "contain", "bg": W},
                 {"f": "concept.jpg", "fit": "contain", "bg": W}]),
        ("split",
         ("Button Grouping", "레드 전원 버튼을 중심으로 라이트·비상등·경적 버튼을 기능별로 묶었습니다.",
          "Light, hazard and horn buttons are grouped by function around the central red power button."),
         ("Display", "표시부를 버튼 위에 두어 누르는 손에 가려지지 않게 했습니다.",
          "The display sits above the buttons so the pressing hand never hides it.")),
        ("text", "Mock-up",
         "3D 프린팅 목업으로 직접 쥐고 조작하며 형상과 버튼 배치를 다듬었습니다.",
         "3D-printed mock-ups were held and operated to refine the form and button layout."),
        ("bleed", "mock_ctrl2.jpg", "strap"),
        ("bleed", "chair186.jpg", "natural"),
        ("text", "In-wheel Motor Wheel",
         "수전동휠체어의 구동부를 휠 안에 담은 인휠모터 휠입니다. 3-스포크의 스포크 인서트를 원하는 컬러로 커스텀할 수 있도록 "
         "확장성을 고려해 디자인했습니다.",
         "An in-wheel motor wheel that places the wheelchair's drive unit inside the wheel. The inserts of its three "
         "spokes were designed to be customised in any colour."),
        ("square", "wheel_render_24.jpg"),
        ("text", "Hand Rim",
         "손으로 수동 주행할 때를 고려해 메탈 핸드림의 두께와 휠과의 간격을 설정했습니다.",
         "The thickness of the metal hand rim and its gap from the wheel were set for manual propulsion."),
        ("dark", [
            ("grid", ["mock_wheel1.jpg", "mock_wheel2.jpg", "mock_wheel3.jpg", "mock_wheel5.jpg", "wheel_cmf_mockup.jpg", "photo_8218.jpg"]),
            ("row", "MOCK-UP &amp; CMF",
             "스포크 인서트 컬러와 핸드림 블랙 / 실버 마감을 실물 목업으로 비교하고, 컬러칩 5종으로 최종 컬러를 확인했습니다.",
             "Spoke-insert colours and black / silver hand-rim finishes were compared on physical mock-ups, and the final "
             "colours were checked against five colour chips."),
            ("mosaic", ["wheel_color_chips.jpg", "wheel_chair_side.jpg", "mock_wheel4.jpg", "gs_wheel_detail.jpg"]),
            ("roles", ["컨트롤러 디자인", "UX 디자인 (팜레스트 형상·버튼 배치·오조작 방지·표시부 가독성)", "3D 프린팅 목업 검증",
                       "휠 · 시장·트렌드·경쟁 제품 리서치", "스케치", "3D 모델링", "CMF 디자인", "디자인 목업"]),
        ]),
        ("bleed", "gs_door.jpg", "natural"),
        ("band",),
    ],
)

# =====================================================================
PAGES["odm-cmf"] = dict(
    dir="odm", cat_key="product", title="CMF & Facelift", year="2024 — 2026", category="CMF · Partial Form · 16 Models",
    desc="에브리봇 · 맥스젠 · 에브리봇모빌리티 양산 제품 CMF · 부분 형상 디자인 16종 (ODM 15 · 페이스리프트 1)",
    lede="ODM 15종과 자사 페이스리프트 1종, 양산 제품 <b>16종의 색상·소재·마감·실크</b>와 부분 형상을 담당했습니다.",
    hero="hero_lineup.jpg",
    meta=[("Term", "2024.06 — 2026.10"), ("Client", "에브리봇 · 맥스젠 · 에브리봇모빌리티"), ("Partner", "중국 ODM 제조사"),
          ("Scope", "CMF · 부분 형상 · 페이스리프트"), ("Output", "ODM 15종 · 페이스리프트 1종")],
    intro=([("13", "Everybot", "에브리봇", "ODM 12 · 페이스리프트 1"),
            ("2", "Maxzen", "맥스젠", "흡입스팀다리미 등"),
            ("1", "Everybot Mobility", "에브리봇모빌리티", "H300")],
           "브랜드 톤은 지키고, 모델마다 다르게",
           "One brand tone, a distinct finish for each model",
           "브랜드 톤을 유지하면서 모델마다 차이가 드러나도록 CMF를 정리했습니다. 디자인 사양서와 CMF 가이드를 제조사에 전달하고, "
           "도장 목업 제작을 감리하고, 양산 샘플을 검수했습니다. <b>Q7 PLUS</b>는 스테이션 물통 커버 형상 디자인과 부분 금형 수정, "
           "<b>Q9</b>은 스테이션 탑 커버 신규 제작까지 맡았습니다.",
           "Products designed and engineered by Chinese ODM partners were given a CMF that keeps one brand tone while "
           "making each model distinct. Work covered design specifications and CMF guides for the manufacturer, supervision "
           "of painted mock-ups and inspection of production samples, plus a redesigned station water-tank cover with "
           "partial mould changes for the Q7 PLUS and a new station top cover for the Q9."),
    sections=[
        ("dark", [
            ("img", "cmf_chips.jpg"),
            ("row", "CMF",
             "컬러북과 컬러칩, 팬톤 가이드로 모델별 컬러를 정하고, 실크 인쇄 위치와 색을 지정했습니다. 도장 목업과 양산 샘플을 "
             "실물로 검수해 가이드와 차이가 없는지 확인했습니다.",
             "Colours for each model were set with colour books, chips and Pantone guides, along with silk-print positions "
             "and colours. Painted mock-ups and production samples were checked against the guide in person."),
            ("dots", ["pantone1.jpg", "pantone2.jpg", "cmf_sample.jpg"]),
            ("row", "COVER",
             "Q7 PLUS는 스테이션 물통 커버의 형상을 디자인하고 금형을 부분 수정했고, Q9은 스테이션 탑 커버를 새로 디자인해 "
             "제작까지 맡았습니다.",
             "For the Q7 PLUS the station water-tank cover was reshaped with partial mould changes; for the Q9 a new station "
             "top cover was designed and taken into production."),
            ("img", {"f": "q9_topcover.jpg", "r": "natural"}, ' style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;"'),
        ]),
        ("text", "Line-up",
         "로봇청소기, 스테이션, 욕실 청소 로봇, 흡입스팀다리미까지 제품군이 다양해, 공통 톤을 유지하면서 모델 간 위계가 보이도록 "
         "정리했습니다.",
         "The range spans robot vacuums, stations, a bathroom-cleaning robot and a steam iron, so a shared tone was kept "
         "while making the hierarchy between models visible."),
        ("lineup", [("q3_turbo.jpg", "Q3 Turbo"), ("q3_turbo_s.jpg", "Q3 Turbo PLUS"), ("q7_plus.jpg", "Q7 PLUS · 물통 커버"),
                    ("q9.jpg", "Q9 · 탑 커버"), ("q9_plus.jpg", "Q9 PLUS"), ("q11.jpg", "Q11"), ("q13.jpg", "Q13"), ("q7.jpg", "Q7"),
                    ("ts402m.jpg", "TS402M · 페이스리프트"), ("b1.jpg", "B1"), ("x1.jpg", "X1"), ("x2.jpg", "X2"), ("sr13w.jpg", "SR13W")],
         ("+ MORE", "TS800 · SR15W(맥스젠) · H300(에브리봇모빌리티)")),
        ("text", "Q9 Station Top Cover",
         "Q9은 스테이션 탑 커버를 새로 디자인해 제작까지 맡았습니다.",
         "For the Q9, a new station top cover was designed and taken into production."),
        ("pair", [{"f": "q9_front.jpg", "fit": "contain", "bg": W}, {"f": "q9_side.jpg", "fit": "contain", "bg": W}]),
        ("tri", [{"f": "x2_pers.jpg", "fit": "contain", "bg": W}, {"f": "q3t_set.jpg", "fit": "contain", "bg": W},
                 {"f": "ts402m_tilt.jpg", "fit": "contain", "bg": W}]),
        ("dark", [
            ("facts", [("13", "에브리봇 (ODM 12 · 페이스리프트 1)"), ("2", "맥스젠"), ("1", "에브리봇모빌리티")]),
            ("row", "PROCESS",
             "제조사 디자인 → CMF 제안 → 디자인 사양서·CMF 가이드 전달 → 도장 목업 감리 → 샘플 검수 → 양산. 마케팅 이미지 "
             "소스도 함께 지원했습니다.",
             "Manufacturer design → CMF proposal → design specification and CMF guide → painted mock-up supervision → "
             "sample inspection → mass production, with source images for marketing."),
            ("roles", ["CMF 디자인", "금형 수정·신규 커버 디자인", "도장 목업 제작 감리", "디자인 사양서·CMF 가이드 전달",
                       "샘플 검수", "마케팅 이미지 소스 지원"]),
        ]),
        ("bleed", "cmf_book.jpg", "final"),
        ("band",),
    ],
)

# =====================================================================
PAGES["wade"] = dict(
    dir="wade", cat_key="product", title="WADE", year="2023", category="Service Robot · KIRO",
    desc="WADE 워터 드로잉 서비스 로봇 — 외관 디자인 · 구조 설계 · 워킹 프로토타입",
    lede="관람객이 터치 디스플레이에 그린 그림을 <b>물로 바닥에 출력하는</b> 놀이공원 서비스 로봇입니다. "
         "물로 그린 그림은 시간이 지나면 증발하기 때문에 따로 지울 필요가 없습니다.",
    hero="cover.jpg",
    meta=[("Term", "2023.07 — 2023.08"), ("Client", "KIRO 서울로봇아카데미"), ("Team", "5인 (엔지니어 4 · 디자이너 1)"),
          ("Role", "리서치 · 컨셉 · 구조 설계 · 3D · 프로토타입 (디자인 기여도 100%)"), ("Output", "워킹 프로토타입 · 특허 · 디자인 등록")],
    intro=([("hci", "2024.01", "HCI Korea", "Creative Award · Excellence Award (최우수상)"),
            ("PAT", "2026.03", "Patent", "특허 제10-2942532호 · 워터 드로잉을 위한 로봇 장치"),
            ("DES", "2024.10", "Design Reg.", "디자인 등록 제30-1280754호 · 지능형 서비스 로봇")],
           "기다리는 시간을 볼거리로 바꾸는 워터 드로잉 로봇",
           "A service robot that turns waiting time into a show, drawn in water",
           "WADE는 야외 바닥에 <b>물로 그림을 그리는</b> 서비스 로봇입니다. 놀이공원에서 가장 불편한 점으로 꼽힌 긴 대기줄"
           "(47.9%, 메타베이 2023.06)에서 출발해, 대기 시간을 줄이는 대신 줄 옆 바닥에 그림을 그려 기다리는 시간을 볼거리로 바꾸는 "
           "컨셉입니다. 관람객이 머리 위 터치 디스플레이에 그림을 그리면 그림을 20×12개의 점으로 바꾸고, 로봇이 직진하는 동안 "
           "12개의 노즐이 한 줄씩 바닥에 물을 뿌려 출력합니다. 물 그림은 소음 속에서도 눈에 띄고, 마르면 흔적 없이 사라집니다.",
           "WADE is a service robot that draws on outdoor ground surfaces with water. It started from the long queues "
           "that visitors named as the biggest discomfort at amusement parks (47.9%, Metabay, June 2023): instead of "
           "shortening the wait, the robot draws next to the line and turns waiting time into something to watch. A visitor "
           "draws on the overhead touch display, the drawing is converted into a 20×12 dot grid, and twelve nozzles print it "
           "row by row while the robot drives straight. Water drawings stand out even in a noisy crowd and disappear "
           "without a trace once they dry."),
    sections=[
        ("dark", [
            ("img", "scene_print.jpg"),
            ("row", "PROBLEM",
             "사람에게는 어딘가에 낙서를 하고 흔적을 남기려는 욕구가 있습니다. 그러나 공공장소에서는 남은 흔적을 다시 지워야 하기 때문에 "
             "이 욕구를 해소할 방법이 거의 없습니다. 로봇으로 그림을 출력하는 방식도 재료가 바닥에 남으면 같은 문제가 반복됩니다. "
             "WADE는 출력 재료를 물로 바꿔서 이 문제를 해결했습니다.",
             "People have an urge to scribble and leave marks. In public spaces, however, there is almost no way to act on "
             "it, because any mark left behind has to be removed. Robotic drawing systems face the same issue when the "
             "printing material stays on the ground. WADE addresses this by using water as the printing material."),
            ("dots", [{"f": "kid_draw.jpg", "pos": "62% 45%"}, "result_heart.jpg", {"f": "studio.jpg", "pos": "50% 22%"}]),
            ("row", "APPROACH",
             "구현 방식은 워터펌프와 솔레노이드 밸브를 조합한 적정기술입니다. 별도 출력 장비 없이 압력탱크로 물을 밀어내고 밸브의 개폐만 "
             "제어하기 때문에 야외에서 운용할 수 있고 유지비가 낮습니다. 여기에 틸팅과 스위블이 가능한 헤드와 표정 변화를 더하고, "
             "캐릭터성은 절제하고 직선을 줄인 유선형으로 다듬어 불쾌한 골짜기를 피했습니다.",
             "The system is built on appropriate technology, combining a water pump with solenoid valves. A pressure tank "
             "pushes the water out and only the valve opening and closing is controlled, which allows outdoor operation at "
             "a low maintenance cost. A tilting and swiveling head with changing expressions was added, while the character "
             "was kept restrained, with a streamlined form and fewer straight lines, to avoid the uncanny valley."),
            ("img", "drone.jpg", ' style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;"'),
        ]),
        ("scene", {"f": "step_print.jpg", "r": "natural"}),
        ("text", "Head &amp; Expression",
         "헤드는 틸팅과 스위블이 가능해 사용자 방향으로 얼굴을 돌립니다. LiDAR 센서가 앞에 있는 사람을 2초간 인식하면 주행을 멈추고 "
         "얼굴을 사용자 쪽으로 회전시킵니다. 이후 상부 터치 디스플레이로 그림 입력을 받습니다. 표정 변화로 현재 동작 상태를 표시해 "
         "처음 사용하는 사람도 진행 순서를 확인할 수 있습니다.",
         "The head tilts and swivels to turn its face toward the user. When the LiDAR sensor detects a person in front "
         "for two seconds, the robot stops driving and rotates its face toward that person. It then receives the drawing "
         "input through the upper touch display. Changes in facial expression indicate the current operating state, so "
         "first-time users can follow the sequence of steps."),
        ("square", {"f": "scene_wait.jpg", "fit": "contain", "bg": "#efefef"}),
        ("tri", [{"f": "step_detect.jpg", "pos": "72% 50%"}, "step_draw.jpg", "step_pixelate.jpg"]),
        ("text", "Draw to Print",
         "사용자가 그린 그림은 세 단계를 거쳐 바닥에 출력됩니다. 먼저 화면에 입력된 그림을 20×12의 점 데이터로 바꿉니다. 이 데이터를 "
         "배열 값에 따라 솔레노이드 밸브를 제어하는 신호로 전송합니다. 로봇이 0.5m/s로 직진하는 동안 12개의 밸브가 열리고 닫히면서 "
         "입력한 그림이 바닥에 출력됩니다.",
         "A drawing is printed onto the ground in three steps. The drawing on the screen is first converted into 20×12 dot "
         "data. That data is sent as control signals that open and close the solenoid valves according to the array. "
         "While the robot drives straight at 0.5 m/s, twelve valves open and close and the drawing appears on the ground."),
        ("text", "Reach for Everyone",
         "터치 디스플레이 높이는 신장 120cm 어린이부터 180cm 성인, 휠체어 이용자까지 함께 사용할 수 있도록 폼보드 "
         "프로토타이핑으로 설정했습니다. 세 조건의 도달 범위를 비교해 상단 패널의 높이를 결정했고, 조작 요소는 상단 한 면에 모아 한 자리에서 입력을 끝낼 수 있게 했습니다.",
         "The touch display height was set so that children from 120 cm, adults up to 180 cm and wheelchair users can all "
         "use it. The panel height was decided by comparing the reach ranges of these three conditions, and all controls "
         "are placed on a single upper face so input is completed from one position."),
        ("text", "Material &amp; Assembly",
         "외피는 PLA로 3D 프린팅한 뒤 조립해 제작했습니다. 내부 지지대는 알루미늄 프로파일로 짜서 외피와 부품의 하중을 프레임이 받도록 "
         "했습니다. 전시장에서 직접 운용하는 것을 전제로 했기 때문에 부품 교체와 정비가 가능한 조립 구조로 만들었습니다.",
         "The outer shell was 3D printed in PLA and then assembled. The internal support was built from aluminium profiles "
         "so that the frame carries the load of the shell and components. Since the robot was to be operated on "
         "exhibition floors, it was built as an assembled structure that allows parts to be replaced and serviced."),
        ("pair", [{"f": "inner_front.jpg", "r": "natural"}, "inner_rear.jpg"]),
        ("text", "Internal Structure",
         "물을 사용하는 로봇이기 때문에 누수가 전자부에 닿지 않도록 내부를 분리했습니다. 배선과 제어 부품(NI myRIO · LattePanda)은 "
         "전면에, 물탱크와 펌프·분배 호스·솔레노이드 밸브는 방수 패널로 나눈 뒤쪽 공간에 배치했습니다.",
         "Because the robot uses water, the interior was divided so that leaks cannot reach the electronics. Wiring and "
         "control components (NI myRIO, LattePanda) sit at the front, while the water tank, pump, distribution hoses and "
         "solenoid valves are in a rear compartment behind a waterproof panel."),
        ("split",
         ("LiDAR Sensor", "하부 LiDAR 센서로 전방의 사람을 인식해 주행을 멈추고 그림 입력 단계로 넘어갑니다.",
          "The lower LiDAR sensor detects a person ahead, stops the robot, and moves to the drawing input step."),
         ("Water Level LED", "몸통 뒷면 LED로 물 잔량을 확인하고, 전면 하단 커버를 열어 배터리를 교체합니다.",
          "An LED on the rear shows the remaining water, and the battery is replaced through the lower front cover.")),
        ("dark", [
            ("grid", ["build_paint.jpg", "build_chassis.jpg", "build_head.jpg", "build_valves.jpg", "test_print.jpg", "build_assembly.jpg"]),
            ("row", "PROCESS",
             "엔지니어 4명과 디자이너 1명으로 구성된 팀에서 디자인 전체를 담당했습니다. 엔지니어링에서 구현 범위 설정과 코딩, 플랫폼 조립, "
             "전기 배선을 맡는 동안 스케치와 3D 모델링, 렌더링, 3D 프린팅, 프로토타이핑, 영상 제작을 진행했습니다. 외장 3D 프린팅·도장 → "
             "플랫폼·배선 → 헤드 프로토타입 → 방수 설계 → 출력 테스트 → 조립 순으로 만들었습니다.",
             "In a team of four engineers and one designer, I handled the entire design track. While engineering covered "
             "scoping, coding, platform assembly and wiring, I worked on sketching, 3D modelling, rendering, 3D printing, "
             "prototyping and film. The build went from printed and painted shell, platform and wiring, head prototype, "
             "waterproofing and print tests to final assembly."),
            ("row", "IN THE FIELD",
             "완성한 로봇은 2023 로보월드와 서울디자인페스티벌, 2024 HCI KOREA 전시에서 직접 운용했습니다. 프로토타입은 원격 조종으로 "
             "주행하고, 사람을 인식해 정지한 뒤 그림을 받고, 0.5m/s로 직진하며 12개 노즐로 출력합니다. 34°C에서도 물 그림이 5분 이상 "
             "유지됐습니다. 이 프로젝트로 HCI KOREA 2024 Creative Award 최우수상을 받았고, 특허와 디자인을 등록했습니다.",
             "The robot was operated at Robot World 2023, the Seoul Design Festival and the HCI KOREA 2024 exhibition. The "
             "prototype is driven by remote control; it detects a person, stops to receive a drawing, and prints with twelve "
             "nozzles while advancing at 0.5 m/s. At 34°C the drawings stayed visible for more than five minutes. The project "
             "received the Excellence Award (최우수상) at the HCI KOREA 2024 Creative Award and was granted a patent and a "
             "design registration."),
            ("roles", ["리서치", "컨셉 수립", "디자인 스케치", "내부 부품 배치 기반 구조 설계", "3D 모델링·렌더링", "3D 프린팅",
                       "도장", "워킹 프로토타입 제작", "특허 서류 및 도면 제작"]),
        ]),
        ("bleed", "print_field.jpg", "natural"),
        ("band",),
    ],
)

# =====================================================================
UX_ROLE = ["선행 연구", "UX 리서치 및 아이템 발굴", "프로토타이핑", "검증"]

PAGES["inclusive"] = dict(
    dir="inclusive", cat_key="ux", title="Inclusive Mobility", year="2023", category="UX Research · Hyundai",
    desc="현대자동차 Inclusive 기반 미래 모빌리티 UX디자인 및 편의장치 개발",
    lede="시각·청각 장애인부터 노약자, 어린이까지 <b>누구나 안전하게 타고 내릴 수 있는 PBV</b>의 UX와 편의장치를 설계했습니다.",
    hero="door_ramp.jpg",
    meta=[("Term", "2023.02 — 2023.05"), ("Client", "현대디자인센터 퓨처모빌리티디자인팀"),
          ("Team", "석사연구원 4 · 학부연구원 3"), ("Method", "애자일 · 1:1 프로토타입"),
          ("Role", "선행 연구 · UX 아이템 발굴 · 프로토타입 · 검증")],
    intro=([("HMC", "2023.02 — 05", "Hyundai Design Center", "퓨처모빌리티디자인팀 산학 과제"),
            ("1:1", "Prototype", "폼보드 · 3D 프린팅", "도어 · 도어스텝 · 시트 목업")],
           "누구나 안전하게 타고 내리는 PBV",
           "A PBV that anyone can board safely",
           "양방향 슬라이드 도어와 도어스텝, 어시스트 시트, 휠체어 고정 장치, 논슬립 그래픽, eHMI까지 승하차와 실내 이동의 불편을 항목별로 "
           "찾아 해결안을 만들고, <b>3D 프린팅과 1:1 폼보드 목업</b>으로 직접 타 보며 검증했습니다.",
           "From two-way sliding doors and door steps to an assist seat, wheelchair lock, non-slip graphics and eHMI, each "
           "pain point in boarding and moving inside the cabin was turned into a solution and verified by actually using "
           "3D-printed parts and full-scale foam-board mock-ups."),
    sections=[
        ("dark", [
            ("img", {"f": "door_wheelchair_test.jpg", "r": "natural"}),
            ("row", "BOARDING",
             "양방향 슬라이드 도어로 출입구를 완전히 열고, 도어스텝이 계단 또는 경사판으로 내려와 휠체어도 바로 탈 수 있습니다. "
             "투명 디스플레이 보조도어와 탑승 신호 eHMI 시나리오도 함께 제안했습니다.",
             "Two-way sliding doors open the entrance fully, and the door step lowers as stairs or a ramp so wheelchairs can "
             "board directly. A transparent-display auxiliary door and an eHMI boarding-signal scenario were also proposed."),
            ("dots", ["doorstep_led_test.jpg", "nonslip_pattern.jpg", "wheelchair_fold.jpg"]),
            ("row", "INTERIOR",
             "실내에서는 일어서고 앉는 동작, 휠체어 고정, 좌석 배치를 다뤘습니다. 도어와 도어스텝은 1:1 목업으로 만들어 휠체어로 직접 "
             "진입하며 폭과 경사를 확인했습니다.",
             "Inside, the work covered standing up and sitting down, securing wheelchairs and seat layout. The door and door "
             "step were built as full-scale mock-ups and checked by actually entering with a wheelchair."),
            ("img", {"f": "s_tdisplay.jpg", "r": "natural"}, ' style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;"'),
        ]),
        ("text", "Assist Seat",
         "노약자가 앉고 일어서는 동작을 돕는 어시스트 시트를 제안했습니다.",
         "An assist seat was proposed to help elderly passengers sit down and stand up."),
        ("bleed", "assist_pair.jpg", "natural"),
        ("split",
         ("Wheelchair Lock", "이동형 모빌리티 안에서 휠체어를 고정하는 장치를 제안했습니다.",
          "A device that secures wheelchairs inside the moving vehicle."),
         ("Flexible Seating", "상황에 따라 좌석 배치를 바꾸는 이동형 좌석 배치 시나리오를 제안했습니다.",
          "A movable seating scenario that changes the layout to suit the situation.")),
        ("pair", [{"f": "s_wc_lock.jpg", "r": "natural"}, "s_ehmi_front.jpg"]),
        ("text", "eHMI",
         "차량 외부에서 이륜차에 승하차를 알리고 보행자에게 횡단을 안내하는 eHMI 시나리오를 제안했습니다.",
         "eHMI scenarios were proposed to alert two-wheelers to boarding passengers and to guide pedestrians across."),
        ("bleed", "s_seat_layout.jpg", "natural"),
        ("dark", [
            ("row", "PROCESS",
             "애자일 방식으로 아이템을 빠르게 만들고 1:1 목업으로 확인하는 과정을 반복했습니다.",
             "In an agile process, items were built quickly and checked again and again on full-scale mock-ups."),
            ("roles", ["선행 연구", "UX 아이템 발굴", "프로토타이핑", "UX 리서치 및 검증"]),
        ]),
        ("bleed", "s_laser.jpg", "natural"),
        ("band",),
    ],
)

PAGES["seuv"] = dict(
    dir="seuv", cat_key="ux", title="SeUV UX", year="2022 — 2023", category="UX Research · Hyundai",
    desc="현대자동차 대형 SeUV 공간 및 웰니스 컨셉 USP 항목 UX디자인",
    lede="대형 SeUV의 <b>실내 공간과 웰니스 경험</b>을 위한 컨셉을 발굴하고, PoC 목업으로 만들어 사용성 테스트에 썼습니다.",
    hero="s_mood.jpg",
    meta=[("Term", "2022.12 — 2023.01"), ("Client", "현대자동차 제품UX팀 × 마크로밀엠브레인"),
          ("Team", "석사연구원 4 · 학부연구원 4"), ("Output", "PoC 목업 · 사용성 테스트"),
          ("Role", "선행 연구 · UX 리서치 · 아이템 발굴 · 프로토타이핑")],
    intro=([("HMC", "2022.12 — 2023.01", "Hyundai Product UX", "× 마크로밀엠브레인"),
            ("PoC", "Usability Test", "PoC 목업", "항목별 사용성 테스트")],
           "쉬고, 머무는 대형 SeUV",
           "A large SeUV made for resting and staying",
           "캐빈 살균, 무드 큐레이터, 감성형 앰비언트 라이트, 원격 시트 베리에이션, 후석 엔터테인먼트, OTT 디스플레이, "
           "클램쉘 테일게이트 등 공간과 웰니스 항목을 발굴하고, 항목별로 <b>3D 애니메이션, 앱 UI, 1:1 폼보드 목업</b>으로 구체화했습니다.",
           "Space and wellness items such as cabin sterilisation, a mood curator, responsive ambient light, remote seat "
           "variation, rear entertainment, OTT displays and a clamshell tailgate were developed and made concrete through "
           "3D animation, app UI and full-scale foam-board mock-ups."),
    sections=[
        ("dark", [
            ("img", {"f": "s_ott.jpg", "r": "natural"}),
            ("row", "SPACE",
             "테일게이트를 펼쳐 앉고 쉬는 공간으로 쓰도록, 그 위에서 쓰는 액세서리를 1:1 폼보드로 만들어 직접 시연했습니다.",
             "To use the opened tailgate as a place to sit and rest, the accessories used on it were built in full-scale "
             "foam board and demonstrated in person."),
            ("dots", ["s_luggage.jpg", "s_tray.jpg", "s_cupholder.jpg"]),
            ("row", "WELLNESS",
             "시트 배열 7가지 모드, 후석 보조 모니터, 캐빈 살균 로직, 무드 큐레이터 등 웰니스 항목을 시나리오와 목업으로 구체화했습니다.",
             "Wellness items such as seven seat-arrangement modes, rear auxiliary monitors, cabin-sterilisation logic and a mood curator were "
             "developed through scenarios and mock-ups."),
            ("img", {"f": "s_ambient.jpg", "r": "natural"}, ' style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;"'),
        ]),
        ("text", "Clamshell Tailgate",
         "테일게이트 컵홀더, 실리콘 트레이 A/B 타입과 러기지보드 A/B/C 타입, 베드 끝에 수납되는 발걸이를 폼보드로 만들어 "
         "실제 높이와 크기를 확인했습니다.",
         "Tailgate cup holders, silicone trays (types A/B), luggage boards (types A/B/C) and a footrest that stows at the "
         "end of the bed were made in foam board to check real heights and sizes."),
        ("pair", [{"f": "clamshell_crop.jpg", "r": "natural"}, "clamshell_step.jpg"]),
        ("text", "Seat Variation",
         "앱으로 1·2·3열 시트를 원격 조절하는 시트 배열 7가지 모드를 제안했습니다.",
         "Seven seat-arrangement modes were proposed, with first- to third-row seats adjusted remotely from an app."),
        ("bleed", "seat_modes.jpg", "natural"),
        ("split",
         ("Rear Entertainment", "후석 보조 모니터를 인치별로 실차에서 비교 검증했습니다.",
          "Rear auxiliary monitors were compared by screen size in a real vehicle."),
         ("OTT Display", "고정형과 팝업형 OTT 디스플레이를 제안했습니다.",
          "Fixed and pop-up OTT displays were proposed.")),
        ("pair", [{"f": "s_ott_popup.jpg", "r": "natural"}, "rear_display_test.jpg"]),
        ("dark", [
            ("row", "PROCESS",
             "항목마다 PoC 목업을 만들어 마크로밀엠브레인의 사용성 테스트에 썼습니다.",
             "A PoC mock-up was built for each item and used in Macromill Embrain's usability tests."),
            ("roles", UX_ROLE),
        ]),
        ("band",),
    ],
)

PAGES["ev-sedan"] = dict(
    dir="ev-sedan", cat_key="ux", title="EV Sedan UX", year="2022", category="UX Research · Hyundai",
    desc="현대자동차 준대형 전기세단 UX 디자인 컨셉 솔루션 발굴",
    lede="UX 아이템 10가지를 발굴해 시나리오는 영상으로, 실내 아이템은 <b>폼보드 PoC</b>로 만들어 직접 써 보며 검증했습니다.",
    hero="ev_scene_console.jpg",
    meta=[("Term", "2022.09 — 2022.11"), ("Client", "현대자동차 제품UX팀 × 마크로밀엠브레인"),
          ("Team", "석사연구원 3 · 학부연구원 3"), ("Output", "폼보드 PoC · 시나리오 영상"),
          ("Role", "선행 연구 · UX 리서치 · 아이템 발굴 · 프로토타이핑")],
    intro=([("HMC", "2022.09 — 11", "Hyundai Product UX", "× 마크로밀엠브레인"),
            ("10", "UX Items", "아이템 10가지", "시나리오 영상 · 폼보드 PoC")],
           "써 보며 고른 전기세단 UX",
           "EV sedan UX items, chosen by using them",
           "커넥티드 서비스, 자동 공조, 주행·주차, 감시모드, 파워 도어, 인테리어 커스텀 모드, 확장형 센터콘솔, 테이블, 컵홀더, "
           "트렁크 러기지박스까지 10가지 아이템을 발굴했습니다. 시나리오는 3D 애니메이션·영상으로, 실내 아이템 4종은 "
           "<b>폼보드 PoC</b>로 만들었고, 이 PoC는 "
           "마크로밀엠브레인의 실사용자 사용성 테스트에 쓰였습니다.",
           "Ten items were developed: connected services, automatic climate, driving and parking, surveillance mode, power "
           "doors, interior custom modes, an expandable centre console, a table, cup holders and a trunk luggage box. "
           "Scenarios were shown as 3D animations and videos, and four interior items were built as foam-board PoCs, which were used in Macromill Embrain's usability tests with real users."),
    sections=[
        ("dark", [
            ("img", {"f": "s_hud.jpg", "r": "natural"}),
            ("row", "SCENARIO",
             "공조 폭염/한파 모드, HUD U턴 가이드, 충돌 전후 10초를 녹화하는 감시 모드, Relax · Cinema 커스텀 모드 같은 시나리오 "
             "아이템은 3D 애니메이션·영상으로 표현했습니다.",
             "Scenario items such as heatwave/cold-snap climate modes, a HUD U-turn guide, a surveillance mode that records "
             "ten seconds before and after a collision, and Relax and Cinema custom modes were shown as 3D animations and videos."),
            ("dots", ["s_aircon.jpg", "s_relax.jpg", "s_cinema.jpg"]),
            ("row", "INTERIOR",
             "실내 아이템 4종은 폼보드 PoC로 만들어 1·2열 배치를 재현하고 직접 사용해 보며 검증했습니다. 테이블은 애프터마켓 "
             "테이블 아이디어 3안을 도출해 실차에서 검증했습니다.",
             "Four interior items were built as foam-board PoCs that reproduce the first- and second-row layout and were "
             "verified by using them. For the table, three aftermarket table ideas were developed and tested in a real car."),
            ("img", {"f": "ev_table_ioniq6.jpg", "r": "natural"}, ' style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;"'),
        ]),
        ("text", "Expandable Center Console",
         "콘솔에서의 1열·2열 수납, 컵홀더, 무선충전, V2L 활용 아이디어를 제안했습니다. 확장 모드는 1열 중심 · 1·2열 공유 · "
         "2열 중심 세 가지이고, 1:1 폼보드 PoC로 검증했습니다.",
         "Ideas for front- and rear-row storage, cup holders, wireless charging and V2L in the console were proposed, with "
         "three extension modes (front-focused, shared, rear-focused) verified on a full-scale foam-board PoC."),
        ("pair", [{"f": "ev_console_poc.jpg", "r": "natural"}, "ev_console_test.jpg"]),
        ("split",
         ("Cup Holder", "센터콘솔 하단 트레이 폴딩 컵홀더 아이템을 제안했습니다.", "A folding cup holder in the tray under the centre console."),
         ("Trunk Luggage Box", "트렁크 러기지박스의 컵홀더와 공간 분할 아이템을 도출하고 검증했습니다.", "Cup-holder and space-dividing items for a trunk luggage box, developed and verified.")),
        ("pair", [{"f": "ev_cupholder_poc.jpg", "r": "natural"}, "ev_trunk_poc.jpg"]),
        ("dark", [
            ("row", "USABILITY TEST",
             "폼보드 PoC는 마크로밀엠브레인의 실사용자 사용성 테스트에 쓰였습니다.",
             "The foam-board PoCs were used in Macromill Embrain's usability tests with real users."),
            ("roles", UX_ROLE),
        ]),
        ("band",),
    ],
)
