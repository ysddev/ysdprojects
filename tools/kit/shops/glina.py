"""«Глина» — посуда ручной работы: сборка сервиза на нужное число персон с выбором глазури."""

IMG = {
    "hero": ("1558535284-3ade92aa58d4", 16, 10, "900,1400,2000"),
    "t1": ("1591632288574-a387f820a1ca", 4, 5, "500,900"),
    "t2": ("1705948731485-6e4c6c180d0d", 4, 5, "500,900"),
    "t3": ("1534273006427-1686266049b7", 4, 5, "500,900"),
    "t4": ("1551807306-4bcd16b92a41", 4, 5, "500,900"),
    "t5": ("1610128361323-6e941c97f023", 4, 5, "500,900"),
    "t6": ("1525973779373-015bdf68e579", 4, 5, "500,900"),
    "t7": ("1587560555570-4d3f84dcee05", 4, 5, "500,900"),
    "t8": ("1782351094137-14cef7134c18", 4, 5, "500,900"),
    "t9": ("1782351076283-73aa35f76058", 4, 5, "500,900"),
    "t10": ("1605117012605-b68dedd4accc", 4, 5, "500,900"),
    "t11": ("1554140426-5e830b73a5e8", 4, 5, "500,900"),
    "t12": ("1548594172-09665cd0e236", 4, 5, "500,900"),
    "t13": ("1683558654439-8b9986cbf1dd", 4, 5, "500,900"),
    "t14": ("1612196808214-b8e1d6145a8c", 4, 5, "500,900"),
    "t15": ("1631125915902-d8abe9225ff2", 4, 5, "500,900"),
    "t16": ("1617695615794-a5abcece0f48", 4, 5, "500,900"),
}
GL = {"Глазурь": ["Молоко", "Песок", "Шалфей", "Графит"]}


def P(id, n, cat, p, img, m, d, s, old=None, tag=None, nw=False, glaze=True):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": s}
    if glaze:
        x["opts"] = GL
    if old:
        x["old"] = old
    if tag:
        x["tag"] = tag
    if nw:
        x["nw"] = 1
    x["stock"] = "В наличии · разбитое при доставке заменим бесплатно"
    return x


PRODUCTS = [
    P("t1", "Тарелка обеденная, 27 см", "plates", 1490, "t1", "Каменная керамика", "Ровная, с невысоким бортом: удобно и для пасты, и для стейка.",
      [["Диаметр", "27 см"], ["Уход", "посудомойка, микроволновка"]], tag="Хит"),
    P("t2", "Тарелка закусочная, 21 см", "plates", 1190, "t2", "Край без глазури", "Тёплый необработанный край, который приятно держать в руках.",
      [["Диаметр", "21 см"], ["Уход", "посудомойка"]]),
    P("t3", "Тарелки десертные, набор из 6", "plates", 6900, "t3", "Шесть оттенков", "Каждому гостю свой цвет: никто не перепутает тарелку.",
      [["Диаметр", "19 см"], ["В наборе", "6 шт."]], glaze=False, nw=True),
    P("t4", "Сервиз «Ужин на двоих»", "plates", 8400, "t4", "8 предметов", "Две обеденные, две закусочные тарелки, две миски и две кружки.",
      [["В наборе", "8 предметов"]], old=9600, tag="Набор"),
    P("t5", "Миска глубокая, 16 см", "bowls", 990, "t5", "600 мл", "Для супа, каши и рамена. Не обжигает руки.",
      [["Объём", "600 мл"], ["Уход", "посудомойка, микроволновка"]]),
    P("t6", "Миски, набор из 4", "bowls", 3600, "t6", "Штабелируются", "Плотно встают друг в друга и занимают одну полку.",
      [["Объём", "450 мл"], ["В наборе", "4 шт."]], tag="Набор"),
    P("t7", "Салатник, 22 см", "bowls", 2250, "t7", "1,4 л · глазурь с потёками", "Большая миска для салата на компанию. Рисунок глазури у каждой свой.",
      [["Объём", "1,4 л"]], glaze=False),
    P("t8", "Кружка ручной лепки, 300 мл", "cups", 1390, "t8", "Гончарный круг", "Чуть неровная, с удобной ручкой на три пальца.",
      [["Объём", "300 мл"]], tag="Хит"),
    P("t9", "Кружка в крапинку, 300 мл", "cups", 1390, "t9", "Глазурь «Шалфей»", "Зелёная глазурь с тёмной крапинкой от красной глины.",
      [["Объём", "300 мл"]], glaze=False, nw=True),
    P("t10", "Чашка с блюдцем, 180 мл", "cups", 1690, "t10", "Для эспрессо и чая", "Толстые стенки держат тепло, блюдце подходит под печенье.",
      [["Объём", "180 мл"]]),
    P("t11", "Стаканы, набор из 3", "cups", 2100, "t11", "Стекло · 320 мл", "Тонкое стекло с тяжёлым дном. Для воды, сока и коктейлей.",
      [["Объём", "320 мл"], ["В наборе", "3 шт."]], glaze=False),
    P("t12", "Приборы на персону", "serve", 2900, "t12", "Сталь и латунь", "Вилка, нож и две ложки с матовыми латунными ручками.",
      [["В наборе", "4 предмета"], ["Уход", "ручная мойка"]], glaze=False),
    P("t13", "Чайник заварочный, 800 мл", "serve", 4200, "t13", "С ситечком", "На четыре чашки. Носик не капает, крышка не выпадает.",
      [["Объём", "800 мл"]]),
    P("t16", "Доска-поднос из дуба", "serve", 2600, "t16", "40 × 18 см", "Подавать сыр и хлеб или нарезать зелень. Пропитана минеральным маслом.",
      [["Размер", "40 × 18 см"], ["Материал", "дуб"]], glaze=False),
    P("t14", "Ваза из шамота, 24 см", "decor", 3800, "t14", "Шероховатая глина", "Хороша и пустой, и с одной веткой.",
      [["Высота", "24 см"]], glaze=False),
    P("t15", "Вазы, набор из 3", "decor", 5400, "t15", "Терракота", "Три формы, которые стоят вместе как одна композиция.",
      [["Высота", "12, 18 и 22 см"]], glaze=False),
]

