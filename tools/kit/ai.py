"""ИИ-ассистент для портфолио: страница продукта с рабочим окном ассистента. Два вида окна:
«chat» — диалог по сценариям (ввод своим текстом, выбор подсказок) и панель «что понял, где искал, что сделал»;
«custom» — своё рабочее окно работы (разбор договора, отбор резюме, реестр документов, отзывы) на общих блоках.
Ответы заданы в конфиге и собираются из текста пользователя правилами — без обращения к модели."""
from __future__ import annotations

from .common import e, favicon, fonts, jdump, out, save, write_images

CSS = r"""
*,*::before,*::after{box-sizing:border-box}
[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth;overflow-x:clip}
body{margin:0;background:var(--bg);color:var(--ink);font:400 16px/1.55 var(--fb);-webkit-font-smoothing:antialiased;overflow-x:clip}
a{color:inherit;text-decoration:none}
button,input,textarea,select{font:inherit;color:inherit}
button{cursor:pointer;background:none;border:0;padding:0}
:focus-visible{outline:2px solid var(--ac);outline-offset:3px;border-radius:6px}
:root{--gut:clamp(16px,4vw,48px);--ok:#17a06a;--warn:#d99600;--bad:#d9483b}
.wrap{width:min(1280px,100% - 2*var(--gut));margin-inline:auto}
h1,h2,h3{font-family:var(--fh);font-weight:var(--hw);letter-spacing:var(--ht);line-height:1.04;margin:0;overflow-wrap:break-word;text-wrap:balance}
h2{font-size:clamp(30px,4.2vw,54px)}
p{margin:0}
.kick{font:600 12px/1 var(--fb);letter-spacing:.14em;text-transform:uppercase;color:var(--kc,var(--ac))}
.lead{font-size:clamp(17px,1.5vw,20px);color:var(--soft);max-width:56ch;text-wrap:pretty}
.sec{padding:clamp(64px,9vw,120px) 0}
.sec.t0{padding-top:0}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;height:54px;padding:0 26px;border-radius:var(--rb);background:var(--ac);color:var(--aci);font-weight:600;transition:transform .2s,box-shadow .2s;white-space:nowrap}
.btn:hover{transform:translateY(-1px);box-shadow:0 12px 30px -12px var(--ac)}
.btn.ghost{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--line2)}
.top{position:sticky;top:0;z-index:30;background:color-mix(in srgb,var(--bg) 84%,transparent);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.top .bar{display:flex;align-items:center;gap:24px;height:68px}
.logo{font-family:var(--fh);font-weight:var(--hw);font-size:22px;display:flex;align-items:center;gap:10px;letter-spacing:var(--ht);white-space:nowrap}
.logo i{display:grid;place-items:center;width:34px;height:34px;border-radius:10px;background:var(--ac);color:var(--aci);font-style:normal;font-size:17px;font-family:var(--fb);font-weight:700}
.nav{display:flex;gap:24px;font-size:15px;color:var(--soft);margin-left:auto}
.nav a:hover{color:var(--ink)}
.top .btn{height:42px;padding:0 18px;font-size:15px}
/* первый экран */
.hero{padding:clamp(36px,5.5vw,84px) 0 clamp(28px,4vw,52px)}
.hg{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,.62fr);gap:clamp(24px,5vw,80px);align-items:end}
.hero h1{font-size:clamp(40px,6vw,86px);margin:18px 0 22px}
.hero h1 em{font-style:normal;color:var(--ac)}
.hero .cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:30px}
.hs{display:grid;gap:0}
.hs div{padding:16px 0;border-top:1px solid var(--line2)}
.hs div:last-child{border-bottom:1px solid var(--line2)}
.hs b{display:block;font-family:var(--fh);font-weight:var(--hw);font-size:clamp(28px,3vw,40px);letter-spacing:-.02em;line-height:1}
.hs span{font-size:14px;color:var(--mut)}
.hero-center .hg{grid-template-columns:1fr;justify-items:center;text-align:center}
.hero-center .lead{margin-inline:auto}
.hero-center .cta{justify-content:center}
.hero-center .hs{grid-template-columns:repeat(3,auto);gap:clamp(20px,5vw,72px);margin-top:8px}
.hero-center .hs div{border:0!important;padding:0}
/* рабочее окно */
.wsx{padding-bottom:clamp(56px,8vw,110px)}
.ws-n{display:flex;align-items:center;gap:10px;font-size:14px;color:var(--mut);margin-bottom:14px}
.ws-n b{flex:none;display:inline-block;width:8px;height:8px;border-radius:50%;background:var(--ok);box-shadow:0 0 0 4px color-mix(in srgb,var(--ok) 22%,transparent)}
.ws{position:relative;border-radius:var(--rw,24px);background:var(--wbg,var(--card));color:var(--wink,var(--ink));box-shadow:var(--wsh,0 60px 120px -70px rgba(0,0,0,.55),0 0 0 1px var(--line));overflow:hidden;--wl:var(--wline,color-mix(in srgb,currentColor 11%,transparent));--w2:var(--wsoft,color-mix(in srgb,currentColor 5%,transparent))}
.ws-bar{display:flex;align-items:center;gap:12px;padding:13px 18px;border-bottom:1px solid var(--wl);font-size:14px}
.ws-bar .dots{width:10px;height:10px;border-radius:50%;background:#ff5f57;box-shadow:16px 0 0 #febc2e,32px 0 0 #28c840;margin-right:36px;flex:none}
.ws-bar b{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ws-bar span{margin-left:auto;font-size:12.5px;opacity:.6;white-space:nowrap}
.panes{display:grid;min-height:0}
.pane{min-width:0;min-height:0;display:flex;flex-direction:column}
.pane+.pane{border-left:1px solid var(--wl)}
.pane-h{display:flex;align-items:center;gap:10px;padding:14px 18px 10px;font:600 11.5px/1 var(--fb);letter-spacing:.12em;text-transform:uppercase;opacity:.62}
.pane-h span{margin-left:auto;letter-spacing:0;text-transform:none;font-weight:500;font-size:12.5px}
.scroll{overflow-y:auto;min-height:0;flex:1;scrollbar-width:thin}
.tag{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:600;line-height:1;padding:6px 9px;border-radius:999px;background:var(--w2);white-space:nowrap}
.tag.ok{background:color-mix(in srgb,var(--ok) 15%,transparent);color:color-mix(in srgb,var(--ok) 80%,currentColor)}
.tag.warn{background:color-mix(in srgb,var(--warn) 18%,transparent);color:color-mix(in srgb,var(--warn) 78%,currentColor)}
.tag.bad{background:color-mix(in srgb,var(--bad) 14%,transparent);color:color-mix(in srgb,var(--bad) 85%,currentColor)}
.tag.ac{background:color-mix(in srgb,var(--ac) 15%,transparent);color:var(--act,var(--ac))}
.btn-s{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:38px;padding:8px 14px;border-radius:var(--rs2,10px);background:var(--ac);color:var(--aci);font-size:14px;font-weight:600;transition:filter .15s,transform .15s}
.btn-s:hover{filter:brightness(1.06)}
.btn-s:active{transform:scale(.98)}
.btn-s.g{background:transparent;color:inherit;box-shadow:inset 0 0 0 1.5px var(--wl)}
.btn-s[disabled]{opacity:.5;cursor:default}
.kv{display:flex;justify-content:space-between;gap:14px;font-size:14px;padding:7px 0;border-bottom:1px dashed var(--wl);animation:kin .3s both}
.kv span{opacity:.62;flex:none}
.kv b{font-weight:600;text-align:right}
@keyframes kin{from{opacity:0;transform:translateY(6px)}}
.meter{height:6px;border-radius:3px;background:var(--w2);overflow:hidden}
.meter i{display:block;height:100%;width:0;border-radius:3px;background:var(--ac);transition:width .7s cubic-bezier(.2,.8,.2,1)}
.spin{width:14px;height:14px;border-radius:50%;border:2px solid var(--wl);border-top-color:var(--ac);animation:sp .7s linear infinite;flex:none}
@keyframes sp{to{transform:rotate(360deg)}}
/* чат */
.ws-chat .panes{grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);height:min(640px,78vh)}
.chat{flex:1;overflow-y:auto;padding:18px 18px 8px;display:flex;flex-direction:column;gap:8px;scrollbar-width:thin;min-height:0}
.m{max-width:min(82%,520px);padding:10px 14px;border-radius:18px;font-size:15px;line-height:1.42;animation:kin .28s both;white-space:pre-line;overflow-wrap:break-word}
.m.b{background:var(--cin,var(--w2));align-self:flex-start;border-bottom-left-radius:6px}
.m.u{background:var(--cout,var(--ac));color:var(--coi,var(--aci));align-self:flex-end;border-bottom-right-radius:6px}
.m.rich{white-space:normal;width:min(92%,560px);max-width:none;padding:0;background:none}
.m.note{align-self:center;background:none;font-size:12.5px;opacity:.65;padding:2px 8px;text-align:center;max-width:100%}
.its{display:grid;gap:8px}
.it{position:relative;padding:14px 14px 12px;border-radius:16px;background:var(--cin,var(--w2));display:grid;gap:3px}
.it .tg{font-style:normal;font-size:11.5px;font-weight:600;color:var(--act,var(--ac));letter-spacing:.02em}
.it b{font-size:15.5px;line-height:1.25}
.it span{font-size:13.5px;opacity:.68}
.itf{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-top:8px}
.itf strong{font-size:16px;white-space:nowrap}
.itf button,.bts button{min-height:36px;padding:7px 13px;border-radius:10px;font-size:13.5px;font-weight:600;background:var(--ac);color:var(--aci)}
.kvc{padding:14px;border-radius:16px;background:var(--cin,var(--w2));font-size:14px}
.kvc h4{margin:0 0 8px;font-size:15px;font-weight:700}
.kvc .r{display:flex;justify-content:space-between;gap:14px;padding:4px 0}
.kvc .r span:first-child{opacity:.62}
.kvc .r span:last-child{text-align:right;font-weight:500}
.kvc .sum{margin-top:6px;padding-top:9px;border-top:1px dashed var(--wl);font-weight:700}
.kvc .sum span:first-child{opacity:1}
.bts{display:flex;flex-wrap:wrap;gap:6px}
.bts button.g{background:transparent;color:inherit;box-shadow:inset 0 0 0 1.5px var(--wl)}
.tr{align-self:flex-start;display:flex;flex-wrap:wrap;gap:5px;margin:-2px 0 6px;animation:kin .3s both}
.tr i{font-style:normal;font-size:11.5px;padding:4px 8px;border-radius:999px;background:var(--w2);opacity:.85;white-space:nowrap}
.typing{align-self:flex-start;display:flex;align-items:center;gap:9px;padding:9px 13px;border-radius:18px;background:var(--cin,var(--w2));font-size:13.5px}
.typing span{opacity:.7}
.chips{display:flex;flex-wrap:wrap;gap:6px;padding:6px 18px 4px}
.chips button{padding:8px 13px;border-radius:999px;font-size:13.5px;line-height:1.2;box-shadow:inset 0 0 0 1.5px var(--wl);text-align:left;transition:background .15s}
.chips button:hover{background:var(--w2)}
.inp{display:flex;gap:8px;padding:10px 14px 14px;align-items:center}
.inp input{flex:1;height:46px;border-radius:14px;border:0;padding:0 16px;background:var(--w2);font-size:15px;min-width:0}
.inp input:focus{outline:0;box-shadow:0 0 0 1.5px var(--ac)}
.inp button{width:46px;height:46px;border-radius:14px;background:var(--ac);color:var(--aci);display:grid;place-items:center;flex:none}
.inp button svg{width:19px;height:19px;fill:currentColor}
.ag{display:flex;align-items:center;gap:11px;padding:13px 18px;border-bottom:1px solid var(--wl)}
.ag .av{width:38px;height:38px;border-radius:50%;background:var(--ac);color:var(--aci);display:grid;place-items:center;font-weight:700;flex:none}
.ag b{display:block;font-size:15px;line-height:1.2}
.ag small{font-size:12.5px;opacity:.6}
.ag button{margin-left:auto;font-size:12.5px;font-weight:600;padding:7px 11px;border-radius:999px;box-shadow:inset 0 0 0 1.5px var(--wl)}
/* панель «что понял» */
.brain{background:var(--bbg,transparent)}
.bb{padding:14px 18px 16px;border-bottom:1px solid var(--wl)}
.bb:last-child{border-bottom:0}
.bb-h{display:flex;align-items:center;gap:9px;font:600 11.5px/1 var(--fb);letter-spacing:.12em;text-transform:uppercase;margin-bottom:8px}
.bb-h i{width:18px;height:18px;border-radius:50%;display:grid;place-items:center;font-style:normal;font-size:11px;box-shadow:inset 0 0 0 1.5px var(--wl);flex:none;letter-spacing:0}
.bb[data-st=wait]{opacity:.5}
.bb[data-st=run] .bb-h i{box-shadow:none;border:2px solid var(--wl);border-top-color:var(--ac);animation:sp .7s linear infinite;color:transparent}
.bb[data-st=done] .bb-h i{background:var(--ok);color:#fff;box-shadow:none}
.bb .em{font-size:13.5px;opacity:.55}
.bb .kv:last-child{border-bottom:0}
.src{display:grid;grid-template-columns:30px 1fr;gap:10px;align-items:start;padding:7px 0;font-size:13.5px;animation:kin .3s both}
.src i{width:30px;height:30px;border-radius:9px;background:var(--w2);display:grid;place-items:center;font-style:normal;font-size:14px}
.src b{display:block;font-size:14px;line-height:1.25}
.src span{opacity:.62;line-height:1.3;display:block}
.act{padding:12px 14px;border-radius:14px;background:color-mix(in srgb,var(--ok) 13%,transparent);animation:kin .3s both}
.act.h{background:color-mix(in srgb,var(--warn) 16%,transparent)}
.act b{display:block;font-size:14.5px}
.act span{font-size:13px;opacity:.72}
.cf{display:flex;align-items:center;gap:10px;font-size:12.5px;margin-top:10px}
.cf .meter{flex:1}
.cf b{min-width:38px;text-align:right}
/* как работает */
.how{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-top:clamp(28px,4vw,48px);counter-reset:h}
.how div{padding:clamp(20px,2.2vw,28px);border-radius:var(--rc);background:var(--card);box-shadow:var(--csh,none);counter-increment:h;min-width:0}
.how div::before{content:counter(h,decimal-leading-zero);display:block;font:600 13px/1 var(--fm,var(--fb));letter-spacing:.1em;color:var(--kc,var(--ac));margin-bottom:26px}
.how b{display:block;font-family:var(--fh);font-weight:var(--hw);font-size:21px;letter-spacing:var(--ht);line-height:1.15;margin-bottom:8px}
.how p{color:var(--soft);font-size:15px}
.feats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:clamp(28px,4vw,48px)}
.feat{padding:clamp(20px,2.4vw,30px);border-radius:var(--rc);background:var(--card);box-shadow:var(--csh,none);display:flex;flex-direction:column;gap:10px;min-width:0}
.feat i{width:46px;height:46px;border-radius:14px;background:var(--bg);display:grid;place-items:center;font-style:normal;font-size:22px;margin-bottom:6px}
.feat b{font-family:var(--fh);font-weight:var(--hw);font-size:21px;letter-spacing:var(--ht);line-height:1.15}
.feat p{color:var(--soft);font-size:15px}
/* контроль */
.adm{display:grid;grid-template-columns:.9fr 1.1fr;gap:clamp(24px,4vw,56px);align-items:center}
.adm>*{min-width:0}
.rules{display:grid;gap:18px;margin-top:26px;padding:0;list-style:none}
.rules li{display:grid;grid-template-columns:28px 1fr;gap:14px}
.rules li::before{content:"";width:28px;height:28px;border-radius:50%;background:var(--ac) no-repeat center/14px;background-image:var(--tick);margin-top:1px}
.rules b{display:block;font-size:17px}
.rules p{color:var(--soft);font-size:15px}
.panel{border-radius:22px;background:var(--pbg,var(--card));color:var(--pink,var(--ink));box-shadow:0 40px 80px -50px rgba(0,0,0,.45),0 0 0 1px var(--line);overflow:hidden;font-size:14px;--pl:color-mix(in srgb,currentColor 9%,transparent)}
.panel .ph{display:flex;align-items:center;gap:10px;padding:14px 18px;border-bottom:1px solid var(--pl)}
.panel .ph i{width:10px;height:10px;border-radius:50%;background:#ff5f57;box-shadow:16px 0 0 #febc2e,32px 0 0 #28c840;margin-right:40px;flex:none}
.panel .ph span{margin-left:auto;font-size:12px;opacity:.55}
.kpi{display:grid;grid-template-columns:repeat(3,1fr);border-bottom:1px solid var(--pl)}
.kpi div{padding:14px 18px;min-width:0}
.kpi div+div{border-left:1px solid var(--pl)}
.kpi b{display:block;font-size:22px;letter-spacing:-.02em;white-space:nowrap}
.kpi span{font-size:12px;opacity:.55}
.rows{max-height:340px;overflow:auto}
.rowx{display:grid;grid-template-columns:auto 1fr auto;gap:12px;align-items:center;padding:12px 18px;border-top:1px solid var(--pl)}
.rowx:first-child{border-top:0}
.rowx .d{width:36px;height:36px;border-radius:10px;background:color-mix(in srgb,currentColor 6%,transparent);display:grid;place-items:center;font-size:16px}
.rowx b{display:block;font-size:14px}
.rowx span{font-size:12.5px;opacity:.6}
.rowx em{font-style:normal;font-size:12px;font-weight:600;padding:5px 9px;border-radius:999px;background:color-mix(in srgb,var(--ac) 14%,transparent);color:var(--act,var(--ac));white-space:nowrap}
.rowx em.h{background:color-mix(in srgb,var(--warn) 18%,transparent);color:color-mix(in srgb,var(--warn) 75%,currentColor)}
.rowx.new{animation:flash 1.6s}
@keyframes flash{0%{background:color-mix(in srgb,var(--ac) 22%,transparent)}100%{background:transparent}}
.res{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border-radius:var(--rc);overflow:hidden;margin-top:clamp(28px,4vw,44px);box-shadow:0 0 0 1px var(--line)}
.res div{background:var(--bg);padding:clamp(20px,2.4vw,30px);min-width:0}
.res b{display:block;font-family:var(--fh);font-weight:var(--hw);font-size:clamp(32px,4vw,52px);letter-spacing:-.03em;line-height:1;color:var(--rcx,var(--ac))}
.res span{display:block;margin-top:10px;color:var(--soft);font-size:15px}
.ints{display:flex;flex-wrap:wrap;gap:10px;margin-top:26px}
.ints span{padding:10px 16px;border-radius:999px;background:var(--card);font-size:14px;font-weight:500;box-shadow:var(--csh,none)}
.faq details{border-top:1px solid var(--line2)}
.faq details:last-child{border-bottom:1px solid var(--line2)}
.faq summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;gap:20px;padding:20px 0;font-size:clamp(17px,1.6vw,19px);font-weight:500}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";font-size:24px;line-height:1;color:var(--mut);transition:transform .3s}
.faq details[open] summary::after{transform:rotate(45deg)}
.faq details p{padding:0 0 22px;color:var(--soft);max-width:70ch}
.cta-b{border-radius:var(--rs);background:var(--cbg,var(--ink));color:var(--cink,var(--bg));padding:clamp(28px,5vw,64px);display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.cta-b h2{max-width:18ch}
.foot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding:28px 0 40px;font-size:14px;color:var(--mut)}
.js .reveal{opacity:0;transform:translateY(18px);transition:opacity .7s,transform .7s cubic-bezier(.2,.8,.2,1)}
.js .reveal.on,.nofx .reveal{opacity:1;transform:none}
@media (max-width:1000px){
 .nav{display:none}.top .btn{margin-left:auto}
 .hg{grid-template-columns:1fr;align-items:start}
 .hs{grid-template-columns:repeat(3,1fr);gap:14px}
 .hs div{border:0!important;padding:0}
 .hs b{font-size:26px}.hs span{font-size:12.5px;line-height:1.3;display:block;margin-top:4px}
 .feats{grid-template-columns:1fr 1fr}
 .adm{grid-template-columns:1fr}
 .res{grid-template-columns:1fr 1fr}
 .ws-chat .panes{grid-template-columns:1fr;height:auto}
 .ws-chat .pane.c{height:min(600px,82vh)}
 .pane+.pane{border-left:0;border-top:1px solid var(--wl)}
}
@media (max-width:640px){
 .hero h1{font-size:clamp(36px,10.4vw,52px)}
 .hero .cta .btn{flex:1 1 100%}
 .hero-center .hs{gap:14px;grid-template-columns:repeat(3,1fr)}
 .feats{grid-template-columns:1fr}
 .ws{border-radius:18px}
 .ws-bar .dots{display:none}
 .m{max-width:88%}.m.rich{width:100%}
 .chips{padding-inline:12px;flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none}.chips::-webkit-scrollbar{display:none}.chips button{flex:none;white-space:nowrap}.chat{padding-inline:12px}.inp{padding-inline:10px}
 .ws-n{align-items:flex-start;font-size:13px}.ws-n b{margin-top:6px}
 .kpi b{font-size:18px}.kpi div{padding:12px}
 .rowx{padding-inline:12px;gap:10px}
 .cta-b .btn{width:100%}
}
@media (prefers-reduced-motion:reduce){*{animation-duration:.01ms!important;transition-duration:.01ms!important}html{scroll-behavior:auto}}
"""

