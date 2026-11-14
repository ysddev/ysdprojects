"""«Параграф» — ИИ-юрист: разбор договора по пунктам, риски с объяснением, готовые правки и протокол разногласий."""
from ..ai import FAQ_COMMON
from ._t import theme

HTML = """<div class="ws-bar"><i class="dots"></i><b>Параграф · проверка договора</b><span id="lgSt">готов к проверке</span></div>
<div class="lg-tabs" data-ox><button type="button" data-doc="supply" class="on">Договор поставки</button><button type="button" data-doc="rent">Договор аренды офиса</button><button type="button" data-doc="own">Свой текст</button></div>
<div class="panes lg">
 <div class="pane"><div class="pane-h"><b id="lgName"></b><span id="lgSide"></span></div>
  <div class="scroll" id="lgDoc"></div></div>
 <div class="pane"><div class="pane-h">Заключение<span id="lgCnt"></span></div>
  <div class="lg-sum"><div class="lg-sc"><b id="lgScore">—</b><span id="lgLvl">риск не оценён</span></div><div class="meter"><i id="lgBar"></i></div>
   <button type="button" class="btn-s g" id="lgDl" disabled>Скачать протокол разногласий</button></div>
  <div class="scroll" id="lgList"></div></div>
</div>"""

CSS = """
.lg-tabs{display:flex;gap:0;border-bottom:1px solid var(--wl);overflow-x:auto;scrollbar-width:none}
.lg-tabs button{padding:13px 18px;font-size:14px;font-weight:500;white-space:nowrap;border-right:1px solid var(--wl);opacity:.6}
.lg-tabs button.on{opacity:1;box-shadow:inset 0 -2px 0 var(--ac)}
.panes.lg{grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);height:min(660px,80vh)}
#lgDoc{padding:8px 26px 26px;font-family:var(--fh);font-size:16px;line-height:1.55}
#lgDoc h4{font:600 19px/1.25 var(--fh);margin:14px 0 4px;text-align:center}
#lgDoc .sub{text-align:center;font-size:14px;opacity:.6;margin-bottom:14px}
.cl{margin:0;padding:7px 10px;border-left:3px solid transparent;border-radius:0 4px 4px 0;transition:background .3s,border-color .3s;scroll-margin:60px}
.cl b{font-weight:600;margin-right:4px}
.cl.scan{background:color-mix(in srgb,var(--ac) 8%,transparent)}
.cl.s2{background:color-mix(in srgb,var(--bad) 10%,transparent);border-left-color:var(--bad)}
.cl.s1{background:color-mix(in srgb,var(--warn) 13%,transparent);border-left-color:var(--warn)}
.cl.okd{background:color-mix(in srgb,var(--ok) 9%,transparent);border-left-color:var(--ok)}
.cl.fl{animation:lgf 1.2s}
@keyframes lgf{30%{box-shadow:0 0 0 3px var(--ac)}}
.cl del{opacity:.5}.cl ins{text-decoration:none;background:color-mix(in srgb,var(--ok) 18%,transparent);padding:1px 2px}
.lg-sum{padding:4px 18px 14px;display:grid;gap:10px;border-bottom:1px solid var(--wl)}
.lg-sc{display:flex;align-items:baseline;gap:12px}
.lg-sc b{font:600 40px/1 var(--fh);letter-spacing:-.02em}
.lg-sc span{font-size:14px;opacity:.7}
#lgList{padding:12px 18px 18px;display:grid;gap:10px;align-content:start}
.fd{padding:14px;border:1px solid var(--wl);border-radius:4px;display:grid;gap:8px;animation:kin .35s both;font-size:14px;line-height:1.45}
.fd-h{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.fd-h b{font-size:15px}
.fd .fx{padding:9px 11px;background:var(--w2);border-radius:4px;font-family:var(--fh);font-size:14.5px}
.fd .fx span{display:block;font:600 11px/1 var(--fb);letter-spacing:.1em;text-transform:uppercase;opacity:.6;margin-bottom:5px}
.fd-b{display:flex;gap:8px;flex-wrap:wrap}
.fd.done{opacity:.72}
.lg-own{display:grid;gap:10px;padding:10px 0}
.lg-own textarea{width:100%;min-height:300px;border:1px solid var(--wl);border-radius:4px;background:transparent;padding:12px;font:400 15px/1.5 var(--fh);resize:vertical}
.lg-own textarea:focus{outline:2px solid var(--ac);outline-offset:1px}
.lg-own p{font:400 13px/1.4 var(--fb);opacity:.65}
@media (max-width:1000px){.panes.lg{grid-template-columns:1fr;height:auto}#lgDoc{max-height:430px;padding-inline:14px}#lgList{overflow:visible}}
"""

