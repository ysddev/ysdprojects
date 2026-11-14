"""«Реестр» — ИИ для документооборота: читает входящие счета, акты и договоры, достаёт реквизиты, проверяет арифметику, дубли и лимиты, ставит на маршрут."""
from ..ai import FAQ_COMMON
from ._t import theme

HTML = """<div class="ws-bar"><i class="dots"></i><b>Реестр · входящие документы</b><span id="dcSt">5 документов в очереди</span></div>
<div class="panes dc">
 <div class="pane"><div class="pane-h">Входящие<span id="dcCnt">0 из 5</span></div><div class="scroll" id="dcIn"></div>
  <label class="dc-th"><span>Финдиректор согласует от <b id="dcTv"></b></span><input type="range" id="dcT" min="100" max="500" step="50" value="300" aria-label="Порог согласования финансовым директором, тысяч рублей"></label></div>
 <div class="pane dc-mid"><div class="pane-h" id="dcPh">Документ</div><div class="scroll dc-desk"><div class="paper" id="dcP"></div></div></div>
 <div class="pane"><div class="pane-h">Что понял ассистент</div><div class="scroll dc-r">
  <div class="bb" data-st="wait"><div class="bb-h"><i>1</i>Реквизиты</div><div id="dcF"><p class="em">Выберите документ слева</p></div></div>
  <div class="bb" data-st="wait"><div class="bb-h"><i>2</i>Проверки</div><div id="dcC"></div></div>
  <div class="bb" data-st="wait"><div class="bb-h"><i>3</i>Маршрут</div><div id="dcR"></div></div></div></div>
</div>"""

