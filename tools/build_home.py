"""Главная ysdprojects.space: витрина живых проектов YSD DEV в стиле ysddev.com.

Данные — home/works.json (порядок = спрос клиентов, как на ysddev.com), картинки home/img/{f}-400|800.webp.
Запуск: python3 tools/build_home.py → home/index.html (его копирует mirror.yml в корень gh-pages).
"""
from __future__ import annotations

import html
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOME = ROOT / "home"
CATS = [("all", "Все"), ("site", "Сайты"), ("bot", "Telegram-боты"), ("deck", "Презентации"),
        ("software", "Программы"), ("design", "Дизайн")]
CAT_NAME = dict(CATS)
FIRST = 12  # карточек сразу, остальные — «Показать ещё» (владелец 09.11: на первом экране только лучшие)
# Витрина — 30 лучших работ в этом порядке; остальные страницы живы по прямым ссылкам (их шлёт бот), но не в витрине.
CURATED = [
    "shop", "cleaning", "bots/food", "kuhni", "stroy", "salon", "miniapp", "metall", "remont", "detailing",
    "medcenter", "dental",  # первый экран: 10 премиальных сайтов + 2 бота
    "apps/crm", "slides/edu", "bots/beauty", "assistant", "online", "realty", "law", "psy", "furniture", "cosmo", "barber", "nails", "pizza", "fitness",
    "avtoshkola", "okna", "pereezd", "hotel", "kids", "english", "buh", "logistics",
    "vet", "massage", "interior", "bakery", "catering",
    "apps/warehouse", "slides/tender", "bots/ai", "garage", "resto", "design/nord", "apps/bi", "slides/pitch",
    "design/terra",
]
TG = "https://t.me/ysd_dev_bot?start=ysdprojects"
SITE = "https://ysddev.com/"


def card(w: dict, k: int) -> str:
    e = html.escape
    f = e(w["f"])
    dup = {"сайт", "telegram", "бот", "презентация", "дизайн", "программа"}
    tags = "".join(f"<i>{e(t)}</i>" for t in [t for t in (w.get("g") or []) if t.lower() not in dup][:2])
    hidden = ' hidden' if k >= FIRST else ''
    return (f'<a class="w" href="{e(w["u"])}" data-c="{e(w["c"])}" style="--k:{k % 12}"{hidden}>'
            f'<span class="ph"><img src="img/{f}-400.webp" srcset="img/{f}-400.webp 400w, img/{f}-800.webp 800w" '
            f'sizes="(max-width:720px) 92vw, (max-width:1100px) 46vw, 30vw" alt="{e(w["t"])}" '
            f'loading="{"eager" if k < 6 else "lazy"}" decoding="async" width="800" height="450">'
            f'<b class="lv"><s></s>онлайн</b><b class="op">Открыть ↗</b></span>'
            f'<span class="meta"><em>{e(CAT_NAME.get(w["c"], ""))}</em>{tags}</span>'
            f'<strong>{e(w["t"])}</strong><span class="d">{e(w["s"])}</span></a>')


