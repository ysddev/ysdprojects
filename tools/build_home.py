"""Главная ysdprojects.space — только работы студии: поиск, фильтр по типу и сетка карточек со ссылками на живые проекты.

Владелец 25.11.2026 15:13: «ysdprojects.space только для наших работ должно быть, не весь сайт». До этого главная была
копией ysddev.com (цены, отзывы, заявка, телефон) со 100 работами с витрины основного сайта. Теперь здесь только
работы: все из витрины бота (profile.md + то, что бот добавляет сам), с обложками — снимками живых страниц из ветки
thumbs (их кладёт mirror.yml в img/<f>-<ширина>.webp по works.json).

Запуск:
  python3 tools/build_home.py /путь/к/ysd-dev-bot
→ home/index.html и home/works.json.
"""
from __future__ import annotations

import html
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOME = ROOT / "home"
KINDS = [("site", "Сайты"), ("shop", "Магазины"), ("design", "Дизайн"), ("bot", "Боты"), ("deck", "Презентации"),
         ("service", "Сервисы и приложения"), ("ai", "ИИ")]
ONE = {"site": "Сайт", "shop": "Интернет-магазин", "design": "Дизайн", "bot": "Бот", "deck": "Презентация",
       "service": "Веб-сервис", "ai": "ИИ-ассистент"}
METRIKA = "112490537"


def pl(n, one, few, many):
    return one if n % 10 == 1 and n % 100 != 11 else few if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14 else many


def cap(s: str) -> str:
    return s[:1].upper() + s[1:] if s else s


def works_from_bot(bot_dir: Path) -> list[dict]:
    """Работы витрины так, как их видит бот: profile.md плюс работы, которые бот дописывает сам; тип — по work_kind."""
    sys.path.insert(0, str(bot_dir))
    from app import ai as A  # noqa: E402
    prof = A.with_shop_works((bot_dir / "profile.md").read_text(encoding="utf-8"))
    out = []
    for url, desc in A._WORK_LINE_RE.findall(prof):
        if "ysdprojects.space/" not in url:
            continue
        slug = url.split("ysdprojects.space/")[-1].strip("/")
        kind = A.work_kind(url, desc)
        m = re.match(r"^(.*?)\s*\((.*)\)\s*$", desc.strip())
        t, s = (m.group(1), m.group(2)) if m else (desc.strip(), "")
        one = "Мобильное приложение" if "мобильное приложение" in desc.lower() else ONE.get(kind, "")
        out.append({"c": kind, "t": cap(t), "s": cap(s), "f": slug.replace("/", "-"), "u": f"https://ysdprojects.space/{slug}/", "o": one})
    order = {k: i for i, (k, _) in enumerate(KINDS)}
    return sorted(out, key=lambda w: order.get(w["c"], 99))  # sorted устойчив: внутри типа — порядок витрины


def card(w: dict, i: int) -> str:
    e = html.escape
    lazy = "" if i < 6 else ' loading="lazy"'
    return (f'<a class="w" href="{e(w["u"])}" target="_blank" rel="noopener" data-c="{w["c"]}" '
            f'data-q="{e((w["t"] + " " + w["s"] + " " + w.get("o", "")).lower().replace("ё", "е"))}">'
            f'<span class="ph"><img src="img/{w["f"]}-400.webp" srcset="img/{w["f"]}-400.webp 400w, img/{w["f"]}-800.webp 800w" '
            f'sizes="(max-width:640px) 100vw, (max-width:1100px) 50vw, 33vw" width="800" height="450" alt=""{lazy} decoding="async" '
            f'onerror="this.parentNode.classList.add(\'no\');this.remove()"></span>'
            f'<span class="tx"><small>{e(w.get("o", ONE.get(w["c"], "")))}</small><b>{e(w["t"])}</b>{"<span>" + e(w["s"]) + "</span>" if w["s"] else ""}</span></a>')


