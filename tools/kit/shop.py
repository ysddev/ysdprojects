"""Интернет-магазин для портфолио: каталог с фильтрами и поиском, карточка товара с опциями, избранное, корзина,
промокод, оформление в 3 шага. Внешний вид — тема и один из четырёх макетов (mega / editorial / lookbook / play),
нишевая фишка — свой блок widget (html + js)."""
from __future__ import annotations

from .common import e, favicon, fonts, img, jdump, out, save, write_images

BASE_CSS = r"""
*,*::before,*::after{box-sizing:border-box}
[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;scroll-padding-top:88px;overflow-x:clip}
body{margin:0;background:var(--bg);color:var(--ink);font:400 16px/1.55 var(--fb);-webkit-font-smoothing:antialiased;overflow-x:clip}
.grid2>*,.layout>*,.cols>*,.feat *{min-width:0}
.sub input,.promo input,.dsub input{min-width:0}
h1,h2,h3{overflow-wrap:break-word;hyphens:auto}
img{max-width:100%;display:block;height:auto}
a{color:inherit;text-decoration:none}
button,input,select,textarea{font:inherit;color:inherit}
button{cursor:pointer;background:none;border:0;padding:0}
:focus-visible{outline:2px solid var(--ac);outline-offset:3px;border-radius:6px}
.wrap{width:min(1320px,100% - 2*var(--gut));margin-inline:auto}
:root{--gut:clamp(16px,4vw,48px)}
h1,h2,h3,h4{font-family:var(--fh);font-weight:var(--hw);letter-spacing:var(--ht);text-transform:var(--hc);line-height:1.04;margin:0}
h2{font-size:clamp(30px,4.4vw,58px)}
h3{font-size:clamp(20px,2vw,26px);line-height:1.15}
p{margin:0}
.kick{font:500 12px/1 var(--fm);letter-spacing:.14em;text-transform:uppercase;color:var(--mut)}
.lead{font-size:clamp(17px,1.6vw,20px);color:var(--soft);max-width:56ch}
.sec{padding:clamp(64px,9vw,128px) 0}
.sec-h{display:flex;align-items:end;justify-content:space-between;gap:24px;margin-bottom:clamp(28px,4vw,48px);flex-wrap:wrap}
.sec-h .lead{margin-top:14px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;height:52px;padding:0 26px;border-radius:var(--rb);background:var(--ac);color:var(--aci);font-weight:600;letter-spacing:.01em;transition:transform .2s,box-shadow .2s,background .2s;white-space:nowrap}
.btn:hover{transform:translateY(-1px);box-shadow:0 10px 30px -12px var(--ac)}
.btn:active{transform:translateY(0)}
.btn.ghost{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--line2)}
.btn.ghost:hover{box-shadow:inset 0 0 0 1.5px var(--ink)}
.btn.sm{height:42px;padding:0 18px;font-size:15px}
.btn.wide{width:100%}
.btn[disabled]{opacity:.45;pointer-events:none}
.chip{display:inline-flex;align-items:center;gap:8px;height:38px;padding:0 16px;border-radius:999px;box-shadow:inset 0 0 0 1px var(--line);font-size:14px;transition:.2s;white-space:nowrap;background:var(--bg)}
.chip:hover{box-shadow:inset 0 0 0 1px var(--ink)}
.chip[aria-pressed=true]{background:var(--ink);color:var(--bg);box-shadow:none}
.chip i{font-style:normal;opacity:.55;font-size:12px}
.badge{display:inline-block;font:600 11px/1 var(--fb);letter-spacing:.06em;text-transform:uppercase;padding:6px 8px;border-radius:6px;background:var(--ac);color:var(--aci)}
.badge.alt{background:var(--ink);color:var(--bg)}
.muted{color:var(--mut)}
.icon{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
/* шапка */
.top{position:sticky;top:0;z-index:40;background:color-mix(in srgb,var(--bg) 82%,transparent);backdrop-filter:saturate(1.4) blur(16px);-webkit-backdrop-filter:saturate(1.4) blur(16px);border-bottom:1px solid transparent;transition:border-color .3s}
.top.scrolled{border-bottom-color:var(--line)}
.top .bar{display:flex;align-items:center;gap:clamp(12px,2.4vw,32px);height:72px}
.logo{font-family:var(--fh);font-weight:var(--lw,700);font-size:24px;letter-spacing:var(--lt,-.02em);white-space:nowrap;display:flex;align-items:center;gap:10px}
.logo b{display:grid;place-items:center;width:34px;height:34px;border-radius:var(--rl,10px);background:var(--ac);color:var(--aci);font-size:18px}
.nav{display:flex;gap:clamp(14px,2vw,28px);font-size:15px;color:var(--soft)}
.nav a:hover{color:var(--ink)}
.tools{margin-left:auto;display:flex;align-items:center;gap:6px}
.search{position:relative;display:flex;align-items:center}
.search input{width:clamp(160px,18vw,280px);height:44px;border-radius:999px;border:0;background:var(--card);padding:0 16px 0 42px;box-shadow:inset 0 0 0 1px var(--line);transition:box-shadow .2s}
.search input:focus{outline:0;box-shadow:inset 0 0 0 1.5px var(--ink)}
.search .icon{position:absolute;left:14px;width:18px;height:18px;color:var(--mut)}
.tbtn{position:relative;display:grid;place-items:center;width:44px;height:44px;border-radius:999px;transition:background .2s}
.tbtn:hover{background:var(--card)}
.tbtn .n{position:absolute;top:4px;right:2px;min-width:18px;height:18px;padding:0 5px;border-radius:9px;background:var(--ac);color:var(--aci);font:700 11px/18px var(--fb);text-align:center;transform:scale(0);transition:transform .25s cubic-bezier(.3,1.6,.5,1)}
.tbtn .n.on{transform:scale(1)}
.tbtn.bump{animation:bump .45s}
@keyframes bump{30%{transform:scale(1.18)}60%{transform:scale(.94)}}
.burger{display:none}
.strip{background:var(--ink);color:var(--bg);font-size:13px;text-align:center;padding:9px var(--gut);letter-spacing:.02em}
.strip b{color:var(--ac2,var(--ac))}
/* hero */
.hero{position:relative}
.hero .stats{display:flex;gap:clamp(20px,4vw,48px);margin-top:clamp(28px,4vw,44px);flex-wrap:wrap}
.hero .stats b{display:block;font-family:var(--fh);font-size:clamp(26px,3vw,36px);font-weight:var(--hw);letter-spacing:-.02em;line-height:1}
.hero .stats span{font-size:13px;color:var(--mut)}
.hero h1{font-size:clamp(44px,7.4vw,112px);line-height:.95}
.hero h1 em{font-style:var(--emst,italic);color:var(--ac);font-family:var(--fe,var(--fh))}
.hero .cta{display:flex;gap:12px;margin-top:clamp(24px,3vw,36px);flex-wrap:wrap}
.ph{position:relative;overflow:hidden;background:var(--card);border-radius:var(--rc)}
.ph img{width:100%;height:100%;object-fit:cover}
/* категории */
.cats{display:grid;grid-template-columns:repeat(var(--cc,4),1fr);gap:var(--gap,16px)}
.cat{position:relative;display:flex;flex-direction:column;justify-content:end;min-height:clamp(180px,22vw,300px);padding:20px;border-radius:var(--rc);overflow:hidden;color:#fff;isolation:isolate;text-align:left}
.cat img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;transition:transform .9s cubic-bezier(.2,.7,.2,1)}
.cat::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,transparent 35%,rgba(0,0,0,.62))}
.cat:hover img{transform:scale(1.06)}
.cat b{font-family:var(--fh);font-weight:var(--hw);font-size:clamp(20px,2vw,26px);letter-spacing:var(--ht);line-height:1.1}
.cat span{font-size:13px;opacity:.82;margin-top:4px}
/* каталог */
.cat-tools{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-bottom:22px}
.cat-tools .chips{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding:2px;flex:1;min-width:0}
.cat-tools .chips::-webkit-scrollbar{display:none}
.sel{height:40px;border-radius:999px;border:0;padding:0 36px 0 16px;background:var(--card) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%23888' fill='none' stroke-width='1.6'/%3E%3C/svg%3E") no-repeat right 14px center;box-shadow:inset 0 0 0 1px var(--line);appearance:none;font-size:14px}
.layout{display:grid;grid-template-columns:minmax(0,1fr);gap:28px}
.side{display:none}
.v-mega .layout{grid-template-columns:250px minmax(0,1fr)}
.v-mega .side{display:block;position:sticky;top:96px;align-self:start}
.side h4{font:600 13px/1 var(--fb);letter-spacing:.08em;text-transform:uppercase;color:var(--mut);margin:22px 0 12px}
.side h4:first-child{margin-top:0}
.side label{display:flex;align-items:center;gap:10px;padding:6px 0;font-size:15px;cursor:pointer}
.side input[type=checkbox]{width:18px;height:18px;accent-color:var(--ac)}
.range{display:flex;gap:8px}
.range input{width:100%;height:40px;border-radius:10px;border:0;padding:0 12px;background:var(--card);box-shadow:inset 0 0 0 1px var(--line)}
.grid{display:grid;grid-template-columns:repeat(var(--pc,4),minmax(0,1fr));gap:clamp(14px,2vw,24px) clamp(12px,1.6vw,20px)}
.v-mega .grid{--pc:3}
.card{position:relative;display:flex;flex-direction:column;border-radius:var(--rc);background:var(--cardbg,transparent);transition:transform .35s cubic-bezier(.2,.7,.2,1),box-shadow .35s}
.card .ph{aspect-ratio:var(--ar,4/5);cursor:pointer}
.card .ph img{transition:transform .9s cubic-bezier(.2,.7,.2,1),opacity .4s}
.card:hover .ph img{transform:scale(1.045)}
.card .tags{position:absolute;top:12px;left:12px;display:flex;gap:6px;z-index:2}
.fav{position:absolute;top:10px;right:10px;z-index:2;display:grid;place-items:center;width:38px;height:38px;border-radius:50%;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(8px);transition:transform .2s}
.fav:hover{transform:scale(1.08)}
.fav svg{width:18px;height:18px;stroke:var(--ink);fill:none;stroke-width:1.8}
.fav[aria-pressed=true] svg{fill:var(--ac);stroke:var(--ac)}
.card .body{padding:14px var(--cpad,2px) var(--cpadb,4px);display:flex;flex-direction:column;gap:6px;flex:1}
.card .nm{font-weight:500;font-size:16px;line-height:1.3;cursor:pointer}
.card .meta{font-size:13px;color:var(--mut)}
.card .row{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:auto;padding-top:8px}
.price{font-family:var(--fp,var(--fb));font-weight:700;font-size:19px;letter-spacing:-.01em;white-space:nowrap}
.price s{font-weight:400;font-size:14px;color:var(--mut);margin-left:6px}
.add{display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 16px;border-radius:var(--rb);background:var(--ink);color:var(--bg);font-weight:600;font-size:14px;transition:background .2s,transform .2s}
.add:hover{background:var(--ac);color:var(--aci)}
.add.done{background:var(--ok);color:#fff}
.stars{color:var(--star,#f5a524);font-size:13px;letter-spacing:1px}
.empty{grid-column:1/-1;padding:60px 0;text-align:center;color:var(--mut)}
.more{display:flex;justify-content:center;margin-top:36px}
/* блок-фишка */
.feat{background:var(--fbg,var(--card));color:var(--fink,var(--ink));border-radius:var(--rs,28px);padding:clamp(24px,5vw,64px);position:relative;overflow:hidden}
/* преимущества / доставка */
.usp{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border-radius:var(--rc);overflow:hidden}
.usp div{background:var(--bg);padding:clamp(20px,2.4vw,32px)}
.usp b{display:block;font-family:var(--fh);font-weight:var(--hw);font-size:20px;letter-spacing:var(--ht);margin-bottom:8px;line-height:1.15}
.usp p{font-size:15px;color:var(--soft)}
.usp .num{font:500 12px/1 var(--fm);color:var(--ac);margin-bottom:22px;letter-spacing:.1em}
.faq{max-width:900px}
.faq details{border-top:1px solid var(--line);padding:4px 0}
.faq details:last-child{border-bottom:1px solid var(--line)}
.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;gap:20px;padding:20px 0;font-size:clamp(17px,1.6vw,20px);font-weight:500}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-size:26px;line-height:1;transition:transform .3s;color:var(--mut)}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq details p{padding:0 0 22px;color:var(--soft);max-width:70ch}
.foot{background:var(--fot,var(--ink));color:var(--fotx,var(--bg));padding:clamp(48px,7vw,96px) 0 28px}
.foot .cols{display:grid;grid-template-columns:2fr 1fr 1fr 1.3fr;gap:32px}
.foot h5{font:600 12px/1 var(--fb);letter-spacing:.12em;text-transform:uppercase;opacity:.55;margin:0 0 16px}
.foot ul{list-style:none;margin:0;padding:0;display:grid;gap:10px;font-size:15px}
.foot a:hover{opacity:.7}
.foot .big{font-family:var(--fh);font-weight:var(--hw);font-size:clamp(28px,3vw,40px);letter-spacing:var(--ht);line-height:1.05;max-width:16ch}
.foot .imprint{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:56px;padding-top:24px;border-top:1px solid color-mix(in srgb,currentColor 16%,transparent);font-size:13px;opacity:.6}
.sub{display:flex;gap:8px;margin-top:20px;max-width:420px}
.sub input{flex:1;height:48px;border-radius:var(--rb);border:0;padding:0 16px;background:color-mix(in srgb,currentColor 9%,transparent);color:inherit}
/* модалки */
dialog{border:0;padding:0;color:var(--ink);background:var(--bg);max-width:none;max-height:none}
dialog::backdrop{background:rgba(10,10,12,.5);backdrop-filter:blur(3px)}
.drawer{position:fixed;inset:0 0 0 auto;width:min(480px,100vw);height:100dvh;margin:0;display:flex;flex-direction:column;transform:translateX(100%);transition:transform .38s cubic-bezier(.2,.8,.2,1)}
.drawer[open]{display:flex}
.drawer.in{transform:none}
.d-head{display:flex;align-items:center;justify-content:space-between;padding:20px 24px;border-bottom:1px solid var(--line)}
.d-head h2{font-size:24px}
.d-body{flex:1;overflow:auto;padding:8px 24px 24px}
.d-foot{padding:18px 24px 24px;border-top:1px solid var(--line);display:grid;gap:12px;background:var(--bg)}
.x{display:grid;place-items:center;width:40px;height:40px;border-radius:50%;font-size:22px;line-height:1}
.x:hover{background:var(--card)}
.line{display:grid;grid-template-columns:78px 1fr auto;gap:14px;padding:16px 0;border-bottom:1px solid var(--line);align-items:center}
.line .ph{width:78px;aspect-ratio:1;border-radius:12px}
.line .t{font-weight:500;font-size:15px;line-height:1.3}
.line .o{font-size:13px;color:var(--mut)}
.qty{display:inline-flex;align-items:center;border-radius:999px;box-shadow:inset 0 0 0 1px var(--line);margin-top:8px}
.qty button{width:32px;height:32px;font-size:18px;border-radius:50%}
.qty button:hover{background:var(--card)}
.qty span{min-width:22px;text-align:center;font-weight:600;font-size:14px}
.line .r{text-align:right;display:grid;gap:8px;justify-items:end}
.rm{font-size:13px;color:var(--mut);text-decoration:underline;text-underline-offset:3px}
.sum{display:flex;justify-content:space-between;font-size:15px;color:var(--soft)}
.sum.tot{font-size:20px;color:var(--ink);font-weight:700}
.promo{display:flex;gap:8px}
.promo input{flex:1;height:44px;border-radius:12px;border:0;padding:0 14px;background:var(--card);box-shadow:inset 0 0 0 1px var(--line);text-transform:uppercase}
.goal{font-size:13px;color:var(--soft)}
.goal i{display:block;height:4px;border-radius:2px;background:var(--line);margin-top:8px;overflow:hidden}
.goal i::after{content:"";display:block;height:100%;width:var(--p,0%);background:var(--ac);transition:width .5s}
.steps{display:flex;gap:6px;margin:18px 0 22px}
.steps span{flex:1;height:4px;border-radius:2px;background:var(--line)}
.steps span.on{background:var(--ac)}
.f{display:grid;gap:14px}
.f label{display:grid;gap:6px;font-size:13px;color:var(--soft)}
.f input,.f textarea{height:50px;border-radius:12px;border:0;padding:0 14px;background:var(--card);box-shadow:inset 0 0 0 1px var(--line);font-size:16px;color:var(--ink)}
.f textarea{height:84px;padding:12px 14px;resize:vertical}
.f input:focus,.f textarea:focus{outline:0;box-shadow:inset 0 0 0 1.5px var(--ink)}
.f .err{box-shadow:inset 0 0 0 1.5px #e5484d}
.opt{display:grid;gap:10px}
.opt label{display:flex;gap:12px;align-items:center;padding:14px 16px;border-radius:14px;box-shadow:inset 0 0 0 1px var(--line);cursor:pointer;color:var(--ink);font-size:15px}
.opt label:has(input:checked){box-shadow:inset 0 0 0 2px var(--ink)}
.opt input{accent-color:var(--ac);width:18px;height:18px}
.opt small{margin-left:auto;color:var(--mut);white-space:nowrap}
.slots{display:flex;gap:8px;flex-wrap:wrap}
.slots button{height:40px;padding:0 14px;border-radius:10px;box-shadow:inset 0 0 0 1px var(--line);font-size:14px}
.slots button[aria-pressed=true]{background:var(--ink);color:var(--bg)}
.done{text-align:center;padding:40px 10px}
.done .ok{width:72px;height:72px;border-radius:50%;background:var(--ok);display:grid;place-items:center;margin:0 auto 20px;color:#fff;font-size:34px;animation:pop .5s cubic-bezier(.3,1.6,.5,1)}
@keyframes pop{from{transform:scale(.3);opacity:0}}
.done h3{font-size:28px;margin-bottom:10px}
.done p{color:var(--soft);margin-bottom:8px}
.modal{width:min(1040px,100vw - 24px);max-height:min(92dvh,820px);border-radius:var(--rs,24px);overflow:hidden;margin:auto;opacity:0;transform:translateY(16px) scale(.98);transition:opacity .3s,transform .35s cubic-bezier(.2,.8,.2,1)}
.modal.in{opacity:1;transform:none}
.pv{display:grid;grid-template-columns:1.05fr 1fr;max-height:min(92dvh,820px)}
.pv .gal{position:relative;background:var(--card);min-height:420px}
.pv .gal img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.pv .info{padding:clamp(22px,3vw,40px);overflow:auto;display:flex;flex-direction:column;gap:16px}
.pv .info h3{font-size:clamp(24px,2.6vw,34px)}
.pv .x{position:absolute;top:14px;right:14px;background:var(--bg);z-index:3}
.pv .desc{color:var(--soft);font-size:15px}
.opts{display:grid;gap:14px}
.opts .og b{display:block;font-size:13px;font-weight:600;margin-bottom:8px;color:var(--soft)}
.opts .og div{display:flex;gap:8px;flex-wrap:wrap}
.opts button{min-width:44px;height:40px;padding:0 14px;border-radius:10px;box-shadow:inset 0 0 0 1px var(--line);font-size:14px}
.opts button[aria-pressed=true]{box-shadow:inset 0 0 0 2px var(--ink);font-weight:600}
.opts button.sw{min-width:34px;width:34px;height:34px;border-radius:50%;padding:0;box-shadow:inset 0 0 0 3px var(--bg),0 0 0 1px var(--line)}
.opts button.sw[aria-pressed=true]{box-shadow:inset 0 0 0 3px var(--bg),0 0 0 2px var(--ink)}
.specs{display:grid;grid-template-columns:auto 1fr;gap:8px 18px;font-size:14px;margin:0}
.specs dt{color:var(--mut)}
.specs dd{margin:0}
.buy{display:flex;gap:10px;align-items:center;margin-top:auto;padding-top:8px;flex-wrap:wrap}
.stock{font-size:13px;color:var(--ok)}
.toast{position:fixed;left:50%;bottom:24px;z-index:90;transform:translate(-50%,140%);visibility:hidden;background:var(--ink);color:var(--bg);padding:14px 20px;border-radius:14px;font-size:15px;box-shadow:0 20px 50px -20px rgba(0,0,0,.5);transition:transform .4s cubic-bezier(.2,.9,.2,1);display:flex;gap:14px;align-items:center;max-width:calc(100vw - 32px)}
.toast.on{transform:translate(-50%,0);visibility:visible}
.toast button{color:var(--ac2,var(--ac));font-weight:600}
.reveal{opacity:0;transform:translateY(24px);transition:opacity .8s cubic-bezier(.2,.7,.2,1),transform .8s cubic-bezier(.2,.7,.2,1)}
.reveal.on{opacity:1;transform:none}
.nofx .reveal{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important;scroll-behavior:auto!important}.reveal{opacity:1;transform:none}}
/* макеты */
.v-editorial .hero .grid2{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(24px,4vw,64px);align-items:center;padding:clamp(32px,5vw,72px) 0 clamp(48px,6vw,96px)}
.v-editorial .hero .ph{aspect-ratio:4/5;border-radius:var(--rh,var(--rc))}
.v-editorial .hero .float{position:absolute;left:-28px;bottom:36px;background:var(--bg);border-radius:18px;padding:16px 18px;box-shadow:0 24px 60px -30px rgba(0,0,0,.45);display:flex;gap:14px;align-items:center;max-width:300px}
.v-editorial .hero .float .ph{width:56px;height:56px;aspect-ratio:1;border-radius:12px;flex:none}
.v-lookbook .hero{height:min(100svh - 72px,920px);min-height:560px;color:#fff;display:flex;align-items:end;isolation:isolate}
.v-lookbook .hero .bg{position:absolute;inset:0;z-index:-2}
.v-lookbook .hero .bg img{width:100%;height:100%;object-fit:cover}
.v-lookbook .hero::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(0,0,0,.15),rgba(0,0,0,.05) 40%,rgba(0,0,0,.7))}
.v-lookbook .hero .wrap{padding-bottom:clamp(36px,6vw,80px)}
.v-lookbook .hero .lead{color:rgba(255,255,255,.86)}.v-lookbook .hero .kick{color:rgba(255,255,255,.78)}
.v-lookbook .hero .stats span{color:rgba(255,255,255,.7)}
.v-lookbook .hero .btn.ghost{color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.6)}
.v-mega .hero{padding:24px 0 0}
.v-mega .hero .grid2{display:grid;grid-template-columns:1.6fr 1fr;gap:16px}
.v-mega .hero .main{position:relative;border-radius:var(--rc);overflow:hidden;color:#fff;min-height:clamp(380px,40vw,540px);display:flex;flex-direction:column;justify-content:end;padding:clamp(24px,4vw,48px);isolation:isolate}
.v-mega .hero .main img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2}
.v-mega .hero .main::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(0,0,0,.78),rgba(0,0,0,.2) 70%)}
.v-mega .hero h1{font-size:clamp(38px,5.2vw,76px)}
.v-mega .hero .lead{color:rgba(255,255,255,.84)}
.v-mega .hero .stats span{color:rgba(255,255,255,.7)}
.v-mega .hero .aside{display:grid;gap:16px;grid-template-rows:1fr 1fr}
.v-mega .hero .tile{position:relative;border-radius:var(--rc);overflow:hidden;padding:22px;display:flex;flex-direction:column;justify-content:space-between;background:var(--card)}
.v-mega .hero .tile.dark{background:var(--ink);color:var(--bg)}
.v-mega .hero .tile b{font-family:var(--fh);font-size:clamp(20px,2vw,28px);font-weight:var(--hw);line-height:1.1;letter-spacing:var(--ht);max-width:14ch}
.v-mega .hero .tile>div,.v-mega .hero .tile>span{position:relative;z-index:2;max-width:58%}.v-mega .hero .tile img{position:absolute;right:-5%;bottom:-10%;width:44%;aspect-ratio:1;object-fit:cover;border-radius:16px;transform:rotate(-5deg);box-shadow:0 20px 40px -20px rgba(0,0,0,.5);transition:transform .6s cubic-bezier(.2,.7,.2,1)}.v-mega .hero .tile:hover img{transform:rotate(-2deg) scale(1.04)}.v-mega .hero .btn.ghost{color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.5)}.v-mega .hero .btn.ghost:hover{box-shadow:inset 0 0 0 1.5px #fff}.v-mega .hero .main .kick{color:rgba(255,255,255,.7)}
.v-play .hero{padding:clamp(24px,4vw,48px) 0 clamp(40px,5vw,80px)}
.v-play .hero .grid2{display:grid;grid-template-columns:1fr 1fr;gap:clamp(20px,3vw,40px);align-items:center;background:var(--hbg,var(--card));border-radius:var(--rs,36px);padding:clamp(24px,5vw,72px);position:relative;overflow:hidden}
.v-play .hero .bubbles{position:relative;aspect-ratio:1}
.v-play .hero .bubbles .ph{position:absolute;border-radius:50%;box-shadow:0 30px 60px -30px rgba(0,0,0,.35)}
.v-play .hero .bubbles .b1{inset:0 18% 18% 0}
.v-play .hero .bubbles .b2{width:44%;height:44%;right:0;bottom:0;border:8px solid var(--hbg,var(--card))}
.v-play .hero .bubbles .b3{width:26%;height:26%;right:6%;top:4%;border:6px solid var(--hbg,var(--card))}
.v-play h1 em{font-style:normal}
.marquee{overflow:hidden;white-space:nowrap;border-block:1px solid var(--line);padding:16px 0;font-family:var(--fh);font-weight:var(--hw);font-size:clamp(20px,2.4vw,30px);letter-spacing:var(--ht);text-transform:var(--hc)}
.marquee div{display:inline-flex;gap:48px;animation:mq 40s linear infinite;padding-right:48px}
.marquee span::after{content:"✦";margin-left:48px;color:var(--ac)}
@keyframes mq{to{transform:translateX(-50%)}}
.v-mega .layout{} @media (max-width:1100px){.v-mega .layout{grid-template-columns:minmax(0,1fr)}.v-mega .side{display:none}.grid{--pc:3}.foot .cols{grid-template-columns:1fr 1fr}.usp{grid-template-columns:1fr 1fr}}
@media (max-width:860px){
 .nav{display:none}.burger{display:grid}.search{display:none}
 .top .bar{height:62px}
 .v-editorial .hero .grid2,.v-mega .hero .grid2,.v-play .hero .grid2{grid-template-columns:1fr}
 .v-editorial .hero .float{left:12px;bottom:12px}
 .v-mega .hero .aside{grid-template-columns:1fr 1fr;grid-template-rows:none}
 .cats{--cc:2}
 .grid,.v-mega .grid{--pc:2}
 .pv{grid-template-columns:1fr}.pv .gal{min-height:300px;aspect-ratio:4/3}
 .modal{width:100vw;max-height:100dvh;height:100dvh;border-radius:0;margin:0}
 .pv{max-height:100dvh;height:100dvh;overflow:auto;display:block}.pv .info{overflow:visible}
}
@media (max-width:560px){
 .usp{grid-template-columns:1fr}.foot .cols{grid-template-columns:1fr}
 .card .row{flex-direction:column;align-items:stretch}.add{justify-content:center}
 .v-mega .hero .aside{grid-template-columns:1fr}
 .hero .cta .btn{flex:1}
 .tools .tbtn.fv{display:none}
}
.mnav{position:fixed;inset:0;z-index:60;background:var(--bg);padding:20px var(--gut);display:none;flex-direction:column;gap:6px}
.mnav.on{display:flex}
.mnav a{font-family:var(--fh);font-weight:var(--hw);font-size:32px;padding:8px 0;letter-spacing:var(--ht)}
.mnav .search{display:flex;margin:16px 0}.mnav .search input{width:100%}
"""