CSS = """
.panes.dc{grid-template-columns:minmax(0,.62fr) minmax(0,1.1fr) minmax(0,.9fr);height:min(700px,84vh)}
#dcIn{padding:6px 10px}
.di{display:grid;grid-template-columns:34px 1fr;gap:10px;align-items:center;width:100%;text-align:left;padding:10px;border-radius:8px;font-size:13.5px;line-height:1.3;margin-bottom:2px}
.di:hover{background:var(--w2)}.di.on{background:color-mix(in srgb,var(--ac) 10%,transparent);box-shadow:inset 2px 0 0 var(--ac)}
.di i{width:34px;height:40px;border-radius:4px;background:var(--w2);display:grid;place-items:center;font:500 10px/1 var(--fm);font-style:normal;box-shadow:inset 0 0 0 1px var(--wl)}
.di b{display:block;font-size:14px;font-weight:600}
.di small{opacity:.6;font-size:12.5px;display:block}
.di .tag{margin-top:5px;font-size:11px;padding:4px 7px}
.dc-th{display:grid;gap:6px;padding:12px 16px 14px;border-top:1px solid var(--wl);font-size:13px}
.dc-th input{width:100%;accent-color:var(--ac)}
.dc-desk{background:var(--w2);padding:18px}
.paper{position:relative;background:#fff;color:#1a2233;box-shadow:0 1px 2px rgba(0,0,0,.08),0 12px 30px -18px rgba(0,0,0,.35);padding:26px 26px 30px;font-size:12.5px;line-height:1.45;min-height:100%;overflow:hidden}
.paper h5{margin:0 0 2px;font:600 17px/1.2 var(--fb)}
.paper .dt{opacity:.6;margin-bottom:14px}
.paper .pp{display:grid;grid-template-columns:86px 1fr;gap:3px 10px;margin-bottom:14px}
.paper .pp span:nth-child(odd){opacity:.55}
.paper table{width:100%;border-collapse:collapse;font-family:var(--fm);font-size:11.5px;margin-bottom:10px}
.paper th{font:500 10.5px/1.2 var(--fb);text-align:left;opacity:.6;padding:6px 6px;border-bottom:1.5px solid #1a2233}
.paper td{padding:7px 6px;border-bottom:1px solid #e3e7ee;vertical-align:top}
.paper td:first-child{font-family:var(--fb);font-size:12.5px}
.paper td:not(:first-child),.paper th:not(:first-child){text-align:right;white-space:nowrap}
.paper .tt{display:grid;justify-content:end;gap:3px;font-family:var(--fm);font-size:12px;text-align:right}
.paper .tt b{font-size:14px}
.paper .ft{margin-top:18px;opacity:.6}
.paper p{margin:0 0 8px}
.paper mark{background:transparent;color:inherit;border-radius:3px;transition:background .4s,box-shadow .4s;padding:0 2px;margin:0 -2px}
.paper mark.hl{background:color-mix(in srgb,var(--ac) 16%,transparent);box-shadow:0 0 0 1px color-mix(in srgb,var(--ac) 45%,transparent)}
.paper mark.er{background:color-mix(in srgb,var(--bad) 16%,transparent);box-shadow:0 0 0 1px var(--bad)}
.paper .scan{position:absolute;left:0;right:0;top:0;height:70px;background:linear-gradient(180deg,transparent,color-mix(in srgb,var(--ac) 22%,transparent));border-bottom:2px solid var(--ac);animation:dsc 1s cubic-bezier(.4,0,.6,1) both;pointer-events:none}
@keyframes dsc{from{transform:translateY(-70px)}to{transform:translateY(560px);opacity:0}}
.dc-r .kv b{font-size:13.5px;font-weight:500;font-variant-numeric:tabular-nums}#dcPh{font-family:var(--fb);letter-spacing:.04em}
.ck{display:grid;grid-template-columns:20px 1fr;gap:9px;padding:6px 0;font-size:13.5px;line-height:1.35;animation:kin .3s both}
.ck i{width:20px;height:20px;border-radius:50%;display:grid;place-items:center;font-style:normal;font-size:11px;font-weight:700;color:#fff;background:var(--ok)}
.ck.w i{background:var(--warn)}.ck.e i{background:var(--bad)}
.ck span{display:block;opacity:.65;font-size:12.5px}
.rt{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-bottom:10px}
.rt i{font-style:normal;font-size:12.5px;font-weight:500;padding:6px 10px;border-radius:6px;background:var(--w2);animation:kin .3s both}
.rt i.me{background:var(--ac);color:var(--aci)}
.rt em{font-style:normal;opacity:.4}
.dc-v{padding:12px;border-radius:8px;font-size:13.5px;line-height:1.4;margin-bottom:10px;animation:kin .3s both}
.dc-v.ok{background:color-mix(in srgb,var(--ok) 12%,transparent)}.dc-v.w{background:color-mix(in srgb,var(--warn) 16%,transparent)}.dc-v.e{background:color-mix(in srgb,var(--bad) 11%,transparent)}
.dc-v b{display:block;font-size:14.5px}
.dc-l{padding:12px;border-radius:8px;background:var(--w2);font-size:13.5px;line-height:1.45;white-space:pre-line;margin-top:10px}
@media (max-width:1000px){.panes.dc{grid-template-columns:1fr;height:auto}#dcIn{display:flex;overflow-x:auto;gap:6px;scrollbar-width:none}.di{flex:none;width:200px;margin:0}.dc-desk{max-height:440px}.dc-r{overflow:visible}}
@media (max-width:640px){.paper{padding:18px 14px}.dc-desk{padding:10px}.paper th:nth-child(2),.paper td:nth-child(2),.paper th:nth-child(3),.paper td:nth-child(3){display:none}}
"""

