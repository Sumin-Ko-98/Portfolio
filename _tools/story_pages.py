"""상세페이지 내용 (gen_story.py 가 읽음). 사실 기준 = _tools/인수인계.md 3절.
문단은 HTML 그대로 들어간다(<b> 사용 가능, & 는 &amp;).
SOURCES: assets/works/<dir>/<이름> 이 없을 때만 쓰는 원본 경로(윈도우). 한 번 만들어지면 레포의 assets 를 쓴다.
"""
import os

LS = r"C:\Users\Hkyum\iCloudDrive\04_포트폴리오\261006 LS 포트폴리오"
HEIC = r"C:\Users\Hkyum\AppData\Local\Temp\claude\C--Users-Hkyum-iCloudDrive\1054dd20-8098-478f-a7d0-c5556a0bf222\scratchpad\heic"  # HEIC → JPG 변환본
J = os.path.join
BEHANCE = r"C:\Users\Hkyum\AppData\Local\Temp\claude\C--Users-Hkyum-iCloudDrive\1054dd20-8098-478f-a7d0-c5556a0bf222\scratchpad\behance_flever"
# 옛 포트폴리오(240430) PDF 쪽 이미지(1920×1080, 쪽마다 한 장)를 뽑아 둔 폴더 — p14.png 등
OLD = r"C:\Users\Hkyum\AppData\Local\Temp\claude\C--Users-Hkyum-iCloudDrive\1054dd20-8098-478f-a7d0-c5556a0bf222\scratchpad\old"
def OLDP(n, crop):
    return {"src": os.path.join(OLD, f"p{n}.png"), "crop": crop}
FINAL_PDF = r"C:\Users\Hkyum\AppData\Local\Temp\claude\C--Users-Hkyum-iCloudDrive\1054dd20-8098-478f-a7d0-c5556a0bf222\scratchpad\final_portfolio.pdf"  # 최종 제출 PDF 사본
ROT_CW = 90  # EXIF 6 — pymupdf insert_image rotate=90 이 맞음(270은 뒤집혀 보였음, 리뷰 확인)

# PDF 순서: TS450 → TS700 → H500 → WADE → CMF, 이어서 대학원 작업과 UX
ORDER = ["threespin", "ts700", "h500", "wade", "odm-cmf", "mobilink", "flever", "inclusive", "seuv", "ev-sedan"]

