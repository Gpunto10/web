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

  // Menú móvil (hamburguesa junto a "Hablemos")
  var mbtn = document.querySelector('.menu-btn'), hdr = document.querySelector('header.nav');
  function setMenu(open) {
    if (!mbtn) return;
    hdr.classList.toggle('open', open);
    mbtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    mbtn.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  }
  if (mbtn) {
    mbtn.addEventListener('click', function () { setMenu(!hdr.classList.contains('open')); });
    document.querySelectorAll('.mnav a, .nav .btn').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  // Menú: "Cómo trabajo", "Casos" y "Sobre mí" se abren como una vista aparte (solo esa sección, sin poder seguir bajando).
  // El logo, "Hablemos" o el botón de volver devuelven la web completa.
  var SOLO = ['como-trabajo', 'casos', 'sobre-mi'], root = document.documentElement;
  function show(id) {
    var main = document.querySelector('main');
    if (!main) return;
    if (id && SOLO.indexOf(id) > -1) {
      root.classList.add('solo'); root.setAttribute('data-view', id);
      var t = document.getElementById(id);
      main.querySelectorAll(':scope > section').forEach(function (sec) { sec.classList.toggle('is-view', sec === t); });
      t.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
      t.querySelectorAll('.doodle.draw').forEach(function (d) { d.classList.add('drawn'); });
      window.scrollTo({ top: 0, behavior: 'instant' });
      if (!reduce) { t.classList.remove('page-in'); void t.offsetWidth; t.classList.add('page-in'); }
      t.setAttribute('tabindex', '-1'); t.focus({ preventScroll: true });
    } else {
      root.classList.remove('solo'); root.removeAttribute('data-view');
    }
    document.querySelectorAll('.nav ul a').forEach(function (a) {
      a.classList.toggle('active', !!id && a.getAttribute('href').split('#')[1] === id);
    });
  }
  function onHome() { var p = location.pathname; return /\/$|index\.html$/.test(p); }
  document.querySelectorAll('.nav a[href*="#"], .solo-back a').forEach(function (a) {
    a.addEventListener('click', function (e) {
      if (!onHome()) return; // desde una página de caso, se navega normalmente
      var id = a.getAttribute('href').split('#')[1] || '';
      e.preventDefault();
      if (SOLO.indexOf(id) > -1) {
        history.pushState({ view: id }, '', '#' + id);
        show(id);
      } else {
        history.pushState({ view: '' }, '', id && id !== 'inicio' ? '#' + id : location.pathname);
        show('');
        var t = id && id !== 'inicio' ? document.getElementById(id) : null;
        window.scrollTo({ top: t ? t.getBoundingClientRect().top + window.pageYOffset - 64 : 0, behavior: 'instant' });
      }
    });
  });
  window.addEventListener('popstate', function (e) {
    show(e.state && e.state.view ? e.state.view : '');
    if (!(e.state && e.state.view)) { var t = location.hash && document.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }
  });
  // Al llegar con un enlace de vista (index.html#casos desde una página de caso), abrir esa vista
  if (onHome() && SOLO.indexOf(location.hash.slice(1)) > -1 && document.referrer.indexOf(location.host) > -1) {
    history.replaceState({ view: location.hash.slice(1) }, '', location.hash);
    show(location.hash.slice(1));
  }

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
  // Chat de contacto: envía a Web3Forms si hay clave (data-key); si no, abre el correo con el mensaje escrito.
  var chat = document.getElementById('chat');
  if (chat) {
    var fab = chat.querySelector('.chat-fab'), panel = chat.querySelector('.chat-panel'),
        xBtn = chat.querySelector('.chat-x'), form = chat.querySelector('.chat-form'),
        log = chat.querySelector('.chat-log'), err = chat.querySelector('.chat-err');
    var openChat = function (open) {
      chat.classList.toggle('open', open);
      panel.hidden = !open;
      fab.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (open) { var f = form.querySelector('textarea'); if (f && !chat.classList.contains('sent')) setTimeout(function () { f.focus(); }, 60); }
      else fab.focus();
    };
    fab.addEventListener('click', function () { openChat(true); });
    xBtn.addEventListener('click', function () { openChat(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && chat.classList.contains('open')) openChat(false); });
    var bubble = function (text, who) {
      var p = document.createElement('p'); p.className = 'bub ' + who; p.textContent = text;
      log.appendChild(p); log.scrollTop = log.scrollHeight; return p;
    };
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = form.message.value.trim(), name = form.name.value.trim(), mail = form.email.value.trim();
      if (!msg || !name || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(mail)) { err.textContent = 'Necesito tu mensaje, tu nombre y un email válido para poder responderte.'; return; }
      if (form.botcheck.checked) return;
      err.textContent = '';
      var btn = form.querySelector('.chat-send'); btn.disabled = true; btn.textContent = 'Enviando…';
      var thanks = function () {
        chat.classList.add('sent');
        bubble(msg, 'me');
        var t = document.createElement('p'); t.className = 'bub them typing'; t.innerHTML = '<i></i><i></i><i></i>';
        log.appendChild(t); log.scrollTop = log.scrollHeight;
        setTimeout(function () {
          t.remove();
          bubble('¡Gracias por escribirme, ' + name.split(' ')[0] + '! 😊', 'them');
          setTimeout(function () {
            var t2 = document.createElement('p'); t2.className = 'bub them typing'; t2.innerHTML = '<i></i><i></i><i></i>';
            log.appendChild(t2); log.scrollTop = log.scrollHeight;
            setTimeout(function () {
              t2.remove();
              bubble('Leo cada mensaje yo misma, con calma. Te contesto por email muy pronto y vemos cómo te puedo echar una mano.', 'them');
            }, 1300);
          }, 700);
        }, 1200);
      };
      var key = chat.getAttribute('data-key');
      if (key) {
        fetch('https://api.web3forms.com/submit', {
          method: 'POST', headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({ access_key: key, subject: 'Nuevo mensaje desde tu web', from_name: 'Web de Gema Díez', name: name, email: mail, message: msg })
        }).then(function (r) { return r.json(); }).then(function (d) {
          if (d && d.success) thanks(); else throw new Error();
        }).catch(function () {
          btn.disabled = false; btn.textContent = 'Enviar';
          err.textContent = 'No se ha podido enviar. Prueba otra vez o escríbeme a ' + chat.getAttribute('data-mail') + '.';
        });
      } else {
        location.href = 'mailto:' + chat.getAttribute('data-mail') + '?subject=' + encodeURIComponent('Mensaje desde tu web, de ' + name) +
          '&body=' + encodeURIComponent(msg + '\n\n' + name + ' · ' + mail);
        thanks();
      }
    });
  }
})();
