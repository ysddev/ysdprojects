"""«Вираж» — велосипеды и экипировка: подбор размера рамы по росту и стилю катания."""

IMG = {
    "hero": ("1534787238916-9ba6764efd4f", 16, 10, "900,1400,2000"),
    "r1": ("1532298229144-0ec0c57515c7", 4, 3, "500,900"),
    "r2": ("1786916901401-338c6ce2e6de", 4, 3, "500,900"),
    "r3": ("1576435728678-68d0fbf94e91", 4, 3, "500,900"),
    "m1": ("1600492110568-f9bf4835500a", 4, 3, "500,900"),
    "m2": ("1511994298241-608e28f14fde", 4, 3, "500,900"),
    "m3": ("1673121414328-52eff37bc6d0", 4, 3, "500,900"),
    "c1": ("1606310241970-4858d5d08f6b", 4, 3, "500,900"),
    "c2": ("1591047139334-337807f2b3e5", 4, 3, "500,900"),
    "c3": ("1523740856324-f2ce89135981", 4, 3, "500,900"),
    "c4": ("1484920274317-87885fcbc504", 4, 3, "500,900"),
    "g1": ("1785711922027-564ddf74a283", 4, 3, "500,900"),
    "h1": ("1701522814490-9d67fe9ab5b7", 4, 3, "500,900"),
    "h2": ("1702693008936-112724759019", 4, 3, "500,900"),
    "l1": ("1579118690145-7753994c2d56", 4, 3, "500,900"),
    "cage": ("1769445910141-37cd5a72981a", 4, 3, "500,900"),
    "glv": ("1645445470303-f96692cf1217", 4, 3, "500,900"),
}
FR = {"Размер рамы": ["S", "M", "L", "XL"]}


def P(id, n, cat, p, img, m, d, s, kind="", old=None, tag=None, nw=False, opts=None):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": s, "r": 4.6 + (len(n) % 4) / 10}
    if kind:
        x["kind"] = kind
        x["opts"] = FR
    if opts:
        x["opts"] = opts
    if old:
        x["old"] = old
    if tag:
        x["tag"] = tag
    if nw:
        x["nw"] = 1
    x["stock"] = "В наличии · соберём и настроим перед выдачей" if kind else "В наличии · доставка завтра"
    return x


