"""Мобильное приложение для портфолио: промо-страница с живым прототипом в телефоне (экраны, вкладки, логика из конфига),
ряд экранов, возможности, платформы и стек, этапы разработки, результат, вопросы. Внешний вид и компоновка — в конфиге."""
from __future__ import annotations

import re

from .common import e, favicon, fonts, jdump, out, save, write_images

CSS = r"""
*,*::before,*::after{box-sizing:border-box}
[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;overflow-x:clip}
body{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.55 var(--fb);-webkit-font-smoothing:antialiased;overflow-x:clip}
a{color:inherit;text-decoration:none}
button,input{font:inherit;color:inherit}
button{cursor:pointer;background:none;border:0;padding:0}
:focus-visible{outline:2px solid var(--ac);outline-offset:3px;border-radius:6px}
:root{--gut:clamp(16px,4vw,56px)}
.wrap{width:min(1240px,100% - 2*var(--gut));margin-inline:auto}
h1,h2,h3{font-family:var(--fh);font-weight:var(--hw);letter-spacing:var(--ht);line-height:1.03;margin:0;text-wrap:balance}
h2{font-size:clamp(32px,4.4vw,58px)}
p{margin:0}
.kick{font:600 15px/1.2 var(--fb);color:var(--ac)}
.lead{font-size:clamp(17px,1.5vw,20px);color:var(--soft);max-width:54ch;text-wrap:pretty}
.sec{padding:clamp(64px,9vw,124px) 0}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;height:54px;padding:0 26px;border-radius:var(--rb);background:var(--ac);color:var(--aci);font-weight:600;transition:transform .2s}
.btn:hover{transform:translateY(-1px)}
.btn.ghost{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--line2)}
.top{position:sticky;top:0;z-index:30;background:color-mix(in srgb,var(--bg) 84%,transparent);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.top .bar{display:flex;align-items:center;gap:24px;height:66px}
.logo{font-family:var(--fh);font-weight:var(--hw);font-size:22px;display:flex;align-items:center;gap:10px;letter-spacing:var(--ht)}
.logo i{display:grid;place-items:center;width:34px;height:34px;border-radius:10px;background:var(--ac);color:var(--aci);font-style:normal;font-size:17px}
.nav{display:flex;gap:24px;font-size:15px;color:var(--soft);margin-left:auto}
.nav a:hover{color:var(--ink)}
.top .btn{height:42px;padding:0 18px;font-size:15px}
.hero{padding:clamp(28px,5vw,72px) 0 clamp(48px,6vw,96px)}
.hero h1{font-size:clamp(42px,6vw,88px);margin:18px 0 20px}
.hero .cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}
.plat{display:flex;gap:10px;flex-wrap:wrap;margin-top:28px}
.plat span{display:inline-flex;align-items:center;gap:8px;padding:9px 14px;border-radius:999px;background:var(--card);box-shadow:0 0 0 1px var(--line);font-size:14px;font-weight:600}
.note{font-size:14px;color:var(--mut);margin-top:18px;display:flex;gap:8px;align-items:center}
.note b{width:8px;height:8px;border-radius:50%;background:#2fbf71;box-shadow:0 0 0 4px rgba(47,191,113,.18)}
/* компоновка первого экрана */
.L-split .hg{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:clamp(24px,4vw,64px);align-items:center}
.L-wide .hg{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(24px,4vw,64px);align-items:center}
.L-wide .hg>.ph-stage{order:-1}
.ph-stage{position:relative;display:flex;justify-content:center;align-items:center;min-width:0;padding:10px 0}
.ph-stage::before{content:"";position:absolute;inset:4% 2%;border-radius:var(--blob,40px);background:var(--stagebg,color-mix(in srgb,var(--ac) 14%,var(--bg)));z-index:0}
.ph-stage>*{position:relative;z-index:1}
.ph-back{position:absolute!important;width:min(270px,62%);opacity:.95;transform:translateX(52%) rotate(5deg) scale(.86);filter:saturate(.9)}
.ph-stage .tag{position:absolute;z-index:3;padding:12px 16px;border-radius:16px;background:var(--card);box-shadow:0 18px 40px -22px rgba(0,0,0,.45),0 0 0 1px var(--line);font-size:14px;line-height:1.3;max-width:220px}
.ph-stage .tag b{display:block;font-size:15px}
.ph-stage .tag span{color:var(--mut)}
.tag.t1{left:0;top:16%}.tag.t2{right:0;bottom:14%}
/* телефон */
.phone{width:min(340px,100%);aspect-ratio:9/19;border-radius:50px;background:#0c0c0e;padding:11px;box-shadow:0 50px 100px -40px rgba(0,0,0,.5),inset 0 0 0 2px #2a2a2e;position:relative}
.phone::before{content:"";position:absolute;top:21px;left:50%;transform:translateX(-50%);width:92px;height:25px;border-radius:14px;background:#0c0c0e;z-index:9}
.app{position:relative;height:100%;border-radius:40px;overflow:hidden;background:var(--abg);color:var(--aink);display:flex;flex-direction:column;font:400 14.5px/1.4 var(--fa,var(--fb))}
.sb{display:flex;justify-content:space-between;align-items:center;padding:16px 26px 6px;font-size:13px;font-weight:600;flex:none}
.sb i{font-style:normal;letter-spacing:2px;font-size:11px}
.scr-wrap{position:relative;flex:1;min-height:0}
.scr{position:absolute;inset:0;overflow-y:auto;padding:6px 16px 16px;opacity:0;visibility:hidden;transform:translateX(16px);transition:opacity .28s,transform .32s cubic-bezier(.2,.8,.2,1),visibility 0s .3s;scrollbar-width:none}
.scr::-webkit-scrollbar{display:none}
.scr.on{opacity:1;visibility:visible;transform:none;transition:opacity .28s,transform .32s cubic-bezier(.2,.8,.2,1)}
.tabs{display:flex;justify-content:space-around;padding:8px 8px 22px;border-top:1px solid var(--aline);background:var(--abar,var(--abg));flex:none}
.tabs button{display:grid;justify-items:center;gap:2px;font-size:11px;font-weight:600;color:var(--amut);min-width:58px;position:relative}
.tabs button b{font-size:19px;line-height:1.1;font-weight:400}
.tabs button.on{color:var(--aac)}
.tabs em{position:absolute;top:-4px;right:10px;min-width:17px;height:17px;padding:0 4px;border-radius:9px;background:var(--aac);color:var(--aaci);font:700 10.5px/17px var(--fb);font-style:normal}
.ah{font:var(--ahw,700) 24px/1.15 var(--fah,var(--fh));letter-spacing:-.01em;margin:6px 0 12px}
.amut{color:var(--amut)}
.abtn{display:flex;align-items:center;justify-content:center;width:100%;min-height:48px;border-radius:var(--arb,14px);background:var(--aac);color:var(--aaci);font-weight:700;font-size:15px;margin-top:12px;transition:transform .15s,filter .15s}
.abtn:active{transform:scale(.98)}
.abtn.ghost{background:var(--acard);color:var(--aink)}
.acard{background:var(--acard);border-radius:var(--arc,16px);padding:12px 14px}
/* ряд экранов */
.shots{display:grid;grid-template-columns:repeat(var(--n,4),minmax(0,1fr));gap:clamp(12px,2vw,24px);margin-top:clamp(28px,4vw,48px)}
.shot{display:grid;gap:12px;justify-items:center;text-align:center}
.shot .mini{width:100%;max-width:240px;aspect-ratio:9/19;border-radius:32px;background:#0c0c0e;padding:7px;box-shadow:0 30px 60px -36px rgba(0,0,0,.45)}
.shot .mini>div{height:100%;border-radius:26px;overflow:hidden;background:var(--abg);color:var(--aink);font:400 9.5px/1.35 var(--fa,var(--fb));padding:22px 10px 10px;position:relative}
.shot b{font-size:16px}.shot span{font-size:14px;color:var(--soft);max-width:28ch}
/* возможности */
.feats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:clamp(28px,4vw,48px)}
.feat{padding:clamp(20px,2.4vw,30px);border-radius:var(--rc);background:var(--card);display:flex;flex-direction:column;gap:10px}
.feat i{font-style:normal;font-size:26px}
.feat b{font-family:var(--fh);font-weight:var(--hw);font-size:21px;letter-spacing:var(--ht);line-height:1.15}
.feat p{color:var(--soft);font-size:15px}
.feats.f-list{grid-template-columns:1fr 1fr;gap:0 48px}
.feats.f-list .feat{background:none;border-radius:0;padding:22px 0;border-top:1px solid var(--line2);display:grid;grid-template-columns:44px 1fr;gap:4px 14px}
.feats.f-list .feat i{grid-row:span 2}
/* стек и этапы */
.two{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(24px,5vw,80px);align-items:start}
.stack{display:grid;gap:0}
.stack div{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:16px;padding:16px 0;border-top:1px solid var(--line2)}
.stack div:last-child{border-bottom:1px solid var(--line2)}
.stack span{color:var(--mut);font-size:15px}.stack b{font-weight:600;font-size:16px}
.steps{list-style:none;margin:28px 0 0;padding:0;display:grid;gap:0;counter-reset:s}
.steps li{counter-increment:s;display:grid;grid-template-columns:58px 1fr auto;gap:16px;align-items:baseline;padding:18px 0;border-top:1px solid var(--line2)}
.steps li::before{content:counter(s);font:var(--hw) 24px/1 var(--fh);color:var(--ac)}
.steps b{display:block;font-size:18px}.steps p{color:var(--soft);font-size:15px}.steps small{color:var(--mut);font-size:14px;white-space:nowrap}
.res{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;background:var(--line);border-radius:var(--rc);overflow:hidden;margin-top:clamp(28px,4vw,44px)}
.res div{background:var(--bg);padding:clamp(20px,2.4vw,30px)}
.res b{display:block;font:var(--hw) clamp(32px,4vw,52px)/1 var(--fh);letter-spacing:-.02em;color:var(--ac)}
.res span{display:block;margin-top:10px;color:var(--soft);font-size:15px}
.faq details{border-top:1px solid var(--line);padding:4px 0}.faq details:last-child{border-bottom:1px solid var(--line)}
.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;gap:20px;padding:18px 0;font-size:clamp(17px,1.6vw,19px);font-weight:600}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-size:24px;line-height:1;color:var(--mut);transition:transform .3s}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq details p{padding:0 0 20px;color:var(--soft);max-width:70ch}
.cta-b{border-radius:var(--rs);background:var(--cbg,var(--ink));color:var(--cink,var(--bg));padding:clamp(28px,5vw,64px);display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.cta-b h2{max-width:18ch}
.foot{padding:28px 0 36px;font-size:14px;color:var(--mut);display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.reveal{opacity:0;transform:translateY(22px);transition:opacity .8s cubic-bezier(.2,.7,.2,1),transform .8s cubic-bezier(.2,.7,.2,1)}
.reveal.on{opacity:1;transform:none}
.nofx .reveal{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.reveal{opacity:1;transform:none}}
@media (max-width:1100px){.ph-stage .tag{display:none}.ph-back{display:none}}
@media (max-width:960px){.L-split .hg,.L-wide .hg,.two{grid-template-columns:1fr}.L-wide .hg>.ph-stage{order:0}.nav{display:none}
 .feats{grid-template-columns:1fr 1fr}.feats.f-list{grid-template-columns:1fr}.res{grid-template-columns:1fr 1fr}.shots{grid-template-columns:1fr 1fr;row-gap:32px}}
@media (max-width:560px){.feats{grid-template-columns:1fr}.hero .cta{flex-direction:column}.hero .cta .btn{width:100%}
 .steps li{grid-template-columns:40px 1fr}.steps small{grid-column:2}.stack div{grid-template-columns:1fr;gap:2px}}
"""