JS = r"""
(function(){var K=AIK,$=K.$,esc=K.esc,
DOCS={supply:{name:'Договор поставки № 47',side:'проверяю в интересах Покупателя',sub:'оборудование для склада, сумма 2 480 000 ₽',cl:[
 ['1.1','Поставщик обязуется передать, а Покупатель принять и оплатить стеллажное оборудование по Спецификации (Приложение № 1).'],
 ['2.1','Общая стоимость товара составляет 2 480 000 рублей, включая НДС.'],
 ['2.2','Покупатель вносит 100% предоплату в течение 3 банковских дней с даты подписания Договора.'],
 ['2.3','Поставщик вправе в одностороннем порядке изменить цену товара при росте закупочных цен, уведомив Покупателя за 3 дня.'],
 ['3.1','Срок поставки — 45 рабочих дней с даты поступления предоплаты на счёт Поставщика.'],
 ['3.2','Доставка выполняется силами Поставщика до склада Покупателя. Разгрузку выполняет Покупатель.'],
 ['4.1','Приёмка товара по количеству и комплектности проводится в момент передачи.'],
 ['4.2','Претензии по качеству товара принимаются в течение 2 календарных дней с даты приёмки.'],
 ['5.1','За просрочку оплаты Покупатель уплачивает неустойку в размере 1% от суммы долга за каждый день просрочки.'],
 ['5.2','Ответственность Поставщика за просрочку поставки ограничивается суммой 10 000 рублей.'],
 ['6.1','Поставщик вправе отказаться от исполнения Договора в одностороннем порядке, уведомив Покупателя за 5 дней.'],
 ['7.1','Гарантийный срок на товар — 12 месяцев с даты подписания товарной накладной.'],
 ['8.1','Все споры рассматриваются в арбитражном суде по месту нахождения Поставщика.']]},
rent:{name:'Договор аренды офиса № 12-А',side:'проверяю в интересах Арендатора',sub:'помещение 84 м², срок 11 месяцев',cl:[
 ['1.1','Арендодатель передаёт Арендатору во временное пользование нежилое помещение площадью 84 кв. м под офис.'],
 ['2.1','Арендная плата составляет 168 000 рублей в месяц и вносится до 5 числа текущего месяца.'],
 ['2.2','Арендодатель вправе индексировать арендную плату один раз в год, но не более чем на 15%.'],
 ['2.3','Арендатор вносит обеспечительный платёж в размере двух месячных арендных плат.'],
 ['3.1','Коммунальные услуги оплачиваются Арендатором отдельно по показаниям счётчиков.'],
 ['4.1','Арендодатель не несёт ответственности за перебои в подаче электроэнергии, воды и интернета.'],
 ['4.2','Текущий ремонт помещения Арендатор выполняет за свой счёт.'],
 ['5.1','Договор считается продлённым на тот же срок, если Арендатор не заявил об отказе за 90 дней до окончания срока аренды.'],
 ['5.2','При досрочном расторжении Договора по инициативе Арендатора обеспечительный платёж не возвращается.'],
 ['6.1','За просрочку арендной платы начисляются пени 0,5% от суммы долга за каждый день просрочки.'],
 ['7.1','Обстоятельства непреодолимой силы освобождают Стороны от ответственности на время их действия.'],
 ['8.1','Споры рассматриваются в арбитражном суде по месту нахождения Арендодателя.']]},
own:{name:'Свой текст',side:'проверяю в интересах стороны, которая платит',sub:'',cl:[]}},
RULES=[
{id:'pen',re:/(\d+(?:[.,]\d+)?)\s*(?:%|процент\S*)[^.;]{0,70}?(?:за каждый день|в день)/i,sev:function(m){var r=parseFloat(m[1].replace(',','.'));return r>=.5?2:r>.1?1:0},
 title:function(m){return'Неустойка '+m[1]+'% в день'},why:function(m){var r=parseFloat(m[1].replace(',','.'));return'Это '+Math.round(r*365)+'% годовых. В деловой практике обычно 0,1% в день с потолком. Суд может снизить такую неустойку по ст. 333 ГК РФ, но доказывать несоразмерность придётся вам.'},
 fix:'За просрочку оплаты начисляется неустойка 0,1% от суммы просроченного платежа за каждый день просрочки, но не более 10% этой суммы.'},
{id:'price',re:/в одностороннем порядке[^.]*?(?:измен|увелич|повыс|пересм)[^.]*?(?:цен|стоимост|плат)|(?:цен|стоимост|плат)[^.]*?(?:измен|увелич|повыс|пересм)[^.]*?в одностороннем порядке/i,sev:function(){return 2},
 title:function(){return'Цена меняется в одностороннем порядке'},why:function(){return'Контрагент может поднять цену уведомлением, а вы уже внесли деньги и обязаны доплатить. Между компаниями такое условие действует, если вы его подписали (ст. 310 ГК РФ).'},
 fix:'Цена товара является твёрдой и изменяется только по письменному соглашению Сторон.'},
{id:'index',re:/индексир\S+[^.]*?(\d+)\s*%/i,sev:function(m){return +m[1]>=10?1:0},title:function(m){return'Индексация до '+m[1]+'% в год'},
 why:function(m){return'Арендодатель может поднять плату на '+m[1]+'% без объяснения причин. Привяжите индексацию к официальной инфляции или ограничьте её.'},
 fix:'Арендодатель вправе индексировать арендную плату один раз в год на величину не выше индекса потребительских цен за предыдущий год.'},
{id:'early',re:/досрочн\S+[^.]*?(?:штраф|неустойк|удержива|не возвраща)/i,sev:function(){return 2},title:function(){return'Досрочный выход с потерей денег'},
 why:function(){return'Если придётся съехать раньше срока, вы теряете обеспечительный платёж целиком, даже если помещение сдано без долгов и повреждений.'},
 fix:'При досрочном расторжении Договора по инициативе Арендатора с уведомлением за 60 дней обеспечительный платёж засчитывается в оплату последних месяцев аренды.'},
{id:'prepay',re:/(?:100\s*%|стопроцентн\S+|полн\S+)\s*предоплат|предоплат\S*[^.]*?(?:100\s*%|в полном объ[её]ме)/i,sev:function(){return 1},
 title:function(){return'Полная предоплата без обеспечения'},why:function(){return'Вы платите всю сумму до поставки. Если поставка сорвётся, срок возврата денег в договоре не указан.'},
 fix:'Покупатель вносит аванс 30% от стоимости товара, оставшиеся 70% — в течение 5 рабочих дней после приёмки. При просрочке поставки более чем на 10 дней аванс возвращается в течение 3 рабочих дней.'},
{id:'exit',re:/(?:вправе|может)[^.]*?(?:отказаться от (?:исполнения )?(?:настоящего )?Договора|расторгнуть (?:настоящий )?Договор)[^.]*?в одностороннем|в одностороннем[^.]*?(?:отказаться|расторгнуть)/i,
 sev:function(m,t){return/кажд\S+ из сторон|люб\S+ из сторон|стороны вправе/i.test(t)?0:1},title:function(){return'Выйти из договора может только контрагент'},
 why:function(){return'Право одностороннего отказа есть у одной стороны, срок уведомления короткий. Просим такое же право для себя и разумный срок.'},
 fix:'Каждая из Сторон вправе отказаться от Договора, письменно уведомив другую Сторону не менее чем за 30 дней. Полученная предоплата за непоставленный товар возвращается в течение 5 рабочих дней.'},
{id:'court',re:/суд\S*\s+по месту нахождения\s+(Поставщика|Арендодателя|Исполнителя|Продавца|Подрядчика|Лицензиара)/i,sev:function(){return 1},
 title:function(m){return'Суд по месту нахождения '+m[1]},why:function(){return'Судиться придётся в чужом регионе: поездки и местный представитель за ваш счёт. Подсудность по договору допускает ст. 37 АПК РФ, её можно согласовать иначе.'},
 fix:'Все споры рассматриваются в арбитражном суде по месту нахождения истца.'},
{id:'auto',re:/автоматически\s+(?:продлева|пролонгир)|считается\s+(?:продл[её]нным|пролонгированным)/i,sev:function(){return 1},title:function(){return'Автоматическое продление'},
 why:function(m,t){var d=t.match(/за\s+(\d+)\s+(?:календарн\S+\s+|рабоч\S+\s+)?дн/i);return'Чтобы не продлить договор, нужно успеть отказаться'+(d?' за '+d[1]+' дней':'')+' до конца срока. Пропустите дату — аренда продлится на весь новый срок.'},
 fix:'Договор продлевается на тот же срок, если Стороны письменно подтвердили продление не позднее чем за 30 дней до окончания срока аренды.'},
{id:'liab',re:/ответственност\S+[^.]*?(?:ограничива|не превыша|не может превыш)|не нес[её]т ответственности за/i,sev:function(){return 1},title:function(){return'Ответственность контрагента ограничена'},
 why:function(m,t){var s=t.match(/(\d[\d\s]*)\s*руб/i);return s?'Предел '+s[1].trim()+' рублей несоизмерим с суммой договора: реальные убытки от срыва вам не возместят.':'Убытки от таких перебоев вам не возместят, даже если виноват контрагент. Оставьте исключение только для причин, которые от него не зависят.'},
 fix:'Сторона, нарушившая Договор, возмещает другой Стороне причинённые убытки в полном объёме, если не докажет, что нарушение вызвано обстоятельствами непреодолимой силы.'},
{id:'claim',re:/(?:претензи|недостат|замечани)[^.]*?в течение\s+(\d+)\s*(?:\([^)]*\)\s*)?(?:календарн\S+\s+|рабоч\S+\s+)?дн|в течение\s+(\d+)\s*(?:\([^)]*\)\s*)?(?:календарн\S+\s+|рабоч\S+\s+)?дн\S*[^.]*?(?:претензи|недостат|замечани)/i,
 sev:function(m){return +(m[1]||m[2])<=3?1:0},title:function(m){var n=+(m[1]||m[2]);return'На претензии всего '+n+' '+(n===1?'день':'дня')},
 why:function(){return'За такой срок не проверить партию и не оформить акт. Позже товар будет считаться принятым без замечаний, включая скрытые недостатки.'},
 fix:'Покупатель вправе заявить претензии по качеству в течение 10 рабочих дней с даты приёмки, а по скрытым недостаткам — в течение гарантийного срока.'}],
cur='supply',F=[],busy=false,run=0;
var doc=$('#lgDoc'),list=$('#lgList');
function render(k){cur=k;var d=DOCS[k];$('#lgName').textContent=d.name;$('#lgSide').textContent=d.side;K.$$('.lg-tabs button').forEach(function(b){b.classList.toggle('on',b.dataset.doc===k)});
 if(k==='own'&&!d.cl.length){doc.innerHTML='<div class="lg-own"><textarea id="lgTxt" placeholder="Вставьте текст договора или отдельные пункты. Каждый пункт — с новой строки."></textarea><button type="button" class="btn-s" id="lgGo">Разобрать текст</button><p>Текст не покидает эту страницу: разбор идёт прямо в браузере.</p></div>';reset('вставьте текст');return false}
 doc.innerHTML='<h4>'+esc(d.name)+'</h4>'+(d.sub?'<div class="sub">'+esc(d.sub)+'</div>':'')+d.cl.map(function(c,i){return'<p class="cl" id="cl'+i+'">'+(c[0]?'<b>'+esc(c[0])+'.</b>':'')+'<span>'+esc(c[1]).replace(/(\d) (?=\d{3})/g,'$1&nbsp;')+'</span></p>'}).join('')+(k==='own'?'<p style="padding:10px"><button type="button" class="btn-s g" id="lgEd">Изменить текст</button></p>':'');
 doc.scrollTop=0;return true}
function reset(t){F=[];list.innerHTML='';$('#lgScore').textContent='—';$('#lgLvl').textContent=t||'идёт проверка';$('#lgBar').style.width='0';$('#lgCnt').textContent='';$('#lgDl').disabled=true}
function score(){var s=0,b=0,w=0;F.forEach(function(f){if(f.done)return;if(f.sev===2){s+=20;b++}else{s+=7;w++}});s=Math.min(100,s);
 $('#lgScore').textContent=s;$('#lgBar').style.width=s+'%';$('#lgBar').style.background=s>=50?'var(--bad)':s>=20?'var(--warn)':'var(--ok)';
 $('#lgLvl').textContent='из 100 · '+(s>=50?'высокий риск':s>=20?'средний риск':'низкий риск');$('#lgCnt').textContent='критичных: '+b+' · внимание: '+w;
 $('#lgDl').disabled=!F.some(function(f){return f.done});return[b,w]}
function card(f){var el=document.createElement('div');el.className='fd';el.dataset.i=f.i;
 el.innerHTML='<div class="fd-h"><span class="tag '+(f.sev===2?'bad':'warn')+'">'+(f.sev===2?'Критично':'Внимание')+'</span><b>'+(f.n?'п. '+esc(f.n)+' · ':'')+esc(f.title)+'</b></div><p>'+esc(f.why)+'</p>'+
  (f.fix?'<div class="fx"><span>Предлагаю редакцию</span>'+esc(f.fix)+'</div><div class="fd-b"><button type="button" class="btn-s" data-fix>Принять правку</button><button type="button" class="btn-s g" data-show>Показать в тексте</button></div>':'');
 list.appendChild(el);list.scrollTop=list.scrollHeight;return el}
async function analyze(){var my=++run,d=DOCS[cur];busy=true;reset();$('#lgSt').textContent='проверяю пункты…';
 for(var i=0;i<d.cl.length;i++){if(my!==run)return;var p=$('#cl'+i),t=d.cl[i][1];p.classList.add('scan');
  doc.scrollTop=Math.max(0,p.offsetTop-doc.offsetTop-120);
  await K.wait(230);var hit=null;
  for(var r=0;r<RULES.length;r++){var m=t.match(RULES[r].re);if(m){var sv=RULES[r].sev(m,t);if(sv){hit={i:i,n:d.cl[i][0],rule:RULES[r],sev:sv,title:RULES[r].title(m,t),why:RULES[r].why(m,t),fix:RULES[r].fix,old:t};break}}}
  if(my!==run)return;p.classList.remove('scan');if(hit){p.classList.add('s'+hit.sev);F.push(hit);hit.el=card(hit);score();await K.wait(260)}}
 var all=d.cl.map(function(c){return c[1]}).join(' ');
 if(!/непреодолимой силы|форс-мажор/i.test(all)&&d.cl.length>3){var f={i:-1,n:'',sev:1,title:'Нет условия о форс-мажоре',why:'В договоре не описано, что происходит при обстоятельствах, которые не зависят от сторон. Добавьте отдельный пункт.',fix:'',old:''};F.push(f);f.el=card(f)}
 var c=score();doc.scrollTop=0;list.scrollTop=0;$('#lgSt').textContent='проверено пунктов: '+d.cl.length+', замечаний: '+F.length;busy=false;
 K.log(['⚖️',d.name,'критичных: '+c[0]+' · внимание: '+c[1]+' · пунктов: '+d.cl.length,'Проверен']);
 if(!F.length)list.innerHTML='<div class="fd"><div class="fd-h"><span class="tag ok">Чисто</span><b>Рискованных условий по моим правилам нет</b></div><p>Проверил неустойки, цену, предоплату, сроки претензий, подсудность, продление и ответственность. Окончательное решение — за юристом.</p></div>'}
$('#ws').addEventListener('click',function(ev){var t=ev.target,b;
 if(b=t.closest('.lg-tabs button')){run++;busy=false;if(render(b.dataset.doc))analyze();return}
 if(t.id==='lgGo'){var v=$('#lgTxt').value.split(/\n+/).map(function(s){return s.trim()}).filter(function(s){return s.length>12});
  if(!v.length){$('#lgTxt').focus();$('#lgTxt').placeholder='Нужен текст: хотя бы один пункт договора длиннее пары слов.';return}
  DOCS.own.cl=v.slice(0,60).map(function(s){var m=s.match(/^(\d+(?:\.\d+)*)\.?\s+(.*)$/);return m?[m[1],m[2]]:['',s]});render('own');analyze();return}
 if(t.id==='lgEd'){run++;var old=DOCS.own.cl.map(function(c){return(c[0]?c[0]+'. ':'')+c[1]}).join('\n');DOCS.own.cl=[];render('own');$('#lgTxt').value=old;return}
 var fd=t.closest('.fd');if(!fd)return;var f=F.filter(function(x){return String(x.i)===fd.dataset.i&&x.el===fd})[0];if(!f)return;var p=$('#cl'+f.i);
 if(t.hasAttribute('data-show')&&p){doc.scrollTop=p.offsetTop-doc.offsetTop-80;p.classList.remove('fl');void p.offsetWidth;p.classList.add('fl');if(window.innerWidth<=1000)doc.scrollIntoView({block:'nearest'})}
 if(t.hasAttribute('data-fix')&&!f.done){f.done=1;fd.classList.add('done');fd.querySelector('.tag').className='tag ok';fd.querySelector('.tag').textContent='Правка принята';t.remove();
  if(p){p.className='cl okd';p.querySelector('span').innerHTML='<del>'+esc(f.old)+'</del> <ins>'+esc(f.fix)+'</ins>'}score();
  K.log(['✍️','Правка к '+(f.n?'п. '+f.n:'договору'),f.title+' · '+DOCS[cur].name,'В протокол'])}});
$('#lgDl').addEventListener('click',function(){var d=DOCS[cur],L=['ПРОТОКОЛ РАЗНОГЛАСИЙ','к документу: '+d.name,''];
 F.filter(function(f){return f.done}).forEach(function(f,i){L.push((i+1)+'. '+(f.n?'Пункт '+f.n:'Условие')+' — '+f.title,'   Редакция контрагента: '+f.old,'   Наша редакция: '+f.fix,'   Обоснование: '+f.why,'')});
 var a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['﻿'+L.join('\r\n')],{type:'text/plain;charset=utf-8'}));a.download='Протокол разногласий.txt';document.body.appendChild(a);a.click();a.remove()});
render('supply');K.demo=function(){analyze()};
})();
"""


