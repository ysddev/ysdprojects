"""«Сальдо» — бухгалтерское сопровождение ИП и ООО в Казани: калькулятор цены обслуживания, перевод от прошлого
бухгалтера, ответственность за штрафы по нашей вине."""

IMAGES = {
    "desk": ("1626266061368-46a8f578ddd6", 16, 9, "800,1400"),
    "binders": ("1633520833019-e34afd4b8fad", 16, 9, "800,1400"),
    "office": ("1497215728101-856f4ea42174", 4, 3, "600,1000"),
    "calc": ("1642043175009-5997b3a078d8", 4, 5, "600,1000"),
    "laptop": ("1651130536923-07a66091b614", 3, 2, "600,1000"),
    "archive": ("1768158989131-64cbff67f292", 4, 5, "600,1000"),
    "hall": ("1497366754035-f200968a6e72", 4, 5, "600,1000"),
    "sign": ("1450101499163-c8848c66ca85", 3, 2, "600,1000"),
}

ICON = {
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/></svg>',
    "people": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M16 4.5a3 3 0 0 1 0 6M21 20c0-2.6-1.6-4.8-4-5.6"/></svg>',
    "bank": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 9l9-5 9 5M5 9v9M10 9v9M14 9v9M19 9v9M3 20h18"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3l8 3v6c0 4.5-3.4 8.2-8 9-4.6-.8-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 20V4M4 20h16M8 16v-5M12 16V8M16 16v-3"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 10h8M8 13h5"/></svg>',
}

LOGO = ('<svg viewBox="0 0 32 32"><rect width="32" height="32" rx="9" fill="#1f4d3a"/><path d="M9 21.5c1.4 1.3 3.4 2 5.6 2 3.4 0 5.6-1.6 5.6-4.1 '
        '0-5.3-10.4-2.9-10.4-7.3 0-1.8 1.7-3.1 4.4-3.1 1.9 0 3.5.6 4.6 1.6" fill="none" stroke="#f3efe4" stroke-width="2.2" stroke-linecap="round"/>'
        '<path d="M22.5 6.5v19" stroke="#c9a96b" stroke-width="2" stroke-linecap="round"/></svg>')


def mono(letters: str, bg: str) -> str:
    return (f'<svg viewBox="0 0 400 500" style="width:100%;height:100%"><rect width="400" height="500" fill="{bg}"/>'
            f'<circle cx="200" cy="215" r="110" fill="none" stroke="#f3efe4" stroke-opacity=".35"/>'
            f'<text x="200" y="250" text-anchor="middle" font-family="Spectral" font-weight="500" font-size="104" fill="#f3efe4">{letters}</text></svg>')


CALC = r"""
<div class="calc rv">
 <div class="panel cq">
  <div class="q"><b>Кто вы</b><div class="seg" id="cWho"><button type="button" data-v="ip" class="on">ИП</button><button type="button" data-v="ooo">ООО</button></div></div>
  <div class="q"><b>Система налогообложения</b><div class="chips" id="cTax"></div></div>
  <div class="q rng"><div class="rh"><span>Сотрудники в штате</span><b id="cEmpV">0</b></div><input type="range" id="cEmp" min="0" max="40" value="0"></div>
  <div class="q rng"><div class="rh"><span>Операций по счёту в месяц</span><b id="cOpsV">30</b></div><input type="range" id="cOps" min="10" max="400" step="10" value="30"></div>
  <div class="q"><b>Ещё</b><div class="chips" id="cExt"></div></div>
 </div>
 <div class="panel cr">
  <span class="kick">Ваш тариф</span>
  <div class="big" id="cSum">—</div><small id="cUnit">в месяц, фиксировано на год</small>
  <ul id="cInc"></ul>
  <div class="cnote" id="cNote"></div>
  <a class="btn" href="#lead" id="cGo">Закрепить цену</a>
 </div>
</div>
"""

