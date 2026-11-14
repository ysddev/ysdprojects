"""«Вольт» — электроника и гаджеты: тёмная витрина, сравнение моделей и калькулятор рассрочки."""

IMG = {
    "hero": ("1505740420928-5e560c06d30e", 16, 9, "800,1400,2000"),
    "hp1": ("1618366712010-f4ae9c647dcb", 1, 1, "500,900"),
    "hp2": ("1583394838336-acd977736f90", 1, 1, "500,900"),
    "hp3": ("1484704849700-f032a568e944", 1, 1, "500,900"),
    "hp4": ("1613040809024-b4ef7ba99bc3", 1, 1, "500,900"),
    "hp5": ("1609081219090-a6d81d3085bf", 1, 1, "500,900"),
    "sp1": ("1608043152269-423dbba4e7e1", 1, 1, "500,900"),
    "sp2": ("1589003077984-894e133dabab", 1, 1, "500,900"),
    "sp3": ("1547052178-7f2c5a20c332", 1, 1, "500,900"),
    "sp4": ("1582978571763-2d039e56f0c3", 1, 1, "500,900"),
    "w1": ("1579586337278-3befd40fd17a", 1, 1, "500,900"),
    "w2": ("1624096104992-9b4fa3a279dd", 1, 1, "500,900"),
    "w3": ("1551816230-ef5deaed4a26", 1, 1, "500,900"),
    "cam": ("1776566347746-1bb7dcaa12d3", 1, 1, "500,900"),
    "desk": ("1787839322261-4caf24adb081", 1, 1, "500,900"),
    "lap": ("1595303526913-c7037797ebe7", 1, 1, "500,900"),
}


def P(id, n, cat, p, img, m, d, s, old=None, tag=None, opts=None, nw=False, cmp=None):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": s, "r": 4.6 + (len(n) % 4) / 10}
    if old:
        x["old"] = old
    if tag:
        x["tag"] = tag
    if opts:
        x["opts"] = opts
    if nw:
        x["nw"] = 1
    if cmp:
        x["cmp"] = cmp
    x["stock"] = "В наличии · заберите сегодня или получите завтра"
    return x


