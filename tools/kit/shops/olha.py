"""«Ольха» — мебельная мастерская: каталог, конфигуратор дивана (размер, ткань, цвет, ножки) с живой ценой и сроком."""

IMG = {
    "hero": ("1590251024078-8a6d9f90b02d", 4, 5, "700,1100,1500"),
    "sofa1": ("1759722665629-29df6ee4f9a5", 4, 5, "500,900"),
    "sofa2": ("1659976733536-dfa71f6015d7", 4, 5, "500,900"),
    "sofa3": ("1704428382813-b6c72be3f6c3", 4, 5, "500,900"),
    "sofa4": ("1611967164521-abae8fba4668", 4, 5, "500,900"),
    "room1": ("1550581190-9c1c48d21d6c", 4, 5, "500,900,1400"),
    "room2": ("1653340513561-3ef95d9e4d94", 4, 5, "500,900,1400"),
    "room3": ("1665522557933-03af6066fb7d", 4, 5, "500,900"),
    "chair1": ("1580480055273-228ff5388ef8", 4, 5, "500,900"),
    "chair2": ("1586023492125-27b2c045efd7", 4, 5, "500,900"),
    "chair3": ("1759722667456-71e7bfd118b2", 4, 5, "500,900"),
    "chair4": ("1567538096630-e0c55bd6374c", 4, 5, "500,900"),
    "chair5": ("1605702098590-d552a98dc93d", 4, 5, "500,900"),
    "chair6": ("1586158291800-2665f07bba79", 4, 5, "500,900"),
    "chair7": ("1617364852223-75f57e78dc96", 4, 5, "500,900"),
    "chair8": ("1623353283172-2518d7e6f5ab", 4, 5, "500,900"),
    "blue": ("1650300636679-b3310a41638d", 4, 5, "500,900"),
    "blanket": ("1757969704802-4d0050f038d7", 4, 5, "500,900"),
}

SW = [{"v": "Овсяный", "c": "#d9cbb3"}, {"v": "Графит", "c": "#4a4b4d"}, {"v": "Шалфей", "c": "#93a08a"}, {"v": "Терракота", "c": "#b4664a"}]


def P(id, n, cat, p, img, m, d, s, old=None, tag=None, opts=None, nw=False, stock=None):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": s}
    if old:
        x["old"] = old
    if tag:
        x["tag"] = tag
    if opts:
        x["opts"] = opts
    if nw:
        x["nw"] = 1
    x["stock"] = stock or "Изготовим за 14 дней · доставка и сборка бесплатно"
    return x


