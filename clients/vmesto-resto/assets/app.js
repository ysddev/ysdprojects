(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  // Показать / скрыть пароль
  $$('[data-pw]').forEach(function (b) {
    b.addEventListener('click', function () {
      var i = b.parentNode.querySelector('input');
      var show = i.type === 'password';
      i.type = show ? 'text' : 'password';
      b.setAttribute('aria-label', show ? 'Скрыть пароль' : 'Показать пароль');
    });
  });

  // Опасные действия — в два нажатия, без всплывающих окон браузера
  $$('[data-confirm]').forEach(function (b) {
    var orig = b.innerHTML, t;
    b.addEventListener('click', function (e) {
      if (b.classList.contains('armed')) return;
      e.preventDefault();
      b.classList.add('armed');
      b.textContent = b.getAttribute('data-confirm');
      clearTimeout(t);
      t = setTimeout(function () { b.classList.remove('armed'); b.innerHTML = orig; }, 4000);
    });
  });

  $$('[data-print]').forEach(function (b) { b.addEventListener('click', function () { window.print(); }); });

  // Списки, которые применяются сразу
  $$('[data-autosubmit]').forEach(function (s) {
    s.addEventListener('change', function () { s.form.submit(); });
  });

  // Логин из ФИО: «Смирнова Анна» → anna.smirnova (если табельного нет)
  var src = $('[data-login-src]'), dst = $('[data-login-dst]'), tab = $('[data-tab-src]');
  if (src && dst) {
    var touched = dst.value !== '';
    dst.addEventListener('input', function () { touched = true; });
    var map = {а:'a',б:'b',в:'v',г:'g',д:'d',е:'e',ё:'e',ж:'zh',з:'z',и:'i',й:'y',к:'k',л:'l',м:'m',н:'n',о:'o',п:'p',р:'r',с:'s',т:'t',у:'u',ф:'f',х:'h',ц:'ts',ч:'ch',ш:'sh',щ:'sch',ъ:'',ы:'y',ь:'',э:'e',ю:'yu',я:'ya'};
    var tr = function (s) { return s.toLowerCase().split('').map(function (c) { return map[c] !== undefined ? map[c] : c; }).join('').replace(/[^a-z0-9]/g, ''); };
    var suffix = dst.getAttribute('data-suffix') || '';
    var fill = function () {
      if (touched) return;
      var t = tab ? tab.value.trim().toLowerCase().replace(/[^a-z0-9._-]/g, '') : '';
      if (t) { dst.value = t + suffix; return; }
      var p = src.value.trim().split(/\s+/);
      dst.value = [tr(p[1] || ''), tr(p[0] || '')].filter(Boolean).join('.');
    };
    src.addEventListener('input', fill);
    if (tab) tab.addEventListener('input', fill);
  }

  // ---------- Меню и корзина ----------
  var form = $('#order');
  if (!form) return;
  var cards = $$('.meal-card', form);
  var cart = $('#cart'), bar = $('.cartbar'), scrim = $('.scrim');
  var max = parseInt(form.getAttribute('data-max'), 10) || 0;
  var already = parseInt(form.getAttribute('data-already'), 10) || 0;
  var each = form.hasAttribute('data-each'); // лимит компании: каждая позиция не больше одной
  var submit = $('[data-submit]', cart);
  var isAdmin = submit.hasAttribute('data-admin');
  var fmt = function (kop) {
    var r = Math.floor(kop / 100), k = kop % 100;
    return String(r).replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + (k ? ',' + (k < 10 ? '0' : '') + k : '') + ' ₽';
  };
  var plural = function (n, a, b, c) { var n10 = n % 10, n100 = n % 100; return n10 === 1 && n100 !== 11 ? a : (n10 >= 2 && n10 <= 4 && (n100 < 10 || n100 >= 20) ? b : c); };

  function update() {
    var lines = [], total = 0, count = 0;
    cards.forEach(function (c) {
      var inp = $('input[type=hidden]', c);
      if (!inp) return;
      var q = Math.max(0, Math.min(each ? 1 : 20, parseInt(inp.value, 10) || 0));
      inp.value = q;
      $('output', c).textContent = q;
      c.classList.toggle('in', q > 0);
      if (q > 0) {
        var p = parseInt(c.getAttribute('data-price'), 10);
        lines.push([c.getAttribute('data-title'), q, p * q]);
        total += p * q; count += q;
      }
    });
    var ul = $('[data-lines]', cart);
    ul.innerHTML = '';
    lines.forEach(function (l) {
      var li = document.createElement('li');
      var a = document.createElement('span'); a.textContent = l[0] + ' × ' + l[1];
      var b = document.createElement('b'); b.textContent = fmt(l[2]);
      li.appendChild(a); li.appendChild(b); ul.appendChild(li);
    });
    $('[data-empty]', cart).hidden = count > 0;
    $('[data-total]', cart).textContent = fmt(total);
    var over = max > 0 && already + count > max;
    var full = max > 0 && already + count >= max;
    // Лимит набран — остальные «В корзину» гаснут, «+» у выбранных тоже
    cards.forEach(function (c) {
      var inp = $('input[type=hidden]', c);
      if (!inp) return;
      var q = parseInt(inp.value, 10) || 0;
      var add = $('[data-add]', c), plus = $('[data-plus]', c);
      if (add) add.disabled = full && q === 0;
      if (plus) plus.disabled = full || (each && q >= 1);
    });
    var lim = $('[data-limit]', cart);
    lim.hidden = !over;
    if (over) lim.textContent = 'На день можно не больше ' + max + ' ' + plural(max, 'позиции', 'позиций', 'позиций') + (already ? ' (уже заказано ' + already + ')' : '') + '.';
    else if (full && count > 0) { lim.hidden = false; lim.textContent = max === 1 ? 'Одна позиция в день — уже выбрана.' : 'Лимит на день набран: ' + max + ' ' + plural(max, 'позиция', 'позиции', 'позиций') + '.'; }
    submit.disabled = count === 0 || over || isAdmin;
    var words = count + ' ' + plural(count, 'позиция', 'позиции', 'позиций');
    if (bar) {
      bar.classList.toggle('on', count > 0);
      $('[data-bar-count]', bar).textContent = words;
      $('[data-bar-total]', bar).textContent = fmt(total);
    }
    var hc = $('[data-head-count]');
    if (hc) hc.textContent = count;
    if (count === 0) closeCart();
  }

  cards.forEach(function (c) {
    var inp = $('input[type=hidden]', c);
    if (!inp) return;
    var set = function (d) { inp.value = (parseInt(inp.value, 10) || 0) + d; update(); };
    $('[data-add]', c).addEventListener('click', function () { set(1); var p = $('[data-plus]', c); if (p) p.focus(); });
    $('[data-plus]', c).addEventListener('click', function () { set(1); });
    $('[data-minus]', c).addEventListener('click', function () { set(-1); if (inp.value === '0') $('[data-add]', c).focus(); });
  });

  // Фильтр по разделам меню
  $$('.chip[data-cat]').forEach(function (ch) {
    ch.addEventListener('click', function () {
      var cat = ch.getAttribute('data-cat');
      $$('.chip[data-cat]').forEach(function (x) { x.setAttribute('aria-pressed', x === ch ? 'true' : 'false'); });
      $$('[data-section]', form).forEach(function (s) { s.hidden = !!cat && s.getAttribute('data-section') !== cat; });
    });
  });

  // Нижняя шторка на телефоне
  function openCart() { cart.classList.add('open'); if (scrim) scrim.classList.add('on'); }
  function closeCart() { cart.classList.remove('open'); if (scrim) scrim.classList.remove('on'); }
  $$('[data-cart-open]').forEach(function (b) {
    b.addEventListener('click', function () {
      if (window.matchMedia('(max-width: 980px)').matches) openCart();
      else cart.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
  $$('[data-cart-close]').forEach(function (b) { b.addEventListener('click', closeCart); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeCart(); });

  // Защита от двойной отправки
  form.addEventListener('submit', function () {
    setTimeout(function () { submit.disabled = true; submit.textContent = 'Отправляем…'; }, 0);
  });

  update();
})();