JS = r"""
(function(){
var C=window.SHOPCFG,P=C.products,KEY='ysd-'+C.slug,st={cart:[],fav:[],promo:''};
try{var s=JSON.parse(localStorage.getItem(KEY)||'null');if(s)st=Object.assign(st,s)}catch(_){}
function save(){try{localStorage.setItem(KEY,JSON.stringify(st))}catch(_){}}
var $=function(s,r){return(r||document).querySelector(s)},$$=function(s,r){return[].slice.call((r||document).querySelectorAll(s))};
var fmt=function(n){return(Math.round(n)).toString().replace(/\B(?=(\d{3})+(?!\d))/g,' ')+' ₽'};
var esc=function(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
var byId={};P.forEach(function(p){byId[p.id]=p});
function im(name,sizes,cls){var I=C.img[name];if(!I)return'';var ws=I[3].split(',');var ss=ws.map(function(w){return'img/'+name+'-'+w+'.webp '+w+'w'}).join(', ');return'<img src="img/'+name+'-'+ws[Math.min(1,ws.length-1)]+'.webp" srcset="'+ss+'" sizes="'+(sizes||'(max-width:860px) 50vw, 25vw')+'" alt="" loading="lazy" decoding="async"'+(cls?' class="'+cls+'"':'')+'>'}
var heart='<svg viewBox="0 0 24 24"><path d="M12 20s-7-4.4-9.2-8.6C1.2 8.2 3 4.5 6.6 4.5c2.1 0 3.6 1.2 4.4 2.6.8-1.4 2.3-2.6 4.4-2.6 3.6 0 5.4 3.7 3.8 6.9C19 15.6 12 20 12 20z"/></svg>';
/* ---- каталог */
var F={cat:'all',q:'',sort:'pop',min:'',max:'',checks:{},shown:C.pageSize||12};
function stars(r){r=r||4.8;return'<span class="stars" aria-label="Рейтинг '+r+'">★★★★★</span> <span class="muted" style="font-size:13px">'+r.toFixed(1)+'</span>'}
function list(){
 var q=F.q.trim().toLowerCase(),r=P.filter(function(p){
  if(F.cat!=='all'&&p.cat!==F.cat&&(p.cats||[]).indexOf(F.cat)<0)return false;
  if(q&&(p.n+' '+(p.d||'')+' '+(p.sku||'')+' '+(p.kw||'')).toLowerCase().indexOf(q)<0)return false;
  if(F.min&&p.p<+F.min)return false;if(F.max&&p.p>+F.max)return false;
  for(var k in F.checks){var v=F.checks[k];if(v.length&&v.indexOf((p.f||{})[k])<0)return false}
  if(F.ext&&!F.ext(p))return false;
  return true});
 if(F.sort==='cheap')r.sort(function(a,b){return a.p-b.p});
 if(F.sort==='exp')r.sort(function(a,b){return b.p-a.p});
 if(F.sort==='new')r.sort(function(a,b){return(b.nw?1:0)-(a.nw?1:0)});
 if(F.sort==='sale')r.sort(function(a,b){return(b.old?1:0)-(a.old?1:0)});
 return r}
function card(p,i){
 var fav=st.fav.indexOf(p.id)>=0,tags=(p.tag?'<span class="badge">'+esc(p.tag)+'</span>':'')+(p.old?'<span class="badge alt">−'+Math.round((1-p.p/p.old)*100)+'%</span>':'');
 return'<article class="card reveal" style="transition-delay:'+(i%4)*60+'ms" data-id="'+p.id+'"><div class="ph" data-open="'+p.id+'">'+im(p.img,C.cardSizes)+'</div><div class="tags">'+tags+'</div><button class="fav" type="button" aria-label="В избранное" aria-pressed="'+fav+'" data-fav="'+p.id+'">'+heart+'</button><div class="body"><div class="meta">'+esc(p.m||'')+'</div><div class="nm" data-open="'+p.id+'">'+esc(p.n)+'</div>'+(C.showStars!==false?'<div>'+stars(p.r)+'</div>':'')+'<div class="row"><div class="price">'+fmt(p.p)+(p.old?'<s>'+fmt(p.old)+'</s>':'')+'</div><button class="add" type="button" data-add="'+p.id+'">'+(C.addLabel||'В корзину')+'</button></div></div></article>'}
function render(){
 var r=list(),g=$('#grid');if(!g)return;
 g.innerHTML=r.length?r.slice(0,F.shown).map(card).join(''):'<p class="empty">Ничего не нашлось. Попробуйте другой запрос или сбросьте фильтры.</p>';
 $('#more').hidden=r.length<=F.shown;$('#found').textContent=r.length+' '+plural(r.length,['товар','товара','товаров']);
 observe()}
function plural(n,f){n=Math.abs(n)%100;var a=n%10;return n>10&&n<20?f[2]:a>1&&a<5?f[1]:a==1?f[0]:f[2]}
$$('[data-cat]').forEach(function(b){b.addEventListener('click',function(){setCat(b.dataset.cat);if(b.dataset.jump!==undefined)document.getElementById('catalog').scrollIntoView({behavior:'smooth'})})});
function setCat(c){F.cat=c;F.shown=C.pageSize||12;$$('.chips [data-cat]').forEach(function(x){x.setAttribute('aria-pressed',x.dataset.cat===c)});render()}
var so=$('#sort');if(so)so.addEventListener('change',function(){F.sort=so.value;render()});
$$('.qsearch').forEach(function(inp){inp.addEventListener('input',function(){F.q=inp.value;$$('.qsearch').forEach(function(o){if(o!==inp)o.value=inp.value});render()});inp.addEventListener('keydown',function(ev){if(ev.key==='Enter'){$('.mnav').classList.remove('on');document.getElementById('catalog').scrollIntoView({behavior:'smooth'})}})});
$$('.side [data-check]').forEach(function(b){b.addEventListener('change',function(){var k=b.dataset.check;F.checks[k]=$$('.side [data-check="'+k+'"]:checked').map(function(x){return x.value});render()})});
$$('.range input').forEach(function(i){i.addEventListener('input',function(){F[i.dataset.r]=i.value;render()})});
$('#more').addEventListener('click',function(){F.shown+=8;render()});
/* ---- избранное, корзина */
document.addEventListener('click',function(ev){
 var t=ev.target.closest('[data-fav],[data-add],[data-open],[data-close],[data-go]');if(!t)return;
 if(t.dataset.fav){var id=t.dataset.fav,i=st.fav.indexOf(id);if(i<0)st.fav.push(id);else st.fav.splice(i,1);t.setAttribute('aria-pressed',i<0);save();badges();toast(i<0?'Добавлено в избранное':'Убрано из избранного')}
 else if(t.dataset.add){var p=byId[t.dataset.add];if(p.opts&&Object.keys(p.opts).length&&!t.dataset.quick){openP(p.id);return}add(p.id,defOpts(p),1);t.classList.add('done');t.textContent='✓ В корзине';setTimeout(function(){t.classList.remove('done');t.textContent=C.addLabel||'В корзину'},1600)}
 else if(t.dataset.open){openP(t.dataset.open)}
 else if(t.dataset.go){var el=document.getElementById(t.dataset.go);if(el)el.scrollIntoView({behavior:'smooth'})}
});
function defOpts(p){var o={};for(var k in(p.opts||{}))o[k]=p.opts[k][0].v||p.opts[k][0];return o}
function key(id,o){return id+'|'+JSON.stringify(o||{})}
function add(id,o,q,extra){var k=key(id,o),l=st.cart.filter(function(x){return x.k===k})[0];var p=byId[id];
 if(l)l.q+=q;else st.cart.push({k:k,id:id,o:o||{},q:q,price:(extra&&extra.price)||p.p,name:(extra&&extra.name)||p.n,img:(extra&&extra.img)||p.img});
 save();badges(true);toast('«'+((extra&&extra.name)||p.n)+'» в корзине','Оформить')}
function badges(b){var n=st.cart.reduce(function(s,x){return s+x.q},0),cb=$('#cartN'),fb=$('#favN');cb.textContent=n;cb.classList.toggle('on',n>0);fb.textContent=st.fav.length;fb.classList.toggle('on',st.fav.length>0);if(b){var t=$('#cartBtn');t.classList.remove('bump');void t.offsetWidth;t.classList.add('bump')}}
function totals(){var s=st.cart.reduce(function(a,x){return a+x.price*x.q},0),d=0,pr=C.promo;if(st.promo&&pr&&st.promo===pr.code)d=Math.round(s*pr.pct/100);return{sub:s,disc:d,total:s-d}}
/* ---- тост */
var tt;function toast(m,act){var t=$('#toast');t.innerHTML='<span>'+esc(m)+'</span>'+(act?'<button type="button">'+act+'</button>':'');t.classList.add('on');clearTimeout(tt);tt=setTimeout(function(){t.classList.remove('on')},2800);if(act)t.querySelector('button').onclick=function(){t.classList.remove('on');openCart()}}
/* ---- диалоги */
function showDlg(d){if(!d.open)d.showModal();requestAnimationFrame(function(){requestAnimationFrame(function(){d.classList.add('in')})});document.documentElement.style.overflow='hidden'}
function hideDlg(d){d.classList.remove('in');setTimeout(function(){if(d.open)d.close();if(!$$('dialog[open]').length)document.documentElement.style.overflow=''},320)}
$$('dialog').forEach(function(d){d.addEventListener('click',function(ev){if(ev.target===d||ev.target.closest('[data-x]'))hideDlg(d)});d.addEventListener('cancel',function(ev){ev.preventDefault();hideDlg(d)})});
/* ---- карточка товара */
var cur=null;
function openP(id){var p=byId[id],d=$('#pv');cur={p:p,o:defOpts(p),q:1};
 var opts=Object.keys(p.opts||{}).map(function(k){return'<div class="og"><b>'+esc(k)+'</b><div>'+p.opts[k].map(function(v,i){var val=v.v||v,sw=v.c?'class="sw" style="background:'+v.c+'" title="'+esc(val)+'" aria-label="'+esc(val)+'"':'';return'<button type="button" '+sw+' data-ok="'+esc(k)+'" data-ov="'+esc(val)+'" aria-pressed="'+(i===0)+'">'+(v.c?'':esc(val))+'</button>'}).join('')+'</div></div>'}).join('');
 var specs=(p.s||[]).map(function(x){return'<dt>'+esc(x[0])+'</dt><dd>'+esc(x[1])+'</dd>'}).join('');
 d.innerHTML='<div class="pv"><div class="gal">'+im(p.img,'(max-width:860px) 100vw, 520px')+'<button class="x" type="button" data-x aria-label="Закрыть">×</button></div><div class="info"><div class="kick">'+esc(p.m||'')+'</div><h3>'+esc(p.n)+'</h3>'+(C.showStars!==false?'<div>'+stars(p.r)+' <span class="muted" style="font-size:13px">· '+(p.rc||Math.round(20+((p.p*7)%180)))+' оценок</span></div>':'')+'<div class="price" style="font-size:28px">'+fmt(p.p)+(p.old?'<s>'+fmt(p.old)+'</s>':'')+'</div><p class="desc">'+esc(p.d||'')+'</p>'+(opts?'<div class="opts">'+opts+'</div>':'')+(specs?'<dl class="specs">'+specs+'</dl>':'')+'<div class="stock">● '+esc(p.stock||'В наличии, отправим завтра')+'</div><div class="buy"><div class="qty"><button type="button" data-q="-1">−</button><span id="pvq">1</span><button type="button" data-q="1">+</button></div><button class="btn" type="button" id="pvAdd" style="flex:1">'+(C.addLabel||'В корзину')+' · '+fmt(p.p)+'</button><button class="tbtn" type="button" data-fav="'+p.id+'" aria-pressed="'+(st.fav.indexOf(p.id)>=0)+'" aria-label="В избранное" style="box-shadow:inset 0 0 0 1px var(--line)">'+heart.replace('<svg','<svg class="icon"')+'</button></div></div></div>';
 showDlg(d)}
$('#pv').addEventListener('click',function(ev){var b=ev.target.closest('[data-ok]');if(b){cur.o[b.dataset.ok]=b.dataset.ov;$$('[data-ok="'+b.dataset.ok+'"]',$('#pv')).forEach(function(x){x.setAttribute('aria-pressed',x===b)})}
 var q=ev.target.closest('[data-q]');if(q){cur.q=Math.max(1,cur.q+ +q.dataset.q);$('#pvq').textContent=cur.q;$('#pvAdd').textContent=(C.addLabel||'В корзину')+' · '+fmt(cur.p.p*cur.q)}
 if(ev.target.closest('#pvAdd')){add(cur.p.id,cur.o,cur.q);hideDlg($('#pv'))}});
/* ---- корзина и оформление */
var cart=$('#cart'),step=0,ship=C.ship[0].id,pay='card',slot=null;
function openCart(){step=0;drawCart();showDlg(cart)}
$('#cartBtn').addEventListener('click',openCart);
$('#favBtn').addEventListener('click',function(){if(!st.fav.length){toast('В избранном пока пусто — нажмите ♡ на карточке');return}F.cat='all';F.ext=function(p){return st.fav.indexOf(p.id)>=0};render();document.getElementById('catalog').scrollIntoView({behavior:'smooth'});toast('Показано избранное','Сбросить');$('#toast button').onclick=function(){F.ext=null;render();$('#toast').classList.remove('on')}});
function lineHtml(l,i){var o=Object.keys(l.o||{}).map(function(k){return l.o[k]}).join(' · ');return'<div class="line"><div class="ph">'+im(l.img,'78px')+'</div><div><div class="t">'+esc(l.name)+'</div>'+(o?'<div class="o">'+esc(o)+'</div>':'')+'<div class="qty"><button type="button" data-l="'+i+'" data-d="-1" aria-label="Меньше">−</button><span>'+l.q+'</span><button type="button" data-l="'+i+'" data-d="1" aria-label="Больше">+</button></div></div><div class="r"><b>'+fmt(l.price*l.q)+'</b><button class="rm" type="button" data-rm="'+i+'">Удалить</button></div></div>'}
function drawCart(){var b=$('#cartBody'),f=$('#cartFoot'),t=totals(),h=$('#cartH');
 if(step==='done')return;
 if(!st.cart.length){h.textContent='Корзина';b.innerHTML='<div class="done"><p style="font-size:44px;margin-bottom:8px">🛒</p><h3>Пока пусто</h3><p>'+esc(C.emptyCart||'Загляните в каталог — там много хорошего.')+'</p><button class="btn" type="button" data-x data-go="catalog" style="margin-top:14px">В каталог</button></div>';f.hidden=true;return}
 f.hidden=false;
 if(step===0){h.textContent='Корзина';var free=C.freeFrom,goal=free?(t.sub>=free?'<div class="goal">🎉 Доставка бесплатная</div>':'<div class="goal">До бесплатной доставки — '+fmt(free-t.sub)+'<i style="--p:'+Math.min(100,t.sub/free*100)+'%"></i></div>'):'';
  b.innerHTML=goal+st.cart.map(lineHtml).join('');
  f.innerHTML=(C.promo?'<div class="promo"><input id="pc" placeholder="Промокод" value="'+esc(st.promo)+'" aria-label="Промокод"><button class="btn ghost sm" type="button" id="pcGo">Применить</button></div>'+(C.promo.hint?'<div class="goal">Подсказка: '+esc(C.promo.hint)+'</div>':''):'')+'<div class="sum"><span>Товары</span><span>'+fmt(t.sub)+'</span></div>'+(t.disc?'<div class="sum"><span>Скидка по промокоду</span><span>−'+fmt(t.disc)+'</span></div>':'')+'<div class="sum tot"><span>Итого</span><span>'+fmt(t.total)+'</span></div><button class="btn wide" type="button" id="next">Оформить заказ</button>'}
 else{h.textContent='Оформление';var steps='<div class="steps"><span class="on"></span><span class="'+(step>1?'on':'')+'"></span><span class="'+(step>2?'on':'')+'"></span></div>';
  if(step===1)b.innerHTML=steps+'<form class="f" id="fm" novalidate><b>Контакты</b><label>Имя<input name="nm" autocomplete="name" required></label><label>Телефон<input name="ph" type="tel" inputmode="tel" placeholder="+7 (___) ___-__-__" autocomplete="tel" required></label><label>Почта для чека<input name="em" type="email" autocomplete="email" placeholder="необязательно"></label></form>';
  if(step===2){var sh=C.ship.map(function(s){var price=s.free&&t.sub>=s.free?0:s.price;return'<label><input type="radio" name="sh" value="'+s.id+'" '+(s.id===ship?'checked':'')+'><span><b style="font-weight:600">'+esc(s.name)+'</b><br><span class="muted" style="font-size:13px">'+esc(s.eta)+'</span></span><small>'+(price?fmt(price):'бесплатно')+'</small></label>'}).join('');
   var days=[],d0=new Date();for(var i=1;i<=4;i++){var dd=new Date(d0.getTime()+i*864e5);days.push(dd.toLocaleDateString('ru-RU',{weekday:'short',day:'numeric',month:'short'}))}
   b.innerHTML=steps+'<form class="f" id="fm" novalidate><b>'+esc(C.shipTitle||'Доставка')+'</b><div class="opt">'+sh+'</div><label>Адрес'+(C.addrNote?' <span class="muted">· '+esc(C.addrNote)+'</span>':'')+'<input name="ad" autocomplete="street-address" placeholder="Город, улица, дом, квартира" required></label><b style="margin-top:6px">Когда удобно</b><div class="slots" id="slots">'+days.map(function(x,i){return'<button type="button" aria-pressed="'+(slot===i)+'" data-slot="'+i+'">'+x+'</button>'}).join('')+'</div>'+(C.slotNote?'<p class="muted" style="font-size:13px">'+esc(C.slotNote)+'</p>':'')+'<label>Комментарий<textarea name="cm" placeholder="'+esc(C.commentPh||'Код домофона, этаж')+'"></textarea></label></form>'}
  if(step===3)b.innerHTML=steps+'<form class="f" id="fm"><b>Оплата</b><div class="opt"><label><input type="radio" name="pay" value="card" '+(pay==='card'?'checked':'')+'>Картой онлайн<small>Visa, МИР</small></label><label><input type="radio" name="pay" value="sbp" '+(pay==='sbp'?'checked':'')+'>СБП<small>по QR</small></label><label><input type="radio" name="pay" value="split" '+(pay==='split'?'checked':'')+'>Долями<small>4 × '+fmt(Math.ceil(t.total/4))+'</small></label><label><input type="radio" name="pay" value="cash" '+(pay==='cash'?'checked':'')+'>При получении<small>картой или наличными</small></label></div><div class="sum" style="margin-top:8px"><span>Товары</span><span>'+fmt(t.sub)+'</span></div>'+(t.disc?'<div class="sum"><span>Скидка</span><span>−'+fmt(t.disc)+'</span></div>':'')+'<div class="sum"><span>Доставка</span><span>'+(shipCost()?fmt(shipCost()):'бесплатно')+'</span></div></form>';
  f.innerHTML='<div class="sum tot"><span>К оплате</span><span>'+fmt(t.total+(step===3?shipCost():0))+'</span></div><div style="display:flex;gap:10px"><button class="btn ghost" type="button" id="back">Назад</button><button class="btn" type="button" id="next" style="flex:1">'+(step===3?'Оплатить заказ':'Продолжить')+'</button></div>';
  var ph=$('[name=ph]',b);if(ph)ph.addEventListener('input',mask);
  if(st.form)$$('#fm input,#fm textarea',b).forEach(function(i){if(st.form[i.name])i.value=st.form[i.name]})}
}
function shipCost(){var s=C.ship.filter(function(x){return x.id===ship})[0],t=totals();return s.free&&t.sub>=s.free?0:s.price}
function mask(ev){var v=ev.target.value.replace(/\D/g,'');if(v[0]==='8')v='7'+v.slice(1);if(v&&v[0]!=='7')v='7'+v;v=v.slice(0,11);var o='+7';if(v.length>1)o+=' ('+v.slice(1,4);if(v.length>=4)o+=') '+v.slice(4,7);if(v.length>=7)o+='-'+v.slice(7,9);if(v.length>=9)o+='-'+v.slice(9,11);ev.target.value=v.length?o:''}
cart.addEventListener('input',function(ev){if(ev.target.closest('#fm')){st.form=st.form||{};st.form[ev.target.name]=ev.target.value;save()}});
cart.addEventListener('change',function(ev){if(ev.target.name==='sh'){ship=ev.target.value;drawCart()}if(ev.target.name==='pay')pay=ev.target.value});
cart.addEventListener('click',function(ev){var t=ev.target;
 if(t.dataset.l!==undefined){var l=st.cart[+t.dataset.l];l.q+= +t.dataset.d;if(l.q<1)st.cart.splice(+t.dataset.l,1);save();badges();drawCart()}
 if(t.dataset.rm!==undefined){st.cart.splice(+t.dataset.rm,1);save();badges();drawCart()}
 if(t.dataset.slot!==undefined){slot=+t.dataset.slot;$$('#slots button').forEach(function(x){x.setAttribute('aria-pressed',x===t)})}
 if(t.id==='pcGo'){var v=$('#pc').value.trim().toUpperCase();if(C.promo&&v===C.promo.code){st.promo=v;save();toast('Промокод применён: −'+C.promo.pct+'%')}else{st.promo='';toast('Такого промокода нет')}drawCart()}
 if(t.id==='back'){step--;drawCart()}
 if(t.id==='next'){if(step>0&&!valid())return;if(step===3){finish();return}step++;drawCart();$('#cartBody').scrollTop=0}
});
function valid(){var ok=true;$$('#fm [required]').forEach(function(i){var bad=!i.value.trim()||(i.name==='ph'&&i.value.replace(/\D/g,'').length<11);i.classList.toggle('err',bad);if(bad&&ok){i.focus();ok=false}});if(step===2&&slot===null&&ok){toast('Выберите день доставки');ok=false}return ok}
function finish(){var t=totals(),sum=t.total+shipCost(),name=((st.form||{}).nm||'').split(' ')[0],no=Math.floor(100000+Math.random()*900000);
 step='done';st.cart=[];st.promo='';save();badges();
 $('#cartH').textContent='Готово';$('#cartBody').innerHTML='<div class="done"><div class="ok">✓</div><h3>Заказ №'+no+' принят</h3><p>'+(name?esc(name)+', спасибо! ':'Спасибо! ')+'Сумма — '+fmt(sum)+'. '+esc(C.doneNote||'Мы пришлём SMS, когда заказ поедет к вам.')+'</p><button class="btn" type="button" data-x style="margin-top:18px">Вернуться в магазин</button></div>';$('#cartFoot').hidden=true}
/* ---- меню, шапка, анимации */
$('.burger').addEventListener('click',function(){$('.mnav').classList.add('on')});
$$('.mnav a, .mnav [data-mx]').forEach(function(a){a.addEventListener('click',function(){$('.mnav').classList.remove('on')})});
var top=$('.top');addEventListener('scroll',function(){top.classList.toggle('scrolled',scrollY>8)},{passive:true});
var io='IntersectionObserver'in window?new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('on');io.unobserve(x.target)}})},{rootMargin:'0px 0px -6% 0px'}):null;
function observe(){$$('.reveal:not(.on)').forEach(function(el){io?io.observe(el):el.classList.add('on')})}
$$('.sub').forEach(function(f){f.addEventListener('submit',function(ev){ev.preventDefault();f.innerHTML='<p>Готово! Первое письмо придёт в течение минуты.</p>'})});
window.SHOP={add:add,open:openP,setCat:setCat,fmt:fmt,esc:esc,toast:toast,img:im,products:P,byId:byId,openCart:openCart,filter:function(fn,label){F.ext=fn;F.cat='all';render();document.getElementById('catalog').scrollIntoView({behavior:'smooth'});if(label){toast(label,'Сбросить');$('#toast button').onclick=function(){F.ext=null;render();$('#toast').classList.remove('on')}}}};
render();badges();observe();window.__shop=1;
})();
"""


