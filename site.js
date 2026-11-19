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
  var SOLO = ['como-trabajo', 'casos', 'sobre-mi'], root = document.documentElement, pushed = false;
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
        history.pushState({ view: id }, '', '#' + id); pushed = true;
        show(id);
      } else {
        history.pushState({ view: '' }, '', id && id !== 'inicio' ? '#' + id : location.pathname);
        show('');
        var t = id && id !== 'inicio' ? document.getElementById(id) : null;
        window.scrollTo({ top: t ? t.getBoundingClientRect().top + window.pageYOffset - 64 : 0, behavior: 'instant' });
      }
    });
  });
  // «← Atrás» en las vistas de sección de la home: vuelve a lo anterior (otra vista o la página de la que vienes); si no hay, a la web completa
  var hb = document.getElementById('home-back');
  if (hb) hb.addEventListener('click', function (e) {
    e.preventDefault();
    var ref = document.referrer && document.referrer.indexOf(location.origin) === 0;
    if (history.state && history.state.view && (pushed || ref) && history.length > 1) { history.back(); return; }
    history.pushState({ view: '' }, '', location.pathname); show(''); window.scrollTo({ top: 0, behavior: 'instant' });
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
      // Errores por campo: se marca cada campo que falla, el mensaje dice cuál y el foco va al primero
      var bad = [];
      if (!msg) bad.push([form.message, 'tu mensaje']);
      if (!name) bad.push([form.name, 'tu nombre']);
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(mail)) bad.push([form.email, mail ? 'un email válido (revisa que tenga @ y dominio)' : 'tu email']);
      [form.message, form.name, form.email].forEach(function (f) { f.removeAttribute('aria-invalid'); });
      if (bad.length) {
        bad.forEach(function (b) { b[0].setAttribute('aria-invalid', 'true'); });
        var parts = bad.map(function (b) { return b[1]; });
        err.textContent = 'Para responderte me falta ' + (parts.length > 1 ? parts.slice(0, -1).join(', ') + ' y ' + parts[parts.length - 1] : parts[0]) + '.';
        bad[0][0].focus();
        return;
      }
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

/* Botón de atrás: vuelve a la página anterior de la web; si se llegó de fuera o no hay historial, va a la home */
(function(){
  var b=document.getElementById('nav-back'); if(!b) return;
  b.addEventListener('click',function(e){
    var r=document.referrer;
    if(r && r.indexOf(location.origin)===0 && history.length>1){ e.preventDefault(); history.back(); }
  });
})();

// Laboratorio · Hecho con IA (19 nov 2026). Recorrido que avanza solo cada 2,8 s, con control del usuario:
// botón de pausa/reanudar, pestañas accesibles (flechas, Inicio, Fin) y respeto a «reducir movimiento».
(function () {
  var lab = document.getElementById('lab');
  if (!lab) return;
  var T = 2800;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var pills = Array.prototype.slice.call(lab.querySelectorAll('.lab-pill'));
  var panels = lab.querySelectorAll('.ls-panel');
  var notes = lab.querySelectorAll('.lab-note[data-done]');
  var row = lab.querySelector('.lab-steps');
  var play = document.getElementById('lab-play');
  var playT = play && play.querySelector('.lab-play-t');
  var cur = 0, timer = null, visible = false, hover = false;
  var userPaused = reduce; // con movimiento reducido empieza parado; se puede activar a mano
  lab.style.setProperty('--lab-t', T + 'ms');
  function show(i) {
    cur = i;
    lab.setAttribute('data-step', i);
    pills.forEach(function (p, k) {
      var on = k === i;
      p.classList.toggle('on', on);
      p.setAttribute('aria-selected', on ? 'true' : 'false');
      p.tabIndex = on ? 0 : -1;
      var bar = p.querySelector('.lp-bar');
      if (on && bar) { bar.style.animation = 'none'; void bar.offsetWidth; bar.style.animation = ''; }
    });
    panels.forEach(function (p, k) { p.classList.toggle('on', k === i); p.hidden = false; p.setAttribute('aria-hidden', k === i ? 'false' : 'true'); });
    notes.forEach(function (n) { n.classList.toggle('done', i >= +n.getAttribute('data-done')); });
    var a = pills[i];
    if (row && row.scrollWidth > row.clientWidth) {
      row.scrollTo({ left: a.offsetLeft - (row.clientWidth - a.offsetWidth) / 2, behavior: reduce ? 'auto' : 'smooth' });
    }
  }
  function syncBtn() {
    if (!play) return;
    play.setAttribute('aria-pressed', userPaused ? 'true' : 'false');
    play.setAttribute('aria-label', userPaused ? 'Reanudar el recorrido automático' : 'Pausar el recorrido automático');
    play.classList.toggle('is-paused', userPaused);
    if (playT) playT.textContent = userPaused ? 'Reanudar' : 'Pausar';
  }
  function run() {
    clearTimeout(timer); timer = null;
    var go = !userPaused && visible && !hover && !document.hidden;
    lab.classList.toggle('playing', go);
    lab.classList.toggle('paused', !go);
    lab.classList.toggle('user-paused', userPaused);
    syncBtn();
    if (go) timer = setTimeout(function () { show((cur + 1) % pills.length); run(); }, T);
  }
  function pick(k, focus) { userPaused = true; show(k); if (focus) pills[k].focus(); run(); }
  pills.forEach(function (p, k) {
    p.addEventListener('click', function () { pick(k, false); });
    p.addEventListener('keydown', function (e) {
      var n = pills.length, t = null;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') t = (k + 1) % n;
      else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') t = (k - 1 + n) % n;
      else if (e.key === 'Home') t = 0;
      else if (e.key === 'End') t = n - 1;
      if (t !== null) { e.preventDefault(); pick(t, true); }
    });
  });
  // Flechas también con el foco en el botón de pausa (además de en los pasos)
  if (play) play.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); var n = pills.length; pick(e.key === 'ArrowRight' ? (cur + 1) % n : (cur - 1 + n) % n, true); }
  });
  if (play) play.addEventListener('click', function () {
    userPaused = !userPaused;
    if (!userPaused) show(cur); // reinicia la barra del paso actual
    run();
  });
  var stage = lab.querySelector('.lab-stage');
  if (stage) {
    stage.addEventListener('mouseenter', function () { hover = true; run(); });
    stage.addEventListener('mouseleave', function () { hover = false; if (!userPaused) show(cur); run(); });
  }
  document.addEventListener('visibilitychange', run);
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (es) { visible = es[0].isIntersecting; run(); }, { threshold: 0.35 }).observe(lab);
  } else { visible = true; run(); }
  show(0); run();
})();

