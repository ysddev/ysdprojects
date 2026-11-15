"""Сайт компании для портфолио: шапка с меню, первый экран (фото или своя графика), услуги с ценами, интерактив (свой
для каждой ниши — в конфиге), этапы, команда, галерея, вопросы, заявка, контакты. Отзывов нет: выдуманные отзывы не
пишем. Стиль (шрифты, цвета, радиусы, раскладка) — в конфиге, каркас общий."""
from __future__ import annotations

from .common import e, favicon, fonts, img, jdump, out, save, write_images

CSS = r"""
*,*::before,*::after{box-sizing:border-box}
[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;overflow-x:clip;scroll-padding-top:80px}
body{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.6 var(--fb);-webkit-font-smoothing:antialiased;overflow-x:clip}
img,svg{max-width:100%;display:block}
img{height:auto}
a{color:inherit}
button,input,select,textarea{font:inherit;color:inherit}
button{cursor:pointer;background:none;border:0;padding:0}
:focus-visible{outline:2px solid var(--ac);outline-offset:3px;border-radius:4px}
:root{--gut:clamp(16px,4.5vw,64px)}
.wrap{width:min(1240px,100% - 2*var(--gut));margin-inline:auto}
h1,h2,h3{font-family:var(--fh);font-weight:var(--hw);letter-spacing:var(--ht);line-height:1.04;margin:0;text-wrap:balance}
p{margin:0}
.kick{font:600 12.5px/1.2 var(--fk,var(--fb));letter-spacing:var(--kls,.14em);text-transform:var(--ktt,uppercase);color:var(--kc,var(--ac))}
.top{position:sticky;top:0;z-index:30;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.top .in{display:flex;align-items:center;gap:24px;height:68px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;font:var(--hw) 20px/1 var(--fh);letter-spacing:var(--ht);white-space:nowrap}
.logo svg{width:30px;height:30px;flex:none}
.top nav{display:flex;gap:22px;margin-left:auto;font-size:15px;color:var(--soft)}
.top nav a{text-decoration:none;white-space:nowrap}.top nav a:hover{color:var(--ink)}
.top .tel{font-weight:600;text-decoration:none;white-space:nowrap;font-size:15px}
.top .btn{height:44px;padding:0 18px;font-size:15px}
.burger{display:none;width:44px;height:44px;border-radius:12px;box-shadow:inset 0 0 0 1.5px var(--line2);place-items:center;margin-left:auto}
.burger i,.burger i::before,.burger i::after{display:block;width:18px;height:2px;background:var(--ink);border-radius:2px;position:relative}
.burger i::before,.burger i::after{content:"";position:absolute;left:0}.burger i::before{top:-6px}.burger i::after{top:6px}
.top .mnav{display:none}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;height:54px;padding:0 26px;border-radius:var(--rb,999px);background:var(--ac);color:var(--aci);font-weight:600;text-decoration:none;transition:transform .2s,background .2s;white-space:nowrap}
.btn:hover{transform:translateY(-1px)}
.btn.g{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--line2)}
.btn.w{background:var(--bg);color:var(--ink)}
.hero{padding:clamp(36px,6vw,88px) 0 clamp(40px,6vw,88px)}
.hero .g{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(28px,5vw,72px);align-items:center}
.hero h1{font-size:var(--h1s,clamp(42px,6vw,88px));margin:18px 0 22px}
.hero h1 em{font-style:var(--emst,normal);color:var(--emc,var(--ac))}
.lead{font-size:clamp(17px,1.5vw,20px);color:var(--soft);max-width:54ch;text-wrap:pretty}
.acts{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}
.pts{display:flex;flex-wrap:wrap;gap:10px 26px;margin-top:30px;font-size:14.5px;color:var(--soft)}
.pts span{display:flex;align-items:center;gap:8px}.pts span::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--ac);flex:none}
.hph{position:relative;border-radius:var(--ra,22px);overflow:hidden;background:var(--card);aspect-ratio:var(--har,4/5)}
.hph img,.hph>svg{width:100%;height:100%;object-fit:cover}
.hph .tag{position:absolute;left:16px;bottom:16px;right:16px;max-width:330px;background:color-mix(in srgb,var(--bg) 92%,transparent);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-radius:16px;padding:14px 16px;font-size:14px;line-height:1.4}
.hph .tag b{display:block;font:var(--hw) 22px/1.1 var(--fh);letter-spacing:var(--ht);margin-bottom:4px}
.hero.full{position:relative;padding:0;min-height:min(86vh,820px);display:grid;align-items:end;color:#fff;isolation:isolate}
.hero.full .bgph{position:absolute;inset:0;z-index:-2}.hero.full .bgph img{width:100%;height:100%;object-fit:cover}
.hero.full::before{content:"";position:absolute;inset:0;z-index:-1;background:var(--shade,linear-gradient(180deg,rgba(0,0,0,.15),rgba(0,0,0,.62)))}
.hero.full .g{grid-template-columns:minmax(0,1fr);padding:clamp(80px,12vw,160px) 0 clamp(36px,6vw,72px)}
.hero.full .lead{color:rgba(255,255,255,.86)}.hero.full .pts{color:rgba(255,255,255,.86)}
.hero.full .btn.g{color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.6)}
.sec{padding:clamp(64px,9vw,120px) 0}
.sec+.sec{border-top:1px solid var(--line)}
.sec.alt{background:var(--alt);border-top:0}.sec.alt+.sec{border-top:0}
.sec.dark{background:var(--dk,var(--ink));color:var(--dki,var(--bg));border-top:0;--line:rgba(255,255,255,.14);--line2:rgba(255,255,255,.3);--soft:rgba(255,255,255,.74);--mut:rgba(255,255,255,.56);--card:rgba(255,255,255,.06)}
.sec.dark+.sec{border-top:0}
.sh{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(20px,4vw,64px);align-items:end;margin-bottom:clamp(28px,4vw,52px)}
.sh h2{font-size:clamp(32px,4.4vw,60px);margin-top:14px}
.sh .lead{justify-self:end}
.cards{display:grid;grid-template-columns:repeat(var(--cd,3),minmax(0,1fr));gap:clamp(12px,1.8vw,20px)}
.card{background:var(--card);border-radius:var(--rc,20px);padding:clamp(20px,2.4vw,30px);display:flex;flex-direction:column;gap:12px;box-shadow:var(--cs,0 0 0 1px var(--line));position:relative;overflow:hidden}
.card h3{font-size:clamp(21px,1.8vw,25px);line-height:1.15}
.card p{color:var(--soft);font-size:15.5px}
.card ul{margin:0;padding:0;list-style:none;display:grid;gap:7px;font-size:15px;color:var(--soft)}
.card li{display:flex;gap:9px}.card li::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--ac);flex:none;margin-top:9px}
.card .pr{margin-top:auto;padding-top:14px;border-top:1px solid var(--line);display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap}
.card .pr b{font:var(--hw) 24px/1 var(--fh);letter-spacing:var(--ht)}
.card .pr small{color:var(--mut);font-size:13.5px}
.card .ic{width:46px;height:46px;border-radius:14px;background:var(--icbg,color-mix(in srgb,var(--ac) 14%,transparent));display:grid;place-items:center;color:var(--ac)}
.card .ic svg{width:24px;height:24px}
.card .ph{margin:calc(-1*clamp(20px,2.4vw,30px)) calc(-1*clamp(20px,2.4vw,30px)) 6px;aspect-ratio:16/10;overflow:hidden}
.card .ph img{width:100%;height:100%;object-fit:cover}
.steps{display:grid;grid-template-columns:repeat(var(--sd,4),minmax(0,1fr));gap:clamp(14px,2vw,24px);counter-reset:s}
.steps div{padding-top:22px;border-top:2px solid var(--ink);counter-increment:s}
.sec.dark .steps div{border-color:var(--ac)}
.steps div::before{content:counter(s,decimal-leading-zero);display:block;font:500 13px var(--fm,var(--fb));color:var(--ac);margin-bottom:12px}
.steps b{display:block;font:var(--hw) clamp(20px,1.7vw,24px)/1.18 var(--fh);letter-spacing:var(--ht);margin-bottom:8px}
.steps p{color:var(--soft);font-size:15.5px}
.steps small{display:block;margin-top:10px;font-size:13.5px;color:var(--mut)}
.team{display:grid;grid-template-columns:repeat(var(--td,3),minmax(0,1fr));gap:clamp(14px,2vw,24px)}
.team figure{margin:0}
.team .tp{aspect-ratio:4/5;border-radius:var(--rc,20px);overflow:hidden;background:var(--card)}
.team .tp img{width:100%;height:100%;object-fit:cover}
.team figcaption{margin-top:14px}.team b{display:block;font-size:18px}.team span{display:block;color:var(--mut);font-size:14.5px;line-height:1.45;margin-top:3px}
.gal{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:clamp(10px,1.4vw,18px)}
.gal figure{margin:0;grid-column:span var(--s,4);border-radius:var(--rc,18px);overflow:hidden;background:var(--card);aspect-ratio:var(--ar,4/3);position:relative}
.gal img{width:100%;height:100%;object-fit:cover;transition:transform .8s}
.gal figure:hover img{transform:scale(1.04)}
.gal figcaption{position:absolute;left:12px;bottom:12px;background:color-mix(in srgb,var(--bg) 90%,transparent);border-radius:10px;padding:6px 10px;font-size:13px}
.faq{display:grid;gap:10px;max-width:900px}
.faq details{background:var(--card);border-radius:16px;box-shadow:0 0 0 1px var(--line);padding:0 22px}
.faq summary{list-style:none;cursor:pointer;padding:20px 30px 20px 0;font-weight:600;font-size:17px;position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";position:absolute;right:0;top:15px;font-size:24px;font-weight:400;color:var(--ac);transition:transform .25s}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq details p{padding:0 0 20px;color:var(--soft)}
.split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,4vw,64px);align-items:start}
.form{background:var(--card);border-radius:var(--rc,24px);padding:clamp(22px,3vw,36px);box-shadow:var(--cs,0 0 0 1px var(--line));display:grid;gap:14px}
.sec.dark .form{background:var(--bg);color:var(--ink);--line:var(--line0);--line2:var(--line20);--soft:var(--soft0);--mut:var(--mut0)}
.form label{display:grid;gap:6px;font-size:14px;color:var(--soft)}
.form input,.form select,.form textarea{width:100%;height:52px;border-radius:12px;border:1.5px solid var(--line2);background:var(--bg);padding:0 14px;font-size:16px;color:var(--ink)}
.form textarea{height:96px;padding:12px 14px;resize:vertical}
.form input:focus,.form select:focus,.form textarea:focus{outline:0;border-color:var(--ac)}
.form .row2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.form .btn{width:100%;margin-top:4px}
.form .ok{display:none;padding:16px;border-radius:12px;background:color-mix(in srgb,var(--ac) 12%,transparent);font-size:15px}
.form.sent .ok{display:block}.form.sent .fl{display:none}
.form .note{font-size:12.5px;color:var(--mut)}
.contacts{display:grid;gap:18px}
.contacts div span{display:block;font-size:13px;color:var(--mut);letter-spacing:.04em}
.contacts div b{font-size:18px;font-weight:600}
.map{border-radius:var(--rc,20px);overflow:hidden;aspect-ratio:16/10;background:var(--card);box-shadow:0 0 0 1px var(--line)}
.map svg{width:100%;height:100%}
.foot{padding:34px 0 46px;font-size:14px;color:var(--mut);border-top:1px solid var(--line)}
.foot .in{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.foot a{color:var(--ink)}
.seg{display:inline-flex;gap:4px;padding:4px;border-radius:999px;background:color-mix(in srgb,var(--ink) 7%,transparent);flex-wrap:wrap}
.seg button{padding:9px 16px;border-radius:999px;font-size:14.5px;font-weight:500;white-space:nowrap}
.seg button.on{background:var(--ink);color:var(--bg)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips button{padding:9px 15px;border-radius:999px;font-size:14.5px;box-shadow:inset 0 0 0 1.5px var(--line2);background:var(--card)}
.chips button.on{background:var(--ac);color:var(--aci);box-shadow:none}
.rng{display:grid;gap:8px}
.rng .rh{display:flex;justify-content:space-between;gap:12px;font-size:14.5px;color:var(--soft)}.rng .rh b{color:var(--ink)}
.rng input{width:100%;accent-color:var(--ac)}
.big{font:var(--hw) clamp(38px,5vw,64px)/1 var(--fh);letter-spacing:var(--ht)}
.panel{background:var(--card);border-radius:var(--rc,24px);padding:clamp(20px,3vw,36px);box-shadow:var(--cs,0 0 0 1px var(--line))}
.toast{position:fixed;left:50%;bottom:24px;transform:translate(-50%,140%);background:var(--ink);color:var(--bg);padding:12px 18px;border-radius:12px;font-size:15px;z-index:60;transition:transform .35s;max-width:calc(100% - 32px)}
.toast{visibility:hidden}.toast.on{transform:translate(-50%,0);visibility:visible}
.js .rv{opacity:0;transform:translateY(20px);transition:opacity .8s,transform .8s cubic-bezier(.2,.8,.2,1)}
.js .rv.on{opacity:1;transform:none}
@media (max-width:1040px){.top nav,.top .tel{display:none}.burger{display:grid}.top .btn{display:none}
 .top .mnav.on{display:grid;gap:4px;padding:10px var(--gut) 18px;border-top:1px solid var(--line)}
 .mnav a{padding:12px 0;text-decoration:none;font-size:17px;border-bottom:1px solid var(--line)}
 .cards,.steps,.team{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:860px){.hero .g,.sh,.split{grid-template-columns:minmax(0,1fr)}.sh .lead{justify-self:start}
 .gal figure{grid-column:span 6!important}}
@media (max-width:620px){.cards,.steps,.team{grid-template-columns:minmax(0,1fr)}.gal figure{grid-column:span 12!important}
 .acts .btn{flex:1 1 100%}.form .row2{grid-template-columns:1fr}.hero.full{min-height:auto}}
@media (prefers-reduced-motion:reduce){*{animation-duration:.01ms!important;transition-duration:.01ms!important}html{scroll-behavior:auto}}
"""