BW = [{"v": "Чёрный", "c": "#16171a"}, {"v": "Серебро", "c": "#d6d8dc"}]
PRODUCTS = [
    P("hp1", "Наушники Volt Air Max ANC", "audio", 24990, "hp1", "Шумоподавление · 40 ч",
      "Адаптивное шумоподавление до −42 дБ, 40 часов работы и быстрая зарядка: 10 минут — 5 часов музыки.",
      [["Шумоподавление", "до −42 дБ"], ["Автономность", "40 ч"], ["Кодеки", "LDAC, AAC"], ["Вес", "254 г"]], tag="Хит", opts={"Цвет": BW},
      cmp={"Шумодав": "−42 дБ", "Батарея": "40 ч", "Вес": "254 г", "Кодек": "LDAC", "Мультипоинт": "да"}),
    P("hp2", "Наушники Volt Studio Pro", "audio", 32990, "hp2", "Для работы со звуком",
      "Ровная АЧХ и съёмный кабель — для монтажа и сведения, но и в метро хороши.",
      [["Драйвер", "50 мм"], ["Автономность", "30 ч"]], cmp={"Шумодав": "−38 дБ", "Батарея": "30 ч", "Вес": "280 г", "Кодек": "LDAC", "Мультипоинт": "да"}),
    P("hp3", "Наушники Volt Classic проводные", "audio", 8990, "hp3", "Кожаные амбушюры",
      "Проводная классика без задержек и зарядки. Кабель 3,5 мм с микрофоном.", [["Импеданс", "32 Ом"]],
      cmp={"Шумодав": "нет", "Батарея": "не нужна", "Вес": "210 г", "Кодек": "провод", "Мультипоинт": "нет"}),
    P("hp4", "Наушники Volt Pop", "audio", 6490, "hp4", "Лёгкие · 5 цветов",
      "220 граммов, складываются в чехол размером с ладонь.", [["Автономность", "50 ч"]], old=7990,
      opts={"Цвет": [{"v": "Розовый", "c": "#f4c6d0"}, {"v": "Белый", "c": "#f5f5f5"}, {"v": "Мята", "c": "#bfe6d4"}]},
      cmp={"Шумодав": "нет", "Батарея": "50 ч", "Вес": "220 г", "Кодек": "AAC", "Мультипоинт": "нет"}),
    P("hp5", "Наушники Volt Sport белые", "audio", 11990, "hp5", "IPX4 · для спорта",
      "Не боятся пота и дождя, держатся на голове при беге.", [["Защита", "IPX4"], ["Автономность", "35 ч"]], nw=True,
      cmp={"Шумодав": "−30 дБ", "Батарея": "35 ч", "Вес": "240 г", "Кодек": "AAC", "Мультипоинт": "да"}),
    P("sp1", "Колонка Volt Go", "speakers", 7990, "sp1", "IP67 · 16 ч",
      "Компактная колонка с ремешком: не тонет, не боится песка. Две можно связать в стерео.", [["Мощность", "20 Вт"], ["Защита", "IP67"]], tag="−20%", old=9990),
    P("sp2", "Колонка Volt Boom XL", "speakers", 19990, "sp2", "60 Вт · подсветка",
      "Громкая колонка для дачи и вечеринок, держит заряд 24 часа.", [["Мощность", "60 Вт"], ["Автономность", "24 ч"]]),
    P("sp3", "Колонка Volt Pebble", "speakers", 4990, "sp3", "Карманная",
      "Помещается в карман куртки, звук на удивление плотный.", [["Мощность", "8 Вт"]]),
    P("sp4", "Умная колонка Volt Home", "speakers", 12990, "sp4", "Голосовой помощник",
      "Управляет светом и розетками, ставит таймеры и включает радио.", [["Wi-Fi", "да"], ["Мощность", "25 Вт"]], nw=True),
    P("w1", "Часы Volt Watch 3", "wear", 18990, "w1", "AMOLED · пульс, SpO₂",
      "Яркий AMOLED-экран, 14 дней без зарядки, бесконтактная оплата.", [["Экран", "1,43\" AMOLED"], ["Автономность", "14 дней"]], tag="Новинка", nw=True, opts={"Ремешок": ["Силикон", "Кожа", "Металл"]}),
    P("w2", "Часы Volt Watch Lite", "wear", 8990, "w2", "21 день без зарядки",
      "Шаги, сон, пульс и уведомления — без лишнего.", [["Автономность", "21 день"]]),
    P("w3", "Фитнес-браслет Volt Band", "wear", 3990, "w3", "Сон и тренировки",
      "Лёгкий браслет, который не чувствуешь на руке ночью.", [["Защита", "5 ATM"]]),
    P("ac1", "Набор для блогера: свет, микрофон, штатив", "acc", 14990, "cam", "Для съёмки на телефон",
      "Кольцевой свет, петличка и штатив-трипод — всё, чтобы начать снимать сегодня.", [["Комплект", "3 предмета"]]),
    P("ac2", "Механическая клавиатура Volt Keys", "acc", 9990, "desk", "Горячая замена свитчей",
      "Алюминиевый корпус, свитчи меняются без пайки, подсветка RGB.", [["Раскладка", "RU/EN"]], opts={"Свитчи": ["Красные", "Коричневые"]}),
]

WIDGET_HTML = """
<div class="cmp">
 <div class="cmp-h"><div><div class="kick" style="color:var(--ac)">Сравнение</div><h2 style="margin-top:12px">Какие наушники <em>ваши</em></h2></div>
 <div class="seg" id="cmpUse"><button data-u="metro" aria-pressed="true">Метро и офис</button><button data-u="sport" aria-pressed="false">Спорт</button><button data-u="studio" aria-pressed="false">Работа со звуком</button></div></div>
 <div class="tbl" id="cmpT"></div>
 <div class="credit">
  <div><div class="kick" style="color:rgba(255,255,255,.55)">Рассрочка 0%</div><b id="crSum">0 ₽ в месяц</b><span id="crNote"></span></div>
  <div class="seg" id="crM"><button data-m="3" aria-pressed="false">3 мес.</button><button data-m="6" aria-pressed="true">6 мес.</button><button data-m="12" aria-pressed="false">12 мес.</button></div>
 </div>
</div>"""