/* Accesibilidad (19 nov 2026, WCAG 2.2.2): el movimiento que dura más de 5 s se puede parar.
   - Las demos animadas de los casos llevan un botón «Pausar» propio.
   - El movimiento decorativo (órbitas, fotos que flotan, puntos que laten) se queda quieto a los 5 s.
   Con «reducir movimiento» no hay animación, así que no se añade nada. */
(function () {
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  setTimeout(function () { document.documentElement.classList.add('still'); }, 5000);
  var figs = document.querySelectorAll('figure.eval');
  Array.prototype.forEach.call(figs, function (fig) {
    var btn = document.createElement('button');
    btn.type = 'button'; btn.className = 'demo-play';
    var set = function (paused) {
      fig.classList.toggle('is-paused', paused);
      btn.setAttribute('aria-pressed', paused ? 'true' : 'false');
      btn.setAttribute('aria-label', paused ? 'Reanudar la animación' : 'Pausar la animación');
      btn.innerHTML = (paused
        ? '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M5 3.2v9.6a.6.6 0 0 0 .9.5l7.6-4.8a.6.6 0 0 0 0-1L5.9 2.7a.6.6 0 0 0-.9.5z"/></svg>Reanudar'
        : '<svg viewBox="0 0 16 16" aria-hidden="true"><rect x="3.5" y="3" width="3" height="10" rx="1"/><rect x="9.5" y="3" width="3" height="10" rx="1"/></svg>Pausar');
    };
    set(false);
    btn.addEventListener('click', function () { set(!fig.classList.contains('is-paused')); });
    fig.insertBefore(btn, fig.firstChild);
  });
})();
