"""«Эхо» — ИИ-разбор отзывов: тональность, темы, главные проблемы и черновики ответов. Разбор идёт правилами прямо на странице."""
from ..ai import FAQ_COMMON
from ._t import theme

HTML = """<div class="ws-bar"><i class="dots"></i><b>Эхо · отзывы о доставке рационов «Ложка»</b><span id="rvSt">12 новых отзывов</span></div>
<div class="panes rv">
 <div class="pane"><div class="pane-h">Лента отзывов<span id="rvF"></span></div>
  <form class="rv-add" id="rvAdd"><textarea id="rvT" rows="2" placeholder="Напишите свой отзыв — разберу его так же. Например: «Курьер опоздал на час, зато еда вкусная»" aria-label="Свой отзыв"></textarea><button class="btn-s" type="submit">Разобрать</button></form>
  <div class="scroll" id="rvL"></div></div>
 <div class="pane"><div class="pane-h">Сводка<span id="rvN"></span></div><div class="scroll rv-s">
  <div class="rv-b"><h5>Тональность</h5><div class="rv-bar" id="rvBar"><i class="p"></i><i class="u"></i><i class="n"></i></div><div class="rv-lg" id="rvLg"></div></div>
  <div class="rv-b"><h5>Темы <small>нажмите, чтобы отфильтровать ленту</small></h5><div id="rvTp"></div></div>
  <div class="rv-b"><h5>Что чинить первым</h5><div id="rvFix"><p class="em">Появится после разбора</p></div></div>
 </div></div>
</div>"""

CSS = """
.panes.rv{grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);height:min(700px,84vh)}
.rv-add{display:flex;gap:8px;padding:0 16px 12px;align-items:stretch;border-bottom:1px solid var(--wl)}
.rv-add textarea{flex:1;min-width:0;border:0;border-radius:14px;background:var(--w2);padding:10px 14px;font-size:14px;line-height:1.4;resize:none}
.rv-add textarea:focus{outline:2px solid var(--ac);outline-offset:1px}
#rvL{padding:12px 16px 16px}
.rw{padding:14px;border-radius:18px;background:var(--w2);margin-bottom:8px;font-size:14.5px;line-height:1.45;transition:opacity .3s}
.rw.new{animation:flash 1.6s}
.rw.dim{display:none}
.rw-h{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:6px;font-size:13px}
.rw-h b{font-size:14px}
.rw-h .st{letter-spacing:1px;color:#f5a400}
.rw-h small{opacity:.55;margin-left:auto}
.rw-g{display:flex;flex-wrap:wrap;gap:5px;margin-top:9px;align-items:center}
.rw-g i{font-style:normal;font-size:12px;line-height:1;padding:5px 8px;border-radius:999px;background:var(--wbg,#fff);white-space:nowrap}
.rw-g i.n{background:color-mix(in srgb,var(--bad) 14%,var(--wbg,#fff))}.rw-g i.p{background:color-mix(in srgb,var(--ok) 16%,var(--wbg,#fff))}
.rw-g button{margin-left:auto;font-size:12.5px;font-weight:600;padding:6px 11px;border-radius:999px;box-shadow:inset 0 0 0 1.5px var(--wl)}
.rw-a{margin-top:10px;padding:11px 13px;border-radius:14px;background:var(--wbg,#fff);font-size:14px;white-space:pre-line;box-shadow:inset 3px 0 0 var(--ac)}
.rw mark{background:color-mix(in srgb,var(--bad) 16%,transparent);color:inherit;border-radius:3px;padding:0 1px}
.rw mark.p{background:color-mix(in srgb,var(--ok) 18%,transparent)}
.rv-s{padding:2px 18px 18px}
.rv-b{padding:12px 0 16px;border-bottom:1px solid var(--wl)}
.rv-b:last-child{border-bottom:0}
.rv-b h5{margin:0 0 10px;font:600 11.5px/1 var(--fb);letter-spacing:.12em;text-transform:uppercase;opacity:.62}
.rv-b h5 small{text-transform:none;letter-spacing:0;font-weight:400;margin-left:6px}
.rv-bar{display:flex;height:14px;border-radius:7px;overflow:hidden;background:var(--w2)}
.rv-bar i{display:block;width:0;transition:width .6s cubic-bezier(.2,.8,.2,1)}
.rv-bar .p{background:var(--ok)}.rv-bar .u{background:color-mix(in srgb,currentColor 22%,transparent)}.rv-bar .n{background:var(--bad)}
.rv-lg{display:flex;gap:14px;flex-wrap:wrap;margin-top:8px;font-size:13px}
.rv-lg b{font-weight:600}
.tp{display:grid;grid-template-columns:92px 1fr auto;gap:10px;align-items:center;width:100%;padding:7px 8px;margin:0 -8px;border-radius:10px;font-size:14px;text-align:left}
.tp:hover,.tp.on{background:var(--w2)}.tp.on{box-shadow:inset 0 0 0 1.5px var(--ac)}
.tp-b{display:flex;height:10px;border-radius:5px;overflow:hidden;background:var(--w2)}
.tp-b i{display:block;transition:width .6s cubic-bezier(.2,.8,.2,1)}.tp-b .n{background:var(--bad)}.tp-b .p{background:var(--ok)}
.tp small{font-size:12.5px;opacity:.65;white-space:nowrap;min-width:54px;text-align:right}
.fx{display:grid;grid-template-columns:26px 1fr;gap:10px;padding:8px 0;font-size:14px;line-height:1.4;animation:kin .3s both}
.fx>b{width:26px;height:26px;border-radius:50%;background:var(--ac);color:var(--aci);display:grid;place-items:center;font-size:13px}
.fx strong{display:block}
.fx span{opacity:.68;font-size:13px}
@media (max-width:1000px){.panes.rv{grid-template-columns:1fr;height:auto}#rvL{max-height:520px}.rv-s{overflow:visible}}
@media (max-width:640px){.rv-add{flex-direction:column}.tp{grid-template-columns:84px 1fr auto}}
"""

