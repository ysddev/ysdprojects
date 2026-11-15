"""«Смена» — сервис графиков смен для кафе, магазинов и салонов: живой макет графика (смены перетаскиваются),
калькулятор экономии, тарифы помесячно и за год. Продуктовый лендинг без фото — интерфейс и есть картинка."""

ROWS = [("Аня", "бариста"), ("Тимур", "бариста"), ("Оля", "кассир"), ("Денис", "повар"), ("Мадина", "повар"), ("Глеб", "курьер")]

APP = r"""
<div class="app" id="app">
 <div class="ahd"><b>График · кофейня на Ленина</b><span class="aw" id="aWarn">Все смены закрыты</span></div>
 <div class="agrid" id="aGrid"></div>
 <div class="aft"><span>Перетащите смену на другой день — «Смена» проверит переработки и пересчитает фонд</span><b id="aFund"></b></div>
</div>
"""

ROI = r"""
<div class="roi rv">
 <div class="panel">
  <div class="rng"><div class="rh"><span>Сотрудников на сменах</span><b id="rEmpV">24</b></div><input type="range" id="rEmp" min="3" max="200" value="24"></div>
  <div class="rng" style="margin-top:24px"><div class="rh"><span>Часов в неделю на график и замены</span><b id="rHrsV">6</b></div><input type="range" id="rHrs" min="1" max="30" value="6"></div>
  <div class="rng" style="margin-top:24px"><div class="rh"><span>Стоимость часа управляющего</span><b id="rRateV">650 ₽</b></div><input type="range" id="rRate" min="300" max="2000" step="50" value="650"></div>
 </div>
 <div class="panel rres"><span class="kick">В месяц сэкономите</span><div class="big" id="rSave"></div><p id="rTxt"></p></div>
</div>
"""

PRICE = r"""
<div class="pt rv"><div class="seg" id="pPer"><button type="button" data-v="m" class="on">Помесячно</button><button type="button" data-v="y">За год −17%</button></div></div>
<div class="plans" id="plans"></div>
"""

CSS = r"""
.hero .g{grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr)}
.hero h1 em{font-style:normal;color:var(--ac)}
.hph{background:none;overflow:visible;aspect-ratio:auto}
.app{background:#fff;border-radius:22px;box-shadow:0 40px 80px -40px rgba(30,20,90,.45),0 0 0 1px var(--line);overflow:hidden;font-size:13px}
.ahd{display:flex;justify-content:space-between;gap:10px;align-items:center;padding:14px 18px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.ahd b{font-size:14px}.aw{font-size:12.5px;padding:5px 10px;border-radius:99px;background:#e6f7ee;color:#167a46;transition:background .3s,color .3s}
.aw.bad{background:#fff0e8;color:#b4471c}
.agrid{display:grid;grid-template-columns:96px repeat(7,minmax(0,1fr))}
.agrid>div{border-bottom:1px solid var(--line);border-right:1px solid var(--line);min-height:44px;padding:5px;position:relative}
.agrid .h{font-weight:600;color:var(--mut);font-size:12px;min-height:30px;text-align:center}
.agrid .n{font-weight:600;font-size:13px;display:grid;align-content:center}.agrid .n small{font-weight:400;color:var(--mut);font-size:11.5px}
.agrid .c.ov{background:#f2efff}
.sh{display:block;border-radius:8px;padding:5px 6px;font-size:11.5px;font-weight:600;line-height:1.2;cursor:grab;user-select:none;touch-action:none;color:#fff}
.sh.m{background:#5b4cf0}.sh.e{background:#ff7a59}.sh.d{background:#1fb47a}
.sh.dr{opacity:.4}
.aft{display:flex;justify-content:space-between;gap:12px;padding:12px 18px;color:var(--mut);font-size:12.5px;flex-wrap:wrap}.aft b{color:var(--ink)}
.feats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.feats div{padding:24px;border-radius:20px;background:var(--card);box-shadow:0 0 0 1px var(--line)}
.feats i{display:inline-block;font-style:normal;font-size:12.5px;font-weight:600;padding:4px 10px;border-radius:99px;background:color-mix(in srgb,var(--ac) 12%,transparent);color:var(--ac);margin-bottom:14px}
.feats h3{font-size:21px;margin-bottom:8px}.feats p{color:var(--soft);font-size:15px}
.roi{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:16px;align-items:stretch}
.rres{background:var(--ac);color:#fff;box-shadow:none;display:grid;align-content:center;gap:10px}.rres .kick{color:#cfc9ff}.rres p{color:#e6e3ff}
.pt{display:flex;justify-content:center;margin-bottom:26px}
.plans{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.plan{border-radius:22px;padding:28px;background:var(--card);box-shadow:0 0 0 1px var(--line);display:flex;flex-direction:column;gap:14px}
.plan.hot{box-shadow:0 0 0 2px var(--ac);position:relative}
.plan.hot::before{content:"Выбирают чаще";position:absolute;top:-12px;left:28px;background:var(--ac);color:#fff;font-size:12px;font-weight:600;padding:4px 10px;border-radius:99px}
.plan h3{font-size:22px}.plan .pp{font:700 40px/1 var(--fh);letter-spacing:-.03em}.plan .pp small{font:400 15px var(--fb);color:var(--mut);letter-spacing:0}
.plan ul{margin:0;padding:0;list-style:none;display:grid;gap:8px;color:var(--soft);font-size:15px}
.plan li::before{content:"✓ ";color:var(--ac);font-weight:700}
.plan .btn{margin-top:auto}
@media (max-width:980px){.hero .g{grid-template-columns:minmax(0,1fr)}.hph{overflow:hidden}.feats,.plans{grid-template-columns:1fr}.roi{grid-template-columns:1fr}}
@media (max-width:620px){.agrid{grid-template-columns:70px repeat(7,minmax(34px,1fr));font-size:11px}.app{overflow-x:auto}.agrid{min-width:520px}.sh{font-size:10px;padding:4px}}
"""

