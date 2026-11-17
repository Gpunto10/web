/* Interacciones compartidas: aparición al hacer scroll, barra de lectura y botón de volver arriba */
(function () {
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Aparición escalonada (.reveal → .in). Sin JS o con movimiento reducido, todo se ve desde el principio.
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce && els.length) {
    document.documentElement.classList.add('anim');
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.15, rootMargin: '0px 0px -6% 0px' });
    els.forEach(function (el) { io.observe(el); });
    // trazos a mano: se dibujan al entrar en pantalla
    var dio = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('drawn'); dio.unobserve(e.target); } });
    }, { threshold: 0.6 });
    document.querySelectorAll('.doodle.draw').forEach(function (d) {
      d.querySelectorAll('path').forEach(function (p) { p.setAttribute('pathLength', '1'); });
      dio.observe(d);
    });
  }

  // Menú: en vez de desplazarse, la sección aparece directamente, como si fuera una página aparte
  document.querySelectorAll('.nav a[href*="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var url = new URL(a.href, location.href);
      if (url.pathname !== location.pathname || !url.hash) return;
      var target = document.getElementById(url.hash.slice(1));
      if (!target) return;
      e.preventDefault();
      history.pushState(null, '', url.hash);
      target.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
      target.querySelectorAll('.doodle.draw').forEach(function (d) { d.classList.add('drawn'); });
      window.scrollTo({ top: target.getBoundingClientRect().top + window.pageYOffset - 64, behavior: 'instant' });
      if (!reduce) { target.classList.remove('page-in'); void target.offsetWidth; target.classList.add('page-in'); }
      target.setAttribute('tabindex', '-1'); target.focus({ preventScroll: true });
    });
  });

  // Barra de lectura (páginas de caso) y botón de volver arriba
  var bar = document.getElementById('progress'), top = document.getElementById('totop'), ticking = false;
  function update() {
    var h = document.documentElement, max = h.scrollHeight - h.clientHeight, y = h.scrollTop || document.body.scrollTop;
    if (bar) bar.style.transform = 'scaleX(' + (max > 0 ? y / max : 0) + ')';
    if (top) top.classList.toggle('show', y > 700);
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  update();
  if (top) top.addEventListener('click', function (e) {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
    var t = document.querySelector('.brand'); if (t) t.focus({ preventScroll: true });
  });
})();