JS = r"""
(function(){var K=AIK,$=K.$,esc=K.esc,
TP=[{k:'Доставка',re:/доставк|курьер|опозда|привез|привоз|вовремя|ждал|ждать|задерж|приехал/i,fix:'Курьеры опаздывают',do:'проверьте маршруты и окна доставки на вечерние часы'},
 {k:'Вкус',re:/вкус|пресн|сол[её]н|свеж|испорч|кисл|блюд|еда |еду |меню|пережар|сыр[оа]/i,fix:'Жалобы на вкус и свежесть',do:'проверьте блюда, которые называют в отзывах, и сроки хранения'},
 {k:'Порции',re:/порци|голодн|сыт|объ[её]м|грамм|наеда|наел|мало еды/i,fix:'Порции кажутся маленькими',do:'покажите граммовку в карточке рациона или добавьте увеличенную порцию'},
 {k:'Упаковка',re:/упаков|контейнер|протек|помят|пролил|крышк|пакет|разлил/i,fix:'Упаковка протекает и мнётся',do:'смените контейнеры для супов и соусов'},
 {k:'Поддержка',re:/поддержк|оператор|чат[еау ]|ответил|не ответ|менеджер|дозвон|игнор|компенс|вернули|извин/i,fix:'Поддержка отвечает медленно',do:'поставьте срок первого ответа и автоответ вне смены'},
 {k:'Цена',re:/цен[аыуе]|дорог|д[её]шев|стоит|стоимост|скидк|подорож|промокод/i,fix:'Цена кажется высокой',do:'объясните состав цены или дайте скидку на длинную подписку'}],
NEG=/опозда\S*|задерж\S*|холодн\S*|остыв\S*|остыл\S*|пресн\S*|несвеж\S*|испорч\S*|протек\S*|помят\S*|пролил\S*|разлил\S*|голодн\S*|дорог\S*|подорож\S*|не ответ\S*|игнор\S*|хам\S*|груб\S*|ужас\S*|плох\S*|разочар\S*|невкус\S*|не вкус\S*|не привез\S*|перепут\S*|забыл\S*|волос\S*|кисл\S*|долго|не дозвон\S*|никто не\S*|не понрав\S*|не совет\S*|верните|маленьк\S*|мало |хотелось бы|кусает\S*|не наел\S*|только через|пережар\S*|сыр(?:ое|ая|ой)|отврат\S*|не наеда\S*|больше не\S*|отпис\S*/gi,
POS=/вкусн\S*|свеж\S*|вовремя|быстр\S*|вежлив\S*|удобн\S*|сытн\S*|нравит\S*|понрав\S*|отличн\S*|спасибо|рекоменд\S*|супер|класс\S*|люблю|довол\S*|аккуратн\S*|выруча\S*|хорош\S*|минута в минуту|наеда\S*|разнообразн\S*|извинил\S*|вернули/gi,
R=[['Ирина','Карты',5,'Заказываю третий месяц. Курьер приезжает минута в минуту, еда свежая, меню разнообразное. Спасибо, выручаете!'],
 ['Олег','Сайт',2,'Курьер опоздал на полтора часа, обед приехал холодный. В поддержку писал дважды, никто не ответил.'],
 ['Наталья','Маркетплейс',4,'Вкусно и удобно, но порции маленькие: к вечеру уже голодная. За такую цену хотелось бы побольше.'],
 ['Дмитрий','Карты',1,'Суп протек на весь пакет, контейнер помят. Второй раз за неделю. Верните деньги.'],
 ['Алина','Соцсети',5,'Очень вкусно, особенно завтраки. Упаковка аккуратная, всё подписано по дням.'],
 ['Виктор','Сайт',3,'Еда нормальная, но подорожало на 15% за месяц. Раньше цена была честнее.'],
 ['Светлана','Маркетплейс',2,'Рыба была пресная и как будто несвежая. Оператор в чате ответил только через день.'],
 ['Павел','Карты',5,'Сытно, хватает на весь день. Доставка всегда вовремя, курьеры вежливые.'],
 ['Екатерина','Соцсети',2,'Опять опоздали с доставкой, ждала до десяти вечера. Больше не закажу.'],
 ['Руслан','Сайт',4,'Меню хорошее, вкусно. Один раз перепутали рацион, но быстро извинились и вернули деньги за день.'],
 ['Марина','Маркетплейс',1,'Курица пережаренная, гарнир холодный. Порция маленькая, не наелась. Дорого за такое.'],
 ['Антон','Карты',4,'Удобно, что не надо готовить. Вкусно. Крышка у соуса иногда протекает, но в целом доволен.']],
A=[],flt=null,busy=false;
function an(text,stars){var S=text.split(/[.!?…;,:]+\s+|\s+(?:но|зато|хотя|а)\s+/i),tp={},ng=0,ps=0,marks=[];
 S.forEach(function(s){var n=s.match(NEG)||[],rest=s.replace(NEG,' '),p=rest.match(POS)||[];ng+=n.length;ps+=p.length;n.forEach(function(w){marks.push([w.trim(),0])});p.forEach(function(w){marks.push([w.trim(),1])});
  TP.forEach(function(t){if(t.re.test(s)){var v=n.length>p.length?-1:p.length>n.length?1:0;if(!tp[t.k])tp[t.k]=[0,0,0];tp[t.k][v+1]++}})});
 var sent=stars?(stars>=4?1:stars<=2?-1:0):(ng>ps?-1:ps>ng?1:0);
 var T=Object.keys(tp).map(function(k){var a=tp[k];return{k:k,v:a[0]>a[2]?-1:a[2]>a[0]?1:0}});
 return{sent:sent,T:T,marks:marks}}
function hl(text,marks){var h=esc(text);marks.sort(function(a,b){return b[0].length-a[0].length}).forEach(function(m){if(m[0].length<3)return;var w=esc(m[0]);h=h.split(w).join('\u0001'+(m[1]?'p':'n')+'\u0002'+w+'\u0003')});
 return h.replace(/\u0001p\u0002/g,'<mark class="p">').replace(/\u0001n\u0002/g,'<mark>').replace(/\u0003/g,'</mark>')}
function reply(r){var neg=r.a.T.filter(function(t){return t.v<0}).map(function(t){return t.k}),nm=r.name;
 if(r.a.sent>0&&!neg.length)return nm+', спасибо за тёплые слова! Передадим команде кухни и курьерам. Если захочется попробовать новое меню, со следующей недели в рационе появятся три новых завтрака.';
 var L=[nm+', здравствуйте! '+(r.a.sent>0?'Спасибо за отзыв и за то, что рассказали о недочёте.':'Простите, что так вышло: вы платили за другое качество.')];
 if(neg.indexOf('Доставка')>=0)L.push('Опоздание курьера — наша ошибка. Мы уже разбираем маршрут в вашем районе и вернём стоимость доставки за этот день.');
 if(neg.indexOf('Вкус')>=0)L.push('Замечание по блюду передали шеф-повару сегодня же. Этот день рациона заменим бесплатно.');
 if(neg.indexOf('Упаковка')>=0)L.push('За протёкший контейнер вернём деньги за блюдо. Для супов и соусов переходим на крышки с защёлкой.');
 if(neg.indexOf('Порции')>=0)L.push('Для тех, кому не хватает, есть рацион на 2 000 ккал: переведём вас на него на неделю без доплаты, чтобы вы сравнили.');
 if(neg.indexOf('Поддержка')>=0)L.push('Отдельно простите за молчание поддержки: так быть не должно, разберёмся со сменой.');
 if(neg.indexOf('Цена')>=0)L.push('Цена выросла из-за продуктов, но при оплате на месяц действует прежняя стоимость. Пришлём вам промокод.');
 if(L.length===1)L.push('Напишите, пожалуйста, что именно пошло не так, — исправим.');
 L.push('Напишите номер заказа в личные сообщения, и мы всё оформим сегодня.');return L.join(' ')}
function card(r,top){var el=r.el=document.createElement('div');el.className='rw';
 el.innerHTML='<div class="rw-h"><b>'+esc(r.name)+'</b>'+(r.stars?'<span class="st">'+'★★★★★'.slice(0,r.stars)+'<span style="opacity:.25">'+'★★★★★'.slice(r.stars)+'</span></span>':'')+'<small>'+esc(r.src)+'</small></div><div class="rw-t">'+esc(r.text)+'</div><div class="rw-g"></div>';
 var L=$('#rvL');if(top)L.insertBefore(el,L.firstChild);else L.appendChild(el);return el}
function mark(r){r.a=an(r.text,r.stars);r.el.querySelector('.rw-t').innerHTML=hl(r.text,r.a.marks.slice());
 r.el.querySelector('.rw-g').innerHTML='<span class="tag '+(r.a.sent>0?'ok':r.a.sent<0?'bad':'')+'">'+(r.a.sent>0?'Позитивный':r.a.sent<0?'Негативный':'Нейтральный')+'</span>'+r.a.T.map(function(t){return'<i class="'+(t.v<0?'n':t.v>0?'p':'')+'">'+(t.v<0?'− ':t.v>0?'+ ':'')+esc(t.k)+'</i>'}).join('')+'<button type="button" data-re>Ответить</button>';A.push(r)}
function sum(){var p=0,u=0,n=0,M={};TP.forEach(function(t){M[t.k]=[0,0,[]]});
 A.forEach(function(r){if(r.a.sent>0)p++;else if(r.a.sent<0)n++;else u++;r.a.T.forEach(function(t){if(t.v<0){M[t.k][0]++;M[t.k][2].push(r)}else if(t.v>0)M[t.k][1]++})});
 var tot=A.length||1,b=$('#rvBar').children;b[0].style.width=p/tot*100+'%';b[1].style.width=u/tot*100+'%';b[2].style.width=n/tot*100+'%';
 $('#rvLg').innerHTML='<span><b>'+p+'</b> позитивных</span><span><b>'+u+'</b> нейтральных</span><span><b>'+n+'</b> негативных</span>';$('#rvN').textContent='разобрано: '+A.length;
 var mx=1;TP.forEach(function(t){mx=Math.max(mx,M[t.k][0]+M[t.k][1])});
 $('#rvTp').innerHTML=TP.map(function(t){var a=M[t.k];return'<button type="button" class="tp'+(flt===t.k?' on':'')+'" data-tp="'+t.k+'"><span>'+t.k+'</span><span class="tp-b"><i class="n" style="width:'+a[0]/mx*100+'%"></i><i class="p" style="width:'+a[1]/mx*100+'%"></i></span><small>−'+a[0]+' / +'+a[1]+'</small></button>'}).join('');
 var top=TP.map(function(t){return{t:t,n:M[t.k][0],q:M[t.k][2]}}).filter(function(x){return x.n>0}).sort(function(a,b){return b.n-a.n}).slice(0,3);
 $('#rvFix').innerHTML=top.length?top.map(function(x,i){return'<div class="fx"><b>'+(i+1)+'</b><div><strong>'+x.t.fix+' · '+x.n+' '+(x.n===1?'отзыв':x.n<5?'отзыва':'отзывов')+'</strong><span>Что сделать: '+x.t.do+'. Пишут: '+x.q.slice(0,3).map(function(r){return esc(r.name)}).join(', ')+'</span></div></div>'}).join(''):'<p class="em">Жалоб по темам нет</p>';return[p,u,n,top]}
function filt(){A.concat(Q).forEach(function(r){if(r.el)r.el.classList.toggle('dim',!!flt&&!(r.a&&r.a.T.some(function(t){return t.k===flt})))});$('#rvF').textContent=flt?'тема: '+flt+' · сбросить ✕':''}
var Q=R.map(function(x){return{name:x[0],src:x[1],stars:x[2],text:x[3]}});Q.forEach(function(r){card(r)});sum();
$('#ws').addEventListener('click',function(ev){var t=ev.target,b=t.closest('.tp');if(b){flt=flt===b.dataset.tp?null:b.dataset.tp;sum();filt();return}
 if(t.id==='rvF'||t.closest('#rvF')){flt=null;sum();filt();return}
 if(t.hasAttribute('data-re')){var el=t.closest('.rw'),r=A.filter(function(x){return x.el===el})[0];if(!r||r.done)return;r.done=1;t.remove();var a=document.createElement('div');a.className='rw-a';el.appendChild(a);
  K.stream(a,reply(r),14);K.log(['💬','Ответ на отзыв: '+r.name,(r.a.sent<0?'негативный':r.a.sent>0?'позитивный':'нейтральный')+' · '+(r.a.T.map(function(x){return x.k.toLowerCase()}).join(', ')||'без темы'),'Черновик'])}});
$('#rvAdd').addEventListener('submit',function(ev){ev.preventDefault();var v=$('#rvT').value.trim();if(v.length<8){$('#rvT').focus();return}$('#rvT').value='';
 var r={name:'Ваш отзыв',src:'только что',stars:0,text:v};Q.push(r);card(r,true).classList.add('new');mark(r);sum();filt();$('#rvL').scrollTop=0;$('#rvSt').textContent='разобрано '+A.length+' отзывов';
 K.log(['🗣','Новый отзыв разобран',(r.a.sent<0?'негативный':r.a.sent>0?'позитивный':'нейтральный')+' · '+(r.a.T.map(function(x){return x.k.toLowerCase()}).join(', ')||'тема не определена'),'Разобран'])});
$('#rvT').addEventListener('keydown',function(ev){if(ev.key==='Enter'&&!ev.shiftKey){ev.preventDefault();$('#rvAdd').requestSubmit()}});
K.demo=async function(){if(busy)return;busy=true;var L=$('#rvL');for(var i=0;i<R.length;i++){var r=Q[i];$('#rvSt').textContent='читаю отзыв '+(i+1)+' из '+R.length;if(K.speed)L.scrollTop=Math.max(0,r.el.offsetTop-L.offsetTop-150);mark(r);sum();await K.wait(360)}
 var s=sum();L.scrollTop=0;$('#rvSt').textContent='разобрано '+A.length+' отзывов';K.log(['📊','Разбор отзывов за неделю','позитивных '+s[0]+' · негативных '+s[2]+(s[3][0]?' · главная проблема: '+s[3][0].t.k.toLowerCase():''),'Сводка'])};
})();
"""


