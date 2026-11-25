"""Telegram-бот для портфолио: промо-страница продукта, в телефоне — живой чат по сценарию (кнопки, ввод, фото,
карточки, оплата), рядом — экран администратора, куда падают заявки из чата. Тема и сценарий — в конфиге."""
from __future__ import annotations

from .common import e, favicon, fonts, img, jdump, out, save, write_images

CSS = r"""
*,*::before,*::after{box-sizing:border-box}
[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;overflow-x:clip}
body{margin:0;background:var(--bg);color:var(--ink);font:400 16px/1.55 var(--fb);-webkit-font-smoothing:antialiased;overflow-x:clip}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
button,input{font:inherit;color:inherit}
button{cursor:pointer;background:none;border:0;padding:0}
:focus-visible{outline:2px solid var(--ac);outline-offset:3px;border-radius:6px}
.wrap{width:min(1240px,100% - 2*var(--gut));margin-inline:auto}
:root{--gut:clamp(16px,4vw,48px)}
h1,h2,h3{font-family:var(--fh);font-weight:var(--hw);letter-spacing:var(--ht);line-height:1.04;margin:0;overflow-wrap:break-word}
h2{font-size:clamp(30px,4.2vw,54px)}
p{margin:0}
.kick{font:600 12px/1 var(--fb);letter-spacing:.14em;text-transform:uppercase;color:var(--ac)}
.lead{font-size:clamp(17px,1.5vw,20px);color:var(--soft);max-width:54ch}
.sec{padding:clamp(64px,9vw,120px) 0}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;height:54px;padding:0 26px;border-radius:var(--rb);background:var(--ac);color:var(--aci);font-weight:600;transition:transform .2s,box-shadow .2s}
.btn:hover{transform:translateY(-1px);box-shadow:0 12px 30px -12px var(--ac)}
.btn.ghost{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--line2)}
.top{position:sticky;top:0;z-index:30;background:color-mix(in srgb,var(--bg) 82%,transparent);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.top .bar{display:flex;align-items:center;gap:24px;height:68px}
.logo{font-family:var(--fh);font-weight:var(--hw);font-size:22px;display:flex;align-items:center;gap:10px;letter-spacing:var(--ht)}
.logo i{display:grid;place-items:center;width:34px;height:34px;border-radius:10px;background:var(--ac);color:var(--aci);font-style:normal;font-size:18px}
.nav{display:flex;gap:24px;font-size:15px;color:var(--soft);margin-left:auto}
.nav a:hover{color:var(--ink)}
.top .btn{height:42px;padding:0 18px;font-size:15px}
.hero{padding:clamp(28px,5vw,64px) 0 clamp(48px,6vw,90px)}
.hero .g{display:grid;grid-template-columns:1.05fr .95fr;gap:clamp(24px,4vw,64px);align-items:center}
.hero .g>*{min-width:0}
.hero h1{font-size:clamp(42px,6.2vw,88px);margin:18px 0 20px}
.hero h1 em{font-style:normal;color:var(--ac)}
.hero .cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}
.stats{display:flex;gap:clamp(18px,4vw,44px);margin-top:36px;flex-wrap:wrap}
.stats b{display:block;font-family:var(--fh);font-weight:var(--hw);font-size:clamp(26px,3vw,36px);letter-spacing:-.02em;line-height:1}
.stats span{font-size:13px;color:var(--mut)}
.note{font-size:13px;color:var(--mut);margin-top:16px;display:flex;gap:8px;align-items:center}
.note b{display:inline-block;width:8px;height:8px;border-radius:50%;background:#2fbf71;box-shadow:0 0 0 4px rgba(47,191,113,.18)}
/* телефон */
.phone{position:relative;width:min(380px,100%);margin:0 auto;aspect-ratio:9/18.6;border-radius:52px;background:#0d0d0f;padding:12px;box-shadow:0 50px 100px -40px rgba(0,0,0,.45),inset 0 0 0 2px #2a2a2e}
.phone::before{content:"";position:absolute;top:22px;left:50%;transform:translateX(-50%);width:96px;height:26px;border-radius:14px;background:#0d0d0f;z-index:5}
.scr{position:relative;height:100%;border-radius:42px;overflow:hidden;background:var(--tgbg);display:flex;flex-direction:column;font-family:-apple-system,"SF Pro Text","Segoe UI",Roboto,var(--fb),sans-serif}
.tgh{display:flex;align-items:center;gap:10px;padding:54px 14px 10px;background:var(--tghead);color:var(--tghi);border-bottom:1px solid rgba(0,0,0,.06)}
.tgh .av{width:38px;height:38px;border-radius:50%;background:var(--ac);color:var(--aci);display:grid;place-items:center;font-weight:700;font-size:16px;flex:none}
.tgh>div:last-child{min-width:0;padding-right:84px}.tgh b{display:block;font-size:15px;line-height:1.2;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tgh small{font-size:12px;opacity:.6}
.tgh .back{font-size:22px;opacity:.7;margin-right:2px}
.chat{flex:1;overflow-y:auto;padding:12px 10px 8px;display:flex;flex-direction:column;gap:6px;scroll-behavior:smooth;background:var(--tgpat)}
.chat::-webkit-scrollbar{display:none}
.m{max-width:84%;padding:8px 11px 7px;border-radius:16px;font-size:14.5px;line-height:1.38;position:relative;animation:min .28s cubic-bezier(.2,.8,.2,1);white-space:pre-line;word-wrap:break-word}
@keyframes min{from{opacity:0;transform:translateY(8px) scale(.98)}}
.m.b{background:var(--tgin);color:var(--tgink);align-self:flex-start;border-bottom-left-radius:5px;box-shadow:0 1px 1px rgba(0,0,0,.06)}
.m.u{background:var(--tgout);color:var(--tgoink);align-self:flex-end;border-bottom-right-radius:5px}
.m .t{display:block;text-align:right;font-size:11px;opacity:.5;margin-top:2px}
.m.ph{padding:4px;overflow:hidden}
.m.ph .pi{border-radius:12px;overflow:hidden;aspect-ratio:4/3;background:#ccc}
.m.ph .pi img{width:100%;height:100%;object-fit:cover}
.m.ph p{padding:6px 7px 2px}
.m.card{padding:0;overflow:hidden;width:84%}
.m.card .pi{aspect-ratio:16/10;background:#ccc}
.m.card .pi img{width:100%;height:100%;object-fit:cover}
.m.card .cb{padding:9px 11px}
.m.card .cb b{display:block;font-size:15px}
.m.card .cb span{font-size:13px;opacity:.7}
.m.rich{width:84%;white-space:normal}
.tk{display:grid;gap:6px;font-size:13.5px}
.tk h4{margin:0 0 4px;font-size:15px;font-weight:700}
.tk .r{display:flex;justify-content:space-between;gap:12px}
.tk .r span:first-child{opacity:.6}
.tk .r span:last-child{text-align:right;font-weight:500}
.tk .sum{margin-top:4px;padding-top:8px;border-top:1px dashed color-mix(in srgb,currentColor 25%,transparent);font-weight:700}
.tk .sum span:first-child{opacity:1}
.tl{list-style:none;margin:0;padding:2px 0;display:grid;gap:11px;font-size:13.5px}
.tl li{display:grid;grid-template-columns:16px 1fr auto;gap:8px;align-items:center}
.tl li::before{content:"";width:10px;height:10px;border-radius:50%;border:2px solid currentColor;opacity:.3;justify-self:center}
.tl li.ok::before{background:var(--tgac,var(--ac));border-color:var(--tgac,var(--ac));opacity:1}
.tl li.now::before{border-color:var(--tgac,var(--ac));opacity:1;box-shadow:0 0 0 4px color-mix(in srgb,var(--tgac,var(--ac)) 28%,transparent)}
.tl li.now b{color:var(--tgac,var(--ac))}
.tl small{opacity:.55;white-space:nowrap}
.qr{display:grid;justify-items:center;gap:8px;padding:4px 0 2px;text-align:center;font-size:13px}
.qr svg{width:136px;height:136px;background:#fff;border-radius:12px;padding:9px}
.qr b{font-size:15px}
.sch{display:grid;gap:6px;font-size:13.5px}
.sch div{display:grid;grid-template-columns:44px 1fr auto;gap:8px;align-items:baseline}
.sch div span:first-child{font-weight:700}
.sch small{opacity:.55;white-space:nowrap}
.m.inv{padding:0;overflow:hidden;width:84%}
.m.inv .ih{padding:10px 12px;border-bottom:1px solid rgba(0,0,0,.08)}
.m.inv .ih b{display:block}
.m.inv .ir{display:flex;justify-content:space-between;padding:4px 12px;font-size:13.5px}
.m.inv .it{display:flex;justify-content:space-between;padding:8px 12px 10px;font-weight:700}
.kb{display:grid;gap:5px;margin:2px 0 4px;align-self:stretch;animation:min .3s .1s both}
.kb .r{display:grid;grid-auto-flow:column;grid-auto-columns:1fr;gap:5px}
.kb button{min-height:38px;padding:6px 8px;border-radius:10px;background:var(--tgbtn);color:var(--tgbtnink);font-size:13.5px;font-weight:500;line-height:1.2;backdrop-filter:blur(6px);transition:filter .15s,transform .15s}
.kb button:hover{filter:brightness(.97)}
.kb button:active{transform:scale(.98)}
.kb button.pay{background:var(--ac);color:var(--aci);font-weight:600}
.typing{align-self:flex-start;background:var(--tgin);border-radius:16px;padding:10px 14px;display:flex;gap:4px}
.typing i{width:7px;height:7px;border-radius:50%;background:var(--tgink);opacity:.35;animation:dot 1.1s infinite}
.typing i:nth-child(2){animation-delay:.15s}.typing i:nth-child(3){animation-delay:.3s}
@keyframes dot{40%{opacity:.85;transform:translateY(-2px)}}
.inp{display:flex;gap:8px;padding:8px 10px 26px;background:var(--tghead);align-items:center}
.inp input{flex:1;height:38px;border-radius:19px;border:0;padding:0 14px;background:var(--tgfield);color:var(--tgink);font-size:14.5px;min-width:0}
.inp input:focus{outline:0;box-shadow:0 0 0 1.5px var(--ac)}
.inp button{width:38px;height:38px;border-radius:50%;background:var(--ac);color:var(--aci);display:grid;place-items:center;flex:none}
.inp button svg{width:18px;height:18px;fill:currentColor}
.inp input:disabled{opacity:.6}
.restart{position:absolute;right:16px;top:60px;z-index:6;font-size:12px;font-weight:600;padding:6px 10px;border-radius:999px;background:color-mix(in srgb,var(--tghi) 9%,transparent);color:var(--tghi);box-shadow:inset 0 0 0 1px color-mix(in srgb,var(--tghi) 14%,transparent)}
.stage{position:relative;display:grid;place-items:center;padding:10px 0}
.stage::before{content:"";position:absolute;inset:6% 4%;border-radius:50%;background:radial-gradient(closest-side,var(--glow,color-mix(in srgb,var(--ac) 34%,transparent)),transparent 72%);filter:blur(30px);z-index:0}
.stage .phone{z-index:1}
.chip{position:absolute;z-index:2;display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:16px;background:var(--chipbg,var(--card));color:var(--ink);box-shadow:0 18px 40px -22px rgba(0,0,0,.5),0 0 0 1px var(--line);font-size:13px;line-height:1.25;max-width:210px;animation:floaty 6s ease-in-out infinite}
.chip i{font-style:normal;font-size:20px}
.chip b{display:block;font-size:13.5px}
.chip span{color:var(--mut)}
.chip.c1{right:calc(50% + 166px);top:15%;width:max-content}.chip.c2{right:-6%;bottom:18%;animation-delay:-3s}
@keyframes floaty{50%{transform:translateY(-8px)}}
.flow{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin-top:clamp(24px,3vw,40px);counter-reset:f}
.flow div{position:relative;padding:18px 16px 16px;border-radius:var(--rc);background:var(--card);counter-increment:f;font-size:15px;line-height:1.3;min-width:0}
.flow div::before{content:counter(f,decimal-leading-zero);display:block;font:600 12px/1 var(--fb);letter-spacing:.12em;color:var(--ac);margin-bottom:10px}
.flow b{display:block;font-family:var(--fh);font-weight:var(--hw);font-size:17px;letter-spacing:var(--ht);margin-bottom:4px}
.flow span{color:var(--soft);font-size:14px}
/* фичи */
.feats{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:clamp(28px,4vw,48px)}
.feat{padding:clamp(20px,2.4vw,30px);border-radius:var(--rc);background:var(--card);display:flex;flex-direction:column;gap:12px}
.feat i{width:46px;height:46px;border-radius:14px;background:var(--bg);display:grid;place-items:center;font-style:normal;font-size:22px}
.feat b{font-family:var(--fh);font-weight:var(--hw);font-size:21px;letter-spacing:var(--ht);line-height:1.15}
.feat p{color:var(--soft);font-size:15px}
/* админка */
.adm{display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(24px,4vw,56px);align-items:center}
.adm>*{min-width:0}
.panel{border-radius:22px;background:var(--pbg,#fff);color:var(--pink,#1a1c22);box-shadow:0 40px 80px -50px rgba(0,0,0,.45),0 0 0 1px var(--line);overflow:hidden;font-size:14px}
.panel .ph{display:flex;align-items:center;gap:10px;padding:14px 18px;border-bottom:1px solid rgba(0,0,0,.07)}
.panel .ph i{width:10px;height:10px;border-radius:50%;background:#ff5f57;box-shadow:16px 0 0 #febc2e,32px 0 0 #28c840;margin-right:40px}
.panel .ph b{font-size:14px}
.panel .ph span{margin-left:auto;font-size:12px;color:#7a7f8a}
.kpi{display:grid;grid-template-columns:repeat(3,1fr);gap:1px;background:rgba(0,0,0,.06)}
.kpi div{background:var(--pbg,#fff);padding:14px 18px}
.kpi b{display:block;font-size:22px;letter-spacing:-.02em}
.kpi span{font-size:12px;color:#7a7f8a}
.rows{max-height:330px;overflow:auto}
.rowx{display:grid;grid-template-columns:auto 1fr auto;gap:12px;align-items:center;padding:12px 18px;border-top:1px solid rgba(0,0,0,.06)}
.rowx .d{width:36px;height:36px;border-radius:10px;background:#f1f2f5;display:grid;place-items:center;font-size:16px}
.rowx b{display:block;font-size:14px}
.rowx span{font-size:12.5px;color:#7a7f8a}
.rowx em{font-style:normal;font-size:12px;font-weight:600;padding:5px 9px;border-radius:999px;background:#eef6ff;color:#2b6cff;white-space:nowrap}
.rowx.new{animation:flash 1.6s}
@keyframes flash{0%{background:color-mix(in srgb,var(--ac) 22%,transparent)}100%{background:transparent}}
.steps{counter-reset:s;display:grid;gap:18px;margin-top:26px}
.steps li{list-style:none;display:grid;grid-template-columns:40px 1fr;gap:14px;counter-increment:s}
.steps li::before{content:counter(s);width:40px;height:40px;border-radius:50%;background:var(--card);display:grid;place-items:center;font-weight:700;color:var(--ac)}
.steps b{display:block;font-size:17px}
.steps p{color:var(--soft);font-size:15px}
.ol{padding:0;margin:0}
.ints{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}
.ints span{padding:10px 16px;border-radius:999px;background:var(--card);font-size:14px;font-weight:500}
.res{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border-radius:var(--rc);overflow:hidden;margin-top:clamp(28px,4vw,44px)}
.res div{background:var(--bg);padding:clamp(20px,2.4vw,30px)}
.res b{display:block;font-family:var(--fh);font-weight:var(--hw);font-size:clamp(32px,4vw,52px);letter-spacing:-.03em;line-height:1;color:var(--ac)}
.res span{display:block;margin-top:10px;color:var(--soft);font-size:15px}
.faq details{border-top:1px solid var(--line);padding:4px 0}
.faq details:last-child{border-bottom:1px solid var(--line)}
.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;gap:20px;padding:18px 0;font-size:clamp(17px,1.6vw,19px);font-weight:500}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-size:24px;line-height:1;color:var(--mut);transition:transform .3s}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq details p{padding:0 0 20px;color:var(--soft);max-width:70ch}
.cta-b{border-radius:var(--rs);background:var(--ink);color:var(--bg);padding:clamp(28px,5vw,64px);display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.cta-b h2{max-width:18ch}
.foot{padding:28px 0 36px;font-size:13px;color:var(--mut);display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.reveal{opacity:0;transform:translateY(22px);transition:opacity .8s cubic-bezier(.2,.7,.2,1),transform .8s cubic-bezier(.2,.7,.2,1)}
.reveal.on{opacity:1;transform:none}
.nofx .reveal{opacity:1;transform:none}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}.reveal{opacity:1;transform:none}}
@media (max-width:1100px){.chip{display:none}}
@media (max-width:960px){.hero .g,.adm{grid-template-columns:1fr}.feats{grid-template-columns:1fr 1fr}.res{grid-template-columns:1fr 1fr}.nav{display:none}}
@media (max-width:560px){.feats{grid-template-columns:1fr}.hero .cta{flex-direction:column}.hero .cta .btn{width:100%;justify-content:center;text-align:center}.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.stats span{font-size:12px;line-height:1.3;display:block;margin-top:4px}.kpi b{font-size:18px}}

/* ===== шапка: варианты ===== */
.top.tc .bar{display:grid;grid-template-columns:1fr auto 1fr}
.top.tc .nav{margin-left:0;justify-self:start}.top.tc .bar>.btn{justify-self:end}
.top.tf{background:transparent;border:0;backdrop-filter:none;-webkit-backdrop-filter:none;top:12px;padding-top:12px}
.top.tf .bar{height:58px;padding:0 8px 0 18px;border-radius:999px;background:color-mix(in srgb,var(--card) 90%,transparent);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);box-shadow:0 14px 40px -24px rgba(0,0,0,.45),0 0 0 1px var(--line)}
.top.tf .bar>.btn{border-radius:999px}
.top.tp{position:relative;background:transparent;border:0;backdrop-filter:none;-webkit-backdrop-filter:none}
.top.tp .nav{display:none}.top.tp .bar{height:84px}
.tlink{margin-left:auto;font-weight:600;font-size:15px;border-bottom:2px solid var(--ac);padding-bottom:2px}
/* ===== телефон: варианты рамки ===== */
.fr-silver .phone{background:linear-gradient(150deg,#f7f7f9,#c9cbd1 60%,#e9eaee);box-shadow:0 50px 100px -40px rgba(0,0,0,.35),inset 0 0 0 1px #aeb0b6,inset 0 0 0 4px #e4e5e9}
.fr-flat .phone{background:transparent;padding:0;border-radius:34px;box-shadow:0 40px 90px -40px rgba(0,0,0,.4),0 0 0 1px var(--line2)}
.fr-flat .phone::before{display:none}.fr-flat .scr{border-radius:34px}.fr-flat .tgh{padding-top:16px}.fr-flat .restart{top:20px}
.fr-edge .phone{background:var(--ac);box-shadow:0 50px 100px -40px rgba(0,0,0,.5),inset 0 0 0 2px color-mix(in srgb,#000 18%,var(--ac))}
.fr-edge .phone::before{background:#0d0d0f}
/* ===== герой: варианты ===== */
.hero.h-mirror .g{grid-template-columns:.95fr 1.05fr}
.hero.h-mirror .stage{order:-1}
.hero.h-mirror .stats{flex-direction:column;gap:0;border-top:1px solid var(--line2);max-width:440px}
.hero.h-mirror .stats div{display:grid;grid-template-columns:6.5ch 1fr;align-items:baseline;gap:16px;padding:13px 0;border-bottom:1px solid var(--line2)}
.hero.h-mirror .stats span{font-size:15px;color:var(--soft)}
.hero.h-mirror .chip.c1{right:auto;left:calc(50% + 150px);top:12%}.hero.h-mirror .chip.c2{right:auto;left:-4%;bottom:14%}
.hero.h-center{text-align:center}
.h-center .hc-t{max-width:980px;margin:0 auto}.h-center .lead{margin-inline:auto}.h-center .cta{justify-content:center}
.h-center .tri{display:grid;grid-template-columns:1fr minmax(300px,370px) 1fr;gap:clamp(20px,3.4vw,56px);align-items:center;margin-top:clamp(36px,5vw,72px);text-align:left}
.h-center .tri>*{min-width:0}
.tri-l{list-style:none;margin:0;padding:0;display:grid;gap:0;counter-reset:t}
.tri-l li{counter-increment:t;display:grid;grid-template-columns:44px 1fr;gap:14px;padding:16px 0;border-top:1px solid var(--line2)}
.tri-l li:last-child{border-bottom:1px solid var(--line2)}
.tri-l li::before{content:counter(t);width:36px;height:36px;border-radius:50%;display:grid;place-items:center;background:var(--ac);color:var(--aci);font-weight:700;font-size:15px}
.tri-l b{display:block;font-family:var(--fh);font-weight:var(--hw);font-size:18px;letter-spacing:var(--ht);line-height:1.2}
.tri-l span{font-size:14px;color:var(--soft)}
.tri-r{display:grid;gap:12px}
.tri-r .tc{padding:18px 20px;border-radius:var(--rc);background:var(--card);box-shadow:0 0 0 1px var(--line)}
.tri-r .tc b{display:block;font-family:var(--fh);font-weight:var(--hw);font-size:clamp(28px,3vw,40px);letter-spacing:-.02em;line-height:1;color:var(--ac)}
.tri-r .tc span{font-size:14px;color:var(--soft)}
.tri-r .tc.ch{display:flex;gap:12px;align-items:center;background:var(--ink);color:var(--bg);box-shadow:none}
.tri-r .tc.ch i{font-style:normal;font-size:22px}.tri-r .tc.ch b{font-size:15px;color:inherit;font-family:var(--fb);letter-spacing:0;line-height:1.3}
.tri-r .tc.ch span{color:color-mix(in srgb,var(--bg) 70%,transparent);font-size:13px}
.h-center .note{justify-content:center}
.hero.h-poster{padding:0 0 clamp(48px,6vw,90px)}
.h-poster .band{background:var(--band,var(--ink));color:var(--bandink,var(--bg));padding:clamp(40px,6vw,84px) 0 clamp(150px,16vw,250px)}
.hero.h-poster h1{font-size:clamp(44px,7.2vw,116px);line-height:.92;margin:22px 0 0;max-width:16ch}.hero.h-poster h1 em{color:var(--bandem,var(--bandink,var(--bg)))}
.h-poster .band .kick{color:var(--bandink,var(--bg));opacity:.8}
.h-poster .pg{display:grid;grid-template-columns:1fr minmax(300px,390px);gap:clamp(24px,5vw,80px);align-items:start}
.h-poster .pg>*{min-width:0}
.h-poster .pg>.reveal{padding-top:clamp(28px,3vw,44px)}
.h-poster .stage{margin-top:calc(-1 * clamp(130px,14vw,230px))}
.h-poster .stage::before{display:none}
.hero.h-duo .dt{display:grid;grid-template-columns:1.25fr .75fr;gap:clamp(24px,4vw,64px);align-items:end}
.hero.h-duo .dt>*{min-width:0}
.hero.h-duo h1{margin-bottom:0}
.h-duo .dt .cta{margin-top:22px}
.dstage{margin-top:clamp(28px,4vw,52px);border-radius:var(--rs);background:var(--dsbg,var(--card));padding:clamp(18px,3.6vw,52px);display:grid;grid-template-columns:minmax(280px,350px) 1fr;gap:clamp(20px,4vw,60px);align-items:center;box-shadow:0 0 0 1px var(--line)}
.dstage>*{min-width:0}
.dstage .stage::before{display:none}
.dside{display:grid;gap:22px}
.dside .stats{margin-top:0}
.dside .cap{font-size:14px;color:var(--soft);display:flex;gap:10px;align-items:center}
.dside .cap::before{content:"";width:26px;height:2px;background:var(--ac)}
.adm.solo{grid-template-columns:1fr}
.adm.solo .steps{grid-template-columns:repeat(3,1fr);gap:24px}
.adm.solo .steps li{grid-template-columns:1fr;gap:12px}
.hero.h-tilt .stage{perspective:1700px}
.hero.h-tilt .stage::before{inset:4% -2%;background:var(--disk,color-mix(in srgb,var(--ac) 20%,var(--bg)));filter:none;border-radius:50%}
.hero.h-tilt .phone{transform:rotateY(-15deg) rotateX(5deg) rotateZ(1.5deg);box-shadow:36px 60px 110px -40px rgba(0,0,0,.5),inset 0 0 0 2px #2a2a2e}
.hero.h-tilt .chip.c1{right:auto;left:-12%;top:6%}
.hero.h-tilt .stats{display:grid;grid-template-columns:1fr 1fr;gap:10px;max-width:460px}
.hero.h-tilt .stats div{background:var(--card);border-radius:var(--rc);padding:16px 18px;box-shadow:0 0 0 1px var(--line)}
.hero.h-tilt .stats div:first-child{grid-column:1/-1;background:var(--ac);color:var(--aci);box-shadow:none}
.hero.h-tilt .stats div:first-child span{color:inherit;opacity:.8}
.hero.h-photo{position:relative;color:#fff;padding:clamp(36px,6vw,90px) 0;overflow:hidden;background:#111}
.hero.h-photo .hbg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.hero.h-photo::before{content:"";position:absolute;inset:0;z-index:1;background:var(--veil,linear-gradient(90deg,rgba(0,0,0,.78) 0%,rgba(0,0,0,.5) 45%,rgba(0,0,0,.15) 100%))}
.hero.h-photo .wrap{position:relative;z-index:2}
.hero.h-photo .kick{color:#fff;opacity:.9}.hero.h-photo .lead{color:rgba(255,255,255,.84)}
.hero.h-photo .stats span,.hero.h-photo .note{color:rgba(255,255,255,.72)}
.hero.h-photo .btn.ghost{color:#fff;box-shadow:inset 0 0 0 1.5px rgba(255,255,255,.55)}
.hero.h-photo .stage::before{display:none}
.hero.h-look .lk{display:grid;grid-template-columns:minmax(0,1fr) minmax(300px,360px);grid-template-areas:"t ph" "g ph";gap:clamp(22px,3vw,40px) clamp(24px,4vw,64px);align-items:end}
.h-look .lk>*{min-width:0}
.h-look .lk-t{grid-area:t;display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:clamp(20px,3vw,48px);align-items:end}
.h-look .lk-t h1{margin-bottom:0}.h-look .lk-t .cta{margin-top:22px}
.h-look .lk-g{grid-area:g;display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:12px;align-items:start}
.h-look .lk-g figure{margin:0;border-radius:var(--rc);overflow:hidden;aspect-ratio:3/4;background:var(--card)}
.h-look .lk-g figure:nth-child(2){margin-top:44px}.h-look .lk-g figure:nth-child(3){margin-top:16px}
.h-look .lk-g img{width:100%;height:100%;object-fit:cover}
.h-look .lk-g figcaption{display:none}
.h-look .stage{grid-area:ph}.h-look .stage::before{display:none}
.sk{display:grid;grid-template-columns:minmax(300px,360px) 1fr;grid-template-areas:"ph hd" "ph bd";column-gap:clamp(36px,6vw,96px)}
.sk>*{min-width:0}
.sk-hd{grid-area:hd;padding:clamp(28px,5vw,72px) 0 clamp(24px,3vw,40px)}
.sk-hd h1{font-size:clamp(40px,5.4vw,80px);margin:18px 0 20px}.sk-hd h1 em{font-style:normal;color:var(--ac)}
.sk-hd .cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
.sk-ph{grid-area:ph;position:sticky;top:84px;align-self:start;padding:clamp(24px,3vw,40px) 0 40px}
.sk-ph .phone{width:min(340px,100%)}
.sk-ph .stage::before{inset:10% -10%}
.sk-bd{grid-area:bd}
.sk-bd .sec{padding:clamp(40px,6vw,80px) 0;border-top:1px solid var(--line)}
.sk-bd .feats{grid-template-columns:1fr 1fr}.sk-bd .adm{grid-template-columns:1fr}.sk-bd .res{grid-template-columns:1fr 1fr}
.sk-bd .flow{grid-template-columns:repeat(auto-fit,minmax(170px,1fr))}
/* ===== возможности: варианты ===== */
.feats.f-list{grid-template-columns:1fr;gap:0;counter-reset:fl}
.feats.f-list .feat{display:grid;grid-template-columns:72px minmax(0,.9fr) minmax(0,1.1fr);gap:20px;align-items:baseline;background:none;border-radius:0;padding:24px 0;border-top:1px solid var(--line2);counter-increment:fl}
.feats.f-list .feat:last-child{border-bottom:1px solid var(--line2)}
.feats.f-list .feat i{display:none}
.feats.f-list .feat::before{content:counter(fl,decimal-leading-zero);font-family:var(--fh);font-weight:var(--hw);font-size:22px;color:var(--ac)}
.feats.f-list .feat b{font-size:clamp(20px,2vw,26px)}
.feats.f-rail{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:14px;padding-bottom:12px;scrollbar-width:thin}
.feats.f-rail .feat{flex:0 0 min(310px,82%);scroll-snap-align:start;min-height:250px;justify-content:space-between}
.feats.f-rail .feat:first-child{background:var(--ac);color:var(--aci)}.feats.f-rail .feat:first-child p{color:inherit;opacity:.85}
.feats.f-rail .feat:first-child i{background:color-mix(in srgb,var(--aci) 18%,transparent)}
.feats.f-bento{grid-template-columns:repeat(3,1fr);grid-auto-flow:dense}
.feats.f-bento .feat:nth-child(1),.feats.f-bento .feat:nth-child(4),.feats.f-bento .feat:nth-child(6){grid-column:span 2}
.feats.f-bento .feat:nth-child(1){background:var(--ink);color:var(--bg)}.feats.f-bento .feat:nth-child(1) p{color:inherit;opacity:.75}
.feats.f-bento .feat:nth-child(1) i{background:color-mix(in srgb,var(--bg) 14%,transparent)}
.feats.f-bento .feat:nth-child(4){background:var(--ac);color:var(--aci)}.feats.f-bento .feat:nth-child(4) p{color:inherit;opacity:.85}
.feats.f-bento .feat:nth-child(4) i{background:color-mix(in srgb,var(--aci) 18%,transparent)}
.feats.f-icons{grid-template-columns:1fr 1fr;gap:clamp(24px,3vw,40px) clamp(28px,5vw,72px)}
.feats.f-icons .feat{background:none;padding:0;display:grid;grid-template-columns:56px 1fr;gap:6px 18px;border-radius:0}
.feats.f-icons .feat i{grid-row:span 2;width:56px;height:56px;border-radius:50%;background:var(--ac);color:var(--aci);font-size:24px}
/* ===== результат: варианты ===== */
.res.r-band{background:var(--ac);gap:0;border-radius:var(--rs)}
.res.r-band div{background:transparent;color:var(--aci)}.res.r-band div+div{box-shadow:inset 1px 0 0 color-mix(in srgb,var(--aci) 22%,transparent)}
.res.r-band b{color:var(--aci)}.res.r-band span{color:color-mix(in srgb,var(--aci) 82%,transparent)}
.res.r-line{background:none;gap:0;border-radius:0;border-top:2px solid var(--ink)}
.res.r-line div{background:none;padding:26px 26px 0 0}.res.r-line b{color:var(--ink);font-size:clamp(40px,5vw,72px)}
@media (max-width:960px){
 .hero.h-look .lk{grid-template-columns:1fr;grid-template-areas:"t" "g" "ph"}.h-look .lk-t{grid-template-columns:1fr}
 .h-center .tri,.h-poster .pg,.hero.h-duo .dt,.dstage{grid-template-columns:1fr}
 .h-center .tri .stage{order:-1}
 .hero.h-mirror .g{grid-template-columns:1fr}.hero.h-mirror .stage{order:0}
 .h-poster .band{padding-bottom:clamp(40px,8vw,80px)}.h-poster .stage{margin-top:28px}
 .adm.solo .steps{grid-template-columns:1fr}
 .sk{grid-template-columns:1fr;grid-template-areas:"hd" "ph" "bd"}.sk-ph{position:static;padding-top:0}
 .feats.f-bento{grid-template-columns:1fr 1fr}.feats.f-bento .feat:nth-child(n){grid-column:auto}.feats.f-bento .feat:nth-child(1){grid-column:1/-1}
 .feats.f-list .feat{grid-template-columns:52px 1fr}.feats.f-list .feat p{grid-column:2}
 .top.tc .bar{display:flex}.top.tc .logo{margin-right:auto}
 .hero.h-tilt .phone{transform:rotateY(-7deg) rotateX(3deg)}
 .res.r-band div+div{box-shadow:none}
}
@media (max-width:560px){
 .feats.f-icons,.sk-bd .feats,.feats.f-bento{grid-template-columns:1fr}
 .sk-bd .res{grid-template-columns:1fr 1fr}
 .hero.h-mirror .stats{display:flex}
 .hero.h-tilt .stats{display:grid;grid-template-columns:1fr 1fr}
 .top.tf .bar{padding:0 6px 0 14px}
 .hero.h-poster h1{font-size:clamp(40px,12vw,64px)}
}
"""

