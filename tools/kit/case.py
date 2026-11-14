"""Кейс дизайна для портфолио: страница работы — обложка, задача и идея, макеты (SVG/CSS), палитра с копированием, шрифты,
сетка носителей, интерактивная часть, результат. Макеты и интерактив — в конфиге работы; здесь только каркас и общий стиль."""
from __future__ import annotations

from .common import e, favicon, fonts, jdump, out, save, write_images

CSS = r"""
*,*::before,*::after{box-sizing:border-box}
[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;overflow-x:clip}
body{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.6 var(--fb);-webkit-font-smoothing:antialiased;overflow-x:clip}
img,svg{max-width:100%;display:block}
a{color:inherit}
button,input,select{font:inherit;color:inherit}
button{cursor:pointer;background:none;border:0;padding:0}
:focus-visible{outline:2px solid var(--ac);outline-offset:3px;border-radius:4px}
:root{--gut:clamp(16px,4.5vw,64px)}
.wrap{width:min(1280px,100% - 2*var(--gut));margin-inline:auto}
h1,h2,h3{font-family:var(--fh);font-weight:var(--hw);letter-spacing:var(--ht);line-height:1.02;margin:0;text-wrap:balance}
p{margin:0}
.kick{font:600 12px/1 var(--fb);letter-spacing:.18em;text-transform:uppercase;color:var(--kc,var(--ac))}
.bar{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--bg) 86%,transparent);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.bar .in{display:flex;align-items:center;gap:22px;height:62px}
.bar .bn{font:var(--hw) 19px/1 var(--fh);letter-spacing:var(--ht);white-space:nowrap;text-decoration:none}
.bar nav{display:flex;gap:20px;margin-left:auto;font-size:14.5px;color:var(--mut);overflow-x:auto;scrollbar-width:none}
.bar nav::-webkit-scrollbar{display:none}
.bar nav a{text-decoration:none;white-space:nowrap}.bar nav a:hover,.bar nav a.on{color:var(--ink)}
.bar .dev{font-size:12.5px;color:var(--mut);white-space:nowrap;text-decoration:none}
.hero{padding:clamp(40px,7vw,104px) 0 clamp(36px,5vw,72px)}
.hero .g{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:clamp(28px,5vw,80px);align-items:center}
.hero h1{font-size:clamp(44px,6.4vw,96px);margin:18px 0 22px}
.hero h1 em{font-style:var(--emst,normal);color:var(--ac)}
.lead{font-size:clamp(17px,1.5vw,20px);color:var(--soft);max-width:52ch;text-wrap:pretty}
.facts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px 28px;margin-top:34px;padding-top:24px;border-top:1px solid var(--line)}
.facts span{display:block;font-size:12.5px;color:var(--mut);letter-spacing:.04em}
.facts b{display:block;font-weight:500;font-size:15px;line-height:1.35}
.acts{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}
.btn{display:inline-flex;align-items:center;gap:10px;height:52px;padding:0 24px;border-radius:var(--rb,999px);background:var(--ac);color:var(--aci);font-weight:600;text-decoration:none;transition:transform .2s}
.btn:hover{transform:translateY(-1px)}
.btn.g{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--line2)}
.art{position:relative;border-radius:var(--ra,20px);overflow:hidden;background:var(--artbg,var(--card))}
.art>svg{width:100%;height:auto}
.sec{padding:clamp(64px,9vw,128px) 0;border-top:1px solid var(--line)}
.sec.alt{background:var(--alt,var(--card))}
.sh{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(20px,4vw,64px);align-items:end;margin-bottom:clamp(28px,4vw,52px)}
.sh h2{font-size:clamp(34px,4.6vw,64px);margin-top:14px}
.sh .lead{justify-self:end}
.t3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(16px,2.5vw,32px)}
.t3 div{padding-top:20px;border-top:2px solid var(--ink)}
.t3 b{display:block;font:var(--hw) clamp(22px,2vw,28px)/1.15 var(--fh);letter-spacing:var(--ht);margin-bottom:10px}
.t3 p{color:var(--soft);font-size:16px}
.t3 i{font-style:normal;font:500 13px var(--fm,var(--fb));color:var(--ac);display:block;margin-bottom:14px}
.cap{font-size:13.5px;color:var(--mut);margin-top:12px}
.pal{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px}
.sw{border-radius:16px;overflow:hidden;background:var(--card);box-shadow:0 0 0 1px var(--line);text-align:left;transition:transform .2s}
.sw:hover{transform:translateY(-3px)}
.sw i{display:block;height:150px}
.sw div{padding:14px 16px 16px;display:grid;gap:2px}
.sw b{font-size:16px}.sw span{font:500 13px var(--fm,var(--fb));color:var(--mut)}.sw small{font-size:12.5px;color:var(--mut)}
.sw.cp span::after{content:" — скопировано";color:var(--ac)}
.tp{display:grid;gap:0}
.tr{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:24px;padding:26px 0;border-top:1px solid var(--line);align-items:baseline}
.tr:last-child{border-bottom:1px solid var(--line)}
.tr b{display:block;font-size:15px}.tr small{display:block;color:var(--mut);font-size:13.5px}
.tr .sm{font-size:clamp(28px,4vw,56px);line-height:1.08;overflow-wrap:anywhere}
.gal{display:grid;grid-template-columns:repeat(12,1fr);gap:clamp(12px,1.6vw,20px)}
.gal figure{margin:0;grid-column:span var(--s,6);min-width:0}
.gal figure>div{border-radius:var(--ra,18px);overflow:hidden;background:var(--tbg,var(--card));aspect-ratio:var(--ar,4/3);display:grid;place-items:center;position:relative}
.gal figure>div>svg{width:100%;height:100%}
.gal figcaption{font-size:13.5px;color:var(--mut);margin-top:10px}
.gal figcaption b{color:var(--ink);font-weight:600}
.res{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;background:var(--line);border-radius:20px;overflow:hidden;box-shadow:0 0 0 1px var(--line)}
.res div{background:var(--bg);padding:clamp(20px,2.4vw,32px)}
.res b{display:block;font:var(--hw) clamp(34px,4vw,54px)/1 var(--fh);letter-spacing:-.02em;color:var(--rc,var(--ac))}
.res span{display:block;margin-top:10px;color:var(--soft);font-size:15px}
.quote{font:var(--qw,400) clamp(24px,3vw,40px)/1.25 var(--fq,var(--fh));max-width:28ch;margin-top:clamp(28px,4vw,48px);text-wrap:balance}
.quote small{display:block;font:400 14px var(--fb);color:var(--mut);margin-top:14px}
.cta{border-radius:var(--rs,28px);background:var(--cbg,var(--ink));color:var(--cink,var(--bg));padding:clamp(32px,6vw,80px);display:flex;justify-content:space-between;align-items:center;gap:28px;flex-wrap:wrap}
.cta h2{font-size:clamp(32px,4.4vw,60px);max-width:16ch}
.cta .btn{background:var(--cbtn,var(--ac));color:var(--cbtni,var(--aci))}
.foot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding:30px 0 44px;font-size:14px;color:var(--mut)}
.seg{display:inline-flex;gap:4px;padding:4px;border-radius:999px;background:color-mix(in srgb,var(--ink) 7%,transparent);flex-wrap:wrap}
.seg button{padding:8px 15px;border-radius:999px;font-size:14px;font-weight:500;white-space:nowrap}
.seg button.on{background:var(--ink);color:var(--bg)}
.js .rv{opacity:0;transform:translateY(22px);transition:opacity .8s,transform .8s cubic-bezier(.2,.8,.2,1)}
.js .rv.on{opacity:1;transform:none}
@media (max-width:980px){
 .bar nav{display:none}.bar .dev{margin-left:auto}
 .hero .g,.sh{grid-template-columns:1fr}.sh .lead{justify-self:start}
 .t3{grid-template-columns:1fr}
 .gal figure{grid-column:span 12!important}
 .res{grid-template-columns:1fr 1fr}
 .tr{grid-template-columns:1fr;gap:8px}
}
@media (max-width:560px){.facts{grid-template-columns:1fr 1fr;gap:12px 16px}.cta .btn{width:100%;justify-content:center}.acts .btn{flex:1 1 100%;justify-content:center}}
@media (prefers-reduced-motion:reduce){*{animation-duration:.01ms!important;transition-duration:.01ms!important}html{scroll-behavior:auto}}
@media print{.bar,.acts,.cta{display:none!important}.js .rv{opacity:1;transform:none}}
"""