CSS = r"""
.hero h1 em{font-style:italic;font-weight:400}
.calc{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:clamp(14px,2vw,22px);align-items:start}
.cq{display:grid;gap:26px}.cq .q{display:grid;gap:12px}.cq .q>b{font-weight:600;font-size:15.5px}
.cr{position:sticky;top:90px;background:var(--dk);color:#f3efe4;box-shadow:none}
.cr .kick{color:#c9a96b}.cr .big{margin:14px 0 4px;color:#fff}.cr small{color:rgba(243,239,228,.7);font-size:14px}
.cr ul{list-style:none;padding:0;margin:22px 0;display:grid;gap:9px;font-size:15px;border-top:1px solid rgba(243,239,228,.18);padding-top:18px}
.cr li{display:flex;gap:10px}.cr li::before{content:"✓";color:#c9a96b}
.cr .cnote{font-size:13.5px;color:rgba(243,239,228,.7);margin-bottom:18px;min-height:2.6em}
.cr .btn{width:100%;background:#c9a96b;color:#1b2b23}
.promise{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(20px,4vw,60px);align-items:center}
.promise .ph{border-radius:var(--rc);overflow:hidden;aspect-ratio:4/5}.promise .ph img{width:100%;height:100%;object-fit:cover}
.promise h2{font-size:clamp(32px,4vw,54px);margin:14px 0 18px}
.promise ol{margin:24px 0 0;padding:0;list-style:none;display:grid;gap:14px}
.promise li{padding:16px 18px;border-radius:14px;background:rgba(243,239,228,.07);font-size:15.5px}
.promise li b{display:block;font:500 19px var(--fh);margin-bottom:3px;color:#fff}
.nums{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;background:var(--line);border-radius:20px;overflow:hidden;margin-top:clamp(30px,4vw,48px)}
.nums div{background:var(--bg);padding:22px}.nums b{display:block;font:500 clamp(30px,3.4vw,44px)/1 var(--fh);color:var(--ac)}.nums span{display:block;margin-top:8px;color:var(--soft);font-size:14.5px}
@media (max-width:860px){.calc,.promise{grid-template-columns:1fr}.cr{position:static}.nums{grid-template-columns:1fr 1fr}}
"""

JS = r"""
(function(){var $=function(s){return document.getElementById(s)};
var TAX={ip:[['usn6','УСН 6%'],['usn15','УСН 15%'],['patent','Патент'],['osno','ОСНО']],ooo:[['usn6','УСН 6%'],['usn15','УСН 15%'],['osno','ОСНО с НДС']]};
var BASE={ip:{usn6:3400,usn15:4900,patent:2900,osno:9700},ooo:{usn6:6900,usn15:8400,osno:13900}};
var EXT=[['mp','Маркетплейсы',3500,'сверка отчётов площадок и комиссий'],['ved','ВЭД',4800,'валютный контроль и импорт'],['kadr','Кадры',1900,'договоры, отпуска, больничные'],['dir','Отчёт собственнику',2300,'деньги, долги и прибыль раз в месяц на одной странице']];
var who='ip',tax='usn6',ext={};
function chips(){$('cTax').innerHTML=TAX[who].map(function(t){return'<button type="button" data-v="'+t[0]+'" class="'+(t[0]==tax?'on':'')+'">'+t[1]+'</button>'}).join('')}
$('cExt').innerHTML=EXT.map(function(x){return'<button type="button" data-v="'+x[0]+'">'+x[1]+' · +'+rub(x[2])+'</button>'}).join('');
function calc(){var emp=+$('cEmp').value,ops=+$('cOps').value;$('cEmpV').textContent=emp;$('cOpsV').textContent=ops;
 if(!BASE[who][tax])tax='usn6';var s=BASE[who][tax];var e=Math.min(emp,5)*650+Math.max(0,emp-5)*450;var o=Math.max(0,Math.ceil((ops-30)/50))*1200;
 var inc=['Учёт по всем счетам и кассе','Налоги и уведомления — считаем и напоминаем за 5 дней','Отчётность в налоговую и фонды','Ответ в чате в течение 2 часов'];
 if(emp)inc.push('Зарплата и отчёты по '+emp+' '+plural(emp,'сотруднику','сотрудникам','сотрудникам'));
 var add=0;EXT.forEach(function(x){if(ext[x[0]]){add+=x[2];inc.push(x[1]+': '+x[3])}});
 var sum=s+e+o+add;$('cSum').textContent=rub(sum);$('cInc').innerHTML=inc.map(function(t){return'<li>'+t+'</li>'}).join('');
 $('cNote').textContent=o?('Включено '+ops+' операций: каждые 50 сверх 30 — +1 200 ₽. Если операций станет меньше, цена снизится со следующего месяца.'):'Цена не растёт в течение года, даже если вырастет оборот.';
 $('cGo').dataset.sum=sum}
$('cWho').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;who=b.dataset.v;[].forEach.call(this.children,function(x){x.classList.toggle('on',x===b)});chips();calc()});
$('cTax').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;tax=b.dataset.v;chips();calc()});
$('cExt').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;ext[b.dataset.v]=!ext[b.dataset.v];b.classList.toggle('on');calc()});
['cEmp','cOps'].forEach(function(id){$(id).addEventListener('input',calc)});
$('cGo').addEventListener('click',function(){var t=document.querySelector('#lead textarea');if(t)t.value=(who=='ip'?'ИП':'ООО')+', '+document.querySelector('#cTax .on').textContent+', сотрудников: '+$('cEmp').value+', операций: '+$('cOps').value+'. Расчёт на сайте: '+rub(+this.dataset.sum)+' в месяц.'});
chips();calc()})();
"""

