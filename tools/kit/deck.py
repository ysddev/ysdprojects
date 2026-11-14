"""Презентация по конфигу: слайды 16:9 на весь экран (стрелки, клик, свайп, полный экран, оглавление), на телефоне —
лента слайдов. Цифры считаются при показе, графики дорисовываются, слайд-калькулятор считает по формулам из конфига.
Типы слайдов: cover, text, cards, stats, bars, line, donut, table, steps, split, quote, price, calc, end."""
from __future__ import annotations

import math
import re

from .common import e, favicon, fonts, img, jdump, out, save, write_images

CSS = r"""
*{box-sizing:border-box}html,body{height:100%}
body{margin:0;background:var(--page);color:var(--ink);font-family:var(--fb);-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
button{font:inherit;color:inherit;background:none;border:0;padding:0;cursor:pointer}
h1,h2,h3,p,ul,ol,figure{margin:0}ul,ol{padding:0;list-style:none}img{display:block;max-width:100%}
.deck{position:fixed;inset:0 0 var(--bar) 0;display:grid;place-items:center;overflow:hidden}
.sl{--u:1cqw;position:absolute;width:min(100vw,calc((100vh - var(--bar)) * 16 / 9));aspect-ratio:16/9;container-type:inline-size;
 background:var(--sbg);color:var(--sink);opacity:0;visibility:hidden;transform:translateX(3%);transition:opacity .45s,transform .55s cubic-bezier(.2,.7,.2,1),visibility 0s .5s;overflow:hidden}
.sl.on{opacity:1;visibility:visible;transform:none;transition:opacity .45s,transform .55s cubic-bezier(.2,.7,.2,1);z-index:2}
.sl.was{transform:translateX(-3%)}
.sl .in{position:absolute;inset:0;padding:calc(var(--u)*5) calc(var(--u)*6);display:flex;flex-direction:column;font-size:calc(var(--u)*1.55);line-height:1.45}
.v-light{--sbg:var(--l-bg);--sink:var(--l-ink);--smut:var(--l-mut);--sline:var(--l-line);--scard:var(--l-card)}
.v-dark{--sbg:var(--d-bg);--sink:var(--d-ink);--smut:var(--d-mut);--sline:var(--d-line);--scard:var(--d-card)}
.v-accent{--sbg:var(--a-bg);--sink:var(--a-ink);--smut:var(--a-mut);--sline:var(--a-line);--scard:var(--a-card)}
.v-soft{--sbg:var(--s-bg);--sink:var(--s-ink);--smut:var(--s-mut);--sline:var(--s-line);--scard:var(--s-card)}
.kick{font:600 calc(var(--u)*1.05)/1 var(--fb);letter-spacing:.16em;text-transform:uppercase;color:var(--sac,var(--ac));margin-bottom:calc(var(--u)*1.6)}
.v-accent .kick{color:var(--a-ink);opacity:.7}
h2{font-family:var(--fh);font-weight:var(--hw);letter-spacing:var(--ht);font-size:calc(var(--u)*4.3);line-height:1.04;max-width:22em;text-wrap:balance}
h2 em,h1 em{font-style:var(--emst,normal);color:var(--sac,var(--ac))}
.v-accent h2 em,.v-accent h1 em{color:inherit;opacity:.62}
.lead{font-size:calc(var(--u)*1.75);color:var(--smut);max-width:36em;margin-top:calc(var(--u)*1.6);text-wrap:pretty}
.grow{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;margin-top:calc(var(--u)*2.4)}
.num{position:absolute;right:calc(var(--u)*3);bottom:calc(var(--u)*2.2);font:500 calc(var(--u)*1)/1 var(--fb);color:var(--smut);letter-spacing:.08em}
.brandm{position:absolute;left:calc(var(--u)*6);bottom:calc(var(--u)*2.2);font:600 calc(var(--u)*1)/1 var(--fb);color:var(--smut);letter-spacing:.08em;text-transform:uppercase}
[data-a]{opacity:0;transform:translateY(calc(var(--u)*1.4));transition:opacity .6s,transform .7s cubic-bezier(.2,.7,.2,1);transition-delay:calc(var(--i,0) * 70ms + 120ms)}
.sl.on [data-a]{opacity:1;transform:none}
/* обложка */
.t-cover .in{justify-content:flex-end}
.t-cover h1{font-family:var(--fh);font-weight:var(--hw);letter-spacing:var(--ht);font-size:calc(var(--u)*7.4);line-height:.98;max-width:13em;text-wrap:balance}
.t-cover .lead{font-size:calc(var(--u)*2)}
.t-cover .meta{display:flex;gap:calc(var(--u)*3);margin-top:calc(var(--u)*3.4);font-size:calc(var(--u)*1.2);color:var(--smut);flex-wrap:wrap}
.t-cover .meta b{display:block;color:var(--sink);font-weight:600;font-size:calc(var(--u)*1.4)}
.t-cover .logo{position:absolute;left:calc(var(--u)*6);top:calc(var(--u)*4.4);font:var(--hw) calc(var(--u)*1.9)/1 var(--fh);letter-spacing:var(--ht);display:flex;align-items:center;gap:.5em}
.t-cover .logo i{width:1.5em;height:1.5em;border-radius:28%;background:var(--sac,var(--ac));color:var(--aci);display:grid;place-items:center;font-style:normal;font-size:.8em}
.v-accent .logo i{background:var(--a-ink);color:var(--a-bg)}
.t-cover .badge{position:absolute;right:calc(var(--u)*6);top:calc(var(--u)*4.4);font:600 calc(var(--u)*1.05)/1 var(--fb);letter-spacing:.14em;text-transform:uppercase;padding:.8em 1.2em;border:1px solid var(--sline);border-radius:99px}
.bgimg{position:absolute;inset:0}.bgimg img{width:100%;height:100%;object-fit:cover}
.bgimg::after{content:"";position:absolute;inset:0;background:var(--shade,linear-gradient(90deg,rgba(0,0,0,.78),rgba(0,0,0,.35) 60%,rgba(0,0,0,.2)))}
.t-cover.pic{--sink:#fff;--smut:rgba(255,255,255,.78);--sline:rgba(255,255,255,.4);color:#fff}
/* текст + тезисы */
.two{display:grid;grid-template-columns:1.05fr .95fr;gap:calc(var(--u)*5);align-items:center}
.pts{display:grid;gap:calc(var(--u)*1.2)}
.pts li{display:grid;grid-template-columns:auto 1fr;gap:calc(var(--u)*1.4);padding:calc(var(--u)*1.5) 0;border-top:1px solid var(--sline)}
.pts li:last-child{border-bottom:1px solid var(--sline)}
.pts i{font:var(--hw) calc(var(--u)*1.5)/1.2 var(--fh);font-style:normal;color:var(--sac,var(--ac));min-width:1.6em}
.pts b{display:block;font-size:calc(var(--u)*1.75);font-weight:600;line-height:1.25}
.pts span{display:block;color:var(--smut);margin-top:.25em}
/* карточки */
.cards{display:grid;grid-template-columns:repeat(var(--c,3),1fr);gap:calc(var(--u)*1.4)}
.card{background:var(--scard);border-radius:var(--r);padding:calc(var(--u)*2.1);display:flex;flex-direction:column;gap:calc(var(--u)*.8);min-height:calc(var(--u)*15)}
.card i{font-style:normal;font:var(--hw) calc(var(--u)*2.2)/1 var(--fh);color:var(--sac,var(--ac));margin-bottom:auto}
.card b{font-size:calc(var(--u)*1.75);font-weight:600;line-height:1.2;margin-top:calc(var(--u)*1.4)}
.card span{color:var(--smut);font-size:calc(var(--u)*1.35)}
/* цифры */
.stats{display:grid;grid-template-columns:repeat(var(--c,3),1fr);gap:calc(var(--u)*1.4)}
.stat{border-top:2px solid var(--sink);padding-top:calc(var(--u)*1.6)}
.stat b{display:block;font:var(--hw) calc(var(--u)*6)/1 var(--fh);letter-spacing:var(--ht);white-space:nowrap}
.stats[style*="4"] .stat b{font-size:calc(var(--u)*4.6)}
.stat strong{display:block;font-weight:600;font-size:calc(var(--u)*1.6);margin-top:calc(var(--u)*1.2)}
.stat>span{display:block;color:var(--smut);font-size:calc(var(--u)*1.3);margin-top:.3em}
/* столбцы */
.chart{display:grid;grid-template-columns:.8fr 1.2fr;gap:calc(var(--u)*5);align-items:end;flex:1;min-height:0;margin-top:calc(var(--u)*2)}
.chart .txt{align-self:center}
.bars{display:flex;align-items:flex-end;gap:calc(var(--u)*1.2);height:calc(var(--u)*24);border-bottom:1px solid var(--sline)}
.bar{flex:1;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;height:100%;position:relative}
.bar s{display:block;width:100%;height:calc(var(--h) * 1%);background:color-mix(in srgb,var(--sink) 16%,transparent);border-radius:calc(var(--r)*.5) calc(var(--r)*.5) 0 0;transform-origin:bottom;transform:scaleY(0);transition:transform .9s cubic-bezier(.2,.7,.2,1);transition-delay:calc(var(--i) * 80ms + 200ms)}
.bar.hl s{background:var(--sac,var(--ac))}
.sl.on .bar s{transform:none}
.bar b{font-weight:600;font-size:calc(var(--u)*1.4);margin-bottom:.4em;white-space:nowrap}
.bar em{position:absolute;top:100%;margin-top:.6em;font-style:normal;font-size:calc(var(--u)*1.15);color:var(--smut);white-space:nowrap}
.hbars{display:grid;gap:calc(var(--u)*1.3)}
.hbar{display:grid;grid-template-columns:calc(var(--u)*17) 1fr auto;gap:calc(var(--u)*1.4);align-items:center}
.hbar span{font-size:calc(var(--u)*1.4)}
.hbar s{display:block;height:calc(var(--u)*2.4);background:color-mix(in srgb,var(--sink) 10%,transparent);border-radius:calc(var(--r)*.4);position:relative;overflow:hidden}
.hbar s::after{content:"";position:absolute;inset:0;width:calc(var(--h) * 1%);background:var(--sink);border-radius:inherit;transform-origin:left;transform:scaleX(0);transition:transform 1s cubic-bezier(.2,.7,.2,1);transition-delay:calc(var(--i) * 90ms + 200ms)}
.hbar.hl s::after{background:var(--sac,var(--ac))}
.sl.on .hbar s::after{transform:none}
.hbar b{font-weight:600;font-size:calc(var(--u)*1.5);min-width:4.5em;text-align:right;white-space:nowrap}
/* линия */
.lchart{position:relative}.lchart svg{width:100%;height:auto;display:block;overflow:visible}
.lchart .ln{fill:none;stroke-width:3;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:1;stroke-dashoffset:1;transition:stroke-dashoffset 1.6s cubic-bezier(.3,.6,.2,1) .25s}
.sl.on .lchart .ln{stroke-dashoffset:0}
.lchart .ar{opacity:0;transition:opacity .8s 1s}.sl.on .lchart .ar{opacity:.16}
.lchart text{font:500 15px var(--fb);fill:var(--smut)}
.lchart .dot{opacity:0;transition:opacity .4s 1.5s}.sl.on .lchart .dot{opacity:1}
.legend{display:flex;gap:calc(var(--u)*2);margin-top:calc(var(--u)*1.2);font-size:calc(var(--u)*1.25);color:var(--smut);flex-wrap:wrap}
.legend i{display:inline-block;width:1em;height:.3em;border-radius:2px;margin-right:.5em;vertical-align:middle}
/* кольцо */
.donut{display:grid;grid-template-columns:.9fr 1.1fr;gap:calc(var(--u)*5);align-items:center}
.donut figure{position:relative;max-width:calc(var(--u)*30);justify-self:center;width:100%}
.donut svg{width:100%;display:block;transform:rotate(-90deg)}
.donut circle{fill:none;stroke-width:13;transition:stroke-dasharray 1.1s cubic-bezier(.2,.7,.2,1);transition-delay:calc(var(--i) * 140ms + 200ms)}
.sl:not(.on) .donut circle.sg{stroke-dasharray:0 100!important}
.donut figcaption{position:absolute;inset:0;display:grid;place-content:center;text-align:center}
.donut figcaption b{font:var(--hw) calc(var(--u)*4.2)/1 var(--fh);letter-spacing:var(--ht)}
.donut figcaption span{font-size:calc(var(--u)*1.2);color:var(--smut);margin-top:.4em}
.dl li{display:grid;grid-template-columns:auto 1fr auto;gap:calc(var(--u)*1.2);align-items:baseline;padding:calc(var(--u)*1.2) 0;border-bottom:1px solid var(--sline)}
.dl i{width:.8em;height:.8em;border-radius:50%;align-self:center}
.dl b{font-weight:600;font-size:calc(var(--u)*1.6)}.dl span{display:block;color:var(--smut);font-size:calc(var(--u)*1.25)}
.dl em{font:var(--hw) calc(var(--u)*2.2)/1 var(--fh);font-style:normal}
/* таблица */
.tbl{width:100%;border-collapse:collapse;font-size:calc(var(--u)*1.45)}
.tbl th{font:600 calc(var(--u)*1.05)/1.2 var(--fb);letter-spacing:.1em;text-transform:uppercase;color:var(--smut);text-align:left;padding:0 calc(var(--u)*1.4) calc(var(--u)*1.2)}
.tbl td{padding:calc(var(--u)*1.25) calc(var(--u)*1.4);border-top:1px solid var(--sline);vertical-align:top}
.tbl td:first-child,.tbl th:first-child{padding-left:0;font-weight:600}
.tbl .hl{background:var(--scard)}.tbl th.hl{color:var(--sac,var(--ac));border-radius:var(--r) var(--r) 0 0;padding-top:calc(var(--u)*1.2)}
.tbl tr:last-child td.hl{border-radius:0 0 var(--r) var(--r)}
/* шаги */
.steps{display:grid;grid-template-columns:repeat(var(--c,4),1fr);gap:calc(var(--u)*1.4);counter-reset:s}
.step{position:relative;padding-top:calc(var(--u)*2.6)}
.step::before{content:"";position:absolute;left:0;right:calc(var(--u)*-1.4);top:calc(var(--u)*.55);height:2px;background:var(--sline)}
.step:last-child::before{right:0}
.step::after{content:"";position:absolute;left:0;top:0;width:calc(var(--u)*1.2);height:calc(var(--u)*1.2);border-radius:50%;background:var(--sac,var(--ac))}
.step small{display:block;font:600 calc(var(--u)*1.05)/1 var(--fb);letter-spacing:.12em;text-transform:uppercase;color:var(--sac,var(--ac))}
.step b{display:block;font-size:calc(var(--u)*1.7);font-weight:600;line-height:1.2;margin:.6em 0 .4em}
.step span{color:var(--smut);font-size:calc(var(--u)*1.3)}
/* фото + текст */
.split{display:grid;grid-template-columns:1fr 1fr;height:100%}
.t-split .in{padding:0}
.split .tx{padding:calc(var(--u)*5) calc(var(--u)*5) calc(var(--u)*5) calc(var(--u)*6);display:flex;flex-direction:column;justify-content:center}
.split .ph{position:relative;overflow:hidden}.split .ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.split.r .ph{order:-1}.split.r .tx{padding-left:calc(var(--u)*5);padding-right:calc(var(--u)*6)}
.chk{display:grid;gap:calc(var(--u)*.9);margin-top:calc(var(--u)*2.2)}
.chk li{padding-left:1.7em;position:relative}
.chk li::before{content:"";position:absolute;left:0;top:.5em;width:.75em;height:.4em;border-left:2px solid var(--sac,var(--ac));border-bottom:2px solid var(--sac,var(--ac));transform:rotate(-45deg)}
/* цитата */
.t-quote .in{justify-content:center}
.t-quote blockquote{margin:0;font:var(--hw) calc(var(--u)*4)/1.16 var(--fh);letter-spacing:var(--ht);max-width:20em;text-wrap:balance}
.t-quote cite{display:block;font-style:normal;margin-top:calc(var(--u)*2.6);color:var(--smut);font-size:calc(var(--u)*1.5)}
.t-quote cite b{color:var(--sink);font-weight:600}
/* тарифы */
.plans{display:grid;grid-template-columns:repeat(var(--c,3),1fr);gap:calc(var(--u)*1.4);align-items:stretch}
.plan{background:var(--scard);border-radius:var(--r);padding:calc(var(--u)*2.2);display:flex;flex-direction:column}
.plan.hl{background:var(--sink);color:var(--sbg)}.plan.hl span,.plan.hl li{color:inherit;opacity:.8}
.plan small{font:600 calc(var(--u)*1.05)/1 var(--fb);letter-spacing:.12em;text-transform:uppercase}
.plan b{font:var(--hw) calc(var(--u)*3.4)/1 var(--fh);letter-spacing:var(--ht);margin:calc(var(--u)*1.2) 0 .3em;white-space:nowrap}
.plan span{color:var(--smut);font-size:calc(var(--u)*1.25)}
.plan ul{margin-top:calc(var(--u)*1.4);display:grid;gap:.5em;font-size:calc(var(--u)*1.3)}
.plan li{padding-left:1.2em;position:relative;color:var(--smut)}.plan li::before{content:"+";position:absolute;left:0}
/* калькулятор */
.calc{display:grid;grid-template-columns:1fr 1fr;gap:calc(var(--u)*5);align-items:center}
.cin{display:grid;gap:calc(var(--u)*2)}
.cin label{display:block}
.cin .row{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:.6em}
.cin .row span{color:var(--smut)}.cin .row b{font:var(--hw) calc(var(--u)*2.1)/1 var(--fh);white-space:nowrap}
.cin input{width:100%;accent-color:var(--sac,var(--ac));height:calc(var(--u)*1.6)}
.cout{background:var(--scard);border-radius:var(--r);padding:calc(var(--u)*2.6);display:grid;gap:calc(var(--u)*1.6)}
.cout div{display:flex;justify-content:space-between;align-items:baseline;gap:1em;padding-bottom:calc(var(--u)*1.4);border-bottom:1px solid var(--sline)}
.cout div:last-of-type{border:0;padding:0}
.cout span{color:var(--smut)}.cout b{font:var(--hw) calc(var(--u)*2.6)/1 var(--fh);white-space:nowrap}
.cout .big b{font-size:calc(var(--u)*4.6);color:var(--sac,var(--ac))}
.cout p{font-size:calc(var(--u)*1.15);color:var(--smut)}
/* финал */
.t-end .in{justify-content:center}
.t-end h2{font-size:calc(var(--u)*6);max-width:14em}
.cts{display:flex;gap:calc(var(--u)*4);margin-top:calc(var(--u)*4);flex-wrap:wrap}
.cts small{display:block;font:600 calc(var(--u)*1.05)/1 var(--fb);letter-spacing:.12em;text-transform:uppercase;color:var(--smut);margin-bottom:.7em}
.cts b{font-weight:600;font-size:calc(var(--u)*1.8)}
/* панель */
.barx{position:fixed;left:0;right:0;bottom:0;height:var(--bar);z-index:20;display:flex;align-items:center;gap:14px;padding:0 16px;background:var(--page);color:var(--pink);font-size:14px;border-top:1px solid rgba(128,128,128,.22)}
.barx .brand{font-weight:700;letter-spacing:.02em;white-space:nowrap}
.barx .ttl{opacity:.6;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0;flex:1}
.barx button{height:36px;min-width:36px;padding:0 10px;border-radius:9px;display:grid;place-items:center;background:rgba(128,128,128,.16)}
.barx button:hover{background:rgba(128,128,128,.3)}
.barx .cnt{font-variant-numeric:tabular-nums;min-width:4.2em;text-align:center}
.prog{position:fixed;left:0;right:0;bottom:var(--bar);height:3px;z-index:21;background:rgba(128,128,128,.2)}
.prog i{display:block;height:100%;width:0;background:var(--ac);transition:width .4s}
.toc{position:fixed;inset:0;z-index:40;background:var(--page);color:var(--pink);padding:clamp(20px,4vw,56px);overflow:auto;display:none}
.toc.open{display:block}
.toc h3{font:var(--hw) clamp(24px,3vw,40px)/1.1 var(--fh);margin-bottom:24px}
.toc ol{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px}
.toc button{width:100%;text-align:left;padding:16px;border-radius:12px;background:rgba(128,128,128,.14);display:grid;gap:6px}
.toc button:hover,.toc button[aria-current=true]{background:var(--ac);color:var(--aci)}
.toc small{opacity:.6;font-size:12px;letter-spacing:.1em}.toc b{font-weight:600;font-size:16px}
.toc .x{position:fixed;right:20px;top:16px;width:44px;height:44px;border-radius:50%;background:rgba(128,128,128,.2);font-size:22px}
.hint{position:fixed;left:50%;bottom:calc(var(--bar) + 18px);transform:translateX(-50%);z-index:19;background:rgba(0,0,0,.72);color:#fff;font-size:13px;padding:9px 14px;border-radius:99px;transition:opacity .5s;pointer-events:none}
.hint.off{opacity:0}
@media (prefers-reduced-motion:reduce){*{transition:none!important}.hint{display:none}}
/* телефон и узкие экраны: лента слайдов */
@media screen and (max-width:760px),screen and (orientation:portrait) and (max-width:1100px){
html,body{height:auto}
.deck{position:static;display:block;padding-bottom:calc(var(--bar) + 8px)}
.sl{--u:clamp(9.4px,2.75vw,13px);position:relative;width:100%;aspect-ratio:auto;opacity:1;visibility:visible;transform:none;container-type:normal;min-height:0}
.sl .in{position:relative;inset:auto;padding:calc(var(--u)*5) 20px calc(var(--u)*6);font-size:16px}
.sl.t-cover .in{min-height:86svh}
[data-a]{opacity:0}.sl.seen [data-a]{opacity:1;transform:none}
.sl.seen .bar s,.sl.seen .hbar s::after{transform:none}.sl.seen .lchart .ln{stroke-dashoffset:0}.sl.seen .lchart .ar{opacity:.16}.sl.seen .lchart .dot{opacity:1}
.sl:not(.seen) .donut circle.sg{stroke-dasharray:0 100!important}.sl.seen .donut circle.sg{stroke-dasharray:var(--da)!important}
h2{font-size:calc(var(--u)*3.3)}.t-cover h1{font-size:calc(var(--u)*4.6)}.t-end h2{font-size:calc(var(--u)*4)}
.lead,.t-cover .lead{font-size:17px}
.two,.chart,.donut,.calc,.split{grid-template-columns:1fr;gap:28px}
.cards,.stats,.plans,.steps{grid-template-columns:1fr 1fr}
.cards[style*="--c:3"],.plans,.steps{grid-template-columns:1fr}
.card{min-height:0;padding:18px}.card b{font-size:18px;margin-top:10px}.card span{font-size:15px}.card i{font-size:22px}
.stat b{font-size:calc(var(--u)*3.6)!important}.stat strong{font-size:16px}.stat>span{font-size:14px}
.pts b{font-size:18px}.pts i{font-size:18px}
.bars{height:220px;gap:6px}.bar b{font-size:12px}.bar em{font-size:11px}
.hbar{grid-template-columns:1fr auto;gap:6px 12px}.hbar span{grid-column:1/-1;font-size:15px}.hbar s{height:18px}.hbar b{font-size:15px}
.tbl{font-size:14px}.tbl th{font-size:10.5px;padding:0 8px 10px}.tbl td{padding:10px 8px}
.step{padding-top:26px}.step::before{right:0;top:6px}.step::after{width:13px;height:13px}.step b{font-size:18px}.step span{font-size:15px}.step small{font-size:11px}
.steps{gap:22px}
.split .tx{padding:calc(var(--u)*5) 20px}.split .ph{aspect-ratio:4/3}.split.r .ph{order:0}.split.r .tx{padding:calc(var(--u)*5) 20px}
.t-quote blockquote{font-size:calc(var(--u)*2.7)}.t-quote cite{font-size:15px}
.plan{padding:20px}.plan b{font-size:30px}.plan span,.plan ul{font-size:15px}.plan small{font-size:11px}
.cin .row b{font-size:22px}.cout{padding:20px}.cout b{font-size:24px}.cout .big b{font-size:38px}.cout p{font-size:13px}
.dl b{font-size:16px}.dl span{font-size:14px}.dl em{font-size:22px}.donut figcaption b{font-size:34px}.donut figcaption span{font-size:13px}.donut figure{max-width:260px}
.cts{gap:22px}.cts b{font-size:18px}.cts small{font-size:11px}
.kick{font-size:11.5px;margin-bottom:14px}.num,.brandm{font-size:11px;bottom:14px}.brandm{left:20px}.num{right:20px}
.t-cover .logo{left:20px;top:22px;font-size:20px}.t-cover .badge{right:20px;top:22px;font-size:10.5px}.t-cover .meta{font-size:13px;gap:20px}.t-cover .meta b{font-size:15px}
.legend{font-size:13px}.grow{margin-top:26px}
.barx .ttl,.barx #fs{display:none}.barx{justify-content:space-between}.hint{display:none}
}
"""