def build() -> str:
    every = json.loads((HOME / "works.json").read_text(encoding="utf-8"))
    by_slug = {w["u"].split("ysdprojects.space/")[-1].strip("/"): w for w in every}
    missing = [c for c in CURATED if c not in by_slug]
    assert not missing, f"нет в works.json: {missing}"
    works = [by_slug[c] for c in CURATED]
    cnt = Counter(w["c"] for w in works)
    logo = (HOME / "ysdmk-symbol.svg").read_text(encoding="utf-8").strip()
    filters = "".join(
        f'<button type="button" data-f="{c}" aria-pressed="{"true" if c == "all" else "false"}">{n}'
        f'<sup>{len(works) if c == "all" else cnt.get(c, 0)}</sup></button>'
        for c, n in CATS if c == "all" or cnt.get(c))
    cards = "".join(card(w, i) for i, w in enumerate(works))
    def pl(n, one, few, many):  # 21 живой проект, 33 живых проекта, 30 живых проектов
        return one if n % 10 == 1 and n % 100 != 11 else few if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14 else many
    n_all, n_site = len(works), cnt.get("site", 0)
    stats = [(n_all, pl(n_all, "живой проект", "живых проекта", "живых проектов")),
             (n_site, pl(n_site, "сайт", "сайта", "сайтов")),
             (cnt.get("bot", 0) + cnt.get("software", 0), "ботов и программ"), ("24/7", "открыты онлайн")]
    stats_html = "".join(f"<div><b>{v}</b><span>{t}</span></div>" for v, t in stats)
    return TEMPLATE.replace("{{LOGO}}", logo).replace("{{FILTERS}}", filters).replace("{{CARDS}}", cards) \
        .replace("{{STATS}}", stats_html).replace("{{TOTAL}} работающих проектов", f"{n_all} {pl(n_all, 'работающий проект', 'работающих проекта', 'работающих проектов')}").replace("{{TOTAL}}", str(n_all)).replace("{{FIRST}}", str(FIRST)) \
        .replace("{{TG}}", TG).replace("{{SITE}}", SITE)


