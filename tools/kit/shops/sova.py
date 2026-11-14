"""«Сова и кубик» — детские игрушки: подбор подарка по возрасту и интересам, подарочная упаковка."""

IMG = {
    "b1": ("1777351396220-9a3801de44df", 1, 1, "500,900,1300"),
    "b2": ("1703581698778-2224c729135b", 1, 1, "400,800"),
    "b3": ("1560859251-d563a49c5e4a", 1, 1, "300,600"),
    "train": ("1769072385024-c962e061c523", 1, 1, "500,900"),
    "blocks": ("1777351396220-9a3801de44df", 1, 1, "500,900"),
    "eleph": ("1703581698778-2224c729135b", 1, 1, "500,900"),
    "clay": ("1536293182766-c9c0c4133b55", 1, 1, "500,900"),
    "cars": ("1560859251-d563a49c5e4a", 1, 1, "500,900"),
    "sorter": ("1774464593838-85b320eb7453", 1, 1, "500,900"),
    "plastic": ("1618842676088-c4d48a6a7c9d", 1, 1, "500,900"),
    "books": ("1777351395942-96046820ddc6", 1, 1, "500,900"),
    "chess": ("1611957082141-c449bb2b4ada", 1, 1, "500,900"),
    "plush": ("1772374998418-3c029939ef6b", 1, 1, "500,900"),
    "plush2": ("1767522247688-a4d70b72fd0c", 1, 1, "500,900"),
    "wblocks": ("1568828668638-b1b4014d91a2", 1, 1, "500,900"),
    "draw": ("1770096679916-2cd9c720d400", 1, 1, "500,900"),
    "craft": ("1613950190144-4f2a84c75e8c", 1, 1, "500,900"),
}


def P(id, n, cat, p, img, m, d, s, age, tags, old=None, tag=None, nw=False):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": s, "age": age, "it": tags}
    if old:
        x["old"] = old
    if tag:
        x["tag"] = tag
    if nw:
        x["nw"] = 1
    x["stock"] = "В наличии · упакуем в подарок бесплатно"
    return x


PRODUCTS = [
    P("p1", "Сортер «Домик» из бука", "wood", 2490, "sorter", "1–3 года",
      "Шесть фигур и шесть отверстий: учит формы и цвета. Краски на водной основе.", [["Возраст", "1–3 года"], ["Материал", "бук"]], [1, 3], ["logic", "baby"], tag="Хит"),
    P("p2", "Набор кубиков, 50 деталей", "wood", 3290, "blocks", "Массив берёзы",
      "Строят башни, гаражи и замки годами — кубики не ломаются.", [["Деталей", "50"]], [1, 6], ["build", "baby"]),
    P("p3", "Паровозик-алфавит", "wood", 2890, "train", "Буквы на колёсах",
      "Вагончики с буквами — собираете имя ребёнка.", [["Деталей", "33"]], [2, 5], ["logic", "baby"], nw=True),
    P("p4", "Слоники-балансиры, 3 шт.", "wood", 1590, "eleph", "Ручная работа",
      "Ставите друг на друга — тренирует мелкую моторику и терпение.", [["Возраст", "3+"]], [3, 7], ["logic"]),
    P("p5", "Машинки гоночные, набор из 5", "cars", 1990, "cars", "Металл · инерционные",
      "Пять ярких болидов с инерционным механизмом.", [["Масштаб", "1:43"]], [3, 8], ["cars"], old=2490),
    P("p6", "Тесто для лепки «Радуга», 12 цветов", "creative", 990, "clay", "Мягкое, не сохнет",
      "Не липнет к рукам и не пачкает одежду.", [["Цветов", "12"]], [2, 8], ["create"]),
    P("p7", "Набор для творчества «Аппликация»", "creative", 1490, "craft", "Бумага, клей, ножницы",
      "200 деталей для аппликаций и безопасные ножницы.", [["Деталей", "200"]], [4, 9], ["create"]),
    P("p8", "Мольберт двусторонний", "creative", 4990, "draw", "Мел и маркер",
      "С одной стороны грифельная доска, с другой — маркерная.", [["Высота", "до 120 см"]], [3, 9], ["create"], nw=True),
    P("p9", "Шахматы детские с обучалкой", "games", 2190, "chess", "Карточки-подсказки",
      "Крупные фигуры и 30 карточек: как ходит каждая фигура.", [["Возраст", "5+"]], [5, 12], ["logic"]),
    P("p10", "Мягкие игрушки «Лесные друзья»", "plush", 1890, "plush", "Набор из 3",
      "Гипоаллергенный наполнитель, можно стирать в машинке.", [["Высота", "25 см"]], [0, 6], ["baby", "plush"], tag="Подарок"),
    P("p11", "Плюшевый кот Персик", "plush", 1290, "plush2", "30 см",
      "Мягкий кот, с которым удобно спать.", [["Высота", "30 см"]], [0, 8], ["plush"]),
    P("p12", "Конструктор «Город», 120 деталей", "games", 3990, "plastic", "Совместим с популярными",
      "Дома, дороги и человечки — строят город и придумывают истории.", [["Деталей", "120"]], [4, 10], ["build"]),
    P("p13", "Книжки-картонки, набор из 4", "games", 1190, "books", "Для самых маленьких",
      "Плотные страницы, которые не порвать.", [["Страниц", "по 12"]], [0, 3], ["baby"]),
    P("p14", "Деревянные бруски-конструктор", "wood", 2590, "wblocks", "60 деталей",
      "Натуральное дерево без покраски — для архитекторов.", [["Деталей", "60"]], [3, 10], ["build"]),
]