JS = r"""
(function(){'use strict';
var D=document,S=[].slice.call(D.querySelectorAll('.sl')),cur=0,n=S.length;
var feed=window.matchMedia('screen and (max-width:760px),screen and (orientation:portrait) and (max-width:1100px)');
var NB=' ';
function fmt(v,d){var s=Number(v).toFixed(d||0).split('.');s[0]=s[0].replace(/\B(?=(\d{3})+(?!\d))/g,NB);return s.join(',')}
function count(sl){[].forEach.call(sl.querySelectorAll('[data-to]'),function(el){if(el._done)return;el._done=1;var to=+el.dataset.to,d=+el.dataset.d||0,t0=null;
 if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){el.textContent=fmt(to,d);return}
 function step(t){if(!t0)t0=t;var k=Math.min(1,(t-t0)/1100);k=1-Math.pow(1-k,3);el.textContent=fmt(to*k,d);if(k<1)requestAnimationFrame(step)}requestAnimationFrame(step)})}
function show(i,noHash){i=Math.max(0,Math.min(n-1,i));
 if(feed.matches){S[i].scrollIntoView({behavior:'smooth',block:'start'});return}
 S.forEach(function(s,k){s.classList.toggle('on',k===i);s.classList.toggle('was',k<i);s.setAttribute('aria-hidden',k!==i)});cur=i;ui();count(S[i]);
 if(!noHash)history.replaceState(null,'','#'+(i+1))}
function ui(){D.getElementById('cnt').textContent=(cur+1)+' / '+n;D.getElementById('ttl').textContent=S[cur].dataset.t||'';D.getElementById('pg').style.width=((cur+1)/n*100)+'%';
 [].forEach.call(D.querySelectorAll('.toc button[data-i]'),function(b){b.setAttribute('aria-current',+b.dataset.i===cur)})}
D.getElementById('prev').onclick=function(){show(cur-1)};D.getElementById('next').onclick=function(){show(cur+1)};
var toc=D.getElementById('toc');function tocOpen(o){toc.classList.toggle('open',o)}
D.getElementById('tocb').onclick=function(){tocOpen(true)};D.getElementById('tocx').onclick=function(){tocOpen(false)};
toc.addEventListener('click',function(e){var b=e.target.closest('button[data-i]');if(!b)return;tocOpen(false);show(+b.dataset.i)});
var fs=D.getElementById('fs');if(fs)fs.onclick=function(){if(D.fullscreenElement)D.exitFullscreen();else if(D.documentElement.requestFullscreen)D.documentElement.requestFullscreen()};
D.addEventListener('keydown',function(e){if(e.target.matches&&e.target.matches('input,textarea,select'))return;var k=e.key;
 if(k==='Escape'){tocOpen(false);return}
 if(k==='ArrowRight'||k==='PageDown'||k===' '||k==='Enter'){e.preventDefault();show(cur+1)}
 else if(k==='ArrowLeft'||k==='PageUp'){e.preventDefault();show(cur-1)}
 else if(k==='Home')show(0);else if(k==='End')show(n-1);else if(k==='f'||k==='F'||k==='а'||k==='А'){if(fs)fs.click()}
 else if(k==='g'||k==='G'||k==='п'||k==='П')tocOpen(!toc.classList.contains('open'))});
D.getElementById('deck').addEventListener('click',function(e){if(feed.matches||e.target.closest('input,button,a,label,.cin,.cout'))return;var r=this.getBoundingClientRect();show(cur+((e.clientX-r.left)/r.width<.25?-1:1))});
var tx=null;D.addEventListener('touchstart',function(e){tx=e.touches[0].clientX},{passive:true});
D.addEventListener('touchend',function(e){if(feed.matches||tx===null)return;var dx=e.changedTouches[0].clientX-tx;tx=null;if(Math.abs(dx)>50)show(cur+(dx<0?1:-1))},{passive:true});
/* лента на телефоне: показ при появлении, счётчик по прокрутке */
var io='IntersectionObserver'in window?new IntersectionObserver(function(es){es.forEach(function(x){if(!x.isIntersecting)return;x.target.classList.add('seen');count(x.target);
 if(feed.matches){cur=S.indexOf(x.target);ui()}})},{threshold:.28}):null;
S.forEach(function(s){if(io)io.observe(s);else s.classList.add('seen')});
/* калькуляторы */
[].forEach.call(D.querySelectorAll('.calc'),function(c){var cfg=JSON.parse(c.dataset.cfg),F={money:function(x){return fmt(Math.abs(x)>=1e6?Math.round(x/1000)*1000:Math.round(x))+NB+'₽'},num:function(x){return fmt(Math.round(x))},pct:function(x){return fmt(x,1)+NB+'%'},dec:function(x){return fmt(x,1)},
  mon:function(x){x=Math.max(0,Math.round(x));return x+NB+(x%10===1&&x%100!==11?'месяц':x%10>1&&x%10<5&&(x%100<10||x%100>20)?'месяца':'месяцев')},mln:function(x){return fmt(x/1e6,1)+NB+'млн'+NB+'₽'},x:function(x){return '×'+fmt(x,1)}};
 function run(){var v={};cfg.inputs.forEach(function(i){var el=c.querySelector('[data-in="'+i.id+'"]');v[i.id]=+el.value;c.querySelector('[data-iv="'+i.id+'"]').textContent=F[i.fmt||'num'](v[i.id])+(i.unit?NB+i.unit:'')});
  cfg.outputs.forEach(function(o,k){var r;try{r=(new Function('v','return '+o.expr))(v)}catch(err){r=0}c.querySelector('[data-out="'+k+'"]').textContent=isFinite(r)?F[o.fmt||'num'](r)+(o.unit?NB+o.unit:''):'—'})}
 c.addEventListener('input',run);run()});
var h=parseInt(location.hash.slice(1),10);show(h>=1&&h<=n?h-1:0,true);
var hint=D.getElementById('hint');if(hint)setTimeout(function(){hint.classList.add('off')},4200);
window.__deck={show:show,n:n};
})();
"""