JS = r"""
(function(){
'use strict';
var C=window.AICFG||{},D=C.demo||{},RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var SP=/[?&]fast/.test(location.search)?0:(RM?.25:1);
function $(s,r){return(r||document).querySelector(s)}
function $$(s,r){return[].slice.call((r||document).querySelectorAll(s))}
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function wait(ms){return new Promise(function(r){setTimeout(r,ms*SP)})}
function fmt(n){return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g,' ')}
function stream(el,text,per){var p=String(text).split(/(\s+)/),i=0;return new Promise(function(res){
 if(!SP){el.textContent=text;return res()}
 (function tick(){if(i>=p.length)return res();el.appendChild(document.createTextNode(p[i]+(p[i+1]||'')));i+=2;
  var sc=el.closest('.chat,.scroll');if(sc&&sc.dataset.follow!=='0')sc.scrollTop=sc.scrollHeight;setTimeout(tick,(per||24)*SP)})()})}
var rows=$('#rows'),k0=$('#kpi0'),cnt=0;
function log(a){if(!rows||!a)return;var r=document.createElement('div');r.className='rowx new';
 r.innerHTML='<div class="d">'+a[0]+'</div><div><b>'+esc(a[1])+'</b><span>'+esc(a[2])+' · только что</span></div><em class="'+(a[4]||'')+'">'+esc(a[3]||'Новая')+'</em>';
 rows.insertBefore(r,rows.firstChild);cnt++;if(k0)k0.textContent=+k0.dataset.base+cnt}
var AIK=window.AIK={$:$,$$:$$,esc:esc,wait:wait,fmt:fmt,stream:stream,log:log,cfg:C,parts:{},speed:SP};

if(D.type==='chat'){
 var chat=$('#chat'),inp=$('#inp'),send=$('#send'),chips=$('#chips'),S=AIK.S=Object.assign({},D.defaults||{}),busy=false,touched=false,byId={};
 (D.intents||[]).forEach(function(it){byId[it.id]=it;if(it.re)it._re=new RegExp(it.re,'i')});
 var B={f:$('#bF'),s:$('#bS'),a:$('#bA'),c:$('#bC'),cv:$('#bCv')};
 function fill(s){return String(s).replace(/\{([^{}]+)\}/g,function(m,k){return S[k]!=null?S[k]:m})}
 function st(el,v){el.parentNode.dataset.st=v}
 function conf(v){B.c.style.width=Math.round(v*100)+'%';B.cv.textContent=v?Math.round(v*100)+'%':'—';B.c.style.background=v&&v<.6?'var(--warn)':''}
 function scroll(){chat.scrollTop=chat.scrollHeight}
 function bubble(cls){var m=document.createElement('div');m.className='m '+cls;chat.appendChild(m);scroll();return m}
 function card(p){
  if(p.t==='items')return'<div class="its">'+p.items.map(function(x){return'<div class="it">'+(x.tag?'<i class="tg">'+esc(fill(x.tag))+'</i>':'')+'<b>'+esc(fill(x.n))+'</b><span>'+esc(fill(x.s))+'</span>'+
   (x.p||x.b?'<div class="itf"><strong>'+esc(fill(x.p||''))+'</strong>'+(x.b?'<button type="button" data-go="'+x.b[1]+'" data-say="'+esc(fill(x.b[2]||x.b[0]))+'">'+esc(x.b[0])+'</button>':'')+'</div>':'')+'</div>'}).join('')+'</div>';
  if(p.t==='kv')return'<div class="kvc">'+(p.h?'<h4>'+esc(fill(p.h))+'</h4>':'')+p.rows.map(function(r){return'<div class="r"><span>'+esc(r[0])+'</span><span>'+esc(fill(r[1]))+'</span></div>'}).join('')+
   (p.sum?'<div class="r sum"><span>'+esc(p.sum[0])+'</span><span>'+esc(fill(p.sum[1]))+'</span></div>':'')+'</div>';
  if(p.t==='btns')return'<div class="bts">'+p.items.map(function(b,i){return'<button type="button"'+(b[3]?' class="g"':'')+' data-go="'+b[1]+'" data-say="'+esc(fill(b[2]||b[0]))+'">'+esc(fill(b[0]))+'</button>'}).join('')+'</div>';
  if(p.html)return p.html;
  return''}
 function typing(t){var el=document.createElement('div');el.className='typing';el.innerHTML='<i class="spin"></i><span></span>';el.lastChild.textContent=t;chat.appendChild(el);scroll();
  return{el:el,set:function(x){el.lastChild.textContent=x;scroll()}}}
 function lock(v){inp.disabled=v;send.disabled=v;inp.placeholder=v?'Ассистент отвечает…':(D.placeholder||'Напишите вопрос своими словами')}
 function setChips(list){chips.innerHTML='';(list||[]).forEach(function(c){var b=document.createElement('button');b.type='button';b.textContent=fill(c[0]);b.dataset.go=c[1]||'';b.dataset.say=fill(c[2]||c[0]);chips.appendChild(b)})}
 function val(x){return typeof x==='string'&&AIK.parts[x]?AIK.parts[x](S):x}
 async function run(it,text){busy=true;lock(true);chips.innerHTML='';
  var over=AIK.hook?AIK.hook(text||'',S,it):null;if(over&&byId[over])it=byId[over];
  [B.f,B.s,B.a].forEach(function(x){x.innerHTML='';st(x,'wait')});conf(0);
  var th=it.think||[],ty=typing(th[0]||'Разбираю сообщение');
  st(B.f,'run');await wait(480);
  var F=val(it.fields)||[];for(var i=0;i<F.length;i++){B.f.insertAdjacentHTML('beforeend','<div class="kv"><span>'+esc(F[i][0])+'</span><b>'+esc(fill(F[i][1]))+'</b></div>');await wait(170)}
  st(B.f,'done');conf(it.conf||.92);
  ty.set(th[1]||'Ищу в данных компании');st(B.s,'run');await wait(520);
  var R=val(it.sources)||[];for(i=0;i<R.length;i++){B.s.insertAdjacentHTML('beforeend','<div class="src"><i>'+R[i][0]+'</i><div><b>'+esc(fill(R[i][1]))+'</b><span>'+esc(fill(R[i][2]))+'</span></div></div>');await wait(230)}
  if(!R.length)B.s.innerHTML='<p class="em">В данных компании ответа нет</p>';
  st(B.s,'done');ty.set(th[2]||'Пишу ответ');await wait(430);ty.el.remove();
  var say=[];(val(it.say)||[]).forEach(function(p){p=p&&p.t==='fn'?AIK.parts[p.f](S):p;say=say.concat(p)});
  for(i=0;i<say.length;i++){var p=say[i];if(!p)continue;
   if(typeof p==='string'){await stream(bubble('b'),fill(p))}
   else if(p.t==='note'){bubble('note').textContent=fill(p.text)}
   else{bubble('b rich').innerHTML=card(p);scroll()}
   await wait(260)}
  st(B.a,'run');await wait(320);var A=val(it.action)||['Ответ отправлен','Клиент получил ответ в чате'];
  B.a.innerHTML='<div class="act'+(A[2]?' '+A[2]:'')+'"><b>'+esc(fill(A[0]))+'</b><span>'+esc(fill(A[1]))+'</span></div>';st(B.a,'done');
  var tr=document.createElement('div');tr.className='tr';tr.innerHTML=(R.length?'<i>📚 '+esc(fill(R[0][1]))+(R.length>1?' и ещё '+(R.length-1):'')+'</i>':'')+'<i>'+(A[2]?'👤 ':'✓ ')+esc(fill(A[0]))+'</i>';chat.appendChild(tr);scroll();
  var L=val(it.log);if(L)log(L.map(function(x){return fill(x)}));
  setChips(val(it.next)||D.chips);busy=false;lock(false);scroll();setTimeout(scroll,60)}
 function match(t){var L=D.intents||[];for(var i=0;i<L.length;i++)if(L[i]._re&&L[i]._re.test(t))return L[i];return null}
 function ask(text,id){if(busy||!text)return;bubble('u').textContent=text;run((id&&byId[id])||match(text)||byId[D.fallback],text)}
 AIK.ask=ask;
 function user(text,id){touched=true;ask(text,id)}
 send.addEventListener('click',function(){var v=inp.value.trim();inp.value='';user(v)});
 inp.addEventListener('keydown',function(ev){if(ev.key==='Enter'){ev.preventDefault();send.click()}});
 inp.addEventListener('focus',function(){touched=true});
 document.addEventListener('click',function(ev){var b=ev.target.closest('[data-go]');if(b&&$('#ws').contains(b)){user(b.dataset.say||b.textContent,b.dataset.go)}});
 async function hello(){chat.innerHTML='';S=AIK.S=Object.assign({},D.defaults||{});[B.f,B.s,B.a].forEach(function(x){x.innerHTML='';st(x,'wait')});conf(0);lock(true);
  for(var i=0;i<(D.greet||[]).length;i++){await stream(bubble('b'),D.greet[i]);await wait(220)}
  setChips(D.chips);lock(false);scroll()}
 $('#again').addEventListener('click',function(){if(busy)return;touched=true;hello()});
 AIK.demo=async function(){await hello();await wait(1500);if(!touched&&D.autoplay)ask(D.autoplay[0],D.autoplay[1])};
}
var started=false;function start(){if(started)return;started=true;if(AIK.demo)AIK.demo()}
var io='IntersectionObserver'in window?new IntersectionObserver(function(es){es.forEach(function(x){if(x.isIntersecting){x.target.classList.add('on');if(x.target.id==='ws')start();io.unobserve(x.target)}})},{threshold:.12}):null;
$$('.reveal,#ws').forEach(function(el){io?io.observe(el):el.classList.add('on')});
if(!io)setTimeout(start,0);
setTimeout(start,2600);
window.__ai=1;
})();
"""