PRODUCTS = [
    P("s1", "Диван «Ольха» 3-местный", "sofas", 89900, "sofa1", "Каркас — массив берёзы",
      "Глубокая посадка 62 см, съёмные чехлы и пружинный блок «змейка» с ППУ высокой плотности. Наш самый продаваемый диван.",
      [["Размер", "240 × 98 × 82 см"], ["Спальное место", "нет"], ["Гарантия", "10 лет на каркас"]], tag="Бестселлер", opts={"Цвет": SW, "Ножки": ["Дуб", "Чёрный металл"]}),
    P("s2", "Диван «Река» угловой", "sofas", 132000, "sofa2", "Угол слева или справа",
      "Модульный угловой диван: угол можно перекинуть на другую сторону после переезда.",
      [["Размер", "290 × 180 × 80 см"], ["Модулей", "3"]], opts={"Угол": ["Левый", "Правый"], "Цвет": SW}),
    P("s3", "Диван-кровать «Сосна»", "sofas", 74500, "sofa3", "Механизм «еврокнижка»",
      "Раскладывается одним движением, спальное место 160 × 200 с ортопедическим основанием.",
      [["Размер", "220 × 100 × 86 см"], ["Спальное", "160 × 200 см"]], old=82000, opts={"Цвет": SW}),
    P("s4", "Диван «Лён» 2-местный", "sofas", 64900, "sofa4", "Компактный · для студий",
      "Ширина 180 см — встаёт в нишу и на небольшую кухню-гостиную.",
      [["Размер", "180 × 92 × 80 см"]], opts={"Цвет": SW}, nw=True, tag="Новинка"),
    P("a1", "Кресло «Берёза»", "chairs", 34900, "chair1", "Массив берёзы, рогожка",
      "Каркас из массива с открытыми подлокотниками. Сиденье на ремнях — мягко, но не проваливаешься.",
      [["Размер", "72 × 80 × 78 см"]], opts={"Цвет": SW}),
    P("a2", "Кресло «Солнце»", "chairs", 29900, "chair2", "Букле · горчичный",
      "Яркий акцент для гостиной: тёплый горчичный букле и деревянная рама.",
      [["Размер", "70 × 76 × 80 см"]]),
    P("a3", "Кресло-мешок «Облако»", "chairs", 18900, "chair3", "Велюр · съёмный чехол",
      "Круглое кресло с подушками — читать, сидеть с ногами, засыпать.",
      [["Диаметр", "96 см"]], tag="Хит", opts={"Цвет": SW}),
    P("a4", "Кресло «Честер»", "chairs", 47500, "chair4", "Экокожа · каретная стяжка",
      "Классика с каретной стяжкой для кабинета и библиотеки.",
      [["Размер", "84 × 82 × 78 см"]], old=52000),
    P("a5", "Кресло «Дуб»", "chairs", 38500, "chair5", "Массив дуба",
      "Лаконичный каркас из дуба под маслом, подушки на молнии.",
      [["Размер", "68 × 74 × 76 см"]]),
    P("a6", "Кресло «Север»", "chairs", 31900, "chair6", "Чёрная рама · белый лён",
      "Скандинавский контраст: чёрная тонированная рама и молочный лён.",
      [["Размер", "66 × 72 × 74 см"]], nw=True),
    P("a7", "Кресло «Лофт»", "chairs", 35900, "chair7", "Орех · кожа",
      "Кожаные подушки, которые с годами становятся только красивее.",
      [["Размер", "70 × 78 × 76 см"]]),
    P("a8", "Кресло «Туман»", "chairs", 27500, "chair8", "Рогожка · серый",
      "Мягкое кресло без острых углов — подходит к любому дивану из коллекции.",
      [["Размер", "74 × 82 × 80 см"]], opts={"Цвет": SW}),
    P("t1", "Плед из шерсти мериноса", "decor", 7900, "blanket", "130 × 180 см",
      "Мягкий, не колется. Стирка на деликатном режиме.", [["Состав", "100% меринос"]]),
    P("t2", "Комплект подушек «Шалфей», 2 шт.", "decor", 4900, "blue", "45 × 45 см · лён",
      "Льняные чехлы на скрытой молнии, наполнитель — холлофайбер.", [["Размер", "45 × 45 см"]]),
]

