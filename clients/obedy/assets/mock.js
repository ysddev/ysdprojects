// Макет: формы не отправляются на сервер, а ведут на следующий экран.
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return JSON.parse(sessionStorage.getItem(k)); } catch (e) { return null; } },
    set: function (k, v) { try { sessionStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };

  function toast(msg) {
    var t = document.createElement('div');
    t.className = 'flash mock-toast';
    t.setAttribute('role', 'status');
    t.textContent = msg;
    document.body.appendChild(t);
    setTimeout(function () { t.style.opacity = '0'; }, 2600);
    setTimeout(function () { t.remove(); }, 3100);
  }

  function setStatus(sel, st) {
    sel.value = st;
    sel.className = 'badge ' + st;
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
      $$('select[name=status]').forEach(function (s) { if (s.value === 'new') setStatus(s, 'accepted'); });
      f.remove();
      toast('Все новые заказы приняты');
      return;
    }
    if (to === 'cancel') {
      var card = f.closest('.order');
      var b = card && $('.badge', card);
      if (b) { b.className = 'badge cancelled'; b.textContent = 'Отменён'; }
      f.remove();
      toast('Заказ отменён');
      return;
    }
    if (to === 'report') {
      if (sub && sub.name === 'download') { location.href = 'report-example.xlsx'; return; }
      toast('В макете период не пересчитывается — скачайте пример отчёта');
      return;
    }
    if (to === 'done') {
      var lines = [];
      $$('.card', f).forEach(function (c) {
        var q = parseInt($('input', c).value, 10) || 0;
        if (q > 0) lines.push([c.getAttribute('data-title'), q, parseInt(c.getAttribute('data-price'), 10) * q]);
      });
      store.set('mock-order', { lines: lines, comment: ($('textarea[name=comment]', f) || {}).value || '' });
      location.href = 'done.html';
      return;
    }
    if (to === 'stay') {
      toast(f.getAttribute('data-msg') || 'Готово. В макете изменения не сохраняются');
      return;
    }
    location.href = to;
  }, true);

  // Списки, которые применяются сразу (статус заказа, фильтр компании)
  $$('[data-mock-auto]').forEach(function (s) {
    s.addEventListener('change', function () { if (s.form.requestSubmit) s.form.requestSubmit(); });
  });

  var css = document.createElement('style');
  css.textContent = '.mock-toast{position:fixed;left:50%;top:16px;transform:translateX(-50%);z-index:100;box-shadow:0 10px 30px -10px rgba(23,32,27,.4);transition:opacity .5s;max-width:calc(100% - 32px)}'
    + '.mock-tag{position:fixed;left:12px;bottom:12px;z-index:40;background:rgba(23,32,27,.82);color:#EEF2EC;font:500 12.5px/1 Onest,system-ui,sans-serif;padding:9px 12px;border-radius:999px;text-decoration:none}'
    + '@media (max-width:900px){body:has(.cartbar.on) .mock-tag{display:none}.mock-tag{bottom:auto;top:auto;left:auto;right:10px;bottom:10px}}';
  document.head.appendChild(css);

  // Экран «Заказ принят» показывает то, что выбрали в меню
  var o = store.get('mock-order');
  var k = document.body.getAttribute('data-page') === 'done.html' && $('.kitchen');
  if (o && o.lines && o.lines.length && k) {
    var fmt = function (kop) { return String(Math.floor(kop / 100)).replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + ' ₽'; };
    var total = 0, html = '';
    var esc = function (s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; };
    o.lines.forEach(function (l) { total += l[2]; html += '<li><span>' + esc(l[0]) + ' × ' + l[1] + '</span><b>' + fmt(l[2]) + '</b></li>'; });
    html += '<li style="border-top:1px solid var(--s2);padding-top:10px"><span><b>Итого</b></span><b>' + fmt(total) + '</b></li>';
    k.innerHTML = html;
    var cm = $('[data-mock-comment]');
    if (cm) { if (o.comment) cm.innerHTML = '<span class="mut">Комментарий:</span> ' + esc(o.comment); else cm.remove(); }
  }

  // Плашка «Макет» со ссылкой на карту экранов
  var tag = document.createElement('a');
  tag.href = 'screens.html';
  tag.className = 'mock-tag';
  tag.textContent = 'Макет · все экраны';
  document.body.appendChild(tag);
})();