def cfg() -> dict:
    return {
        "slug": "ai/reviews", "brand": "Эхо", "logoIcon": "Э", "heroLayout": "center",
        "title": "Эхо — ИИ-разбор отзывов: тональность, темы и ответы клиентам",
        "desc": "ИИ-ассистент читает отзывы со всех площадок, определяет тональность и темы, показывает, что чинить первым, "
                "и готовит ответ на каждый отзыв.",
        "theme": theme(bg="#fff3ec", ink="#2a0f1e", soft="#6b4a58", mut="#a08390", line="#f3ddd2", line2="#e2c3b6",
                       card="#ffffff", ac="#ff5533", aci="#ffffff", fh='"Unbounded",sans-serif', fb='"Rubik",sans-serif',
                       hw="600", ht="-.04em", rb="999px", rc="26px", rs="36px", rw="30px", wbg="#ffffff",
                       cbg="#2a0f1e", cink="#fff3ec", wsh="0 50px 110px -60px rgba(255,85,51,.55),0 0 0 1px #f3ddd2",
                       csh="0 0 0 1px #f3ddd2", ok="#1ea672", bad="#e5383b"),
        "fonts": [("Unbounded", "unbounded", [500, 600], "normal"), ("Rubik", "rubik", [400, 500, 600], "normal")],
        "css": CSS + ".hero h1{font-size:clamp(34px,5.4vw,78px);line-height:1.04;max-width:17ch;margin-inline:auto}"
                     "h2{font-size:clamp(26px,3.6vw,46px);line-height:1.1}.how b,.feat b{font-size:18px;letter-spacing:-.03em;line-height:1.25}"
                     ".hs b,.res b{font-size:clamp(26px,3vw,40px)}.logo{font-size:19px}.logo i{border-radius:50%}"
                     ".feat i{background:#fff3ec;border-radius:50%}.cta-b .btn{background:#ff5533}"
                     ".hero{background:radial-gradient(50% 60% at 50% 0,rgba(255,85,51,.18),transparent 70%)}.kick{letter-spacing:.1em}",
        "hero": {"kicker": "ИИ-разбор отзывов", "h1": "Тысяча отзывов — <em>три вещи, которые надо починить</em>",
                 "lead": "Эхо читает отзывы с карт, маркетплейсов, сайта и соцсетей, раскладывает их по темам и тональности, показывает "
                         "главные проблемы недели и пишет черновик ответа каждому клиенту.",
                 "cta": "Разобрать отзывы",
                 "stats": [("100%", "отзывов прочитано"), ("15 мин", "до ответа на негатив"), ("6", "тем под контролем")]},
        "demo": {"type": "custom", "html": HTML, "js": JS,
                 "note": "Разбор работает: нажмите на тему, чтобы отфильтровать ленту, попросите ответ на отзыв или напишите свой отзыв в поле"},
        "howTitle": "Как Эхо слышит клиентов",
        "howLead": "Отзывы перестают быть лентой, которую некогда читать, и становятся списком дел с цифрами.",
        "how": [("Собирает отзывы", "С карт, маркетплейсов, сайта, соцсетей и из чатов поддержки — в одну ленту без дублей."),
                ("Разбирает каждый", "Определяет тональность и темы. В одном отзыве может быть похвала за вкус и жалоба на курьера — учтёт обе."),
                ("Считает и сравнивает", "Показывает, о чём пишут чаще всего и что выросло за неделю. Проблемы ранжирует по числу жалоб."),
                ("Готовит ответы", "Пишет черновик ответа по вашим правилам: извинение, решение, следующий шаг. Отправляет сотрудник.")],
        "featsTitle": "Что видно в Эхо",
        "feats": [("🎭", "Тональность", "Позитив, нейтрально, негатив — по каждому отзыву и по каждой теме внутри него."),
                  ("🏷", "Темы", "Доставка, вкус, порции, упаковка, поддержка, цена. Темы настраиваются под ваш бизнес."),
                  ("🛠", "Что чинить первым", "Три главные проблемы с числом жалоб, примерами и подсказкой, что сделать."),
                  ("💬", "Черновики ответов", "Ответ учитывает, на что именно жалуется клиент, и предлагает решение по вашим правилам."),
                  ("🚨", "Сигналы", "Резкий рост жалоб на одну тему или отзыв с одной звездой сразу уходит ответственному."),
                  ("📈", "Динамика", "Как менялись темы и оценка после ваших изменений: стало лучше или нет.")],
        "control": {"title": "Отвечает человек, Эхо готовит",
                    "lead": "Ассистент не публикует ответы сам и ничего не обещает клиенту без ваших правил.",
                    "rules": [("Не публикует без согласия", "Каждый ответ — черновик. Сотрудник читает, правит и отправляет."),
                              ("Не обещает лишнего", "Компенсации и замены предлагает только те, что записаны в ваших правилах."),
                              ("Не прячет негатив", "Плохие отзывы не фильтруются и не занижаются: они в сводке первыми."),
                              ("Показывает основание", "В каждом отзыве подсвечены слова, по которым сделан вывод.")],
                    "panel": {"name": "Эхо · журнал отзывов",
                              "kpi": [(58, "отзывов сегодня"), ("21", "ответ отправлен"), ("15 мин", "до ответа на негатив")],
                              "rows": [("🚨", "Сигнал: жалобы на упаковку", "5 отзывов за день вместо одного", "Сигнал", "h"),
                                       ("💬", "Ответ на отзыв: Тимофей", "негативный · доставка, поддержка", "Отправлен"),
                                       ("📊", "Сводка за неделю", "позитивных 212 · негативных 47", "Сводка")]}},
        "resTitle": "Что получает бизнес",
        "results": [("100%", "отзывов разобрано, а не выборка"), ("15 мин", "до ответа на негативный отзыв"),
                    ("3", "главные проблемы недели с цифрами"), ("−60%", "времени на чтение и отчёты")],
        "ints": ["Яндекс Карты", "2ГИС", "Ozon", "Wildberries", "ВКонтакте", "Telegram", "Сайт", "Чаты поддержки"],
        "faq": [("Эхо понимает сарказм и смешанные отзывы?", "Смешанные — да: в одном отзыве отдельно оцениваются доставка, вкус и цена. "
                                                             "Сарказм и неочевидные случаи помечаются для проверки человеком."),
                ("Можно свои темы?", "Да. Темы и признаки, по которым они определяются, настраиваются под ваш продукт, "
                                     "а новые темы ассистент предлагает сам, когда видит повторяющиеся слова.")] + FAQ_COMMON,
        "ctaTitle": "Узнайте, о чём на самом деле пишут клиенты", "ctaBtn": "Открыть разбор",
    }
