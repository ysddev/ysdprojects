"""«Сад и уголь» — меню гриль-ресторана: разворот RU/EN, фильтр аллергенов, носители."""

OLIVE, EMBER, CREAM, SOOT = "#3d4a2f", "#c8562b", "#f3ecdf", "#1f1c18"

AL = {"g": ("глютен", "gluten"), "l": ("лактоза", "lactose"), "n": ("орехи", "nuts"), "f": ("рыба", "fish"), "e": ("яйцо", "egg")}

MENU = [
    {"sec": ("С огня", "From the fire"), "items": [
        ("Шея свиная на углях", "Pork neck on charcoal", "маринад из печёного лука, соус из слив", "baked onion marinade, plum sauce", 870, "", "hit"),
        ("Каре ягнёнка", "Rack of lamb", "розмарин, печёный чеснок, йогурт с мятой", "rosemary, roasted garlic, mint yoghurt", 1940, "l", ""),
        ("Форель целиком", "Whole trout", "лимон, укроп, масло с каперсами", "lemon, dill, caper butter", 1180, "fl", ""),
        ("Кукуруза с углей", "Charred corn", "копчёная паприка, сыр брынза", "smoked paprika, feta-style cheese", 390, "l", "veg"),
        ("Баклажан на огне", "Fire-roasted aubergine", "тахини, гранат, кинза", "tahini, pomegranate, coriander", 520, "n", "veg"),
    ]},
    {"sec": ("Из сада", "From the garden"), "items": [
        ("Салат с печёной тыквой", "Roast pumpkin salad", "руккола, козий сыр, тыквенные семечки", "rocket, goat cheese, pumpkin seeds", 610, "l", "veg"),
        ("Томаты трёх сортов", "Three-tomato salad", "красный лук, зелёное масло, сухари", "red onion, herb oil, croutons", 540, "g", "veg"),
        ("Хумус с углей", "Ember hummus", "печёный перец, лаваш из печи", "roasted pepper, oven flatbread", 460, "gn", "veg"),
    ]},
    {"sec": ("К столу", "For the table"), "items": [
        ("Хлеб из печи", "Oven bread", "сливочное масло с зеленью", "herb butter", 230, "gl", ""),
        ("Соленья своего посола", "House pickles", "огурцы, капуста, черемша", "cucumbers, cabbage, wild garlic", 340, "", "veg"),
        ("Паштет из печени", "Chicken liver pâté", "брусничный джем, тосты", "lingonberry jam, toast", 480, "gle", ""),
    ]},
    {"sec": ("Сладкое", "Sweet"), "items": [
        ("Печёное яблоко", "Baked apple", "мёд, грецкий орех, сметанный крем", "honey, walnut, sour cream", 410, "nl", "hit"),
        ("Медовик с углей", "Smoked honey cake", "дымный крем, облепиха", "smoky cream, sea buckthorn", 470, "gle", ""),
    ]},
]


def sv(body, vb="0 0 480 300", bg="#e9e1d1"):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="{bg}"/>{body}</svg>'


def emblem(x, y, s=1.0, c=EMBER, leaf=OLIVE):
    return (f'<g transform="translate({x} {y}) scale({s})"><circle cx="40" cy="40" r="38" fill="none" stroke="{leaf}" stroke-width="2.4"/>'
            f'<path d="M40 64 C26 54 26 36 40 18 C54 36 54 54 40 64Z" fill="{c}"/><path d="M40 64 C34 56 35 46 40 38 C45 46 46 56 40 64Z" fill="#f2b04a"/>'
            f'<path d="M40 64 V72 M22 30 C28 30 32 34 34 40 M58 30 C52 30 48 34 46 40" stroke="{leaf}" stroke-width="2.4" fill="none" stroke-linecap="round"/></g>')


HERO = sv(
    '<rect x="70" y="40" width="250" height="400" rx="6" fill="#f3ecdf"/><rect x="320" y="40" width="250" height="400" rx="6" fill="#f7f1e6"/>'
    '<rect x="318" y="40" width="4" height="400" fill="#d9ccb4"/>' + emblem(155, 80, 1.0)
    + '<text x="195" y="210" text-anchor="middle" font-family="Prata" font-size="30" fill="#3d4a2f">Сад и уголь</text>'
      '<text x="195" y="236" text-anchor="middle" font-family="Commissioner" font-size="12" letter-spacing="3" fill="#8a7d63">ГРИЛЬ · ОГОРОД · ПЕЧЬ</text>'
    + "".join(f'<rect x="110" y="{290 + k * 22}" width="{150 - (k % 3) * 24}" height="5" rx="2" fill="#d9ccb4"/>' for k in range(6))
    + '<text x="345" y="92" font-family="Prata" font-size="20" fill="#3d4a2f">С огня</text>'
    + "".join(f'<rect x="345" y="{116 + k * 40}" width="{140 - (k % 2) * 30}" height="6" rx="3" fill="#3d4a2f" opacity=".75"/><rect x="345" y="{128 + k * 40}" width="{170 - (k % 3) * 20}" height="4" rx="2" fill="#cdbfa4"/>'
              f'<text x="545" y="{124 + k * 40}" text-anchor="end" font-family="Commissioner" font-size="12" fill="#c8562b">{p}</text>' for k, p in enumerate(["870", "1 940", "1 180", "390", "520", "610", "540"])),
    "0 0 640 480", "#e2d7c2")