_NUM = re.compile(r"^([^\d]*?)(\d[\d\s ]*(?:[.,]\d+)?)(.*)$", re.S)


def _count(v: str) -> str:
    """«128 млн ₽» → число досчитывается от нуля при показе слайда; текст без числа — как есть."""
    m = _NUM.match(v)
    if not m or re.match(r"\s*[:×x/–-]\s*\d", m.group(3)) or v.strip().startswith(("−", "-", "×")):
        return e(v)  # время «7:30», диапазон «3–5», «×2» — не досчитываем, показываем как есть
    raw = re.sub(r"[\s ]", "", m.group(2)).replace(",", ".")
    dec = len(raw.split(".")[1]) if "." in raw else 0
    shown = m.group(2).strip()
    gap = "\u00a0" if m.group(2) != m.group(2).rstrip() else ""  # «1 284 млн ₽»: пробел перед единицей не теряем
    return f'{e(m.group(1))}<span data-to="{raw}" data-d="{dec}">{e(shown)}</span>{gap}{e(m.group(3))}'


def _head(s: dict, i: int = 0) -> str:
    k = f'<div class="kick" data-a style="--i:{i}">{e(s["k"])}</div>' if s.get("k") else ""
    h = f'<h2 data-a style="--i:{i + 1}">{s["h"]}</h2>' if s.get("h") else ""
    p = f'<p class="lead" data-a style="--i:{i + 2}">{s["p"]}</p>' if s.get("p") else ""
    return k + h + p