WIDGET_CSS = """
#feat .feat{--fbg:#111317;--fink:#f2f3f5;background:radial-gradient(70% 90% at 90% 0%,rgba(91,124,255,.25),transparent 60%),#111317}
.cmp h2 em{font-style:normal;color:var(--ac)}
.cmp-h{display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap;margin-bottom:28px}
.seg{display:flex;gap:6px;flex-wrap:wrap;background:rgba(255,255,255,.06);padding:4px;border-radius:999px}
.seg button{height:40px;padding:0 16px;border-radius:999px;font-size:14px;color:rgba(255,255,255,.7)}
.seg button[aria-pressed=true]{background:#fff;color:#111}
.tbl{display:grid;grid-template-columns:150px repeat(3,1fr);border-radius:20px;overflow:hidden;box-shadow:inset 0 0 0 1px rgba(255,255,255,.1)}
.tbl>div{padding:14px 16px;border-bottom:1px solid rgba(255,255,255,.08);font-size:15px;display:flex;align-items:center;gap:8px}
.tbl .lbl{color:rgba(255,255,255,.5);font-size:13px}
.tbl .hd{flex-direction:column;align-items:flex-start;gap:10px;padding:18px 16px}
.tbl .hd .ph{width:100%;aspect-ratio:1;border-radius:14px;background:#1b1e24}
.tbl .hd b{font-size:15px;line-height:1.3}
.tbl .best{background:rgba(91,124,255,.12)}
.tbl .win{color:var(--ac);font-weight:600}
.tbl .tag{font:600 11px/1 var(--fb);background:var(--ac);color:#fff;padding:5px 8px;border-radius:6px}
.credit{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;margin-top:22px;padding:20px 22px;border-radius:20px;background:rgba(255,255,255,.05)}
.credit b{display:block;font-size:30px;margin-top:6px}
.credit span{font-size:13px;color:rgba(255,255,255,.55)}
@media (max-width:860px){.tbl{grid-template-columns:96px repeat(3,minmax(110px,1fr));overflow-x:auto}}
"""

WIDGET_JS = r"""
(function(){
var S=window.SHOP,$=function(s){return document.querySelector(s)};
var SETS={metro:['hp1','hp4','hp3'],sport:['hp5','hp1','hp4'],studio:['hp2','hp1','hp3']},use='metro',months=6;
var ROWS=['Шумодав','Батарея','Вес','Кодек','Мультипоинт'];
function draw(){var ids=SETS[use],ps=ids.map(function(i){return S.byId[i]}),h='<div class="lbl"></div>';
 ps.forEach(function(p,i){h+='<div class="hd'+(i===0?' best':'')+'"><div class="ph">'+S.img(p.img,'200px')+'</div>'+(i===0?'<span class="tag">Советуем</span>':'')+'<b>'+S.esc(p.n.replace('Наушники ',''))+'</b><span>'+S.fmt(p.p)+'</span><button class="add" type="button" data-add="'+p.id+'">В корзину</button></div>'});
 ROWS.forEach(function(r){h+='<div class="lbl">'+r+'</div>';ps.forEach(function(p,i){h+='<div class="'+(i===0?'best win':'')+'">'+S.esc(p.cmp[r])+'</div>'})});
 $('#cmpT').innerHTML=h;credit(ps[0])}
function credit(p){var m=Math.ceil(p.p/months);$('#crSum').textContent=S.fmt(m)+' в месяц';$('#crNote').textContent=p.n+' · '+months+' платежей без переплаты, решение банка за 2 минуты'}
$('#cmpUse').onclick=function(e){var b=e.target.closest('button');if(!b)return;use=b.dataset.u;this.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});draw()};
$('#crM').onclick=function(e){var b=e.target.closest('button');if(!b)return;months=+b.dataset.m;this.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});credit(S.byId[SETS[use][0]])};
draw();
})();
"""


