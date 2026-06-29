(function () {
  'use strict';

  var TOTAL   = window.WEB_TOTAL_FRAMES || 91;
  var section = document.getElementById('webFrameSection');
  var canvas  = document.getElementById('webFrameCanvas');
  if (!section || !canvas) return;

  var ctx  = canvas.getContext('2d');
  var BASE = window.WEB_FRAME_PATH || 'static/images/webframes/';
  if (BASE.charAt(0) !== '/' && BASE.indexOf('http') !== 0) BASE = '/' + BASE;

  var images        = new Array(TOTAL);
  var currentFrame  = 0;
  var locked        = false;
  var wheelAccum    = 0;
  var DELTA_PER     = 50;
  var cooldown      = false;
  var lastScrollY   = window.scrollY;
  var sectionDocTop = -1;

  /* ── Smooth animation state ──────────────────────────────── */
  var targetFrame = 0;
  var renderFrame = 0.0;
  var rafId       = null;

  /* ── Word reveal data ────────────────────────────────────── */
  var WF_WORDS = [
    { id: 'wfw0', showAt:  8, hideAt: 44 },
    { id: 'wfw1', showAt: 18, hideAt: 44 },
    { id: 'wfw2', showAt: 28, hideAt: 44 },
    { id: 'wfw3', showAt: 52, hideAt: 999 },
    { id: 'wfw4', showAt: 60, hideAt: 999 },
    { id: 'wfw5', showAt: 68, hideAt: 999 },
    { id: 'wfw6', showAt: 76, hideAt: 999 },
  ];
  var wfWordEls = [];

  function initWords() {
    for (var i = 0; i < WF_WORDS.length; i++)
      wfWordEls.push(document.getElementById(WF_WORDS[i].id));
  }

  function revealWords(fi) {
    for (var i = 0; i < WF_WORDS.length; i++) {
      if (!wfWordEls[i]) continue;
      var on = fi >= WF_WORDS[i].showAt && fi < WF_WORDS[i].hideAt;
      wfWordEls[i].classList.toggle('wf-word-visible', on);
    }
  }

  var lastUnlockDir = 0;

  function getSectionDocTop() {
    if (sectionDocTop < 0)
      sectionDocTop = section.getBoundingClientRect().top + window.scrollY;
    return sectionDocTop;
  }

  /* ── Canvas ─────────────────────────────────────────────── */
  function resizeCanvas() {
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width  = Math.round(window.innerWidth  * dpr);
    canvas.height = Math.round(window.innerHeight * dpr);
    canvas.style.width  = window.innerWidth  + 'px';
    canvas.style.height = window.innerHeight + 'px';
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.scale(dpr, dpr);
    drawFrame(currentFrame);
  }

  function drawFrame(idx) {
    idx          = Math.max(0, Math.min(TOTAL - 1, idx));
    currentFrame = idx;
    var img = images[idx];
    if (!img || !img.complete || !img.naturalWidth) return;
    var cw = window.innerWidth;
    var ch = window.innerHeight;
    var r  = Math.max(cw / img.naturalWidth, ch / img.naturalHeight);
    var dw = img.naturalWidth  * r;
    var dh = img.naturalHeight * r;
    ctx.clearRect(0, 0, cw, ch);
    ctx.drawImage(img, (cw - dw) / 2, (ch - dh) / 2, dw, dh);
  }

  resizeCanvas();
  initWords();
  revealWords(0);

  /* ── rAF smooth animation loop ───────────────────────────── */
  function animate() {
    var diff = targetFrame - renderFrame;
    if (Math.abs(diff) < 0.08) {
      renderFrame = targetFrame;
      var fi = Math.round(renderFrame);
      drawFrame(fi);
      revealWords(fi);
      rafId = null;
      return;
    }
    renderFrame += diff * 0.18;
    var fi = Math.round(renderFrame);
    drawFrame(fi);
    revealWords(fi);
    rafId = requestAnimationFrame(animate);
  }

  function scheduleDraw() {
    if (!rafId) rafId = requestAnimationFrame(animate);
  }

  function cancelAnim() {
    if (rafId) { cancelAnimationFrame(rafId); rafId = null; }
  }

  /* ── Lock ────────────────────────────────────────────────── */
  function lock(startFrame) {
    if (window.gfScrollToTop) return;
    cancelAnim();
    locked       = true;
    wheelAccum   = startFrame * DELTA_PER;
    targetFrame  = startFrame;
    renderFrame  = startFrame;
    currentFrame = startFrame;
    drawFrame(startFrame);
    revealWords(startFrame);
    window.scrollTo(0, getSectionDocTop());
    document.documentElement.style.overflow = 'hidden';
    document.body.style.overflow            = 'hidden';
  }

  /* ── Unlock ──────────────────────────────────────────────── */
  function unlock(goForward) {
    cancelAnim();
    var top       = getSectionDocTop();
    lastUnlockDir = goForward ? 1 : -1;
    locked        = false;
    cooldown      = true;
    revealWords(-1);
    document.documentElement.style.overflow = '';
    document.body.style.overflow            = '';
    /* On mobile scroll-up, jump further above the section so the page
       actually moves and the user doesn't feel stuck at the boundary. */
    var scrollTarget = goForward
      ? top + 1
      : Math.max(0, top - Math.round(window.innerHeight * 0.35));
    window.scrollTo(0, scrollTarget);
    setTimeout(function () {
      cooldown    = false;
      lastScrollY = window.scrollY;
    }, 400);
  }

  /* ── Wheel ───────────────────────────────────────────────── */
  function onWheel(e) {
    if (cooldown) return;

    var delta = e.deltaY;
    if (e.deltaMode === 1) delta *= 40;
    if (e.deltaMode === 2) delta *= window.innerHeight;

    if (locked) {
      e.preventDefault();
      wheelAccum += delta;
      if (wheelAccum < 0) wheelAccum = 0;
      var newFrame = Math.min(Math.round(wheelAccum / DELTA_PER), TOTAL - 1);
      targetFrame = newFrame;
      scheduleDraw();
      if (newFrame >= TOTAL - 1 && delta > 0) { unlock(true);  return; }
      if (wheelAccum <= 0          && delta < 0) { unlock(false); return; }
      return;
    }

    var rect = section.getBoundingClientRect();
    var vh   = window.innerHeight;

    if (delta > 0 && rect.top <= 200 && rect.top >= -200) {
      if (lastUnlockDir === 1) return;
      e.preventDefault();
      lastUnlockDir = 0;
      lock(0);
      return;
    }
    if (delta < 0 && rect.bottom >= vh - 200 && rect.bottom <= vh + 200) {
      if (lastUnlockDir === -1) return;
      e.preventDefault();
      lastUnlockDir = 0;
      lock(TOTAL - 1);
      return;
    }
  }

  document.addEventListener('wheel', onWheel, { passive: false });

  /* ── Touch (mobile) ─────────────────────────────────────── */
  var touchLastY = 0;

  function onTouchStart(e) {
    touchLastY = e.touches[0].clientY;
  }

  function onTouchMove(e) {
    if (window.gfMobileNavOpen) return;
    if (cooldown) return;
    var touchY = e.touches[0].clientY;
    var delta  = touchLastY - touchY; // positive = finger up = scroll down
    touchLastY = touchY;
    if (Math.abs(delta) < 2) return;

    if (locked) {
      e.preventDefault();
      /* Cap backward delta so a single fast swipe can't skip past all frames.
         Forward stays uncapped so advancing feels snappy. */
      var effectiveDelta = delta < 0 ? Math.max(delta, -18) : delta;
      wheelAccum += effectiveDelta * 5;
      if (wheelAccum < 0) wheelAccum = 0;
      var newFrame = Math.min(Math.round(wheelAccum / DELTA_PER), TOTAL - 1);
      targetFrame = newFrame;
      scheduleDraw();
      if (newFrame >= TOTAL - 1 && delta > 0) { unlock(true);  return; }
      if (wheelAccum <= 0        && delta < 0) { unlock(false); return; }
      return;
    }

    var rect = section.getBoundingClientRect();
    var vh   = window.innerHeight;
    if (delta > 0 && rect.top >= -10 && rect.top <= 220) {
      if (lastUnlockDir === 1) return;
      e.preventDefault();
      lastUnlockDir = 0;
      lock(0);
      return;
    }
    if (delta < 0 && rect.bottom >= vh - 220 && rect.bottom <= vh + 10) {
      if (lastUnlockDir === -1) return;
      e.preventDefault();
      lastUnlockDir = 0;
      lock(TOTAL - 1);
      return;
    }
  }

  document.addEventListener('touchstart', onTouchStart, { passive: true });
  document.addEventListener('touchmove',  onTouchMove,  { passive: false });

  /* ── Scroll fallback (keyboard / scrollbar / fast fling) ── */
  window.addEventListener('scroll', function () {
    if (cooldown) { lastScrollY = window.scrollY; return; }
    if (locked)   { return; }

    var scrollY   = window.scrollY;
    var top       = getSectionDocTop();
    var vh        = window.innerHeight;
    var upTrigger = top + section.offsetHeight - vh;

    if (scrollY > lastScrollY && lastScrollY < top && scrollY >= top) {
      if (lastUnlockDir !== 1) {
        lastScrollY   = scrollY;
        lastUnlockDir = 0;
        lock(0);
        return;
      }
      lastScrollY = scrollY;
      return;
    }

    if (scrollY < lastScrollY && lastScrollY > upTrigger && scrollY <= upTrigger) {
      if (lastUnlockDir !== -1) {
        lastScrollY   = scrollY;
        lastUnlockDir = 0;
        lock(TOTAL - 1);
        return;
      }
      lastScrollY = scrollY;
      return;
    }

    lastScrollY = scrollY;
  }, { passive: true });

  /* ── Resize ─────────────────────────────────────────────── */
  var resizeTimer;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(function () {
      sectionDocTop = -1;
      resizeCanvas();
    }, 150);
  }, { passive: true });

  /* ── Public reset (called by TOP button) ────────────────── */
  window.gfShowcaseReset = function () {
    cancelAnim();
    if (locked) {
      locked = false;
      document.documentElement.style.overflow = '';
      document.body.style.overflow            = '';
    }
    lastUnlockDir = 0;
    wheelAccum    = 0;
    targetFrame   = 0;
    renderFrame   = 0;
    currentFrame  = 0;
    drawFrame(0);
    revealWords(0);
  };

  /* ── Preload ─────────────────────────────────────────────── */
  for (var i = 0; i < TOTAL; i++) {
    (function (n) {
      var img = new Image();
      img.src = BASE + 'webframe_' + String(n + 1).padStart(4, '0') + '.webp';
      images[n] = img;
      if (n === 0) img.onload = function () { drawFrame(0); };
    }(i));
  }

}());
