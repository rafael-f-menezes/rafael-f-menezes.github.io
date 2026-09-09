// Theme toggle (persists in localStorage) and lazy autoplay for looping clips.
(function () {
  var root = document.documentElement;
  var stored = null;
  try { stored = localStorage.getItem('theme'); } catch (e) {}
  if (stored === 'dark' || stored === 'light') root.setAttribute('data-theme', stored);

  function currentIsDark() {
    var t = root.getAttribute('data-theme');
    if (t) return t === 'dark';
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function label(btn) { btn.textContent = currentIsDark() ? 'Light mode' : 'Dark mode'; }

  document.addEventListener('DOMContentLoaded', function () {
    var btn = document.querySelector('.theme-btn');
    if (btn) {
      label(btn);
      btn.addEventListener('click', function () {
        var next = currentIsDark() ? 'light' : 'dark';
        root.setAttribute('data-theme', next);
        try { localStorage.setItem('theme', next); } catch (e) {}
        label(btn);
      });
    }

    var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var vids = Array.prototype.slice.call(document.querySelectorAll('video[data-src]'));
    function load(v) {
      if (!v.getAttribute('src')) v.setAttribute('src', v.getAttribute('data-src'));
    }
    if (reduce || !('IntersectionObserver' in window)) {
      vids.forEach(function (v) { load(v); v.controls = true; v.removeAttribute('autoplay'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var v = en.target;
        if (en.isIntersecting && en.intersectionRatio >= 0.25) {
          load(v);
          var p = v.play();
          if (p && p.catch) p.catch(function () { v.controls = true; });
        } else if (!v.paused) {
          v.pause();
        }
      });
    }, { threshold: [0, 0.25] });
    vids.forEach(function (v) { io.observe(v); });
  });
})();
