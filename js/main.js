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
