"""«Грядка» — фермерские продукты: корзина на неделю под размер семьи, доставка по субботам."""

IMG = {
    "b1": ("1635341083777-5f93a755e916", 1, 1, "500,900,1300"),
    "b2": ("1559738928-5d5dc5c2458d", 1, 1, "400,800"),
    "b3": ("1767065888377-e5ffb4e39645", 1, 1, "300,600"),
    "milk": ("1635436338433-89747d0ca0ef", 1, 1, "500,900"),
    "yog": ("1581868164904-77b124b80242", 1, 1, "500,900"),
    "cheese": ("1683314573422-649a3c6ad784", 1, 1, "500,900"),
    "aged": ("1627935722051-395636b0d8a5", 1, 1, "500,900"),
    "butter": ("1603596310923-dbb12732f9c7", 1, 1, "500,900"),
    "eggs": ("1506976785307-8732e854ad03", 1, 1, "500,900"),
    "bread": ("1767065888377-e5ffb4e39645", 1, 1, "500,900"),
    "loaf": ("1771160962771-00186d83364e", 1, 1, "500,900"),
    "tom": ("1518977822534-7049a61ee0c2", 1, 1, "500,900"),
    "cherry": ("1546094096-0df4bcaaa337", 1, 1, "500,900"),
    "herbs": ("1779173932688-2bc0e3ecb95e", 1, 1, "500,900"),
    "crate": ("1635341083777-5f93a755e916", 1, 1, "500,900"),
    "apples": ("1617235178117-a1f5fecb72bd", 1, 1, "500,900"),
    "berry": ("1593895349007-8e6700308b3d", 1, 1, "500,900"),
    "honey": ("1613548058193-1cd24c1bebcf", 1, 1, "500,900"),
    "jam": ("1779120708355-7a41581b4584", 1, 1, "500,900"),
}


def P(id, n, cat, p, img, m, d, s, grp, old=None, tag=None, nw=False):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": s, "grp": grp}
    if old:
        x["old"] = old
    if tag:
        x["tag"] = tag
    if nw:
        x["nw"] = 1
    x["stock"] = "Привезём в субботу · собрано утром в день доставки"
    return x


PRODUCTS = [
    P("p1", "Молоко цельное, 1 л", "milk", 189, "milk", "Жирность 3,6–4,2%", "Утренняя дойка, пастеризация при 72 °C. Хранится 5 дней.",
      [["Объём", "1 л"], ["Ферма", "Савельевых, Тверская обл."]], "milk", tag="Хит"),
    P("p2", "Йогурт без добавок, 500 г", "milk", 240, "yog", "Только молоко и закваска", "Густой, без сахара и крахмала. Хорош с мёдом и ягодами.",
      [["Вес", "500 г"], ["Срок", "7 дней"]], "milk"),
    P("p3", "Сыр «Качотта», 300 г", "milk", 690, "cheese", "Полутвёрдый, 30 дней", "Мягкий сливочный вкус, плавится. Из молока той же фермы.",
      [["Вес", "300 г"], ["Выдержка", "30 дней"]], "milk"),
    P("p4", "Сыр выдержанный, 250 г", "milk", 890, "aged", "Твёрдый, 6 месяцев", "Плотный, с ореховым послевкусием. К вину и в пасту.",
      [["Вес", "250 г"], ["Выдержка", "6 месяцев"]], "milk", nw=True),
    P("p5", "Масло сливочное 82,5%, 200 г", "milk", 390, "butter", "Сладкосливочное", "Сбито из свежих сливок, без растительных жиров.",
      [["Вес", "200 г"]], "milk"),
    P("p6", "Яйца деревенские, 10 шт.", "bread", 220, "eggs", "Категория С0", "От кур на свободном выгуле, собраны на этой неделе.",
      [["В упаковке", "10 шт."]], "bread", tag="Хит"),
    P("p7", "Хлеб на закваске, 600 г", "bread", 320, "bread", "Пшеничный, 36 часов", "Мука, вода, соль и закваска. Печём в пятницу ночью, к субботе он ваш.",
      [["Вес", "600 г"]], "bread"),
    P("p8", "Хлеб цельнозерновой, 500 г", "bread", 290, "loaf", "С семенами льна", "Плотный мякиш, не крошится, хорош для бутербродов.",
      [["Вес", "500 г"]], "bread"),
    P("p9", "Томаты грунтовые, 1 кг", "veg", 450, "tom", "Сладкие, мясистые", "Собраны спелыми, а не дозревали в ящике.",
      [["Вес", "1 кг"]], "veg"),
    P("p10", "Черри на ветке, 500 г", "veg", 380, "cherry", "Теплица, без обработки", "Сладкие, как конфеты. Дети едят вместо сладкого.",
      [["Вес", "500 г"]], "veg", old=440),
    P("p11", "Зелень: укроп и петрушка, 150 г", "veg", 160, "herbs", "Срезана утром", "Пучок укропа и пучок петрушки в бумажном пакете.",
      [["Вес", "150 г"]], "veg"),
    P("p12", "Овощной ящик недели, 5 кг", "veg", 1490, "crate", "8–10 видов по сезону", "Картофель, морковь, свёкла, капуста, лук и то, что созрело на этой неделе.",
      [["Вес", "около 5 кг"], ["Состав", "меняется по сезону"]], "veg", tag="Выгодно"),
    P("p13", "Яблоки садовые, 2 кг", "fruit", 360, "apples", "Без воска", "Сладкие с кислинкой, хрустят. Сорт меняется по сезону.",
      [["Вес", "2 кг"]], "fruit"),
    P("p14", "Клубника, 500 г", "fruit", 590, "berry", "Собрана вчера", "Ароматная, некрупная, сладкая до самого хвостика.",
      [["Вес", "500 г"]], "fruit", nw=True),
    P("p15", "Мёд липовый, 500 г", "pantry", 650, "honey", "Сбор этого года", "Светлый, с лёгкой горчинкой. Пасека в 12 км от фермы.",
      [["Вес", "500 г"]], "pantry"),
    P("p16", "Варенье из чёрной смородины, 350 г", "pantry", 420, "jam", "Ягоды и сахар", "Варим небольшими партиями, без загустителей.",
      [["Вес", "350 г"]], "pantry"),
]

