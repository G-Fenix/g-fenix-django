(function () {
  'use strict';

  /* Prevent browser from restoring scroll position on reload/language change */
  if ('scrollRestoration' in history) {
    history.scrollRestoration = 'manual';
  }

  var TOTAL   = window.TOTAL_FRAMES || 91;
  var section = document.getElementById('frameSequenceSection');
  var canvas  = document.getElementById('frameCanvas');
  if (!section || !canvas) return;

  var ctx  = canvas.getContext('2d');
  var BASE = window.FRAME_PATH || 'static/images/frames/';
  if (BASE.charAt(0) !== '/' && BASE.indexOf('http') !== 0) BASE = '/' + BASE;

  var siteMain = document.querySelector('.site-main');
  if (siteMain) siteMain.style.paddingTop = '0';

  /* ── State ─────────────────────────────────────────────────── */
  var images       = new Array(TOTAL);
  var currentFrame = 0;
  var locked       = true;
  var wheelAccum   = 0;
  var DELTA_PER    = 50;   /* ~50px of wheel delta per frame */

  /* ── Word reveal: frame thresholds for each word ────────────
     5 words across 91 frames — words appear at ~12, 26, 40, 55, 70
  ─────────────────────────────────────────────────────────── */
  var wordThresholds = [12, 26, 40, 55, 70];
  var wordEls = [];

  function initWords() {
    var spans = document.querySelectorAll('#tsHeadline .ts-word');
    for (var i = 0; i < spans.length; i++) wordEls.push(spans[i]);
  }

  function revealWordsByFrame(fi) {
    for (var i = 0; i < wordEls.length; i++) {
      if (fi >= wordThresholds[i]) {
        wordEls[i].classList.add('ts-word-visible');
      } else {
        wordEls[i].classList.remove('ts-word-visible');
      }
    }
  }

  /* ── Scroll lock ────────────────────────────────────────────── */
  function lockPage() {
    locked = true;
    document.documentElement.style.overflow = 'hidden';
    document.body.style.overflow            = 'hidden';
  }

  function unlockPage() {
    locked = false;
    document.documentElement.style.overflow = '';
    document.body.style.overflow            = '';
  }

  /* Reset scroll and lock — called on every page show */
  function initLock() {
    document.documentElement.scrollTop = 0;
    document.body.scrollTop            = 0;
    window.scrollTo(0, 0);
    locked     = true;
    wheelAccum = 0;
    revealWordsByFrame(0);
    lockPage();
  }

  /* pageshow fires on initial load AND after BFCache/language-change redirect */
  window.addEventListener('pageshow', function () {
    initLock();
  });

  initLock();

  /* ── Canvas ─────────────────────────────────────────────────── */
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

  /* ── Wheel ──────────────────────────────────────────────────── */
  function onWheel(e) {
    var delta = e.deltaY;
    if (e.deltaMode === 1) delta *= 40;
    if (e.deltaMode === 2) delta *= window.innerHeight;

    if (locked) {
      e.preventDefault();

      wheelAccum = Math.max(0, wheelAccum + delta);
      var newFrame = Math.min(Math.round(wheelAccum / DELTA_PER), TOTAL - 1);
      drawFrame(newFrame);
      revealWordsByFrame(newFrame);

      if (newFrame >= TOTAL - 1) {
        unlockPage();
      }

    } else {
      if (window.scrollY === 0 && delta < 0) {
        e.preventDefault();
        lockPage();
        wheelAccum = currentFrame * DELTA_PER;
      }
    }
  }

  document.addEventListener('wheel', onWheel, { passive: false });

  /* ── Touch (mobile) ─────────────────────────────────────────── */
  var touchLastY = 0;

  function onTouchStart(e) {
    touchLastY = e.touches[0].clientY;
  }

  function onTouchMove(e) {
    var touchY = e.touches[0].clientY;
    var delta  = touchLastY - touchY; // positive = finger up = forward
    touchLastY = touchY;
    if (Math.abs(delta) < 2) return;

    if (locked) {
      e.preventDefault();
      wheelAccum = Math.max(0, wheelAccum + delta * 5);
      var newFrame = Math.min(Math.round(wheelAccum / DELTA_PER), TOTAL - 1);
      drawFrame(newFrame);
      revealWordsByFrame(newFrame);
      if (newFrame >= TOTAL - 1) unlockPage();
    } else {
      if (window.scrollY === 0 && delta < 0) {
        e.preventDefault();
        lockPage();
        wheelAccum = currentFrame * DELTA_PER;
      }
    }
  }

  document.addEventListener('touchstart', onTouchStart, { passive: true });
  document.addEventListener('touchmove',  onTouchMove,  { passive: false });

  /* ── Resize ─────────────────────────────────────────────────── */
  var resizeTimer;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(resizeCanvas, 150);
  }, { passive: true });

  /* ── Preload ─────────────────────────────────────────────────── */
  for (var i = 0; i < TOTAL; i++) {
    (function (n) {
      var img = new Image();
      img.src = BASE + 'frame_' + String(n + 1).padStart(4, '0') + '.webp';
      images[n] = img;
      if (n === 0) img.onload = function () { drawFrame(0); };
    }(i));
  }

}());