JS = r"""
(function(){
var io='IntersectionObserver'in window?new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('on');io.unobserve(x.target)}})},{threshold:.08}):null;
document.querySelectorAll('.rv').forEach(function(el){io?io.observe(el):el.classList.add('on')});
setTimeout(function(){document.querySelectorAll('.rv').forEach(function(el){el.classList.add('on')})},4000);
document.addEventListener('click',function(e){var b=e.target.closest('.sw[data-hex]');if(!b)return;var t=b.dataset.hex;
 try{navigator.clipboard&&navigator.clipboard.writeText(t)}catch(x){}b.classList.add('cp');setTimeout(function(){b.classList.remove('cp')},1400)});
var links=[].slice.call(document.querySelectorAll('.bar nav a'));if(links.length&&io){var so=new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){links.forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+x.target.id)})}})},{rootMargin:'-45% 0px -50% 0px'});
 links.forEach(function(a){var s=document.querySelector(a.getAttribute('href'));if(s)so.observe(s)})}
window.__case=1;
})();
"""


def sec_head(s: dict) -> str:
    return (f'<div class="sh rv"><div><div class="kick">{e(s.get("kick", ""))}</div><h2>{s["h2"]}</h2></div>'
            + (f'<p class="lead">{s["lead"]}</p>' if s.get("lead") else "") + "</div>")