WIDGET_HTML = """
<div class="st">
 <div class="stview">
  <svg viewBox="0 0 440 340" role="img" aria-label="Сервировка на одну персону">
   <rect width="440" height="340" rx="18" fill="#d9c9b4"/>
   <g id="stDin"><circle cx="190" cy="178" r="118" fill="rgba(60,40,20,.14)"/><circle cx="188" cy="172" r="118" class="gz"/><circle cx="188" cy="172" r="92" fill="none" stroke="rgba(0,0,0,.07)" stroke-width="2"/></g>
   <g id="stSal"><circle cx="190" cy="176" r="76" fill="rgba(60,40,20,.14)"/><circle cx="188" cy="171" r="76" class="gz gz2"/><circle cx="188" cy="171" r="58" fill="none" stroke="rgba(0,0,0,.07)" stroke-width="2"/></g>
   <g id="stBowl"><circle cx="190" cy="174" r="50" fill="rgba(60,40,20,.16)"/><circle cx="188" cy="170" r="50" class="gz"/><circle cx="188" cy="170" r="40" fill="rgba(0,0,0,.08)"/></g>
   <g id="stMug"><circle cx="364" cy="92" r="40" fill="rgba(60,40,20,.14)"/><rect x="392" y="80" width="26" height="16" rx="8" class="gz"/><circle cx="362" cy="88" r="40" class="gz"/><circle cx="362" cy="88" r="31" fill="#5a3a22"/></g>
  </svg>
  <div class="stsw" id="stG"><button data-c="#f3efe6" aria-pressed="true" title="Молоко" style="--c:#f3efe6"></button><button data-c="#d8c3a1" aria-pressed="false" title="Песок" style="--c:#d8c3a1"></button><button data-c="#a9b89a" aria-pressed="false" title="Шалфей" style="--c:#a9b89a"></button><button data-c="#4a4a4c" aria-pressed="false" title="Графит" style="--c:#4a4a4c"></button><span id="stGn">Глазурь «Молоко»</span></div>
 </div>
 <div>
  <div class="kick">Соберите сервиз</div>
  <h2 style="margin:12px 0 12px">Посуда на всех, <em>кто сядет за стол</em></h2>
  <p class="lead" style="font-size:17px">Выберите, сколько вас, какие предметы нужны и цвет глазури. Всё сделаем из одной партии глины, чтобы оттенок совпал.</p>
  <div class="gq"><b>Персон</b><div class="gtags" id="stN"><button data-n="2">2</button><button data-n="4" aria-pressed="true">4</button><button data-n="6">6</button><button data-n="8">8</button><button data-n="12">12</button></div></div>
  <div class="gq"><b>Что входит</b><div class="stit" id="stI">
   <label><input type="checkbox" data-id="t1" data-g="stDin" checked> Обеденная тарелка, 27 см</label>
   <label><input type="checkbox" data-id="t2" data-g="stSal" checked> Закусочная тарелка, 21 см</label>
   <label><input type="checkbox" data-id="t5" data-g="stBowl" checked> Глубокая миска, 16 см</label>
   <label><input type="checkbox" data-id="t8" data-g="stMug" checked> Кружка, 300 мл</label></div></div>
  <div class="stsum"><div><span id="stC"></span><b id="stT"></b></div><button class="btn" type="button" id="stAdd">Добавить сервиз</button></div>
 </div>
</div>"""