JS = r"""
(function(){var K=AIK,$=K.$,esc=K.esc,MN=['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря'];
function dt(n){var d=new Date();d.setDate(d.getDate()+n);return d}
function fd(d){return d.getDate()+' '+MN[d.getMonth()]+' '+d.getFullYear()}
function wd(d,n){d=new Date(d);while(n>0){d.setDate(d.getDate()+1);if(d.getDay()%6)n--}return d}
function r2(n){return n.toFixed(2).replace('.',',').replace(/\B(?=(\d{3})+(?!\d))/g,' ')}
function rub(n){return K.fmt(n)+' ₽'}
var VAT=22,TH=300,
D=[{id:'a',ty:'Счёт',no:'318',d:dt(-1),from:'ООО «Северный фанерный двор»',base:'Договор поставки № 14-П',lim:[2000000,1240000],lines:[['Фанера ФК 18 мм, 1525×1525',120,1450],['Доставка до склада',1,9500]],vat:null,init:'отдел снабжения'},
   {id:'b',ty:'Счёт',no:'77',d:dt(-1),from:'ООО «Чистый этаж»',base:'Договор услуг № 3-У',lim:[1200000,860000],lines:[['Уборка офиса, ноябрь',1,86000]],vat:18920,init:'административный отдел'},
   {id:'c',ty:'Акт',no:'205',d:dt(-2),from:'ООО «Печатня № 4»',base:'Счёт № 198 на 400 000 ₽',pay:400000,lines:[['Печать каталогов, 2 000 шт.',2000,186],['Доставка тиража',1,40600]],vat:null,init:'отдел маркетинга'},
   {id:'d',ty:'Счёт',no:'318',d:dt(-1),from:'ООО «Северный фанерный двор»',base:'Договор поставки № 14-П',lim:[2000000,1240000],lines:[['Фанера ФК 18 мм, 1525×1525',120,1450],['Доставка до склада',1,9500]],vat:null,init:'отдел снабжения',dup:'a'},
   {id:'e',ty:'Договор',no:'22',d:dt(0),from:'ООО «Гранит и сыновья»',sum:1850000,init:'отдел снабжения',contract:1}],
cur=null,run=0,done={},reg={};
function tot(x){return x.contract?x.sum:x.lines.reduce(function(s,l){return s+l[1]*l[2]},0)}
function vat(x){return Math.round(tot(x)*VAT/(100+VAT)*100)/100}
function inbox(){$('#dcIn').innerHTML=D.map(function(x){var st=done[x.id];return'<button type="button" class="di'+(cur===x?' on':'')+'" data-d="'+x.id+'"><i>'+(x.contract?'DOC':'PDF')+'</i><span><b>'+x.ty+' № '+x.no+'</b><small>'+esc(x.from.replace('ООО ',''))+'</small>'+(st?'<span class="tag '+st[1]+'">'+st[0]+'</span>':'')+'</span></button>'}).join('');
 var n=Object.keys(done).length;$('#dcCnt').textContent=n+' из '+D.length;$('#dcSt').textContent=n===D.length?'очередь разобрана':(D.length-n)+' в очереди'}
function paper(x){var h='<h5><mark data-f="ty">'+x.ty+(x.contract?' поставки':x.ty==='Счёт'?' на оплату':' выполненных работ')+'</mark> № <mark data-f="no">'+x.no+'</mark></h5><div class="dt">от <mark data-f="d">'+fd(x.d)+'</mark></div>';
 if(x.contract)return h+'<div class="pp"><span>Поставщик</span><span><mark data-f="from">'+esc(x.from)+'</mark></span><span>Покупатель</span><span>ООО «Ваша компания»</span></div>'+
  '<p>1.1. Поставщик обязуется поставить гранитную плитку по спецификации, а Покупатель принять и оплатить её.</p><p>2.1. Цена договора составляет <mark data-f="sum">1 850 000 рублей</mark>, включая НДС '+VAT+'%.</p><p>2.2. Покупатель вносит <mark data-f="pre">предоплату 50%</mark> в течение 5 банковских дней.</p>'+
  '<p>3.1. Срок поставки — <mark data-f="term">30 календарных дней</mark> с даты предоплаты.</p><p>5.1. За просрочку оплаты начисляется неустойка <mark data-f="pen">0,5% за каждый день</mark> просрочки.</p><p>8.1. Договор действует до <mark data-f="end">31 декабря '+x.d.getFullYear()+' года</mark>.</p><div class="ft">Подпись Поставщика: есть · Подпись Покупателя: нет</div>';
 var t=tot(x),v=x.vat!=null?x.vat:vat(x);
 return h+'<div class="pp"><span>'+(x.ty==='Акт'?'Исполнитель':'Поставщик')+'</span><span><mark data-f="from">'+esc(x.from)+'</mark></span><span>'+(x.ty==='Акт'?'Заказчик':'Покупатель')+'</span><span>ООО «Ваша компания»</span><span>Основание</span><span><mark data-f="base">'+esc(x.base)+'</mark></span></div>'+
  '<table><tr><th>Наименование</th><th>Кол-во</th><th>Цена</th><th>Сумма</th></tr>'+x.lines.map(function(l){return'<tr><td>'+esc(l[0])+'</td><td>'+K.fmt(l[1])+'</td><td>'+r2(l[2])+'</td><td>'+r2(l[1]*l[2])+'</td></tr>'}).join('')+'</table>'+
  '<div class="tt"><span>Итого: <b><mark data-f="sum">'+r2(t)+'</mark></b></span><span>В том числе НДС '+VAT+'%: <mark data-f="vat">'+r2(v)+'</mark></span></div>'+
  '<div class="ft">'+(x.ty==='Счёт'?'Оплатить до '+fd(wd(x.d,5))+'. Счёт действителен 5 банковских дней.':'Работы выполнены полностью, стороны претензий не имеют.')+'</div>'}
function st(id,v){$('#'+id).parentNode.dataset.st=v}
function fields(x){if(x.contract)return[['Тип','договор поставки, проект','ty'],['Номер и дата','№ '+x.no+' от '+fd(x.d),'no'],['Контрагент',x.from,'from'],['Сумма',rub(x.sum),'sum'],['Предоплата','50% — '+rub(x.sum/2),'pre'],['Срок поставки','30 дней','term'],['Неустойка','0,5% в день','pen'],['Действует до','31.12.'+x.d.getFullYear(),'end']];
 return[['Тип',x.ty==='Счёт'?'счёт на оплату':'акт выполненных работ','ty'],['Номер и дата','№ '+x.no+' от '+fd(x.d),'no'],['Контрагент',x.from,'from'],['Основание',x.base,'base'],['Сумма',r2(tot(x))+' ₽','sum'],['НДС '+VAT+'%',r2(x.vat!=null?x.vat:vat(x))+' ₽','vat']].concat(x.ty==='Счёт'?[['Оплатить до',fd(wd(x.d,5)),'']]:[])}
function checks(x){var c=[],t=tot(x),bad=0,warn=0;
 if(x.contract){c.push(['e','Нет подписи с нашей стороны','документ — проект, регистрировать как действующий нельзя']);c.push(['w','Неустойка 0,5% в день','это 183% годовых — выше принятого в компании 0,1%']);c.push(['w','Предоплата 50% — '+rub(x.sum/2),'по регламенту аванс свыше 500 000 ₽ согласует финдиректор']);return{c:c,v:'law'}}
 c.push(['','Сумма строк сходится с итогом',x.lines.length+' '+(x.lines.length===1?'строка':'строки')+' · '+r2(t)+' ₽']);
 var v=vat(x);if(x.vat!=null&&Math.abs(x.vat-v)>0.5){c.push(['e','НДС посчитан неверно','в документе '+r2(x.vat)+' ₽, должно быть '+r2(v)+' ₽ · разница '+r2(Math.abs(x.vat-v))+' ₽']);bad=1}else c.push(['','НДС '+VAT+'% посчитан верно',r2(v)+' ₽ в составе суммы']);
 if(x.dup){c.push(['e',reg[x.dup]?'Дубль: документ уже в реестре':'Дубль: такой же счёт уже в очереди','счёт № '+x.no+' от того же контрагента на ту же сумму '+(reg[x.dup]?'зарегистрирован сегодня':'получен раньше и ждёт разбора')]);return{c:c,v:'dup'}}
 else c.push(['','Дублей в реестре нет','сверено по номеру, контрагенту и сумме']);
 if(x.lim){var left=x.lim[0]-x.lim[1];if(t>left){c.push(['w','Превышен остаток по договору','остаток '+rub(left)+', счёт на '+rub(t)]);warn=1}else c.push(['','Укладывается в лимит договора','остаток по договору после оплаты: '+rub(left-t)])}
 if(x.pay!=null){if(Math.abs(t-x.pay)>1){c.push(['w','Сумма акта не равна оплаченному счёту','акт на '+rub(t)+', оплачено '+rub(x.pay)+' · разница '+rub(Math.abs(t-x.pay))]);warn=1}else c.push(['','Сумма акта равна оплаченному счёту',rub(x.pay)])}
 return{c:c,v:bad?'ret':warn?'ask':'ok'}}
function route(x,v){var t=tot(x),big=t>=TH*1000,r=[];
 if(v==='dup')return{r:[],cls:'e',h:'Не регистрировать',p:'Дубль отклонён, чтобы счёт не оплатили дважды. Оригинал уже на маршруте.',btn:['Отклонить дубль','Дубль','bad']};
 if(v==='ret')return{r:['Реестр','Контрагент'],cls:'e',h:'Вернуть контрагенту на исправление',p:'С ошибкой в НДС документ не примет бухгалтерия. Письмо с просьбой исправить готово.',btn:['Отправить письмо контрагенту','Возврат','bad'],letter:1};
 if(v==='law')return{r:['Реестр','Юрист','Финдиректор','Подписант'],cls:'w',h:'На проверку юристу',p:'Проект договора с отклонениями от регламента. К карточке приложены замечания.',btn:['Отправить юристу','У юриста','warn']};
 r=['Реестр',x.init.replace(/^./,function(a){return a.toUpperCase()})];if(big)r.push('Финдиректор');r.push(x.ty==='Акт'?'Бухгалтерия: закрытие':'Бухгалтерия: оплата');
 if(v==='ask')return{r:r,cls:'w',h:'На согласование с пометкой',p:'Расхождение не блокирует документ, но инициатор должен подтвердить сумму.'+(big?' Сумма от '+TH+' 000 ₽: добавлен финдиректор.':''),btn:['Отправить по маршруту','На согласовании','warn']};
 return{r:r,cls:'ok',h:'Можно '+(x.ty==='Акт'?'закрывать':'оплачивать'),p:'Все проверки пройдены.'+(big?' Сумма от '+TH+' 000 ₽: в маршрут добавлен финдиректор.':' Сумма меньше '+TH+' 000 ₽: финдиректор не нужен.'),btn:['Отправить по маршруту','На маршруте','ok']}}
function drawRoute(x,v){var R=route(x,v);$('#dcR').innerHTML=(R.r.length?'<div class="rt">'+R.r.map(function(s,i){return(i?'<em>→</em>':'')+'<i class="'+(i?'':'me')+'">'+esc(s)+'</i>'}).join('')+'</div>':'')+
  '<div class="dc-v '+R.cls+'"><b>'+esc(R.h)+'</b>'+esc(R.p)+'</div>'+(done[x.id]?'<span class="tag '+done[x.id][1]+'">'+done[x.id][0]+'</span>':'<button type="button" class="btn-s" id="dcGo">'+R.btn[0]+'</button>')+'<div class="dc-l" id="dcL" hidden></div>';return R}
async function open(x){var my=++run;cur=x;inbox();$('#dcPh').textContent=x.ty+' № '+x.no+' · '+x.from;$('#dcP').innerHTML=paper(x)+'<div class="scan"></div>';$('#dcP').parentNode.scrollTop=0;
 ['dcF','dcC','dcR'].forEach(function(i){$('#'+i).innerHTML='';st(i,'wait')});st('dcF','run');await K.wait(900);if(my!==run)return;
 var F=fields(x);for(var i=0;i<F.length;i++){var m=F[i][2]&&$('#dcP mark[data-f="'+F[i][2]+'"]');if(m)m.classList.add('hl');$('#dcF').insertAdjacentHTML('beforeend','<div class="kv"><span>'+esc(F[i][0])+'</span><b>'+esc(F[i][1])+'</b></div>');await K.wait(150);if(my!==run)return}
 st('dcF','done');st('dcC','run');await K.wait(350);var C=checks(x);
 for(i=0;i<C.c.length;i++){var c=C.c[i];$('#dcC').insertAdjacentHTML('beforeend','<div class="ck '+c[0]+'"><i>'+(c[0]==='e'?'✕':c[0]==='w'?'!':'✓')+'</i><div>'+esc(c[1])+'<span>'+esc(c[2])+'</span></div></div>');
  if(c[0]==='e'&&/НДС/.test(c[1])){var vm=$('#dcP mark[data-f="vat"]');vm.classList.remove('hl');vm.classList.add('er')}await K.wait(260);if(my!==run)return}
 st('dcC','done');st('dcR','run');await K.wait(300);x._v=C.v;drawRoute(x,C.v);st('dcR','done')}
$('#ws').addEventListener('click',function(ev){var t=ev.target,b=t.closest('.di');if(b){open(D.filter(function(x){return x.id===b.dataset.d})[0]);return}
 if(t.id==='dcGo'&&cur){var x=cur,R=route(x,x._v);done[x.id]=[R.btn[1],R.btn[2]];if(x._v!=='dup'&&x._v!=='ret')reg[x.id]=1;
  if(R.letter){var L=$('#dcL');L.hidden=false;K.stream(L,'Здравствуйте!\n\nВ счёте № '+x.no+' от '+fd(x.d)+' неверно указан НДС: '+r2(x.vat)+' ₽ вместо '+r2(vat(x))+' ₽ при сумме '+r2(tot(x))+' ₽ с НДС '+VAT+'%.\n\nПожалуйста, пришлите исправленный счёт — оплатим в течение 5 банковских дней после получения.',14)}
  t.outerHTML='<span class="tag '+R.btn[2]+'">'+R.btn[1]+'</span>';inbox();
  K.log([x._v==='ok'?'📄':x._v==='dup'?'🚫':x._v==='ret'?'↩️':'👤',x.ty+' № '+x.no+' · '+x.from.replace('ООО ',''),R.h+(x.contract?'':' · '+rub(tot(x))),R.btn[1],x._v==='ok'?'':'h'])}});
$('#dcT').addEventListener('input',function(){TH=+this.value;$('#dcTv').textContent=TH+' 000 ₽';if(cur&&cur._v&&$('#dcR').innerHTML)drawRoute(cur,cur._v)});
$('#dcTv').textContent=TH+' 000 ₽';inbox();$('#dcP').innerHTML=paper(D[0]);
K.demo=function(){open(D[0])};
})();
"""