JS = r"""
(function(){
var io='IntersectionObserver'in window?new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('on');io.unobserve(x.target)}})},{threshold:.06}):null;
document.querySelectorAll('.rv').forEach(function(el){io?io.observe(el):el.classList.add('on')});
setTimeout(function(){document.querySelectorAll('.rv').forEach(function(el){el.classList.add('on')})},3500);
var b=document.querySelector('.burger'),m=document.querySelector('.mnav');
if(b&&m){b.addEventListener('click',function(){var o=m.classList.toggle('on');b.setAttribute('aria-expanded',o)});m.addEventListener('click',function(e){if(e.target.closest('a'))m.classList.remove('on')})}
var t=document.createElement('div');t.className='toast';t.setAttribute('role','status');document.body.appendChild(t);var tt;
window.toast=function(s){t.textContent=s;t.classList.add('on');clearTimeout(tt);tt=setTimeout(function(){t.classList.remove('on')},2600)};
document.querySelectorAll('form.form').forEach(function(f){f.addEventListener('submit',function(ev){ev.preventDefault();
 var bad=[].slice.call(f.querySelectorAll('[required]')).filter(function(i){return !String(i.value||'').trim()});
 if(bad.length){bad[0].focus();toast('Заполните: '+(bad[0].dataset.n||'поле'));return}
 f.classList.add('sent');var ok=f.querySelector('.ok');if(ok&&f.dataset.ok)ok.textContent=f.dataset.ok})});
document.addEventListener('click',function(ev){var a=ev.target.closest('[data-mail]');if(!a)return;ev.preventDefault();
 var s=a.dataset.mail;try{navigator.clipboard&&navigator.clipboard.writeText(s)}catch(x){}toast('Адрес скопирован: '+s)});
window.rub=function(n){return Math.round(n).toLocaleString('ru-RU').replace(/ /g,' ')+' ₽'};
window.plural=function(n,a,b,c){var x=Math.abs(n)%100,y=x%10;return x>10&&x<20?c:y>1&&y<5?b:y==1?a:c};
})();
"""