WIDGET_CSS = """
.st{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,64px);align-items:center}
.st h2 em{font-style:italic;color:var(--ac)}
.stview svg{width:100%;height:auto;display:block;border-radius:var(--rc)}
.stview .gz{fill:var(--gz,#f3efe6);transition:fill .3s}
.stview .gz2{filter:brightness(.96)}
.stview g{transition:opacity .3s}
.stsw{display:flex;align-items:center;gap:10px;margin-top:14px}
.stsw button{width:34px;height:34px;border-radius:50%;background:var(--c);box-shadow:inset 0 0 0 1px rgba(0,0,0,.15)}
.stsw button[aria-pressed=true]{box-shadow:0 0 0 2px var(--bg),0 0 0 4px var(--ink)}
.stsw span{margin-left:6px;font-size:15px;color:var(--soft)}
.gq{margin-top:22px}
.gq b{display:block;font-size:13px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--soft);margin-bottom:10px}
.gtags{display:flex;gap:8px;flex-wrap:wrap}
.gtags button{width:52px;height:46px;border-radius:var(--rb);box-shadow:inset 0 0 0 1px var(--line2);font-weight:600}
.gtags button[aria-pressed=true]{background:var(--ink);color:var(--bg);box-shadow:none}
.stit{display:grid;gap:10px}
.stit label{display:flex;gap:10px;align-items:center;cursor:pointer;font-size:16px}
.stit input{width:20px;height:20px;accent-color:var(--ac)}
.stsum{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-top:26px;padding-top:20px;border-top:1px solid var(--line);flex-wrap:wrap}
.stsum span{display:block;font-size:14px;color:var(--mut)}
.stsum b{font-family:var(--fh);font-size:34px;font-weight:400}
@media (max-width:860px){.st{grid-template-columns:1fr}}
"""

WIDGET_JS = r"""
(function(){
var S=window.SHOP,$=function(s){return document.querySelector(s)},n=4,glaze='Молоко';
function picked(){return [].slice.call(document.querySelectorAll('#stI input')).filter(function(i){return i.checked})}
function draw(){var t=0,c=0;document.querySelectorAll('#stI input').forEach(function(i){document.getElementById(i.dataset.g).style.opacity=i.checked?1:0});
 picked().forEach(function(i){t+=S.byId[i.dataset.id].p*n;c+=n});
 $('#stC').textContent=c?c+' '+(c%10===1&&c!==11?'предмет':c%10>1&&c%10<5&&(c<10||c>20)?'предмета':'предметов')+' на '+n+' персон':'Выберите хотя бы один предмет';
 $('#stT').textContent=c?S.fmt(t):'';$('#stAdd').disabled=!c}
$('#stN').onclick=function(e){var b=e.target.closest('button');if(!b)return;n=+b.dataset.n;this.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});draw()};
$('#stG').onclick=function(e){var b=e.target.closest('button');if(!b)return;glaze=b.title;this.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});
 document.querySelector('.stview svg').style.setProperty('--gz',b.dataset.c);$('#stGn').textContent='Глазурь «'+glaze+'»'};
$('#stI').addEventListener('change',draw);
$('#stAdd').addEventListener('click',function(){picked().forEach(function(i){S.add(i.dataset.id,{'Глазурь':glaze},n)})});
draw();
})();
"""