WIDGET_HTML = """
<div class="wk">
 <div>
  <div class="kick">Корзина на неделю</div>
  <h2 style="margin:12px 0 12px">Соберём продукты <em>под вашу семью</em></h2>
  <p class="lead" style="font-size:17px">Скажите, сколько вас и что вы едите. Посчитаем количество на неделю и привезём в субботу утром.</p>
  <div class="gq"><b>Сколько вас</b><div class="gtags" id="wkN"><button data-n="1" aria-pressed="false">1–2 человека</button><button data-n="2" aria-pressed="true">3–4 человека</button><button data-n="3" aria-pressed="false">5 и больше</button></div></div>
  <div class="gq"><b>Что кладём</b><div class="gtags" id="wkG"><button data-g="milk" aria-pressed="true">🥛 Молочное</button><button data-g="bread" aria-pressed="true">🥚 Яйца и хлеб</button><button data-g="veg" aria-pressed="true">🥕 Овощи и зелень</button><button data-g="fruit" aria-pressed="false">🍎 Фрукты и ягоды</button><button data-g="pantry" aria-pressed="false">🍯 Мёд и варенье</button></div></div>
  <label class="gwrap"><input type="checkbox" id="wkS" checked> Привозить каждую субботу <span>со второй корзины −10%</span></label>
 </div>
 <div class="wkbox">
  <div class="wkhead"><b>Ваша корзина</b><span id="wkC"></span></div>
  <ul id="wkL" aria-live="polite"></ul>
  <div class="wksum"><span>Итого за неделю</span><b id="wkT"></b></div>
  <button class="btn" type="button" id="wkAdd" style="width:100%">Положить всё в корзину</button>
  <p class="wknote" id="wkNote"></p>
 </div>
</div>"""

WIDGET_CSS = """
#feat .feat{--fbg:#e9f3dc}
.wk{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,56px);align-items:start}
.wk h2 em{font-style:normal;color:var(--ac)}
.gq{margin-top:22px}
.gq b{display:block;font-size:15px;font-weight:700;margin-bottom:10px}
.gtags{display:flex;gap:8px;flex-wrap:wrap}
.gtags button{height:44px;padding:0 16px;border-radius:999px;background:#fff;font-weight:600;font-size:15px;box-shadow:0 3px 0 rgba(0,0,0,.06)}
.gtags button[aria-pressed=true]{background:var(--ac);color:#fff}
.gwrap{display:flex;gap:10px;align-items:center;margin-top:22px;font-weight:600;cursor:pointer;flex-wrap:wrap}
.gwrap input{width:20px;height:20px;accent-color:var(--ac)}
.gwrap span{color:var(--ok);font-size:14px}
.wkbox{background:#fff;border-radius:28px;padding:22px;box-shadow:0 24px 50px -34px rgba(40,70,20,.45)}
.wkhead{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px}
.wkhead b{font-family:var(--fh);font-size:22px}
.wkhead span{color:var(--mut);font-size:14px}
#wkL{list-style:none;margin:0;padding:0;max-height:330px;overflow:auto}
#wkL li{display:grid;grid-template-columns:44px 1fr auto;gap:12px;align-items:center;padding:9px 0;border-bottom:1px solid var(--line)}
#wkL .ph{width:44px;height:44px;border-radius:12px;aspect-ratio:1}
#wkL b{font-size:15px;font-weight:600;line-height:1.25;display:block}
#wkL small{color:var(--mut);font-size:13px}
#wkL .pr{font-weight:700;white-space:nowrap}
#wkL .none{display:block;padding:24px 0;text-align:center;color:var(--soft)}
.wksum{display:flex;justify-content:space-between;align-items:baseline;margin:16px 0 14px}
.wksum b{font-family:var(--fh);font-size:28px}
.wknote{margin:12px 0 0;font-size:13.5px;color:var(--soft);text-align:center}
@media (max-width:860px){.wk{grid-template-columns:1fr}}
"""

