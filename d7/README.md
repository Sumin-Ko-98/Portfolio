# SU-MIN KO — Portfolio 2026

산업 / 제품 디자이너 **고수민 (Su-min Ko)** 의 개인 포트폴리오 웹사이트입니다.
정적 HTML + CSS + JavaScript 로 제작되어 **GitHub Pages** 에서 별도 빌드 과정 없이 바로 호스팅됩니다.

**Live**: `https://sumin-ko-98.github.io/Portfolio/` *(GitHub Pages 활성화 후)*

---

## 📁 구조

```
.
├── index.html              # 홈 (히어로 비디오 + 작업 그리드 + 어워드)
├── work.html               # 전체 작업 인덱스
├── about.html              # 소개 · 커리어
├── contact.html            # 연락처
│
├── css/
│   ├── main.css            # 글로벌 토큰, 내비, 푸터, 타이포, 커서, 그리드
│   └── work.css            # 케이스 스터디 페이지 스타일
│
├── js/
│   └── main.js             # 커스텀 커서, 내비 스크롤, 리빌, 마그네틱, 시계
│
├── work/                   # 케이스 스터디 페이지
│   ├── threespin.html      # Threespin Slim (TS450) — 물걸레 로봇청소기
│   ├── wade.html           # WADE
│   ├── wade2.html
│   ├── mobilink.html       # MobiLink
│   ├── flever.html         # Flever
│   ├── inclusive.html      # Inclusive UX
│   ├── seuv.html           # sEUV
│   └── suv.html            # SUV UX
│
├── assets/
│   ├── main-video.mp4      # 홈 히어로 루프 (약 13 MB — Git LFS 권장)
│   ├── hero-image.jpg
│   ├── about-portrait.jpg
│   ├── awards/             # 어워드 뱃지 6종
│   └── works/              # 케이스 스터디 이미지
│
├── .nojekyll               # GitHub Pages Jekyll 비활성화
├── .gitignore
└── README.md
```

---

## 🚀 GitHub Pages 배포 방법

### 방법 1 · 기존 레포에 push

1. 이 폴더의 모든 파일을 [github.com/Sumin-Ko-98/Portfolio](https://github.com/Sumin-Ko-98/Portfolio) 의 **main** 브랜치 루트에 올립니다.
   ```bash
   git clone https://github.com/Sumin-Ko-98/Portfolio.git
   cd Portfolio
   # 이 폴더의 내용을 여기로 복사
   git add .
   git commit -m "Deploy portfolio site"
   git push origin main
   ```
2. 레포 → **Settings → Pages** 이동.
3. **Source** 를 `Deploy from a branch` 로 두고, **Branch** 를 `main` / `/(root)` 로 선택 후 Save.
4. 몇 분 뒤 `https://sumin-ko-98.github.io/Portfolio/` 에서 확인 가능합니다.

### 방법 2 · 새 레포로 시작

1. GitHub 에서 새 레포 생성 (예: `portfolio`).
2. `git init` → 이 폴더 내용 커밋 → `git push`.
3. Settings → Pages 에서 위와 동일하게 설정.

### ⚠️ 주의 · 히어로 비디오 (`main-video.mp4`, ~13 MB)

GitHub 파일 단일 용량 제한은 100 MB, 권장은 50 MB 이하이므로 그대로 push 해도 문제는 없습니다.
다만 **저장소가 무거워지는 것을 피하려면** Git LFS 사용을 권장합니다:

```bash
git lfs install
git lfs track "*.mp4"
git add .gitattributes
git add assets/main-video.mp4
git commit -m "Track video with LFS"
git push
```

프로덕션에서 로딩 최적화를 원한다면 WebM 트랜스코딩 후 병기:

```bash
ffmpeg -i assets/main-video.mp4 -vcodec libvpx-vp9 -crf 34 -b:v 0 assets/main-video.webm
```

그리고 `index.html` 의 `<video>` 태그에 `<source src="assets/main-video.webm" type="video/webm">` 를 추가합니다.

---

## 🖥️ 로컬에서 미리보기

빌드 도구 없이 정적 파일만 서빙하면 됩니다:

```bash
# Python 3
python3 -m http.server 8000

# 또는 Node
npx serve .
```

브라우저에서 `http://localhost:8000` 접속.

> `file://` 로 직접 열면 일부 브라우저에서 fetch/이미지 CORS 문제가 생길 수 있어 로컬 서버 사용을 권장합니다.

---

## 🎨 디자인 시스템 요약

- **컬러**: 따뜻한 종이색 배경 `#f6f5f2`, 잉크 블랙 `#0b0b0f`, 하이라이트 hairline `rgba(11,11,15,0.12)`
- **타이포**: Archivo Black (display), Archivo (heavy), Inter (본문), Pretendard (한글), SF Mono (라벨)
  — Google Fonts + jsDelivr CDN 로드
- **간격**: 가로 여백 `clamp(24px, 5vw, 88px)`, 섹션 세로 `clamp(80px, 10vw, 160px)`
- **모션**: 스크롤 리빌 · 커스텀 커서 · 카드 마그네틱 틸트 · 마퀴 · Seoul 실시간 시계
- **반응형**: 순수 `clamp()` 기반, 900 / 760 / 560 / 420 / 380 / 360 px 브레이크포인트

세부 토큰과 재구현 가이드는 프로젝트 루트의 원본 README (16 KB, 상세 핸드오프 문서) 를 참고하세요.

---

## 📄 라이선스 / 저작권

© 2026 SU-MIN KO. All rights reserved.
포트폴리오 내 이미지 · 프로젝트 저작권은 각 클라이언트 및 저자에게 있습니다.

---

## 📮 Contact

- **Email**: ssom98@naver.com
- **Phone**: +82 10 5660 5032