SOURCES = {
    "ts450": {
        "cover_src.jpg": J(LS, "_시안", "assets", "ts450", "cover_src.jpg"),
        "main_pers.jpg": J(LS, "TS450", "TS450_Main_Pers.png"),
        "side_02.jpg": J(LS, "TS450", "TS450_Side_02.png"),
        "front_sq.jpg": {"src": J(LS, "TS450", "TS450_Front_Pers.png"), "trim": 0.08, "square": True},
        "side_sq.jpg": {"src": J(LS, "TS450", "TS450_Side_02.png"), "trim": 0.05, "square": True},
        "macro2.jpg": J(LS, "TS450", "genspark", "gs_ts450_mop_macro_02.png"),
        # 최종 PDF 7쪽의 주석(화살표·라벨) 포함 Before / After / Cradle
        "sensor_before_pdf.jpg": {"pdf": FINAL_PDF, "page": 6, "rect": (584, 120, 1194, 529), "scale": 2},
        "sensor_after_pdf.jpg": {"pdf": FINAL_PDF, "page": 6, "rect": (1210, 120, 1820, 529), "scale": 2},
        "sensor_cradle_pdf.jpg": {"pdf": FINAL_PDF, "page": 6, "rect": (584, 582, 1820, 959), "scale": 1.5},
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
        "cover_src.jpg": J(LS, "_시안", "assets", "ts700", "cover_src.jpg"),
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
        "ctrl_pers.jpg": J(LS, "_시안", "assets", "h500", "ctrl_pers.jpg"),
        "wheel_chair_side.jpg": J(LS, "_시안", "assets", "h500", "wheel_chair_side.jpg"),
        "mock_ctrl3.jpg": J(LS, "H500", "H500_Mockup_Controller_03.jpg"),
        "ctrl_cover_src.jpg": J(LS, "_시안", "assets", "h500", "ctrl_cover_src.jpg"),
        "wheel_cover_src.jpg": J(LS, "_시안", "assets", "h500", "wheel_cover_src.jpg"),
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
        "q3t_set.jpg": J(LS, "ODM", "260714_Q3 Turbo_Set_Pers R 20_v1.png"),
        "ts402m_tilt.jpg": J(LS, "ODM", "260319_TS402M_3DR_Set_Front Tilting_v1.png"),
        "q9_side.jpg": J(LS, "ODM", "Q9_Set_Side_R.png"),
        "q9_front.jpg": J(LS, "ODM", "Q9_Set_Front.png"),
        "cmf_book.jpg": {"src": J(LS, "Work_Photos", "CMF_Color_Book_6775.JPG"), "rot": ROT_CW},  # EXIF 6
        "cmf_chips.jpg": J(HEIC, "CMF_Color_Chips_7998.jpg"),
        "cmf_sample.jpg": J(HEIC, "CMF_Sample_Check_0013.jpg"),
        "pantone1.jpg": J(HEIC, "CMF_Silk_Pantone_0954.jpg"),
        "pantone2.jpg": J(HEIC, "CMF_Silk_Pantone_0955.jpg"),
        "q9_topcover.jpg": J(HEIC, "Q9_TopCover_Photo.jpg"),
    },
    "wade": {
        "studio.jpg": J(LS, "WADE", "genspark", "gs_wade_studio_01.png"),
        "step_detect2.jpg": {"src": J(LS, "_시안", "assets", "wade", "step_detect.jpg"), "crop": (0.40, 0.0, 0.985, 1.0)},
        "kid_draw.jpg": J(LS, "WADE", "genspark", "gs_wade_kid_draw_DtsenQa9.jpg"),
        "drone.jpg": J(LS, "WADE", "genspark", "gs_wade_drone_UFcdm34p.jpg"),
        "nozzle1.jpg": J(LS, "WADE", "genspark", "gs_wade_nozzle_6KZTCK5o.jpg"),
        "nozzle2.jpg": J(LS, "WADE", "genspark", "gs_wade_nozzle_It2CF2g5.jpg"),
        "result_heart.jpg": J(LS, "_시안", "assets", "wade", "result_heart.jpg"),
    },
    # 옛 포트폴리오 PDF 14–21쪽 (MobiLink) / 30–35쪽 (Flever). crop = 쪽 안 비율 좌표
    "mobilink": {
        "hero3.jpg": OLDP(14, (0.38, 0.19, 1.0, 0.80)),  # 왼쪽 아래 PDF 글자 · 오른쪽 위 Spark 로고 제외
        "render_sq.jpg": {**OLDP(15, (0.42, 0.10, 1.0, 0.98)), "square": True},
        "connect2.jpg": OLDP(16, (0.0, 0.0, 1.0, 0.67)),  # Mobility·Home 라벨 포함
        "mobility.jpg": OLDP(17, (0.0, 0.06, 0.5, 0.49)),
        "home.jpg": OLDP(17, (0.5, 0.06, 1.0, 0.49)),
        "tech_glazing.jpg": OLDP(17, (0.035, 0.66, 0.26, 0.88)),
        "tech_display.jpg": OLDP(17, (0.27, 0.66, 0.49, 0.88)),
        "dock_diagram.jpg": OLDP(20, (0.76, 0.63, 0.98, 0.80)),  # PBV Docking Step 도식
        "speaker_panel.jpg": OLDP(20, (0.02, 0.10, 0.58, 0.62)),  # 측면 스마트 서피스 스피커
        "dock_step.jpg": OLDP(20, (0.0, 0.52, 0.50, 0.98)),  # 도킹 스텝 (PDF 주석 제외)
        "handle.jpg": OLDP(18, (0.0, 0.14, 1.0, 0.33)),
        "multi_clean.jpg": OLDP(18, (0.17, 0.50, 0.80, 1.0)),  # PDF 주석 글자 제외
        "storage.jpg": OLDP(19, (0.26, 0.22, 0.68, 1.0)),
        "storage_side.jpg": OLDP(19, (0.69, 0.22, 1.0, 1.0)),
        "lifestyle.jpg": OLDP(21, (0.0, 0.0, 1.0, 0.79)),
    },
    "flever": {
        # Behance 본인 프로젝트 원본 19장 (behance.net/gallery/145103341/flever, 사용자 승인 후 source 해상도 다운로드)
        # m01~m19 = Behance 페이지 순서. m07·m10 GIF 는 ffmpeg 로 anim_screen.mp4 · anim_hinge.mp4 (레포에 직접 저장)
        "bh_hero.jpg": J(BEHANCE, "m01.png"),
        "bh_ui_hello.jpg": {"src": J(BEHANCE, "m04.png"), "crop": (0.42, 0.50, 0.68, 0.80)},  # UI 화면 한 장 확대
        "bh_set.jpg": J(BEHANCE, "m02.png"),
        "bh_pair.jpg": J(BEHANCE, "m03.png"),
        "bh_ui.jpg": J(BEHANCE, "m04.png"),
        "bh_magnet.jpg": J(BEHANCE, "m05.png"),
        "bh_wall.jpg": J(BEHANCE, "m06.jpg"),
        "bh_green.jpg": J(BEHANCE, "m08.png"),
        "bh_grey.jpg": J(BEHANCE, "m09.png"),
        "bh_hinge.jpg": J(BEHANCE, "m11.png"),
        "bh_hinge_side.jpg": J(BEHANCE, "m12.png"),
        "bh_exploded.jpg": J(BEHANCE, "m13.png"),
        "bh_usbc.jpg": J(BEHANCE, "m14.png"),
        "bh_speaker.jpg": J(BEHANCE, "m15.png"),
        "bh_cable.jpg": J(BEHANCE, "m16.png"),
        "bh_call.jpg": J(BEHANCE, "m17.png"),
        "bh_ideation.jpg": J(BEHANCE, "m18.png"),
        "bh_sketch.jpg": J(BEHANCE, "m19.png"),
    },
    "inclusive": {
        "door_test_crop.jpg": {"src": J(LS, "_시안", "assets", "ux", "inclusive", "door_wheelchair_test.jpg"),
                               "crop": (0.26, 0.04, 1.0, 0.92)},  # 왼쪽 잡동사니 제외
        "s_ehmi_side.jpg": J(LS, "_시안", "assets", "ux", "inclusive", "s_ehmi_side.jpg"),
    },
    "seuv": {
        "s_ott.jpg": J(LS, "_시안", "assets", "ux", "seuv", "s_ott.jpg"),
    },
    "ev-sedan": {
        # 기아 엠블럼·번호판이 보이는 차량 패널(2·3번)은 제외하고 대시보드·시트 패널만
        "s_aircon_dash.jpg": {"src": J(LS, "_시안", "assets", "ux", "ev_sedan", "s_aircon.jpg"), "crop": (0.0, 0.0, 0.245, 1.0)},
        "s_aircon_seat.jpg": {"src": J(LS, "_시안", "assets", "ux", "ev_sedan", "s_aircon.jpg"), "crop": (0.755, 0.0, 1.0, 1.0)},
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
    hero="cover_src.jpg",
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
            ("img", {"f": "macro.jpg", "pos": "50% 60%"}),
            ("row", "FORM",
             "<b>#슬림 · #심리스 · #미니멀</b> — 세 가지 키워드로 형태를 정리했습니다. ROBO-SPIN 구조의 세 회전 패드 배치가 "
             "그대로 삼각형 외형으로 이어졌고, 다양한 R값으로 모서리를 다듬어 원형 로봇청소기와 다른 조형 언어를 만들었습니다.",
             "The form was organised around three keywords: slim, seamless and minimal. The layout of the three rotating pads in the "
             "ROBO-SPIN structure carries straight into a triangular silhouette, and corners finished with varied radii "
             "give it a form language distinct from round robot vacuums."),
            ("dots", ["padchange_gs.jpg", "shelf_gs.jpg", "macro2.jpg"]),
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
         "다른 인상을 만듭니다.",
         "A black sensor-window line wraps the body through 360 degrees and leads the eye horizontally, while corners "
         "finished with varied radii set it apart from round robot vacuums."),
        ("square", {"f": "main_pers.jpg", "fit": "contain", "bg": "auto", "pad": "7%"}),
        ("tri", ["front_sq.jpg",
                 "side_sq.jpg", "topview.jpg"]),
        ("text", "Low Proportion",
         "상단부 두께를 최소화하고 측면 라인이 바닥으로 흘러내리도록 처리해 바닥에 밀착된 인상을 줍니다. 개발 중 IR 센서가 "
         "측후면으로 이동한 뒤에도 손잡이·상면 곡률·센서창 비율을 함께 조정해 이 라인을 유지했습니다.",
         "The top is kept as thin as possible and the side line flows down to the floor, so the robot looks pressed to "
         "the ground. When the IR sensor moved to the rear side during development, the handle, top curvature and "
         "sensor-window proportions were adjusted together to keep this line."),
        ("bleed", {"f": "side_view.jpg", "fit": "contain", "bg": "auto", "pad": "3% 7%"}, "natural"),
        ("text", "Sensor Protection",
         "센서창 보호 단차와 함께, 크래들에 거치할 때도 센서창이 크래들에 직접 닿는 면을 없애 스크래치를 막았습니다. "
         "위 왼쪽이 이전 모델, 오른쪽이 TS450입니다.",
         "Besides the protective step, the cradle was shaped so that no surface touches the sensor window when the robot "
         "is docked. Left: previous model. Right: TS450."),
        ("pair", [{"f": "sensor_before_pdf.jpg", "r": "natural", "cap": "<b>Before</b>자사 이전 모델 · 센서창과 하우징이 같은 면"},
                  {"f": "sensor_after_pdf.jpg", "cap": "<b>After</b>TS450 · 상·하단 하우징이 센서창보다 돌출"}]),
        ("single", "sensor_cradle_pdf.jpg", "<b>Cradle</b>거치 시 센서창이 크래들에 닿지 않는 구조"),
        ("duo", ["robospin.jpg", {"f": "ui.jpg", "pos": "62% 50%"}]),
        ("split",
         ("ROBO-SPIN", "구동 바퀴 없이 세 개의 회전 패드만으로 이동과 청소를 동시에 수행합니다. 본체 무게가 세 패드에 실려 바닥을 눌러 닦습니다.",
          "With no drive wheels, three rotating pads both move the robot and clean; the body's weight presses the pads to the floor."),
         ("Simple UI", "시작·정지와 물 공급량 버튼 2개, 작동 상태를 알리는 라이트 라인, 음성 안내만으로 매뉴얼 없이 조작합니다.",
          "Two buttons for start/stop and water flow, a light line for status and voice guidance: no manual needed.")),
        ("text", "Mop Pads", "세 개의 회전 패드는 손쉽게 탈착·세탁할 수 있고, 세탁해 반복 사용할 수 있습니다.",
         "The three rotating pads detach easily and can be washed and reused."),
        ("bleed", "mop_pads.jpg", "macro"),
        ("text", "Storage &amp; CMF",
         "본체를 세워 결합하는 수직형 거치대로 보관 면적을 줄였습니다. 거치대도 본체와 같은 곡면·컬러·마감으로 통일해 보관 중에도 "
         "하나의 오브제로 읽힙니다.",
         "A vertical cradle that holds the robot upright reduces the storage footprint. The cradle shares the body's "
         "curves, colour and finish, so the two read as one object even in storage."),
        ("bleed", "cradle_shelf.jpg", "natural"),
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
        ("bleed", "overview_life.jpg", "natural"),
        ("band",),
    ],
)