def cfg() -> dict:
    return {
        "slug": "ai/docs", "brand": "Реестр", "logoIcon": "Р",
        "title": "Реестр — ИИ для документооборота: счета, акты и договоры без ручного ввода",
        "desc": "ИИ-ассистент документооборота: читает входящие документы, достаёт реквизиты и суммы, проверяет арифметику, "
                "дубли и лимиты договоров и отправляет документ по маршруту согласования.",
        "theme": theme(bg="#edf0f5", ink="#0e1a2e", soft="#46536a", mut="#7b879b", line="#d6dce6", line2="#b9c2d0",
                       card="#ffffff", ac="#1f5eff", aci="#ffffff", fh='"IBM Plex Sans",sans-serif', fb='"IBM Plex Sans",sans-serif',
                       fm='"IBM Plex Mono",monospace', hw="600", ht="-.03em", rb="6px", rc="8px", rs="10px", rw="10px",
                       rs2="6px", wbg="#ffffff", cbg="#0e1a2e", cink="#ffffff",
                       wsh="0 0 0 1px #c9d1dd,0 50px 100px -60px rgba(14,26,46,.5)", csh="0 0 0 1px #d6dce6"),
        "fonts": [("IBM Plex Sans", "ibm-plex-sans", [400, 500, 600], "normal"), ("IBM Plex Mono", "ibm-plex-mono", [400, 500], "normal")],
        "css": CSS + ".kick,.pane-h,.bb-h,.how div::before{font-family:var(--fm);font-weight:500;letter-spacing:.06em}"
                     ".hero h1{font-size:clamp(38px,5.4vw,78px);line-height:1.02}.hs b,.res b{font-family:var(--fm);font-weight:500;letter-spacing:-.04em}"
                     ".feat i{background:#edf0f5;border-radius:6px}.tag,.rowx em,.ints span{border-radius:4px}.panel{border-radius:10px}"
                     ".hero{background:repeating-linear-gradient(90deg,transparent 0 119px,#e0e5ed 119px 120px)}",
        "hero": {"kicker": "ИИ для документооборота", "h1": "Счёт пришёл — <em>через 20 секунд он уже на маршруте</em>",
                 "lead": "Реестр читает входящие счета, акты и договоры, сам заполняет карточку, пересчитывает суммы и НДС, ловит дубли "
                         "и превышение лимитов и отправляет документ тем, кто должен его согласовать.",
                 "cta": "Разобрать входящие",
                 "stats": [("20 сек", "на документ вместо 6 минут"), ("0", "счетов, оплаченных дважды"), ("96%", "карточек без ручных правок")]},
        "demo": {"type": "custom", "html": HTML, "js": JS,
                 "note": "Разбор работает: открывайте документы слева, отправляйте по маршруту и двигайте порог согласования финдиректором"},
        "howTitle": "Что происходит с каждым документом",
        "howLead": "От письма с вложением до согласующего документ проходит четыре шага. Человек подключается там, где нужно решение.",
        "how": [("Читает документ", "PDF, скан, фото или файл из ЭДО. Определяет тип, номер, дату, контрагента, основание, суммы и строки."),
                ("Пересчитывает", "Складывает строки, проверяет НДС по ставке, сверяет акт с оплаченным счётом и остатком по договору."),
                ("Ищет дубли и нарушения", "Сверяет с реестром по номеру, контрагенту и сумме. Проекты договоров сравнивает с регламентом компании."),
                ("Ставит на маршрут", "Строит цепочку согласования по вашим правилам и порогам сумм. Ошибочные документы возвращает с письмом.")],
        "featsTitle": "Что Реестр снимает с бухгалтерии и офис-менеджера",
        "feats": [("📥", "Ввод без рук", "Реквизиты, строки и суммы попадают в карточку сами. В документе подсвечено, откуда взято каждое поле."),
                  ("🧮", "Проверка арифметики", "Итог, НДС, расхождение акта и счёта. Ошибку видно до оплаты, а не на сверке через квартал."),
                  ("🚫", "Защита от дублей", "Один и тот же счёт, пришедший почтой и через ЭДО, не уйдёт в оплату второй раз."),
                  ("📊", "Лимиты договоров", "Помнит, сколько уже оплачено по договору, и предупреждает о превышении."),
                  ("🧭", "Маршрут по правилам", "Кто согласует, зависит от суммы, типа документа и подразделения. Пороги меняете сами."),
                  ("✉️", "Письма контрагентам", "Просьба исправить документ готова сразу: что не так, на сколько и что прислать.")],
        "control": {"title": "Деньги двигает человек",
                    "lead": "Реестр готовит карточку и маршрут. Оплату, подпись и отказ подтверждают ответственные сотрудники.",
                    "rules": [("Ничего не оплачивает сам", "Документ попадает в оплату только после согласования по маршруту."),
                              ("Не угадывает нечитаемое", "Если поле распознано неуверенно, оно помечается для проверки, а не заполняется наугад."),
                              ("Показывает основание", "Каждое поле карточки подсвечено в исходном документе."),
                              ("Пишет всё в журнал", "Кто, когда и что сделал с документом — видно в истории карточки.")],
                    "panel": {"name": "Реестр · журнал документов",
                              "kpi": [(87, "документов сегодня"), ("4", "возврата контрагентам"), ("2 дубля", "остановлено")],
                              "rows": [("📄", "Счёт № 1042 · Офис-Снаб", "Можно оплачивать · 48 300 ₽", "На маршруте"),
                                       ("↩️", "УПД № 77 · Вектор-Сервис", "нет подписи и даты приёмки", "Возврат", "h"),
                                       ("🚫", "Счёт № 311 · Городская типография", "тот же счёт пришёл через ЭДО", "Дубль", "h")]}},
        "resTitle": "Что получает компания",
        "results": [("20 сек", "на документ вместо шести минут"), ("−85%", "ручного ввода в учётную систему"),
                    ("0", "двойных оплат"), ("1 день", "на согласование вместо четырёх")],
        "ints": ["1С:Бухгалтерия", "1С:Документооборот", "Диадок", "СБИС", "Directum", "Битрикс24", "Почта", "Telegram"],
        "faq": [("Какие документы Реестр читает?", "Счета, акты, УПД, накладные, договоры и письма: PDF, сканы, фото и файлы из ЭДО. "
                                                   "Новые типы документов добавляем под ваш процесс."),
                ("Что, если скан плохого качества?", "Поля, в которых ассистент не уверен, помечаются для проверки человеком. "
                                                     "Такой документ не уходит на маршрут, пока поле не подтвердят.")] + FAQ_COMMON,
        "ctaTitle": "Разберите входящие, не открывая 1С", "ctaBtn": "Открыть реестр",
    }