def ico(name: str) -> str:
    paths = {
        "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
        "heart": '<path d="M12 20s-7-4.4-9.2-8.6C1.2 8.2 3 4.5 6.6 4.5c2.1 0 3.6 1.2 4.4 2.6.8-1.4 2.3-2.6 4.4-2.6 3.6 0 5.4 3.7 3.8 6.9C19 15.6 12 20 12 20z"/>',
        "bag": '<path d="M5 8h14l-1 12H6L5 8z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/>',
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
        "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/>',
    }
    return f'<svg class="icon" viewBox="0 0 24 24" aria-hidden="true">{paths[name]}</svg>'


def build(c: dict) -> str:
    d = out(c["slug"])
    write_images(d, c["images"])
    I = c["images"]
    th = c["theme"]
    font_css = fonts(d, c["fonts"])
    var = c.get("variant", "editorial")
    css_vars = ";".join(f"--{k}:{v}" for k, v in th.items())
    nav = "".join(f'<a href="#{h}">{e(t)}</a>' for t, h in c["nav"])
    search = (f'<label class="search">{ico("search")}<input class="qsearch" type="search" placeholder="{e(c.get("searchPh", "Поиск по каталогу"))}" '
              f'aria-label="Поиск"></label>')
    header = f"""
<header class="top"><div class="wrap bar">
<a class="logo" href="#top" aria-label="{e(c['brand'])}">{c.get('logo') or e(c['brand'])}</a>
<nav class="nav" aria-label="Разделы">{nav}</nav>
<div class="tools">{search}
<button class="tbtn fv" id="favBtn" type="button" aria-label="Избранное">{ico('heart')}<span class="n" id="favN">0</span></button>
<button class="tbtn" id="cartBtn" type="button" aria-label="Корзина">{ico('bag')}<span class="n" id="cartN">0</span></button>
<button class="tbtn burger" type="button" aria-label="Меню">{ico('menu')}</button>
</div></div></header>
<div class="mnav" role="dialog" aria-label="Меню"><div style="display:flex;justify-content:space-between;align-items:center"><span class="logo">{c.get('logo') or e(c['brand'])}</span><button class="x" type="button" data-mx aria-label="Закрыть">×</button></div>
{search}{nav}<a href="#contacts">Контакты</a></div>"""
    strip = f'<div class="strip">{c["strip"]}</div>' if c.get("strip") else ""
    H = c["hero"]
    stats = "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in H.get("stats", []))
    cta = (f'<div class="cta"><a class="btn" href="#{H.get("ctaTo", "catalog")}">{e(H["cta"])}</a>'
           + (f'<a class="btn ghost" href="#{H.get("cta2To", "feat")}">{e(H["cta2"])}</a>' if H.get("cta2") else "") + "</div>")
    text = f'<div class="kick">{e(H["kicker"])}</div><h1 id="h1" style="margin:18px 0 22px">{H["h1"]}</h1><p class="lead">{H["lead"]}</p>{cta}<div class="stats">{stats}</div>'
    if var == "editorial":
        fl = H.get("float")
        float_html = (f'<div class="float"><div class="ph">{img(fl["img"], I, "56px")}</div><div><b style="font-size:15px">{e(fl["t"])}</b>'
                      f'<div class="muted" style="font-size:13px">{e(fl["s"])}</div></div></div>') if fl else ""
        hero = (f'<section class="hero" id="top"><div class="wrap grid2"><div class="reveal">{text}</div><div class="reveal" style="position:relative">'
                f'<div class="ph">{img(H["img"], I, "(max-width:860px) 100vw, 48vw", H.get("alt", ""), eager=True)}</div>{float_html}</div></div></section>')
    elif var == "lookbook":
        hero = (f'<section class="hero" id="top"><div class="bg">{img(H["img"], I, "100vw", H.get("alt", ""), eager=True)}</div>'
                f'<div class="wrap"><div style="max-width:880px">{text}</div></div></section>')
    elif var == "mega":
        tiles = "".join(
            f'<a class="tile{" dark" if i == 0 else ""}" href="#{t.get("to", "catalog")}"{" data-cat=" + chr(34) + t["cat"] + chr(34) + " data-jump" if t.get("cat") else ""}>'
            f'<div><div class="kick" style="color:inherit;opacity:.6">{e(t["k"])}</div><b style="display:block;margin-top:10px">{e(t["t"])}</b></div>'
            f'<span style="font-weight:600;font-size:14px;position:relative;z-index:2">{e(t.get("a", "Смотреть →"))}</span>'
            f'{img(t["img"], I, "220px") if t.get("img") else ""}</a>'
            for i, t in enumerate(H["tiles"]))
        hero = (f'<section class="hero" id="top"><div class="wrap grid2"><div class="main">{img(H["img"], I, "(max-width:860px) 100vw, 62vw", H.get("alt", ""), eager=True)}'
                f'{text}</div><div class="aside">{tiles}</div></div></section>')
    else:  # play
        b = H["bubbles"]
        hero = (f'<section class="hero" id="top"><div class="wrap"><div class="grid2"><div class="reveal">{text}</div>'
                f'<div class="bubbles reveal"><div class="ph b1">{img(b[0], I, "(max-width:860px) 80vw, 40vw", eager=True)}</div>'
                f'<div class="ph b2">{img(b[1], I, "300px")}</div><div class="ph b3">{img(b[2], I, "180px")}</div></div></div></div></section>')
    marquee = ""
    if c.get("marquee"):
        items = "".join(f"<span>{e(x)}</span>" for x in c["marquee"] * 2)
        marquee = f'<div class="marquee" aria-hidden="true"><div>{items}</div></div>'
    cats = "".join(
        f'<button class="cat reveal" type="button" data-cat="{x["id"]}" data-jump style="transition-delay:{i * 60}ms">{img(x["img"], I, "(max-width:860px) 50vw, 25vw")}'
        f'<b>{e(x["n"])}</b><span>{e(x.get("s", ""))}</span></button>' for i, x in enumerate(c["cats"]) if x.get("img"))
    cats_sec = (f'<section class="sec" id="cats" style="padding-bottom:clamp(32px,5vw,64px)"><div class="wrap"><div class="sec-h reveal"><div><div class="kick">{e(c.get("catsKick", "Каталог"))}</div>'
                f'<h2 style="margin-top:14px">{c.get("catsTitle", "Категории")}</h2></div></div><div class="cats" style="--cc:{c.get("catCols", 4)}">{cats}</div></div></section>') if cats else ""
    chips = '<button class="chip" type="button" data-cat="all" aria-pressed="true">Всё</button>' + "".join(
        f'<button class="chip" type="button" data-cat="{x["id"]}" aria-pressed="false">{e(x["n"])} <i>{sum(1 for p in c["products"] if p["cat"] == x["id"] or x["id"] in p.get("cats", []))}</i></button>'
        for x in c["cats"])
    side = ""
    if var == "mega":
        groups = ""
        for key, (label, values) in c.get("facets", {}).items():
            groups += f"<h4>{e(label)}</h4>" + "".join(
                f'<label><input type="checkbox" data-check="{key}" value="{e(v)}">{e(v)}</label>' for v in values)
        side = (f'<aside class="side" aria-label="Фильтры"><h4>Цена, ₽</h4><div class="range"><input data-r="min" inputmode="numeric" placeholder="от" aria-label="Цена от">'
                f'<input data-r="max" inputmode="numeric" placeholder="до" aria-label="Цена до"></div>{groups}</aside>')
    catalog = f"""
<section class="sec" id="catalog"><div class="wrap">
<div class="sec-h reveal"><div><div class="kick">{e(c.get('gridKick', 'Каталог'))}</div><h2 style="margin-top:14px">{c.get('gridTitle', 'Все товары')}</h2></div>
<p class="muted" id="found" aria-live="polite"></p></div>
<div class="cat-tools"><div class="chips" role="group" aria-label="Категории">{chips}</div>
<select class="sel" id="sort" aria-label="Сортировка"><option value="pop">Сначала популярные</option><option value="cheap">Сначала дешевле</option><option value="exp">Сначала дороже</option><option value="new">Новинки</option><option value="sale">Со скидкой</option></select></div>
<div class="layout">{side}<div><div class="grid" id="grid"></div><div class="more"><button class="btn ghost" type="button" id="more">Показать ещё</button></div></div></div>
</div></section>"""
    W = c["widget"]
    widget = (f'<section class="sec" id="feat" style="padding-top:0"><div class="wrap"><div class="feat reveal">{W["html"]}</div></div></section>')
    usp = "".join(f'<div class="reveal" style="transition-delay:{i * 70}ms"><div class="num">0{i + 1}</div><b>{e(a)}</b><p>{e(b)}</p></div>'
                  for i, (a, b) in enumerate(c["usp"]))
    usp_sec = (f'<section class="sec" id="why" style="padding-top:0"><div class="wrap"><div class="sec-h reveal"><div><div class="kick">{e(c.get("uspKick", "Почему мы"))}</div>'
               f'<h2 style="margin-top:14px">{c.get("uspTitle", "Покупать у нас спокойно")}</h2></div></div><div class="usp">{usp}</div></div></section>')
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{a}</p></details>" for q, a in c["faq"])
    faq_sec = (f'<section class="sec" id="faq" style="padding-top:0"><div class="wrap"><div class="sec-h reveal"><div><div class="kick">Вопросы</div>'
               f'<h2 style="margin-top:14px">Частые вопросы</h2></div></div><div class="faq reveal">{faq}</div></div></section>')
    ct = c["contacts"]
    footer = f"""
<footer class="foot" id="contacts"><div class="wrap">
<div class="cols"><div><div class="big">{c['footBig']}</div>
<form class="sub"><input type="email" placeholder="Ваша почта" aria-label="Почта" required><button class="btn" type="submit">Подписаться</button></form>
<p style="font-size:13px;opacity:.6;margin-top:10px">{e(c.get('subNote', 'Новинки и скидки раз в неделю. Без спама.'))}</p></div>
<div><h5>Покупателям</h5><ul><li><a href="#catalog">Каталог</a></li><li><a href="#feat">{e(W['nav'])}</a></li><li><a href="#why">Доставка и оплата</a></li><li><a href="#faq">Возврат</a></li></ul></div>
<div><h5>Компания</h5><ul>{''.join(f'<li><a href="#{h}">{e(t)}</a></li>' for t, h in c['nav'][:3])}<li><a href="#contacts">Контакты</a></li></ul></div>
<div><h5>Связаться</h5><ul><li><a href="tel:+74950000000">{e(ct.get('phone', '+7 (495) 000-00-00'))}</a></li><li>{e(ct['addr'])}</li><li>{e(ct['hours'])}</li></ul></div></div>
<div class="imprint"><span>© 2026 {e(c['brand'])}</span><span>Сайт разработан YSD DEV</span></div>
</div></footer>"""
    dialogs = """
<dialog class="drawer" id="cart" aria-labelledby="cartH"><div class="d-head"><h2 id="cartH">Корзина</h2><button class="x" type="button" data-x aria-label="Закрыть">×</button></div>
<div class="d-body" id="cartBody"></div><div class="d-foot" id="cartFoot"></div></dialog>
<dialog class="modal" id="pv" aria-label="Товар"></dialog>
<div class="toast" id="toast" role="status" aria-live="polite"></div>"""
    cfg = {k: c[k] for k in ("slug", "products", "ship") if k in c}
    for k in ("promo", "freeFrom", "pageSize", "addLabel", "emptyCart", "doneNote", "shipTitle", "addrNote", "slotNote",
              "commentPh", "showStars", "cardSizes"):
        if k in c:
            cfg[k] = c[k]
    cfg["img"] = {k: list(v) for k, v in I.items()}
    extra = "".join(c.get("sections", []))
    order = c.get("order", ["cats", "marquee", "catalog", "widget", "extra", "usp", "faq"])
    blocks = {"cats": cats_sec, "marquee": marquee, "catalog": catalog, "widget": widget, "extra": extra, "usp": usp_sec, "faq": faq_sec}
    body = "".join(blocks[k] for k in order)
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
<meta property="og:type" content="website">
<meta property="og:image" content="img/{H['img']}-{I[H['img']][3].split(',')[-1]}.webp">
<meta name="theme-color" content="{th['bg']}">
<link rel="icon" href="{favicon(c.get('favLetter', c['brand'][0]), th['ac'], th['aci'])}">
<script>document.documentElement.classList.add('js');setTimeout(function(){{if(!window.__shop)document.documentElement.classList.add('nofx')}},3500)</script>
<style>
{font_css}
:root{{{css_vars}}}
{BASE_CSS}
{c.get('css', '')}
{W.get('css', '')}
</style>
</head>
<body class="v-{var}">
{strip}{header}
<main>
{hero}{body}
</main>
{footer}{dialogs}
<script>window.SHOPCFG={jdump(cfg)};</script>
<script>{JS}</script>
<script>{W.get('js', '')}</script>
</body>
</html>
"""
    save(d, page)
    return d