def sec_head(s: dict) -> str:
    return (f'<div class="sh rv"><div><div class="kick">{e(s.get("kick", ""))}</div><h2>{s["h2"]}</h2></div>'
            + (f'<p class="lead">{s["lead"]}</p>' if s.get("lead") else "") + "</div>")


def render(s: dict, I: dict) -> str:
    t = s["type"]
    head = sec_head(s) if s.get("h2") else ""
    if t == "cards":
        def card(c):
            ph = f'<div class="ph">{img(c["img"], I, "(max-width:620px) 100vw, 33vw", c.get("alt", ""))}</div>' if c.get("img") else ""
            ic = f'<div class="ic">{c["icon"]}</div>' if c.get("icon") else ""
            ul = ("<ul>" + "".join(f"<li>{x}</li>" for x in c["list"]) + "</ul>") if c.get("list") else ""
            pr = (f'<div class="pr"><b>{c["price"]}</b><small>{c.get("unit", "")}</small></div>') if c.get("price") else ""
            return (f'<article class="card rv"{" style=" + chr(34) + c["style"] + chr(34) if c.get("style") else ""}>{ph}{ic}'
                    f'<h3>{c["t"]}</h3>{"<p>" + c["d"] + "</p>" if c.get("d") else ""}{ul}{pr}</article>')
        body = f'<div class="cards" style="--cd:{s.get("cols", 3)}">' + "".join(card(c) for c in s["items"]) + "</div>"
    elif t == "steps":
        body = f'<div class="steps" style="--sd:{s.get("cols", 4)}">' + "".join(
            f'<div class="rv"><b>{a}</b><p>{b}</p>{"<small>" + c + "</small>" if c else ""}</div>' for a, b, c in s["items"]) + "</div>"
    elif t == "team":
        body = f'<div class="team" style="--td:{s.get("cols", 3)}">' + "".join(
            f'<figure class="rv"><div class="tp">{img(p["img"], I, "(max-width:620px) 100vw, 30vw", p["n"]) if p.get("img") else p.get("art", "")}</div>'
            f'<figcaption><b>{e(p["n"])}</b><span>{p["r"]}</span></figcaption></figure>' for p in s["items"]) + "</div>"
    elif t == "gallery":
        body = '<div class="gal">' + "".join(
            f'<figure class="rv" style="--s:{g.get("span", 4)};--ar:{g.get("ar", "4/3")}">{img(g["img"], I, "(max-width:620px) 100vw, 40vw", g.get("alt", ""))}'
            + (f'<figcaption>{g["cap"]}</figcaption>' if g.get("cap") else "") + "</figure>" for g in s["items"]) + "</div>"
    elif t == "faq":
        body = '<div class="faq">' + "".join(
            f'<details class="rv"{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(s["items"])) + "</div>"
    elif t == "html":
        body = s["html"]
    else:
        raise ValueError(t)
    cls = "sec" + (" alt" if s.get("alt") else "") + (" dark" if s.get("dark") else "")
    return (f'<section class="{cls}" id="{s["id"]}"{" style=" + chr(34) + s["style"] + chr(34) if s.get("style") else ""}>'
            f'<div class="wrap">{head}{body}</div></section>')


def form(c: dict) -> str:
    """Заявка: поля [(name, label, type, opts, required)], ok — текст после отправки (на сайте ничего не отправляется)."""
    f = c["form"]
    def field(x):
        n, lab, typ = x[0], x[1], x[2]
        opts = x[3] if len(x) > 3 else None
        req = " required" if (len(x) > 4 and x[4]) else ""
        dn = f' data-n="{e(lab.lower())}"'
        if typ == "select":
            ctl = f'<select name="{n}"{req}{dn}>' + "".join(f"<option>{e(o)}</option>" for o in opts) + "</select>"
        elif typ == "textarea":
            ctl = f'<textarea name="{n}" placeholder="{e(opts or "")}"{req}{dn}></textarea>'
        else:
            ctl = f'<input name="{n}" type="{typ}" placeholder="{e(opts or "")}"{req}{dn}{" inputmode=tel autocomplete=tel" if typ == "tel" else ""}>'
        return f"<label>{e(lab)}{ctl}</label>"
    rows = []
    fl = f["fields"]
    i = 0
    while i < len(fl):
        if i + 1 < len(fl) and fl[i][2] not in ("textarea",) and fl[i + 1][2] not in ("textarea",) and f.get("pairs", True):
            rows.append(f'<div class="row2">{field(fl[i])}{field(fl[i + 1])}</div>')
            i += 2
        else:
            rows.append(field(fl[i]))
            i += 1
    return (f'<form class="form rv" id="{f.get("id", "lead")}" novalidate data-ok="{e(f["ok"])}"><div class="fl" style="display:grid;gap:14px">'
            f'{"<h3 style=" + chr(34) + "font-size:26px" + chr(34) + ">" + f["title"] + "</h3>" if f.get("title") else ""}'
            + "".join(rows) + f'<button class="btn" type="submit">{e(f.get("btn", "Отправить заявку"))}</button>'
            f'<p class="note">Нажимая кнопку, вы соглашаетесь на обработку персональных данных. Перезвоним в рабочее время.</p></div>'
            f'<p class="ok" role="status"></p></form>')


def build(c: dict) -> str:
    d = out(c["slug"])
    I = c.get("images", {})
    write_images(d, I)
    th = dict(c["theme"])
    for k in ("line", "line2", "soft", "mut"):  # тёмная секция с белой формой — исходные цвета формы
        th[k + "0"] = th[k] if k in th else "#ddd"
    font_css = fonts(d, c["fonts"])
    css_vars = ";".join(f"--{k}:{v}" for k, v in th.items())
    H = c["hero"]
    nav = "".join(f'<a href="#{a}">{e(b)}</a>' for a, b in c["nav"])
    tel = c["phone"]
    pts = "".join(f"<span>{e(x)}</span>" for x in H.get("points", []))
    if H.get("full"):
        hero = (f'<section class="hero full" id="top"><div class="bgph">{img(H["img"], I, "100vw", H.get("alt", ""), eager=True)}</div>'
                f'<div class="wrap g"><div class="rv"><div class="kick">{e(H["kicker"])}</div><h1>{H["h1"]}</h1><p class="lead">{H["lead"]}</p>'
                f'<div class="acts"><a class="btn" href="#{H.get("go", "lead")}">{e(H["cta"])}</a>'
                + (f'<a class="btn g" href="#{H["go2"][0]}">{e(H["go2"][1])}</a>' if H.get("go2") else "")
                + f'</div><div class="pts">{pts}</div></div></div></section>')
    else:
        visual = (img(H["img"], I, "(max-width:860px) 100vw, 50vw", H.get("alt", ""), eager=True) if H.get("img") else H.get("art", ""))
        tag = f'<div class="tag">{H["tag"]}</div>' if H.get("tag") else ""
        hero = (f'<section class="hero" id="top"><div class="wrap g"><div class="rv"><div class="kick">{e(H["kicker"])}</div><h1>{H["h1"]}</h1>'
                f'<p class="lead">{H["lead"]}</p><div class="acts"><a class="btn" href="#{H.get("go", "lead")}">{e(H["cta"])}</a>'
                + (f'<a class="btn g" href="#{H["go2"][0]}">{e(H["go2"][1])}</a>' if H.get("go2") else "")
                + f'</div><div class="pts">{pts}</div></div><div class="hph rv" style="--har:{H.get("ar", "4/5")}">{visual}{tag}</div></div></section>')
    C = c["contact"]
    contacts = "".join(f"<div><span>{e(a)}</span><b>{b}</b></div>" for a, b in C["rows"])
    lead_sec = (f'<section class="sec{" " + C["cls"] if C.get("cls") else ""}" id="lead"><div class="wrap split">'
                f'<div class="rv"><div class="kick">{e(C["kick"])}</div><h2 style="font-size:clamp(32px,4.4vw,58px);margin:14px 0 18px">{C["h2"]}</h2>'
                f'<p class="lead">{C["lead"]}</p><div class="contacts" style="margin-top:30px">{contacts}</div>'
                + (f'<div class="map" style="margin-top:26px">{C["map"]}</div>' if C.get("map") else "")
                + f'</div>{form(c)}</div></section>')
    mail = c["mail"]
    page = f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(c['title'])}</title>