JS = r"""
(function(){var $=function(s){return document.getElementById(s)};var R=window.SITE.rows,D=['Пн','Вт','Ср','Чт','Пт','Сб','Вс'];
var S={0:{0:'m',1:'m',3:'m',4:'e'},1:{1:'e',2:'e',4:'m',5:'m',6:'e'},2:{0:'d',2:'d',3:'d',5:'d'},3:{0:'d',1:'d',4:'d'},4:{2:'d',3:'d',6:'d'},5:{4:'e',5:'e',6:'e',0:'e'}};
var LAB={m:'07–15',e:'14–22',d:'10–22'},HRS={m:8,e:8,d:12},RATE=[310,310,280,360,360,250];
function draw(){var h='<div class="h"></div>'+D.map(function(d){return'<div class="h">'+d+'</div>'}).join('');var bad=0,fund=0;
 R.forEach(function(r,i){var wk=0;Object.keys(S[i]).forEach(function(k){wk+=HRS[S[i][k]]});var over=wk>40;if(over)bad++;
  h+='<div class="n">'+r[0]+'<small>'+r[1]+' · '+wk+' ч</small></div>';
  for(var d=0;d<7;d++){var t=S[i][d];fund+=t?HRS[t]*RATE[i]:0;h+='<div class="c'+(over&&t?' ov':'')+'" data-r="'+i+'" data-d="'+d+'">'+(t?'<span class="sh '+t+'" data-r="'+i+'" data-d="'+d+'">'+LAB[t]+'</span>':'')+'</div>'}});
 $('aGrid').innerHTML=h;var w=$('aWarn');w.textContent=bad?'Переработка: '+bad+' '+plural(bad,'сотрудник','сотрудника','сотрудников')+' больше 40 ч':'Все смены закрыты, переработок нет';w.classList.toggle('bad',!!bad);
 $('aFund').textContent='Фонд недели: '+rub(fund)}
draw();var drag=null,g=$('aGrid');
g.addEventListener('pointerdown',function(e){var s=e.target.closest('.sh');if(!s)return;drag={r:+s.dataset.r,d:+s.dataset.d,el:s};s.classList.add('dr');s.setPointerCapture(e.pointerId)});
g.addEventListener('pointerup',function(e){if(!drag)return;var el=document.elementFromPoint(e.clientX,e.clientY);var c=el&&el.closest('.c');
 if(c&&+c.dataset.r===drag.r&&+c.dataset.d!==drag.d&&!S[drag.r][+c.dataset.d]){S[drag.r][+c.dataset.d]=S[drag.r][drag.d];delete S[drag.r][drag.d]}
 else if(c&&+c.dataset.r!==drag.r){toast('Смену можно двигать только по дням одного сотрудника')}
 drag=null;draw()});
// экономия
function roi(){var e=+$('rEmp').value,h=+$('rHrs').value,r=+$('rRate').value;$('rEmpV').textContent=e;$('rHrsV').textContent=h;$('rRateV').textContent=rub(r);
 var saveH=h*4.3*.72,save=saveH*r+e*90;$('rSave').textContent=rub(Math.round(save/10)*10);
 var cost=e<=15?1490:e<=60?3990:3990+Math.ceil((e-60)/10)*590;
 $('rTxt').textContent=Math.round(saveH)+' '+plural(Math.round(saveH),'час','часа','часов')+' управляющего и меньше переработок по табелю. Тариф на '+e+' '+plural(e,'сотрудника','сотрудников','сотрудников')+' — '+rub(cost)+' в месяц: окупается в '+Math.max(1.5,save/cost).toFixed(1).replace('.',',')+' раза.'}
['rEmp','rHrs','rRate'].forEach(function(id){$(id).addEventListener('input',roi)});roi();
// тарифы
var P=[['Точка',1490,'до 15 сотрудников, одна точка',['график и замены','табель для бухгалтера','приложение для сотрудников']],
 ['Сеть',3990,'до 60 сотрудников, до 5 точек',['всё из «Точки»','переработки и бюджет фонда','обмен сменами между точками','выгрузка в зарплату'],1],
 ['Компания',9990,'без ограничений',['всё из «Сети»','роли и согласования','API и единый вход','персональный менеджер']]];
var per='m';function plans(){$('plans').innerHTML=P.map(function(p){var pr=per=='y'?Math.round(p[1]*10/12/10)*10:p[1];
 return'<div class="plan'+(p[4]?' hot':'')+'"><h3>'+p[0]+'</h3><div class="pp">'+rub(pr)+' <small>/ мес'+(per=='y'?', при оплате за год':'')+'</small></div><p style="color:var(--mut);font-size:14.5px">'+p[2]+'</p><ul>'+p[3].map(function(x){return'<li>'+x+'</li>'}).join('')+'</ul><a class="btn'+(p[4]?'':' g')+'" href="#lead">Попробовать 14 дней</a></div>'}).join('')}
$('pPer').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;per=b.dataset.v;[].forEach.call(this.children,function(x){x.classList.toggle('on',x===b)});plans()});plans();
})();
"""

