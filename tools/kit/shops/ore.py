"""«Орэ» — ювелирные украшения: определитель размера кольца и примерка гравировки."""

IMG = {
    "hero": ("1626122780071-c09d403b8e32", 4, 5, "700,1100,1600"),
    "r1": ("1543294001-f7cd5d7fb516", 4, 5, "500,900"),
    "r2": ("1611955167811-4711904bb9f8", 4, 5, "500,900"),
    "r3": ("1589207212797-cfd546dea0fe", 4, 5, "500,900"),
    "r4": ("1561812350-932aed735105", 4, 5, "500,900"),
    "r5": ("1701777696655-17fb18395ccc", 4, 5, "500,900"),
    "r6": ("1615655114865-4cc1bda5901e", 4, 5, "500,900"),
    "e1": ("1701777892740-88419a701472", 4, 5, "500,900"),
    "e2": ("1653227907864-560dce4c252d", 4, 5, "500,900"),
    "e3": ("1535632787350-4e68ef0ac584", 4, 5, "500,900"),
    "e4": ("1693212793204-bcea856c75fe", 4, 5, "500,900"),
    "n1": ("1783541507490-edb026e2a961", 4, 5, "500,900"),
    "n2": ("1773929345739-94db8a4ccd0c", 4, 5, "500,900"),
    "n3": ("1786052337650-9e1c0dd01f5e", 4, 5, "500,900"),
    "n4": ("1611107683227-e9060eccd846", 4, 5, "500,900"),
    "b1": ("1602173574767-37ac01994b2a", 4, 5, "500,900"),
    "b2": ("1777999802051-f6f0296e76af", 4, 5, "500,900"),
    "b3": ("1778000000743-87e855360c51", 4, 5, "500,900"),
}

SIZES = ["15,5", "16", "16,5", "17", "17,5", "18", "18,5", "19"]


def P(id, n, cat, p, img, m, d, s, old=None, tag=None, nw=False, eng=False):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": s}
    if cat == "rings":
        x["opts"] = {"Размер": SIZES}
    if cat == "necklaces":
        x["opts"] = {"Длина": ["40 см", "45 см", "50 см"]}
    if old:
        x["old"] = old
    if tag:
        x["tag"] = tag
    if nw:
        x["nw"] = 1
    if eng:
        x["eng"] = 1
    x["stock"] = "В наличии · отправим в день заказа в фирменном футляре"
    return x


