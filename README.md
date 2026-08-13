# Handoff: SU-MIN KO — Product Design Portfolio Website

## Overview
A personal portfolio website for **Su-min Ko**, an industrial / product designer. The site presents her work across product design (kettles, appliances, purifiers) and UX design (mobility, interior UI), an About page with bio and career, a Contact page with a big call-to-action, and six individual case-study pages. Aesthetic direction is **editorial-minimal / industrial-gothic** — warm paper background, near-black ink, oversized Archivo Black display type, and hairline dividers. There is a custom cursor, a subtle magnetic tilt on work cards, scroll-reveal animation, and a live Seoul clock in the footer.

## About the Design Files
The files in this bundle are **design references created in HTML** — static prototypes that show intended look, layout, copy, and behavior. They are **not production code to ship as-is**. The task is to **recreate these designs in the target codebase's existing environment** — React / Next.js, Vue / Nuxt, Astro, SvelteKit, or plain HTML/CSS/JS — using the codebase's established component patterns, routing, and asset pipeline. If no environment exists yet, **Next.js (App Router) + TypeScript + Tailwind CSS** is the recommended default for this design because the layout is content-driven, the type system is central, and image optimization matters (there are several hero JPEGs and one 13 MB looping MP4).

## Fidelity
**High-fidelity (hifi).** All colors, type ramp, spacing scale, hover interactions, cursor behavior, and page compositions are final. Exact values (hex, `clamp()` ranges, font weights) are listed in **Design Tokens** and inline throughout **Screens**. Recreate pixel-perfectly; where the codebase already has a Design System, map tokens onto its equivalents (e.g. Tailwind `theme.extend`).

## Screens / Views

The site has **4 top-level pages** + **6 case-study pages** (linked from Work grid).

### 1. Home (`index.html`)
- **Purpose**: Landing. Introduce the designer with a full-bleed looping product video, then flow through work grids, awards, and a footer CTA.
- **Layout (top → bottom)**:
  1. **Fixed nav** (68 px tall, transparent → glassy blur on scroll; goes light-on-dark over the hero video).
  2. **Hero** — full-viewport (`100vh`) video (`assets/main-video.mp4`) with a top-left "Portfolio 2026 · Industrial Design" label, huge white `PORTFOLIO` wordmark bottom-left (`h-display`, `clamp(64px, 13vw, 220px)`), and a "Su-min Ko — Designer" tag lower-right. Scrim overlay: `linear-gradient(to bottom, rgba(0,0,0,0.35), rgba(0,0,0,0.55))`.
  3. **Marquee strip** — infinite horizontal ticker of specialties (`Industrial Design · UX · Mobility · …`), Archivo Black uppercase, animates left at ~40 s cycle.
  4. **Product Design work grid** — 2-column CSS grid, gap `clamp(24px, 3vw, 48px)`. Each `.work__card` = cover image on top (aspect-ratio `4/3`), then a caption row (title, tags, year).
  5. **UX Design work grid** — same component, second header.
  6. **Awards list** — 6 rows. Each row: award badge PNG (48×48), year, name, one-line note. Hairline dividers between rows.
  7. **Footer** with the "Let's make Something Together." headline (see §9) and 4-column meta grid.
- **Nav items**: `Work` (`work.html`), `About` (`about.html`), `Contact` (`contact.html`). Brand mark = solid black dot + `SU-MIN KO`.

### 2. Work (`work.html`)
- **Purpose**: Full index of case studies. Same two `PRODUCT DESIGN.` and `UX DESIGN.` groups as Home but exhaustive, no hero video.
- **Layout**: Page-title strip at top (`h-1` "SELECTED WORK"), then the two work grids, then footer.

### 3. About (`about.html`)
- **Purpose**: Bio, career timeline, capabilities.
- **Layout**:
  1. Nav.
  2. Two-column intro block: left = large portrait `assets/about-portrait.jpg` (aspect `4/5`, object-fit cover); right = eyebrow "ABOUT", `h-1` name/tagline, body paragraph, capabilities tag list.
  3. **Career timeline** — vertical list, year on the left column (mono), role/company on the right.
  4. **Education / Awards summary**.
  5. Footer.

### 4. Contact (`contact.html`)
- **Purpose**: Simple contact hub.
- **Layout**: Nav, then a large `h-display` "LET'S MAKE SOMETHING TOGETHER." (single flow — not force-broken; sizing controlled by `.footer__big` rules), then a 4-column grid (Contact / Index / Now / CV), then a bottom meta strip (copyright + version). No footer — this page IS the footer treatment.