JS = r"""
(function(){
var C=window.BOTCFG,N=C.nodes,chat=document.getElementById('chat'),inp=document.getElementById('inp'),send=document.getElementById('send');
var esc=function(s){return String(s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
var V={},waiting=null,busy=false,auto=true;
var F={money:function(n){return String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g,'\u00a0')+' ₽'},
 day:function(add){var d=new Date();d.setDate(d.getDate()+add);return['вс','пн','вт','ср','чт','пт','сб'][d.getDay()]+', '+d.getDate()+' '+['янв','фев','мар','апр','мая','июн','июл','авг','сен','окт','ноя','дек'][d.getMonth()]}};
function tm(){var d=new Date();return d.getHours()+':'+String(d.getMinutes()).padStart(2,'0')}
function fill(s){return String(s).replace(/\{(\w+)\}/g,function(_,k){return V[k]!=null?V[k]:''})}
function im(name){var I=C.img[name];if(!I)return'';var ws=I[3].split(',');return'<img src="img/'+name+'-'+ws[0]+'.webp" alt="" loading="lazy">'}
function scroll(){chat.scrollTop=chat.scrollHeight}
function add(html,cls){var d=document.createElement('div');d.className='m '+cls;d.innerHTML=html;chat.appendChild(d);scroll();return d}
function bot(msg){if(typeof msg==='string')msg={t:msg};
 if(msg.photo)return add('<div class="pi">'+im(msg.photo)+'</div>'+(msg.t?'<p>'+esc(fill(msg.t))+'</p>':'')+'<span class="t">'+tm()+'</span>','b ph');
 if(msg.card)return add('<div class="pi">'+im(msg.card.img)+'</div><div class="cb"><b>'+esc(fill(msg.card.t))+'</b><span>'+esc(fill(msg.card.s||''))+'</span></div>','b card');
 if(msg.inv)return add('<div class="ih"><b>'+esc(fill(msg.inv.t))+'</b><span style="font-size:12px;opacity:.6">'+esc(C.brand)+'</span></div>'+msg.inv.rows.map(function(r){return'<div class="ir"><span>'+esc(fill(r[0]))+'</span><span>'+esc(fill(r[1]))+'</span></div>'}).join('')+'<div class="it"><span>Итого</span><span>'+esc(fill(msg.inv.total))+'</span></div>','b inv');
 if(msg.html)return add(fill(msg.html)+'<span class="t">'+tm()+'</span>','b rich');
 return add(esc(fill(msg.t)).replace(/\*([^*]+)\*/g,'<b>$1</b>')+'<span class="t">'+tm()+'</span>','b')}
function user(t){add(esc(t)+'<span class="t">'+tm()+' ✓✓</span>','u')}
function typing(){var d=document.createElement('div');d.className='typing';d.innerHTML='<i></i><i></i><i></i>';chat.appendChild(d);scroll();return d}
function wait(ms){return new Promise(function(r){setTimeout(r,ms)})}
var first=true;
async function go(id){var n=N[id];if(!n)return;busy=true;
 if(n.set)for(var k in n.set)V[k]=n.set[k];
 if(n.calc)V=Object.assign(V,(new Function('V','F',n.calc))(V,F)||{});
 for(var i=0;i<(n.say||[]).length;i++){if(first&&id==='start'){bot(n.say[i]);continue}var t=typing();await wait(Math.min(1400,420+String(n.say[i].t||n.say[i]||'').length*9));t.remove();bot(n.say[i]);await wait(160)}
 if(id==='start'&&first){first=false;await wait(900)}
 if(n.admin)admin(n.admin);
 busy=false;
 if(n.kb)keyboard(n.kb);
 if(n.ask){waiting=n.ask;inp.disabled=false;inp.placeholder=n.ask.ph||'Сообщение';inp.type=n.ask.type==='tel'?'tel':'text';if(!auto)inp.focus()}
 if(n.next)setTimeout(function(){go(n.next)},500);
 if(auto&&n.kb&&C.autoplay&&C.autoplay[id]!=null)setTimeout(function(){var b=chat.querySelector('.kb:last-of-type button[data-i="'+C.autoplay[id]+'"]');if(b&&auto)b.click()},1500);
 if(auto&&n.ask&&C.autofill&&C.autofill[id])setTimeout(function(){if(!auto||waiting!==n.ask)return;inp.value=C.autofill[id];submit(true)},1700)}
function keyboard(rows){var k=document.createElement('div');k.className='kb';var idx=0;
 k.innerHTML=rows.map(function(r){return'<div class="r">'+r.map(function(b){return'<button type="button" class="'+(b[2]==='pay'?'pay':'')+'" data-i="'+(idx++)+'" data-n="'+b[1]+'" data-v="'+esc(fill(b[3]||b[0]))+'">'+esc(fill(b[0]))+'</button>'}).join('')+'</div>'}).join('');
 chat.appendChild(k);scroll();
 k.addEventListener('click',function(ev){var b=ev.target.closest('button');if(!b||busy)return;if(ev.isTrusted)auto=false;var kv=rows.flat()[+b.dataset.i];if(kv[4])V[kv[4]]=b.dataset.v;k.remove();user(b.textContent);setTimeout(function(){go(b.dataset.n)},350)})}
function submit(isAuto){var v=inp.value.trim();if(!waiting||!v)return;var a=waiting;
 if(a.type==='tel'&&v.replace(/\D/g,'').length<10){inp.value='';bot('Похоже, в номере не хватает цифр. Пример: +7 900 123-45-67');return}
 if(!isAuto)auto=false;V[a.key]=v;waiting=null;inp.value='';inp.disabled=true;inp.placeholder='Выберите кнопку выше';user(v);setTimeout(function(){go(a.next)},350)}
send.addEventListener('click',function(){submit(false)});
inp.addEventListener('keydown',function(e){if(e.key==='Enter')submit(false)});
document.getElementById('restart').addEventListener('click',function(){chat.innerHTML='';V={};waiting=null;auto=false;inp.disabled=true;go('start')});
/* админка */
var rows=document.getElementById('rows'),cnt=0;
function admin(a){var r=document.createElement('div');r.className='rowx new';r.innerHTML='<div class="d">'+a.i+'</div><div><b>'+esc(fill(a.t))+'</b><span>'+esc(fill(a.s))+' · только что</span></div><em>'+esc(fill(a.st||'Новая'))+'</em>';rows.prepend(r);
 cnt++;var k=document.getElementById('kpi0');if(k)k.textContent=+k.dataset.base+cnt;var s=document.getElementById('kpiSum'),sm=a.sum||+V[a.sumKey]||0;if(s&&sm){s.dataset.v=(+s.dataset.v||+s.dataset.base)+sm;s.textContent=(+s.dataset.v).toString().replace(/\B(?=(\d{3})+(?!\d))/g,' ')+' ₽'}}
/* запуск, когда телефон виден */
var started=false,io='IntersectionObserver'in window?new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('on');if(x.target.id==='phoneBox'&&!started){started=true;go('start')}io.unobserve(x.target)}})},{threshold:.2}):null;
document.querySelectorAll('.reveal,#phoneBox').forEach(function(el){io?io.observe(el):el.classList.add('on')});
if(!io){started=true;go('start')}
setTimeout(function(){if(!started){started=true;go('start')}},2500);
window.__bot=1;
})();
"""