TEMPLATE = r"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>YSD DEV — живые проекты</title>
<meta name="description" content="{{TOTAL}} работающих проектов студии YSD DEV: сайты, интернет-магазины, Telegram-боты, презентации и программы. Каждый открывается и работает.">
<meta name="theme-color" content="#000000">
<link rel="canonical" href="https://ysdprojects.space/">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="favicon-48.png" sizes="48x48">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="YSD DEV — живые проекты">
<meta property="og:description" content="Сайты, боты и презентации, которые можно открыть и потрогать.">
<meta property="og:url" content="https://ysdprojects.space/">
<meta property="og:image" content="https://ysdprojects.space/img/105-800.webp">
<link rel="preload" href="onest.woff2" as="font" type="font/woff2" crossorigin>
<style>
@font-face{font-family:"Onest";src:url(onest.woff2) format("woff2");font-weight:100 900;font-display:swap}
:root{--bg:#000;--ink:#fff;--dim:#8a8a8a;--line:rgba(255,255,255,.14);--card:rgba(255,255,255,.035);--card-h:rgba(255,255,255,.07);
--f:"Onest",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--m:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,"Liberation Mono",monospace;--pad:clamp(16px,5vw,72px)}
*{box-sizing:border-box}
html{background:var(--bg);color-scheme:dark;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--f);-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit}
.field{position:fixed;inset:0;z-index:0;pointer-events:none}
.glow{position:absolute;left:50%;top:-30vh;width:120vmax;height:100vmax;transform:translateX(-50%);background:radial-gradient(closest-side,rgba(255,255,255,.10),transparent 70%)}
.grid{position:absolute;inset:-2px;background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);background-size:72px 72px;opacity:.28;-webkit-mask-image:radial-gradient(120% 90% at 50% 0%,#000 0%,transparent 72%);mask-image:radial-gradient(120% 90% at 50% 0%,#000 0%,transparent 72%)}
.noise{position:absolute;inset:0;opacity:.045;mix-blend-mode:screen;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.wrap{position:relative;z-index:1;max-width:1320px;margin:0 auto;padding:0 var(--pad)}
header{position:sticky;top:0;z-index:20;backdrop-filter:blur(14px) saturate(1.2);-webkit-backdrop-filter:blur(14px) saturate(1.2);background:rgba(0,0,0,.55);border-bottom:1px solid transparent;transition:border-color .3s}
header.sc{border-bottom-color:var(--line)}
.bar{display:flex;align-items:center;gap:22px;height:68px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none}
.brand .mk{height:22px;width:auto;color:#fff;transition:filter .4s}
.brand:hover .mk{filter:drop-shadow(0 0 10px rgba(255,255,255,.55))}
.brand span{font-family:var(--m);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--dim);padding-left:12px;border-left:1px solid var(--line)}
.sp{flex:1}
.links{display:flex;gap:26px;font-size:14px}
.links a{text-decoration:none;color:#cfcfcf;transition:color .2s}
.links a:hover{color:#fff}
.btn{display:inline-flex;align-items:center;gap:8px;height:42px;padding:0 20px;border-radius:999px;background:#fff;color:#000;font:600 14px/1 var(--f);letter-spacing:-.01em;text-decoration:none;border:1px solid #fff;transition:transform .15s,box-shadow .3s;white-space:nowrap}
.btn:hover{transform:translateY(-1px);box-shadow:0 0 0 6px rgba(255,255,255,.08),0 10px 40px -10px rgba(255,255,255,.5)}
.btn.ghost{background:transparent;color:#fff;border-color:var(--line)}
.btn.ghost:hover{border-color:#fff;box-shadow:none}
.hero{padding:clamp(56px,11vh,120px) 0 clamp(36px,6vh,64px)}
.eyebrow{font-family:var(--m);font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:#fff;display:flex;align-items:center;gap:12px;margin:0 0 26px}
.eyebrow::before{content:"";width:28px;height:1px;background:var(--dim)}
.eyebrow s{width:9px;height:9px;border-radius:50%;background:#3ddc84;box-shadow:0 0 0 0 rgba(61,220,132,.6);animation:pulse 2s infinite;text-decoration:none}
h1{font-size:clamp(38px,7.4vw,90px);line-height:.98;letter-spacing:-.045em;font-weight:700;margin:0 0 22px;max-width:15ch;background:linear-gradient(180deg,#fff 40%,#9d9da4 120%);-webkit-background-clip:text;background-clip:text;color:transparent}
.lead{font-size:clamp(16px,1.6vw,19px);line-height:1.55;color:#bdbdbd;max-width:56ch;margin:0 0 34px}
.cta{display:flex;flex-wrap:wrap;gap:12px}
.stats{display:grid;grid-template-columns:repeat(4,1fr);margin-top:clamp(44px,7vh,72px);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats div{padding:22px 0 22px 22px;border-left:1px solid var(--line)}
.stats div:first-child{border-left:0;padding-left:0}
.stats b{display:block;font-size:clamp(28px,3.4vw,44px);font-weight:600;letter-spacing:-.04em;line-height:1}
.stats span{display:block;margin-top:8px;font-family:var(--m);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--dim)}
section{padding:clamp(40px,7vh,72px) 0;scroll-margin-top:60px}
.head{display:flex;align-items:flex-end;justify-content:space-between;gap:24px;flex-wrap:wrap}
h2{font-size:clamp(30px,4.4vw,54px);line-height:1;letter-spacing:-.04em;font-weight:700;margin:0;background:linear-gradient(180deg,#fff 30%,#a6a6ac 115%);-webkit-background-clip:text;background-clip:text;color:transparent}
.filters{display:flex;flex-wrap:wrap;gap:9px;margin-top:30px}
.filters button{font:500 14px/1 var(--f);color:#d6d6d6;background:var(--card);border:1px solid var(--line);border-radius:999px;padding:11px 16px;cursor:pointer;transition:background .2s,color .2s,border-color .2s}
.filters button:hover{border-color:rgba(255,255,255,.4);color:#fff}
.filters button[aria-pressed=true]{background:#fff;color:#000;border-color:#fff}
.filters sup{font-family:var(--m);font-size:10px;margin-left:6px;opacity:.6;vertical-align:2px}
.works{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(14px,2vw,26px);margin-top:34px}
.w{display:flex;flex-direction:column;text-decoration:none;border-radius:16px;padding:10px 10px 18px;background:var(--card);border:1px solid rgba(255,255,255,.07);transition:background .3s,border-color .3s,transform .3s;animation:rise .8s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--k,0)*55ms)}
.w[hidden]{display:none}
.w:hover{background:var(--card-h);border-color:rgba(255,255,255,.18);transform:translateY(-3px)}
.ph{position:relative;display:block;aspect-ratio:16/9;border-radius:11px;overflow:hidden;background:#0d0d10}
.ph img{width:100%;height:100%;object-fit:cover;object-position:top;display:block;transition:transform .9s cubic-bezier(.2,.8,.2,1)}
.w:hover .ph img{transform:scale(1.04)}
.lv{position:absolute;left:10px;top:10px;display:flex;align-items:center;gap:6px;padding:5px 9px;border-radius:999px;background:rgba(10,10,12,.72);color:#fff;font:500 10.5px/1 var(--m);letter-spacing:.14em;text-transform:uppercase;backdrop-filter:blur(6px)}
.lv s{width:6px;height:6px;border-radius:50%;background:#3ddc84}
.op{position:absolute;right:10px;bottom:10px;background:#fff;color:#000;border-radius:999px;padding:8px 13px;font:600 12.5px/1 var(--f);opacity:0;transform:translateY(6px);transition:opacity .25s,transform .25s;box-shadow:0 8px 24px -8px rgba(0,0,0,.7)}
.w:hover .op,.w:focus-visible .op{opacity:1;transform:none}
.meta{display:flex;flex-wrap:wrap;gap:6px;margin:16px 6px 10px}
.meta em,.meta i{font:500 10.5px/1 var(--m);letter-spacing:.1em;text-transform:uppercase;font-style:normal;color:var(--dim);border:1px solid var(--line);border-radius:999px;padding:5px 8px}
.meta em{color:#fff;border-color:rgba(255,255,255,.3)}
.w strong{display:block;margin:0 6px;font-size:18px;line-height:1.25;font-weight:600;letter-spacing:-.02em}
.w .d{display:block;margin:8px 6px 0;font-size:14px;line-height:1.5;color:#9c9ca3}
.more{display:flex;justify-content:center;margin-top:36px}
.more[hidden]{display:none}
.cta-box{position:relative;overflow:hidden;border:1px solid var(--line);border-radius:24px;padding:clamp(28px,5vw,64px);background:radial-gradient(80% 120% at 100% 0%,rgba(255,255,255,.09),transparent 60%),var(--card);display:flex;align-items:center;justify-content:space-between;gap:28px;flex-wrap:wrap}
.cta-box p{color:#bdbdbd;font-size:17px;line-height:1.55;margin:14px 0 0;max-width:52ch}
footer{position:relative;z-index:1;border-top:1px solid var(--line);margin-top:24px}
.foot{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;padding:28px 0 calc(28px + env(safe-area-inset-bottom));font-size:13px;color:var(--dim)}
.foot a{text-decoration:none;color:#cfcfcf}
.foot a:hover{color:#fff}
.foot .mk{height:16px;width:auto;color:#fff;vertical-align:-3px;margin-right:10px}
@keyframes rise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(61,220,132,.55)}70%{box-shadow:0 0 0 9px rgba(61,220,132,0)}100%{box-shadow:0 0 0 0 rgba(61,220,132,0)}}
@media (max-width:1100px){.works{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:820px){.links{display:none}.brand span{display:none}}
@media (max-width:720px){
.works{grid-template-columns:1fr}
.stats{grid-template-columns:repeat(2,1fr)}
.stats div:nth-child(3){border-left:0;padding-left:0}
.stats div:nth-child(n+3){border-top:1px solid var(--line)}
.bar .btn.ghost{display:none}
.op{opacity:1;transform:none}
.filters{flex-wrap:nowrap;overflow-x:auto;margin-left:calc(-1*var(--pad));margin-right:calc(-1*var(--pad));padding:0 var(--pad) 4px;scrollbar-width:none}
.filters::-webkit-scrollbar{display:none}
.filters button{flex:none}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}html{scroll-behavior:auto}}
</style>
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{{LOGO}}</svg>
<div class="field" aria-hidden="true"><div class="glow"></div><div class="grid"></div><div class="noise"></div></div>
<header id="hd"><div class="wrap bar">
<a class="brand" href="./" aria-label="YSD DEV — живые проекты"><svg class="mk" viewBox="0 0 2346 852" role="img" aria-label="YSD DEV"><use href="#ysdmk"></use></svg><span>projects</span></a>
<div class="sp"></div>
<nav class="links"><a href="#works">Проекты</a><a href="{{SITE}}#prices">Цены</a><a href="{{SITE}}">Студия</a></nav>
<a class="btn ghost" href="{{SITE}}">ysddev.com</a>
<a class="btn" href="{{TG}}">Обсудить задачу</a>
</div></header>
<main class="wrap">
<div class="hero">
<p class="eyebrow"><s></s>Работает прямо сейчас</p>
<h1>Живые проекты студии YSD DEV</h1>
<p class="lead">Не скриншоты, а работающие сайты, магазины, боты и презентации. Откройте любой — нажимайте кнопки, листайте каталог, оформляйте заказ. Так же будет выглядеть и ваш проект.</p>
<div class="cta"><a class="btn" href="#works">Смотреть проекты</a><a class="btn ghost" href="{{TG}}">Обсудить свой проект ↗</a></div>
<div class="stats">{{STATS}}</div>
</div>
<section id="works">
<div class="head"><h2>Проекты</h2><p class="eyebrow" style="margin:0">Сначала — самые востребованные</p></div>
<div class="filters" role="toolbar" aria-label="Категории">{{FILTERS}}</div>
<div class="works" id="grid">{{CARDS}}</div>
<div class="more" id="more"><button class="btn ghost" type="button">Показать ещё</button></div>
</section>
<section>
<div class="cta-box">
<div><h2>Нужен такой же?</h2><p>Расскажите задачу — предложим решение, срок и цену за один день. Договор, поэтапная оплата, 14 дней гарантии.</p></div>
<div class="cta"><a class="btn" href="{{TG}}">Написать в Telegram</a><a class="btn ghost" href="{{SITE}}">Сайт студии</a></div>
</div>
</section>
</main>
<footer><div class="wrap foot">
<span><svg class="mk" viewBox="0 0 2346 852" aria-hidden="true"><use href="#ysdmk"></use></svg>© <span id="yr">2026</span> YSD DEV</span>
<span><a href="{{SITE}}">ysddev.com</a> · <a href="{{TG}}">Telegram</a></span>
</div></footer>
<script>
(function(){
  var FIRST={{FIRST}},cur='all',open=false,
      cards=[].slice.call(document.querySelectorAll('#grid .w')),
      btns=[].slice.call(document.querySelectorAll('.filters button')),
      more=document.getElementById('more');
  function render(){
    var n=0,total=0;
    cards.forEach(function(c){
      var ok=cur==='all'||c.getAttribute('data-c')===cur;
      if(ok)total++;
      var show=ok&&(open||n<FIRST);
      if(show){c.style.setProperty('--k',n%12);n++;}
      c.hidden=!show;
    });
    more.hidden=open||total<=FIRST;
  }
  btns.forEach(function(b){b.addEventListener('click',function(){
    cur=b.getAttribute('data-f');open=false;
    btns.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
    render();
  })});
  more.querySelector('button').addEventListener('click',function(){open=true;render()});
  var hd=document.getElementById('hd');
  addEventListener('scroll',function(){hd.classList.toggle('sc',scrollY>8)},{passive:true});
  document.getElementById('yr').textContent=new Date().getFullYear();
  render();
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    (HOME / "index.html").write_text(build(), encoding="utf-8")
    print("home/index.html", (HOME / "index.html").stat().st_size)