### 5–12. Case studies (`work/*.html`)
- `threespin.html` — **Threespin Slim (TS450)**: 물걸레 로봇청소기 (2026 iF Gold · Red Dot)
- `wade.html`, `wade2.html` — WADE (2 variants)
- `mobilink.html`, `flever.html`, `inclusive.html`, `seuv.html`, `suv.html`
- Each follows the same template:
  - Nav.
  - Cover image full-bleed (`aspect-ratio: 16/9`, `object-fit: cover`).
  - Project header: eyebrow (category), `h-1` project title, meta row (year · role · client).
  - Body: alternating full-width figures and 2-column text/image blocks.
  - "Next project ->" link at the bottom pointing to the next slug.
  - Footer.

## Interactions & Behavior

Implemented in `js/main.js` (~120 LOC, framework-free — port to hooks / composables as needed):

1. **Custom cursor**
   - Two elements: `.cursor-dot` (6×6 solid ink) tracks pointer 1:1; `.cursor-ring` (36×36 hairline) lerps at `0.18` per frame in `requestAnimationFrame`.
   - Hover targets (`a, button, [data-hover]`): ring grows to `72×72`, fills `rgba(11,11,15,0.85)`, `mix-blend-mode: difference`, dot hides.
   - Dark-section awareness: elements with `data-cursor="light"` switch dot to white + ring border to `rgba(255,255,255,0.5)` while the cursor is over them.
   - **Disabled on touch** via `@media (hover: none)`.

2. **Nav scroll state**
   - `.nav` starts transparent. Over a `data-nav="dark"` region (hero) it gets `.is-dark` → white text.
   - After `scrollY > 40`, gets `.is-scrolled` → `background: rgba(246,245,242,0.78)`, `backdrop-filter: blur(14px) saturate(1.2)`, resets color to ink.

3. **Scroll-reveal**
   - `.reveal` elements start `opacity: 0; transform: translateY(24px)` and transition (`.9s cubic-bezier(.2,.7,.2,1)`) to visible when they cross an IntersectionObserver at `threshold: 0.14, rootMargin: '0px 0px -8% 0px'`.
   - `.delay-1 … .delay-4` add `.08s` stagger increments.
   - `.reveal-lines .line > span` variant: line-by-line mask reveal (`translateY(110%)` → `0`) with cascading `.08s` delays.

4. **Magnetic work-card tilt**
   - `[data-magnetic]` cards update CSS vars `--tx` / `--ty` on `pointermove` (max ±3 px each) and reset on `pointerleave`. Consumed by the card transform.

5. **Marquee**
   - `.marquee__track` contains the ticker line duplicated twice, animated with a CSS keyframe `translateX(0 → -50%)` over ~40 s linear infinite.

6. **Seoul clock**
   - Element with `[data-clock]` updates every 1 s via `toLocaleTimeString('en-GB', { timeZone: 'Asia/Seoul', hour12: false })`. Format: `Seoul · HH:MM:SS`.

7. **Holo hue on hover**
   - `[data-holo]` sets `--holo-x` CSS var to pointer's normalized X% for gradient positioning on large headings.

8. **Smooth scroll**
   - `html { scroll-behavior: smooth; }`.

## State Management
Purely presentational — **no client state, no data fetching, no forms**. Everything is static content. If you re-implement in a framework:
- Case-study pages could be driven by a CMS collection (Contentful / Sanity / MDX). Fields: `slug, title, category, year, role, client, cover, gallery[]`.
- Awards list could be a JSON/YAML file.
- Career timeline (About) same.

## Responsive Behavior

Layout is fluid via `clamp()` — no rigid breakpoints for type. Explicit `@media` breakpoints in `css/main.css`:

| Breakpoint | What changes |
|---|---|
| `≤ 900 px` | Work grid → 1 column. About intro → stacks. |
| `≤ 760 px` | Footer meta grid → 2 columns. Footer bottom meta → vertical stack. |
| `≤ 560 px` | Nav menu tightens (12 px, 14 px gap). Footer big → `clamp(28px, 7.4vw, 44px)`. |
| `≤ 420 px` | Footer grid → 1 column. Footer big → `clamp(26px, 7.6vw, 36px)`. Nav further tightened. |
| `≤ 380 px` | Nav brand text → 11 px, 8 px gap. |
| `≤ 360 px` | Footer big → 24 px flat. |

`--pad-x: clamp(24px, 5vw, 88px)` controls global horizontal padding.

## Design Tokens

