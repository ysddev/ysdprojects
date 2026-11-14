"""«Лист» — чайная лавка: подбор чая по вкусу (крепость, бодрость, вкус, время дня) и коробка-подписка."""

IMG = {
    "hero": ("1766232578337-ff7bdb6d1f8b", 4, 5, "700,1100,1500"),
    "spoons": ("1563822249366-3efb23b8e0c9", 4, 5, "500,900"),
    "pots": ("1766232574096-4c4380105cc7", 4, 5, "500,900"),
    "pots2": ("1766232578330-14018a51e69f", 4, 5, "500,900"),
    "cups": ("1765153743332-949b8d623d92", 4, 5, "500,900,1300"),
    "green": ("1763617702099-d956f3fd8324", 4, 5, "500,900"),
    "mug": ("1571934811356-5cc061b6821f", 4, 5, "500,900"),
    "herbs": ("1653937855510-ec3fd2036d98", 4, 5, "500,900"),
    "jars": ("1563911892437-1feda0179e1b", 4, 5, "500,900"),
    "dry": ("1628153792464-21bffac488d4", 4, 5, "500,900"),
    "beans": ("1447933601403-0c6688de566e", 4, 5, "500,900"),
    "latte": ("1509042239860-f550ce710b93", 4, 5, "500,900"),
    "fruit": ("1608036586781-26f0d5debbee", 4, 5, "500,900"),
}


def P(id, n, cat, p, img, m, d, s, prof, old=None, tag=None, nw=False):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": s, "prof": prof, "opts": {"Вес": ["50 г", "100 г", "250 г"]}}
    if old:
        x["old"] = old
    if tag:
        x["tag"] = tag
    if nw:
        x["nw"] = 1
    x["stock"] = "Свежий урожай 2026 · отправим завтра"
    return x


# prof: [крепость 0–2, бодрость 0–2, вкус: flower/fruit/nut/smoke/herb, время: m/d/e]
PRODUCTS = [
    P("t1", "Да Хун Пао «Большой красный халат»", "oolong", 890, "dry", "Улун · Уишань, Фуцзянь",
      "Тёмный улун с нотами жареного ореха, какао и сухофруктов. Выдерживает 7–8 проливов.",
      [["Заваривание", "95 °C, 5–10 с"], ["Проливов", "7–8"], ["Урожай", "весна 2026"]], [2, 2, "nut", "d"], tag="Хит"),
    P("t2", "Те Гуань Инь «Железная богиня»", "oolong", 790, "spoons", "Улун · Аньси",
      "Светлый улун с ароматом сирени и сливочным послевкусием.", [["Заваривание", "90 °C"]], [1, 1, "flower", "d"]),
    P("t3", "Шу пуэр «Старый мастер», 2018", "puer", 1290, "jars", "Пуэр · Юньнань",
      "Глубокий, бархатистый, с нотами чернослива и мокрого дерева. Хорошо согревает.", [["Выдержка", "8 лет"]], [2, 1, "smoke", "e"], old=1490),
    P("t4", "Шэн пуэр «Горный», 2023", "puer", 1490, "pots2", "Пуэр · Банджан",
      "Бодрящий молодой пуэр с горчинкой и долгим сладким послевкусием.", [["Выдержка", "3 года"]], [2, 2, "herb", "m"], nw=True),
    P("t5", "Лун Цзин «Колодец дракона»", "green", 990, "green", "Зелёный · Ханчжоу",
      "Плоские листья, вкус каштана и свежей травы. Классика китайского зелёного.", [["Заваривание", "80 °C, 2 мин"]], [1, 2, "nut", "m"], tag="Свежий урожай"),
    P("t6", "Би Ло Чунь «Изумрудные спирали»", "green", 860, "pots", "Зелёный · Цзянсу",
      "Нежный, фруктовый, с нотой абрикоса.", [["Заваривание", "75 °C"]], [0, 1, "fruit", "d"]),
    P("t7", "Дянь Хун «Золотые почки»", "red", 750, "cups", "Красный · Юньнань",
      "Мёд, сладкий картофель и хлебная корочка. Не горчит, даже если передержать.", [["Заваривание", "90 °C, 3 мин"]], [1, 1, "fruit", "e"]),
    P("t8", "Лапсанг Сушонг", "red", 690, "mug", "Красный · копчёный",
      "Копчёный на сосне — пахнет костром и смолой. Хорош с сыром.", [["Заваривание", "95 °C"]], [2, 1, "smoke", "e"]),
    P("t9", "Сбор «Вечерний»: ромашка, мята, липа", "herbal", 490, "herbs", "Травяной · без кофеина",
      "Мягкий сбор для спокойного вечера. Можно детям.", [["Кофеин", "нет"]], [0, 0, "herb", "e"], tag="Без кофеина"),
    P("t10", "Чай с облепихой и чабрецом", "herbal", 450, "fruit", "Травяной · ягодный",
      "Кисло-сладкий, яркий, с ароматом чабреца.", [["Кофеин", "нет"]], [0, 0, "fruit", "e"]),
    P("k1", "Кофе «Эфиопия Иргачеффе», зерно", "coffee", 1190, "beans", "Обжарка под фильтр",
      "Цветы жасмина, бергамот и чай. Обжариваем по средам.", [["Обжарка", "светлая"], ["Вес", "250 г"]], [1, 2, "flower", "m"]),
    P("k2", "Кофе «Бразилия Сантос», зерно", "coffee", 990, "latte", "Обжарка под эспрессо",
      "Шоколад и орех, плотное тело — для капучино и турки.", [["Обжарка", "средняя"], ["Вес", "250 г"]], [2, 2, "nut", "m"]),
]