def cfg():
    return {
        "slug": "shops/glina", "images": IMG, "brand": "Глина",
        "logo": '<span style="font-family:var(--fh);font-weight:300;font-size:28px;letter-spacing:.04em">глина</span><span style="font:500 10px/1 var(--fb);letter-spacing:.2em;text-transform:uppercase;color:var(--mut);margin-left:8px">посуда</span>',
        "title": "Глина — посуда ручной работы и сервизы на заказ",
        "desc": "Тарелки, миски, кружки и вазы из каменной керамики. Соберите сервиз на нужное число персон в своей глазури, доставим с заменой боя.",
        "variant": "lookbook", "favLetter": "Г",
        "theme": {"bg": "#f5f0e8", "ink": "#2a2420", "soft": "#5e544c", "mut": "#9a8f85", "line": "rgba(42,36,32,.1)", "line2": "rgba(42,36,32,.26)",
                  "card": "#e9e0d2", "ac": "#a3522c", "aci": "#fff", "ok": "#4d7a55", "rc": "6px", "rb": "4px", "rs": "10px",
                  "fh": '"Spectral",Georgia,serif', "fe": '"Spectral",Georgia,serif', "fb": '"Manrope",system-ui,sans-serif', "fm": '"Manrope",system-ui,sans-serif',
                  "hw": "300", "ht": "-.02em", "hc": "none", "lw": "300", "lt": "0", "ar": "4/5", "fot": "#2a2420"},
        "fonts": [("Spectral", "spectral", [300, 400], "normal"), ("Spectral", "spectral", [400], "italic"), ("Manrope", "manrope", [400, 500, 600], "normal")],
        "strip": "Разбитое при доставке <b>заменим бесплатно</b> · сервиз на заказ за 14 дней · можно в посудомойку",
        "nav": [("Посуда", "catalog"), ("Собрать сервиз", "feat"), ("Мастерская", "why"), ("Вопросы", "faq")],
        "searchPh": "Тарелка, миска, кружка…",
        "hero": {"kicker": "Гончарная мастерская · Суздаль", "h1": "Посуда, за которой <em>хочется задержаться</em>", "img": "hero",
                 "lead": "Тарелки, миски и кружки из каменной керамики. Лепим вручную небольшими партиями, поэтому у каждой вещи свой характер.",
                 "cta": "Смотреть посуду", "cta2": "Собрать сервиз", "cta2To": "feat",
                 "stats": [("1 240 °C", "обжиг каменной керамики"), ("4 глазури", "на выбор"), ("14 дней", "сервиз на заказ")]},
        "cats": [{"id": "plates", "n": "Тарелки"}, {"id": "bowls", "n": "Миски"}, {"id": "cups", "n": "Кружки и стаканы"}, {"id": "serve", "n": "Сервировка"},
                 {"id": "decor", "n": "Вазы"}],
        "products": PRODUCTS, "pageSize": 8, "showStars": False, "cardSizes": "(max-width:860px) 50vw, 25vw",
        "freeFrom": 7000, "promo": {"code": "ГЛИНА", "pct": 10, "hint": "ГЛИНА — минус 10% на первый заказ"},
        "ship": [{"id": "cour", "name": "Курьер", "eta": "2–3 дня, в коробке с ячейками", "price": 390, "free": 7000},
                 {"id": "pvz", "name": "Пункт выдачи", "eta": "3–6 дней по России", "price": 290, "free": 7000},
                 {"id": "pick", "name": "Мастерская в Суздале", "eta": "заберите сами и посмотрите, как мы работаем", "price": 0}],
        "commentPh": "Подарок? Упакуем и вложим открытку",
        "doneNote": "Перед отправкой пришлём фото вашего заказа из мастерской.",
        "addLabel": "В корзину",
        "widget": {"nav": "Собрать сервиз", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS},
        "usp": [("Каменная керамика", "Обжиг при 1 240 °C: посуда не впитывает воду и не боится посудомойки и микроволновки."),
                ("Замена боя", "Разбилось при доставке: пришлите фото, отправим новую вещь за наш счёт."),
                ("Докупить через год", "Храним рецепты глазурей: сделаем такую же тарелку, если одна разобьётся."),
                ("Сервиз на заказ", "Нужное число персон, предметы и глазурь. Срок изготовления 14 дней.")],
        "uspTitle": "Сделано руками, служит годами", "uspKick": "Мастерская",
        "faq": [("Посуду можно мыть в посудомойке?", "Да. Каменная керамика с пищевой глазурью выдерживает посудомоечную машину, микроволновку и духовку до 220 °C."),
                ("Все предметы одинаковые?", "Почти. Это ручная работа: диаметр может отличаться на пару миллиметров, а рисунок глазури у каждой вещи свой."),
                ("Сколько делается сервиз на заказ?", "14 дней: лепка, сушка, два обжига. Если нужные предметы есть в наличии, отправим на следующий день."),
                ("Что если посуда разобьётся в дороге?", "Пакуем в коробки с ячейками. Если что-то всё же разбилось, пришлите фото в течение 3 дней, заменим бесплатно.")],
        "footBig": "Стол, за который зовут",
        "contacts": {"addr": "Суздаль, ул. Лебедева, 4", "hours": "Мастерская открыта 11:00–19:00, кроме понедельника"},
        "order": ["catalog", "widget", "usp", "faq"], "gridTitle": "Посуда из мастерской", "gridKick": "В наличии",
        "css": ".hero h1{font-size:clamp(46px,6.8vw,108px);line-height:.96}.v-lookbook .hero h1 em{font-style:italic;color:#f1d9c4}.card .nm{font-family:var(--fh);font-size:21px;font-weight:400}"
               ".price{font-weight:500}",
    }
