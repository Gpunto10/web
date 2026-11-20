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
    document.documentElement.classList.toggle('menu-open', open);
    mbtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    mbtn.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
  }
  if (mbtn) {
    mbtn.addEventListener('click', function () { setMenu(!hdr.classList.contains('open')); });
    document.querySelectorAll('.mnav a, .nav .btn').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  // Menú de la home (19 nov 2026): la home es una sola página. Los enlaces bajan con scroll suave a su sección
  // (el navegador lo hace con el ancla y scroll-behavior) y el menú marca la sección en la que estás.
  var onHome = /\/$|index\.html$/.test(location.pathname);
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.nav ul a[href^="#"]:not(.btn), .mnav a[href^="#"]'));
  if (onHome && navLinks.length && 'IntersectionObserver' in window) {
    var secs = {};
    navLinks.forEach(function (a) { var id = a.getAttribute('href').slice(1), t = document.getElementById(id); if (t) secs[id] = t; });
    var mark = function (id) {
      navLinks.forEach(function (a) {
        var on = a.getAttribute('href') === '#' + id;
        a.classList.toggle('active', on);
        if (on) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current');
      });
    };
    var vis = {};
    var so = new IntersectionObserver(function (es) {
      es.forEach(function (e) { vis[e.target.id] = e.isIntersecting; });
      var cur = '';
      Object.keys(secs).forEach(function (id) { if (vis[id]) cur = id; });
      mark(cur);
    }, { rootMargin: '-45% 0px -50% 0px' });
    Object.keys(secs).forEach(function (id) { so.observe(secs[id]); });
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
  var cur = 0, timer = null, visible = false, hover = false, focused = false;
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
    panels.forEach(function (p, k) { p.classList.toggle('on', k === i); p.hidden = false; p.removeAttribute('aria-hidden'); });
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
    var go = !userPaused && visible && !hover && !focused && !document.hidden;
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
  // Con el foco del teclado en los pasos o en la pantalla, el recorrido se detiene (se reanuda al salir)
  lab.addEventListener('focusin', function (e) { focused = e.target !== play; run(); });
  lab.addEventListener('focusout', function (e) { if (!lab.contains(e.relatedTarget)) { focused = false; run(); } });
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

/* Móvil (19 nov 2026): el chat flotante y «volver arriba» se apartan mientras se baja, para no tapar el contenido.
   Vuelven al subir, al pararse arriba del todo o al llegar al final de la página. */
(function () {
  var root = document.documentElement, last = window.pageYOffset, tick = false;
  function upd() {
    var y = window.pageYOffset, max = root.scrollHeight - root.clientHeight;
    if (window.innerWidth > 720 || y < 80 || y > max - 80) root.classList.remove('fab-away');
    else if (y > last + 6) root.classList.add('fab-away');
    else if (y < last - 6) root.classList.remove('fab-away');
    last = y; tick = false;
  }
  window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(upd); } }, { passive: true });
})();

/* Sobre mí: «Leer más» pliega la bio y el bloque docente (19 nov 2026) */
(function () {
  var b = document.getElementById('more-toggle'); if (!b) return;
  var sec = document.getElementById('sobre-mi'), t = b.querySelector('.mt-t');
  function set(open) {
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
    t.textContent = open ? 'Leer menos' : 'Leer más';
    sec.classList.toggle('is-folded', !open);
  }
  b.hidden = false; set(false);
  b.addEventListener('click', function () { set(b.getAttribute('aria-expanded') !== 'true'); });
})();

/* Contacto: «Escribir por el chat» abre el chat flotante (19 nov 2026) */
(function () {
  var b = document.getElementById('open-chat'), fab = document.querySelector('#chat .chat-fab');
  if (!b) return; if (!fab) { b.hidden = true; return; }
  b.addEventListener('click', function () { fab.click(); });
})();