WIDGET_HTML = """
<div class="tq">
 <div>
  <div class="kick" style="color:#cdd8c4">Подбор чая</div>
  <h2 style="margin:14px 0 14px;color:#f6f1e7">Расскажите, что вы <em>любите</em> — нальём подходящий</h2>
  <p class="lead" style="color:rgba(246,241,231,.75)">Четыре вопроса — и три чая, с которых стоит начать. Положим пробники по 10 г, чтобы не ошибиться с пачкой.</p>
  <div class="tqq"><b>Крепость</b><div class="seg" data-k="0"><button data-v="0">Нежный</button><button data-v="1" aria-pressed="true">Средний</button><button data-v="2">Насыщенный</button></div></div>
  <div class="tqq"><b>Бодрость</b><div class="seg" data-k="1"><button data-v="0">Без кофеина</button><button data-v="1" aria-pressed="true">Немного</button><button data-v="2">Чтобы проснуться</button></div></div>
  <div class="tqq"><b>Вкус</b><div class="seg" data-k="2"><button data-v="flower">Цветочный</button><button data-v="fruit" aria-pressed="true">Фруктовый</button><button data-v="nut">Ореховый</button><button data-v="smoke">Дымный</button><button data-v="herb">Травяной</button></div></div>
  <div class="tqq"><b>Когда пьёте</b><div class="seg" data-k="3"><button data-v="m">Утром</button><button data-v="d" aria-pressed="true">Днём</button><button data-v="e">Вечером</button></div></div>
 </div>
 <div class="tres" id="tres"></div>
</div>"""

WIDGET_CSS = """
#feat .feat{--fbg:#23372a;color:#f6f1e7}
.tq{display:grid;grid-template-columns:1.1fr 1fr;gap:clamp(24px,4vw,64px)}
.tq h2 em{font-style:italic;color:#e7c98b}
.tqq{margin-top:18px}
.tqq b{display:block;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:rgba(246,241,231,.55);margin-bottom:10px;font-weight:500}
.seg{display:flex;gap:6px;flex-wrap:wrap}
.seg button{height:40px;padding:0 16px;border-radius:999px;font-size:15px;color:#f6f1e7;box-shadow:inset 0 0 0 1px rgba(246,241,231,.25)}
.seg button[aria-pressed=true]{background:#f6f1e7;color:#23372a}
.tres{background:#f6f1e7;color:#23372a;border-radius:var(--rc);padding:clamp(20px,3vw,32px);display:grid;gap:14px;align-content:start}
.tres h3{font-size:26px}
.tr{display:grid;grid-template-columns:72px 1fr auto;gap:14px;align-items:center;padding:10px 0;border-top:1px solid rgba(35,55,42,.12)}
.tr .ph{width:72px;aspect-ratio:1;border-radius:50%}
.tr b{display:block;font-family:var(--fh);font-size:18px;line-height:1.2}
.tr span{font-size:13px;color:#6c7a6e}
.tr .m{font:600 12px/1 var(--fb);color:#b28a3e;letter-spacing:.06em;text-transform:uppercase}
@media (max-width:860px){.tq{grid-template-columns:1fr}}
.cer{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,64px);align-items:center}
.cer .ph{aspect-ratio:4/5;border-radius:var(--rc)}
.cer dl{display:grid;grid-template-columns:auto 1fr;gap:16px 24px;margin:28px 0 0}
.cer dt{font-family:var(--fh);font-size:40px;line-height:1;color:var(--ac)}
.cer dd{margin:0;color:var(--soft);align-self:center}
@media (max-width:860px){.cer{grid-template-columns:1fr}}
"""