def render(s: dict) -> str:
    t = s["type"]
    head = sec_head(s) if s.get("h2") else ""
    if t == "text3":
        body = '<div class="t3">' + "".join(
            f'<div class="rv" style="transition-delay:{i * 80}ms">{"<i>" + e(n) + "</i>" if n else ""}<b>{e(a)}</b><p>{b}</p></div>'
            for i, (n, a, b) in enumerate(s["items"])) + "</div>"
    elif t == "palette":
        body = '<div class="pal">' + "".join(
            f'<button class="sw rv" type="button" data-hex="{e(h)}" title="Скопировать {e(h)}"><i style="background:{h}"></i>'
            f'<div><b>{e(n)}</b><span>{e(h)}</span><small>{e(r)}</small></div></button>' for n, h, r in s["colors"]) + "</div>"
    elif t == "type":
        body = '<div class="tp">' + "".join(
            f'<div class="tr rv"><div><b>{e(n)}</b><small>{e(u)}</small></div><div class="sm" style="font-family:{f};{st}">{smp}</div></div>'
            for n, f, u, smp, st in s["fonts"]) + "</div>"
    elif t == "gallery":
        body = '<div class="gal">' + "".join(
            f'<figure class="rv" style="--s:{g.get("span", 6)};--ar:{g.get("ar", "4/3")}{";--tbg:" + g["bg"] if g.get("bg") else ""}">'
            f'<div>{g["html"]}</div><figcaption>{g.get("cap", "")}</figcaption></figure>' for g in s["items"]) + "</div>"
    elif t == "html":
        body = f'<div class="rv">{s["html"]}</div>'
    elif t == "result":
        body = ('<div class="res rv">' + "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in s["stats"]) + "</div>"
                + (f'<p class="quote rv">«{e(s["quote"][0])}»<small>{e(s["quote"][1])}</small></p>' if s.get("quote") else ""))
    else:
        raise ValueError(t)
    cls = "sec alt" if s.get("alt") else "sec"
    return f'<section class="{cls}" id="{s["id"]}"{" style=" + chr(34) + s["style"] + chr(34) if s.get("style") else ""}><div class="wrap">{head}{body}</div></section>'


def build(c: dict) -> str:
    d = out(c["slug"])
    write_images(d, c.get("images", {}))
    th = c["theme"]
    font_css = fonts(d, c["fonts"])
    css_vars = ";".join(f"--{k}:{v}" for k, v in th.items())
    H = c["hero"]
    nav = "".join(f'<a href="#{s["id"]}">{e(s["nav"])}</a>' for s in c["sections"] if s.get("nav"))
    facts = "".join(f"<div><span>{e(a)}</span><b>{e(b)}</b></div>" for a, b in c["facts"])
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
<script>document.documentElement.classList.add('js')</script>
<style>
{font_css}
:root{{{css_vars}}}
{CSS}
{c.get('css', '')}
</style>
</head>
<body>
<header class="bar"><div class="wrap in"><a class="bn" href="#top">{e(c['brand'])}</a><nav aria-label="Разделы кейса">{nav}</nav>
<a class="dev" href="https://ysddev.com" rel="noopener">YSD DEV</a></div></header>
<main>
<section class="hero" id="top"><div class="wrap g">
 <div class="rv"><div class="kick">{e(H['kicker'])}</div><h1>{H['h1']}</h1><p class="lead">{H['lead']}</p>
 <div class="acts"><a class="btn" href="#{H.get('go', c['sections'][0]['id'])}">{e(H.get('cta', 'Смотреть работу'))}</a>
 <a class="btn g" href="https://ysddev.com" rel="noopener">Обсудить проект</a></div>
 <div class="facts">{facts}</div></div>
 <div class="art rv">{H['art']}</div>
</div></section>
{''.join(render(s) for s in c['sections'])}
<section class="sec"><div class="wrap"><div class="cta rv"><h2>{c.get('ctaTitle', 'Нужен такой же дизайн?')}</h2><a class="btn" href="https://ysddev.com" rel="noopener">Обсудить проект</a></div></div></section>
</main>
<footer class="wrap foot"><span>© 2026 {e(c['brand'])}</span><span>Дизайн YSD DEV</span></footer>
<script>window.CASECFG={jdump(c.get('data', {}))};</script>
<script>{JS}</script>
{('<script>' + c['js'] + '</script>') if c.get('js') else ''}
</body>
</html>
"""
    save(d, page)
    return d