### Colors
```
--bg:         #f6f5f2   /* warm paper white — page background */
--bg-alt:     #efece7   /* alt block background */
--ink:        #0b0b0f   /* near-black text/ink */
--ink-2:      #1a1a1f   /* secondary text */
--mute:       #7a7a80   /* muted labels */
--mute-2:     #b8b6b0   /* very muted */
--hair:       rgba(11,11,15,0.12)   /* hairline dividers */
--hair-soft:  rgba(11,11,15,0.06)   /* softer dividers */

/* Holographic accents — used on select hover states */
--holo-a: #6d8bff  (blue)
--holo-b: #b18cff  (purple)
--holo-c: #ff7db8  (rose)
--holo-d: #7be0d3  (mint)
```

### Typography
Font families (loaded from Google Fonts + jsDelivr):
- `--f-display`: `'Archivo Black', 'Archivo', 'Pretendard', system-ui, sans-serif`
- `--f-heavy`:   `'Archivo', 'Pretendard', system-ui, sans-serif`
- `--f-text`:    `'Inter', 'Pretendard', system-ui, sans-serif`
- `--f-kr`:      `'Pretendard', 'Inter', system-ui, sans-serif`
- `--f-mono`:    `ui-monospace, 'SF Mono', Menlo, monospace`

Type scale (all uppercase for display / heavy):

| Class | Font | Weight | Size | Line | Tracking |
|---|---|---|---|---|---|
| `.h-display` | Archivo Black | 900 | `clamp(64px, 13vw, 220px)` | 0.9 | -0.02em |
| `.h-1` | Archivo Black | 900 | `clamp(48px, 8vw, 128px)` | 0.95 | -0.02em |
| `.h-2` | Archivo Black | 900 | `clamp(32px, 4.5vw, 64px)` | 1 | -0.015em |
| `.h-3` | Archivo | 700 | `clamp(22px, 2.2vw, 32px)` | 1.15 | -0.01em |
| `.body-lg` | Inter | 400 | `clamp(16px, 1.15vw, 19px)` | 1.55 | 0 |
| `.body` | Inter | 400 | 15 px | 1.6 | 0 |
| `.eyebrow` | Inter | 500 | 11 px | — | 0.18em (uppercase) |
| `.mono` | SF Mono | 400 | 11 px | — | 0.04em (uppercase) |
| Base body | Inter | 400 | 15 px | 1.55 | 0 |
| `.footer__big` | Archivo Black | 900 | `clamp(28px, 5.2vw, 76px)` | 1.02 | -0.02em, `max-width: 18ch` |

### Spacing / Rhythm
- Horizontal page padding: `--pad-x: clamp(24px, 5vw, 88px)`
- Nav height: `--nav-h: 68px`
- Section vertical rhythm: `padding-block: clamp(80px, 10vw, 160px)` (typical)
- Grid gap: `clamp(24px, 3vw, 48px)`
- Footer top spacing: `padding-top: clamp(60px, 8vw, 120px)`, `margin-top: clamp(100px, 12vw, 180px)`

### Borders / Radius / Shadow
- No border-radius on cards or images — everything is rectilinear (industrial aesthetic).
- Hairline dividers: `1px solid var(--hair)` (which is `rgba(11,11,15,0.12)`).
- **No drop shadows** — depth is signaled by contrast and hairlines only.

### Motion
- Default easing: `cubic-bezier(.2, .7, .2, 1)` (custom "soft-out")
- Reveal duration: `.9s` (elements) / `1.1s` (line masks)
- Nav color transition: `.3s ease`
- Link-arrow gap transition: `.3s ease` (`10px → 18px` on hover)
- Cursor ring lerp: `0.18` per frame

## Assets

All under `assets/` in this handoff.

| File | Purpose | Notes |
|---|---|---|
| `assets/main-video.mp4` | Home hero looping video (13 MB) | `<video autoplay muted loop playsinline>`. Consider serving a lower-bitrate WebM alongside in production. |
| `assets/hero-image.jpg` | Fallback / secondary hero still | ~790 KB |
| `assets/about-portrait.jpg` | About page portrait | ~1 MB, 4:5 aspect |
| `assets/works/*_cover.jpg` | Work grid cover images | ~40–260 KB each |
| `assets/works/threespin_cover.jpg`, `threespin_02.jpg` | Threespin TS450 hero + in-use scene | |
| `assets/works/wade_02.jpg`, `wade_03.jpg`, `mobilink_02.jpg`, `mobilink_03.jpg`, `pbv_02.jpg` | Case-study body imagery | |
| `assets/works/ux_inclusive.jpg`, `ux_seuv.jpg`, `ux_suv.jpg` | UX case covers | |
| `assets/awards/*.png` | Award badge marks (6): `hci, idea, if, if-gold, reddot, spark` | 19–150 KB each |
| **NOT INCLUDED** — `assets/portfolio.pdf` | Full 40 MB downloadable resume/portfolio | Too large for this bundle. Original path in source project: `assets/portfolio.pdf`. The "PDF · 40 MB" link in the Contact footer expects this file. |

