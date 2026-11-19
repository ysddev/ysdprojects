(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const ENDPOINT = /(^|\.)homuting\.ru$/.test(location.hostname) ? '/send.php' : '';

  // ---------- позиции заявки ----------
  const items = new Map(); // id -> {name, qty}
  const box = $('#items'), empty = $('#items-empty'), sel = $('#items-select');
  const cartbar = $('#cartbar'), cartN = $('#cart-n');
  const toast = $('#toast');
  const say = m => { toast.textContent = m; toast.classList.add('is-on'); clearTimeout(say.t); say.t = setTimeout(() => toast.classList.remove('is-on'), 2200); };
  const plural = n => (n % 10 === 1 && n % 100 !== 11) ? 'позиция' : (n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 10 || n % 100 >= 20)) ? 'позиции' : 'позиций';

  const render = () => {
    $$('.item', box).forEach(e => e.remove());
    items.forEach((v, id) => {
      const row = document.createElement('div');
      row.className = 'item';
      row.innerHTML = '<span></span><input type="number" min="1" step="1" inputmode="numeric" placeholder="шт." aria-label="Количество, шт."><button type="button" aria-label="Убрать позицию">×</button>';
      $('span', row).textContent = v.name;
      const q = $('input', row); q.value = v.qty || ''; q.addEventListener('input', () => { v.qty = q.value; });
      $('button', row).addEventListener('click', () => toggle(id, false));
      box.insertBefore(row, empty);
    });
    empty.hidden = items.size > 0;
    $$('.add').forEach(b => {
      const on = items.has(b.dataset.id);
      b.setAttribute('aria-pressed', on ? 'true' : 'false');
      b.textContent = on ? 'В заявке ✓' : 'В заявку';
    });
    cartN.textContent = items.size + ' ' + plural(items.size);
    updateBar();
  };
  const toggle = (id, on) => {
    const opt = $(`option[value="${id}"]`, sel);
    const name = opt ? opt.textContent : id;
    if (on === undefined) on = !items.has(id);
    if (on) { items.set(id, { name, qty: '' }); say('Добавлено в заявку: ' + name); }
    else items.delete(id);
    render();
  };
  $$('.add').forEach(b => b.addEventListener('click', () => toggle(b.dataset.id)));
  $('#items-add').addEventListener('click', () => { if (sel.value) { toggle(sel.value, true); sel.value = ''; } });

  // плавающая кнопка «к заявке»: только если есть позиции и форма не на экране
  let orderVisible = false;
  const updateBar = () => cartbar.classList.toggle('is-on', items.size > 0 && !orderVisible);
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(es => { orderVisible = es[0].isIntersecting; updateBar(); }, { threshold: 0.15 }).observe($('#order'));
  }

  // ---------- маска телефона +7 ----------
  const tel = $('#f-tel');
  const fmt = v => {
    let d = v.replace(/\D/g, '');
    if (d.startsWith('8')) d = '7' + d.slice(1);
    if (!d.startsWith('7')) d = '7' + d;
    d = d.slice(0, 11);
    const p = [d.slice(1, 4), d.slice(4, 7), d.slice(7, 9), d.slice(9, 11)];
    let s = '+7';
    if (p[0]) s += ' (' + p[0] + (p[0].length === 3 ? ')' : '');
    if (p[1]) s += ' ' + p[1];
    if (p[2]) s += '-' + p[2];
    if (p[3]) s += '-' + p[3];
    return s;
  };
  tel.addEventListener('focus', () => { if (!tel.value) tel.value = '+7 '; });
  tel.addEventListener('input', () => { tel.value = fmt(tel.value); });
  tel.addEventListener('blur', () => { if (tel.value.replace(/\D/g, '').length <= 1) tel.value = ''; });

  // ---------- форма ----------
  const form = $('#lead'), btn = $('#f-submit'), status = $('#f-status'), consent = $('#f-consent');
  const ts = $('#f-ts'); ts.value = String(Date.now());
  const sync = () => { btn.disabled = !consent.checked; };
  consent.addEventListener('change', sync); sync();

  const rules = {
    'f-name': v => v.trim().length >= 2,
    'f-tel': v => v.replace(/\D/g, '').length === 11,
    'f-email': v => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()),
  };
  const check = id => { const el = $('#' + id), ok = rules[id](el.value); el.closest('.f').classList.toggle('err', !ok); el.setAttribute('aria-invalid', ok ? 'false' : 'true'); return ok; };
  Object.keys(rules).forEach(id => $('#' + id).addEventListener('blur', () => { if ($('#' + id).value) check(id); }));

  form.addEventListener('submit', async e => {
    e.preventDefault();
    status.textContent = '';
    const bad = Object.keys(rules).filter(id => !check(id));
    if (bad.length) { $('#' + bad[0]).focus(); status.textContent = 'Проверьте выделенные поля.'; return; }
    if (!consent.checked) { status.textContent = 'Нужно согласие на обработку персональных данных.'; return; }
    const fd = new FormData(form);
    items.forEach((v, id) => { fd.append('items[]', v.name + ' — ' + (v.qty ? v.qty + ' шт.' : 'кол-во не указано')); });
    const p = new URLSearchParams(location.search);
    ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'from'].forEach(k => { if (p.get(k)) fd.append('utm[' + k + ']', p.get(k)); });
    fd.append('page', location.href);
    btn.disabled = true; btn.textContent = 'Отправляем…';
    try {
      if (ENDPOINT) {
        const r = await fetch(ENDPOINT, { method: 'POST', body: fd, headers: { Accept: 'application/json' } });
        const j = await r.json().catch(() => ({}));
        if (r.status === 429) throw Object.assign(new Error('often'), { often: true });
        if (!r.ok || !j.ok) throw new Error('bad');
      } else {
        await new Promise(r => setTimeout(r, 500)); // тестовая версия: без отправки
      }
      if (window.goal) window.goal('lead');
      form.hidden = true; $('#done').classList.add('is-on');
      items.clear(); render();
    } catch (x) {
      status.textContent = x.often ? 'Заявка уже отправлена, подождите минуту.' : 'Не удалось отправить. Позвоните или напишите на info@homuting.ru.';
      btn.textContent = 'Отправить заявку'; sync();
    }
  });

  render();
})();