FEATS = ('<div class="feats">' + "".join(f'<div class="rv"><i>{a}</i><h3>{b}</h3><p>{c}</p></div>' for a, b, c in [
    ("Замены", "Заболел — замена за 4 минуты", "Сотрудник жмёт «не могу выйти», «Смена» предлагает свободных коллег с нужной ролью, первый согласившийся получает смену."),
    ("Табель", "Отметка по геолокации", "Приход и уход — кнопкой в приложении у точки. Опоздания видны сразу, табель для бухгалтера собирается сам."),
    ("Бюджет", "Фонд недели под контролем", "Видно, сколько стоит график ещё до публикации. Переработки и ночные часы подсвечиваются красным."),
    ("Пожелания", "Сотрудники отмечают удобные дни", "График учитывает пожелания и учёбу. Меньше «я не могу в субботу» после публикации."),
    ("Сеть", "Обмен людьми между точками", "Не хватает бариста на Ленина — «Смена» предложит того, кто свободен на Мира в 12 минутах."),
    ("Выгрузка", "Зарплата без пересчёта вручную", "Часы, ставки и надбавки уходят в зарплатную программу одним файлом.")]) + "</div>")


def cfg() -> dict:
    return {
        "slug": "smena", "brand": "Смена", "legal": "ООО «Смена», Новосибирск", "favLetter": "С",
        "logo": '<svg viewBox="0 0 32 32"><rect width="32" height="32" rx="9" fill="#5b4cf0"/><rect x="7" y="9" width="8" height="5" rx="2" fill="#fff"/><rect x="17" y="9" width="8" height="5" rx="2" fill="#ff9d80"/><rect x="7" y="17" width="12" height="5" rx="2" fill="#7ee0b6"/></svg>',
        "title": "Смена — графики смен для кафе, магазинов и салонов",
        "desc": "Сервис графиков смен: замены за 4 минуты, табель по геолокации, бюджет фонда до публикации графика. "
                "Тарифы от 1 490 ₽ в месяц, 14 дней бесплатно.",
        "theme": {"bg": "#f7f6fd", "ink": "#16132e", "soft": "#4c4867", "mut": "#8a87a3", "line": "#e6e3f3", "line2": "#d3cfe8",
                  "card": "#ffffff", "alt": "#efecfb", "ac": "#5b4cf0", "aci": "#ffffff", "fh": '"Wix Madefor Display",sans-serif',
                  "fb": '"Wix Madefor Text",sans-serif', "hw": "700", "ht": "-.03em", "dk": "#16132e", "dki": "#fff", "rc": "22px", "rb": "14px", "h1s": "clamp(40px,4.8vw,70px)"},
        "fonts": [("Wix Madefor Display", "wix-madefor-display", [600, 700], "normal"), ("Wix Madefor Text", "wix-madefor-text", [400, 600], "normal")],
        "images": {},
        "phone": ("+73830000000", "+7 383 000-00-00"),
        "mail": "hello@smena.ysdprojects.space",
        "nav": [("features", "Возможности"), ("roi", "Экономия"), ("price", "Тарифы"), ("faq", "Вопросы")],
        "topCta": "Попробовать бесплатно",
        "hero": {"kicker": "Для кафе, магазинов и салонов", "h1": "График смен за <em>12 минут</em> в неделю, а не за вечер",
                 "lead": "«Смена» собирает график с учётом пожеланий, находит замену заболевшему и считает фонд до публикации. "
                         "1 270 точек уже не рисуют графики в таблице.",
                 "cta": "Попробовать 14 дней", "go": "lead", "go2": ("features", "Как работает"),
                 "points": ["Без карты для пробного периода", "Перенесём график из таблицы за вас", "Приложение для сотрудников"],
                 "art": APP},
        "data": {"rows": ROWS},
        "sections": [
            {"type": "html", "id": "features", "kick": "Возможности", "h2": "Всё, на что уходит вечер управляющего", "html": FEATS},
            {"type": "html", "id": "roi", "kick": "Экономия", "h2": "Посчитайте, сколько «Смена» вернёт в месяц", "alt": True,
             "lead": "В среднем управляющий тратит на график и замены 6 часов в неделю. После «Смены» — меньше двух.", "html": ROI},
            {"type": "html", "id": "price", "kick": "Тарифы", "h2": "Платите за точки, а не за каждого сотрудника", "html": PRICE},
            {"type": "steps", "id": "start", "kick": "Старт", "h2": "Запуск за один день", "alt": True,
             "items": [("Заявка", "Оставляете контакт — пришлём доступ за 10 минут.", "0 ₽"),
                       ("Перенос", "Пришлите таблицу с графиком — перенесём сотрудников и смены сами.", "в тот же день"),
                       ("Приложение", "Сотрудники ставят приложение по ссылке из сообщения.", "2 минуты на человека"),
                       ("Первый график", "Публикуете — сотрудники видят смены и могут меняться.", "12 минут")]},
            {"type": "faq", "id": "faq", "kick": "Вопросы", "h2": "Что спрашивают владельцы",
             "items": [("Нужно ли сотрудникам ставить приложение?", "Желательно, но не обязательно: график и замены приходят и в мессенджер, и по SMS."),
                       ("Подойдёт для круглосуточной работы?", "Да, смены через полночь, ночные часы и надбавки считаются отдельно."),
                       ("Где хранятся данные?", "На серверах в России, персональные данные — по 152-ФЗ. Договор и NDA — по запросу."),
                       ("Что будет после 14 дней?", "Выбираете тариф или ничего не делаете — доступ просто станет только для чтения, данные не удалим.")]},
        ],
        "contact": {"kick": "Пробный период", "h2": "14 дней бесплатно — с переносом вашего графика",
                    "lead": "Оставьте контакт — пришлём доступ и поможем перенести текущий график из таблицы.",
                    "rows": [("Поддержка", "ежедневно 8:00–23:00 по Москве"), ("Телефон", "+7 383 000-00-00"), ("Офис", "Новосибирск, Красный проспект, 77")]},
        "form": {"fields": [("name", "Имя", "text", "", True), ("phone", "Телефон", "tel", "+7", True),
                            ("biz", "Бизнес", "select", ["Кафе или ресторан", "Магазин", "Салон или студия", "Другое"]), ("pts", "Точек", "select", ["1", "2–5", "6–20", "больше 20"])],
                 "ok": "Готово! Доступ придёт в SMS в течение 10 минут.", "btn": "Получить доступ"},
        "css": CSS, "js": JS,
    }
