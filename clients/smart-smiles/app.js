(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  // шапка: тонкая линия при прокрутке
  var hd = $('.hd');
  var onScroll = function () { if (hd) hd.classList.toggle('sc', scrollY > 8); };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // мобильное меню
  var mnav = $('#mnav'), burger = $('.burger');
  function menu(open) {
    if (!mnav) return;
    mnav.classList.toggle('open', open);
    mnav.setAttribute('aria-hidden', open ? 'false' : 'true');
    burger && burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open ? 'hidden' : '';
    if (open) { var f = $('nav a', mnav); f && f.focus(); } else { burger && burger.focus(); }
  }
  burger && burger.addEventListener('click', function () { menu(true); });
  $$('[data-close-menu]').forEach(function (b) { b.addEventListener('click', function () { menu(false); }); });
  mnav && $$('a', mnav).forEach(function (a) { a.addEventListener('click', function () { menu(false); }); });
  addEventListener('keydown', function (e) { if (e.key === 'Escape' && mnav && mnav.classList.contains('open')) menu(false); });

  // вопросы-ответы
  $$('.qa button').forEach(function (b) {
    b.addEventListener('click', function () {
      var open = b.getAttribute('aria-expanded') === 'true';
      b.setAttribute('aria-expanded', open ? 'false' : 'true');
      var a = document.getElementById(b.getAttribute('aria-controls'));
      if (a) a.hidden = open;
    });
  });

  // всплывающая подсказка
  var toast = $('#toast'), tt;
  function say(msg) {
    if (!toast) return;
    toast.textContent = msg; toast.classList.add('on');
    clearTimeout(tt); tt = setTimeout(function () { toast.classList.remove('on'); }, 3600);
  }
  $$('[data-demo]').forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); say(a.getAttribute('data-demo')); });
  });

  // запись: проверка полей; в демо заявка никуда не уходит — честно об этом пишем
  $$('form.fm').forEach(function (f) {
    var err = $('.err', f);
    var tel = $('input[type=tel]', f);
    tel && tel.addEventListener('input', function () {
      var d = tel.value.replace(/\D/g, '');
      if (d[0] === '8') d = '7' + d.slice(1);
      if (d && d[0] !== '7') d = '7' + d;
      d = d.slice(0, 11);
      var o = d ? '+7' : '';
      if (d.length > 1) o += ' (' + d.slice(1, 4);
      if (d.length >= 4) o += ') ' + d.slice(4, 7);
      if (d.length >= 7) o += '-' + d.slice(7, 9);
      if (d.length >= 9) o += '-' + d.slice(9, 11);
      tel.value = o;
    });
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = $('input[name=name]', f), ok = $('input[name=agree]', f);
      var msg = '';
      if (!name.value.trim()) msg = 'Укажите имя.';
      else if (tel.value.replace(/\D/g, '').length < 11) msg = 'Проверьте номер телефона.';
      else if (!ok.checked) msg = 'Нужно согласие на обработку персональных данных.';
      err.textContent = msg;
      if (msg) return;
      var box = f.parentNode;
      box.innerHTML = '<div class="done" role="status" tabindex="-1"><h3>Заявка заполнена верно</h3>' +
        '<p class="mut">Это демо-версия, поэтому заявка никуда не отправлена.</p>' +
        '<div class="note">В рабочем сайте на Tilda заявка сразу уходит администратору клиники в Telegram и на почту, а при желании в CRM.</div></div>';
      $('.done', box).focus();
    });
  });

  // cookie
  var ck = $('#cookie');
  if (ck && !store.get('ck-ok')) ck.hidden = false;
  ck && $('button', ck).addEventListener('click', function () { store.set('ck-ok', '1'); ck.hidden = true; });

  // что учтено по законам РФ
  var dlg = $('#law');
  $$('[data-law]').forEach(function (b) {
    b.addEventListener('click', function () { if (dlg && dlg.showModal) dlg.showModal(); });
  });
  dlg && $('.law-x', dlg).addEventListener('click', function () { dlg.close(); });
  dlg && dlg.addEventListener('click', function (e) { if (e.target === dlg) dlg.close(); });

  // фильтр врачей
  var chips = $$('[data-filter]');
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      var v = c.getAttribute('data-filter');
      chips.forEach(function (x) { x.setAttribute('aria-pressed', x === c ? 'true' : 'false'); });
      $$('[data-dir]').forEach(function (d) {
        d.hidden = v !== 'all' && d.getAttribute('data-dir').split(' ').indexOf(v) < 0;
      });
    });
  });

  // поиск по прайсу
  var ps = $('#psearch');
  ps && ps.addEventListener('input', function () {
    var q = ps.value.trim().toLowerCase();
    $$('.pgroup').forEach(function (g) {
      var any = false;
      $$('tbody tr', g).forEach(function (tr) {
        var hit = !q || tr.textContent.toLowerCase().indexOf(q) >= 0;
        tr.hidden = !hit; if (hit) any = true;
      });
      g.hidden = !any;
    });
    var none = $('#pnone'); if (none) none.hidden = $$('.pgroup').some(function (g) { return !g.hidden; });
  });
})();
