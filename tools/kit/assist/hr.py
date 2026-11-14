"""«Отбор» — ИИ-ассистент HR: оценка откликов по требованиям вакансии, рейтинг с объяснением, вопросы к интервью, письма."""
from ..ai import FAQ_COMMON
from ._t import theme

HTML = """<div class="ws-bar"><i class="dots"></i><b>Отбор · Менеджер по продажам B2B</b><span id="hrSt">8 откликов ждут разбора</span></div>
<div class="panes hr">
 <div class="pane"><div class="pane-h">Требования вакансии<span>меняйте — рейтинг пересчитается</span></div>
  <div class="scroll hr-req"><div id="hrCr"></div>
   <label class="hr-bud"><span>Бюджет на оклад: <b id="hrBv"></b></span><input type="range" id="hrB" min="90" max="220" step="10" value="150" aria-label="Бюджет на оклад, тысяч рублей"></label>
   <form class="hr-add" id="hrAdd"><input id="hrNew" placeholder="Своё требование: тендеры, медицина…" aria-label="Своё требование"><button class="btn-s" type="submit">Добавить</button></form>
   <p class="hr-fair">Пол, возраст, фото и семейное положение в оценке не участвуют: ассистент их не читает.</p></div></div>
 <div class="pane"><div class="pane-h">Кандидаты<span id="hrCnt"></span></div><div class="scroll" id="hrList"></div></div>
</div>"""

CSS = """
.panes.hr{grid-template-columns:minmax(0,.72fr) minmax(0,1.28fr);height:min(680px,82vh)}
.hr-req{padding:4px 18px 18px}
.cr{display:grid;grid-template-columns:auto 1fr auto;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid var(--wl);font-size:14.5px;line-height:1.3}
.cr input{appearance:none;width:20px;height:20px;border-radius:5px;box-shadow:inset 0 0 0 2px currentColor;cursor:pointer;display:grid;place-items:center;margin:0}
.cr input:checked{background:var(--ink)}.cr input:checked::after{content:"";width:10px;height:6px;border:2px solid #ffd91a;border-top:0;border-right:0;transform:rotate(-45deg) translate(1px,-1px)}
.cr.off span{opacity:.45;text-decoration:line-through}
.cr button{font-size:11.5px;font-weight:700;padding:5px 8px;border-radius:999px;box-shadow:inset 0 0 0 1.5px var(--wl);white-space:nowrap}
.cr button.must{background:#ffd91a;box-shadow:inset 0 0 0 1.5px #111}
.hr-bud{display:grid;gap:8px;padding:14px 0 6px;font-size:14.5px}
.hr-bud input{width:100%;accent-color:#111}
.hr-add{display:flex;gap:8px;margin-top:10px}
.hr-add input{flex:1;min-width:0;height:38px;border-radius:10px;border:0;background:var(--w2);padding:0 12px;font-size:14px}
.hr-fair{font-size:12.5px;opacity:.6;margin-top:14px;line-height:1.4}
#hrList{padding:10px 14px 16px;position:relative}
.cd{border:1.5px solid var(--wl);border-radius:14px;padding:12px 14px;margin-bottom:8px;background:var(--wbg,#fff);cursor:pointer;transition:border-color .2s}
.cd:hover,.cd.open{border-color:#111}
.cd-t{display:grid;grid-template-columns:28px 1fr auto;gap:12px;align-items:center}
.cd-n{font:800 22px/1 var(--fh);opacity:.35}
.cd-t b{display:block;font-size:15.5px;line-height:1.25}
.cd-t small{font-size:13px;opacity:.62;display:block}
.cd-s{display:grid;justify-items:end;gap:5px;min-width:96px}
.cd-s strong{font:800 26px/1 var(--fh)}
.cd .meter{width:96px;height:5px}.cd .meter i{background:#111}
.cd-g{display:flex;flex-wrap:wrap;gap:5px;margin-top:10px}
.cd-g i{font-style:normal;font-size:12px;line-height:1;padding:5px 8px;border-radius:999px;background:var(--w2);white-space:nowrap}
.cd-g i.y{background:color-mix(in srgb,var(--ok) 16%,transparent)}.cd-g i.n{background:color-mix(in srgb,var(--bad) 12%,transparent)}
.cd-g i.w{background:color-mix(in srgb,var(--warn) 22%,transparent)}
.cd-d{display:none;margin-top:12px;padding-top:12px;border-top:1px dashed var(--wl);font-size:14px;line-height:1.45;cursor:default}
.cd.open .cd-d{display:grid;gap:10px}
.cd-d h5{margin:0 0 4px;font:700 11.5px/1 var(--fb);letter-spacing:.1em;text-transform:uppercase;opacity:.6}
.cd-d ul{margin:0;padding-left:18px}
.cd-b{display:flex;gap:8px;flex-wrap:wrap}
.cd-m{padding:12px;border-radius:10px;background:var(--w2);white-space:pre-line;font-size:14px}
@media (max-width:1000px){.panes.hr{grid-template-columns:1fr;height:auto}#hrList{overflow:visible}.hr-req{overflow:visible}}
@media (max-width:640px){.cd-s{min-width:64px}.cd .meter{width:64px}.cd-t{grid-template-columns:20px 1fr auto;gap:8px}}
"""

