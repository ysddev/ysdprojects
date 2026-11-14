"""«Хвост» — зоомагазин: подбор корма по питомцу (вид, возраст, вес, особенности) с суточной нормой и подпиской."""

IMG = {
    "b1": ("1591946559594-8c6d3b7391eb", 1, 1, "500,900,1300"),
    "b2": ("1541188495357-ad2dc89487f4", 1, 1, "400,800"),
    "b3": ("1568640347023-a616a30bc3bd", 1, 1, "300,600"),
    "dogbowl": ("1714068691210-073dc52c6c1d", 1, 1, "500,900"),
    "dogbowl2": ("1632236568025-1256513514b7", 1, 1, "500,900"),
    "dogfood": ("1676193866128-03a926df76ef", 1, 1, "500,900"),
    "treats": ("1568640347023-a616a30bc3bd", 1, 1, "500,900"),
    "bowl": ("1589924691995-400dc9ecc119", 1, 1, "500,900"),
    "bed1": ("1581888227599-779811939961", 1, 1, "500,900"),
    "bed2": ("1601758123927-4f7acc7da589", 1, 1, "500,900"),
    "bed3": ("1598397678815-c5dc869035b8", 1, 1, "500,900"),
    "catbed": ("1573682127988-f67136e7f12a", 1, 1, "500,900"),
    "cattoy": ("1638826595775-e2eae86cda8e", 1, 1, "500,900"),
    "cattoy2": ("1780775229486-a30ada737c76", 1, 1, "500,900"),
    "scratch": ("1545249390-6bdfa286032f", 1, 1, "500,900"),
    "cattree": ("1652113935269-cb82cbd01524", 1, 1, "500,900"),
    "leash": ("1669891286005-8e32cc879a3f", 1, 1, "500,900"),
    "puppy": ("1600369671236-e74521d4b6ad", 1, 1, "500,900"),
    "kitten": ("1516750105099-4b8a83e217ee", 1, 1, "500,900"),
}


def P(id, n, cat, p, img, m, d, s, pet="dog", old=None, tag=None, opts=None, kcal=None, nw=False):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": s, "f": {"pet": pet}, "kw": "собак" if pet == "dog" else "кош"}
    if old:
        x["old"] = old
    if tag:
        x["tag"] = tag
    if opts:
        x["opts"] = opts
    if kcal:
        x["kcal"] = kcal
    if nw:
        x["nw"] = 1
    x["stock"] = "Привезём сегодня с 19 до 23 · в наличии"
    return x