PRODUCTS = [
    P("r1", "Шоссейный Вираж R1", "road", 89900, "r1", "Алюминий · 2×9 скоростей", "Первый шоссейный велосипед: устойчивая геометрия и надёжное оборудование.",
      [["Рама", "алюминий"], ["Вес", "9,8 кг"], ["Тормоза", "дисковые механические"]], kind="road", tag="Хит"),
    P("r2", "Шоссейный Вираж R3 Carbon", "road", 214000, "r2", "Карбон · 2×11 скоростей", "Карбоновая рама и вилка: быстрый набор скорости и комфорт на длинной дистанции.",
      [["Рама", "карбон"], ["Вес", "8,1 кг"], ["Тормоза", "дисковые гидравлические"]], kind="road", nw=True),
    P("r3", "Шоссейный Вираж Classic", "road", 74900, "r3", "Сталь · 2×8 скоростей", "Стальная рама гасит вибрации: для тренировок и поездок на выходных.",
      [["Рама", "хромомолибденовая сталь"], ["Вес", "10,6 кг"]], kind="road"),
    P("m1", "Горный Вираж Trail 29", "mtb", 96900, "m1", "Хардтейл · вилка 120 мм", "Колёса 29 дюймов и воздушная вилка: лес, грунт и корни.",
      [["Рама", "алюминий"], ["Вилка", "воздушная, 120 мм"], ["Передачи", "1×12"]], kind="mtb", tag="Хит"),
    P("m2", "Горный Вираж Enduro", "mtb", 189000, "m2", "Двухподвес · ход 150 мм", "Для трасс со спусками: уверенно держит траекторию на камнях.",
      [["Рама", "алюминий"], ["Ход подвески", "150 мм"], ["Передачи", "1×12"]], kind="mtb"),
    P("m3", "Горный Вираж XC", "mtb", 67900, "m3", "Хардтейл · вилка 100 мм", "Лёгкий и накатистый: для длинных прогулок по пересечённой местности.",
      [["Рама", "алюминий"], ["Вилка", "100 мм"], ["Передачи", "2×9"]], kind="mtb", old=74900),
    P("c1", "Городской Вираж City 7", "city", 42900, "c1", "Планетарная втулка · 7 скоростей", "Крылья, багажник и защита цепи в комплекте: сел и поехал на работу.",
      [["Рама", "алюминий"], ["Передачи", "планетарная втулка, 7"], ["Комплект", "крылья, багажник, подножка"]], kind="city"),
    P("c2", "Городской Вираж Urban", "city", 38900, "c2", "8 скоростей · V-brake", "Простая и лёгкая городская модель с прямым рулём.",
      [["Рама", "алюминий"], ["Вес", "11,9 кг"]], kind="city"),
    P("c3", "Круизер Вираж Bay", "city", 34900, "c3", "Низкая рама · 3 скорости", "Широкое седло, высокий руль и корзина: для набережной и парка.",
      [["Рама", "сталь"], ["Комплект", "корзина, крылья"]], kind="city"),
    P("c4", "Синглспид Вираж One", "city", 31900, "c4", "Одна передача · флип-флоп", "Нечему ломаться: одна передача и минимум обслуживания.",
      [["Рама", "сталь"], ["Вес", "10,2 кг"]], kind="city", nw=True),
    P("g1", "Гравийный Вираж Tour", "gravel", 124900, "g1", "Алюминий · 1×11 · покрышки 40 мм", "Асфальт, грунт и багаж: крепления для сумок и трёх фляг.",
      [["Рама", "алюминий"], ["Вилка", "карбон"], ["Покрышки", "700×40"]], kind="gravel", tag="Для путешествий"),
    P("h1", "Шлем Вираж Aero", "gear", 8900, "h1", "260 г · 18 вентиляционных каналов", "Лёгкий шоссейный шлем с системой регулировки одной рукой.",
      [["Вес", "260 г"]], opts={"Размер": ["S/M", "L/XL"]}),
    P("h2", "Шлем Вираж Trail", "gear", 7400, "h2", "С козырьком", "Закрывает затылок глубже шоссейного: для леса и грунта.",
      [["Вес", "310 г"]], opts={"Размер": ["S/M", "L/XL"]}),
    P("l1", "Фонарь передний 800 лм", "gear", 3900, "l1", "USB-C · до 12 часов", "Пять режимов, крепление без инструмента, не боится дождя.",
      [["Яркость", "800 лм"], ["Защита", "IPX6"]]),
    P("cage", "Флягодержатель алюминиевый", "gear", 890, "cage", "38 г", "Держит флягу на грунте и брусчатке.",
      [["Вес", "38 г"]]),
    P("glv", "Перчатки с гелевыми вставками", "gear", 2400, "glv", "Короткие пальцы", "Снимают нагрузку с ладоней на длинных поездках.",
      [["Материал", "лайкра, гель"]], opts={"Размер": ["S", "M", "L", "XL"]}),
]

WIDGET_HTML = """
<div class="fit">
 <div>
  <div class="kick">Подбор размера</div>
  <h2 style="margin:12px 0 12px">Рама под ваш рост <em>за 10 секунд</em></h2>
  <p class="lead" style="font-size:17px">Укажите рост и где собираетесь кататься. Покажем размер рамы и велосипеды, которые есть в этом размере.</p>
  <div class="gq"><b>Рост · <span id="ftH">176 см</span></b><input type="range" id="ftR" min="150" max="200" value="176"></div>
  <div class="gq"><b>Где катаетесь</b><div class="gtags" id="ftK"><button data-k="city" aria-pressed="true">Город</button><button data-k="road" aria-pressed="false">Шоссе</button><button data-k="mtb" aria-pressed="false">Лес и горы</button><button data-k="gravel" aria-pressed="false">Грунт и походы</button></div></div>
  <div class="ftsize"><div><span>Размер рамы</span><b id="ftS">M</b></div><div><span>Ростовка</span><b id="ftC">54 см</b></div><div><span>Высота седла</span><b id="ftD">75 см</b></div></div>
  <p class="ftnote">Между двумя размерами берите меньший для манёвренности и больший для дальних поездок. Перед выдачей настроим посадку под вас.</p>
 </div>
 <div class="ftres" id="ftRes" aria-live="polite"></div>
</div>"""