JS = r"""
(function(){var K=AIK,$=K.$,esc=K.esc,
CR=[{k:'b2b',t:'Опыт B2B-продаж от 2 лет',s:'B2B от 2 лет',m:'B2B-продажи',g:'опыт B2B-продаж от двух лет',must:1,on:1,q:'Какие B2B-сделки вели сами от первого контакта до оплаты?'},
 {k:'crm',t:'Работа в CRM: amoCRM или Битрикс24',s:'CRM',m:'работа в CRM',g:'опыт работы в CRM',on:1,q:'Как вели воронку и какие отчёты смотрели в CRM?'},
 {k:'cold',t:'Холодные звонки и поиск клиентов',s:'холодные звонки',m:'холодный поиск клиентов',g:'опыт холодного поиска клиентов',on:1,q:'Сколько холодных контактов в день и какая конверсия во встречу?'},
 {k:'it',t:'Опыт продаж IT или SaaS',s:'IT или SaaS',m:'продажи IT-продуктов',g:'опыт продаж IT-продуктов',on:1,q:'Какие IT-продукты продавали и кому?'},
 {k:'long',t:'Длинные сделки от 1 млн ₽',s:'сделки от 1 млн ₽',m:'длинные сделки',g:'опыт длинных сделок от миллиона',on:1,q:'Опишите самую длинную сделку: сколько людей согласовывало покупку?'},
 {k:'eng',t:'Английский от B1',s:'английский B1',m:'английский',g:'рабочий английский',on:0,q:'Готовы провести часть интервью на английском?'},
 {k:'office',t:'Офис в Москве 3 дня в неделю',s:'офис в Москве',m:'',g:'возможность работать из офиса в Москве',on:1,q:'Подходит ли гибридный график: 3 дня в офисе?'}],
C=[{n:'Анна К.',r:'Менеджер по работе с ключевыми клиентами, облачная телефония',y:5,sal:160,has:['b2b','crm','it','long','office','eng'],jobs:1,tx:'Продажи облачной АТС среднему бизнесу, сделки 1–4 млн ₽, цикл 2–3 месяца. amoCRM, тендеры по 223-ФЗ, английский B2.'},
 {n:'Тимур С.',r:'Менеджер по продажам, оптовая торговля стройматериалами',y:4,sal:130,has:['b2b','crm','cold','office'],jobs:2,tx:'Опт стройматериалов, холодные звонки застройщикам, 60 звонков в день. Битрикс24. План выполнял 11 месяцев из 12.'},
 {n:'Ольга В.',r:'Менеджер по продажам SaaS для ресторанов',y:3,sal:150,has:['b2b','crm','cold','it','office'],jobs:1,tx:'Продажа сервиса учёта для ресторанов: холодный поиск, демонстрации, сделки 200–600 тыс. ₽. amoCRM, вебинары для клиентов.'},
 {n:'Денис М.',r:'Руководитель группы продаж, интегратор 1С',y:7,sal:210,has:['b2b','crm','it','long','office'],jobs:2,tx:'Внедрение 1С в производственных компаниях, сделки до 12 млн ₽, тендеры, работа с медицинскими холдингами. Битрикс24.'},
 {n:'Карина Л.',r:'Менеджер по продажам, фитнес-клуб',y:0,sal:90,has:['crm','cold','office'],jobs:3,tx:'Продажа абонементов частным клиентам, входящие и холодные звонки. amoCRM. Опыта работы с компаниями нет.'},
 {n:'Игорь П.',r:'Менеджер по развитию, логистическая компания',y:2,sal:140,has:['b2b','cold','long'],jobs:1,tx:'Поиск грузовладельцев, договоры на перевозки от 1 млн ₽ в год. Работает удалённо из Казани, переезд не рассматривает. CRM не вели, таблицы.'},
 {n:'Мария Д.',r:'Аккаунт-менеджер, digital-агентство',y:3,sal:145,has:['b2b','crm','it','eng','office'],jobs:3,tx:'Ведение клиентов агентства, допродажи, английский C1. amoCRM. Холодным поиском не занималась, три места работы за три года.'},
 {n:'Сергей Н.',r:'Торговый представитель, FMCG',y:1,sal:120,has:['crm','office','cold'],jobs:2,tx:'Маршрутные продажи в розницу, работа с магазинами и небольшим оптом, 1 год с юрлицами. Мобильная CRM.'}],
bud=150,scored=false,list=$('#hrList'),open=null;
function stem(w){w=w.toLowerCase();return w.length>5?w.slice(0,-2):w}
function hasC(c,cr){if(cr.custom)return cr.words.every(function(w){return(c.tx+' '+c.r).toLowerCase().indexOf(w)>=0});if(cr.k==='b2b')return c.y>=2;return c.has.indexOf(cr.k)>=0}
function calc(c){var tot=0,got=0,miss=[],hit=[],mustFail=0;CR.forEach(function(cr){if(!cr.on)return;var w=cr.must?3:1.5,ok=hasC(c,cr);tot+=w;if(ok){got+=w;hit.push(cr)}else{miss.push(cr);if(cr.must)mustFail=1}});
 var s=tot?Math.round(got/tot*100):0,over=c.sal>bud?Math.round((c.sal-bud)/bud*100):0;if(over>0)s=Math.max(0,s-Math.min(25,over));if(mustFail)s=Math.min(s,40);
 c.s=s;c.hit=hit;c.miss=miss;c.over=over;c.mf=mustFail;c.v=mustFail?['Не подходит','bad']:s>=75&&over<=15?['Пригласить','ok']:s>=50?['В резерв','warn']:['Не подходит','bad'];return c}
function short(x){return x.s||x.t}
function slot(n){var d=new Date(),k=0;while(k<n){d.setDate(d.getDate()+1);if(d.getDay()%6)k++}return['','в понедельник','во вторник','в среду','в четверг','в пятницу'][d.getDay()]+', '+d.getDate()+' '+['января','февраля','марта','апреля','мая','июня','июля','августа','сентября','октября','ноября','декабря'][d.getMonth()]}
function draw(c,i){var el=c.el;if(!el){el=c.el=document.createElement('div');el.className='cd';list.appendChild(el)}
 var tags=scored?c.hit.map(function(x){return'<i class="y">✓ '+esc(short(x))+'</i>'}).join('')+c.miss.map(function(x){return'<i class="n">✕ '+esc(short(x))+'</i>'}).join('')+(c.over>0?'<i class="w">оклад выше бюджета на '+c.over+'%</i>':'')+(c.jobs>=3?'<i class="w">3 места работы за 3 года</i>':''):'';
 var qs=!scored?'':c.miss.filter(function(x){return!x.custom}).slice(0,3).map(function(x){return'<li>'+esc(x.q)+'</li>'}).join('')+(c.jobs>=3?'<li>Что было причиной смены работы в последние три года?</li>':'')+(c.over>0?'<li>Из чего складываются ожидания по окладу '+c.sal+' 000 ₽?</li>':'');
 el.innerHTML='<div class="cd-t"><span class="cd-n">'+(scored?i+1:'·')+'</span><div><b>'+esc(c.n)+'</b><small>'+esc(c.r)+' · '+(c.y?c.y+' '+(c.y===1?'год':c.y<5?'года':'лет')+' в B2B':'без опыта B2B')+' · '+c.sal+' 000 ₽</small></div>'+
  '<div class="cd-s">'+(scored?'<strong>'+c.s+'</strong><div class="meter"><i style="width:'+c.s+'%"></i></div><span class="tag '+c.v[1]+'">'+c.v[0]+'</span>':'<span class="tag">не разобран</span>')+'</div></div>'+
  (scored?'<div class="cd-g">'+tags+'</div><div class="cd-d"><div><h5>Из резюме</h5>'+esc(c.tx)+'</div>'+(qs?'<div><h5>Что уточнить на интервью</h5><ul>'+qs+'</ul></div>':'')+
  '<div class="cd-b"><button type="button" class="btn-s" data-m="inv">Написать приглашение</button><button type="button" class="btn-s g" data-m="no">Вежливый отказ</button></div><div class="cd-m" hidden></div></div>':'');
 el.classList.toggle('open',open===c)}
function order(anim){var first={};C.forEach(function(c){if(c.el)first[c.n]=c.el.getBoundingClientRect().top});
 var L=scored?C.slice().sort(function(a,b){return b.s-a.s||a.sal-b.sal}):C;L.forEach(function(c,i){draw(c,i);list.appendChild(c.el)});
 if(anim&&K.speed)L.forEach(function(c){var d=first[c.n]-c.el.getBoundingClientRect().top;if(d){c.el.animate([{transform:'translateY('+d+'px)'},{transform:'none'}],{duration:480,easing:'cubic-bezier(.2,.8,.2,1)'})}});
 if(scored){var inv=C.filter(function(c){return c.v[0]==='Пригласить'}).length;$('#hrCnt').textContent='пригласить: '+inv+' из '+C.length;$('#hrSt').textContent='разобрано '+C.length+' откликов';return inv}}
function crs(){$('#hrCr').innerHTML=CR.map(function(cr,i){return'<label class="cr'+(cr.on?'':' off')+'"><input type="checkbox" data-i="'+i+'"'+(cr.on?' checked':'')+'><span>'+esc(cr.t)+'</span><button type="button" data-must="'+i+'" class="'+(cr.must?'must':'')+'">'+(cr.must?'обязательно':'желательно')+'</button></label>'}).join('');$('#hrBv').textContent='до '+bud+' 000 ₽'}
function re(){C.forEach(calc);order(true)}
$('#ws').addEventListener('click',function(ev){var t=ev.target,m;
 if(t.dataset.must){ev.preventDefault();var cr=CR[+t.dataset.must];cr.must=cr.must?0:1;crs();if(scored)re();return}
 if(m=t.dataset.m){var c=open,box=t.closest('.cd-d').querySelector('.cd-m'),nm=c.n.split(' ')[0];box.hidden=false;box.textContent='';
  var best=c.hit.filter(function(x){return x.m}).slice(0,2).map(function(x){return x.m}).join(' и ');
  var txt=m==='inv'?nm+', здравствуйте! Это команда найма «Орбиты». Посмотрели ваш отклик на вакансию «Менеджер по продажам B2B» — нам близок ваш опыт'+(best?': '+best:'')+'.\n\nПредлагаю созвониться на 30 минут и познакомиться: '+slot(1)+' в 11:00 или '+slot(2)+' в 16:00. Какое время удобнее?'
   :nm+', здравствуйте! Спасибо за отклик на вакансию «Менеджер по продажам B2B» и за время, которое вы на него потратили.\n\nСейчас мы ищем кандидата, у которого уже есть '+(c.miss.length?c.miss.slice(0,2).map(function(x){return x.g||('опыт: '+x.t.toLowerCase())}).join(' и '):'более близкий к нашему продукту опыт')+', поэтому не готовы пригласить вас на интервью. Резюме сохраним и напишем, если появится подходящая вакансия. Успехов в поиске!';
  K.stream(box,txt,16);K.log([m==='inv'?'✉️':'🕊',m==='inv'?'Приглашение: '+c.n:'Отказ: '+c.n,m==='inv'?'оценка '+c.s+' · два слота на выбор':'оценка '+c.s+' · письмо с причиной',m==='inv'?'Письмо':'Отказ']);return}
 var cd=t.closest('.cd');if(cd&&scored&&!t.closest('.cd-d')){var c2=C.filter(function(x){return x.el===cd})[0];open=open===c2?null:c2;C.forEach(function(x){x.el.classList.toggle('open',open===x)})}});
$('#ws').addEventListener('change',function(ev){var t=ev.target;if(t.dataset.i){CR[+t.dataset.i].on=t.checked?1:0;crs();if(scored)re()}});
$('#hrB').addEventListener('input',function(){bud=+this.value;$('#hrBv').textContent='до '+bud+' 000 ₽';if(scored)re()});
$('#hrAdd').addEventListener('submit',function(ev){ev.preventDefault();var v=$('#hrNew').value.trim();if(v.length<3)return;$('#hrNew').value='';
 CR.push({t:v,on:1,custom:1,words:v.split(/[\s,]+/).filter(function(w){return w.length>2}).map(stem),q:''});crs();if(scored)re()});
crs();order(false);
K.demo=async function(){for(var i=0;i<C.length;i++){var c=C[i];c.el.style.borderColor='#111';$('#hrSt').textContent='читаю резюме: '+c.n;await K.wait(330);c.el.style.borderColor=''}
 scored=true;C.forEach(calc);var inv=order(true);K.log(['🧑‍💼','Разбор откликов: менеджер B2B','8 резюме · пригласить: '+inv,'Отобрано'])};
})();
"""