WIDGET_HTML = """
<div class="cfg">
 <div class="cfg-view">
  <div class="cfg-stage" id="cfgStage" aria-hidden="true">
   <svg viewBox="0 0 640 360" class="sofa"><defs><linearGradient id="sh" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".18"/></linearGradient></defs>
    <ellipse cx="320" cy="318" rx="270" ry="16" fill="#000" opacity=".08"/>
    <g id="sofaG"><rect id="sBack" x="70" y="96" width="500" height="120" rx="34"/><rect id="sSeat" x="60" y="190" width="520" height="80" rx="26"/>
    <rect id="sArmL" x="40" y="150" width="70" height="140" rx="30"/><rect id="sArmR" x="530" y="150" width="70" height="140" rx="30"/>
    <rect x="60" y="190" width="520" height="80" rx="26" fill="url(#sh)"/>
    <g id="sCush"><rect x="122" y="168" width="190" height="44" rx="18" opacity=".55" fill="#fff"/><rect x="328" y="168" width="190" height="44" rx="18" opacity=".55" fill="#fff"/></g>
    <g id="sLegs"><rect x="92" y="286" width="12" height="26" rx="3"/><rect x="536" y="286" width="12" height="26" rx="3"/><rect x="200" y="286" width="10" height="22" rx="3"/><rect x="430" y="286" width="10" height="22" rx="3"/></g></g>
   </svg>
   <div class="cfg-dim" id="cfgDim">240 см</div>
  </div>
  <p class="cfg-note">Фото ткани пришлём в мессенджер, образцы привезём домой бесплатно.</p>
 </div>
 <div class="cfg-form">
  <div class="kick">Конфигуратор</div>
  <h2 style="margin:12px 0 10px">Соберите свой <em>диван</em></h2>
  <p class="lead" style="font-size:17px">Размер, ткань и ножки — под вашу комнату. Цена и срок пересчитываются сразу.</p>
  <div class="cfg-g"><b>Длина</b><div class="seg" data-k="len"><button data-v="200" aria-pressed="false">200 см</button><button data-v="240" aria-pressed="true">240 см</button><button data-v="280" aria-pressed="false">280 см</button></div></div>
  <div class="cfg-g"><b>Ткань</b><div class="seg" data-k="fab"><button data-v="rog" aria-pressed="true">Рогожка</button><button data-v="vel" aria-pressed="false">Велюр</button><button data-v="buk" aria-pressed="false">Букле</button></div><small id="fabNote">Плотная, не боится когтей и пятен</small></div>
  <div class="cfg-g"><b>Цвет · <span id="colName">Овсяный</span></b><div class="sws" id="sws"></div></div>
  <div class="cfg-g"><b>Ножки</b><div class="seg" data-k="leg"><button data-v="oak" aria-pressed="true">Дуб</button><button data-v="black" aria-pressed="false">Чёрный металл</button><button data-v="brass" aria-pressed="false">Латунь</button></div></div>
  <label class="cfg-chk"><input type="checkbox" id="cfgBed"> Спальное место 160 × 200 <span>+ 18 000 ₽</span></label>
  <div class="cfg-sum"><div><div class="muted" style="font-size:13px">Ваш диван · готов <span id="cfgDays"></span></div><div class="price" id="cfgPrice" style="font-size:32px"></div></div><button class="btn" type="button" id="cfgAdd">В корзину</button></div>
 </div>
</div>"""

WIDGET_CSS = """
#feat .feat{--fbg:#ebe4d8}
.cfg{display:grid;grid-template-columns:1.15fr 1fr;gap:clamp(24px,4vw,64px);align-items:center}
.cfg-stage{position:relative;border-radius:22px;background:radial-gradient(90% 80% at 50% 30%,#fbf8f2,#e6dccb);aspect-ratio:16/10;display:grid;place-items:center;overflow:hidden}
.sofa{width:92%;transition:transform .5s cubic-bezier(.2,.7,.2,1)}
#sofaG rect{transition:fill .45s,width .45s,x .45s}
.cfg-dim{position:absolute;left:50%;bottom:16px;transform:translateX(-50%);font:500 13px/1 var(--fm);letter-spacing:.1em;color:var(--soft);background:rgba(255,255,255,.7);padding:8px 12px;border-radius:999px}
.cfg-note{font-size:13px;color:var(--mut);margin-top:12px}
.cfg-form h2 em{font-style:italic;color:var(--ac)}
.cfg-g{margin-top:22px}
.cfg-g b{display:block;font-size:14px;font-weight:500;margin-bottom:10px}
.cfg-g small{display:block;font-size:13px;color:var(--mut);margin-top:8px}
.seg{display:flex;gap:6px;flex-wrap:wrap}
.seg button{height:42px;padding:0 16px;border-radius:999px;box-shadow:inset 0 0 0 1px var(--line2);font-size:14px;transition:.2s}
.seg button[aria-pressed=true]{background:var(--ink);color:var(--bg);box-shadow:none}
.sws{display:flex;gap:10px}
.sws button{width:40px;height:40px;border-radius:50%;box-shadow:inset 0 0 0 3px #ebe4d8,0 0 0 1px var(--line2);transition:transform .2s}
.sws button[aria-pressed=true]{box-shadow:inset 0 0 0 3px #ebe4d8,0 0 0 2px var(--ink);transform:scale(1.06)}
.cfg-chk{display:flex;align-items:center;gap:10px;margin-top:20px;font-size:15px;cursor:pointer}
.cfg-chk input{width:18px;height:18px;accent-color:var(--ac)}
.cfg-chk span{margin-left:auto;color:var(--mut);font-size:14px}
.cfg-sum{display:flex;justify-content:space-between;align-items:end;gap:16px;margin-top:26px;padding-top:22px;border-top:1px solid var(--line2);flex-wrap:wrap}
@media (max-width:860px){.cfg{grid-template-columns:1fr}}
.story{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,64px);align-items:center}
.story .ph{aspect-ratio:4/5;border-radius:var(--rc)}
.story .duo{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.story .duo .ph:last-child{margin-top:60px}
.story ol{list-style:none;margin:28px 0 0;padding:0;display:grid;gap:18px;counter-reset:s}
.story li{display:grid;grid-template-columns:44px 1fr;gap:14px;counter-increment:s}
.story li::before{content:"0" counter(s);font:500 13px/44px var(--fm);color:var(--ac);border:1px solid var(--line2);border-radius:50%;width:44px;height:44px;text-align:center}
.story li b{display:block;font-family:var(--fh);font-size:22px;font-weight:500}
.story li p{color:var(--soft);font-size:15px}
@media (max-width:860px){.story{grid-template-columns:1fr}}
"""