def cfg() -> dict:
    return {
        "slug": "ai/legal", "brand": "Параграф", "logoIcon": "§",
        "title": "Параграф — ИИ-юрист: проверка договора по пунктам и протокол разногласий",
        "desc": "ИИ-ассистент юриста: читает договор по пунктам, находит рискованные условия, объясняет их простым языком, "
                "предлагает редакцию и собирает протокол разногласий.",
        "theme": theme(bg="#f6f3ec", ink="#17140f", soft="#514b40", mut="#8a8375", line="#ded8ca", line2="#17140f",
                       card="#fbf9f4", ac="#8a1f14", aci="#ffffff", fh='"Spectral",serif', fb='"Inter Tight",sans-serif',
                       hw="500", ht="-.02em", rb="2px", rc="0px", rs="2px", rw="4px", rs2="2px", wbg="#fffefb",
                       warn="#b67a00", ok="#2f7a4f", bad="#b3261a", wsh="0 0 0 1px #17140f,10px 10px 0 #17140f"),
        "fonts": [("Spectral", "spectral", [400, 500, 600], "normal"), ("Spectral", "spectral", [500], "italic"),
                  ("Inter Tight", "inter-tight", [400, 500, 600], "normal")],
        "css": CSS + ".hero h1{font-size:clamp(42px,6.2vw,92px);line-height:1}.hero h1 em{font-style:italic}"
                     ".how div,.feat{background:transparent;border-top:2px solid var(--ink);padding-inline:0}"
                     ".feat i{background:transparent;width:auto;height:auto;font-size:26px;place-items:start}"
                     ".res{background:var(--ink);box-shadow:0 0 0 1px var(--ink)}.ints span{background:transparent;box-shadow:inset 0 0 0 1px var(--ink)}"
                     ".tag{border-radius:2px}.panel{border-radius:4px;box-shadow:0 0 0 1px #17140f,8px 8px 0 #17140f}.rowx em,.rowx .d{border-radius:2px}"
                     ".btn.ghost{box-shadow:inset 0 0 0 1.5px var(--ink)}.kick{letter-spacing:.2em}",
        "hero": {"kicker": "ИИ-юрист · разбор договора", "h1": "Читает договор и находит то, <em>что обойдётся дорого</em>",
                 "lead": "Параграф проходит договор пункт за пунктом, объясняет каждый риск простым языком, предлагает свою редакцию "
                         "и собирает протокол разногласий. Юрист получает готовую основу вместо чистого листа.",
                 "cta": "Проверить договор",
                 "stats": [("2 мин", "на договор в 20 страниц"), ("10", "типов рисков в каждом пункте"), ("−70%", "времени юриста на первичную вычитку")]},
        "demo": {"type": "custom", "html": HTML, "js": JS,
                 "note": "Проверка работает: откройте другой договор или вставьте свои пункты во вкладке «Свой текст»"},
        "howTitle": "Как Параграф читает договор",
        "howLead": "Тот же порядок, что у внимательного юриста, только за минуты и без пропущенных пунктов на двадцатой странице.",
        "how": [("Разбивает на пункты", "Берёт текст из Word, PDF или скана, восстанавливает нумерацию и определяет, чьи интересы защищать."),
                ("Проверяет каждый пункт", "Неустойки, цена, предоплата, сроки претензий, выход из договора, подсудность, продление, ответственность."),
                ("Объясняет и считает", "Пишет, чем условие опасно, и переводит проценты в понятные цифры: 1% в день — это 365% годовых."),
                ("Предлагает редакцию", "Даёт формулировку из вашей библиотеки условий. Принятые правки складывает в протокол разногласий.")],
        "featsTitle": "Что юрист получает на выходе",
        "feats": [("⚖️", "Оценку риска договора", "Одна цифра и список причин: сразу видно, подписывать, править или отказываться."),
                  ("🔎", "Замечания с привязкой к пункту", "Каждое замечание ведёт к месту в тексте. Ничего не нужно искать глазами."),
                  ("✍️", "Готовые формулировки", "Редакции берутся из библиотеки условий вашей компании, а не придумываются на ходу."),
                  ("📄", "Протокол разногласий", "Редакция контрагента, ваша редакция и обоснование — файлом, который можно отправлять."),
                  ("📚", "Ссылки на нормы", "К замечаниям — статьи ГК и АПК, чтобы юрист мог быстро проверить вывод."),
                  ("🗂", "Сверку с шаблоном", "Сравнивает договор контрагента с вашей типовой формой и показывает, что изменено.")],
        "control": {"title": "Решение остаётся за юристом",
                    "lead": "Параграф готовит черновик заключения. Что принять, что править и что подписывать, решает человек.",
                    "rules": [("Не выдаёт заключение за юридическое", "Это первичная вычитка: спорные места помечаются для проверки юристом."),
                              ("Не придумывает нормы", "Ссылается только на статьи из подключённой базы и показывает, откуда вывод."),
                              ("Не правит без согласия", "Каждая правка попадает в текст и протокол только после кнопки «Принять»."),
                              ("Не выносит документы наружу", "Договоры обрабатываются в вашем контуре, доступ — по ролям.")],
                    "panel": {"name": "Параграф · журнал проверок",
                              "kpi": [(14, "договоров сегодня"), ("37", "критичных условий"), ("2 мин", "на договор")],
                              "rows": [("⚖️", "Договор подряда № 8/26", "критичных: 1 · внимание: 3 · пунктов: 42", "Проверен"),
                                       ("✍️", "Правка к п. 6.4", "неустойка 0,5% в день · договор услуг", "В протокол"),
                                       ("👤", "Передан юристу", "нетиповая схема оплаты через третье лицо", "Юристу", "h")]}},
        "resTitle": "Что получает компания",
        "results": [("2 мин", "первичная вычитка вместо часа"), ("−70%", "времени юриста на типовые договоры"),
                    ("0", "пунктов, пропущенных на двадцатой странице"), ("1 день", "на согласование вместо трёх")],
        "ints": ["Word и PDF", "Сканы с распознаванием", "1С:Документооборот", "Directum", "Битрикс24", "Консультант Плюс", "Гарант", "Telegram"],
        "faq": [("Параграф заменяет юриста?", "Нет. Он снимает первичную вычитку и готовит протокол, а решение и ответственность "
                                              "остаются за юристом. Нетиповые условия он не оценивает, а помечает для проверки."),
                ("Откуда берутся формулировки правок?", "Из библиотеки условий вашей компании: мы загружаем ваши типовые договоры и "
                                                        "позиции по спорным пунктам. Нет библиотеки — соберём её вместе с юристом.")] + FAQ_COMMON,
        "ctaTitle": "Проверьте свой договор за две минуты", "ctaBtn": "Открыть проверку",
    }