CSS = r"""
.hero h1{font-size:clamp(44px,6.2vw,92px)}
.mbar{display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center;justify-content:space-between;margin-bottom:18px}
.alg{display:flex;flex-wrap:wrap;gap:8px;align-items:center}.alg small{color:var(--mut);font-size:14px;margin-right:4px}
.alg button{font:500 14px var(--fb);padding:8px 14px;border-radius:99px;border:1px solid var(--line2);background:var(--card);color:var(--ink);cursor:pointer}
.alg button.on{background:#7a2b14;border-color:#7a2b14;color:#fff;text-decoration:line-through}
.spread{display:grid;grid-template-columns:1fr 1fr;background:#f3ecdf;border-radius:10px;box-shadow:0 30px 60px -30px rgba(40,30,10,.45),0 0 0 1px #e0d4bd;position:relative;color:#2b261f}
.spread:before{content:"";position:absolute;left:50%;top:0;bottom:0;width:2px;background:linear-gradient(#d6c8ad,#e6dcc8,#d6c8ad);transform:translateX(-1px)}
.pg{padding:clamp(22px,4vw,54px);display:grid;gap:30px;align-content:start}
.pg section{display:grid;gap:18px}
.pg h3{font:400 clamp(24px,2.6vw,32px)/1.1 Prata,serif;color:#3d4a2f;display:flex;align-items:center;gap:14px}.pg h3:after{content:"";flex:1;height:1px;background:#cdbfa4}
.ds{display:grid;gap:16px}
.d{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:2px 16px;transition:opacity .3s,filter .3s}
.d b{font:500 17px var(--fb)}.d i{font-style:normal;font-size:14px;color:#7c705c;grid-column:1}.d em{font:500 16px var(--fb);font-style:normal;color:#c8562b;grid-row:1;grid-column:2}
.d .tg{grid-column:1;display:flex;gap:6px;flex-wrap:wrap}.d .tg span{font-size:11.5px;letter-spacing:.04em;padding:2px 8px;border-radius:99px;background:#e5dcc9;color:#5b5140}
.d .tg span.v{background:#dfe6cf;color:#3d4a2f}.d .tg span.h{background:#f5d9cb;color:#7a2b14}
.d.off{opacity:.28;filter:grayscale(1)}
.cnt{font-size:14px;color:var(--mut)}
.two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(18px,3vw,36px);align-items:center}
.two svg{border-radius:16px}.two ul{margin:0;padding-left:20px;display:grid;gap:10px;color:var(--soft)}
@media (max-width:860px){.spread{grid-template-columns:1fr}.spread:before{display:none}.pg+.pg{border-top:2px solid #d6c8ad}.two{grid-template-columns:1fr}}
"""

JS = r"""
(function(){var C=window.CASECFG,M=C.menu,AL=C.al,lang='ru',off={},sp=document.getElementById('spread'),al=document.getElementById('alg'),cnt=document.getElementById('cnt'),ls=document.getElementById('lang');
function sp_(n){return n.toLocaleString('ru-RU').replace(/ /g,' ')}
function word(n){var a=n%10,b=n%100;return a==1&&b!=11?'блюдо':a>=2&&a<=4&&(b<10||b>=20)?'блюда':'блюд'}
function draw(){var L=lang==='ru'?0:1,ok=0,all=0,h=['',''];M.forEach(function(s,i){var x='<section><h3>'+s.sec[L]+'</h3><div class="ds">';s.items.forEach(function(d){all++;var bad=d[5].split('').some(function(k){return off[k]});if(!bad)ok++;
var tg='';if(d[6]==='veg')tg+='<span class="v">'+(L?'vegetarian':'без мяса')+'</span>';if(d[6]==='hit')tg+='<span class="h">'+(L?'guest favourite':'любят гости')+'</span>';d[5].split('').forEach(function(k){if(k)tg+='<span>'+AL[k][L]+'</span>'});
x+='<div class="d'+(bad?' off':'')+'"><b>'+d[L]+'</b><em>'+sp_(d[4])+' ₽</em><i>'+d[2+L]+'</i><div class="tg">'+tg+'</div></div>'});h[i<2?0:1]+=x+'</div></section>'});
sp.innerHTML='<div class="pg">'+h[0]+'</div><div class="pg">'+h[1]+'</div>';
cnt.textContent=Object.keys(off).some(function(k){return off[k]})?(lang==='ru'?'Подходит '+ok+' '+word(ok)+' из '+all:ok+' of '+all+' dishes fit'):(lang==='ru'?all+' '+word(all)+' в меню':all+' dishes on the menu');
al.querySelectorAll('button').forEach(function(b){b.textContent=AL[b.dataset.k][L];b.classList.toggle('on',!!off[b.dataset.k])});al.querySelector('small').textContent=L?'Exclude:':'Без:';
ls.querySelectorAll('button').forEach(function(b){b.classList.toggle('on',b.dataset.l===lang)})}
al.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;off[b.dataset.k]=!off[b.dataset.k];draw()});
ls.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;lang=b.dataset.l;draw()});draw();
})();
"""