PRODUCTS = [
    P("f1", "Корм для собак средних пород, индейка", "food", 3890, "dogfood", "Беззерновой · 6 кг",
      "64% мяса, без пшеницы и кукурузы. Подходит собакам с чувствительным пищеварением.",
      [["Белок", "28%"], ["Калорийность", "370 ккал/100 г"], ["Вес", "6 кг"]], tag="Хит", opts={"Фасовка": ["6 кг", "12 кг"]}, kcal=370),
    P("f2", "Корм для щенков, ягнёнок и рис", "food", 2990, "puppy", "Для роста суставов",
      "Кальций и фосфор в правильном балансе, гранулы под молочные зубы.",
      [["Возраст", "2–12 мес."], ["Калорийность", "395 ккал/100 г"]], kcal=395),
    P("f3", "Корм для взрослых собак, лосось", "food", 4290, "dogbowl", "Для шерсти и кожи",
      "Омега-3 из лосося — шерсть блестит, кожа не шелушится.", [["Калорийность", "360 ккал/100 г"], ["Вес", "7 кг"]], old=4890, kcal=360),
    P("f4", "Корм для кошек, кролик", "food", 2490, "kitten", "Для стерилизованных",
      "Меньше жира и больше белка — помогает держать вес после стерилизации.", [["Калорийность", "355 ккал/100 г"], ["Вес", "3 кг"]], pet="cat", kcal=355, tag="Новинка", nw=True),
    P("f5", "Влажный корм для кошек, 12 паучей", "food", 1190, "bowl", "Курица в соусе",
      "Набор на две недели: 12 паучей по 85 г.", [["Состав", "курица 70%"]], pet="cat", opts={"Вкус": ["Курица", "Тунец", "Индейка"]}),
    P("t1", "Лакомство «Косточки» из говядины", "treats", 590, "treats", "Натуральные · 200 г",
      "Сушёная говядина без соли и консервантов. Для дрессировки ломается на кусочки.", [["Вес", "200 г"]]),
    P("t2", "Миска на подставке, керамика", "bowls", 1890, "dogbowl2", "Нескользящая",
      "Тяжёлая керамика не ездит по полу, можно мыть в посудомойке.", [["Объём", "1,2 л"]], opts={"Размер": ["M", "L"]}),
    P("bd1", "Лежак «Облако» с бортиком", "beds", 4590, "bed1", "Съёмный чехол",
      "Мягкий бортик поддерживает голову, чехол стирается при 40 °C.", [["Размер", "80 × 60 см"]], opts={"Размер": ["S", "M", "L"]}, tag="−15%", old=5390),
    P("bd2", "Матрас ортопедический", "beds", 6900, "bed2", "Для пожилых собак",
      "Пена с памятью формы разгружает суставы.", [["Размер", "100 × 70 см"]]),
    P("bd3", "Лежак «Овал» для крупных пород", "beds", 5900, "bed3", "Износостойкая ткань",
      "Ткань не рвётся когтями, дно не скользит.", [["Размер", "110 × 80 см"]]),
    P("c1", "Домик-лежанка для кошки", "beds", 3490, "catbed", "Плюш",
      "Мягкий плюш и высокие стенки — кошка чувствует себя в укрытии.", [["Диаметр", "50 см"]], pet="cat"),
    P("c2", "Когтеточка-столбик", "toys", 1990, "scratch", "Сизаль · 70 см",
      "Плотный сизаль и игрушка на верёвке — меньше царапин на диване.", [["Высота", "70 см"]], pet="cat"),
    P("c3", "Игровой комплекс «Башня»", "toys", 8900, "cattree", "3 уровня · домик",
      "Три яруса, домик и гамак. Устойчивое основание 50 × 50 см.", [["Высота", "140 см"]], pet="cat", nw=True),
    P("c4", "Набор игрушек «Мышиный дом»", "toys", 690, "cattoy2", "6 штук",
      "Мыши с кошачьей мятой, мячик и пёрышко.", [["В наборе", "6 игрушек"]], pet="cat"),
    P("c5", "Дразнилка-удочка", "toys", 390, "cattoy", "С перьями",
      "Перья на гибкой удочке — для игр вдвоём.", [["Длина", "60 см"]], pet="cat"),
    P("w1", "Поводок-рулетка 5 м", "walk", 1790, "leash", "До 25 кг",
      "Мягкая ручка и кнопка блокировки, лента со светоотражающей полосой.", [["Длина", "5 м"], ["Вес собаки", "до 25 кг"]]),
]