PRODUCTS = [
    P("r1", "Кольца «Трио» с дорожкой камней", "rings", 34900, "r1", "Золото 585 · фианиты", "Три тонких кольца, которые носят вместе или по одному.",
      [["Металл", "жёлтое золото 585"], ["Вставка", "фианиты"]], tag="Хит"),
    P("r2", "Кольцо с бриллиантом 0,3 карата", "rings", 89000, "r2", "Золото 585 · бриллиант", "Классическая оправа на шести крапанах: камень открыт свету со всех сторон.",
      [["Металл", "жёлтое золото 585"], ["Вставка", "бриллиант 0,3 ct"], ["Чистота", "VS1"]], eng=True),
    P("r3", "Кольцо гладкое «Линия»", "rings", 21500, "r3", "Золото 585 · 3 мм", "Гладкое кольцо комфортной посадки. Подходит для гравировки внутри.",
      [["Металл", "жёлтое золото 585"], ["Ширина", "3 мм"]], eng=True),
    P("r4", "Кольцо с сапфиром", "rings", 64000, "r4", "Золото 585 · сапфир", "Синий сапфир огранки «овал» в лаконичной оправе.",
      [["Металл", "жёлтое золото 585"], ["Вставка", "сапфир 0,8 ct"]], nw=True),
    P("r5", "Кольцо «Три ряда» с бриллиантами", "rings", 118000, "r5", "Белое золото · бриллианты", "Три дорожки мелких бриллиантов: блестит при любом свете.",
      [["Металл", "белое золото 585"], ["Вставка", "бриллианты 0,6 ct"]]),
    P("r6", "Обручальные кольца, пара", "rings", 48000, "r6", "Белое и жёлтое золото", "Два кольца одного профиля в разных оттенках золота. Гравировка внутри бесплатно.",
      [["Металл", "золото 585"], ["Ширина", "4 мм"]], eng=True, tag="Гравировка в подарок"),
    P("e1", "Серьги-подвески «Капля»", "earrings", 27900, "e1", "Золото 585", "Лёгкие подвески, которые двигаются вместе с вами.",
      [["Металл", "жёлтое золото 585"], ["Замок", "английский"]]),
    P("e2", "Серьги с гранатом", "earrings", 31500, "e2", "Золото 585 · гранат", "Тёплый красный камень в золотой оправе.",
      [["Металл", "жёлтое золото 585"], ["Вставка", "гранат"]], old=35000),
    P("e3", "Серьги-кольца из серебра", "earrings", 9800, "e3", "Серебро 925", "Гладкие кольца на каждый день, не темнеют благодаря родиевому покрытию.",
      [["Металл", "серебро 925"], ["Покрытие", "родий"]]),
    P("e4", "Серьги-пусеты с камнем", "earrings", 14900, "e4", "Золото 585 · фианит", "Небольшие пусеты: первые серьги в шкатулке или вторая пара в ухо.",
      [["Металл", "жёлтое золото 585"], ["Замок", "винтовой"]], nw=True),
    P("n1", "Колье с овальной подвеской", "necklaces", 38500, "n1", "Золото 585", "Овальный медальон на тонкой цепочке. На обороте можно сделать гравировку.",
      [["Металл", "жёлтое золото 585"]], eng=True),
    P("n2", "Цепочка с круглой подвеской", "necklaces", 24900, "n2", "Золото 585", "Тонкая цепочка и маленький диск: носится с любой одеждой.",
      [["Металл", "жёлтое золото 585"]], tag="Хит"),
    P("n3", "Подвеска с жемчугом", "necklaces", 29900, "n3", "Золото 585 · жемчуг", "Барочная жемчужина в свободной оправе: двух одинаковых не бывает.",
      [["Металл", "жёлтое золото 585"], ["Вставка", "жемчуг пресноводный"]]),
    P("n4", "Цепь якорного плетения", "necklaces", 42000, "n4", "Золото 585 · 3 мм", "Плотная цепь, которую носят одну или с подвесками.",
      [["Металл", "жёлтое золото 585"], ["Ширина", "3 мм"]]),
    P("b1", "Браслет-цепь «Звено»", "bracelets", 36000, "b1", "Золото 585", "Крупные звенья, надёжный замок-карабин.",
      [["Металл", "жёлтое золото 585"], ["Длина", "18 см"]]),
    P("b2", "Браслет с пластиной для гравировки", "bracelets", 28500, "b2", "Золото 585", "Тонкий браслет с пластиной: имя, дата или координаты.",
      [["Металл", "жёлтое золото 585"], ["Длина", "17–19 см"]], eng=True),
    P("b3", "Браслеты с шармами, набор из 3", "bracelets", 33000, "b3", "Золото 585", "Три тонких браслета с подвесками, которые звенят совсем тихо.",
      [["Металл", "жёлтое золото 585"]], nw=True),
]

WIDGET_HTML = """
<div class="rg">
 <div>
  <div class="kick">Размер и гравировка</div>
  <h2 style="margin:12px 0 12px">Подойдёт по размеру <em>и будет только вашим</em></h2>
  <p class="lead" style="font-size:17px">Обмотайте палец полоской бумаги, отметьте стык и измерьте длину. Ниже покажем размер и то, как будет выглядеть гравировка.</p>
  <div class="gq"><b>Обхват пальца · <span id="rgC">53 мм</span></b><input type="range" id="rgR" min="46" max="62" step="0.5" value="53"></div>
  <div class="rgsize">Ваш размер <b id="rgS">17</b><span id="rgH"></span></div>
  <div class="gq"><b>Гравировка</b><input type="text" id="rgT" maxlength="18" value="Навсегда" placeholder="До 18 знаков" class="rgin">
   <div class="gtags" id="rgF"><button data-f="i" aria-pressed="true"><i>Курсив</i></button><button data-f="n" aria-pressed="false">Прямой</button></div></div>
  <div class="gq"><b>Изделие</b><select id="rgP" class="rgin"></select></div>
  <button class="btn" type="button" id="rgAdd" style="margin-top:22px">Добавить с гравировкой</button>
 </div>
 <div class="rgview">
  <svg viewBox="0 0 400 300" role="img" aria-label="Примерка гравировки на кольце">
   <defs><linearGradient id="rgG" x1="0" x2="1"><stop offset="0" stop-color="#b98d3e"/><stop offset=".3" stop-color="#f3dc9a"/><stop offset=".55" stop-color="#d2a956"/><stop offset=".8" stop-color="#f6e6b4"/><stop offset="1" stop-color="#a67c32"/></linearGradient>
   <path id="rgArc" d="M40 150 Q200 232 360 150" fill="none"/></defs>
   <path d="M30 118 Q200 200 370 118 L370 182 Q200 264 30 182 Z" fill="url(#rgG)"/>
   <path d="M30 118 Q200 200 370 118" fill="none" stroke="rgba(255,255,255,.55)" stroke-width="2"/>
   <path d="M30 182 Q200 264 370 182" fill="none" stroke="rgba(90,60,10,.35)" stroke-width="2"/>
   <text id="rgTx" font-size="30" fill="rgba(80,52,8,.82)" text-anchor="middle" letter-spacing="2"><textPath href="#rgArc" startOffset="50%" id="rgTp">Навсегда</textPath></text>
  </svg>
  <p>Так гравировка выглядит на внутренней стороне кольца. Наносим лазером в день заказа, это бесплатно.</p>
 </div>
</div>"""