CARRIERS = [
    ("Тейбл-тент на стол", sv('<path d="M150 260 L200 60 H280 L330 260Z" fill="#f3ecdf"/><path d="M200 60 H280 L330 260 H150Z" fill="none" stroke="#cdbfa4"/>' + emblem(214, 84, .65)
                              + '<text x="240" y="170" text-anchor="middle" font-family="Prata" font-size="17" fill="#3d4a2f">Сезон тыквы</text>'
                              '<text x="240" y="192" text-anchor="middle" font-family="Commissioner" font-size="11" fill="#7c705c">до 30 ноября</text>'
                              '<text x="240" y="230" text-anchor="middle" font-family="Commissioner" font-size="13" fill="#c8562b">салат · 610 ₽</text>'), 4),
    ("Папка для счёта", sv('<rect x="150" y="40" width="180" height="230" rx="8" fill="#3d4a2f"/><rect x="150" y="40" width="14" height="230" rx="4" fill="#2f3a24"/>'
                           + emblem(208, 96, .82, c="#e07b4f", leaf="#e9e1d1") + '<text x="248" y="210" text-anchor="middle" font-family="Prata" font-size="18" fill="#f3ecdf">Сад и уголь</text>'), 4),
    ("Табличка на дверь", sv('<rect x="110" y="70" width="260" height="160" rx="80" fill="#1f1c18"/>' + emblem(140, 110, 1.0, c="#e07b4f", leaf="#c9b98f")
                             + '<text x="238" y="146" font-family="Prata" font-size="22" fill="#f3ecdf">Открыто</text>'
                             '<text x="238" y="172" font-family="Commissioner" font-size="12" fill="#c9b98f">12:00 — 23:30</text>'), 4),
    ("Барное меню A5", sv('<rect x="90" y="30" width="150" height="240" fill="#1f1c18"/><rect x="240" y="30" width="150" height="240" fill="#26221d"/>'
                          '<text x="110" y="70" font-family="Prata" font-size="17" fill="#f2b04a">Настойки</text>'
                          + "".join(f'<rect x="110" y="{92 + k * 26}" width="{90 - (k % 2) * 20}" height="5" rx="2" fill="#6b604e"/><text x="222" y="{98 + k * 26}" text-anchor="end" font-family="Commissioner" font-size="10" fill="#e07b4f">{p}</text>' for k, p in enumerate(["290", "340", "310", "380", "260", "420"]))
                          + '<text x="260" y="70" font-family="Prata" font-size="17" fill="#f2b04a">Морсы</text>'
                          + "".join(f'<rect x="260" y="{92 + k * 26}" width="{84 - (k % 3) * 14}" height="5" rx="2" fill="#6b604e"/>' for k in range(5)), bg="#d8cbb2"), 6),
    ("Наклейка на упаковку доставки", sv('<rect x="80" y="90" width="320" height="170" rx="8" fill="#b88b5a"/><path d="M80 90 L240 40 L400 90" fill="#a17749"/>'
                                         '<circle cx="240" cy="170" r="58" fill="#f3ecdf"/>' + emblem(206, 128, .85)
                                         + '<text x="240" y="250" text-anchor="middle" font-family="Commissioner" font-size="11" fill="#f3ecdf" letter-spacing="2">ГОРЯЧЕЕ · ОТКРЫТЬ ДОМА</text>'), 6),
]