WIDGET_JS = r"""
(function(){
var S=window.SHOP,$=function(s){return document.querySelector(s)};
var COL=[["Овсяный","#d9cbb3"],["Графит","#4a4b4d"],["Шалфей","#93a08a"],["Терракота","#b4664a"],["Пыльная роза","#c9a29a"],["Индиго","#3d4b6b"]];
var st={len:'240',fab:'rog',leg:'oak',col:0,bed:false};
var FAB={rog:[0,'Плотная, не боится когтей и пятен'],vel:[6000,'Бархатистая, глубокий цвет, приятная на ощупь'],buk:[11000,'Фактурная «барашковая» ткань — самая модная']};
var LEN={'200':[-14000,.84],'240':[0,1],'280':[16000,1.16]},LEG={oak:['#b98a5e',0],black:['#222',2500],brass:['#c9a45c',4500]};
$('#sws').innerHTML=COL.map(function(c,i){return'<button type="button" aria-pressed="'+(i===0)+'" aria-label="'+c[0]+'" data-c="'+i+'" style="background:'+c[1]+'"></button>'}).join('');
function shade(hex,k){var n=parseInt(hex.slice(1),16),r=n>>16,g=n>>8&255,b=n&255;return'rgb('+[r,g,b].map(function(v){return Math.round(Math.min(255,v*k))}).join(',')+')'}
function price(){return 89900+LEN[st.len][0]+FAB[st.fab][0]+LEG[st.leg][1]+(st.bed?18000:0)}
function draw(){var c=COL[st.col][1],sc=LEN[st.len][1];
 $('#sBack').setAttribute('fill',shade(c,.92));$('#sSeat').setAttribute('fill',c);$('#sArmL').setAttribute('fill',shade(c,.86));$('#sArmR').setAttribute('fill',shade(c,.86));
 document.querySelectorAll('#sLegs rect').forEach(function(r){r.setAttribute('fill',LEG[st.leg][0])});
 $('.sofa').style.transform='scaleX('+sc+')';$('#cfgDim').textContent=st.len+' см'+(st.bed?' · раскладной':'');
 $('#colName').textContent=COL[st.col][0];$('#fabNote').textContent=FAB[st.fab][1];
 $('#cfgPrice').textContent=S.fmt(price());var d=new Date(Date.now()+(st.fab==='buk'?21:14)*864e5);$('#cfgDays').textContent=d.toLocaleDateString('ru-RU',{day:'numeric',month:'long'})}
document.querySelectorAll('.seg').forEach(function(g){g.addEventListener('click',function(ev){var b=ev.target.closest('button');if(!b)return;st[g.dataset.k]=b.dataset.v;g.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});draw()})});
$('#sws').addEventListener('click',function(ev){var b=ev.target.closest('button');if(!b)return;st.col=+b.dataset.c;this.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});draw()});
$('#cfgBed').onchange=function(){st.bed=this.checked;draw()};
$('#cfgAdd').onclick=function(){var fab={rog:'рогожка',vel:'велюр',buk:'букле'}[st.fab],leg={oak:'ножки дуб',black:'чёрные ножки',brass:'латунные ножки'}[st.leg];
 S.add('s1',{'Конфигурация':st.len+' см, '+fab+', '+COL[st.col][0].toLowerCase()+', '+leg+(st.bed?', спальное место':'')},1,{price:price(),name:'Диван «Ольха» по вашей конфигурации'})};
draw();
})();
"""