WIDGET_JS = r"""
(function(){
var S=window.SHOP,$=function(s){return document.querySelector(s)},pick=[1,1,'fruit','d'];
function score(p){var f=p.prof,s=0;s-=Math.abs(f[0]-pick[0])*1.2;s-=Math.abs(f[1]-pick[1])*1.5;if(f[2]===pick[2])s+=3;if(f[3]===pick[3])s+=1;if(pick[1]===0&&f[1]>0)s-=5;return s}
function draw(){var r=S.products.filter(function(p){return p.prof}).map(function(p){return[score(p),p]}).sort(function(a,b){return b[0]-a[0]}).slice(0,3);
 var tot=r.reduce(function(a,x){return a+x[1].p},0),box=Math.round(tot*.85/10)*10;
 $('#tres').innerHTML='<div class="kick" style="color:#6c7a6e">Ваши три чая</div><h3>Начните с этих</h3>'+r.map(function(x,i){var p=x[1],m=Math.max(62,Math.min(98,Math.round(90+x[0]*3)));return'<div class="tr" data-open="'+p.id+'" style="cursor:pointer"><div class="ph">'+S.img(p.img,'72px')+'</div><div><div class="m">совпадение '+m+'%</div><b>'+S.esc(p.n)+'</b><span>'+S.esc(p.m)+'</span></div><span>'+S.fmt(p.p)+'</span></div>'}).join('')+
 '<div style="background:#ebe3d3;border-radius:16px;padding:16px;margin-top:6px"><b style="font-family:var(--fh);font-size:20px">Коробка «Знакомство»</b><p style="font-size:14px;color:#6c7a6e;margin:4px 0 12px">Все три чая по 50 г + пробники ещё трёх. Каждый месяц новые — отменить можно в любой момент.</p><button class="btn wide" type="button" id="tBox">Коробка за '+S.fmt(box)+' <s style="opacity:.6;font-weight:400">'+S.fmt(tot)+'</s></button></div>';
 $('#tBox').onclick=function(){S.add(r[0][1].id,{'Коробка':r.map(function(x){return x[1].n.split(' «')[0].split(',')[0]}).join(' + ')},1,{price:box,name:'Коробка «Знакомство» — 3 чая'})}}
document.querySelectorAll('.tq .seg').forEach(function(g){g.querySelectorAll('button').forEach(function(b){if(!b.hasAttribute('aria-pressed'))b.setAttribute('aria-pressed','false')});
 g.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var k=+g.dataset.k;pick[k]=k<2?+b.dataset.v:b.dataset.v;g.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});draw()})});
draw();
})();
"""

CER = """
<section class="sec" id="tea" style="padding-top:0"><div class="wrap cer">
 <div class="ph reveal">%IMG%</div>
 <div class="reveal"><div class="kick">Как мы работаем</div><h2 style="margin:14px 0 18px">Чай напрямую <em style="font-style:italic;color:var(--ac)">из садов</em></h2>
 <p class="lead">Два раза в год ездим в Юньнань и Фуцзянь, пробуем десятки партий и привозим только те, что пьём сами. Каждую пачку фасуем вручную в день отправки.</p>
 <dl><dt>27</dt><dd>сортов в лавке — ни одного «для ассортимента»</dd><dt>2×</dt><dd>в год ездим к производителям за новым урожаем</dd><dt>24 ч</dt><dd>от фасовки до отправки — чай не стоит на складе</dd></dl></div>
</div></section>"""


