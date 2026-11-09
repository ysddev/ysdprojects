// Демо: формы не отправляются на сервер, а ведут на следующий экран.
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return JSON.parse(sessionStorage.getItem(k)); } catch (e) { return null; } },
    set: function (k, v) { try { sessionStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };
  var esc = function (s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; };

  function toast(msg) {
    var t = document.createElement('div');
    t.className = 'notice ok mock-toast';
    t.setAttribute('role', 'status');
    t.textContent = msg;
    document.body.appendChild(t);
    setTimeout(function () { t.style.opacity = '0'; }, 2600);
    setTimeout(function () { t.remove(); }, 3100);
  }

  function setStatus(sel, st) {
    sel.value = st;
    sel.className = 'status ' + st;
    var tr = sel.closest('tr');
    if (tr) tr.classList.toggle('off', st === 'cancelled');
  }

  document.addEventListener('submit', function (e) {
    var f = e.target, to = f.getAttribute('data-to') || 'stay';
    var sub = e.submitter;
    e.preventDefault();
    e.stopImmediatePropagation();

    if (to === 'login') {
      var l = (($('input[name=login]', f) || {}).value || '').trim().toLowerCase();
      location.href = (l === 'olga' || l === 'admin') ? 'admin-orders.html' : (l === 'new' ? 'welcome.html' : 'menu.html');
      return;
    }
    if (to === 'status') {
      var sel = $('select[name=status]', f);
      if (sel) { setStatus(sel, sel.value); toast('Статус изменён'); return; }
      $$('.tbl select[name=status]').forEach(function (s) { if (s.value === 'new') setStatus(s, 'accepted'); });
      f.remove();
      toast('Все новые заказы приняты');
      return;
    }
    if (to === 'cancel') {
      var card = f.closest('.history-card');
      var b = card && $('.status', card);
      if (b) { b.className = 'status cancelled'; b.textContent = 'Отменён'; }
      var sp = f.previousElementSibling;
      if (sp && sp.tagName === 'SPAN') sp.remove();
      f.remove();
      toast('Заказ отменён');
      return;
    }
    if (to === 'report') {
      if (sub && sub.name === 'download') { location.href = 'report-example.xlsx'; return; }
      toast('В демо период не пересчитывается — скачайте пример отчёта');
      return;
    }
    if (to === 'done') {
      var lines = [];
      $$('.meal-card', f).forEach(function (c) {
        var inp = $('input[type=hidden]', c);
        var q = inp ? parseInt(inp.value, 10) || 0 : 0;
        if (q > 0) lines.push([c.getAttribute('data-title'), q, parseInt(c.getAttribute('data-price'), 10) * q]);
      });
      var loc = $('select[name=location_id]', f);
      var cur = $('.date[aria-current=true]');
      var when = cur ? cur.innerText.split('\n').filter(Boolean).pop() : '';
      store.set('mock-order', {
        when: when,
        lines: lines,
        comment: ($('textarea[name=comment]', f) || {}).value || '',
        place: loc && loc.value ? loc.options[loc.selectedIndex].text : ''
      });
      location.href = 'done.html';
      return;
    }
    if (to === 'stay') {
      toast(f.getAttribute('data-msg') || 'Готово. В демо изменения не сохраняются');
      return;
    }
    location.href = to;
  }, true);

  // Списки, которые применяются сразу (статус заказа, фильтры)
  $$('[data-mock-auto]').forEach(function (s) {
    s.addEventListener('change', function () { if (s.form.requestSubmit) s.form.requestSubmit(); });
  });

  var css = document.createElement('style');
  css.textContent = '.mock-toast{position:fixed;left:50%;top:16px;transform:translateX(-50%);z-index:100;box-shadow:0 10px 30px -10px rgba(35,49,40,.4);transition:opacity .5s;max-width:calc(100% - 32px)}'
    + '.mock-tag{position:fixed;right:12px;bottom:12px;z-index:40;background:rgba(35,49,40,.88);color:#fffef9;font:600 12.5px/1 Manrope,system-ui,sans-serif;padding:9px 12px;border-radius:999px;text-decoration:none}'
    + '@media (max-width:980px){body:has(.cartbar.on) .mock-tag{display:none}.mock-tag{right:10px}}'
    + '@media print{.mock-tag,.mock-toast{display:none}}';
  document.head.appendChild(css);

  // Экран «Заказ принят» показывает то, что выбрали в меню
  var o = store.get('mock-order');
  var k = document.body.getAttribute('data-page') === 'done.html' && $('.receipt .lines');
  if (o && o.lines && o.lines.length && k) {
    var fmt = function (kop) { return String(Math.floor(kop / 100)).replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + ' ₽'; };
    var total = 0, html = '';
    o.lines.forEach(function (l) { total += l[2]; html += '<div><span>' + esc(l[0]) + ' × ' + l[1] + '</span><b>' + fmt(l[2]) + '</b></div>'; });
    html += '<div class="total"><span>Итого</span><span>' + fmt(total) + '</span></div>';
    k.innerHTML = html;
    var cm = $('.receipt .comment');
    if (cm) { if (o.comment) cm.textContent = o.comment; else cm.remove(); }
    else if (o.comment) { var p = document.createElement('p'); p.className = 'comment'; p.textContent = o.comment; k.after(p); }
    var no = $('.receipt > p.mut');
    if (no && o.when) no.textContent = no.textContent.replace(/доставка .*/, 'доставка ' + o.when);
    if (o.place) {
      $$('.receipt .meta div').forEach(function (d) {
        var s = $('span', d);
        if (s && s.textContent === 'Куда') d.innerHTML = '<span>Куда</span>' + esc(o.place);
      });
    }
  }

  // Плашка «Демо» со ссылкой на карту экранов
  if (document.body.getAttribute('data-page') !== 'screens.html') {
    var tag = document.createElement('a');
    tag.href = 'screens.html';
    tag.className = 'mock-tag';
    tag.textContent = 'Демо · все экраны';
    document.body.appendChild(tag);
  }
})();