Fonts are loaded from CDN:
- Google Fonts: `Archivo` (400–900), `Archivo Black`, `Inter` (300–700)
- jsDelivr: Pretendard (`https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.min.css`)

For production, self-host these to remove the render-blocking CDN request and comply with GDPR / privacy policies.

## Content / Copy

All copy is final. Notable strings:
- Nav brand: `● SU-MIN KO`
- Home hero: `Portfolio · 2026.04 — Industrial Design` (top-left), `PORTFOLIO` (main), `Su-min Ko — Designer` (bottom-right)
- Marquee (repeats): `Industrial Design · UX · Mobility · Appliance · Interior UI · CMF · Prototyping`
- Section titles: `PRODUCT DESIGN.` and `UX DESIGN.`
- Awards list: 6 entries with years `2026.04` (iF Gold), `2026.04` (Red Dot), `2024.04` (IDEA × 2 — MobiLink, ARO), `2024.01` (HCI Korea — WADE), `2023.12` (Spark — MobiLink/FODI)
- Footer big text: `Let's make Something Together.` (`Together.` is underlined; the whole line is a link to `contact.html`)
- Contact meta grid columns: `Contact` (email + phone), `Index` (Work/About/Contact), `Now` (`Available for freelance`, live Seoul clock), `CV` (`View resume`, `PDF · 40 MB`)
- Copyright: `© 2026 SU-MIN KO. ALL RIGHTS RESERVED.`
- Version stamp: `PORTFOLIO V. 2026.04 — INDUSTRIAL DESIGN`

## Accessibility Notes
- Custom cursor hides on touch devices (`@media (hover: none)`).
- Nav uses `aria-current="page"` on the active link.
- Hero title carries `aria-label="Portfolio"` (visible text is decorative letter-by-letter).
- All images have descriptive `alt` text (award marks name the award; work covers name the project).
- Color contrast: ink `#0b0b0f` on bg `#f6f5f2` = **~17:1** (AAA). Mute `#7a7a80` on bg = **~4.7:1** (AA for body).
- Respect `prefers-reduced-motion` — **not currently implemented in `main.js`**. Add a guard around the reveal animations, marquee, and cursor-ring RAF when re-implementing.

## Files

Copied into this handoff:

```
design_handoff_sumin_portfolio/
├── README.md                    ← you are here
├── index.html                   ← Home
├── work.html                    ← Work index
├── about.html                   ← About
├── contact.html                 ← Contact
├── css/
│   ├── main.css                 ← global tokens, nav, footer, type, cursor, grids
│   └── work.css                 ← case-study page styles
├── js/
│   └── main.js                  ← cursor, nav scroll, reveal, tilt, clock
├── work/
│   ├── threespin.html
│   ├── wade.html
│   ├── wade2.html
│   ├── mobilink.html
│   ├── flever.html
│   ├── inclusive.html
│   ├── seuv.html
│   └── suv.html
└── assets/
    ├── main-video.mp4
    ├── hero-image.jpg
    ├── about-portrait.jpg
    ├── awards/  (hci, idea, if, if-gold, reddot, spark .png)
    └── works/   (12 project images)
```

## Suggested Implementation Steps (Next.js reference)

1. `npx create-next-app@latest sumin-portfolio --typescript --tailwind --app`
2. Copy `assets/` into `public/`.
3. Move fonts to `next/font/google` (`Archivo`, `Archivo_Black`, `Inter`) — self-hosts them and eliminates layout shift.
4. Port CSS custom properties into `tailwind.config.ts` under `theme.extend.colors` / `fontFamily` / `spacing`; keep `clamp()` sizes as arbitrary values (`text-[clamp(48px,8vw,128px)]`) or as `fontSize` scale entries.
5. Create shared components: `<Nav>`, `<Footer>`, `<WorkCard>`, `<AwardRow>`, `<Cursor>`, `<Marquee>`, `<Reveal>`.
6. Build routes: `app/page.tsx` (Home), `app/work/page.tsx`, `app/about/page.tsx`, `app/contact/page.tsx`, `app/work/[slug]/page.tsx` (case studies from MDX or a data file).
7. Port `js/main.js` behaviors to hooks: `useCursor`, `useNavScroll`, `useReveal` (IntersectionObserver), `useMagnetic`, `useSeoulClock`. Guard each with `useReducedMotion()` from Framer Motion or a `prefers-reduced-motion` MediaQuery.
8. Compress the hero video: `ffmpeg -i main-video.mp4 -vcodec libvpx-vp9 -crf 34 -b:v 0 main-video.webm` and add both sources to `<video>`.
9. Add `next/image` for all still images with `sizes` hints.
