(function () {
  'use strict';
  document.documentElement.classList.remove('no-js');

  // Mobile-Menü
  var burger = document.querySelector('.burger'), menu = document.getElementById('menu');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    menu.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { menu.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); }
    });
  }

  // Hell-/Dunkelmodus: standardmäßig automatisch nach Gerät (System-Einstellung).
  // Der Umschalter wechselt Automatisch → Hell → Dunkel; die Wahl wird gespeichert, falls der Browser es erlaubt.
  var root = document.documentElement, tbtn = document.querySelector('.themebtn');
  var mode = 'auto';
  try { var saved = localStorage.getItem('theme'); if (saved === 'light' || saved === 'dark') { mode = saved; } } catch (e) {}
  var apply = function () {
    if (mode === 'auto') { root.removeAttribute('data-theme'); } else { root.setAttribute('data-theme', mode); }
    if (tbtn) {
      var label = { auto: ['◐', 'Darstellung: automatisch nach Gerät. Zum Umschalten klicken (nächster Modus: hell)'],
                    light: ['☀', 'Darstellung: hell. Zum Umschalten klicken (nächster Modus: dunkel)'],
                    dark: ['☾', 'Darstellung: dunkel. Zum Umschalten klicken (nächster Modus: automatisch)'] }[mode];
      tbtn.textContent = label[0]; tbtn.setAttribute('aria-label', label[1]); tbtn.title = label[1];
    }
  };
  if (tbtn) {
    tbtn.addEventListener('click', function () {
      mode = mode === 'auto' ? 'light' : mode === 'light' ? 'dark' : 'auto';
      try { if (mode === 'auto') { localStorage.removeItem('theme'); } else { localStorage.setItem('theme', mode); } } catch (e) {}
      apply();
    });
  }
  apply();

  // Einblenden beim Scrollen
  var items = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) { items.forEach(function (el) { el.classList.add('in'); }); }
  else {
    // „Zusammenbauen“: jedes Element fliegt aus wechselnder Richtung an seinen Platz (gleiche Dauer, kleiner Versatz je Geschwister)
    var dirs = ['l', 'u', 'r', 's'];
    items.forEach(function (el) {
      var sibs = Array.prototype.filter.call(el.parentNode.children, function (c) { return c.classList.contains('reveal') || c.querySelector('.reveal') === null; }), i = Math.max(0, sibs.indexOf(el));
      el.setAttribute('data-from', 'u');
      el.__d = Math.min(i, 4) * 0.05;
    });
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        var el = en.target;
        if (en.isIntersecting) {
          el.style.setProperty('--rd', el.__d + 's'); el.classList.add('in');
          clearTimeout(el.__t); el.__t = setTimeout(function () { el.style.setProperty('--rd', '0s'); }, 1300);
        } else { el.style.setProperty('--rd', '0s'); el.classList.remove('in'); }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });
    items.forEach(function (el) { io.observe(el); });
    // Abschnitte: Zeichnungen und Hintergrundzeichen bauen sich beim ersten Erscheinen auf
    var secIO = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('seen'); secIO.unobserve(en.target); } });
    }, { threshold: 0.05 });
    document.querySelectorAll('section').forEach(function (sx) { secIO.observe(sx); });

    // Aktiver Menüpunkt beim Scrollen
    var links = {};
    document.querySelectorAll('.menu a[href^="#"]').forEach(function (a) { links[a.getAttribute('href').slice(1)] = a; });
    var spy = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting && links[en.target.id]) {
          Object.keys(links).forEach(function (k) { links[k].classList.remove('on'); });
          links[en.target.id].classList.add('on');
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    Object.keys(links).forEach(function (id) { var s = document.getElementById(id); if (s) { spy.observe(s); } });
  }


  // Animationen: Lesefortschritt, Parallaxe der Zeichnungen, Lichtkegel auf Produktkacheln (nicht bei „Bewegung reduzieren“)
  if (!(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches)) {
    var bar = document.createElement('div'); bar.className = 'progress'; bar.setAttribute('aria-hidden', 'true'); document.body.appendChild(bar);
    var decos = Array.prototype.slice.call(document.querySelectorAll('.deco')), ticking = false;
    var frame = function () {
      ticking = false;
      var h = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.setProperty('--p', h > 0 ? Math.min(1, window.scrollY / h).toFixed(4) : 0);
      var vc = window.innerHeight / 2;
      decos.forEach(function (d) {
        var sec = d.parentNode, r = sec.getBoundingClientRect();
        if (r.bottom < -200 || r.top > window.innerHeight + 200) { return; }
        var off = ((r.top + r.height / 2) - vc) * -0.07;
        d.style.setProperty('--py', Math.max(-60, Math.min(60, off)).toFixed(1) + 'px');
      });
    };
    var onScroll = function () { if (!ticking) { ticking = true; requestAnimationFrame(frame); } };
    window.addEventListener('scroll', onScroll, { passive: true }); window.addEventListener('resize', onScroll); frame();
  }


  // Aufklappen mit Animation (Höhe + Einblenden); bei „Bewegung reduzieren“ ganz normal ohne Animation
  if (!(window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) && 'animate' in Element.prototype) {
    document.querySelectorAll('details').forEach(function (d) {
      var sum = d.querySelector('summary'), body = d.querySelector('.dbody'), anim = null;
      if (!sum || !body) { return; }
      sum.addEventListener('click', function (e) {
        e.preventDefault();
        if (anim) { anim.cancel(); }
        var opening = !d.open;
        if (opening) { d.open = true; }
        var h = body.offsetHeight;
        body.style.overflow = 'hidden';
        var frames = opening
          ? [{ height: '0px', opacity: 0, transform: 'translateY(-8px)' }, { height: h + 'px', opacity: 1, transform: 'none' }]
          : [{ height: h + 'px', opacity: 1, transform: 'none' }, { height: '0px', opacity: 0, transform: 'translateY(-8px)' }];
        anim = body.animate(frames, { duration: 450, easing: 'cubic-bezier(.2,.7,.2,1)' });
        anim.onfinish = function () { if (!opening) { d.open = false; } body.style.overflow = ''; anim = null; };
        anim.oncancel = function () { body.style.overflow = ''; };
      });
    });
  }


  // Defekte Original-Bilder ausblenden statt kaputtes Symbol zu zeigen
  document.querySelectorAll('img[data-orig]').forEach(function (img) {
    img.addEventListener('error', function () { img.style.display = 'none'; });
  });

  // Copyright-Jahr automatisch
  var yr = document.getElementById('yr'); if (yr) { yr.textContent = new Date().getFullYear(); }

  // Kontaktformular: zuerst Versand an den Server-Endpunkt (/_tp/form.php, turbopress).
  // Ist er nicht erreichbar oder antwortet nicht mit Erfolg, öffnet sich stattdessen
  // das E-Mail-Programm mit vorausgefüllter Nachricht – das Formular läuft nie ins Leere.
  var form = document.getElementById('contact-form');
  if (form) {
    var status = form.querySelector('.form-status');
    var say = function (msg, ok) { status.textContent = msg; status.className = 'form-status ' + (ok ? 'ok' : 'warn'); };
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button[type=submit]');
      btn.disabled = true; say('Wird gesendet …', true);
      var fd = new FormData(form);
      var viaMail = function () {
        var body = 'Name: ' + fd.get('name') + '\nE-Mail: ' + fd.get('email') + '\n\n' + fd.get('message');
        window.location.href = 'mailto:' + form.dataset.mail + '?subject=' + encodeURIComponent('Anfrage über robertross.de') + '&body=' + encodeURIComponent(body);
        say('Der Server-Versand ist derzeit nicht verfügbar. Ihr E-Mail-Programm wurde mit der Nachricht geöffnet – bitte dort absenden.', false);
        btn.disabled = false;
      };
      if (!window.fetch || location.protocol === 'file:') { viaMail(); return; }
      fetch(form.action, { method: 'POST', body: fd })
        .then(function (r) {
          if (r.ok) { say('Vielen Dank, Ihre Nachricht wurde gesendet.', true); form.reset(); btn.disabled = false; }
          else { viaMail(); }
        })
        .catch(viaMail);
    });
  }
})();
