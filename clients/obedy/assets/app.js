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
      b.textContent = show ? 'Скрыть' : 'Показать';
    });
  });

  // Опасные действия — в два нажатия, без всплывающих окон браузера
  $$('[data-confirm]').forEach(function (b) {
    var orig = b.textContent, t;
    b.addEventListener('click', function (e) {
      if (b.classList.contains('armed')) return;
      e.preventDefault();
      b.classList.add('armed');
      b.textContent = b.getAttribute('data-confirm');
      clearTimeout(t);
      t = setTimeout(function () { b.classList.remove('armed'); b.textContent = orig; }, 4000);
    });
  });

  // Списки, которые применяются сразу
  $$('[data-autosubmit]').forEach(function (s) {
    s.addEventListener('change', function () { s.form.submit(); });
  });

  // Логин из ФИО: «Смирнова Анна» → anna.smirnova
  var src = $('[data-login-src]'), dst = $('[data-login-dst]');
  if (src && dst) {
    var touched = dst.value !== '';
    dst.addEventListener('input', function () { touched = true; });
    var map = {а:'a',б:'b',в:'v',г:'g',д:'d',е:'e',ё:'e',ж:'zh',з:'z',и:'i',й:'y',к:'k',л:'l',м:'m',н:'n',о:'o',п:'p',р:'r',с:'s',т:'t',у:'u',ф:'f',х:'h',ц:'ts',ч:'ch',ш:'sh',щ:'sch',ъ:'',ы:'y',ь:'',э:'e',ю:'yu',я:'ya'};
    var tr = function (s) { return s.toLowerCase().split('').map(function (c) { return map[c] !== undefined ? map[c] : c; }).join('').replace(/[^a-z0-9]/g, ''); };
    src.addEventListener('input', function () {
      if (touched) return;
      var p = src.value.trim().split(/\s+/);
      dst.value = [tr(p[1] || ''), tr(p[0] || '')].filter(Boolean).join('.');
    });
  }

  // ---------- Меню и судок ----------
  var form = $('#order');
  if (!form) return;
  var cards = $$('.card', form);
  var cart = $('#cart'), bar = $('.cartbar'), scrim = $('.scrim');
  var max = parseInt(form.getAttribute('data-max'), 10) || 0;
  var already = parseInt(form.getAttribute('data-already'), 10) || 0;
  var fmt = function (kop) {
    var r = Math.floor(kop / 100), k = kop % 100;
    return String(r).replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + (k ? ',' + (k < 10 ? '0' : '') + k : '') + ' ₽';
  };
  var plural = function (n, a, b, c) { var n10 = n % 10, n100 = n % 100; return n10 === 1 && n100 !== 11 ? a : (n10 >= 2 && n10 <= 4 && (n100 < 10 || n100 >= 20) ? b : c); };

  function update() {
    var lines = [], total = 0, count = 0;
    cards.forEach(function (c) {
      var inp = $('input', c), q = Math.max(0, Math.min(20, parseInt(inp.value, 10) || 0));
      inp.value = q;
      var step = $('.step', c);
      step.classList.toggle('zero', q === 0);
      $('.minus', c).disabled = q === 0;
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
    var lim = $('[data-limit]', cart);
    lim.hidden = !over;
    if (over) lim.textContent = 'На день можно не больше ' + max + ' ' + plural(max, 'обеда', 'обедов', 'обедов') + (already ? ' (уже заказано ' + already + ')' : '') + '.';
    $('[data-submit]', cart).disabled = count === 0 || over || !!$('[data-submit]', cart).title;
    if (bar) {
      bar.classList.toggle('on', count > 0);
      $('[data-bar-count]', bar).textContent = count + ' ' + plural(count, 'обед', 'обеда', 'обедов');
      $('[data-bar-total]', bar).textContent = fmt(total);
    }
    if (count === 0) closeCart();
  }

  cards.forEach(function (c) {
    var inp = $('input', c);
    $('.plus', c).addEventListener('click', function () { inp.value = (parseInt(inp.value, 10) || 0) + 1; update(); });
    $('.minus', c).addEventListener('click', function () { inp.value = (parseInt(inp.value, 10) || 0) - 1; update(); });
    inp.addEventListener('change', update);
  });

  // Фильтр по меткам
  $$('.chip').forEach(function (ch) {
    ch.addEventListener('click', function () {
      var tag = ch.getAttribute('data-tag');
      $$('.chip').forEach(function (x) { x.setAttribute('aria-pressed', x === ch ? 'true' : 'false'); });
      cards.forEach(function (c) {
        var tags = (c.getAttribute('data-tags') || '').split(',');
        c.hidden = !!tag && tags.indexOf(tag) < 0 && !c.classList.contains('in');
      });
    });
  });

  // Нижняя шторка на телефоне
  function openCart() { cart.classList.add('open'); scrim && scrim.classList.add('on'); }
  function closeCart() { cart.classList.remove('open'); scrim && scrim.classList.remove('on'); }
  $$('[data-cart-open]').forEach(function (b) { b.addEventListener('click', openCart); });
  $$('[data-cart-close]').forEach(function (b) { b.addEventListener('click', closeCart); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeCart(); });

  // Защита от двойной отправки
  form.addEventListener('submit', function () {
    var b = $('[data-submit]', cart);
    setTimeout(function () { b.disabled = true; b.textContent = 'Отправляем…'; }, 0);
  });

  update();
})();