WIDGET_HTML = """
<div class="gift">
 <div>
  <div class="kick">Подбор подарка</div>
  <h2 style="margin:12px 0 12px">Что подарить, если <em>не знаете, что подарить</em></h2>
  <p class="lead" style="font-size:17px">Возраст и что ребёнок любит — покажем игрушки, которые точно не будут пылиться на полке.</p>
  <div class="gq"><b>Возраст · <span id="gA">4 года</span></b><input type="range" id="gAge" min="0" max="12" value="4"></div>
  <div class="gq"><b>Любит</b><div class="gtags" id="gT"><button data-t="build" aria-pressed="true">🧱 Строить</button><button data-t="create" aria-pressed="false">🎨 Творить</button><button data-t="logic" aria-pressed="false">🧩 Думать</button><button data-t="cars" aria-pressed="false">🚗 Машинки</button><button data-t="plush" aria-pressed="false">🧸 Обниматься</button></div></div>
  <div class="gq"><b>Бюджет до · <span id="gB">3 000 ₽</span></b><input type="range" id="gBud" min="1000" max="6000" step="500" value="3000"></div>
  <label class="gwrap"><input type="checkbox" id="gWrap" checked> Упаковать в подарок и вложить открытку <span>бесплатно</span></label>
 </div>
 <div class="gres" id="gRes" aria-live="polite"></div>
</div>"""

WIDGET_CSS = """
#feat .feat{--fbg:#e9f3ff}
.gift{display:grid;grid-template-columns:1fr 1.1fr;gap:clamp(24px,4vw,56px)}
.gift h2 em{font-style:normal;color:var(--ac)}
.gq{margin-top:22px}
.gq b{display:block;font-size:15px;font-weight:700;margin-bottom:10px}
.gift input[type=range]{width:100%;accent-color:var(--ac)}
.gtags{display:flex;gap:8px;flex-wrap:wrap}
.gtags button{height:44px;padding:0 16px;border-radius:999px;background:#fff;font-weight:600;font-size:15px;box-shadow:0 3px 0 rgba(0,0,0,.06)}
.gtags button[aria-pressed=true]{background:var(--ac);color:#fff}
.gwrap{display:flex;gap:10px;align-items:center;margin-top:22px;font-weight:600;cursor:pointer}
.gwrap input{width:20px;height:20px;accent-color:var(--ac)}
.gwrap span{color:var(--ok);font-size:14px}
.gres{display:grid;grid-template-columns:1fr 1fr;gap:12px;align-content:start}
.gres .gi{background:#fff;border-radius:22px;padding:12px;display:flex;flex-direction:column;gap:8px;box-shadow:0 20px 40px -30px rgba(30,60,120,.4)}
.gres .gi .ph{aspect-ratio:1;border-radius:16px}
.gres .gi b{font-size:15px;line-height:1.25}
.gres .gi .row{display:flex;justify-content:space-between;align-items:center;margin-top:auto}
.gres .none{grid-column:1/-1;background:#fff;border-radius:22px;padding:28px;text-align:center;color:var(--soft)}
@media (max-width:860px){.gift{grid-template-columns:1fr}}
"""