TICK = ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M3.5 8.4l3 3 6-6.6' "
        "fill='none' stroke='{c}' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E\")")

FAQ_COMMON = [
    ("Ассистент не выдумает ответ?", "Он отвечает только по вашим данным: каталогу, базе знаний, регламентам, расписанию. "
                                     "Если ответа там нет или уверенность низкая, он не угадывает, а передаёт вопрос сотруднику "
                                     "вместе с краткой сводкой диалога."),
    ("Сколько занимает внедрение?", "В первый день согласуем сценарии и границы: что ассистент делает сам, а что отдаёт людям. "
                                    "Рабочая версия на ваших данных готова за 7–10 дней, с интеграциями в учётные системы — за 2–3 недели."),
    ("Что нужно от нас?", "Материалы, по которым отвечают ваши сотрудники: прайс, каталог, инструкции, типовые ответы, и доступ к "
                          "системам, с которыми ассистент должен работать. Правила и тон согласуем с вами."),
    ("Где хранятся данные?", "На вашем сервере или в облаке в России, по вашему выбору. Диалоги и действия ассистента пишутся "
                             "в журнал, доступ к нему у тех сотрудников, которым вы его дали."),
]


def chat_html(D: dict) -> str:
    return f"""<div class="ws ws-chat reveal" id="ws"><div class="panes">
 <div class="pane c"><div class="ag"><div class="av">{e(D['agent'][0])}</div><div><b>{e(D['agent'])}</b><small>{e(D['role'])}</small></div><button type="button" id="again">↻ Заново</button></div>
  <div class="chat" id="chat" aria-live="polite"></div><div class="chips" id="chips" data-ox></div>
  <div class="inp"><input id="inp" placeholder="{e(D.get('placeholder', 'Напишите вопрос своими словами'))}" aria-label="Сообщение ассистенту" autocomplete="off"><button id="send" type="button" aria-label="Отправить"><svg viewBox="0 0 24 24"><path d="M3 20.5 21 12 3 3.5l.02 6.6L15 12 3.02 13.9z"/></svg></button></div></div>
 <div class="pane brain"><div class="pane-h">{e(D.get('brainTitle', 'Что происходит за ответом'))}</div><div class="scroll">
  <div class="bb" data-st="wait"><div class="bb-h"><i>1</i>{e(D.get('b1', 'Понял из сообщения'))}</div><div id="bF"></div><div class="cf"><span>Уверенность</span><div class="meter"><i id="bC"></i></div><b id="bCv">—</b></div></div>
  <div class="bb" data-st="wait"><div class="bb-h"><i>2</i>{e(D.get('b2', 'Где искал'))}</div><div id="bS"></div></div>
  <div class="bb" data-st="wait"><div class="bb-h"><i>3</i>{e(D.get('b3', 'Что сделал'))}</div><div id="bA"></div></div>
 </div></div>
</div></div>"""


