// Оплата урока «Крашу сама» через ЮKassa — Yandex Cloud Function (Node.js 18+), без зависимостей.
// Переменные окружения (задаются в настройках функции, НЕ в коде):
//   YK_SHOP_ID     — shopId из ЮKassa
//   YK_SECRET      — секретный ключ live_…
//   TOKEN_SECRET   — любая длинная случайная строка (подпись ссылки доступа)
//   SITE           — адрес сайта, напр. https://ysdprojects.space/clients/kraschu
//   SEND_RECEIPT   — "1", если в ЮKassa подключены чеки (54-ФЗ), иначе "0"
const crypto = require('crypto');
const ITEMS = {
  lesson:  { value: '2990.00', title: 'Видеоурок «Крашу сама»' },
  consult: { value: '5990.00', title: 'Личная консультация колориста' },
};
const CORS = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': 'Content-Type', 'Access-Control-Allow-Methods': 'GET,POST,OPTIONS', 'Content-Type': 'application/json; charset=utf-8' };
const reply = (code, obj) => ({ statusCode: code, headers: CORS, body: JSON.stringify(obj) });
const auth = () => 'Basic ' + Buffer.from(process.env.YK_SHOP_ID + ':' + process.env.YK_SECRET).toString('base64');
const sign = (s) => crypto.createHmac('sha256', process.env.TOKEN_SECRET).update(s).digest('base64url').slice(0, 32);

async function yk(path, opts = {}) {
  const r = await fetch('https://api.yookassa.ru/v3' + path, { ...opts, headers: { Authorization: auth(), 'Content-Type': 'application/json', ...(opts.headers || {}) } });
  const j = await r.json(); if (!r.ok) throw new Error(j.description || ('ЮKassa ' + r.status)); return j;
}

module.exports.handler = async (event) => {
  if (event.httpMethod === 'OPTIONS') return reply(200, {});
  try {
    const q = event.queryStringParameters || {};
    // 1) создать платёж
    if (event.httpMethod === 'POST') {
      const b = JSON.parse(event.isBase64Encoded ? Buffer.from(event.body, 'base64').toString() : (event.body || '{}'));
      const it = ITEMS[b.item] || ITEMS.lesson;
      const email = String(b.email || '').trim().slice(0, 100);
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return reply(400, { error: 'Проверьте почту' });
      const body = {
        amount: { value: it.value, currency: 'RUB' }, capture: true,
        confirmation: { type: 'redirect', return_url: process.env.SITE + '/' + (b.item === 'consult' ? 'pay.html?item=consult&done=1' : 'lesson.html?check=1') },
        description: it.title, metadata: { item: b.item || 'lesson', email },
      };
      if (process.env.SEND_RECEIPT === '1') body.receipt = { customer: { email }, items: [{ description: it.title, quantity: '1.00', amount: { value: it.value, currency: 'RUB' }, vat_code: 1, payment_mode: 'full_payment', payment_subject: 'service' }] };
      const p = await yk('/payments', { method: 'POST', headers: { 'Idempotence-Key': crypto.randomUUID() }, body: JSON.stringify(body) });
      return reply(200, { id: p.id, url: p.confirmation.confirmation_url });
    }
    // 2) проверить оплату и выдать ключ доступа
    if (q.id) {
      if (!/^[0-9a-f-]{36}$/.test(q.id)) return reply(400, { error: 'bad id' });
      const p = await yk('/payments/' + q.id);
      if (p.status !== 'succeeded') return reply(200, { status: p.status });
      const t = p.id + '.' + sign(p.id);
      return reply(200, { status: 'succeeded', token: t, item: (p.metadata || {}).item, email: (p.metadata || {}).email });
    }
    // 3) проверить ключ доступа (ссылка «вернуться к уроку»)
    if (q.t) {
      const [id, s] = String(q.t).split('.');
      return reply(200, { ok: !!id && s === sign(id) });
    }
    return reply(404, { error: 'not found' });
  } catch (e) { return reply(500, { error: e.message }); }
};