WIDGET_CSS = """
.fit{display:grid;grid-template-columns:1fr 1.05fr;gap:clamp(24px,4vw,56px);align-items:start}
.fit h2 em{font-style:normal;color:var(--ac)}
.gq{margin-top:22px}
.gq b{display:block;font-size:15px;font-weight:600;margin-bottom:10px}
.fit input[type=range]{width:100%;accent-color:var(--ac)}
.gtags{display:flex;gap:8px;flex-wrap:wrap}
.gtags button{height:44px;padding:0 16px;border-radius:var(--rb);background:var(--bg);font-weight:600;font-size:15px;box-shadow:inset 0 0 0 1px var(--line2)}
.gtags button[aria-pressed=true]{background:var(--ink);color:var(--bg);box-shadow:none}
.ftsize{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:24px}
.ftsize div{background:var(--bg);border-radius:var(--rc);padding:14px 16px}
.ftsize span{display:block;font-size:13px;color:var(--mut)}
.ftsize b{font-family:var(--fh);font-size:34px;line-height:1.1;font-style:italic}
.ftnote{margin:16px 0 0;font-size:14px;color:var(--soft)}
.ftres{display:grid;gap:12px}
.ftres .fi{display:grid;grid-template-columns:150px 1fr;gap:16px;background:var(--bg);border-radius:var(--rc);padding:12px;align-items:center}
.ftres .fi .ph{aspect-ratio:4/3;border-radius:calc(var(--rc) - 4px);cursor:pointer}
.ftres .fi b{display:block;font-size:17px;line-height:1.25}
.ftres .fi small{display:block;color:var(--mut);font-size:13.5px;margin:3px 0 10px}
.ftres .fi .row{display:flex;justify-content:space-between;align-items:center;gap:10px;flex-wrap:wrap}
@media (max-width:860px){.fit{grid-template-columns:1fr}.ftres .fi{grid-template-columns:110px 1fr}}
"""

WIDGET_JS = r"""
(function(){
var S=window.SHOP,$=function(s){return document.querySelector(s)},kind='city';
function size(h){return h<165?'S':h<178?'M':h<189?'L':'XL'}
function draw(){var h=+$('#ftR').value,s=size(h),k={road:.665,gravel:.66,city:.64,mtb:.56}[kind];
 $('#ftH').textContent=h+' см';$('#ftS').textContent=s;
 $('#ftC').textContent=kind==='mtb'?String(Math.round((h*0.226-21.5)*2)/2).replace('.',',')+'″':Math.round(h*0.47*k)+' см';
 $('#ftD').textContent=Math.round(h*0.47*0.885)+' см';
 var r=S.products.filter(function(p){return p.kind===kind}).slice(0,3);
 $('#ftRes').innerHTML=r.map(function(p){return'<div class="fi"><div class="ph" data-open="'+p.id+'">'+S.img(p.img,'(max-width:860px) 110px, 150px')+'</div><div><b>'+S.esc(p.n)+'</b><small>'+S.esc(p.m)+'</small><div class="row"><span class="price" style="font-size:18px">'+S.fmt(p.p)+'</span><button class="add" type="button" data-fit="'+p.id+'">В корзину · '+s+'</button></div></div></div>'}).join('')}
$('#ftR').addEventListener('input',draw);
$('#ftK').onclick=function(e){var b=e.target.closest('button');if(!b)return;kind=b.dataset.k;this.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});draw()};
$('#ftRes').addEventListener('click',function(e){var b=e.target.closest('[data-fit]');if(!b)return;S.add(b.dataset.fit,{'Размер рамы':size(+$('#ftR').value)},1)});
draw();
})();
"""