JS_BASE = r"""
(function(){
var A=document.getElementById('app'),S=[].slice.call(A.querySelectorAll('.scr')),T=[].slice.call(A.querySelectorAll('.tabs button'));
var U={auto:true,hist:[]};
U.go=function(n,noHist){S.forEach(function(s){s.classList.toggle('on',s.dataset.s===n)});T.forEach(function(t){t.classList.toggle('on',(t.dataset.tab||'')===(A.querySelector('.scr[data-s="'+n+'"]')||{}).dataset.tab)});
 var s=A.querySelector('.scr[data-s="'+n+'"]');if(s)s.scrollTop=0;U.cur=n;if(U.on&&U.on[n])U.on[n](s)};
U.money=function(n){return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g,' ')+' ₽'};
U.$=function(q){return A.querySelector(q)};U.$$=function(q){return[].slice.call(A.querySelectorAll(q))};
A.addEventListener('click',function(ev){var b=ev.target.closest('[data-go]');if(ev.isTrusted)U.auto=false;if(b){ev.preventDefault();U.go(b.dataset.go)}},true);
T.forEach(function(t){t.addEventListener('click',function(){U.go(t.dataset.first)})});
window.APP=U;
var started=false,io='IntersectionObserver'in window?new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('on');if(x.target.id==='app'&&!started){started=true;U.start&&U.start()}io.unobserve(x.target)}})},{threshold:.2}):null;
document.querySelectorAll('.reveal,#app').forEach(function(el){io?io.observe(el):el.classList.add('on')});
setTimeout(function(){if(!started){started=true;U.start&&U.start()}},2500);
window.__app=1;
})();
"""