WIDGET_HTML = """
<div class="pick">
 <div class="pick-l">
  <div class="kick">Подбор корма · 1 минута</div>
  <h2 style="margin:14px 0 12px">Сколько и какого корма нужно <em id="pkName">вашему</em>?</h2>
  <p class="lead" style="font-size:17px">Посчитаем суточную норму по весу и активности, подберём корм и привезём, когда пачка будет заканчиваться.</p>
  <div class="pg"><b>Кто у вас</b><div class="seg" data-k="pet"><button data-v="dog" aria-pressed="true">🐕 Собака</button><button data-v="cat" aria-pressed="false">🐈 Кошка</button></div></div>
  <div class="pg"><b>Кличка</b><input id="pkNick" class="pin" placeholder="Например, Буся" maxlength="20"></div>
  <div class="pg"><b>Возраст</b><div class="seg" data-k="age"><button data-v="young" aria-pressed="false">До года</button><button data-v="adult" aria-pressed="true">1–7 лет</button><button data-v="old" aria-pressed="false">Старше 7</button></div></div>
  <div class="pg"><b>Вес · <span id="pkW">12 кг</span></b><input type="range" id="pkWeight" min="1" max="60" value="12"></div>
  <div class="pg"><b>Активность</b><div class="seg" data-k="act"><button data-v="0.9" aria-pressed="false">Диванный</button><button data-v="1" aria-pressed="true">Обычная</button><button data-v="1.3" aria-pressed="false">Очень активный</button></div></div>
 </div>
 <div class="pick-r">
  <div class="norm"><span>Суточная норма</span><b id="pkG">—</b><small id="pkK"></small></div>
  <div class="rec" id="pkRec"></div>
  <div class="sub2"><label><input type="checkbox" id="pkSub" checked> Привозить автоматически <span id="pkEvery"></span></label><small>Скидка 10% на каждую доставку, отменить можно в любой момент.</small></div>
  <button class="btn wide" type="button" id="pkAdd">Положить в корзину</button>
 </div>
</div>"""

WIDGET_CSS = """
#feat .feat{--fbg:#ffe9d6}
.pick{display:grid;grid-template-columns:1.2fr 1fr;gap:clamp(24px,4vw,56px);align-items:start}
.pick h2 em{font-style:normal;color:var(--ac)}
.pg{margin-top:20px}
.pg b{display:block;font-size:14px;font-weight:600;margin-bottom:10px}
.seg{display:flex;gap:8px;flex-wrap:wrap}
.seg button{height:44px;padding:0 18px;border-radius:999px;background:#fff;font-size:15px;font-weight:500;box-shadow:0 2px 0 rgba(0,0,0,.06);transition:.2s}
.seg button[aria-pressed=true]{background:var(--ink);color:#fff}
.pin{height:48px;border-radius:999px;border:0;padding:0 18px;background:#fff;width:min(320px,100%);font-size:16px}
.pick input[type=range]{width:100%;accent-color:var(--ac)}
.pick-r{background:#fff;border-radius:28px;padding:clamp(20px,3vw,32px);box-shadow:0 30px 60px -40px rgba(120,60,20,.5)}
.norm{display:grid;gap:2px;text-align:center;padding:10px 0 18px;border-bottom:2px dashed var(--line)}
.norm span{font-size:13px;color:var(--mut)}
.norm b{font-family:var(--fh);font-size:64px;line-height:1;color:var(--ac);font-weight:800}
.norm small{font-size:14px;color:var(--soft)}
.rec{display:grid;grid-template-columns:84px 1fr;gap:14px;align-items:center;padding:18px 0}
.rec .ph{width:84px;aspect-ratio:1;border-radius:20px}
.rec b{display:block;font-size:16px;line-height:1.3}
.rec span{font-size:14px;color:var(--mut)}
.sub2{background:var(--card);border-radius:18px;padding:14px 16px;margin-bottom:16px}
.sub2 label{display:flex;gap:10px;align-items:center;font-weight:600;font-size:15px;cursor:pointer}
.sub2 input{width:20px;height:20px;accent-color:var(--ac)}
.sub2 small{display:block;color:var(--mut);font-size:13px;margin:6px 0 0 30px}
@media (max-width:860px){.pick{grid-template-columns:1fr}}
"""