WIDGET_JS = r"""
(function(){
var S=window.SHOP,$=function(s){return document.querySelector(s)},n=2,g={milk:1,bread:1,veg:1};
/* сколько берём на 1–2 человек в неделю; дальше умножаем на размер семьи */
var BASE={p1:2,p2:1,p3:1,p5:1,p6:1,p7:1,p9:1,p11:1,p12:1,p13:1,p14:1,p15:1,p16:1};
function items(){return S.products.filter(function(p){return g[p.grp]&&BASE[p.id]}).map(function(p){var q=BASE[p.id]*(p.id==='p12'||p.grp==='pantry'||p.id==='p5'?1:n);return[p,q]})}
function draw(){var it=items(),t=0;
 $('#wkL').innerHTML=it.length?it.map(function(x){var p=x[0],q=x[1];t+=p.p*q;return'<li><div class="ph">'+S.img(p.img,'44px')+'</div><div><b>'+S.esc(p.n)+'</b><small>'+q+' шт. × '+S.fmt(p.p)+'</small></div><span class="pr">'+S.fmt(p.p*q)+'</span></li>'}).join(''):'<li class="none">Выберите, что положить в корзину.</li>';
 $('#wkT').textContent=S.fmt(t);$('#wkC').textContent=it.length?it.length+' продуктов':'';
 $('#wkAdd').disabled=!it.length;
 $('#wkNote').textContent=$('#wkS').checked?'Следующие корзины привезём по субботам со скидкой 10%. Состав можно менять до четверга.':'Привезём в ближайшую субботу с 8 до 12.'}
function tog(box,key,single){box.onclick=function(e){var b=e.target.closest('button');if(!b)return;
  if(single){n=+b.dataset.n;box.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)})}
  else{var k=b.dataset.g;if(g[k])delete g[k];else g[k]=1;b.setAttribute('aria-pressed',!!g[k])}draw()}}
tog($('#wkN'),'n',true);tog($('#wkG'),'g',false);$('#wkS').addEventListener('change',draw);
$('#wkAdd').addEventListener('click',function(){var o=$('#wkS').checked?{'Доставка':'каждую субботу'}:{};items().forEach(function(x){S.add(x[0].id,o,x[1])})});
draw();
})();
"""