WIDGET_JS = r"""
(function(){
var S=window.SHOP,$=function(s){return document.querySelector(s)},tags=['build'];
function yr(n){return n===0?'до года':n+' '+(n%10===1&&n!==11?'год':n%10>1&&n%10<5&&(n<10||n>20)?'года':'лет')}
function draw(){var a=+$('#gAge').value,bud=+$('#gBud').value;$('#gA').textContent=yr(a);$('#gB').textContent=S.fmt(bud);
 var r=S.products.filter(function(p){return a>=p.age[0]&&a<=p.age[1]&&p.p<=bud}).map(function(p){return[p.it.filter(function(t){return tags.indexOf(t)>=0}).length,p]}).sort(function(x,y){return y[0]-x[0]||x[1].p-y[1].p}).slice(0,4);
 $('#gRes').innerHTML=r.length?r.map(function(x){var p=x[1];return'<div class="gi"><div class="ph" data-open="'+p.id+'" style="cursor:pointer">'+S.img(p.img,'(max-width:860px) 45vw, 260px')+'</div><b>'+S.esc(p.n)+'</b><div class="row"><span class="price" style="font-size:17px">'+S.fmt(p.p)+'</span><button class="add" type="button" data-gift="'+p.id+'">Подарить</button></div></div>'}).join(''):'<div class="none">В этом бюджете для такого возраста ничего не нашли — подвиньте бюджет чуть выше.</div>'}
$('#gT').onclick=function(e){var b=e.target.closest('button');if(!b)return;var t=b.dataset.t,i=tags.indexOf(t);if(i>=0){if(tags.length>1)tags.splice(i,1)}else tags.push(t);this.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',tags.indexOf(x.dataset.t)>=0)});draw()};
['#gAge','#gBud'].forEach(function(id){$(id).addEventListener('input',draw)});
$('#gRes').addEventListener('click',function(e){var b=e.target.closest('[data-gift]');if(!b)return;S.add(b.dataset.gift,$('#gWrap').checked?{'Упаковка':'подарочная + открытка'}:{},1)});
draw();
})();
"""