def build(c: dict) -> str:
    d = out(c["slug"])
    write_images(d, c.get("images", {}))
    th = c["theme"]
    font_css = fonts(d, c["fonts"])
    css_vars = ";".join(f"--{k}:{v}" for k, v in th.items())
    H = c["hero"]
    nav = "".join(f'<a href="#{h}">{e(t)}</a>' for t, h in [("Прототип", "demo"), ("Экраны", "screens"), ("Возможности", "feats"),
                                                             ("Как делаем", "how"), ("Вопросы", "faq")])
    screens = "".join(f'<section class="scr{" on" if i == 0 else ""}" data-s="{k}" data-tab="{v.get("tab", "")}">{v["html"]}</section>'
                      for i, (k, v) in enumerate(c["screens"].items()))
    tabs = "".join(f'<button type="button" data-tab="{t[0]}" data-first="{t[1]}"{" class=on" if i == 0 else ""}><b>{t[2]}</b>{e(t[3])}'
                   f'{"<em id=" + chr(34) + t[4] + chr(34) + " hidden></em>" if len(t) > 4 else ""}</button>' for i, t in enumerate(c["tabs"]))
    phone = (f'<div class="phone"><div class="app" id="app"><div class="sb"><span>9:41</span><i>●●● ▮</i></div>'
             f'<div class="scr-wrap">{screens}</div><nav class="tabs">{tabs}</nav></div></div>')
    noid = lambda h: re.sub(r'\sid="[^"]*"', "", h)  # копии экранов: без id, чтобы не путать скрипт
    back = f'<div class="phone ph-back" aria-hidden="true"><div class="app">{noid(c["backScreen"])}</div></div>' if c.get("backScreen") else ""
    tags = "".join(f'<div class="tag t{i + 1}"><b>{e(a)}</b><span>{e(b)}</span></div>' for i, (a, b) in enumerate(H.get("tags", [])[:2]))
    plat = "".join(f"<span>{x}</span>" for x in c["platforms"])
    shots = "".join(f'<div class="shot reveal" style="transition-delay:{i * 70}ms"><div class="mini" aria-hidden="true"><div>{noid(s[2])}</div></div><b>{e(s[0])}</b><span>{e(s[1])}</span></div>'
                    for i, s in enumerate(c["shots"]))
    fcls = " f-list" if c.get("featsStyle") == "list" else ""
    feats = "".join(f'<div class="feat reveal"><i>{a}</i><b>{e(b)}</b><p>{e(t)}</p></div>' for a, b, t in c["feats"])
    stack = "".join(f"<div><span>{e(a)}</span><b>{e(b)}</b></div>" for a, b in c["stack"])
    steps = "".join(f"<li><div><b>{e(a)}</b><p>{e(b)}</p></div><small>{e(t)}</small></li>" for a, b, t in c["steps"])
    res = "".join(f'<div class="reveal"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in c["results"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in c["faq"])
    page = f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(c['title'])}</title>