PROMISE = ('<div class="promise"><div class="rv"><div class="kick">Ответственность</div><h2>Штраф по нашей вине оплачиваем мы</h2>'
           '<p class="lead">Это записано в договоре, а не в рекламе. Опоздали с отчётом или ошиблись в расчёте — возмещаем штраф и пени '
           'в течение 10 рабочих дней после требования налоговой.</p>'
           '<ol><li><b>Двойная проверка</b>Каждую декларацию сверяет второй бухгалтер — не тот, кто её готовил.</li>'
           '<li><b>Календарь на год вперёд</b>Сроки по вашей системе налогообложения заранее в календаре — у нас и у вас.</li>'
           '<li><b>Страхование ответственности</b>На 1 500 000 ₽ — на случай, если ошибка окажется дороже наших гарантий.</li></ol></div>'
           '<div class="ph rv">{IMG}</div></div>'
           '<div class="nums rv"><div><b>214</b><span>компаний и ИП на обслуживании</span></div><div><b>11 лет</b><span>ведём учёт в Казани</span></div>'
           '<div><b>2 часа</b><span>максимум до ответа в рабочее время</span></div><div><b>0 ₽</b><span>штрафов за 2025 год по нашей вине</span></div></div>')


def cfg() -> dict:
    from ..common import img
    return {
        "slug": "saldo", "brand": "Сальдо", "legal": "ООО «Сальдо», Казань", "favLetter": "С", "logo": LOGO,
        "title": "Сальдо — бухгалтерское сопровождение ИП и ООО в Казани",
        "desc": "Бухгалтерия для ИП и ООО в Казани: учёт, налоги, зарплата и отчётность. Калькулятор цены обслуживания, "
                "фиксированный тариф на год, штрафы по нашей вине оплачиваем сами.",
        "theme": {"bg": "#f6f3ec", "ink": "#16241d", "soft": "#46524b", "mut": "#7c857f", "line": "#e2ddd1", "line2": "#cdc6b6",
                  "card": "#fffdf8", "alt": "#ece6d9", "ac": "#1f4d3a", "aci": "#f6f3ec", "fh": "Spectral,serif", "fb": '"Inter Tight",sans-serif',
                  "hw": "500", "ht": "-.015em", "dk": "#1b2b23", "dki": "#f3efe4", "rc": "20px", "rb": "12px", "emst": "italic", "emc": "#1f4d3a"},
        "fonts": [("Spectral", "spectral", [400, 500], "normal"), ("Spectral", "spectral", [400], "italic"),
                  ("Inter Tight", "inter-tight", [400, 600], "normal")],
        "images": IMAGES,
        "phone": ("+78430000000", "+7 843 000-00-00"),
        "mail": "hello@saldo.ysdprojects.space",
        "nav": [("services", "Услуги"), ("calc", "Цена"), ("promise", "Гарантии"), ("move", "Переход"), ("faq", "Вопросы")],
        "topCta": "Рассчитать",
        "hero": {"kicker": "Бухгалтерия для ИП и ООО · Казань", "h1": "Бухгалтер, который <em>отвечает за штрафы</em> рублём",
                 "lead": "Ведём учёт, считаем налоги и сдаём отчётность за 214 компаний. Тариф фиксируем на год, а если штраф случился "
                         "по нашей вине — оплачиваем его сами.",
                 "cta": "Рассчитать цену", "go": "calc", "go2": ("services", "Что входит"),
                 "points": ["Ответ в чате за 2 часа", "Переход от старого бухгалтера — за нас", "Работаем удалённо по всей России"],
                 "img": "desk", "alt": "Рабочий стол бухгалтера", "ar": "4/5",
                 "tag": "<b>3 400 ₽ в месяц</b>ИП на УСН 6% без сотрудников — учёт, налоги и все отчёты"},
        "sections": [
            {"type": "cards", "id": "services", "kick": "Услуги", "h2": "Берём на себя всю бухгалтерию — или её часть",
             "lead": "Можно отдать всё целиком, можно только зарплату или только отчётность. Цена — за то, что вы правда отдаёте.",
             "items": [
                 {"icon": ICON["doc"], "t": "Полное сопровождение", "d": "Учёт, налоги, отчёты, ответы на требования налоговой.",
                  "list": ["первичка в электронном виде", "расчёт налогов и уведомлений", "сдача всей отчётности"], "price": "от 3 400 ₽", "unit": "в месяц"},
                 {"icon": ICON["people"], "t": "Зарплата и кадры", "d": "Начисления, НДФЛ и взносы, договоры и кадровые документы.",
                  "list": ["расчёт зарплаты дважды в месяц", "отпуска и больничные", "отчёты в фонды"], "price": "от 650 ₽", "unit": "за сотрудника"},
                 {"icon": ICON["bank"], "t": "Восстановление учёта", "d": "Когда прошлый бухгалтер ушёл и оставил хвосты.",
                  "list": ["разбор банка и первички", "уточнённые декларации", "план закрытия долгов"], "price": "от 18 500 ₽", "unit": "за квартал"},
                 {"icon": ICON["chart"], "t": "Отчёт собственнику", "d": "Сколько заработали, кому должны и сколько уйдёт в налоги — на одной странице.",
                  "list": ["прибыль по направлениям", "дебиторка и кредиторка", "прогноз налогов на квартал"], "price": "2 300 ₽", "unit": "в месяц"},
                 {"icon": ICON["shield"], "t": "Сопровождение проверок", "d": "Отвечаем на требования и сопровождаем камеральные и выездные проверки.",
                  "list": ["ответ на требование за 1 день", "пояснения и документы", "представительство"], "price": "от 4 700 ₽", "unit": "за требование"},
                 {"icon": ICON["chat"], "t": "Разовая консультация", "d": "Какую систему налогообложения выбрать, как платить себе дивиденды, что с НДС.",
                  "list": ["60 минут с главным бухгалтером", "письменные выводы после встречи"], "price": "3 900 ₽", "unit": "за час"}]},
            {"type": "html", "id": "calc", "kick": "Калькулятор", "h2": "Посчитайте цену за 30 секунд", "alt": True,
             "lead": "Это точная цена, а не «от»: её закрепим в договоре на год.", "html": CALC},
            {"type": "html", "id": "promise", "dark": True, "html": PROMISE.replace("{IMG}", img("archive", IMAGES, "(max-width:860px) 100vw, 45vw", "Архив документов"))},
            {"type": "steps", "id": "move", "kick": "Переход", "h2": "Уйти от прошлого бухгалтера — это наша работа, не ваша",
             "items": [("Заявка и доступы", "Подписываем договор и NDA, вы даёте доступ к банку и программе.", "1 день"),
                       ("Аудит учёта", "Проверяем последние 3 года: налоги, взносы, остатки. Находим, что исправить.", "3–5 дней"),
                       ("Передача дел", "Сами связываемся с прошлым бухгалтером и забираем базу и документы.", "до 7 дней"),
                       ("Ведём учёт", "С первого месяца — по тарифу. Ошибки прошлых периодов исправляем по плану.", "дальше каждый месяц")]},
            {"type": "team", "id": "team", "kick": "Кто ведёт учёт", "h2": "За каждой компанией — два бухгалтера", "alt": True,
             "lead": "Ведущий бухгалтер считает, второй — проверяет. Отпуск или больничный не останавливают вашу отчётность.",
             "items": [{"n": "Гульнара Сафина", "r": "Главный бухгалтер · 17 лет в учёте, аттестат профессионального бухгалтера", "art": mono("ГС", "#1f4d3a")},
                       {"n": "Илья Котов", "r": "Ведущий бухгалтер ООО на ОСНО · ВЭД и НДС", "art": mono("ИК", "#2f5f4b")},
                       {"n": "Алсу Нуриева", "r": "Зарплата и кадры · 9 лет, 1 140 сотрудников клиентов", "art": mono("АН", "#3e6f5a")}]},
            {"type": "gallery", "id": "office", "kick": "Офис", "h2": "Можно прийти — а можно никогда не приезжать",
             "items": [{"img": "office", "span": 5, "ar": "4/3", "alt": "Офис"}, {"img": "binders", "span": 7, "ar": "16/9", "alt": "Документы"},
                       {"img": "laptop", "span": 4, "ar": "3/2", "alt": "Работа удалённо"}, {"img": "calc", "span": 4, "ar": "3/2", "alt": "Расчёты"},
                       {"img": "sign", "span": 4, "ar": "3/2", "alt": "Подписание договора"}]},
            {"type": "faq", "id": "faq", "kick": "Вопросы", "h2": "Что спрашивают перед договором",
             "items": [("Документы нужно привозить?", "Нет. Банк подключаем по API, первичку присылаете фото в чат или через ЭДО. Оригиналы храните у себя."),
                       ("Что если оборот вырастет?", "Цена зафиксирована на год. Пересчитываем только при переходе на другую систему налогообложения или резком росте операций — и предупреждаем за месяц."),
                       ("Как вы отвечаете за ошибки?", "Пункт 6.2 договора: штраф и пени по нашей вине возмещаем в течение 10 рабочих дней. Ответственность застрахована на 1 500 000 ₽."),
                       ("Можно ли начать с середины года?", "Да. Проверим, что сделано до нас, и продолжим с любого месяца."),
                       ("Работаете с маркетплейсами?", "Да, сверяем отчёты площадок, комиссии и возвраты. Это опция «Маркетплейсы» в калькуляторе.")]},
        ],
        "contact": {"kick": "Заявка", "h2": "Пришлём расчёт и договор сегодня",
                    "lead": "Оставьте телефон — главный бухгалтер позвонит в течение часа в рабочее время и ответит на вопросы.",
                    "rows": [("Адрес", "Казань, ул. Пушкина, 26, офис 504"), ("Телефон", "+7 843 000-00-00"), ("Часы", "Пн–пт 9:00–19:00, чат — до 21:00")]},
        "form": {"fields": [("name", "Имя", "text", "Как к вам обращаться", True), ("phone", "Телефон", "tel", "+7", True),
                            ("who", "Форма бизнеса", "select", ["ИП", "ООО", "Пока не открыли"]), ("tax", "Налоги", "select", ["УСН 6%", "УСН 15%", "Патент", "ОСНО", "Не знаю"]),
                            ("msg", "Комментарий", "textarea", "Что сейчас с учётом")],
                 "ok": "Спасибо! Главный бухгалтер позвонит в течение часа в рабочее время.", "btn": "Получить расчёт"},
        "css": CSS, "js": JS,
    }