STORY = """
<section class="sec" id="made" style="padding-top:0"><div class="wrap story">
 <div class="duo reveal"><div class="ph">%IMG1%</div><div class="ph">%IMG2%</div></div>
 <div class="reveal"><div class="kick">Мастерская в Коломне</div><h2 style="margin:14px 0 18px">Делаем руками, <em style="font-style:italic;color:var(--ac)">под вас</em></h2>
 <p class="lead">Каждый диван собирают двое мастеров — от каркаса до последнего стежка. Поэтому можно поменять размер на 10 см или выбрать ткань не из каталога.</p>
 <ol><li><div><b>Каркас из массива</b><p>Берёза и дуб камерной сушки, на шипах и клею — без скоб и ДСП.</p></div></li>
 <li><div><b>Наполнение в три слоя</b><p>Пружинный блок, ППУ высокой плотности и синтепух — форма держится годами.</p></div></li>
 <li><div><b>Привезём и соберём</b><p>Доставка по Москве и области бесплатно, заберём упаковку с собой.</p></div></li></ol></div>
</div></section>"""


def cfg():
    from ..common import img
    return {
        "slug": "shops/olha", "images": IMG, "brand": "Ольха",
        "logo": '<span style="font-style:italic">Ольха</span><small style="font:500 11px/1 var(--fm);letter-spacing:.14em;text-transform:uppercase;color:var(--mut);margin-left:4px">мастерская мебели</small>',
        "title": "Ольха — мягкая мебель из массива на заказ",
        "desc": "Диваны и кресла из массива берёзы и дуба: конфигуратор размера, ткани и цвета, изготовление за 14 дней, доставка и сборка по Москве бесплатно.",
        "variant": "editorial", "favLetter": "О",
        "theme": {"bg": "#f6f2ec", "ink": "#2b2620", "soft": "#5a5249", "mut": "#8c8378", "line": "rgba(43,38,32,.12)", "line2": "rgba(43,38,32,.28)",
                  "card": "#ece6dc", "ac": "#8a5a3b", "aci": "#fff", "ok": "#4f7a4a", "rc": "6px", "rb": "999px", "rs": "8px", "rh": "200px 200px 6px 6px",
                  "fh": '"Cormorant Infant",Georgia,serif', "fb": '"Jost",system-ui,sans-serif', "fm": '"Jost",system-ui,sans-serif', "fp": '"Jost",system-ui,sans-serif',
                  "hw": "500", "ht": "-.01em", "hc": "none", "lw": "500", "lt": "0"},
        "fonts": [("Cormorant Infant", "cormorant-infant", [400, 500], "normal"), ("Jost", "jost", [300, 400, 500], "normal")],
        "strip": "Бесплатные образцы тканей на дом · изготовление <b>от 14 дней</b> · рассрочка 0% на 6 месяцев",
        "nav": [("Каталог", "catalog"), ("Конфигуратор", "feat"), ("Мастерская", "made"), ("Доставка", "why")],
        "searchPh": "Диван, кресло, плед…",
        "hero": {"kicker": "Мебель из массива · сделано в Коломне", "h1": "Диван, на котором <em>хочется</em> жить",
                 "lead": "Собираем вручную из берёзы и дуба: выберите размер, ткань и цвет — привезём через две недели и соберём бесплатно.",
                 "img": "hero", "cta": "Собрать свой диван", "ctaTo": "feat", "cta2": "Смотреть каталог", "cta2To": "catalog",
                 "stats": [("10 лет", "гарантия на каркас"), ("14 дней", "изготовление"), ("2 мастера", "на каждый диван")],
                 "float": {"img": "chair3", "t": "Кресло «Облако»", "s": "18 900 ₽ · хит недели"}},
        "cats": [{"id": "sofas", "n": "Диваны", "s": "4 модели", "img": "room1"}, {"id": "chairs", "n": "Кресла", "s": "8 моделей", "img": "chair2"},
                 {"id": "decor", "n": "Текстиль", "s": "пледы и подушки", "img": "blanket"}],
        "catCols": 3, "catsTitle": "Для гостиной и спальни",
        "products": PRODUCTS, "pageSize": 8, "showStars": False, "cardSizes": "(max-width:860px) 50vw, 25vw",
        "freeFrom": 0, "promo": {"code": "ОЛЬХА", "pct": 5, "hint": "ОЛЬХА — минус 5% на первый заказ"},
        "ship": [{"id": "msk", "name": "Доставка и сборка по Москве и области", "eta": "в выбранный день, 2-часовой интервал", "price": 0},
                 {"id": "rus", "name": "Транспортная компания по России", "eta": "5–12 дней, в жёсткой обрешётке", "price": 4900}],
        "slotNote": "За день до доставки менеджер позвонит и уточнит подъём и проход.",
        "commentPh": "Этаж, есть ли лифт, ширина проёмов",
        "doneNote": "Менеджер позвонит в течение часа и пришлёт фото тканей в мессенджер.",
        "emptyCart": "Начните с конфигуратора — соберём диван под вашу комнату.",
        "widget": {"nav": "Конфигуратор", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS},
        "sections": [STORY.replace("%IMG1%", img("room2", IMG, "(max-width:860px) 50vw, 24vw")).replace("%IMG2%", img("chair5", IMG, "(max-width:860px) 50vw, 24vw"))],
        "usp": [("Образцы тканей домой", "Привезём 20 образцов бесплатно — выберите при своём свете."),
                ("Рассрочка 0%", "До 6 месяцев без переплаты, одобрение за 2 минуты."),
                ("Сборка и вывоз упаковки", "Соберём за час и заберём коробки с собой."),
                ("10 лет на каркас", "Массив и честная столярка — диван переживёт два переезда.")],
        "uspTitle": "Спокойная покупка", "uspKick": "Сервис",
        "faq": [("Можно изменить размер?", "Да, длину и глубину меняем с шагом 10 см без доплаты в пределах ±20 см. Больше — посчитаем отдельно."),
                ("Как ухаживать за тканью?", "Чехлы съёмные: рогожку и велюр можно стирать при 30 °C. Букле — только химчистка, зато она почти не пачкается."),
                ("Что если диван не пройдёт в дверь?", "Перед заказом пришлём замерщика или попросим фото проёмов. Большие модели собираем из модулей прямо в квартире."),
                ("Есть ли шоурум?", "Да, в Москве на Большой Пироговской, 27 — там все ткани и шесть моделей вживую. Приезжайте в любой день с 11 до 21.")],
        "footBig": "Приезжайте посидеть на всех диванах",
        "contacts": {"addr": "Москва, Б. Пироговская, 27, стр. 2", "hours": "Шоурум ежедневно 11:00–21:00"},
        "order": ["cats", "catalog", "widget", "extra", "usp", "faq"],
        "gridTitle": "Коллекция",
        "css": ".v-editorial .hero h1{font-size:clamp(48px,7vw,104px);line-height:.92}.card .nm{font-family:var(--fh);font-size:21px;font-weight:500}.price{font-weight:500}",
    }