<meta name="description" content="{e(c['desc'])}">
<meta property="og:title" content="{e(c['title'])}">
<meta property="og:description" content="{e(c['desc'])}">
<meta name="theme-color" content="{th['bg']}">
<link rel="icon" href="{favicon(c.get('favLetter', c['brand'][0]), th['ac'], th['aci'])}">
<script>document.documentElement.classList.add('js');setTimeout(function(){{if(!window.__app)document.documentElement.classList.add('nofx')}},3500)</script>
<style>
{font_css}
:root{{{css_vars}}}
{CSS}
{c.get('appCss', '')}
{c.get('css', '')}
</style>
</head>
<body class="L-{c.get('layout', 'split')}">
<header class="top"><div class="wrap bar"><a class="logo" href="#top"><i>{c['logoIcon']}</i>{e(c['brand'])}</a><nav class="nav">{nav}</nav>
<a class="btn" href="#demo">{e(c.get('topCta', 'Открыть прототип'))}</a></div></header>
<main>
<section class="hero" id="top"><div class="wrap hg">
 <div class="reveal"><div class="kick">{e(H['kicker'])}</div><h1>{H['h1']}</h1><p class="lead">{H['lead']}</p>
 <div class="cta"><a class="btn" href="#demo">{e(H['cta'])}</a><a class="btn ghost" href="#how">{e(H.get('cta2', 'Как мы делаем приложения'))}</a></div>
 <div class="plat">{plat}</div>
 <p class="note"><b></b>{e(c.get('demoNote', 'Прототип в телефоне работает: нажимайте кнопки'))}</p></div>
 <div class="ph-stage" id="demo">{tags}{back}{phone}</div>