def build(c: dict) -> str:
    d = out(c["slug"])
    write_images(d, c.get("images", {}))
    th = dict(c["theme"])
    th.setdefault("tick", TICK.format(c=th["aci"].replace("#", "%23")))
    font_css = fonts(d, c["fonts"])
    css_vars = ";".join(f"--{k}:{v}" for k, v in th.items())
    D = c["demo"]
    nav = "".join(f'<a href="#{h}">{e(t)}</a>' for t, h in [("Ассистент", "demo"), ("Как работает", "how"), ("Возможности", "feats"),
                                                            ("Контроль", "control"), ("Вопросы", "faq")])
    H = c["hero"]
    stats = "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in H["stats"])
    how = "".join(f"<div><b>{e(a)}</b><p>{e(b)}</p></div>" for a, b in c["how"])
    feats = "".join(f'<div class="feat reveal" style="transition-delay:{(i % 3) * 70}ms"><i>{a}</i><b>{e(b)}</b><p>{e(t)}</p></div>'
                    for i, (a, b, t) in enumerate(c["feats"]))
    K = c["control"]
    P = K["panel"]
    kpi = (f'<div><b id="kpi0" data-base="{P["kpi"][0][0]}">{P["kpi"][0][0]}</b><span>{e(P["kpi"][0][1])}</span></div>'
           + "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in P["kpi"][1:]))
    rows = "".join(f'<div class="rowx"><div class="d">{r[0]}</div><div><b>{e(r[1])}</b><span>{e(r[2])}</span></div>'
                   f'<em class="{r[4] if len(r) > 4 else ""}">{e(r[3])}</em></div>' for r in P["rows"])
    rules = "".join(f"<li><div><b>{e(a)}</b><p>{e(b)}</p></div></li>" for a, b in K["rules"])
    ints = "".join(f"<span>{e(x)}</span>" for x in c["ints"])
    res = "".join(f'<div class="reveal"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in c["results"])
    faq = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in c["faq"])
    ws = chat_html(D) if D["type"] == "chat" else f'<div class="ws ws-custom reveal" id="ws">{D["html"]}</div>'
    cfg = {"demo": {k: v for k, v in D.items() if k not in ("html", "js")}}
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
<script>document.documentElement.classList.add('js');setTimeout(function(){{if(!window.__ai)document.documentElement.classList.add('nofx')}},3500)</script>
<style>
{font_css}
:root{{{css_vars}}}
{CSS}
{c.get('css', '')}
</style>
</head>
<body>
<header class="top"><div class="wrap bar"><a class="logo" href="#top"><i>{c['logoIcon']}</i>{e(c['brand'])}</a><nav class="nav">{nav}</nav>
<a class="btn" href="#demo">{e(c.get('topCta', 'Попробовать'))}</a></div></header>
<main>
<section class="hero hero-{c.get('heroLayout', 'split')}" id="top"><div class="wrap hg">
 <div class="reveal"><div class="kick">{e(H['kicker'])}</div><h1>{H['h1']}</h1><p class="lead">{H['lead']}</p>
 <div class="cta"><a class="btn" href="#demo">{e(H['cta'])}</a><a class="btn ghost" href="#how">{e(H.get('cta2', 'Как это работает'))}</a></div></div>
 <div class="hs reveal">{stats}</div>
</div></section>
<section class="wsx" id="demo"><div class="wrap"><p class="ws-n reveal"><b></b>{e(D['note'])}</p>
{ws}
</div></section>
<section class="sec t0" id="how"><div class="wrap"><div class="reveal"><div class="kick">Как работает</div><h2 style="margin:14px 0 16px">{c['howTitle']}</h2>
<p class="lead">{c['howLead']}</p></div><div class="how reveal">{how}</div></div></section>
<section class="sec t0" id="feats"><div class="wrap"><div class="reveal"><div class="kick">Возможности</div><h2 style="margin-top:14px">{c['featsTitle']}</h2></div>
<div class="feats">{feats}</div></div></section>
<section class="sec t0" id="control"><div class="wrap adm">
 <div class="reveal"><div class="kick">Контроль</div><h2 style="margin:14px 0 16px">{K['title']}</h2><p class="lead">{K['lead']}</p><ul class="rules">{rules}</ul></div>
 <div class="panel reveal"><div class="ph"><i></i><b>{e(P['name'])}</b><span>сегодня</span></div><div class="kpi">{kpi}</div><div class="rows" id="rows">{rows}</div></div>
</div></section>
<section class="sec t0"><div class="wrap"><div class="reveal"><div class="kick">Результат</div><h2 style="margin-top:14px">{c['resTitle']}</h2></div>
<div class="res">{res}</div><div class="ints reveal">{ints}</div></div></section>
<section class="sec t0" id="faq"><div class="wrap" style="max-width:900px"><div class="reveal"><div class="kick">Вопросы</div><h2 style="margin:14px 0 24px">Частые вопросы</h2></div><div class="faq">{faq}</div></div></section>
<section class="sec t0"><div class="wrap"><div class="cta-b reveal"><h2>{c['ctaTitle']}</h2><a class="btn" href="#demo">{e(c.get('ctaBtn', 'Попробовать ассистента'))}</a></div></div></section>
</main>
<footer class="wrap foot"><span>© 2026 {e(c['brand'])}</span><span>Ассистент разработан YSD DEV</span></footer>
<script>window.AICFG={jdump(cfg)};</script>
<script>{JS}</script>
{('<script>' + D['js'] + '</script>') if D.get('js') else ''}
</body>
</html>
"""
    save(d, page)
    return d