# =====================================================================
PAGES["ts700"] = dict(
    dir="ts700", cat_key="product", title="Threespin Steam", year="2025 — 2026", category="Robot Mop · Everybot",
    desc="쓰리스핀 스팀 TS700 제품디자인 · 양산 지원",
    lede="스팀 모듈을 탑재한 쓰리스핀 로봇청소기입니다. 높아진 전고를 <b>슬림한 실루엣</b>으로 보이게 하고, "
         "<b>A/S 효율성을 높인 하우징 분할 구조</b>를 설계했습니다.",
    hero="cover_src.jpg",
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
            ("dots", [{"f": "mop_exploded.jpg", "pos": "50% 60%"}, {"f": "hand_cradle.jpg", "pos": "55% 50%"}, "steam_macro2.jpg"]),
            ("row", "APPROACH",
             "바텀 하우징 엣지에 대형 챔퍼를, 바텀 파트에 다크 톤 CMF를 적용해 하단부가 시각적으로 후퇴하도록 했습니다. "
             "그리고 바디를 바텀·미들·탑 3분할로 재구성해, 상단 전체를 해체하지 않고도 하단 모듈에 접근할 수 있게 했습니다.",
             "A large chamfer on the bottom-housing edge and a dark-tone CMF on the bottom part make the lower body visually "
             "recede. The body was then rebuilt as bottom, middle and top, so the lower module can be reached without "
             "dismantling the entire top."),
            ("img", {"f": "home2.jpg", "r": "natural"}, ' style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;"'),
        ]),
        ("scene", {"f": "hero_gs.jpg", "r": "natural"}),
        ("text", "Slim Look",
         "사용자가 서서 내려다보는 시선 각도에서는 챔퍼로 덜어낸 측면과 어두운 하단이 잘 보이지 않습니다. 그래서 실제 전고보다 "
         "얇은 바디로 인지됩니다.",
         "From the angle at which a standing user looks down, the chamfered side and the dark lower part barely register, "
         "so the body is perceived as thinner than its actual height."),
        ("bleed", "eye_angle.png", "natural"),
        ("tri", [{"f": "cutout_front.jpg", "fit": "contain", "bg": "auto", "pad": "9%"},
                 {"f": "pers5.jpg", "fit": "contain", "bg": "auto", "pad": "9%"},
                 {"f": "cradle2.jpg", "fit": "contain", "bg": "auto", "pad": "9%"}]),
        ("text", "3-Part Body",
         "하우징을 바텀·미들·탑 3분할 구조로 재구성해, 상단 전체를 해체하지 않고도 하단 모듈에 접근할 수 있도록 "
         "서비스성을 개선했습니다.",
         "The housing was rebuilt in three parts (bottom, middle and top), so the lower module can be reached without "
         "dismantling the whole top."),
        ("bleed", {"f": "three_part_body.jpg", "fit": "contain", "bg": "auto", "pad": "2% 8%"}, "natural"),
        ("text", "Product Details",
         "물통은 래치 방식으로 탈착하고, 사용하지 않을 때는 거치대에 세워 보관합니다.",
         "The water tank detaches with a latch, and the robot stands upright on its cradle when not in use."),
        ("pair", [{"f": "detail_top_cover.jpg", "r": "natural"}, "detail_storage.jpg"]),
        ("split",
         ("Water Tank", "래치 방식으로 탈착하는 물통", "A water tank that detaches with a latch."),
         ("Storage", "거치대에 세워 보관", "Stored upright on its cradle.")),
        ("text", "LED UI · Sound", "동작 사양에 따른 라이팅 UI와 음성 안내를 설계하고, 효과음·TTS를 제작했습니다.",
         "Lighting UI and voice guidance were designed from the operating specification, with sound effects and TTS produced in-house."),
        ("text", "CMF", "다양한 컬러의 디자인 목업을 제작·검토한 뒤 CMF와 실크를 확정했습니다.",
         "Design mock-ups in a range of colours were built and reviewed before the CMF and silk-screen were fixed."),
        ("dark", [
            ("grid", ["mockup_2325.jpg", "photo_0188.jpg", "mockup_1109.jpg"]),  # 같은 구도 2323·2324 제외, 다른 공정 사진은 보유분 없음
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
    hero={"f": "wheel_cover_src.jpg", "fit": "contain", "bg": "auto", "pad": "4% 0"},  # 컨트롤러 투시는 Final Design 3열에 있어 히어로는 휠
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
        ("text", "Button Grouping &amp; Display",
         "레드 전원 버튼을 중심으로 라이트·비상등·경적 버튼을 기능별로 묶고, 표시부를 버튼 위에 두어 누르는 손에 가려지지 않게 "
         "했습니다.",
         "Light, hazard and horn buttons are grouped by function around the central red power button, and the display "
         "sits above the buttons so the pressing hand never hides it."),
        ("tri", [{"f": "ctrl_pers.jpg", "fit": "contain", "bg": "auto", "pad": "10%",
                  "cap": "<b>Perspective</b>레드 전원 버튼 중심 · 라이트·비상등·경적"},
                 {"f": "ctrl_top.jpg", "fit": "contain", "bg": "auto", "pad": "10%",
                  "cap": "<b>Top</b>탈착해 왼손잡이도 쓰는 팜레스트"},
                 {"f": "ctrl_side.jpg", "fit": "contain", "bg": "auto", "pad": "10%",
                  "cap": "<b>Side</b>기성품 조이스틱으로 원가 절감"}]),
        ("text", "Mock-up",
         "3D 프린팅 목업으로 직접 쥐고 조작하며 형상과 버튼 배치를 다듬었습니다.",
         "3D-printed mock-ups were held and operated to refine the form and button layout."),
        ("text", "In-wheel Motor Wheel",
         "수전동휠체어의 구동부를 휠 안에 담은 인휠모터 휠입니다. 3-스포크의 스포크 인서트를 원하는 컬러로 커스텀할 수 있도록 "
         "확장성을 고려해 디자인했습니다.",
         "An in-wheel motor wheel that places the wheelchair's drive unit inside the wheel. The inserts of its three "
         "spokes were designed to be customised in any colour."),
        ("square", "gs_wheel_side.jpg"),  # 휠체어 렌더 원본은 모두 발판이 잘려 있어 휠 측면 컷 사용
        ("text", "Hand Rim",
         "손으로 수동 주행할 때를 고려해 메탈 핸드림의 두께와 휠과의 간격을 설정했습니다.",
         "The thickness of the metal hand rim and its gap from the wheel were set for manual propulsion."),
        ("dark", [
            ("grid", ["mock_wheel1.jpg", "wheel_cmf_mockup.jpg", "wheel_color_chips.jpg"]),  # 3열 한 줄 (5장이면 빈 칸이 생김)
            ("row", "MOCK-UP &amp; CMF",
             "스포크 인서트 컬러와 핸드림 블랙 / 실버 마감을 실물 목업으로 비교하고, 컬러칩 5종으로 최종 컬러를 확인했습니다.",
             "Spoke-insert colours and black / silver hand-rim finishes were compared on physical mock-ups, and the final "
             "colours were checked against five colour chips."),
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
    hero="cmf_chips.jpg",
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
            ("img", {"f": "cmf_book.jpg", "pos": "50% 45%"}),
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
        ("pair", [{"f": "q9_front.jpg", "fit": "contain", "bg": "auto", "pad": "7%"}, {"f": "q9_side.jpg", "fit": "contain", "bg": "auto", "pad": "7%"}]),
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
          ("Role", "리서치 · 컨셉 · 구조 설계 · 3D · 프로토타입"), ("Output", "워킹 프로토타입 · 특허 · 디자인 등록")],
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
        ("square", {"f": "scene_wait.jpg", "fit": "contain", "bg": "auto"}),
        ("text", "Draw to Print",
         "사용자가 그린 그림은 세 단계를 거쳐 바닥에 출력됩니다. 먼저 화면에 입력된 그림을 20×12의 점 데이터로 바꿉니다. 이 데이터를 "
         "배열 값에 따라 솔레노이드 밸브를 제어하는 신호로 전송합니다. 로봇이 0.5m/s로 직진하는 동안 12개의 밸브가 열리고 닫히면서 "
         "입력한 그림이 바닥에 출력됩니다.",
         "A drawing is printed onto the ground in three steps. The drawing on the screen is first converted into 20×12 dot "
         "data. That data is sent as control signals that open and close the solenoid valves according to the array. "
         "While the robot drives straight at 0.5 m/s, twelve valves open and close and the drawing appears on the ground."),
        ("tri", [{"f": "step_detect2.jpg", "pos": "70% 50%"}, "step_draw.jpg", "step_pixelate.jpg"]),
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
        ("text", "Internal Structure",
         "물을 사용하는 로봇이기 때문에 누수가 전자부에 닿지 않도록 내부를 분리했습니다. 배선과 제어 부품(NI myRIO · LattePanda)은 "
         "전면에, 물탱크와 펌프·분배 호스·솔레노이드 밸브는 방수 패널로 나눈 뒤쪽 공간에 배치했습니다. 하부 LiDAR 센서로 전방의 "
         "사람을 인식하고, 몸통 뒷면 LED로 물 잔량을 확인하며, 전면 하단 커버를 열어 배터리를 교체합니다.",
         "Because the robot uses water, the interior was divided so that leaks cannot reach the electronics. Wiring and "
         "control components (NI myRIO, LattePanda) sit at the front, while the water tank, pump, distribution hoses and "
         "solenoid valves are in a rear compartment behind a waterproof panel. A LiDAR sensor at the bottom detects people "
         "ahead, an LED on the rear shows the remaining water, and the battery is replaced through the lower front cover."),
        ("pair", [{"f": "inner_front.jpg", "r": "natural"}, "inner_rear.jpg"]),
        ("split",
         ("Front", "제어부·배선 (NI myRIO · LattePanda)", "Control and wiring (NI myRIO, LattePanda)."),
         ("Rear", "물탱크·펌프·솔레노이드 밸브", "Water tank, pump and solenoid valves.")),
        ("dark", [
            ("grid", ["build_paint.jpg", "build_chassis.jpg", "build_head.jpg", "build_valves.jpg", "test_print.jpg", "build_assembly.jpg"]),
            ("row", "PROCESS",
             "엔지니어 4명과 디자이너 1명으로 구성된 팀에서 디자인 전체를 담당했습니다. 엔지니어링에서 구현 범위 설정과 코딩, 플랫폼 조립, "
             "전기 배선을 맡는 동안 스케치와 3D 모델링, 렌더링, 3D 프린팅, 프로토타이핑, 영상 제작을 진행했습니다. 외장 3D 프린팅·도장 → "
             "플랫폼·배선 → 헤드 프로토타입 → 방수 설계 → 출력 테스트 → 조립 순으로 만들었습니다.",
             "In a team of four engineers and one designer, the entire design track was handled by the designer. While "
             "engineering covered scoping, coding, platform assembly and wiring, design covered sketching, 3D modelling, "
             "rendering, 3D printing, prototyping and film. The build went from printed and painted shell, platform and wiring, head prototype, "
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
        ("bleed", "nozzle2.jpg", "natural"),
        ("band",),
    ],
)

# =====================================================================
# 대학원(HIDE Lab) 작업 — 사실 기준: 옛 포트폴리오 PDF(240430) 14–21쪽 / 30–35쪽만
PAGES["mobilink"] = dict(
    dir="mobilink", cat_key="product", title="MobiLink", year="2022", category="Mobile Console · Hongik Univ.",  # noqa
    desc="MobiLink — 모빌리티와 주거 공간을 오가는 이동형 모바일 콘솔 (공모전 참여작, IDEA · Spark Finalist)",
    lede="모빌리티와 주거 공간 사이를 자유롭게 오가는 <b>이동형 모바일 콘솔</b>입니다. 모빌리티 안에서는 주행 경험을, "
         "집에서는 스마트 홈 제어를 돕습니다.",
    hero="hero3.jpg",
    meta=[("Term", "2022.09 — 2022.12"), ("Type", "공모전 참여작 · HIDE Lab"), ("Team", "3인 (기여도 60%)"),
          ("Process", "생성형 AI · Midjourney · Vizcom"), ("Award", "IDEA · Spark Finalist")],
    intro=([("idea", "2024.04", "IDEA", "International Design Excellence Awards · Finalist"),
            ("spark", "2023.12", "Spark Design Awards", "Finalist")],
           "모빌리티와 집을 잇는 모바일 리빙 스페이스",
           "A mobile console that links the vehicle and the home",
           "모빌리티가 주거 공간과 연결되는 ‘모바일 리빙 스페이스’ 개념에 따라, 미래 모빌리티 환경에서 새로운 경험을 제공하는 "
           "모바일 콘솔입니다. MobiLink는 모빌리티와 연결된 주거 환경 사이에서 자유롭게 이동할 수 있습니다. 모빌리티 내부에서는 "
           "<b>사용자의 주행 경험 맞춤화 서비스</b>를 제공하고, 스마트 홈과 연결되었을 때는 <b>집안의 환경을 관리하고 제어</b>합니다.",
           "Following the idea of a ‘mobile living space’ where the vehicle connects to the home, MobiLink is a mobile console "
           "for future mobility. It moves freely between the vehicle and the connected home: inside the vehicle it tailors the "
           "ride to the user, and when docked to a smart home it manages and controls the home environment."),
    sections=[
        ("dark", [
            ("img", {"f": "connect2.jpg", "r": "natural"}),
            ("row", "BACKGROUND",
             "미래 모빌리티는 이동수단과 생활 공간의 역할을 동시에 수행하므로, 이러한 라이프 스타일에 맞춘 다용도 기능이 필요합니다. "
             "MobiLink는 모빌리티 내부에서 온도·조명·음향 같은 환경을 손쉽게 조작하게 하고, 모빌리티를 벗어나 주거 환경으로 이동해서도 "
             "역할을 이어 갑니다. 모빌리티와 주거 환경 사이의 경계를 희미하게 하며 통합된 라이프스타일을 지향합니다.",
             "Future vehicles act as both transport and living space, calling for multi-purpose functions. MobiLink makes "
             "temperature, lighting and sound in the vehicle easy to control, then keeps working after it moves into the home, "
             "blurring the line between vehicle and home."),
            ("dots", ["tech_glazing.jpg", "tech_display.jpg", "dock_diagram.jpg"]),
            ("row", "TECHNOLOGY",
             "(주)서연이화의 보유 기술력을 반영해 기획한 모바일 콘솔입니다. PC Glazing Tech, Smart Surfaces, Transparent Garnish를 "
             "활용해 복곡면 투명 소재에 Shy Tech를 적용했고, Transparent Display로 터치 조작과 내부 공간이 보이는 수납·냉장 기능을 "
             "담았습니다. PBV Docking Step을 더해 주행 중인 모빌리티 안에서도 콘솔이 바닥에 도킹되도록 디자인했습니다.",
             "Planned around Seoyon E-Hwa's in-house technologies: PC glazing, smart surfaces and a transparent garnish bring "
             "shy tech to a doubly curved transparent surface, a transparent display adds touch control and a see-through "
             "storage and fridge compartment, and a PBV docking step lets the console dock to the floor inside a moving vehicle."),
            ("img", {"f": "lifestyle.jpg", "r": "natural"}, ' style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;"'),
        ]),
        ("text", "Mobility &amp; Home",
         "주행 중인 모빌리티 안에서는 도킹된 상태로 사용합니다. 완만한 곡선의 전동식 핸들은 팔을 걸쳐 암레스트로 쓰고, 모빌리티 "
         "내부 환경을 제어해 편리한 주행 경험을 제공합니다. 모빌리티가 스마트 홈에 도킹되면 핸들을 밀어 콘솔을 옮기고, IoT로 연결된 "
         "주거 환경을 쉽게 제어합니다.",
         "Inside a moving vehicle the console stays docked; its gently curved powered handle doubles as an armrest while the "
         "console controls the cabin. When the vehicle docks to a smart home, the handle is used to push the console inside, "
         "where it controls the IoT-connected home."),
        ("pair", [{"f": "mobility.jpg", "r": "natural", "cap": "<b>Mobility</b>모빌리티 안에서 도킹된 상태로 사용"},
                  {"f": "home.jpg", "cap": "<b>Home</b>핸들을 밀어 집 안으로 이동"}]),
        ("text", "Pop up-down Handle",
         "버튼을 눌러 전동 핸들을 상하로 조정합니다. 핸들이 올라가 있을 때는 이동 가능한 상태가 되고, 내려가 있을 때는 콘솔이 "
         "움직이지 않도록 바퀴가 고정됩니다.",
         "A button raises or lowers the powered handle. With the handle up the console can be moved; with it down the wheels "
         "lock so the console stays put."),
        ("text", "Multi-Function",
         "모빌리티와 스마트 홈의 실내 환경을 제어하는 컨트롤러와 수납함을 탑재했습니다. 핸드폰을 올려 두면 충전되는 무선 충전, "
         "음료와 간단한 식품을 보관하는 펠티어 냉장고를 갖췄고, 복곡면 투명 가니시에 Shy Tech로 기능 제어 아이콘을 넣었습니다.",
         "A controller for the vehicle and smart-home environment and storage are built in, with wireless charging for a "
         "phone, a Peltier fridge for drinks and snacks, and shy-tech control icons in the doubly curved transparent garnish."),
        ("bleed", {"f": "multi_clean.jpg", "r": "natural"}, "natural"),
        ("text", "Transparent Display",
         "상단 스토리지의 커버는 투명 디스플레이로 만들어, 커버를 열어 L자형으로 고정하면 OTT·동영상을 보기 편한 각도가 됩니다. "
         "좌우 스토리지와 후면 소형 냉장고의 커버는 손잡이 없이 손으로 살짝 누르면 부드럽게 열리는 심리스 커버입니다.",
         "The top storage cover is a transparent display; opened and fixed in an L shape it sits at a comfortable angle for "
         "OTT and video. The side storage and rear mini-fridge use handle-free seamless covers that slide open with a light press."),
        ("pair", [{"f": "storage.jpg", "r": "natural"}, "storage_side.jpg"]),
        ("pair", [{"f": "speaker_panel.jpg", "r": "natural"}, "dock_step.jpg"]),
        ("split",
         ("Smart Surfaces Speaker",
          "사용자가 손으로 표면을 쓸면 터치 센서가 압력을 감지하고, 빛이 스마트 표면에서 나옵니다. 빛이 방출되는 패턴은 맞춤형으로 "
          "만들 수 있습니다.",
          "Sweeping a hand across the surface triggers the touch sensor and light emerges through the smart surface, in a "
          "pattern the user can customise."),
         ("PBV Docking Step",
          "모빌리티 내부 충전 구역의 도킹 스텝이 콘솔 바퀴를 바닥에 고정해 주행 중에도 흔들리지 않게 합니다. 도킹을 해제하면 스텝 "
          "내부 스프링이 복구되며 평평한 면이 되어 틈새에 먼지가 쌓이지 않습니다.",
          "A docking step in the vehicle's charging zone locks the console's wheels so it stays steady while driving. Undocked, "
          "springs return the step to a flat floor so no dust collects in the gaps.")),
        ("square", "render_sq.jpg"),
        ("dark", [
            ("row", "PROCESS",
             "(주)서연이화 주관 정부과제 ‘심리스 환경 제공을 위한 자동차 내장재 보유기술 기반 미래 모빌리티 내장디자인 연구’에서 진행한 "
             "내용을 토대로 미래형 콘솔을 디자인해 공모전에 출품했습니다. 컨셉 기획·유저 시나리오 → Midjourney로 컨셉 이미지 대량 생성·셀렉 → "
             "Vizcom 퀵 렌더링 → 디자인 스케치 · Low-fidelity 프로토타이핑 · 3D 모델링·렌더링 순으로, 생성형 AI를 활용한 디자인 "
             "프로세스를 적용했습니다.",
             "Building on the government project led by Seoyon E-Hwa on future mobility interiors, the console was designed and "
             "entered into competition through a generative-AI process: concept planning and user scenarios, mass concept "
             "images in Midjourney, quick renders in Vizcom, then sketching, low-fidelity prototyping and 3D modelling and rendering."),
            ("row", "OUTCOME",
             "공모전 출품 후 Spark Design Awards Finalist(2023.12), IDEA International Design Excellence Awards Finalist(2024.04)에 "
             "선정됐습니다.",
             "The project was selected as a Spark Design Awards finalist (Dec 2023) and an IDEA International Design Excellence "
             "Awards finalist (Apr 2024)."),
        ]),
        ("band",),
    ],
)

PAGES["flever"] = dict(
    dir="flever", cat_key="product", title="Flever", year="2022", category="Smart Home Screen · Team Project",  # noqa
    desc="Flever — 가족 간 감정 공유 콘텐츠를 중심으로 한 탈부착형 스마트 홈스크린 (대학원 팀 프로젝트)",
    lede="가족 간 감정 공유 콘텐츠를 중심으로 한 <b>탈부착형 스마트 홈스크린</b>입니다. 하나의 오브제로 자리하면서도 "
         "톡톡 튀는 컬러로 존재감을 드러내도록 디자인했습니다.",
    hero="bh_hero.jpg",
    meta=[("Term", "2022.03 — 2022.06"), ("Type", "대학원 팀 프로젝트"), ("Team", "2인 (기여도 50%)"),
          ("Product", "디스플레이 · 포터블 스피커"), ("Output", "UXUI · 3D 모델링")],
    intro=([("UX", "Design Process", "Research → Concept → Design", "Sketch · 3D modeling · UXUI"),
            ("2022", "Color", "2022 인테리어 트렌드 컬러", "오렌지 · 파스텔")],
           "가족의 소통 창구가 되는 스마트 홈스크린",
           "A smart home screen that opens a channel for the family",
           "현대 사회에서 심화되고 있는 가족 해체 현상과 함께, 코로나19로 집에 머무는 시간이 길어진 현상을 바탕으로 진행한 "
           "제품디자인 프로젝트입니다. 즐거움을 주고 접근하기 쉬운 UXUI와, 가족 구성원의 <b>세대별 특성</b>을 고려한 요소로 내부 "
           "콘텐츠를 구성했습니다.",
           "A product design project grounded in the growing breakdown of family ties and in the longer time families spent "
           "at home during COVID-19. The UXUI is playful and easy to approach, and the content reflects the traits of each "
           "generation in the family."),
    sections=[
        ("dark", [
            ("img", {"f": "bh_wall.jpg", "r": "natural"}),
            ("row", "PAINPOINT",
             "가족 안에서 서로 존중하고 함께 대화하려는 노력이 이뤄지고 있다는 사실에, 젊은 층은 부모 세대보다 덜 공감합니다. 부모 세대와 "
             "자녀 세대가 느끼는 가족 간 친밀감에는 차이가 있고, 이 차이를 극복해야 더 깊은 유대감을 기대할 수 있습니다.",
             "Younger family members feel less than their parents that the family is making an effort to respect and talk to "
             "one another. Closing this gap in perceived closeness is the key to a deeper bond."),
            ("dots", ["bh_magnet.jpg", "bh_ui_hello.jpg", {"f": "bh_cable.jpg", "pos": "62% 50%"}]),
            ("row", "SOLUTION",
             "가족 구성원의 세대별 특성을 리서치하고, 그 결과를 바탕으로 전 세대를 잇는 감정 공유 콘텐츠형 스마트 홈스크린 Flever를 "
             "제안했습니다. 출퇴근·등하교로 소통이 없는 가족을 위한 소통 창구가 되어, 삭막한 집 안을 소통이 활발한 공간으로 바꿉니다.",
             "Based on research into each generation's traits, Flever was proposed as an emotion-sharing smart home screen that "
             "connects every generation, a channel for families who barely talk between commutes and school runs."),
            ("img", {"f": "bh_call.jpg", "r": "natural"}, ' style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;"'),
        ]),
        ("scene", {"f": "bh_green.jpg", "r": "natural"}),
        ("text", "Market",
         "다기능이거나 소통 기능이 있을수록 개인을 위한 제품인 경우가 많고, 가족을 위한 제품일수록 단순한 기능만 있는 경우가 많았습니다. "
         "Flever는 가족에 초점을 맞춰, 멀티프로필로 각자의 개성을 표현하고 세대별 특성과 소통 방식의 차이를 활용한 콘텐츠를 담았습니다.",
         "Multi-function and communication devices tend to be personal, while family products tend to be simple. Flever "
         "focuses on the family, with multi-profiles for each member and content built on generational differences in how "
         "people communicate."),
        ("pair", [{"f": "bh_set.jpg", "r": "natural"}, "bh_grey.jpg"]),
        ("text", "UXUI",
         "가족 구성원마다 프로필을 나누는 멀티프로필, 단순한 메뉴 바, 크게 보이는 레이아웃으로 아이부터 어르신까지 쉽게 쓰도록 "
         "구성했습니다.",
         "Multi-profiles for each family member, a simple menu bar and a large, easy-to-read layout make it usable from "
         "children to the elderly."),
        ("bleed", {"f": "bh_ui.jpg", "r": "natural"}, "natural"),
        ("video", "anim_screen.mp4", "anim_screen_poster.jpg"),
        ("text", "Display",
         "디스플레이 뒷면에는 마그네틱이 내장되어 스피커 본체에 부착해 거치합니다. 거실 탁상에서는 스마트 스피커 역할을 하고, 떼어 내 "
         "냉장고나 철제 파티션에 붙이면 스마트 냉장고처럼 가족 간 포스트잇 메모로 쓸 수 있습니다. 스케줄 알림과 음성 메모·그림 메모로 "
         "가족 간 유대감 형성을 돕습니다. 얼굴 인식으로 자동 로그인하고, 전면 카메라로 영상 메시지를 남기거나 터치로 메시지를 남길 수 "
         "있습니다.",
         "A magnet in the back of the display mounts it on the speaker body. On a living-room table it works as a smart "
         "speaker; detached and stuck to a fridge or steel partition it becomes a family note board. Schedule alerts and voice "
         "and drawing memos help the family stay close. Face recognition logs each member in, and messages can be left as "
         "front-camera video or by touch."),
        ("bleed", {"f": "bh_pair.jpg", "r": "natural"}, "natural"),
        ("text", "Detachable",
         "화면과 거치대에 자석이 있어 쉽게 붙이고 뗄 수 있고, 화면 각도를 자유롭게 조절할 수 있습니다.",
         "Magnets in the screen and the base make it easy to attach and detach, and the screen angle adjusts freely."),
        ("video", "anim_hinge.mp4", "anim_hinge_poster.jpg"),
        ("bleed", {"f": "bh_exploded.jpg", "r": "natural"}, "natural"),
        ("text", "Speaker",
         "배터리와 스피커가 내장된 하단 파츠는 디스플레이를 떼어 두었을 때 별도의 포터블 스피커로 쓸 수 있고, USB-C 타입으로 충전합니다. "
         "디스플레이를 부착한 상태에서는 거치대 역할을 하며, 다각도 힌지로 원하는 각도와 높이를 맞출 수 있습니다. 화면을 붙이면 "
         "블루투스로 자동 연결되고 무선으로 충전되며, 타공 외관을 교체해 원하는 컬러와 형태로 바꿀 수 있습니다.",
         "The lower part houses a battery and speaker: with the display removed it works as a portable speaker, charged over "
         "USB-C. With the display attached it serves as the stand, and a multi-angle hinge sets the angle and height. "
         "Attaching the screen pairs it over Bluetooth and charges it wirelessly, and the perforated shell can be swapped "
         "for another colour or shape."),
        ("square", "bh_speaker.jpg"),
        ("pair", [{"f": "bh_hinge_side.jpg", "cap": "<b>Hinge</b>다각도 힌지로 각도·높이 조절"},
                  {"f": "bh_usbc.jpg", "cap": "<b>USB-C</b>포터블 스피커 충전"}]),
        ("dark", [
            ("row", "PROCESS",
             "Research(Problems · Background · User · Target User · Market · Field Research) → Concept(Design concept · "
             "Differentiated Value · Storytelling) → Design(Inspirations · Mood board · Design Strategy · Sketch · 3D modeling · "
             "UXUI · Visualizing) 순으로 진행했습니다.",
             "Research (problems, background, users, target users, market and field research), concept (design concept, "
             "differentiated value, storytelling) and design (inspiration, mood board, strategy, sketching, 3D modelling, UXUI, "
             "visualising)."),
            ("img", {"f": "bh_ideation.jpg", "r": "natural"}),
            ("img", {"f": "bh_sketch.jpg", "r": "natural"}),
        ]),
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
            ("img", {"f": "door_test_crop.jpg", "pos": "50% 0%"}),
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
        ("pair", [{"f": "s_wc_lock.jpg", "r": "natural"}, {"f": "s_seat_layout.jpg", "fit": "contain", "bg": "auto", "pad": "4%"}]),
        ("split",
         ("Wheelchair Lock", "이동형 모빌리티 안에서 휠체어를 고정하는 장치를 제안했습니다.",
          "A device that secures wheelchairs inside the moving vehicle."),
         ("Flexible Seating", "상황에 따라 좌석 배치를 바꾸는 이동형 좌석 배치 시나리오를 제안했습니다.",
          "A movable seating scenario that changes the layout to suit the situation.")),
        ("text", "eHMI",
         "차량 외부에서 이륜차에 승하차를 알리고 보행자에게 횡단을 안내하는 eHMI 시나리오를 제안했습니다.",
         "eHMI scenarios were proposed to alert two-wheelers to boarding passengers and to guide pedestrians across."),
        ("single", "s_ehmi_front.jpg", "<b>eHMI</b>횡단 안내"),
        ("dark", [
            ("row", "PROCESS",
             "애자일 방식으로 아이템을 빠르게 만들고 1:1 목업으로 확인하는 과정을 반복했습니다.",
             "In an agile process, items were built quickly and checked again and again on full-scale mock-ups."),
            ("roles", ["선행 연구", "UX 아이템 발굴", "프로토타이핑", "UX 리서치 및 검증"]),
        ]),
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
           "캐빈 살균, 무드 큐레이터, 감응형 엠비언트 라이트, 원격 시트 베리에이션, 후석 엔터테인먼트, OTT 디스플레이, "
           "클램쉘 테일게이트 등 공간과 웰니스 항목을 발굴하고, 항목별로 <b>3D 애니메이션, 앱 UI, 1:1 폼보드 목업</b>으로 구체화했습니다.",
           "Space and wellness items such as cabin sterilisation, a mood curator, responsive ambient light, remote seat "
           "variation, rear entertainment, OTT displays and a clamshell tailgate were developed and made concrete through "
           "3D animation, app UI and full-scale foam-board mock-ups."),
    sections=[
        ("dark", [
            ("img", {"f": "clamshell_crop.jpg", "r": "natural"}),
            ("row", "SPACE",
             "테일게이트를 펼쳐 앉고 쉬는 공간으로 쓰도록, 그 위에서 쓰는 액세서리를 1:1 폼보드로 만들어 직접 시연했습니다.",
             "To use the opened tailgate as a place to sit and rest, the accessories used on it were built in full-scale "
             "foam board and demonstrated in person."),
            ("dots", ["s_tray.jpg", "s_cupholder.jpg", "s_luggage.jpg"]),
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
        ("single", "clamshell_step.jpg", "<b>Step</b>베드 끝에 수납되는 발걸이"),
        ("text", "Seat Variation",
         "앱으로 1·2·3열 시트를 원격 조절하는 시트 배열 7가지 모드를 제안했습니다.",
         "Seven seat-arrangement modes were proposed, with first- to third-row seats adjusted remotely from an app."),
        ("bleed", "seat_modes.jpg", "natural"),
        ("pair", [{"f": "rear_display_test.jpg", "r": "natural"}, "s_ott_popup.jpg"]),
        ("split",
         ("Rear Entertainment", "후석 보조 모니터를 인치별로 실차에서 비교 검증했습니다.",
          "Rear auxiliary monitors were compared by screen size in a real vehicle."),
         ("OTT Display", "고정형과 팝업형 OTT 디스플레이를 제안했습니다.",
          "Fixed and pop-up OTT displays were proposed.")),
        ("single", "s_ott.jpg", "<b>OTT Display</b>고정형 디스플레이"),
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
            ("dots", ["s_aircon_dash.jpg", "s_aircon_seat.jpg"]),  # 공조(대시보드 · 시트) — 감시 모드 렌더는 대비가 없어 제외
            ("row", "INTERIOR",
             "실내 아이템 4종은 폼보드 PoC로 만들어 1·2열 배치를 재현하고 직접 사용해 보며 검증했습니다. 테이블은 애프터마켓 "
             "테이블 아이디어 3안을 도출해 실차에서 검증했습니다.",
             "Four interior items were built as foam-board PoCs that reproduce the first- and second-row layout and were "
             "verified by using them. For the table, three aftermarket table ideas were developed and tested in a real car."),
            ("img", {"f": "ev_table_ioniq6.jpg", "pos": "50% 55%"}, ' style="margin-top: clamp(48px, 6vw, 88px); margin-bottom: 0;"'),
        ]),
        ("text", "Expandable Center Console",
         "콘솔에서의 1열·2열 수납, 컵홀더, 무선충전, V2L 활용 아이디어를 제안했습니다. 확장 모드는 1열 중심 · 1·2열 공유 · "
         "2열 중심 세 가지이고, 1:1 폼보드 PoC로 검증했습니다.",
         "Ideas for front- and rear-row storage, cup holders, wireless charging and V2L in the console were proposed, with "
         "three extension modes (front-focused, shared, rear-focused) verified on a full-scale foam-board PoC."),
        ("pair", [{"f": "ev_console_poc.jpg", "r": "natural"}, "ev_console_test.jpg"]),
        ("pair", [{"f": "ev_cupholder_poc.jpg", "r": "natural"}, "ev_trunk_poc.jpg"]),
        ("split",
         ("Cup Holder", "센터콘솔 하단 트레이 폴딩 컵홀더 아이템을 제안했습니다.", "A folding cup holder in the tray under the centre console."),
         ("Trunk Luggage Box", "트렁크 러기지박스의 컵홀더와 공간 분할 아이템을 도출하고 검증했습니다.", "Cup-holder and space-dividing items for a trunk luggage box, developed and verified.")),
        ("dark", [
            ("row", "USABILITY TEST",
             "폼보드 PoC는 마크로밀엠브레인의 실사용자 사용성 테스트에 쓰였습니다.",
             "The foam-board PoCs were used in Macromill Embrain's usability tests with real users."),
            ("roles", UX_ROLE),
        ]),
        ("band",),
    ],
)