def cfg():
    from ..common import img
    return {
        "slug": "shops/list", "images": IMG, "brand": "Лист",
        "logo": '<span style="font-style:italic;font-weight:400">Лист</span><span style="font:500 11px/1 var(--fb);letter-spacing:.16em;text-transform:uppercase;color:var(--mut);margin-left:6px">чайная лавка</span>',
        "title": "Лист — китайский чай и кофе свежей обжарки, подбор по вкусу",
        "desc": "Улуны, пуэры, зелёный и красный чай напрямую из садов Китая. Подбор по вкусу за минуту, коробка-подписка и доставка по России от 1 дня.",
        "variant": "editorial", "favLetter": "Л",
        "theme": {"bg": "#f6f1e7", "ink": "#23372a", "soft": "#4e5f52", "mut": "#8a948a", "line": "rgba(35,55,42,.12)", "line2": "rgba(35,55,42,.28)",
                  "card": "#ebe3d3", "ac": "#b2733e", "aci": "#fff", "ok": "#3d7a4f", "rc": "4px", "rb": "4px", "rs": "6px", "rh": "4px",
                  "fh": '"Literata",Georgia,serif', "fb": '"Alegreya Sans",system-ui,sans-serif', "fm": '"Alegreya Sans",system-ui,sans-serif', "fp": '"Literata",Georgia,serif',
                  "hw": "400", "ht": "-.02em", "hc": "none", "lw": "400", "lt": "0", "ar": "4/5"},
        "fonts": [("Literata", "literata", [400, 500], "normal"), ("Literata", "literata", [400], "italic"), ("Alegreya Sans", "alegreya-sans", [400, 500], "normal")],
        "strip": "Бесплатная доставка <b>от 3 000 ₽</b> · пробник в каждом заказе · свежий урожай 2026",
        "nav": [("Каталог", "catalog"), ("Подбор чая", "feat"), ("О лавке", "tea"), ("Доставка", "why")],
        "searchPh": "Пуэр, улун, Да Хун Пао…",
        "hero": {"kicker": "Чайная лавка · с 2014 года", "h1": "Чай, который <em>хочется</em> заваривать ещё", "img": "hero",
                 "lead": "Двадцать семь сортов напрямую из садов Юньнани и Фуцзяни. Не знаете, с чего начать, — ответьте на четыре вопроса, подберём три чая.",
                 "cta": "Подобрать чай", "ctaTo": "feat", "cta2": "Весь каталог", "cta2To": "catalog",
                 "stats": [("27 сортов", "в лавке"), ("от 450 ₽", "за 50 г"), ("1 день", "до отправки")],
                 "float": {"img": "dry", "t": "Да Хун Пао", "s": "890 ₽ · 7–8 проливов"}},
        "cats": [{"id": "oolong", "n": "Улуны", "img": "spoons", "s": "от нежных до тёмных"}, {"id": "puer", "n": "Пуэры", "img": "jars", "s": "шу и шэн"},
                 {"id": "green", "n": "Зелёный", "img": "green", "s": "урожай весны"}, {"id": "red", "n": "Красный", "img": "cups", "s": "медовый и копчёный"},
                 {"id": "herbal", "n": "Травяной"}, {"id": "coffee", "n": "Кофе"}],
        "catsTitle": "Что заварим сегодня",
        "products": PRODUCTS, "pageSize": 8, "showStars": False, "cardSizes": "(max-width:860px) 50vw, 25vw",
        "freeFrom": 3000, "promo": {"code": "ЧАЙ", "pct": 10, "hint": "ЧАЙ — минус 10% на первый заказ"},
        "ship": [{"id": "cour", "name": "Курьер по Москве", "eta": "завтра в удобный интервал", "price": 290, "free": 3000},
                 {"id": "pvz", "name": "Пункт выдачи по России", "eta": "2–5 дней", "price": 250, "free": 3000},
                 {"id": "post", "name": "Почта России", "eta": "5–10 дней, в любой посёлок", "price": 350}],
        "doneNote": "Соберём и упакуем вручную завтра утром, трек-номер пришлём на почту.",
        "widget": {"nav": "Подбор чая", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS},
        "sections": [CER.replace("%IMG%", img("pots", IMG, "(max-width:860px) 100vw, 48vw"))],
        "usp": [("Пробник в каждом заказе", "Кладём 10 г сорта, который вы ещё не пробовали."),
                ("Фасуем в день отправки", "Чай не лежит месяцами на складе — аромат сохраняется."),
                ("Подскажем, как заваривать", "Карточка с температурой и временем — к каждому сорту."),
                ("Не понравился — заменим", "Если чай не ваш, пришлём другой бесплатно.")],
        "uspTitle": "Маленькая лавка с большим вниманием", "uspKick": "Сервис",
        "faq": [("Как хранить чай?", "В плотно закрытой банке, подальше от света и запахов. Улуны и зелёные лучше выпить за полгода, пуэр с годами только лучше."),
                ("Что выбрать новичку?", "Начните с Дянь Хуна или Те Гуань Иня — они мягкие и прощают ошибки в заваривании. Или пройдите подбор выше."),
                ("Как работает коробка-подписка?", "Раз в месяц присылаем три чая по 50 г и пробники ещё трёх. Цена на 15% ниже, чем по отдельности, отменить можно в один клик."),
                ("Есть ли чайная, где можно попробовать?", "Да, на Покровке, 12: дегустации по выходным в 15:00, записываться не нужно.")],
        "footBig": "Заходите на чай — нальём бесплатно",
        "contacts": {"addr": "Москва, Покровка, 12", "hours": "Ежедневно 11:00–22:00"},
        "order": ["cats", "widget", "catalog", "extra", "usp", "faq"], "gridTitle": "Чай и кофе",
        "css": ".v-editorial .hero h1{font-size:clamp(46px,6.4vw,96px);line-height:.98}.card .nm{font-family:var(--fh);font-size:19px;line-height:1.25}"
               ".price{font-weight:500}.btn{letter-spacing:.04em;text-transform:uppercase;font-size:14px}",
    }