def cfg() -> dict:
    return {
        "slug": "ai/hr", "brand": "Отбор", "logoIcon": "О",
        "title": "Отбор — ИИ-ассистент HR: оценка резюме по требованиям вакансии",
        "desc": "ИИ-ассистент рекрутера: читает отклики, оценивает каждого кандидата по требованиям вакансии, объясняет оценку, "
                "готовит вопросы к интервью и письма с приглашением или отказом.",
        "theme": theme(bg="#ffd91a", ink="#111111", soft="#3b3515", mut="#6e6325", line="rgba(17,17,17,.16)", line2="#111111",
                       card="#ffffff", ac="#111111", aci="#ffd91a", act="#111111", fh='"Sofia Sans Condensed",sans-serif',
                       fb='"Onest",sans-serif', hw="800", ht="-.01em", rb="999px", rc="18px", rs="26px", rw="22px",
                       wbg="#ffffff", wsh="0 0 0 2px #111,0 40px 80px -40px rgba(0,0,0,.5)", cbg="#111111", cink="#ffd91a",
                       kc="#111111", rcx="#111111"),
        "fonts": [("Sofia Sans Condensed", "sofia-sans-condensed", [800], "normal"), ("Onest", "onest", [400, 500, 600, 700], "normal")],
        "css": CSS + ".hero h1{text-transform:uppercase;font-size:clamp(52px,8.6vw,132px);line-height:.88;letter-spacing:-.015em}"
                     ".hero h1 em{color:#111;background:#fff;padding:0 .12em;box-decoration-break:clone;-webkit-box-decoration-break:clone}"
                     "h2{text-transform:uppercase;font-size:clamp(38px,5.4vw,76px);line-height:.92}"
                     ".how b,.feat b{font-size:28px;text-transform:uppercase;line-height:1}.hs b,.res b{font-size:clamp(40px,4.6vw,64px)}"
                     ".feat i{background:#ffd91a}.cta-b .btn{background:#ffd91a;color:#111}.res{background:#111;box-shadow:0 0 0 2px #111}"
                     ".res div{background:#fff}.panel{box-shadow:0 0 0 2px #111}.logo{font-size:28px;text-transform:uppercase}"
                     ".logo i{border-radius:50%}.ints span{box-shadow:inset 0 0 0 1.5px #111;background:transparent}"
                     ".rowx em{background:#ffd91a;color:#111}.top{background:#ffd91a}.kick{font-weight:700}",
        "hero": {"kicker": "ИИ-ассистент HR · отбор резюме", "h1": "Из сотни откликов — <em>пятеро, с кем стоит говорить</em>",
                 "lead": "Отбор читает каждое резюме, сверяет с требованиями вакансии и показывает рейтинг с объяснением: что совпало, "
                         "чего не хватает и о чём спросить на интервью. Рекрутер тратит время на людей, а не на чтение.",
                 "cta": "Разобрать отклики",
                 "stats": [("8 сек", "на одно резюме"), ("100%", "откликов прочитано, а не первые 30"), ("0", "решений без объяснения")]},
        "demo": {"type": "custom", "html": HTML, "js": JS,
                 "note": "Отбор работает: снимите требование, сделайте его обязательным, поменяйте бюджет или добавьте своё — рейтинг пересчитается. Нажмите на кандидата"},
        "howTitle": "Как Отбор читает отклики",
        "howLead": "Каждое резюме проходит один и тот же путь. Оценку всегда можно раскрыть и увидеть, из чего она сложилась.",
        "how": [("Разбирает резюме", "Достаёт опыт, сферу, навыки, формат работы и ожидания по окладу из любого формата: файл, ссылка, отклик с сайта."),
                ("Сверяет с требованиями", "Обязательные требования весят больше желательных. Нет обязательного — кандидат не проходит, и видно почему."),
                ("Объясняет оценку", "Показывает, что совпало и чего не хватает. Спорные места помечает вопросом к интервью, а не минусом."),
                ("Готовит следующий шаг", "Пишет приглашение с двумя слотами или вежливый отказ с причиной. Отправляет рекрутер.")],
        "featsTitle": "Что Отбор делает за рекрутера",
        "feats": [("📥", "Читает все отклики", "Сто резюме за пятнадцать минут. Сильный кандидат не теряется на третьей странице списка."),
                  ("🎯", "Рейтинг по вашим требованиям", "Требования и их вес задаёте вы. Поменяли — рейтинг пересчитался сразу."),
                  ("🔍", "Оценка с объяснением", "Под каждой цифрой — совпадения и пробелы из текста резюме. Никакого чёрного ящика."),
                  ("❓", "Вопросы к интервью", "По каждому пробелу и спорному месту готов вопрос, чтобы проверить это в разговоре."),
                  ("✉️", "Письма кандидатам", "Приглашение с конкретными слотами и отказ с человеческой причиной вместо молчания."),
                  ("⚖️", "Одинаковые правила", "Все резюме оцениваются по одним критериям. Пол, возраст и фото в оценку не попадают.")],
        "control": {"title": "Решает рекрутер, а не алгоритм",
                    "lead": "Отбор расставляет отклики по порядку и объясняет почему. Кого звать и кому отказать, решает человек.",
                    "rules": [("Никому не отказывает сам", "Письмо с отказом — это черновик. Отправляет его рекрутер, когда согласен с причиной."),
                              ("Не оценивает по личным данным", "Пол, возраст, фото, семейное положение и национальность не читаются вовсе."),
                              ("Не штрафует за спорное", "Частую смену работы и пробелы помечает вопросом к интервью, а не снижает балл."),
                              ("Показывает основание", "Любую оценку можно раскрыть до строк резюме, на которых она основана.")],
                    "panel": {"name": "Отбор · журнал найма",
                              "kpi": [(64, "резюме сегодня"), ("9", "приглашений"), ("3", "вакансии в работе")],
                              "rows": [("✉️", "Приглашение: Елена Р.", "вакансия «Бухгалтер» · оценка 86", "Письмо"),
                                       ("🧑‍💼", "Разбор откликов: аналитик данных", "23 резюме · пригласить: 4", "Отобрано"),
                                       ("🕊", "Отказ: Павел Г.", "нет обязательного опыта · письмо с причиной", "Отказ")]}},
        "resTitle": "Что получает команда найма",
        "results": [("−76%", "времени на первичный отбор"), ("100%", "откликов получают ответ"),
                    ("2 дня", "от отклика до интервью вместо недели"), ("0", "сильных кандидатов, потерянных в списке")],
        "ints": ["hh.ru", "Хантфлоу", "Talantix", "Potok", "Авито Работа", "Google Календарь", "Telegram", "Почта"],
        "faq": [("Ассистент сам решает, кого не брать?", "Нет. Он ранжирует и объясняет, а решение принимает рекрутер. Ни одно письмо "
                                                         "кандидату не уходит без человека."),
                ("Как избежать предвзятости?", "Ассистент не читает пол, возраст, фото и другие личные данные и оценивает всех по одним "
                                               "критериям. Спорные моменты он выносит в вопросы к интервью, а не в оценку.")] + FAQ_COMMON,
        "ctaTitle": "Разберите отклики за минуту", "ctaBtn": "Открыть отбор",
    }
