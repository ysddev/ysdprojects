(function () {
  var html = document.documentElement;
  var lang = html.lang === 'en' ? 'en' : 'ru';
  var base = document.body.getAttribute('data-base') || '';
  var T = {
    ru: { area: 'Площадь', year: 'Год', place: 'Место', type: 'Тип', m2: 'м²', next: 'Следующий проект',
          photo: 'Фото', of: 'из', close: 'Закрыть', prev: 'Назад', fwd: 'Вперёд',
          need: 'Заполните это поле', agree: 'Нужно согласие на обработку данных',
          sending: 'Отправляем…', sent: 'Заявка отправлена. Мы свяжемся с вами в ближайшее время.',
          fail: 'Не удалось отправить заявку. Проверьте соединение и попробуйте ещё раз.', notfound: 'Проект не найден.' },
    en: { area: 'Area', year: 'Year', place: 'Location', type: 'Type', m2: 'm²', next: 'Next project',
          photo: 'Photo', of: 'of', close: 'Close', prev: 'Previous', fwd: 'Next',
          need: 'Please fill in this field', agree: 'Please agree to the processing of your data',
          sending: 'Sending…', sent: 'Your request has been sent. We will get back to you shortly.',
          fail: 'The request could not be sent. Check your connection and try again.', notfound: 'Project not found.' }
  }[lang];

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function data() { return fetch(base + 'content/projects.json').then(function (r) { return r.json(); }); }

  /* Шапка: прозрачная над фото, плотная после прокрутки */
  var top = document.querySelector('.top');
  if (top && !top.classList.contains('light')) {
    var onScroll = function () { top.classList.toggle('solid', window.scrollY > window.innerHeight * 0.6); };
    window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  }
  var burger = document.querySelector('.burger');
  if (burger) {
    burger.addEventListener('click', function () {
      var open = top.classList.toggle('open');
      burger.setAttribute('aria-expanded', open);
    });
    document.querySelectorAll('.nav a').forEach(function (a) { a.addEventListener('click', function () { top.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); }); });
  }

  /* Портфолио на главной */
  var grid = document.getElementById('grid');
  if (grid) {
    data().then(function (d) {
      grid.innerHTML = d.projects.map(function (p, i) {
        var t = p[lang];
        return '<a class="card g' + (i % 6) + '" href="project.html?p=' + p.slug + '">' +
          '<div class="ph"><img src="' + base + p.cover + '" alt="' + esc(t.title) + '" loading="lazy"></div>' +
          '<div class="cap"><b>' + esc(t.title) + '</b><span>' + esc(t.place) + ', ' + p.year + '</span></div></a>';
      }).join('');
    });
  }

  /* Страница проекта */
  var page = document.getElementById('project');
  if (page) {
    var slug = new URLSearchParams(location.search).get('p');
    data().then(function (d) {
      var list = d.projects, idx = -1;
      list.forEach(function (p, i) { if (p.slug === slug) idx = i; });
      if (idx < 0) { idx = 0; if (slug) { page.innerHTML = '<div class="wrap p-head"><p>' + T.notfound + '</p></div>'; return; } }
      var p = list[idx], t = p[lang], nx = list[(idx + 1) % list.length];
      document.title = t.title + ' — ' + document.querySelector('.brand').textContent;
      var md = document.querySelector('meta[name=description]'); if (md) md.content = t.text.slice(0, 160);
      document.querySelectorAll('[data-switch]').forEach(function (a) { a.href = a.getAttribute('data-switch') + '?p=' + p.slug; });
      var ph = p.photos, gal = '', i = 1;
      while (i < ph.length) {
        var a = ph[i], b = ph[i + 1];
        var land = a.w > a.h * 1.15;
        if (land) { gal += cell(a, i, 'w'); i += 1; }
        else if (b && !(b.w > b.h * 1.15)) { gal += cell(a, i, 'h') + cell(b, i + 1, 'h'); i += 2; }
        else { gal += cell(a, i, 'h solo'); i += 1; }
      }
      function cell(x, n, cls) { return '<button class="' + cls + '" data-i="' + n + '" aria-label="' + T.photo + ' ' + (n + 1) + '"><img src="' + base + x.src + '" alt="' + esc(t.title) + ', ' + T.photo.toLowerCase() + ' ' + (n + 1) + '" loading="lazy"></button>'; }
      page.innerHTML =
        '<div class="wrap p-head"><a class="back" href="index.html#projects">' + (lang === 'en' ? 'All projects' : 'Все проекты') + '</a>' +
        '<h1 class="p-title">' + esc(t.title) + '</h1></div>' +
        '<div class="p-cover"><button style="border:0;padding:0;width:100%;cursor:zoom-in;display:block" data-i="0" aria-label="' + T.photo + ' 1"><img src="' + base + ph[0].src + '" alt="' + esc(t.title) + '"></button></div>' +
        '<div class="wrap"><div class="p-info"><dl class="p-meta">' +
          '<dt>' + T.place + '</dt><dd>' + esc(t.place) + '</dd><dt>' + T.type + '</dt><dd>' + esc(t.type) + '</dd>' +
          '<dt>' + T.area + '</dt><dd>' + p.area + ' ' + T.m2 + '</dd><dt>' + T.year + '</dt><dd>' + p.year + '</dd></dl>' +
          '<p class="p-text">' + esc(t.text) + '</p></div>' +
        '<div class="gal">' + gal + '</div>' +
        '<div class="p-cta"><p>' + (lang === 'en' ? 'Planning a house or an interior?' : 'Задумали дом или интерьер?') + '</p>' +
          '<a class="btn" href="index.html#contact">' + (lang === 'en' ? 'Discuss your project' : 'Обсудить проект') + '</a></div>' +
        '<a class="next" href="project.html?p=' + nx.slug + '"><small>' + T.next + '</small><b>' + esc(nx[lang].title) + '</b></a></div>';
      lightbox(ph.map(function (x) { return base + x.src; }), t.title);
    });
  }

  function lightbox(srcs, title) {
    var lb = document.createElement('div');
    lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', title);
    lb.innerHTML = '<img alt=""><button class="x">' + T.close + '</button><button class="pv">' + T.prev + '</button><button class="nx">' + T.fwd + '</button><div class="cnt"></div>';
    document.body.appendChild(lb);
    var img = lb.querySelector('img'), cnt = lb.querySelector('.cnt'), cur = 0, last = null;
    function show(n) { cur = (n + srcs.length) % srcs.length; img.src = srcs[cur]; img.alt = title + ', ' + T.photo.toLowerCase() + ' ' + (cur + 1); cnt.textContent = (cur + 1) + ' ' + T.of + ' ' + srcs.length; }
    function open(n) { last = document.activeElement; show(n); lb.classList.add('on'); document.body.style.overflow = 'hidden'; lb.querySelector('.x').focus(); }
    function close() { lb.classList.remove('on'); document.body.style.overflow = ''; if (last) last.focus(); }
    document.querySelectorAll('[data-i]').forEach(function (b) { b.addEventListener('click', function () { open(+b.getAttribute('data-i')); }); });
    lb.querySelector('.x').onclick = close;
    lb.querySelector('.pv').onclick = function () { show(cur - 1); };
    lb.querySelector('.nx').onclick = function () { show(cur + 1); };
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('on')) return;
      if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(cur - 1); if (e.key === 'ArrowRight') show(cur + 1);
    });
    var sx = 0;
    lb.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) { var dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) show(cur + (dx < 0 ? 1 : -1)); });
  }

  /* Заявка. Куда отправлять, задаётся в data-endpoint формы (почта или Telegram — уточняем у клиента). */
  var form = document.getElementById('form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll('[required]').forEach(function (el) {
        var bad = el.type === 'checkbox' ? !el.checked : !el.value.trim();
        var err = form.querySelector('[data-err="' + el.name + '"]');
        if (el.type !== 'checkbox') el.setAttribute('aria-invalid', bad);
        if (err) err.textContent = bad ? (el.type === 'checkbox' ? T.agree : T.need) : '';
        if (bad && ok) { el.focus(); ok = false; }
      });
      if (!ok) return;
      var btn = form.querySelector('.btn'), label = btn.textContent;
      btn.disabled = true; btn.textContent = T.sending;
      var fd = new FormData(form), endpoint = form.getAttribute('data-endpoint');
      var send = endpoint ? fetch(endpoint, { method: 'POST', body: fd }).then(function (r) { if (!r.ok) throw 0; })
                          : new Promise(function (res) { setTimeout(res, 500); });
      send.then(function () {
        if (window.ym && window.YM_ID) window.ym(window.YM_ID, 'reachGoal', 'lead');
        var done = document.createElement('p'); done.className = 'done'; done.setAttribute('role', 'status'); done.textContent = T.sent;
        form.replaceWith(done);
      }).catch(function () {
        btn.disabled = false; btn.textContent = label;
        var err = form.querySelector('[data-err="form"]'); if (err) err.textContent = T.fail;
      });
    });
  }
})();