CSS = r"""
@font-face{font-family:"Onest";src:url(fonts/onest.woff2) format("woff2");font-weight:100 900;font-display:swap}
:root{--bg:#000;--ink:#f3f3f6;--dim:rgba(243,243,246,.62);--line:rgba(255,255,255,.12);--card:#0d0d10;--ac:#fff}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:400 16px/1.55 Onest,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}button,input{font:inherit;color:inherit}
:focus-visible{outline:2px solid #fff;outline-offset:3px;border-radius:6px}
.wrap{width:min(1320px,100% - 2*clamp(16px,4vw,48px));margin-inline:auto}
header{position:sticky;top:0;z-index:5;background:rgba(0,0,0,.82);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.bar{display:flex;align-items:center;gap:16px;height:64px}
.bar svg{width:74px;height:auto;flex:none}
.bar span{color:var(--dim);font-size:15px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.top{padding:clamp(40px,7vw,96px) 0 clamp(24px,3vw,36px)}
h1{margin:0;font-size:clamp(40px,7vw,104px);line-height:.98;letter-spacing:-.045em;font-weight:700;max-width:12em;text-wrap:balance}
.lead{margin:18px 0 0;color:var(--dim);font-size:clamp(17px,1.6vw,20px);max-width:44em}
.ctl{position:sticky;top:64px;z-index:4;background:rgba(0,0,0,.9);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);padding:14px 0;border-bottom:1px solid var(--line)}
.ctl .wrap{display:flex;gap:12px;align-items:center}
.chips{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;flex:1 1 auto;min-width:0}.chips::-webkit-scrollbar{display:none}
.chips button{background:transparent;border:1px solid var(--line);border-radius:999px;padding:9px 15px;white-space:nowrap;cursor:pointer;font-size:15px;transition:background .2s,border-color .2s}
.chips button:hover{border-color:rgba(255,255,255,.4)}
.chips button[aria-pressed=true]{background:#fff;color:#000;border-color:#fff}
.chips em{font-style:normal;opacity:.55;margin-left:6px}
.find{position:relative;flex:0 0 280px}
.find input{width:100%;background:#0d0d10;border:1px solid var(--line);border-radius:999px;padding:10px 16px;font-size:15px}
.find input::placeholder{color:var(--dim)}
.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(14px,2vw,24px);padding:clamp(22px,3vw,36px) 0 64px}
.w{display:flex;flex-direction:column;text-decoration:none;border-radius:16px;background:var(--card);border:1px solid var(--line);overflow:hidden;transition:border-color .25s,transform .25s}
.w:hover{border-color:rgba(255,255,255,.35);transform:translateY(-2px)}
.ph{display:block;aspect-ratio:16/9;background:#16161b;overflow:hidden}
.ph img{width:100%;height:100%;object-fit:cover;object-position:top;display:block;transition:transform .5s}
.w:hover .ph img{transform:scale(1.03)}
.ph.no{background:linear-gradient(135deg,#1b1b22,#0d0d10)}
.tx{display:grid;gap:4px;padding:14px 16px 18px}
.tx small{font-size:14px;color:var(--dim)}
.tx b{font-size:17px;font-weight:600;line-height:1.3}
.tx span{font-size:14px;color:var(--dim);line-height:1.45}
.empty{padding:40px 0 80px;color:var(--dim);font-size:17px}
footer{border-top:1px solid var(--line);padding:28px 0 40px;font-size:14px;color:var(--dim)}
footer .wrap{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
footer a{color:var(--dim)}
.cc{position:fixed;left:16px;right:16px;bottom:16px;z-index:9;max-width:560px;margin-inline:auto;background:#111116;border:1px solid var(--line);border-radius:16px;padding:16px;font-size:14px;color:var(--dim);display:none}
.cc.on{display:block}.cc p{margin:0 0 12px}.cc a{color:var(--ink)}
.cc div{display:flex;gap:8px;flex-wrap:wrap}.cc button{border:1px solid var(--line);background:transparent;border-radius:999px;padding:9px 14px;cursor:pointer;font-size:14px}
.cc button.y{background:#fff;color:#000;border-color:#fff}
@media (max-width:1100px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:900px){.ctl .wrap{flex-wrap:wrap}.find{flex:1 1 100%}}
@media (max-width:640px){.grid{grid-template-columns:1fr}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

JS = r"""
(function(){
var cur='all',q='',G=document.getElementById('grid'),W=[].slice.call(G.children),E=document.getElementById('empty'),C=document.getElementById('chips');
function norm(s){return s.toLowerCase().replace(/ё/g,'е').trim()}
/* «кофейня» находит и «кофеен»: сравниваем по началу слова без окончания */
function stem(w){return w.length<5?w:w.slice(0,Math.max(4,w.length-3))}
function apply(){var n=0;W.forEach(function(a){var ok=(cur==='all'||a.dataset.c===cur)&&(!q||q.split(/\s+/).every(function(w){return a.dataset.q.indexOf(stem(w))>=0}));
 a.hidden=!ok;if(ok)n++});E.hidden=n>0;try{history.replaceState(null,'',cur==='all'?location.pathname:'#'+cur)}catch(e){}}
C.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;cur=b.dataset.k;
 C.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});apply()});
