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
.tgh b{display:block;font-size:15px;line-height:1.2}
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
.restart{position:absolute;right:16px;top:60px;z-index:6;font-size:12px;padding:6px 10px;border-radius:999px;background:rgba(0,0,0,.35);color:#fff;backdrop-filter:blur(8px)}
.stage{position:relative;display:grid;place-items:center;padding:10px 0}
.stage::before{content:"";position:absolute;inset:6% 4%;border-radius:50%;background:radial-gradient(closest-side,var(--glow,color-mix(in srgb,var(--ac) 34%,transparent)),transparent 72%);filter:blur(30px);z-index:0}
.stage .phone{z-index:1}
.chip{position:absolute;z-index:2;display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:16px;background:var(--chipbg,var(--card));color:var(--ink);box-shadow:0 18px 40px -22px rgba(0,0,0,.5),0 0 0 1px var(--line);font-size:13px;line-height:1.25;max-width:210px;animation:floaty 6s ease-in-out infinite}
.chip i{font-style:normal;font-size:20px}
.chip b{display:block;font-size:13.5px}
.chip span{color:var(--mut)}
.chip.c1{left:-4%;top:16%}.chip.c2{right:-6%;bottom:18%;animation-delay:-3s}
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
@media (max-width:560px){.feats{grid-template-columns:1fr}.hero .cta .btn{flex:1}.kpi b{font-size:18px}}
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
async function go(id){var n=N[id];if(!n)return;busy=true;
 if(n.set)for(var k in n.set)V[k]=n.set[k];
 if(n.calc)V=Object.assign(V,(new Function('V','F',n.calc))(V,F)||{});
 for(var i=0;i<(n.say||[]).length;i++){var t=typing();await wait(Math.min(1400,420+String(n.say[i].t||n.say[i]||'').length*9));t.remove();bot(n.say[i]);await wait(160)}
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
    th = c["theme"]
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
    flow = ""
    if c.get("flow"):
        flow = ('<section class="sec" style="padding-top:0"><div class="wrap"><div class="reveal"><div class="kick">Сценарий</div>'
                f'<h2 style="margin-top:14px">{c.get("flowTitle", "Путь клиента в боте")}</h2></div><div class="flow reveal">'
                + "".join(f"<div><b>{e(a)}</b><span>{e(b)}</span></div>" for a, b in c["flow"]) + "</div></div></section>")
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
<body>
<header class="top"><div class="wrap bar"><a class="logo" href="#top"><i>{c['logoIcon']}</i>{e(c['brand'])}</a><nav class="nav">{nav}</nav>
<a class="btn" href="#demo">{e(c.get('topCta', 'Открыть бота'))}</a></div></header>
<main>
<section class="hero" id="top"><div class="wrap g">
 <div class="reveal"><div class="kick">{e(H['kicker'])}</div><h1>{H['h1']}</h1><p class="lead">{H['lead']}</p>
 <div class="cta"><a class="btn" href="#demo">{e(H['cta'])}</a><a class="btn ghost" href="#admin">{e(H.get('cta2', 'Что видит администратор'))}</a></div>
 <div class="stats">{stats}</div>
 <p class="note"><b></b>Бот в телефоне работает: нажимайте кнопки или пишите сами</p></div>
 <div id="demo" class="stage">{chips}<div class="phone" id="phoneBox"><div class="scr">
  <div class="tgh"><span class="back">‹</span><div class="av">{c['avatar']}</div><div><b>{e(c['botName'])}</b><small>бот</small></div></div>
  <button class="restart" id="restart" type="button">↻ Заново</button>
  <div class="chat" id="chat" aria-live="polite"></div>
  <div class="inp"><input id="inp" placeholder="Выберите кнопку выше" disabled aria-label="Сообщение боту"><button id="send" type="button" aria-label="Отправить"><svg viewBox="0 0 24 24"><path d="M3 20.5 21 12 3 3.5l.02 6.6L15 12 3.02 13.9z"/></svg></button></div>
 </div></div></div>
</div></section>
{flow}<section class="sec" id="feats" style="padding-top:0"><div class="wrap"><div class="reveal"><div class="kick">Возможности</div><h2 style="margin-top:14px">{c['featsTitle']}</h2></div>
<div class="feats">{feats}</div></div></section>
<section class="sec" id="admin" style="padding-top:0"><div class="wrap adm">
 <div class="reveal"><div class="kick">Для команды</div><h2 style="margin:14px 0 16px">{A['title']}</h2><p class="lead">{A['lead']}</p><ol class="steps ol">{steps}</ol></div>
 <div class="panel reveal"><div class="ph"><i></i><b>{e(A['name'])}</b><span>онлайн</span></div><div class="kpi">{kpi}</div><div class="rows" id="rows">{rows}</div></div>
</div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="reveal"><div class="kick">Результат</div><h2 style="margin-top:14px">{c['resTitle']}</h2></div>
<div class="res">{res}</div><div class="ints reveal">{ints}</div></div></section>
<section class="sec" id="faq" style="padding-top:0"><div class="wrap" style="max-width:900px"><div class="reveal"><div class="kick">Вопросы</div><h2 style="margin:14px 0 24px">Частые вопросы</h2></div><div class="faq">{faq}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap"><div class="cta-b reveal"><h2>{c['ctaTitle']}</h2><a class="btn" href="#demo">{e(c.get('ctaBtn', 'Попробовать бота'))}</a></div></div></section>
</main>
<footer class="wrap foot"><span>© 2026 {e(c['brand'])}</span><span>Бот разработан YSD DEV</span></footer>
<script>window.BOTCFG={jdump(cfg)};</script>
<script>{JS}</script>
</body>
</html>
"""
    save(d, page)
    return d