def cfg():
    return {
        "slug": "shops/gryadka", "images": IMG, "brand": "Грядка",
        "logo": '<b style="background:#2f8a45;color:#fff">🥕</b>грядка',
        "title": "Грядка — фермерские продукты с доставкой по субботам",
        "desc": "Молоко, сыр, яйца, хлеб на закваске, овощи и ягоды от небольших ферм. Корзина на неделю под размер семьи, доставка в субботу утром.",
        "variant": "play", "favLetter": "Г",
        "theme": {"bg": "#fbf8ef", "ink": "#22301b", "soft": "#4c5a44", "mut": "#8b9682", "line": "rgba(34,48,27,.1)", "line2": "rgba(34,48,27,.25)",
                  "card": "#f1ecdd", "ac": "#2f8a45", "aci": "#fff", "ac2": "#f6c443", "ok": "#2f8a45", "rc": "24px", "rb": "999px", "rs": "40px", "hbg": "#e4efd0",
                  "fh": '"Bitter",Georgia,serif', "fb": '"Golos Text",system-ui,sans-serif', "fm": '"Golos Text",system-ui,sans-serif',
                  "hw": "800", "ht": "-.02em", "hc": "none", "lw": "800", "lt": "-.01em", "ar": "1/1", "cardbg": "#fff", "cpad": "14px", "cpadb": "14px", "rl": "50%"},
        "fonts": [("Bitter", "bitter", [700, 800], "normal"), ("Golos Text", "golos-text", [400, 500, 600, 700], "normal")],
        "strip": "Доставка <b>в субботу с 8 до 12</b> · собираем утром в день доставки · бесплатно от 3 000 ₽",
        "nav": [("Каталог", "catalog"), ("Корзина на неделю", "feat"), ("Доставка", "why"), ("Вопросы", "faq")],
        "searchPh": "Молоко, яйца, томаты…",
        "hero": {"kicker": "Фермерские продукты · Москва и область", "h1": "С грядки на стол <em>за одно утро</em>", "bubbles": ["b1", "b2", "b3"], "img": "b1",
                 "lead": "Молоко вчерашней дойки, хлеб, который пекли ночью, и овощи, собранные спелыми. Привозим раз в неделю, в субботу утром.",
                 "cta": "Собрать корзину на неделю", "ctaTo": "feat", "cta2": "Каталог", "cta2To": "catalog",
                 "stats": [("7 ферм", "знаем каждую лично"), ("суббота", "день доставки"), ("до четверга", "можно менять заказ")]},
        "cats": [{"id": "milk", "n": "Молочное", "s": "молоко, сыр, масло", "img": "milk"}, {"id": "bread", "n": "Яйца и хлеб", "s": "на закваске", "img": "eggs"},
                 {"id": "veg", "n": "Овощи и зелень", "img": "tom", "s": "по сезону"}, {"id": "fruit", "n": "Фрукты и ягоды", "img": "berry", "s": "собраны спелыми"},
                 {"id": "pantry", "n": "Мёд и варенье"}],
        "catsTitle": "Что привезём в субботу",
        "products": PRODUCTS, "pageSize": 8, "showStars": False, "cardSizes": "(max-width:860px) 50vw, 25vw",
        "freeFrom": 3000, "promo": {"code": "ГРЯДКА", "pct": 10, "hint": "ГРЯДКА — минус 10% на первую корзину"},
        "ship": [{"id": "sat", "name": "Курьер в субботу", "eta": "с 8 до 12, в термосумке", "price": 290, "free": 3000},
                 {"id": "eve", "name": "Курьер в субботу вечером", "eta": "с 17 до 21", "price": 390, "free": 5000},
                 {"id": "pick", "name": "Самовывоз с рынка", "eta": "суббота, Даниловский рынок, с 9 до 15", "price": 0}],
        "commentPh": "Код домофона, куда поставить, если вас не будет",
        "doneNote": "В пятницу вечером пришлём состав корзины и время приезда курьера.",
        "widget": {"nav": "Корзина на неделю", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS},
        "usp": [("Знаем, откуда продукт", "На карточке каждого продукта указана ферма. Раз в сезон ездим к каждой сами."),
                ("Собрано в день доставки", "Молоко вчерашней дойки, хлеб из ночной выпечки, зелень срезана утром."),
                ("Довезём холодным", "Молочное и ягоды едут в термосумках с хладоэлементами."),
                ("Не понравилось, вернём деньги", "Пришлите фото в день доставки: вернём деньги или привезём замену.")],
        "uspTitle": "Еда, про которую всё понятно", "uspKick": "Почему мы",
        "faq": [("Почему доставка только по субботам?", "Фермы отгружают продукты в пятницу вечером и в субботу утром. Так всё приезжает свежим, а не лежит на складе."),
                ("Можно изменить заказ?", "Да, до четверга 20:00: добавить, убрать или пропустить неделю. Напишите нам или поменяйте корзину на сайте."),
                ("Как работает подписка?", "Раз в неделю привозим вашу корзину, со второй доставки скидка 10%. Пропустить неделю или отменить можно в любой момент."),
                ("Что если чего-то не окажется?", "Позвоним в пятницу и предложим замену. Не подойдёт — вернём деньги за эту позицию.")],
        "footBig": "Вкусно, когда знаешь, откуда",
        "contacts": {"addr": "Москва, Даниловский рынок, место 114", "hours": "Заказы принимаем до четверга 20:00"},
        "order": ["cats", "widget", "catalog", "usp", "faq"], "gridTitle": "На этой неделе", "catCols": 4,
        "css": ".hero h1{font-size:clamp(44px,6.6vw,98px);line-height:.96}.v-play .hero h1 em{color:var(--ac)}.cats .cat:nth-child(n+5){display:none}"
               ".add{background:var(--ac);color:#fff}.logo b{font-size:20px}",
    }