/* Móvil: en Contacto se apartan los botones flotantes para no tapar el chat del cuadro (19 nov 2026) */
(function () {
  var c = document.getElementById('contacto');
  if (!c || !('IntersectionObserver' in window)) return;
  new IntersectionObserver(function (es) {
    document.documentElement.classList.toggle('contact-in', es[0].isIntersecting);
  }, { threshold: 0.35 }).observe(c);
})();

/* Banner de píxeles: los píxeles de la foto de nubes vuelan y se unen hasta formar la imagen (20 nov 2026).
   Con «reducir movimiento» o sin canvas se ve la imagen tal cual. */
(function () {
  var box = document.getElementById('statement-px');
  if (!box) return;
  var cv = box.querySelector('.px-canvas');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce || !cv || !cv.getContext || !('IntersectionObserver' in window)) { if (cv) cv.remove(); return; }
  box.classList.add('px-js');
  var img = new Image(), ready = false, seen = false, started = false;
  img.onload = function () { ready = true; go(); };
  img.onerror = function () { box.classList.remove('px-js'); cv.remove(); };
  img.src = box.getAttribute('data-img');
  new IntersectionObserver(function (es, o) {
    if (es[0].isIntersecting) { seen = true; o.disconnect(); go(); }
  }, { threshold: 0.35 }).observe(box);

  function go() {
    if (!ready || !seen || started) return;
    started = true;
    var W = box.clientWidth, H = box.clientHeight, dpr = Math.min(window.devicePixelRatio || 1, 2);
    cv.width = W * dpr; cv.height = H * dpr;
    var ctx = cv.getContext('2d'); ctx.scale(dpr, dpr);
    var t = Math.max(14, Math.round(W / 46)), cols = Math.ceil(W / t), rows = Math.ceil(H / t);
    // muestrea la imagen recortada como «cover» a una rejilla de cols × rows
    var off = document.createElement('canvas'); off.width = cols; off.height = rows;
    var oc = off.getContext('2d'), s = Math.max(cols / img.width, rows / img.height);
    var dw = img.width * s, dh = img.height * s;
    oc.drawImage(img, (cols - dw) / 2, (rows - dh) / 2, dw, dh);
    var data;
    try { data = oc.getImageData(0, 0, cols, rows).data; } catch (e) { box.classList.add('px-done'); return; }
    var tiles = [], cx = cols / 2, cy = rows / 2, maxd = Math.hypot(cx, cy);
    for (var y = 0; y < rows; y++) for (var x = 0; x < cols; x++) {
      var i = (y * cols + x) * 4, a = Math.random() * Math.PI * 2, r = (0.3 + Math.random() * 0.7) * W * 0.6;
      tiles.push({ x: x * t, y: y * t, sx: x * t + Math.cos(a) * r, sy: y * t + Math.sin(a) * r,
        c: 'rgb(' + data[i] + ',' + data[i + 1] + ',' + data[i + 2] + ')',
        d: (Math.hypot(x - cx, y - cy) / maxd) * 700 + Math.random() * 350 });
    }
    var DUR = 900, t0 = performance.now(), gap = Math.max(1, t * 0.12);
    function frame(now) {
      var el = now - t0, done = true;
      ctx.clearRect(0, 0, W, H);
      for (var k = 0; k < tiles.length; k++) {
        var p = tiles[k], q = Math.min(1, Math.max(0, (el - p.d) / DUR));
        if (q < 1) done = false;
        if (q <= 0) continue;
        var e = 1 - Math.pow(1 - q, 3);
        ctx.globalAlpha = Math.min(1, q * 1.6);
        ctx.fillStyle = p.c;
        ctx.fillRect(p.sx + (p.x - p.sx) * e, p.sy + (p.y - p.sy) * e, t - gap, t - gap);
      }
      ctx.globalAlpha = 1;
      if (!done) requestAnimationFrame(frame); else box.classList.add('px-done');
    }
    requestAnimationFrame(frame);
  }
})();