def _line_svg(s: dict, colors: list[str]) -> str:
    W, H, pl, pb, pt = 760, 360, 8, 34, 16
    series, labels = s["series"], s["labels"]
    hi, lo = max(max(x["pts"]) for x in series), min(min(x["pts"]) for x in series)
    top, low = hi + (hi - lo) * 0.18, max(0.0, lo - (hi - lo) * 0.45)  # ось от близкого минимума: рост виден, а не полоска
    n = len(labels)

    def xy(i, v):
        return pl + (W - pl * 2) * i / (n - 1), pt + (H - pt - pb) * (1 - (v - low) / (top - low))
    out_ = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{e(s.get("alt", "График"))}">']
    for g in range(4):
        y = pt + (H - pt - pb) * g / 3
        out_.append(f'<line x1="{pl}" x2="{W - pl}" y1="{y:.1f}" y2="{y:.1f}" stroke="currentColor" opacity=".12"/>')
    for i, lb in enumerate(labels):
        x, _ = xy(i, 0)
        anchor = "start" if i == 0 else "end" if i == n - 1 else "middle"
        out_.append(f'<text x="{x:.1f}" y="{H - 8}" text-anchor="{anchor}">{e(lb)}</text>')
    for k, ser in enumerate(series):
        col = colors[k % len(colors)]
        pts = [xy(i, v) for i, v in enumerate(ser["pts"])]
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        if ser.get("area"):
            out_.append(f'<path class="ar" d="{d} L{pts[-1][0]:.1f} {H - pb} L{pts[0][0]:.1f} {H - pb} Z" fill="{col}"/>')
        out_.append(f'<path class="ln" pathLength="1" d="{d}" stroke="{col}"/>')
        x, y = pts[-1]
        out_.append(f'<g class="dot"><circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{col}"/>'
                    f'<text x="{x - 12:.1f}" y="{y - 12:.1f}" text-anchor="end" style="font-weight:700;fill:currentColor;font-size:19px">{e(ser.get("last", ""))}</text></g>')
    out_.append("</svg>")
    legend = "".join(f'<span><i style="background:{colors[k % len(colors)]}"></i>{e(x["name"])}</span>' for k, x in enumerate(series))
    return f'<div class="lchart" data-a style="--i:3">{"".join(out_)}<div class="legend">{legend}</div></div>'