def cfg():
    return {
        "slug": "shops/virazh", "images": IMG, "brand": "Вираж",
        "logo": '<b style="background:#f0361f;color:#fff;font-style:italic;border-radius:6px">В</b>ВИРАЖ',
        "title": "Вираж — велосипеды и экипировка с подбором размера рамы",
        "desc": "Шоссейные, горные, городские и гравийные велосипеды, шлемы и аксессуары. Подбор размера рамы по росту, сборка и настройка перед выдачей, рассрочка.",
        "variant": "mega", "favLetter": "В",
        "theme": {"bg": "#f4f4f1", "ink": "#121413", "soft": "#3d423f", "mut": "#7c827e", "line": "rgba(18,20,19,.12)", "line2": "rgba(18,20,19,.28)",
                  "card": "#e8e8e3", "ac": "#f0361f", "aci": "#fff", "ac2": "#f0361f", "ok": "#1b7f3a", "rc": "14px", "rb": "10px", "rs": "20px",
                  "fh": '"Sofia Sans Condensed",Impact,sans-serif', "fb": '"Inter Tight",system-ui,sans-serif', "fm": '"Inter Tight",system-ui,sans-serif',
                  "hw": "800", "ht": "-.01em", "hc": "uppercase", "emst": "italic", "ar": "4/3", "cardbg": "#fff", "cpad": "12px", "cpadb": "14px",
                  "fot": "#121413", "fotx": "#f4f4f1"},
        "fonts": [("Sofia Sans Condensed", "sofia-sans-condensed", [800], "normal"), ("Sofia Sans Condensed", "sofia-sans-condensed", [800], "italic"),
                  ("Inter Tight", "inter-tight", [400, 500, 600], "normal")],
        "strip": "Сборка и настройка <b>бесплатно</b> · рассрочка 0% на 6 месяцев · первое ТО в подарок",
        "nav": [("Каталог", "catalog"), ("Подбор размера", "feat"), ("Сервис", "why"), ("Вопросы", "faq")],
        "searchPh": "Шоссейный, шлем, фонарь…",
        "hero": {"kicker": "Велосипеды и экипировка · Москва", "h1": "Ваш размер, ваш маршрут, <em>ваш вираж</em>", "img": "hero",
                 "lead": "Подберём раму по росту, соберём и настроим велосипед под вас. Первое техобслуживание через месяц бесплатно.",
                 "cta": "Подобрать размер", "ctaTo": "feat", "cta2": "Каталог", "cta2To": "catalog",
                 "stats": [("4", "типа велосипедов"), ("0%", "рассрочка на 6 месяцев"), ("1 день", "сборка и настройка")],
                 "tiles": [{"k": "Горные", "t": "Вираж XC: −7 000 ₽ до конца месяца", "cat": "mtb", "img": "m3", "a": "Смотреть →"},
                           {"k": "Экипировка", "t": "Шлем к велосипеду со скидкой 15%", "cat": "gear", "img": "h1", "a": "Выбрать шлем →"}]},
        "cats": [{"id": "road", "n": "Шоссейные"}, {"id": "mtb", "n": "Горные"}, {"id": "city", "n": "Городские"}, {"id": "gravel", "n": "Гравийные"},
                 {"id": "gear", "n": "Экипировка"}],
        "facets": {},
        "products": PRODUCTS, "pageSize": 12, "showStars": True, "cardSizes": "(max-width:860px) 50vw, 300px",
        "freeFrom": 20000, "promo": {"code": "ВИРАЖ", "pct": 5, "hint": "ВИРАЖ — минус 5% на экипировку"},
        "ship": [{"id": "cour", "name": "Курьер, собранный велосипед", "eta": "послезавтра, настроим на месте", "price": 990, "free": 20000},
                 {"id": "pick", "name": "Самовывоз из мастерской", "eta": "завтра после сборки, м. Спортивная", "price": 0},
                 {"id": "post", "name": "Доставка по России", "eta": "3–7 дней, в коробке, собран на 90%", "price": 2490}],
        "doneNote": "Механик позвонит, уточнит рост и соберёт велосипед под вас.",
        "widget": {"nav": "Подбор размера", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS},
        "usp": [("Сборка и настройка", "Механик собирает велосипед, выставляет переключатели и тормоза, подгоняет седло и руль."),
                ("Первое ТО бесплатно", "Через месяц подтянем тросы и спицы: после обкатки это нужно каждому велосипеду."),
                ("Тест-драйв", "В мастерской можно проехать на двух размерах и выбрать свой."),
                ("Рассрочка 0%", "На 6 месяцев без переплаты, оформление в корзине за пару минут.")],
        "uspTitle": "Не просто коробка с велосипедом", "uspKick": "Сервис",
        "faq": [("Как выбрать размер рамы?", "Укажите рост в подборе размера. Если вы между двумя размерами, приезжайте на тест-драйв или напишите нам длину ноги по внутреннему шву."),
                ("Велосипед приедет собранным?", "По Москве привозим полностью собранным и настроенным. В регионы отправляем в коробке: остаётся поставить руль, переднее колесо и педали."),
                ("Что входит в первое ТО?", "Подтяжка тросов и спиц, проверка тормозов и переключателей, смазка цепи. Занимает около часа."),
                ("Можно вернуть, если не подошёл?", "Да, в течение 14 дней, если на велосипеде нет следов эксплуатации. Размер поменяем без доплаты.")],
        "footBig": "Катайтесь больше",
        "contacts": {"addr": "Москва, ул. Усачёва, 11", "hours": "Ежедневно 10:00–21:00"},
        "order": ["catalog", "widget", "usp", "faq"], "gridTitle": "Велосипеды и экипировка", "gridKick": "Каталог",
        "css": ".v-mega .layout{grid-template-columns:minmax(0,1fr)}.v-mega .side{display:none}.v-mega .grid{--pc:4}.hero h1{font-size:clamp(48px,6.6vw,104px);line-height:.9}"
               ".v-mega .hero h1 em{color:var(--ac)}.add{background:var(--ink);color:var(--bg)}.logo{font-family:var(--fh);font-style:italic;font-size:26px}.strip b{color:#ff9a8c}",
    }