WIDGET_CSS = """
.rg{display:grid;grid-template-columns:1fr 1fr;gap:clamp(24px,4vw,64px);align-items:center}
.rg h2 em{font-style:italic;color:var(--ac)}
.gq{margin-top:22px}
.gq b{display:block;font:500 12px/1 var(--fb);letter-spacing:.14em;text-transform:uppercase;color:var(--soft);margin-bottom:12px}
.rg input[type=range]{width:100%;accent-color:var(--ac)}
.rgsize{margin-top:16px;font-size:16px;color:var(--soft);display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
.rgsize b{font-family:var(--fh);font-size:54px;line-height:1;color:var(--ink);font-weight:400}
.rgsize span{font-size:14px}
.rgin{width:100%;height:50px;padding:0 14px;border:1px solid var(--line2);border-radius:var(--rb);background:transparent;font:inherit;color:var(--ink)}
.gtags{display:flex;gap:8px;margin-top:10px}
.gtags button{height:40px;padding:0 16px;border:1px solid var(--line2);border-radius:var(--rb);font-size:15px}
.gtags button[aria-pressed=true]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.rgview{background:var(--card);padding:clamp(20px,3vw,40px);border-radius:var(--rs)}
.rgview svg{width:100%;height:auto;display:block}
.rgview p{margin:10px 0 0;font-size:14px;color:var(--soft);text-align:center}
@media (max-width:860px){.rg{grid-template-columns:1fr}}
"""

WIDGET_JS = r"""
(function(){
var S=window.SHOP,$=function(s){return document.querySelector(s)},font='i';
var list=S.products.filter(function(p){return p.eng});
$('#rgP').innerHTML=list.map(function(p){return'<option value="'+p.id+'">'+S.esc(p.n)+' · '+S.fmt(p.p)+'</option>'}).join('');
function size(){var c=+$('#rgR').value,d=Math.round(c/Math.PI*2)/2;d=Math.max(15.5,Math.min(19,d));return d}
function draw(){var c=+$('#rgR').value,s=size();$('#rgC').textContent=String(c).replace('.',',')+' мм';$('#rgS').textContent=String(s).replace('.',',');
 $('#rgH').textContent=c/Math.PI>19.2||c/Math.PI<15.3?'Такого размера нет в наличии, изготовим за 7 дней':'Между размерами выбирайте больший';
 var t=$('#rgT').value.trim()||' ';$('#rgTp').textContent=t;var x=$('#rgTx');
 x.setAttribute('font-style',font==='i'?'italic':'normal');x.setAttribute('font-family',font==='i'?'Georgia,"Times New Roman",serif':'Arial,Helvetica,sans-serif');
 x.setAttribute('font-size',t.length>13?22:t.length>9?26:30)}
['#rgR','#rgT'].forEach(function(id){$(id).addEventListener('input',draw)});
$('#rgF').onclick=function(e){var b=e.target.closest('button');if(!b)return;font=b.dataset.f;this.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});draw()};
$('#rgAdd').addEventListener('click',function(){var p=S.byId[$('#rgP').value],o={},t=$('#rgT').value.trim();
 if(p.cat==='rings')o['Размер']=String(size()).replace('.',',');if(p.cat==='necklaces')o['Длина']='45 см';
 if(t)o['Гравировка']=t+(font==='i'?' (курсив)':' (прямой)');S.add(p.id,o,1)});
draw();
})();
"""


