// Скриншоты обложек для карточек на ysddev.com: 1920×1080 (DPR 2) → webp 400/800/1200/1920/3840
import { chromium } from 'playwright';
import sharp from 'sharp';
import fs from 'node:fs';
import path from 'node:path';
const root = path.resolve('works'); const out = path.resolve('thumbs-out');
fs.mkdirSync(out, { recursive: true });
const only = (process.env.ONLY || '').split(',').filter(Boolean);
const slugs = fs.readdirSync(root).filter(d => fs.existsSync(path.join(root, d, 'index.html')) && (!only.length || only.includes(d)));
const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 2, reducedMotion: 'reduce', locale: 'ru-RU' });
for (const s of slugs) {
  const page = await ctx.newPage();
  try {
    // живая страница с фото (img/ качает mirror) — ждём, пока Pages отдаст свежую версию, иначе файл с диска
    const local = fs.readFileSync(path.join(root, s, 'index.html'), 'utf8');
    let url = 'file://' + path.join(root, s, 'index.html');
    for (let t = 0; t < 40; t++) {
      const live = 'https://ysdprojects.space/' + s + '/index.html?thumb=' + Date.now();
      try { const r = await fetch(live); if (r.ok && (await r.text()) === local) { url = live; break; } } catch {}
      await new Promise(r => setTimeout(r, 20000));
    }
    await page.goto(url, { waitUntil: 'networkidle', timeout: 90000 });
    await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } scrollTo(0, 0); });
    await page.evaluate(() => document.fonts && document.fonts.ready);
    await page.waitForTimeout(2500);
    const png = await page.screenshot({ type: 'png' });
    for (const w of [400, 800, 1200, 1920, 3840]) {
      await sharp(png).resize(w, Math.round(w * 9 / 16)).webp({ quality: w >= 1920 ? 78 : 80 }).toFile(path.join(out, `${s}-${w}.webp`));
    }
    // мобильный вид для проверки
    await page.setViewportSize({ width: 390, height: 844 });
    await page.waitForTimeout(800);
    await sharp(await page.screenshot({ type: 'png' })).resize(390).webp({ quality: 75 }).toFile(path.join(out, `${s}-mobile.webp`));
    console.log('ok', s);
  } catch (e) { console.log('FAIL', s, e.message); }
  await page.close();
}
await browser.close();