document.getElementById('q').addEventListener('input',function(e){q=norm(e.target.value);apply()});
var h=location.hash.slice(1),b=h&&C.querySelector('button[data-k="'+h+'"]');if(b)b.click();
/* Яндекс Метрика — только после согласия на куки */
var K='ysd-cc',cc=document.getElementById('cc'),v=null;try{v=localStorage.getItem(K)}catch(e){}
function start(){window.ym=window.ym||function(){(window.ym.a=window.ym.a||[]).push(arguments)};window.ym.l=+new Date;
 var s=document.createElement('script');s.async=1;s.src='https://mc.yandex.ru/metrika/tag.js';document.head.appendChild(s);
 ym(METRIKA_ID,'init',{clickmap:true,trackLinks:true,accurateTrackBounce:true})}
if(v==='yes')start();else if(v!=='no')cc.classList.add('on');
function set(x){try{localStorage.setItem(K,x)}catch(e){}cc.classList.remove('on');if(x==='yes')start()}
document.getElementById('ccY').onclick=function(){set('yes')};document.getElementById('ccN').onclick=function(){set('no')};
})();
"""


def build(bot_dir: Path) -> None:
    works = works_from_bot(bot_dir)
    n = len(works)
    cnt = Counter(w["c"] for w in works)
    mark = re.sub(r"\s+", " ", (HOME / "ysdmk-symbol.svg").read_text(encoding="utf-8")).strip()
    mark = mark.replace('<symbol id="ysdmk" viewBox="0 0 2346 852">', '<svg viewBox="0 0 2346 852" aria-label="YSD DEV" role="img">').replace("</symbol>", "</svg>")
    title = f"{n} {pl(n, 'работа', 'работы', 'работ')} студии YSD DEV"
    desc = (f"{n} живых проектов студии YSD DEV: сайты, интернет-магазины, боты, презентации и дизайн. "
            "Каждый открывается и работает — не скриншоты.")
    chips = (f'<button type="button" data-k="all" aria-pressed="true">Все<em>{n}</em></button>'
             + "".join(f'<button type="button" data-k="{k}" aria-pressed="false">{t}<em>{cnt[k]}</em></button>' for k, t in KINDS if cnt[k]))
    page = f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{html.escape(title)} — живые проекты</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="https://ysdprojects.space/">
<meta name="theme-color" content="#000000">
<meta property="og:type" content="website">
<meta property="og:url" content="https://ysdprojects.space/">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" type="image/png" sizes="96x96" href="/icon-96.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="fonts/onest.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap bar">{mark}<span>Работы студии</span></div></header>
<main>
<section class="wrap top"><h1>{html.escape(title)}</h1>
<p class="lead">Не скриншоты, а работающие проекты: посчитайте в калькуляторе, положите товар в корзину, пройдите сценарий бота, листайте слайды.
Нажмите на карточку — проект откроется в новой вкладке.</p></section>
<div class="ctl"><div class="wrap"><div class="chips" id="chips" role="group" aria-label="Тип работы">{chips}</div>
<label class="find"><input id="q" type="search" placeholder="Поиск: кофейня, стоматология" aria-label="Поиск по работам"></label></div></div>
<div class="wrap"><div class="grid" id="grid">{"".join(card(w, i) for i, w in enumerate(works))}</div>
<p class="empty" id="empty" hidden>Ничего не нашлось. Попробуйте другое слово или выберите «Все».</p></div>
</main>
<footer><div class="wrap"><span>© 2026 YSD DEV</span><a href="https://ysddev.com/" target="_blank" rel="noopener">Разработан с душой студией YSD DEV</a></div></footer>
<div class="cc" id="cc" role="region" aria-label="Куки"><p>Сайт использует куки и Яндекс Метрику, чтобы понимать, какие работы смотрят. Метрика включится только после согласия.
<a href="https://ysddev.com/privacy.html#cookie" target="_blank" rel="noopener">Подробнее</a></p>
<div><button type="button" id="ccN">Только необходимые</button><button type="button" class="y" id="ccY">Принять</button></div></div>
<script>{JS.replace("METRIKA_ID", METRIKA)}</script>
</body>
</html>
"""
    (HOME / "index.html").write_text(page, encoding="utf-8")
    # mirror.yml копирует обложки из ветки thumbs в img/<f>-<ширина>.webp по этому списку
    (HOME / "works.json").write_text(json.dumps(works, ensure_ascii=False, indent=1), encoding="utf-8")
    print("работ:", n, dict(cnt))


if __name__ == "__main__":
    build(Path(sys.argv[1] if len(sys.argv) > 1 else "../ysd-dev-bot").resolve())