def cfg():
    return {
        "slug": "shops/volt", "images": IMG, "brand": "Вольт",
        "logo": '<b style="font-style:italic">V</b>вольт',
        "title": "Вольт — наушники, колонки и гаджеты с рассрочкой 0%",
        "desc": "Наушники, колонки, умные часы и аксессуары. Сравнение моделей под задачу, рассрочка 0% до 12 месяцев, доставка завтра и 30 дней на возврат.",
        "variant": "mega", "favLetter": "V",
        "theme": {"bg": "#0b0c0f", "ink": "#f2f3f5", "soft": "#b4b8c0", "mut": "#7d828c", "line": "rgba(255,255,255,.09)", "line2": "rgba(255,255,255,.22)",
                  "card": "#16181d", "ac": "#5b7cff", "aci": "#fff", "ok": "#2fbf71", "rc": "22px", "rb": "14px", "rs": "28px",
                  "fh": '"Geist",system-ui,sans-serif', "fb": '"Geist",system-ui,sans-serif', "fm": '"Geist Mono",ui-monospace,monospace',
                  "hw": "600", "ht": "-.04em", "hc": "none", "emst": "normal", "ar": "1/1", "cardbg": "#14161b", "cpad": "16px", "cpadb": "16px",
                  "fot": "#050506", "fotx": "#f2f3f5", "star": "#5b7cff"},
        "fonts": [("Geist", "geist", [400, 500, 600, 700], "normal"), ("Geist Mono", "geist-mono", [400], "normal")],
        "strip": "Рассрочка <b>0% до 12 месяцев</b> · доставка завтра · 30 дней на возврат",
        "nav": [("Каталог", "catalog"), ("Сравнить", "feat"), ("Доставка", "why"), ("Вопросы", "faq")],
        "searchPh": "Наушники, колонка, часы…",
        "hero": {"kicker": "Новинка ноября", "h1": "Тишина, <em>которую слышно</em>", "img": "hero",
                 "lead": "Volt Air Max ANC: шумоподавление −42 дБ и 40 часов музыки. От 4 165 ₽ в месяц без переплаты.",
                 "cta": "Купить за 24 990 ₽", "ctaTo": "catalog", "cta2": "Сравнить модели", "cta2To": "feat",
                 "stats": [("−42 дБ", "шумоподавление"), ("40 ч", "без зарядки"), ("0%", "рассрочка")],
                 "tiles": [{"k": "Колонки", "t": "Volt Go −20% до воскресенья", "cat": "speakers", "img": "sp1", "a": "Смотреть →"},
                           {"k": "Часы", "t": "14 дней без зарядки", "cat": "wear", "img": "w1", "a": "Выбрать часы →"}]},
        "cats": [{"id": "audio", "n": "Наушники"}, {"id": "speakers", "n": "Колонки"}, {"id": "wear", "n": "Часы и браслеты"}, {"id": "acc", "n": "Аксессуары"}],
        "facets": {},
        "products": PRODUCTS, "pageSize": 12, "showStars": True, "cardSizes": "(max-width:860px) 50vw, 300px",
        "freeFrom": 3000, "promo": {"code": "VOLT", "pct": 5, "hint": "VOLT — минус 5% на первый заказ"},
        "ship": [{"id": "cour", "name": "Курьер", "eta": "завтра с 10 до 22", "price": 290, "free": 3000},
                 {"id": "pick", "name": "Самовывоз из магазина", "eta": "сегодня через 2 часа, м. Курская", "price": 0},
                 {"id": "post", "name": "Доставка по России", "eta": "2–6 дней", "price": 390}],
        "doneNote": "Пришлём SMS с номером для отслеживания.",
        "widget": {"nav": "Сравнить", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS},
        "usp": [("Рассрочка 0%", "До 12 месяцев без переплаты, решение за 2 минуты прямо в корзине."),
                ("30 дней на возврат", "Не понравилось — вернём деньги, даже если коробка вскрыта."),
                ("Официальная гарантия", "1 год гарантии производителя и сервис в Москве."),
                ("Проверка при получении", "Включите и послушайте у курьера, прежде чем платить.")],
        "uspTitle": "Покупать технику спокойно", "uspKick": "Сервис",
        "faq": [("Как работает рассрочка?", "В корзине выберите «Долями» или рассрочку на 3–12 месяцев. Банк одобряет за пару минут, переплаты нет — проценты платим мы."),
                ("Можно вернуть наушники?", "Да, в течение 30 дней, если они в порядке и с комплектом. Деньги вернём в день возврата."),
                ("Есть ли trade-in?", "Да, примем старые наушники или часы в зачёт новых: оценка по фото в чате за 10 минут."),
                ("Сколько идёт доставка?", "По Москве — завтра, курьер позвонит за час. Самовывоз с Курской — через 2 часа после заказа.")],
        "footBig": "Техника, которой приятно пользоваться",
        "contacts": {"addr": "Москва, Земляной Вал, 33", "hours": "Ежедневно 10:00–22:00"},
        "order": ["catalog", "widget", "usp", "faq"], "gridTitle": "Хиты недели", "gridKick": "Каталог",
        "css": ".v-mega .layout{grid-template-columns:minmax(0,1fr)}.v-mega .side{display:none}.v-mega .grid{--pc:4}.card{box-shadow:inset 0 0 0 1px var(--line)}"
               ".add{background:#f2f3f5;color:#0b0c0f}.hero h1 em{background:linear-gradient(90deg,#8aa2ff,#5b7cff 60%,#b28bff);-webkit-background-clip:text;background-clip:text;color:transparent}"
               ".top{background:color-mix(in srgb,var(--bg) 70%,transparent)}.v-mega .hero .tile{background:#16181d}.v-mega .hero .tile.dark{background:#1e2230;color:#f2f3f5}"
               ".sel{background-color:var(--card);color:var(--ink)}dialog{color:var(--ink)}.ph{background:#16181d}",
    }