WIDGET_JS = r"""
(function(){
var S=window.SHOP,$=function(s){return document.querySelector(s)},st={pet:'dog',age:'adult',act:'1'};
function rec(){var id=st.pet==='cat'?'f4':st.age==='young'?'f2':(+$('#pkWeight').value>25?'f1':'f3');return S.byId[id]}
function calc(){var w=+$('#pkWeight').value,p=rec(),rer=70*Math.pow(w,.75),k=st.pet==='cat'?1.2:(st.age==='young'?2:st.age==='old'?1.4:1.6);
 var kcal=Math.round(rer*k*(+st.act)),g=Math.round(kcal/(p.kcal||370)*100),bag=p.n.indexOf('12')>=0?12000:(parseFloat((p.s.filter(function(x){return x[0]==='Вес'})[0]||['','6'])[1])||6)*1000,days=Math.max(7,Math.floor(bag/g));
 $('#pkW').textContent=w+' кг';$('#pkG').textContent=g+' г';$('#pkK').textContent=kcal+' ккал в день · '+(g>120?'2–3 кормления':'2 кормления');
 var nick=$('#pkNick').value.trim();$('#pkName').textContent=nick||(st.pet==='cat'?'вашей кошке':'вашей собаке');
 $('#pkRec').innerHTML='<div class="ph">'+S.img(p.img,'84px')+'</div><div><b>'+S.esc(p.n)+'</b><span>Хватит на '+days+' дней · '+S.fmt(p.p)+'</span></div>';
 $('#pkEvery').textContent='раз в '+days+' '+(days%10===1&&days%100!==11?'день':days%10>1&&days%10<5&&(days%100<10||days%100>20)?'дня':'дней');st.p=p;st.days=days}
document.querySelectorAll('.pick .seg').forEach(function(g){g.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;st[g.dataset.k]=b.dataset.v;g.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});
 if(g.dataset.k==='pet'){var r=$('#pkWeight');r.max=st.pet==='cat'?12:60;if(+r.value>+r.max)r.value=4}calc()})});
$('#pkWeight').addEventListener('input',calc);$('#pkNick').addEventListener('input',calc);
$('#pkAdd').onclick=function(){var sub=$('#pkSub').checked,p=st.p;S.add(p.id,sub?{'Подписка':'каждые '+st.days+' дней, −10%'}:{},1,sub?{price:Math.round(p.p*.9),name:p.n+' — подписка'}:null)};
calc();
})();
"""


