/* SUMIN KO — Portfolio interactions */

(() => {
  /* ---------- Custom cursor ---------- */
  const dot = document.createElement('div');
  const ring = document.createElement('div');
  dot.className = 'cursor-dot';
  ring.className = 'cursor-ring';
  document.body.append(ring, dot);

  let mx = window.innerWidth / 2, my = window.innerHeight / 2;
  let rx = mx, ry = my;
  window.addEventListener('pointermove', (e) => {
    if (e.pointerType === 'mouse') document.documentElement.classList.add('cursor-on');
    mx = e.clientX; my = e.clientY;
    dot.style.transform = `translate(${mx}px, ${my}px) translate(-50%,-50%)`;
  });
  const raf = () => {
    rx += (mx - rx) * 0.18;
    ry += (my - ry) * 0.18;
    ring.style.transform = `translate(${rx}px, ${ry}px) translate(-50%,-50%)`;
    requestAnimationFrame(raf);
  };
  raf();

  // hover targets
  const hoverSel = 'a, button, [data-hover]';
  document.addEventListener('pointerover', (e) => {
    if (e.target.closest(hoverSel)) ring.classList.add('is-hover');
  });
  document.addEventListener('pointerout', (e) => {
    if (e.target.closest(hoverSel)) ring.classList.remove('is-hover');
  });

  // dark-section awareness (elements with data-cursor="light")
  const setCursorMode = (isDark) => {
    dot.classList.toggle('on-dark', isDark);
    ring.classList.toggle('on-dark', isDark);
  };
  const darkZones = document.querySelectorAll('[data-cursor="light"]');
  if (darkZones.length) {
    const check = () => {
      let dark = false;
      const y = my;
      darkZones.forEach(z => {
        const r = z.getBoundingClientRect();
        if (r.top < y && r.bottom > y) dark = true;
      });
      setCursorMode(dark);
    };
    window.addEventListener('pointermove', check);
    window.addEventListener('scroll', check, { passive: true });
  }

  /* ---------- Nav scroll state ---------- */
  const nav = document.querySelector('.nav');
  if (nav) {
    const wasDark = nav.classList.contains('is-dark');
    if (wasDark) nav.classList.add('was-dark');
    const onScroll = () => {
      nav.classList.toggle('is-scrolled', window.scrollY > 40);
      // dark nav zone check (hero) → element data-nav="dark"
      const darkTop = document.querySelector('[data-nav="dark"]');
      if (darkTop) {
        const r = darkTop.getBoundingClientRect();
        const inDark = r.top <= 30 && r.bottom > 30;
        nav.classList.toggle('is-dark', inDark && !nav.classList.contains('is-scrolled'));
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Reveal on scroll ---------- */
  // 모션 줄이기 설정이거나 ?static (전체 페이지 캡처용)이면 애니메이션 없이 바로 표시
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('video[autoplay]').forEach(v => {
      v.removeAttribute('autoplay'); v.pause(); v.preload = 'none';
      try { v.currentTime = 0; } catch (e) {}
    });
  }
  if (matchMedia('(prefers-reduced-motion: reduce)').matches || /[?&]static\b/.test(location.search)) {
    document.documentElement.classList.add('no-motion');
    document.querySelectorAll('.reveal, .reveal-lines').forEach(el => el.classList.add('is-in'));
  }
  const io = new IntersectionObserver((entries) => {
    entries.forEach(en => {
      if (en.isIntersecting) {
        en.target.classList.add('is-in');
        io.unobserve(en.target);
      }
    });
  }, { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });
  document.querySelectorAll('.reveal, .reveal-lines').forEach(el => io.observe(el));

  /* ---------- Marquee holo hue on hover (large headings) ---------- */
  document.querySelectorAll('[data-holo]').forEach(el => {
    el.addEventListener('pointermove', (e) => {
      const r = el.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width;
      el.style.setProperty('--holo-x', `${(x * 100).toFixed(1)}%`);
    });
  });

  /* ---------- Time in Seoul ticker ---------- */
  const ticker = document.querySelector('[data-clock]');
  if (ticker) {
    const tick = () => {
      const d = new Date();
      const t = d.toLocaleTimeString('en-GB', { timeZone: 'Asia/Seoul', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false });
      ticker.textContent = `Seoul · ${t}`;
    };
    tick(); setInterval(tick, 1000);
  }

  /* ---------- Detail pages: tap an image to view it full size ----------
     주석이 들어간 보고서 보드(Before/After, UX Strategy 등)는 휴대폰에서 글자가 작아 읽히지 않으므로
     상세 페이지 본문 이미지를 누르면 화면 전체로 크게 보여 준다(핀치 줌은 브라우저 기본). */
  if (document.body.dataset.page === 'work-detail') {
    const imgs = document.querySelectorAll('main img:not([src*="/awards/"])');
    let box = null;
    const close = () => { if (box) { box.remove(); box = null; document.documentElement.style.overflow = ''; } };
    imgs.forEach(img => {
      img.style.cursor = 'zoom-in';
      img.addEventListener('click', () => {
        box = document.createElement('div');
        box.className = 'lb';
        box.setAttribute('role', 'dialog');
        box.setAttribute('aria-label', img.alt || 'Image');
        const big = document.createElement('img');
        big.src = img.currentSrc || img.src; big.alt = img.alt || '';
        const x = document.createElement('button');
        x.className = 'lb__close'; x.type = 'button'; x.setAttribute('aria-label', 'Close'); x.textContent = '×';
        if (img.naturalWidth > img.naturalHeight * 1.3) box.classList.add('lb--wide');
        box.append(big, x);
        box.addEventListener('click', (e) => { if (e.target !== big) close(); });
        document.body.append(box);
        document.documentElement.style.overflow = 'hidden';
        x.focus();
      });
    });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
  }

  /* ---------- Work card magnetic tilt (subtle) ---------- */
  document.querySelectorAll('[data-magnetic]').forEach(card => {
    card.addEventListener('pointermove', (e) => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width - 0.5;
      const py = (e.clientY - r.top) / r.height - 0.5;
      card.style.setProperty('--tx', `${px * 6}px`);
      card.style.setProperty('--ty', `${py * 6}px`);
    });
    card.addEventListener('pointerleave', () => {
      card.style.setProperty('--tx', `0px`);
      card.style.setProperty('--ty', `0px`);
    });
  });
})();
