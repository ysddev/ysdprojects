"""«Кронверк» — заказная разработка для бизнеса (Санкт-Петербург): оценка проекта по функциям, кейсы с цифрами,
как устроена работа спринтами. Тёмная техническая эстетика, моноширинные подписи."""

IMAGES = {
    "team": ("1522071820081-009f0129c71c", 16, 10, "800,1400"),
    "code": ("1629904853893-c2c8981a1dc5", 4, 5, "700,1100"),
    "meet": ("1541746972996-4e0b0f43e02a", 3, 2, "700,1100"),
    "desk": ("1519241047957-be31d7379a5d", 3, 2, "700,1100"),
    "sun": ("1629904869392-ae2a682d4d01", 3, 2, "700,1100"),
}

LOGO = ('<svg viewBox="0 0 32 32"><path d="M16 2l12 7v14l-12 7-12-7V9z" fill="none" stroke="#7cf0b5" stroke-width="2"/>'
        '<path d="M12 11v10M12 16l7-5M14 15l5 6" stroke="#e8edf2" stroke-width="2" stroke-linecap="round" fill="none"/></svg>')

EST = r"""
<div class="est rv">
 <div class="panel eq">
  <div class="q"><b>Что делаем</b><div class="chips" id="eType"></div></div>
  <div class="q"><b>Платформы</b><div class="chips" id="ePlat"></div></div>
  <div class="q"><b>Функции</b><div class="feat" id="eFeat"></div></div>
 </div>
 <div class="panel er">
  <div class="mono">// оценка</div>
  <div class="erow"><span>Срок до первого релиза</span><b id="eWeeks">—</b></div>
  <div class="bar"><i id="eBar"></i></div>
  <div class="erow"><span>Команда</span><b id="eTeam">—</b></div>
  <div class="erow"><span>Бюджет</span><b id="eSum">—</b></div>
  <pre class="mono plan" id="ePlan"></pre>
  <a class="btn" href="#lead" id="eGo">Обсудить оценку</a>
 </div>
</div>
"""

CSS = r"""
.mono{font:500 13px/1.6 "IBM Plex Mono",monospace;color:var(--ac)}
.hero h1{letter-spacing:-.035em}
.hero h1 em{font-style:normal;color:var(--ac)}
.hph{box-shadow:0 0 0 1px var(--line)}
.hph::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 50%,rgba(11,14,18,.85));pointer-events:none}
.hph .tag{z-index:2;background:rgba(11,14,18,.72);color:#e8edf2;box-shadow:0 0 0 1px rgba(124,240,181,.3)}
.hph .tag b{color:var(--ac)}
.card{background:rgba(255,255,255,.03)}
.card:hover{box-shadow:0 0 0 1px var(--ac)}
.est{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:clamp(14px,2vw,22px);align-items:start}
.eq{display:grid;gap:26px}.eq .q{display:grid;gap:12px}.eq .q>b{font-weight:600}
.feat{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.feat label{display:flex;gap:10px;align-items:flex-start;padding:12px 14px;border-radius:12px;box-shadow:inset 0 0 0 1px var(--line2);cursor:pointer;font-size:14.5px;line-height:1.35}
.feat label:has(input:checked){box-shadow:inset 0 0 0 1.5px var(--ac);background:rgba(124,240,181,.06)}
.feat input{accent-color:var(--ac);margin-top:2px}
.feat small{display:block;color:var(--mut);font:500 12px "IBM Plex Mono",monospace;margin-top:3px}
.er{position:sticky;top:90px;display:grid;gap:14px}
.erow{display:flex;justify-content:space-between;align-items:baseline;gap:12px;padding-bottom:12px;border-bottom:1px solid var(--line)}
.erow span{color:var(--soft);font-size:15px}.erow b{font:600 clamp(22px,2.2vw,30px) var(--fh);text-align:right}
.bar{height:6px;border-radius:3px;background:var(--line)}.bar i{display:block;height:100%;border-radius:3px;background:var(--ac);transition:width .4s;width:0}
.plan{white-space:pre-wrap;margin:6px 0 4px;color:var(--soft);font-size:12.5px}
.er .btn{width:100%}
.case{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.case article{border-radius:20px;padding:26px;box-shadow:0 0 0 1px var(--line);display:grid;gap:14px;align-content:start}
.case .n{font:600 clamp(40px,4vw,56px)/1 var(--fh);color:var(--ac)}
.case h3{font-size:21px}.case p{color:var(--soft);font-size:15px}
.case .st{font:500 12.5px "IBM Plex Mono",monospace;color:var(--mut)}
.stack{display:flex;flex-wrap:wrap;gap:8px;margin-top:clamp(26px,3vw,40px)}
.stack span{font:500 13px "IBM Plex Mono",monospace;padding:7px 12px;border-radius:8px;box-shadow:inset 0 0 0 1px var(--line2);color:var(--soft)}
@media (max-width:860px){.est,.case{grid-template-columns:1fr}.er{position:static}.feat{grid-template-columns:1fr}}
"""