def _slide(s: dict, i: int, n: int, c: dict) -> str:
    t, I = s["t"], c.get("images", {})
    pal = c["palette"]
    body = ""
    cls = ""
    if t == "cover":
        bg = f'<div class="bgimg">{img(s["img"], I, "100vw", eager=True)}</div>' if s.get("img") else ""
        cls = " pic" if s.get("img") else ""
        meta = "".join(f"<div><b>{e(a)}</b>{e(b)}</div>" for a, b in s.get("meta", []))
        badge = f'<div class="badge" data-a>{e(s["badge"])}</div>' if s.get("badge") else ""
        body = (f'{bg}<div class="in"><div class="logo" data-a><i>{c.get("logoIcon", c["brand"][0])}</i>{e(c["brand"])}</div>{badge}'
                f'{"<div class=kick data-a>" + e(s["k"]) + "</div>" if s.get("k") else ""}<h1 data-a style="--i:1">{s["h"]}</h1>'
                f'{"<p class=lead data-a style=--i:2>" + s["p"] + "</p>" if s.get("p") else ""}<div class="meta" data-a style="--i:3">{meta}</div></div>')
    elif t == "text":
        pts = "".join(f'<li data-a style="--i:{k + 2}"><i>{k + 1:02d}</i><div><b>{e(a)}</b><span>{e(b)}</span></div></li>' for k, (a, b) in enumerate(s["points"]))
        body = f'<div class="in"><div class="two" style="flex:1"><div>{_head(s)}</div><ul class="pts">{pts}</ul></div></div>'
    elif t == "cards":
        items = "".join(f'<div class="card" data-a style="--i:{k + 2}"><i>{a}</i><b>{e(b)}</b><span>{e(x)}</span></div>' for k, (a, b, x) in enumerate(s["items"]))
        body = f'<div class="in">{_head(s)}<div class="grow"><div class="cards" style="--c:{s.get("cols", len(s["items"]))}">{items}</div></div></div>'
    elif t == "stats":
        items = "".join(f'<div class="stat" data-a style="--i:{k + 2}"><b>{_count(v)}</b><strong>{e(a)}</strong><span>{e(b)}</span></div>' for k, (v, a, b) in enumerate(s["items"]))
        body = f'<div class="in">{_head(s)}<div class="grow"><div class="stats" style="--c:{len(s["items"])}">{items}</div></div></div>'
    elif t == "bars":
        top = max(v for _, v, *_ in s["data"])
        if s.get("dir") == "h":
            rows = "".join(f'<div class="hbar{" hl" if (r[3:] and r[3]) else ""}" style="--h:{v / top * 100:.1f};--i:{k}"><span>{e(lb)}</span><s></s><b>{e(r[2])}</b></div>'
                           for k, r in enumerate(s["data"]) for lb, v in [(r[0], r[1])])
            body = f'<div class="in">{_head(s)}<div class="grow"><div class="hbars" data-a style="--i:3">{rows}</div></div></div>'
        else:
            cols = "".join(f'<div class="bar{" hl" if (r[3:] and r[3]) else ""}" style="--h:{r[1] / top * 86:.1f};--i:{k}"><b>{e(r[2])}</b><s></s><em>{e(r[0])}</em></div>'
                           for k, r in enumerate(s["data"]))
            body = (f'<div class="in"><div class="chart"><div class="txt">{_head(s)}</div><div data-a style="--i:3;padding-bottom:calc(var(--u)*2.4)">'
                    f'<div class="bars">{cols}</div></div></div></div>')
    elif t == "line":
        body = f'<div class="in"><div class="chart" style="align-items:center"><div class="txt">{_head(s)}</div>{_line_svg(s, pal)}</div></div>'
    elif t == "donut":
        circ, off, lis = [], 0.0, []
        for k, (lb, pct, note) in enumerate(s["items"]):
            col = pal[k % len(pal)]
            circ.append(f'<circle class="sg" cx="50" cy="50" r="42" pathLength="100" stroke="{col}" stroke-dasharray="{pct - 0.8:.1f} {100 - pct + 0.8:.1f}" '
                        f'stroke-dashoffset="{-off:.1f}" style="--i:{k};--da:{pct - 0.8:.1f} {100 - pct + 0.8:.1f}"/>')
            off += pct
            lis.append(f'<li data-a style="--i:{k + 2}"><i style="background:{col}"></i><div><b>{e(lb)}</b><span>{e(note)}</span></div><em>{pct}%</em></li>')
        cen = s.get("center", ("", ""))
        body = (f'<div class="in">{_head(s)}<div class="grow"><div class="donut"><figure data-a style="--i:2"><svg viewBox="0 0 100 100">'
                f'<circle cx="50" cy="50" r="42" stroke="currentColor" opacity=".1" style="stroke-width:13;fill:none"/>{"".join(circ)}</svg>'
                f'<figcaption><b>{e(cen[0])}</b><span>{e(cen[1])}</span></figcaption></figure><ul class="dl">{"".join(lis)}</ul></div></div></div>')
    elif t == "table":
        hl = s.get("hl", -1)
        th = "".join(f'<th class="{"hl" if k == hl else ""}">{e(x)}</th>' for k, x in enumerate(s["cols"]))
        trs = "".join("<tr>" + "".join(f'<td class="{"hl" if k == hl else ""}">{e(x)}</td>' for k, x in enumerate(r)) + "</tr>" for r in s["rows"])
        body = f'<div class="in">{_head(s)}<div class="grow"><table class="tbl" data-a style="--i:3"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div></div>'
    elif t == "steps":
        items = "".join(f'<div class="step" data-a style="--i:{k + 2}"><small>{e(a)}</small><b>{e(b)}</b><span>{e(x)}</span></div>' for k, (a, b, x) in enumerate(s["items"]))
        body = f'<div class="in">{_head(s)}<div class="grow"><div class="steps" style="--c:{len(s["items"])}">{items}</div></div></div>'
    elif t == "split":
        chk = "".join(f'<li data-a style="--i:{k + 3}">{e(x)}</li>' for k, x in enumerate(s.get("bullets", [])))
        body = (f'<div class="in"><div class="split {s.get("side", "")}"><div class="tx">{_head(s)}<ul class="chk">{chk}</ul></div>'
                f'<div class="ph">{img(s["img"], I, "(max-width:760px) 100vw, 50vw")}</div></div></div>')
    elif t == "quote":
        body = (f'<div class="in">{"<div class=kick data-a>" + e(s["k"]) + "</div>" if s.get("k") else ""}<blockquote data-a style="--i:1">{s["text"]}</blockquote>'
                f'<cite data-a style="--i:2"><b>{e(s["who"])}</b>{", " + e(s["role"]) if s.get("role") else ""}</cite></div>')
    elif t == "price":
        plans = "".join(f'<div class="plan{" hl" if p.get("hl") else ""}" data-a style="--i:{k + 2}"><small>{e(p["n"])}</small><b>{e(p["p"])}</b><span>{e(p["s"])}</span>'
                        f'<ul>{"".join("<li>" + e(x) + "</li>" for x in p["items"])}</ul></div>' for k, p in enumerate(s["plans"]))
        body = f'<div class="in">{_head(s)}<div class="grow"><div class="plans" style="--c:{len(s["plans"])}">{plans}</div></div></div>'
    elif t == "calc":
        ins = "".join(f'<label><div class="row"><span>{e(x["label"])}</span><b data-iv="{x["id"]}"></b></div>'
                      f'<input type="range" data-in="{x["id"]}" min="{x["min"]}" max="{x["max"]}" step="{x.get("step", 1)}" value="{x["val"]}" aria-label="{e(x["label"])}"></label>'
                      for x in s["inputs"])
        outs = "".join(f'<div class="{"big" if o.get("big") else ""}"><span>{e(o["label"])}</span><b data-out="{k}"></b></div>' for k, o in enumerate(s["outputs"]))
        cfg = {"inputs": [{k: x[k] for k in ("id", "fmt", "unit") if k in x} for x in s["inputs"]],
               "outputs": [{k: o[k] for k in ("expr", "fmt", "unit") if k in o} for o in s["outputs"]]}
        note = f'<p>{e(s["note"])}</p>' if s.get("note") else ""
        body = (f"<div class=\"in\">{_head(s)}<div class=\"grow\"><div class=\"calc\" data-cfg='{jdump(cfg)}'><div class=\"cin\" data-a style=\"--i:2\">{ins}</div>"
                f'<div class="cout" data-a style="--i:3">{outs}{note}</div></div></div></div>')
    elif t == "end":
        cts = "".join(f"<div><small>{e(a)}</small><b>{e(b)}</b></div>" for a, b in s.get("contacts", []))
        body = f'<div class="in">{_head(s)}<div class="cts" data-a style="--i:3">{cts}</div></div>'
    foot = "" if t in ("cover", "split") else f'<div class="brandm">{e(c["brand"])}</div>'
    num = "" if t == "cover" else f'<div class="num">{i + 1:02d} / {n:02d}</div>'
    return (f'<section class="sl t-{t} v-{s.get("v", "light")}{cls}" data-t="{e(s["title"])}" aria-roledescription="слайд" '
            f'aria-label="{i + 1} из {n}: {e(s["title"])}">{body}{foot}{num}</section>')