def build(c: dict) -> str:
    d = out(c["slug"])
    I = c.get("images", {})
    write_images(d, I)
    th = {**c["theme"], **c.get("vars", {})}
    font_css = fonts(d, c["fonts"])
    css_vars = ";".join(f"--{k}:{v}" for k, v in th.items())
    nav = "".join(f'<a href="#{h}">{e(t)}</a>' for t, h in [("Как работает", "demo"), ("Возможности", "feats"), ("Админка", "admin"), ("Вопросы", "faq")])
    H = c["hero"]
    stats = "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in H["stats"])
    feats = "".join(f'<div class="feat reveal" style="transition-delay:{(i % 3) * 70}ms"><i>{a}</i><b>{e(b)}</b><p>{e(t)}</p></div>'
                    for i, (a, b, t) in enumerate(c["feats"]))
    A = c["admin"]
    kpi = (f'<div><b id="kpi0" data-base="{A["kpi"][0][0]}">{A["kpi"][0][0]}</b><span>{e(A["kpi"][0][1])}</span></div>'
           f'<div><b id="kpiSum" data-base="{A["kpi"][1][0]}">{A["kpi"][1][2]}</b><span>{e(A["kpi"][1][1])}</span></div>'
           f'<div><b>{e(A["kpi"][2][0])}</b><span>{e(A["kpi"][2][1])}</span></div>')
    rows = "".join(f'<div class="rowx"><div class="d">{r[0]}</div><div><b>{e(r[1])}</b><span>{e(r[2])}</span></div><em>{e(r[3])}</em></div>' for r in A["rows"])
    steps = "".join(f"<li><div><b>{e(a)}</b><p>{e(b)}</p></div></li>" for a, b in A["steps"])
    ints = "".join(f"<span>{e(x)}</span>" for x in c["ints"])
    res = "".join(f'<div class="reveal"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in c["results"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in c["faq"])
    chips = "".join(f'<div class="chip c{i + 1}"><i>{a}</i><div><b>{e(b)}</b><span>{e(t)}</span></div></div>'
                    for i, (a, b, t) in enumerate(H.get("chips", [])[:2]))
    L = c.get("layout", "split")
    hdr = c.get("header", "bar")
    W = "" if L == "sticky" else "wrap"
    flow = ""
    if c.get("flow") and L != "center":
        flow = (f'<section class="sec" style="padding-top:0"><div class="{W}"><div class="reveal"><div class="kick">Сценарий</div>'
                f'<h2 style="margin-top:14px">{c.get("flowTitle", "Путь клиента в боте")}</h2></div><div class="flow reveal">'
                + "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in c["flow"]) + "</div></div></section>")
    kick = f'<div class="kick">{e(H["kicker"])}</div>'
    h1 = f"<h1>{H['h1']}</h1>"
    lead = f'<p class="lead">{H["lead"]}</p>'
    cta = (f'<div class="cta"><a class="btn" href="#demo">{e(H["cta"])}</a>'
           f'<a class="btn ghost" href="#admin">{e(H.get("cta2", "Что видит администратор"))}</a></div>')
    statsH = f'<div class="stats">{stats}</div>'
    note = '<p class="note"><b></b>Бот в телефоне работает: нажимайте кнопки или пишите сами</p>'
    phone = (f'<div class="phone" id="phoneBox"><div class="scr">'
             f'<div class="tgh"><span class="back">‹</span><div class="av">{c["avatar"]}</div><div><b>{e(c["botName"])}</b><small>бот</small></div></div>'
             '<button class="restart" id="restart" type="button">↻ Заново</button>'
             '<div class="chat" id="chat" aria-live="polite"></div>'
             '<div class="inp"><input id="inp" placeholder="Выберите кнопку выше" disabled aria-label="Сообщение боту"><button id="send" type="button" aria-label="Отправить"><svg viewBox="0 0 24 24"><path d="M3 20.5 21 12 3 3.5l.02 6.6L15 12 3.02 13.9z"/></svg></button></div>'
             '</div></div>')
    stage = f'<div id="demo" class="stage">{chips}{phone}</div>'
    stage0 = f'<div id="demo" class="stage">{phone}</div>'
    panel = (f'<div class="panel reveal"><div class="ph"><i></i><b>{e(A["name"])}</b><span>онлайн</span></div>'
             f'<div class="kpi">{kpi}</div><div class="rows" id="rows">{rows}</div></div>')
    if L == "duo":
        admin_sec = (f'<section class="sec" id="admin" style="padding-top:0"><div class="{W} adm solo"><div class="reveal"><div class="kick">Для команды</div>'
                     f'<h2 style="margin:14px 0 16px;max-width:22ch">{A["title"]}</h2><p class="lead">{A["lead"]}</p><ol class="steps ol">{steps}</ol></div></div></section>')
    else:
        admin_sec = (f'<section class="sec" id="admin" style="padding-top:0"><div class="{W} adm">'
                     f'<div class="reveal"><div class="kick">Для команды</div><h2 style="margin:14px 0 16px">{A["title"]}</h2><p class="lead">{A["lead"]}</p><ol class="steps ol">{steps}</ol></div>'
                     f'{panel}</div></section>')
    fcls = {"cards": "", "list": " f-list", "rail": " f-rail", "bento": " f-bento", "icons": " f-icons"}[c.get("featsStyle", "cards")]
    rcls = {"grid": "", "band": " r-band", "line": " r-line"}[c.get("resStyle", "grid")]
    feats_sec = (f'<section class="sec" id="feats" style="padding-top:0"><div class="{W}"><div class="reveal"><div class="kick">Возможности</div>'
                 f'<h2 style="margin-top:14px">{c["featsTitle"]}</h2></div><div class="feats{fcls}">{feats}</div></div></section>')
    res_sec = (f'<section class="sec" style="padding-top:0"><div class="{W}"><div class="reveal"><div class="kick">Результат</div><h2 style="margin-top:14px">{c["resTitle"]}</h2></div>'
               f'<div class="res{rcls}">{res}</div><div class="ints reveal">{ints}</div></div></section>')
    faq_sec = (f'<section class="sec" id="faq" style="padding-top:0"><div class="{W}" style="max-width:900px"><div class="reveal"><div class="kick">Вопросы</div>'
               f'<h2 style="margin:14px 0 24px">Частые вопросы</h2></div><div class="faq">{faq}</div></div></section>')
    cta_sec = (f'<section class="sec" style="padding-top:0"><div class="{W}"><div class="cta-b reveal"><h2>{c["ctaTitle"]}</h2>'
               f'<a class="btn" href="#demo">{e(c.get("ctaBtn", "Попробовать бота"))}</a></div></div></section>')
    rest = flow + feats_sec + admin_sec + res_sec + faq_sec + cta_sec
    if L == "center":
        tri_l = "".join(f"<li><div><b>{e(a)}</b><span>{e(b)}</span></div></li>" for a, b in (c.get("flow") or [(f[1], "") for f in c["feats"]])[:5])
        tri_r = ("".join(f'<div class="tc"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in H["stats"][:2])
                 + "".join(f'<div class="tc ch"><i>{a}</i><div><b>{e(b)}</b><span>{e(t)}</span></div></div>' for a, b, t in H.get("chips", [])[:1]))
        hero = (f'<section class="hero h-center" id="top"><div class="wrap"><div class="hc-t reveal">{kick}{h1}{lead}{cta}</div>'
                f'<div class="tri"><ol class="tri-l reveal">{tri_l}</ol>{stage0}<div class="tri-r reveal">{tri_r}</div></div>{note}</div></section>')
        body = hero + rest
    elif L == "poster":
        hero = (f'<section class="hero h-poster" id="top"><div class="band"><div class="wrap">{kick}{h1}</div></div>'
                f'<div class="wrap pg"><div class="reveal">{lead}{cta}{statsH}{note}</div>{stage0}</div></section>')
        body = hero + rest
    elif L == "duo":
        hero = (f'<section class="hero h-duo" id="top"><div class="wrap"><div class="dt reveal"><div>{kick}{h1}</div><div>{lead}{cta}</div></div>'
                f'<div class="dstage">{stage0}<div class="dside"><p class="cap">{e(c.get("duoCap", "Заявка из чата сразу появляется у администратора"))}</p>{panel}{statsH}</div></div></div></section>')
        body = hero + rest
    elif L == "look":
        figs = "".join(f'<figure>{img(n, I, "(max-width:960px) 33vw, 22vw", "", "", eager=True).replace("<img ", f"<img style=\"object-position:{pos}\" ", 1)}</figure>' for n, pos in c["lookbook"][:3])
        hero = (f'<section class="hero h-look" id="top"><div class="wrap lk"><div class="lk-t reveal"><div>{kick}{h1}</div><div>{lead}{cta}</div></div>'
                f'<div class="lk-g reveal">{figs}</div>{stage0}</div></section>')
        body = hero + rest
    elif L == "sticky":
        body = (f'<div class="wrap sk" id="top"><div class="sk-hd reveal">{kick}{h1}{lead}{cta}{statsH}{note}</div>'
                f'<aside class="sk-ph">{stage0}</aside><div class="sk-bd">{rest}</div></div>')
    else:
        bg = ""
        if L == "photo":
            bg = img(c["heroImg"], I, "100vw", "", "hbg", eager=True)
        hero = (f'<section class="hero h-{L}" id="top">{bg}<div class="wrap g">'
                f'<div class="reveal">{kick}{h1}{lead}{cta}{statsH}{note}</div>{stage}</div></section>')
        body = hero + rest
    logo = f'<a class="logo" href="#top"><i>{c["logoIcon"]}</i>{e(c["brand"])}</a>'
    topbtn = f'<a class="btn" href="#demo">{e(c.get("topCta", "Открыть бота"))}</a>'
    navh = f'<nav class="nav">{nav}</nav>'
    header = {"bar": f'<header class="top"><div class="wrap bar">{logo}{navh}{topbtn}</div></header>',
              "center": f'<header class="top tc"><div class="wrap bar">{navh}{logo}{topbtn}</div></header>',
              "float": f'<header class="top tf"><div class="wrap bar">{logo}{navh}{topbtn}</div></header>',
              "plain": f'<header class="top tp"><div class="wrap bar">{logo}<a class="tlink" href="#demo">{e(c.get("topCta", "Открыть бота"))}</a></div></header>'}[hdr]
    cfg = {"brand": c["botName"], "nodes": c["nodes"], "img": {k: list(v) for k, v in I.items()}, "autoplay": c.get("autoplay", {}), "autofill": c.get("autofill", {})}
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
<script>document.documentElement.classList.add('js');setTimeout(function(){{if(!window.__bot)document.documentElement.classList.add('nofx')}},3500)</script>
<style>
{font_css}
:root{{{css_vars}}}
{CSS}
{c.get('css', '')}
</style>
</head>
<body class="fr-{c.get('frame', 'black')}">
{header}
<main>
{body}
</main>
<footer class="wrap foot"><span>© 2026 {e(c['brand'])}</span><a href="https://ysddev.com/" target="_blank" rel="noopener" style="color:inherit">Разработан с душой студией YSD DEV</a></footer>
<script>window.BOTCFG={jdump(cfg)};</script>
<script>{JS}</script>
</body>
</html>
"""
    save(d, page)
    return d