def cfg():
    return {
        "slug": "shops/hvost", "images": IMG, "brand": "Хвост",
        "logo": '<b>🐾</b>хвост',
        "title": "Хвост — зоомагазин с доставкой за 2 часа и подбором корма",
        "desc": "Корма, лежаки, игрушки и всё для прогулок. Подбор корма и суточной нормы за минуту, доставка по Москве за 2 часа, подписка на корм со скидкой 10%.",
        "variant": "play", "favLetter": "Х",
        "theme": {"bg": "#fffaf4", "ink": "#2a1c14", "soft": "#5e4a3d", "mut": "#9a887a", "line": "rgba(42,28,20,.1)", "line2": "rgba(42,28,20,.25)",
                  "card": "#fff1e3", "ac": "#ff6b2c", "aci": "#fff", "ok": "#2f9e44", "rc": "26px", "rb": "999px", "rs": "40px", "hbg": "#ffe9d6",
                  "fh": '"M PLUS Rounded 1c",system-ui,sans-serif', "fb": '"Golos Text",system-ui,sans-serif', "fm": '"Golos Text",system-ui,sans-serif',
                  "hw": "800", "ht": "-.02em", "hc": "lowercase", "lw": "800", "lt": "-.02em", "ar": "1/1", "cardbg": "#fff", "cpad": "16px", "cpadb": "16px", "rl": "50%"},
        "fonts": [("M PLUS Rounded 1c", "m-plus-rounded-1c", [500, 800], "normal"), ("Golos Text", "golos-text", [400, 500, 600, 700], "normal")],
        "strip": "Доставка по Москве <b>за 2 часа</b> · бесплатно от 2 500 ₽ · ветеринар-консультант в чате",
        "nav": [("Каталог", "catalog"), ("Подбор корма", "feat"), ("Доставка", "why"), ("Вопросы", "faq")],
        "searchPh": "Корм, лежак, когтеточка…",
        "hero": {"kicker": "Зоомагазин · Москва", "h1": "всё для тех, <em>кто ждёт</em> вас дома", "bubbles": ["b1", "b2", "b3"], "img": "b1",
                 "lead": "Корм, лежаки и игрушки с доставкой за 2 часа. Посчитаем суточную норму и привезём новую пачку раньше, чем закончится старая.",
                 "cta": "Подобрать корм", "ctaTo": "feat", "cta2": "Каталог", "cta2To": "catalog",
                 "stats": [("2 часа", "доставка по Москве"), ("−10%", "по подписке"), ("24/7", "ветеринар в чате")]},
        "cats": [{"id": "food", "n": "Корм", "s": "сухой и влажный", "img": "dogfood"}, {"id": "treats", "n": "Лакомства", "img": "treats", "s": "натуральные"},
                 {"id": "beds", "n": "Лежаки и домики", "img": "bed1", "s": "для собак и кошек"}, {"id": "toys", "n": "Игрушки", "img": "cattoy", "s": "и когтеточки"},
                 {"id": "bowls", "n": "Миски"}, {"id": "walk", "n": "Прогулка"}],
        "catsTitle": "для собак и кошек",
        "products": PRODUCTS, "pageSize": 8, "showStars": True, "cardSizes": "(max-width:860px) 50vw, 25vw",
        "freeFrom": 2500, "promo": {"code": "ХВОСТ", "pct": 10, "hint": "ХВОСТ — минус 10% на первый заказ"},
        "ship": [{"id": "fast", "name": "Курьер за 2 часа", "eta": "сегодня, с 9 до 23", "price": 290, "free": 2500},
                 {"id": "slot", "name": "Курьер в удобный интервал", "eta": "завтра и позже", "price": 190, "free": 2500},
                 {"id": "pick", "name": "Самовывоз из магазина", "eta": "Тверская, 18 — через 30 минут", "price": 0}],
        "slotNote": "Тяжёлые мешки поднимем на этаж бесплатно.",
        "commentPh": "Подъезд, этаж, собака громко лает — звоните заранее 🙂",
        "doneNote": "Курьер напишет в Telegram, когда выедет.",
        "addLabel": "В корзину",
        "widget": {"nav": "Подбор корма", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS},
        "usp": [("Доставка за 2 часа", "Сами возим по Москве с 9 до 23, мешки поднимаем на этаж."),
                ("Подписка −10%", "Посчитаем, когда закончится корм, и привезём новый заранее."),
                ("Ветеринар в чате", "Спросите про питание, аллергию и прививки — ответим за 10 минут."),
                ("Возврат вскрытого корма", "Не понравился питомцу — заберём и вернём деньги в течение 14 дней.")],
        "uspTitle": "заботимся о хвостах", "uspKick": "Сервис",
        "faq": [("Как перевести питомца на новый корм?", "Постепенно, за 7–10 дней: каждый день добавляйте немного нового корма к старому. Расписание пришлём вместе с заказом."),
                ("Можно вернуть, если питомец не ест?", "Да, даже вскрытую пачку — в течение 14 дней. Заберём курьером и вернём деньги."),
                ("Как работает подписка?", "Вы выбираете корм, а мы считаем, на сколько его хватит, и привозим новую пачку за 2–3 дня до конца. Каждая доставка −10%, отменить можно в один клик."),
                ("Есть ли самовывоз?", "Да, из магазина на Тверской, 18: соберём заказ за 30 минут, пока вы гуляете с собакой.")],
        "footBig": "Пусть миска будет полной",
        "contacts": {"addr": "Москва, Тверская, 18, стр. 1", "hours": "Ежедневно 9:00–23:00"},
        "order": ["cats", "widget", "catalog", "usp", "faq"],
        "gridTitle": "популярное", "catCols": 4,
        "css": ".hero h1{font-size:clamp(44px,6.4vw,96px);line-height:.98}.v-play .hero h1 em{color:var(--ac)}.cat{border-radius:26px}.logo b{background:transparent;font-size:24px}"
               ".cats .cat:nth-child(n+5){display:none}",
    }