<meta name="description" content="{e(c['desc'])}">
<meta property="og:type" content="website">
<meta property="og:locale" content="ru_RU">
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
<header class="top"><div class="wrap in"><a class="logo" href="#top">{c.get('logo', '')}<span>{e(c['brand'])}</span></a>
<nav aria-label="Разделы">{nav}</nav><a class="tel" href="tel:{tel[0]}">{e(tel[1])}</a><a class="btn" href="#lead">{e(c.get('topCta', 'Оставить заявку'))}</a>
<button class="burger" type="button" aria-label="Меню" aria-expanded="false"><i></i></button></div>
<nav class="mnav" aria-label="Меню">{nav}<a href="tel:{tel[0]}">{e(tel[1])}</a></nav></header>
<main>
{hero}
{''.join(render(s, I) for s in c['sections'])}
{lead_sec}
</main>
<footer class="foot"><div class="wrap in"><span>© 2026 {e(c['legal'])}</span><span><a href="#" data-mail="{e(mail)}">{e(mail)}</a></span>
<span>Сайт разработан <a href="https://ysddev.com" target="_blank" rel="noopener">YSD DEV</a></span></div></footer>
<script>window.SITE={jdump(c.get('data', {}))};</script>
<script>{JS}</script>
{('<script>' + c['js'] + '</script>') if c.get('js') else ''}
</body>
</html>
"""
    save(d, page)
    return d