def cfg():
    return {
        "slug": "shops/sova", "images": IMG, "brand": "Сова и кубик",
        "logo": '<b style="background:#ffcf33;color:#1d2b4f">🦉</b>сова и кубик',
        "title": "Сова и кубик — развивающие игрушки из дерева и подарки детям",
        "desc": "Деревянные игрушки, конструкторы и наборы для творчества. Подбор подарка по возрасту и интересам, бесплатная подарочная упаковка и доставка завтра.",
        "variant": "play", "favLetter": "С",
        "theme": {"bg": "#fbfcff", "ink": "#1d2b4f", "soft": "#4a5878", "mut": "#8a94ab", "line": "rgba(29,43,79,.1)", "line2": "rgba(29,43,79,.25)",
                  "card": "#eef3fb", "ac": "#ff5d73", "aci": "#fff", "ac2": "#ffcf33", "ok": "#22a06b", "rc": "24px", "rb": "999px", "rs": "40px", "hbg": "#fff1c7",
                  "fh": '"Geologica",system-ui,sans-serif', "fb": '"Golos Text",system-ui,sans-serif', "fm": '"Golos Text",system-ui,sans-serif',
                  "hw": "800", "ht": "-.03em", "hc": "none", "lw": "800", "lt": "-.02em", "ar": "1/1", "cardbg": "#fff", "cpad": "14px", "cpadb": "14px", "rl": "50%"},
        "fonts": [("Geologica", "geologica", [600, 800], "normal") if False else ("Geologica", "geologica", [600, 700, 900], "normal"), ("Golos Text", "golos-text", [400, 500, 600, 700], "normal")],
        "strip": "Подарочная упаковка <b>бесплатно</b> · доставка завтра · обмен 30 дней",
        "nav": [("Каталог", "catalog"), ("Подбор подарка", "feat"), ("Доставка", "why"), ("Вопросы", "faq")],
        "searchPh": "Сортер, кубики, шахматы…",
        "hero": {"kicker": "Игрушки, которые не надоедают", "h1": "Играть — это <em>серьёзно</em>", "bubbles": ["b1", "b2", "b3"], "img": "b1",
                 "lead": "Деревянные игрушки, конструкторы и наборы для творчества, которые развивают и не ломаются через неделю. Упакуем в подарок бесплатно.",
                 "cta": "Подобрать подарок", "ctaTo": "feat", "cta2": "Каталог", "cta2To": "catalog",
                 "stats": [("0+", "от рождения"), ("бук и берёза", "натуральное дерево"), ("30 дней", "на обмен")]},
        "cats": [{"id": "wood", "n": "Деревянные", "s": "сортеры, кубики", "img": "sorter"}, {"id": "creative", "n": "Творчество", "s": "лепка, рисование", "img": "clay"},
                 {"id": "games", "n": "Игры и конструкторы", "img": "chess", "s": "для 4+"}, {"id": "plush", "n": "Мягкие", "img": "plush", "s": "для обнимашек"},
                 {"id": "cars", "n": "Машинки"}],
        "catsTitle": "Для любого возраста",
        "products": PRODUCTS, "pageSize": 8, "showStars": True, "cardSizes": "(max-width:860px) 50vw, 25vw",
        "freeFrom": 3000, "promo": {"code": "ПОДАРОК", "pct": 10, "hint": "ПОДАРОК — минус 10% на первый заказ"},
        "ship": [{"id": "cour", "name": "Курьер", "eta": "завтра в удобный интервал", "price": 290, "free": 3000},
                 {"id": "pvz", "name": "Пункт выдачи", "eta": "1–4 дня по России", "price": 199, "free": 3000},
                 {"id": "pick", "name": "Самовывоз из магазина", "eta": "Москва, Ленинский пр., 30", "price": 0}],
        "commentPh": "Если это сюрприз — напишите, кому позвонит курьер",
        "doneNote": "Упакуем в подарочную бумагу и пришлём фото до отправки.",
        "widget": {"nav": "Подбор подарка", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS},
        "usp": [("Безопасные материалы", "Бук, берёза и краски на водной основе — с сертификатами."),
                ("Упаковка в подарок", "Бесплатно: крафт, лента и открытка с вашим текстом."),
                ("Обмен 30 дней", "Подарили второй такой же — поменяем на другую игрушку."),
                ("По возрасту", "На каждой карточке — для какого возраста и что развивает.")],
        "uspTitle": "Родителям спокойно, детям интересно", "uspKick": "Почему мы",
        "faq": [("Безопасны ли игрушки для малышей?", "Да: натуральное дерево, краски на водной основе и мелкие детали только в наборах 3+. Сертификаты пришлём по запросу."),
                ("Можно обменять, если подарили такую же?", "Да, в течение 30 дней, если игрушка не использовалась и цела упаковка."),
                ("Упакуете в подарок?", "Бесплатно: крафтовая бумага, лента и открытка. Отметьте в корзине или напишите в комментарии."),
                ("Доставите ко дню рождения?", "Да, курьер привезёт в выбранный день и интервал. Можно доставить имениннику напрямую — без чека в коробке.")],
        "footBig": "Пусть дома будет интересно",
        "contacts": {"addr": "Москва, Ленинский пр., 30", "hours": "Ежедневно 10:00–21:00"},
        "order": ["cats", "catalog", "widget", "usp", "faq"], "gridTitle": "Любимые игрушки", "catCols": 4,
        "css": ".hero h1{font-size:clamp(46px,7vw,104px);line-height:.95}.v-play .hero h1 em{color:var(--ac)}.cats .cat:nth-child(n+5){display:none}"
               ".add{background:var(--ac);color:#fff}.logo b{font-size:20px}",
    }