JS = r"""
(function(){var $=function(s){return document.getElementById(s)};
var T=[['web','Веб-сервис',6],['crm','CRM / кабинет',7],['mob','Мобильное приложение',7],['int','Интеграции',4]];
var PL=[['web','Веб',1],['ios','iOS',1.35],['and','Android',1.3],['tg','Telegram Mini App',1.12]];
var F=[['auth','Вход и роли','SSO, права',1],['pay','Оплата','эквайринг, чеки',1.5],['1c','Обмен с учётной системой','двусторонний',2],['chat','Чат и уведомления','push, e-mail',1.2],
 ['rep','Отчёты и дашборды','выгрузки в Excel',1.4],['ai','ИИ-функции','поиск, ассистент',2.2],['map','Карты и логистика','маршруты',1.6],['adm','Админ-панель','контент, справочники',1]];
var t='web',pl={web:1},f={auth:1,adm:1};
$('eType').innerHTML=T.map(function(x){return'<button type="button" data-v="'+x[0]+'" class="'+(x[0]==t?'on':'')+'">'+x[1]+'</button>'}).join('');
$('ePlat').innerHTML=PL.map(function(x){return'<button type="button" data-v="'+x[0]+'" class="'+(pl[x[0]]?'on':'')+'">'+x[1]+'</button>'}).join('');
$('eFeat').innerHTML=F.map(function(x){return'<label><input type="checkbox" value="'+x[0]+'"'+(f[x[0]]?' checked':'')+'><span>'+x[1]+'<small>'+x[2]+'</small></span></label>'}).join('');
$('eType').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;t=b.dataset.v;[].forEach.call(this.children,function(x){x.classList.toggle('on',x===b)});
 if(t=='mob'){pl={ios:1,and:1}}else if(t!='mob'&&!pl.web&&!pl.tg){pl={web:1}}[].forEach.call($('ePlat').children,function(x){x.classList.toggle('on',!!pl[x.dataset.v])});run()});
$('ePlat').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var v=b.dataset.v;if(pl[v]&&Object.keys(pl).length>1){delete pl[v]}else pl[v]=1;b.classList.toggle('on',!!pl[v]);run()});
$('eFeat').addEventListener('change',function(e){f[e.target.value]=e.target.checked;run()});
function run(){var base=T.filter(function(x){return x[0]==t})[0][2];var k=0,plat=0;PL.forEach(function(x){if(pl[x[0]])plat+=x[2]});plat=1+.12*(Object.keys(pl).length-1);
 F.forEach(function(x){if(f[x[0]])k+=x[3]});var w=Math.round((base+k*1.1)*plat);var dev=w<8?2:w<14?3:w<20?4:5;var sum=w*dev*5*11800;
 $('eWeeks').textContent=w+' '+plural(w,'неделя','недели','недель');$('eBar').style.width=Math.min(100,w/30*100)+'%';
 $('eTeam').textContent=dev+' разработчика + дизайнер, аналитик, QA';
 var r=function(x){return Math.round(x/10000)*10000};$('eSum').textContent=rub(r(sum*.9))+' – '+rub(r(sum*1.15));
 var sp=Math.ceil(w/2);$('ePlan').textContent='> спринт 0 · 1 нед · прототип и архитектура\n> спринты 1–'+sp+' · по 2 нед · демо каждую пятницу\n> релиз · неделя '+(w+1)+' · публикация и поддержка 3 мес';
 $('eGo').dataset.v=$('eWeeks').textContent+', '+$('eSum').textContent}
$('eGo').addEventListener('click',function(){var ta=document.querySelector('#lead textarea');if(ta)ta.value='Оценка с сайта: '+this.dataset.v+'. Функции: '+F.filter(function(x){return f[x[0]]}).map(function(x){return x[1]}).join(', ')});
run()})();
"""