</div></section>
<section class="sec" id="screens" style="padding-top:0"><div class="wrap"><div class="reveal"><div class="kick">Экраны</div><h2 style="margin-top:14px">{c['shotsTitle']}</h2></div>
<div class="shots" style="--n:{len(c['shots'])}">{shots}</div></div></section>
<section class="sec" id="feats" style="padding-top:0"><div class="wrap"><div class="reveal"><div class="kick">Возможности</div><h2 style="margin-top:14px">{c['featsTitle']}</h2></div>
<div class="feats{fcls}">{feats}</div></div></section>
<section class="sec" id="how" style="padding-top:0"><div class="wrap two">
 <div class="reveal"><div class="kick">Платформы и стек</div><h2 style="margin:14px 0 24px">{c['stackTitle']}</h2><div class="stack">{stack}</div></div>
 <div class="reveal"><div class="kick">Как делаем</div><h2 style="margin:14px 0 0">{c['stepsTitle']}</h2><ol class="steps">{steps}</ol></div>
</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="reveal"><div class="kick">Результат</div><h2 style="margin-top:14px">{c['resTitle']}</h2></div>
<div class="res">{res}</div></div></section>
<section class="sec" id="faq" style="padding-top:0"><div class="wrap" style="max-width:900px"><div class="reveal"><div class="kick">Вопросы</div><h2 style="margin:14px 0 24px">Частые вопросы</h2></div><div class="faq">{faq}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="cta-b reveal"><h2>{c['ctaTitle']}</h2><a class="btn" href="#demo">{e(c.get('ctaBtn', 'Открыть прототип'))}</a></div></div></section>
</main>
<footer class="wrap foot"><span>© 2026 {e(c['brand'])}</span><a href="https://ysddev.com/" target="_blank" rel="noopener" style="color:inherit">Разработан с душой студией YSD DEV</a></footer>
<script>window.APPCFG={jdump(c.get('data', {}))};</script>
<script>{JS_BASE}</script>
<script>{c.get('appJs', '')}</script>
</body>
</html>
"""
    save(d, page)
    return d