def cfg() -> dict:
    n = sum(len(s["items"]) for s in MENU)
    spread = ('<div class="mbar"><div class="seg" id="lang"><button type="button" data-l="ru" class="on">RU</button><button type="button" data-l="en">EN</button></div>'
              '<div class="alg" id="alg"><small>Без:</small>' + "".join(f'<button type="button" data-k="{k}">{v[0]}</button>' for k, v in AL.items()) + '</div></div>'
              '<div class="spread" id="spread"></div><p class="cnt" id="cnt" style="margin-top:14px"></p>')
    ident = ('<div class="two"><div>' + sv(emblem(150, 40, 2.2) + '<text x="240" y="268" text-anchor="middle" font-family="Prata" font-size="26" fill="#3d4a2f">Сад и уголь</text>', bg="#f3ecdf")
             + '</div><ul><li>Знак — язычок огня, выросший из листа: гриль и свой огород в одной фигуре.</li>'
               '<li>Цвета взяты из кухни: оливковый — зелень с грядок, жжёная охра — угли, крем — бумага меню.</li>'
               '<li>Цены без «руб.» и копеек, блюда без лишних прилагательных: описание — это состав, а не реклама.</li>'
               '<li>Пометки «без мяса» и аллергены вынесены в метки, чтобы официант не пересказывал состав каждому гостю.</li></ul></div>')
    return {
        "slug": "design/sad", "brand": "Сад и уголь", "favLetter": "С",
        "title": "Сад и уголь — меню гриль-ресторана · YSD DEV",
        "desc": "Дизайн меню гриль-ресторана: разворот на двух языках, метки аллергенов и блюд без мяса, фирменный знак и носители — "
                "тейбл-тент, папка для счёта, барное меню, наклейка на доставку.",
        "theme": {"bg": "#efe8da", "ink": "#1f1c18", "soft": "#4c463b", "mut": "#82786a", "line": "#ddd2bd", "line2": "#c7b998",
                  "card": "#f8f3ea", "alt": "#e6ddca", "ac": "#3d4a2f", "aci": "#f3ecdf", "fh": "Prata,serif", "fb": "Commissioner,sans-serif",
                  "fm": "Commissioner,sans-serif", "hw": "400", "ht": "-.01em", "cbg": "#3d4a2f", "cink": "#f3ecdf", "cbtn": "#c8562b", "cbtni": "#fff", "rc": "#c8562b"},
        "fonts": [("Prata", "prata", [400], "normal"), ("Commissioner", "commissioner", [400, 500], "normal")],
        "css": CSS,
        "hero": {"kicker": "Меню ресторана", "h1": "Меню, в котором <em>легко выбрать</em>",
                 "lead": "Меню гриль-ресторана с собственным огородом. Гость за минуту находит блюдо без глютена или орехов, "
                         "иностранец читает тот же разворот на английском, а кухня меняет сезонные позиции без дизайнера.",
                 "art": HERO, "cta": "Открыть меню", "go": "menu"},
        "facts": [("Клиент", "«Сад и уголь», гриль-ресторан на 64 места"), ("Работа", "Меню, барная карта, знак и носители"),
                  ("Срок", "3 недели"), ("Позиций в меню", str(n))],
        "data": {"menu": MENU, "al": AL},
        "sections": [
            {"type": "html", "id": "menu", "nav": "Меню", "kick": "Разворот", "h2": "Попробуйте выбрать ужин",
             "lead": "Переключите язык и отметьте, что гостю нельзя, — неподходящие блюда погаснут.", "html": spread},
            {"type": "html", "id": "ident", "nav": "Знак", "kick": "Знак и правила", "h2": "Огонь, выросший из листа", "html": ident, "alt": True},
            {"type": "palette", "id": "color", "nav": "Цвет", "kick": "Цвет", "h2": "Цвета кухни", "lead": "Нажмите на цвет — код скопируется.",
             "colors": [("Олива", OLIVE, "заголовки, знак"), ("Жжёная охра", EMBER, "цены, акценты"), ("Крем", CREAM, "бумага меню"),
                        ("Сажа", SOOT, "барная карта"), ("Мёд", "#f2b04a", "сердце огня")]},
            {"type": "gallery", "id": "carriers", "nav": "Носители", "kick": "Носители", "h2": "Один стиль от стола до доставки", "alt": True,
             "items": [{"html": s, "cap": f"<b>{t}</b>", "span": sp, "ar": "8/5"} for t, s, sp in CARRIERS]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что изменилось после нового меню",
             "stats": [("−37%", "вопросов официанту о составе"), ("2 мин", "на выбор вместо 6 у нового гостя"), ("+14%", "заказов десертов"), ("1 час", "на замену сезонной позиции")]},
        ],
        "ctaTitle": "Нужно меню или стиль для ресторана?",
        "js": JS,
    }