def build(c: dict) -> str:
    d = out(c["slug"])
    write_images(d, c.get("images", {}))
    th = c["theme"]
    font_css = fonts(d, c["fonts"])
    c.setdefault("palette", [th["ac"], th.get("ac2", "#888"), th.get("ac3", "#bbb"), th.get("ac4", "#ddd")])
    css_vars = ";".join(f"--{k}:{v}" for k, v in th.items())
    S = c["slides"]
    slides = "\n".join(_slide(s, i, len(S), c) for i, s in enumerate(S))
    toc = "".join(f'<li><button type="button" data-i="{i}"><small>{i + 1:02d}</small><b>{e(s["title"])}</b></button></li>' for i, s in enumerate(S))
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
<meta name="theme-color" content="{th['page']}">
<link rel="icon" href="{favicon(c.get('favLetter', c['brand'][0]), th['ac'], th['aci'])}">
<style>
{font_css}
:root{{--bar:56px;{css_vars}}}
{CSS}
{c.get('css', '')}
</style>
</head>
<body>
<main class="deck" id="deck" aria-roledescription="презентация" aria-label="{e(c['title'])}">
{slides}
</main>
<div class="prog" aria-hidden="true"><i id="pg"></i></div>
<nav class="barx" aria-label="Навигация по слайдам">
 <span class="brand">{e(c['brand'])}</span><span class="ttl" id="ttl"></span>
 <button type="button" id="tocb" aria-label="Оглавление" title="Оглавление (G)">☰</button>
 <button type="button" id="prev" aria-label="Предыдущий слайд">←</button><span class="cnt" id="cnt"></span>
 <button type="button" id="next" aria-label="Следующий слайд">→</button>
 <button type="button" id="fs" aria-label="Во весь экран" title="Во весь экран (F)">⛶</button>
</nav>
<div class="toc" id="toc" role="dialog" aria-label="Оглавление"><button type="button" class="x" id="tocx" aria-label="Закрыть">×</button><h3>{e(c['title'])}</h3><ol>{toc}</ol></div>
<div class="hint" id="hint">Листайте стрелками или кликом · F — во весь экран</div>
<script>{JS}</script>
</body>
</html>
"""
    save(d, page)
    return d