CASES = ('<div class="case">' + "".join(
    f'<article class="rv"><div class="st">{st}</div><div class="n">{n}</div><h3>{h}</h3><p>{p}</p></article>' for st, n, h, p in [
        ("сеть клиник · 14 филиалов · 2025", "−38%", "неявок на приём", "Запись, напоминания и перенос визита в мессенджере. Врачи видят расписание и анализы в одном окне."),
        ("логистика · 230 машин · 2025", "4 мин", "вместо 40 на маршрут", "Диспетчерская: заявки, автоматическая раскладка по машинам и статус доставки для клиента по ссылке."),
        ("производство мебели · 2026", "×2,4", "заказов через кабинет дилера", "Кабинет дилера с конфигуратором, остатками со склада и обменом с учётной системой каждые 5 минут."),
    ]) + '</div><div class="stack rv">' + "".join(f"<span>{x}</span>" for x in
    ["Python", "Go", "TypeScript", "React", "Flutter", "PostgreSQL", "Redis", "Kubernetes", "ClickHouse", "LLM-ассистенты"]) + "</div>")


def cfg() -> dict:
    return {
        "slug": "kronverk", "brand": "Кронверк", "legal": "ООО «Кронверк Софт», Санкт-Петербург", "favLetter": "К", "logo": LOGO,
        "title": "Кронверк — заказная разработка веб-сервисов и приложений для бизнеса",
        "desc": "Разработка веб-сервисов, CRM, мобильных приложений и интеграций. Оценка проекта на сайте, спринты по 2 недели, "
                "демо каждую пятницу. Санкт-Петербург.",
        "theme": {"bg": "#0b0e12", "ink": "#e8edf2", "soft": "#a5aeb8", "mut": "#6c7681", "line": "#1f262e", "line2": "#2f3842",
                  "card": "#11161c", "alt": "#0f1318", "ac": "#7cf0b5", "aci": "#06110b", "fh": '"IBM Plex Sans",sans-serif',
                  "fb": '"IBM Plex Sans",sans-serif', "fm": '"IBM Plex Mono",monospace', "hw": "600", "ht": "-.025em", "dk": "#e8edf2", "dki": "#0b0e12",
                  "rc": "18px", "rb": "10px", "fk": '"IBM Plex Mono",monospace', "kls": ".04em", "ktt": "none", "har": "4/5"},
        "fonts": [("IBM Plex Sans", "ibm-plex-sans", [400, 500, 600], "normal"), ("IBM Plex Mono", "ibm-plex-mono", [400, 500], "normal")],
        "images": IMAGES,
        "phone": ("+78120000000", "+7 812 000-00-00"),
        "mail": "hello@kronverk.ysdprojects.space",
        "nav": [("services", "Что делаем"), ("estimate", "Оценка"), ("cases", "Кейсы"), ("process", "Как работаем"), ("faq", "Вопросы")],
        "topCta": "Оценить проект",
        "hero": {"kicker": "// заказная разработка с 2017 года", "h1": "Делаем софт, который <em>окупается</em>, а не просто запускается",
                 "lead": "Веб-сервисы, CRM, мобильные приложения и интеграции с учётными системами для компаний от 50 сотрудников. Показываем рабочую версию "
                         "каждые две недели — вы видите, за что платите.",
                 "cta": "Оценить проект за минуту", "go": "estimate", "go2": ("cases", "Смотреть кейсы"),
                 "points": ["47 инженеров в штате", "Фиксированная цена спринта", "Код и права — ваши"],
                 "img": "code", "alt": "Разработчики за работой", "ar": "4/5",
                 "tag": "<b>83 проекта</b>в продакшене, 9 из них — дольше 5 лет на нашей поддержке"},
        "sections": [
            {"type": "cards", "id": "services", "kick": "// что делаем", "h2": "Четыре направления, одна команда",
             "lead": "Не берём всё подряд: только то, где у нас есть свои наработки и люди с опытом.", "cols": 2,
             "items": [
                 {"t": "Веб-сервисы и платформы", "d": "Личные кабинеты, маркетплейсы услуг, внутренние порталы.", "list": ["нагрузка до 50 000 пользователей онлайн", "SLA 99,9%"], "price": "от 1,4 млн ₽", "unit": "первый релиз"},
                 {"t": "CRM и автоматизация", "d": "Под ваш процесс, а не процесс под коробку.", "list": ["импорт из старой системы", "обучение сотрудников"], "price": "от 980 тыс. ₽", "unit": "первый релиз"},
                 {"t": "Мобильные приложения", "d": "iOS и Android на Flutter — одна кодовая база.", "list": ["публикация в магазинах", "аналитика и push"], "price": "от 1,7 млн ₽", "unit": "первый релиз"},
                 {"t": "Интеграции и учёт", "d": "Склад, сайт, CRM и банк обмениваются данными сами.", "list": ["обмен каждые 5 минут", "журнал ошибок"], "price": "от 340 тыс. ₽", "unit": "под ключ"}]},
            {"type": "html", "id": "estimate", "kick": "// оценка", "h2": "Соберите проект — увидите срок и бюджет", "alt": True,
             "lead": "Оценка по нашим 83 проектам. Точную смету дадим после бесплатного созвона на 40 минут.", "html": EST},
            {"type": "html", "id": "cases", "kick": "// кейсы", "h2": "Считаем результат в цифрах заказчика", "html": CASES},
            {"type": "steps", "id": "process", "kick": "// как работаем", "h2": "Спринты по две недели и демо каждую пятницу", "alt": True,
             "items": [("Discovery", "Интервью с вашей командой, карта процессов, прототип в Figma.", "2–3 недели, фиксированная цена"),
                       ("Спринты", "Каждые 2 недели — рабочая версия на тестовом сервере.", "оплата по спринтам"),
                       ("Релиз", "Публикация, нагрузочное тестирование, обучение.", "1 неделя"),
                       ("Поддержка", "Дежурный инженер, обновления, развитие по плану.", "от 3 месяцев")]},
            {"type": "gallery", "id": "office", "kick": "// команда", "h2": "Офис на Петроградской — и удалённые инженеры по всей России",
             "items": [{"img": "team", "span": 8, "ar": "16/10", "alt": "Команда"}, {"img": "meet", "span": 4, "ar": "4/5", "alt": "Планирование спринта"},
                       {"img": "desk", "span": 6, "ar": "3/2", "alt": "Рабочие места"}, {"img": "sun", "span": 6, "ar": "3/2", "alt": "Офис"}]},
            {"type": "faq", "id": "faq", "kick": "// вопросы", "h2": "Что обычно спрашивают техдиректора", "alt": True,
             "items": [("Кому принадлежит код?", "Вам — с первого коммита. Репозиторий в вашей организации, права передаём по акту после каждого спринта."),
                       ("Можно зайти в проект, который начинала другая команда?", "Да. Сначала двухнедельный аудит кода и архитектуры — скажем честно, что дописывать, а что переписать."),
                       ("Работаете по фиксированной цене?", "Discovery — фикс. Разработка — фиксированная цена каждого спринта; объём спринта согласуем перед стартом."),
                       ("Что после запуска?", "Поддержка от 3 месяцев: дежурный инженер, время реакции на критическую ошибку — 30 минут.")]},
        ],
        "contact": {"kick": "// контакт", "h2": "Расскажите о задаче — ответим с оценкой за 2 дня",
                    "lead": "Пришлём вопросы, проведём созвон на 40 минут и вернёмся с вилкой бюджета и планом первого релиза.",
                    "rows": [("Офис", "Санкт-Петербург, Каменноостровский пр., 42"), ("Телефон", "+7 812 000-00-00"), ("Ответ", "в течение рабочего дня")]},
        "form": {"fields": [("name", "Имя", "text", "", True), ("company", "Компания", "text", ""),
                            ("phone", "Телефон или e-mail", "text", "", True), ("budget", "Бюджет", "select", ["до 1 млн ₽", "1–3 млн ₽", "3–10 млн ₽", "больше 10 млн ₽"]),
                            ("msg", "Задача", "textarea", "Что нужно сделать и к какому сроку")],
                 "ok": "Спасибо! Пришлём вопросы и время созвона в течение рабочего дня.", "btn": "Отправить задачу"},
        "css": CSS, "js": JS,
    }