def cfg():
    return {
        "slug": "shops/ore", "images": IMG, "brand": "Орэ",
        "logo": '<span style="font-family:var(--fh);font-size:30px;letter-spacing:.12em">ОРЭ</span><span style="font:500 10px/1 var(--fb);letter-spacing:.2em;text-transform:uppercase;color:var(--mut);margin-left:10px">ювелирный дом</span>',
        "title": "Орэ — украшения из золота и серебра с гравировкой",
        "desc": "Кольца, серьги, колье и браслеты из золота 585 и серебра 925. Определитель размера кольца, бесплатная гравировка в день заказа, доставка в фирменном футляре.",
        "variant": "editorial", "favLetter": "О",
        "theme": {"bg": "#f7f4ee", "ink": "#1e1b18", "soft": "#57504a", "mut": "#968d84", "line": "rgba(30,27,24,.12)", "line2": "rgba(30,27,24,.28)",
                  "card": "#ece6db", "ac": "#8c6a2f", "aci": "#fff", "ok": "#4f7a52", "rc": "0px", "rb": "0px", "rs": "0px", "rh": "0px",
                  "fh": '"Forum",Georgia,serif', "fb": '"Jost",system-ui,sans-serif', "fm": '"Jost",system-ui,sans-serif', "fp": '"Forum",Georgia,serif',
                  "hw": "400", "ht": "0", "hc": "none", "lw": "400", "lt": ".12em", "ar": "4/5"},
        "fonts": [("Forum", "forum", [400], "normal"), ("Jost", "jost", [400, 500, 600], "normal")],
        "strip": "Гравировка <b>бесплатно</b> в день заказа · доставка курьером в футляре · обмен размера без доплаты",
        "nav": [("Украшения", "catalog"), ("Размер и гравировка", "feat"), ("Сервис", "why"), ("Вопросы", "faq")],
        "searchPh": "Кольцо, серьги, цепочка…",
        "hero": {"kicker": "Ювелирный дом · Санкт-Петербург", "h1": "Украшения, которые <em>носят каждый день</em>", "img": "hero",
                 "lead": "Золото 585 и серебро 925, лаконичные формы и камни без лишнего блеска. Сделаем гравировку и подберём размер, не выходя из дома.",
                 "cta": "Смотреть украшения", "ctaTo": "catalog", "cta2": "Узнать размер кольца", "cta2To": "feat",
                 "stats": [("585", "проба золота"), ("1 день", "гравировка и отправка"), ("30 дней", "на обмен размера")],
                 "float": {"img": "r3", "t": "Кольцо «Линия»", "s": "21 500 ₽ · гравировка внутри"}},
        "cats": [{"id": "rings", "n": "Кольца", "img": "r2", "s": "помолвочные и на каждый день"}, {"id": "earrings", "n": "Серьги", "img": "e1", "s": "пусеты, кольца, подвески"},
                 {"id": "necklaces", "n": "Колье и цепи", "img": "n2", "s": "с подвесками и без"}, {"id": "bracelets", "n": "Браслеты", "img": "b1", "s": "цепи и наборы"}],
        "products": PRODUCTS, "pageSize": 8, "showStars": False, "cardSizes": "(max-width:860px) 50vw, 25vw",
        "freeFrom": 15000, "promo": {"code": "ОРЭ", "pct": 7, "hint": "ОРЭ — минус 7% на первое украшение"},
        "ship": [{"id": "cour", "name": "Курьер с примеркой", "eta": "завтра, оплата после примерки", "price": 490, "free": 15000},
                 {"id": "post", "name": "Застрахованная доставка по России", "eta": "2–5 дней, с описью", "price": 690, "free": 30000},
                 {"id": "pick", "name": "Салон на Большой Конюшенной", "eta": "сегодня, с 11 до 21", "price": 0}],
        "commentPh": "Текст гравировки, пожелания к упаковке",
        "doneNote": "Ювелир пришлёт фото гравировки перед отправкой.",
        "addLabel": "В корзину",
        "widget": {"nav": "Размер и гравировка", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS},
        "usp": [("Проба и бирка", "На каждом изделии клеймо пробирной палаты и бирка с весом и характеристиками камней."),
                ("Гравировка за день", "Наносим лазером в мастерской, перед отправкой присылаем фото."),
                ("Обмен размера", "Не подошло кольцо: поменяем на другой размер в течение 30 дней без доплаты."),
                ("Уход раз в год", "Бесплатно почистим, отполируем и проверим закрепку камней.")],
        "uspTitle": "Покупка, в которой спокойно", "uspKick": "Сервис",
        "faq": [("Как узнать размер кольца?", "Измерьте обхват пальца полоской бумаги вечером, когда руки тёплые, и введите длину в определитель. Сомневаетесь: привезём два размера на примерку."),
                ("Можно ли вернуть украшение с гравировкой?", "Изделие с гравировкой сделано для вас, поэтому вернуть его нельзя, но размер поменяем или подгоним в мастерской."),
                ("Что будет в комплекте?", "Фирменный футляр, бирка с характеристиками, чек и салфетка для ухода. По просьбе уберём чек и добавим открытку."),
                ("Камни натуральные?", "Да. Для бриллиантов и сапфиров указываем вес, цвет и чистоту на бирке, к камням от 0,3 карата прикладываем сертификат.")],
        "footBig": "На каждый день и на всю жизнь",
        "contacts": {"addr": "Санкт-Петербург, Большая Конюшенная, 9", "hours": "Ежедневно 11:00–21:00"},
        "order": ["cats", "catalog", "widget", "usp", "faq"], "gridTitle": "Коллекция", "gridKick": "Золото и серебро",
        "css": ".v-editorial .hero h1{font-size:clamp(40px,5.2vw,80px);line-height:1.04;hyphens:manual}.card .nm{font-family:var(--fh);font-size:21px;line-height:1.2}"
               ".price{font-weight:500}.btn{letter-spacing:.1em;text-transform:uppercase;font-size:13px}",
    }
