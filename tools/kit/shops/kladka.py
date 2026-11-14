"""«Кладка» — стройматериалы для частных стройщиков и бригад: калькулятор стены (блоки, клей, поддоны, машина)."""

IMG = {
    "hero": ("1672627170267-fca17bb54156", 16, 9, "800,1400,2000"),
    "bricks": ("1637241612956-b7309005288b", 1, 1, "500,900"),
    "brickwall": ("1627882206813-8c1ffd86efec", 1, 1, "500,900"),
    "frame": ("1517011453931-c30f571a4fab", 1, 1, "500,900"),
    "pipes": ("1580810734898-5e1753f23337", 1, 1, "500,900"),
    "site": ("1508450859948-4e04fabaa4ea", 1, 1, "500,900"),
    "crane": ("1609867271967-a82f85c48531", 1, 1, "500,900"),
    "drill": ("1518709414768-a88981a4515d", 1, 1, "500,900"),
    "drill2": ("1590635023142-73c3d34f2805", 1, 1, "500,900"),
    "tools": ("1540103711724-ebf833bde8d1", 1, 1, "500,900"),
    "toolset": ("1606676539940-12768ce0e762", 1, 1, "500,900"),
    "saw": ("1585201731775-0597e1be4bfb", 1, 1, "500,900"),
    "worker": ("1587582423116-ec07293f0395", 1, 1, "500,900"),
    "pour": ("1774931363306-5a896cd4dd02", 1, 1, "500,900"),
    "roller": ("1599619585752-c3edb42a414c", 1, 1, "500,900"),
}


def P(id, n, cat, p, img, m, d, s, unit="шт.", old=None, tag=None, opt=None, f=None):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": s, "unit": unit, "f": f or {}}
    if old:
        x["old"] = old
    if tag:
        x["tag"] = tag
    if opt:
        x["opt"] = opt
    x["stock"] = "Склад в Мытищах · доставка завтра манипулятором"
    return x


PRODUCTS = [
    P("b1", "Газобетонный блок D500, 600×300×250", "walls", 289, "site", "за блок · поддон 40 шт.",
      "Тёплый и лёгкий блок для несущих стен до 3 этажей. Ровная геометрия ±1 мм — кладка на клей.",
      [["Плотность", "D500"], ["Размер", "600×300×250 мм"], ["Прочность", "B3,5"], ["На поддоне", "40 шт."]], tag="Хит", opt=280, f={"brand": "Bonolit"}),
    P("b2", "Кирпич облицовочный «Красный гладкий»", "walls", 32, "brickwall", "за штуку · поддон 480 шт.",
      "Морозостойкость F100, водопоглощение до 8%. Одна партия — один оттенок.",
      [["Марка", "М175"], ["Размер", "250×120×65 мм"]], opt=29, f={"brand": "Кирово-Чепецк"}),
    P("b3", "Кирпич рядовой полнотелый М150", "walls", 18, "bricks", "за штуку",
      "Для фундаментов, цоколей и печей.", [["Марка", "М150"]], opt=16, f={"brand": "Кирово-Чепецк"}),
    P("m1", "Клей для газобетона, 25 кг", "mix", 420, "pour", "Зимний до −10 °C",
      "Тонкий шов 2 мм — меньше мостиков холода. Мешка хватает на 1,5 м³ кладки.", [["Расход", "25 кг на 1,5 м³"]], opt=380, f={"brand": "Ceresit"}),
    P("m2", "Цемент М500 Д0, 50 кг", "mix", 590, "pour", "ЦЕМ I 42,5Н",
      "Без добавок — для фундаментов и стяжек.", [["Марка", "М500"]], old=650, opt=540, f={"brand": "Евроцемент"}),
    P("m3", "Кладочная сетка 50×50, рулон 50 м²", "mix", 2890, "frame", "Проволока 3 мм",
      "Армирование каждого 4-го ряда кладки.", [["Ячейка", "50×50 мм"]], f={"brand": "Северсталь"}),
    P("r1", "Арматура А500С, 12 мм, 11,7 м", "metal", 640, "pipes", "за хлыст",
      "Рифлёная арматура для фундаментов и армопоясов. Режем в размер на складе бесплатно.", [["Диаметр", "12 мм"], ["Длина", "11,7 м"]], opt=590, f={"brand": "Северсталь"}),
    P("r2", "Профильная труба 40×20, 6 м", "metal", 780, "frame", "Сталь 2 мм",
      "Для каркасов навесов и заборов.", [["Сечение", "40×20×2 мм"]], f={"brand": "Северсталь"}),
    P("t1", "Дрель-шуруповёрт аккумуляторная 18 В", "tools", 8990, "drill2", "2 АКБ · кейс",
      "Два аккумулятора по 2 А·ч и быстрая зарядка за 40 минут.", [["Крутящий момент", "60 Н·м"]], tag="−15%", old=10590, f={"brand": "Зубр"}),
    P("t2", "Перфоратор SDS-plus 800 Вт", "tools", 7490, "drill", "3 режима",
      "Сверление, удар и долбление. В кейсе — три бура.", [["Энергия удара", "3 Дж"]], f={"brand": "Зубр"}),
    P("t3", "Набор ручного инструмента, 48 предметов", "tools", 3490, "toolset", "В кейсе",
      "Молоток, отвёртки, ключи, уровень и рулетка — для ремонта и стройки.", [["Предметов", "48"]], f={"brand": "Зубр"}),
    P("t4", "Ножовка по газобетону", "tools", 1290, "saw", "Твердосплавные зубья",
      "Пилит блоки ровно, без сколов.", [["Длина", "550 мм"]], f={"brand": "Зубр"}),
    P("f1", "Валик фасадный с ручкой", "finish", 690, "roller", "Для грунта и краски",
      "Шубка 18 мм для штукатурки и бетона.", [["Ширина", "250 мм"]], f={"brand": "Ceresit"}),
]

WIDGET_HTML = """
<div class="calc">
 <div>
  <div class="kick">Калькулятор кладки</div>
  <h2 style="margin:12px 0 12px">Сколько блоков на <em>ваш</em> дом</h2>
  <p class="lead" style="font-size:17px">Введите размеры — посчитаем блоки с запасом 5%, клей, сетку, поддоны и машину. Цены — оптовые, от одного поддона.</p>
  <div class="cg"><b>Материал</b><div class="seg" id="cMat"><button data-v="gas" aria-pressed="true">Газобетон D500</button><button data-v="brick" aria-pressed="false">Кирпич облицовочный</button></div></div>
  <div class="cgrid">
   <label>Периметр стен, м<input id="cP" type="number" min="1" value="40" inputmode="decimal"></label>
   <label>Высота этажа, м<input id="cH" type="number" min="1" step="0.1" value="3" inputmode="decimal"></label>
   <label>Этажей<input id="cF" type="number" min="1" max="3" value="1" inputmode="numeric"></label>
   <label>Окна и двери, м²<input id="cO" type="number" min="0" value="14" inputmode="decimal"></label>
  </div>
 </div>
 <div class="cres">
  <div class="cbig"><span>Нужно</span><b id="cN">—</b><small id="cU"></small></div>
  <ul id="cL"></ul>
  <div class="ctot"><span>Итого с доставкой</span><b id="cT"></b></div>
  <button class="btn wide" type="button" id="cAdd">Добавить всё в корзину</button>
  <small class="muted" style="display:block;margin-top:10px;font-size:13px">Менеджер проверит расчёт по проекту и позвонит в течение 20 минут.</small>
 </div>
</div>"""

WIDGET_CSS = """
#feat .feat{--fbg:#ffd400;--fink:#111}
.calc{display:grid;grid-template-columns:1.1fr 1fr;gap:clamp(24px,4vw,56px)}
.calc h2 em{font-style:normal;background:#111;color:#ffd400;padding:0 .12em}
.cg{margin-top:22px}
.cg b{display:block;font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;margin-bottom:10px}
.seg{display:flex;gap:6px;flex-wrap:wrap}
.seg button{height:44px;padding:0 16px;border-radius:8px;font-size:15px;font-weight:600;box-shadow:inset 0 0 0 2px #111}
.seg button[aria-pressed=true]{background:#111;color:#ffd400}
.cgrid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:18px}
.cgrid label{display:grid;gap:6px;font-size:13px;font-weight:600}
.cgrid input{height:52px;border-radius:8px;border:0;padding:0 14px;font-size:18px;font-weight:600;background:#fff;box-shadow:inset 0 0 0 2px #111}
.cres{background:#111;color:#fff;border-radius:16px;padding:clamp(20px,3vw,32px)}
.cbig span{font-size:13px;color:rgba(255,255,255,.55);text-transform:uppercase;letter-spacing:.08em}
.cbig b{display:block;font-family:var(--fh);font-size:clamp(48px,6vw,76px);line-height:1;color:#ffd400}
.cbig small{font-size:15px;color:rgba(255,255,255,.75)}
.cres ul{list-style:none;margin:20px 0;padding:0;display:grid;gap:10px;font-size:15px}
.cres li{display:flex;justify-content:space-between;gap:12px;padding-bottom:10px;border-bottom:1px dashed rgba(255,255,255,.15)}
.cres li span:last-child{white-space:nowrap;font-weight:600}
.ctot{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:16px}
.ctot b{font-size:28px}
.cres .btn{background:#ffd400;color:#111}
@media (max-width:860px){.calc{grid-template-columns:1fr}}
.card .opt{font-size:12px;color:var(--ok);font-weight:600}
"""

WIDGET_JS = r"""
(function(){
var S=window.SHOP,$=function(s){return document.querySelector(s)},mat='gas',R={};function pl(n,f){n=Math.abs(n)%100;var a=n%10;return n>10&&n<20?f[2]:a>1&&a<5?f[1]:a==1?f[0]:f[2]}function nf(x){return x.toLocaleString('ru-RU',{maximumFractionDigits:1})}
function v(id){return Math.max(0,parseFloat($(id).value.replace(',','.'))||0)}
function calc(){var area=v('#cP')*v('#cH')*Math.max(1,Math.round(v('#cF')))-v('#cO'),L=[],tot=0;area=Math.max(0,area);
 if(mat==='gas'){var vol=area*.3,blocks=Math.ceil(vol/(.6*.3*.25)*1.05),pal=Math.ceil(blocks/40),glue=Math.ceil(vol/1.5),mesh=Math.ceil(area/4/50);
  var bp=pal>=1?S.byId.b1.opt:S.byId.b1.p;R={b1:blocks,m1:glue,m3:mesh};
  L=[['Блоки D500 · '+blocks+' шт. ('+pal+' под.)',blocks*bp],['Клей · '+glue+' меш.',glue*S.byId.m1.p],['Сетка · '+mesh+' рул.',mesh*S.byId.m3.p]];
  $('#cN').textContent=blocks+' '+pl(blocks,['блок','блока','блоков']);$('#cU').textContent=nf(area)+' м² стен · '+nf(vol)+' м³ · ≈'+nf(Math.round(vol*500/100)/10)+' т'}
 else{var br=Math.ceil(area*51*1.05),pal2=Math.ceil(br/480),cem=Math.ceil(area*.025*1.7/0.05/10);R={b2:br,m2:cem};
  L=[['Кирпич · '+br+' шт. ('+pal2+' под.)',br*S.byId.b2.opt],['Цемент М500 · '+cem+' меш.',cem*S.byId.m2.p]];
  $('#cN').textContent=br+' '+pl(br,['кирпич','кирпича','кирпичей']);$('#cU').textContent=nf(area)+' м² облицовки · ≈'+nf(Math.round(br*3.6/100)/10)+' т'}
 var trips=Math.max(1,Math.ceil((mat==='gas'?Math.ceil((R.b1||0)/40):Math.ceil((R.b2||0)/480))/10));L.push(['Манипулятор · '+trips+' '+pl(trips,['рейс','рейса','рейсов']),trips*6500]);
 tot=L.reduce(function(a,x){return a+x[1]},0);R.total=tot;R.trips=trips;
 $('#cL').innerHTML=L.map(function(x){return'<li><span>'+x[0]+'</span><span>'+S.fmt(x[1])+'</span></li>'}).join('');$('#cT').textContent=S.fmt(tot)}
['#cP','#cH','#cF','#cO'].forEach(function(id){$(id).addEventListener('input',calc)});
$('#cMat').onclick=function(e){var b=e.target.closest('button');if(!b)return;mat=b.dataset.v;this.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});calc()};
$('#cAdd').onclick=function(){var main=mat==='gas'?'b1':'b2';S.add(main,{'Расчёт':$('#cN').textContent+', манипулятор '+R.trips+' рейс.'},1,{price:R.total,name:'Материалы на стены по расчёту'})};
calc();
new MutationObserver(function(){document.querySelectorAll('#grid .card:not([data-x])').forEach(function(el){el.dataset.x=1;var p=S.byId[el.dataset.id];if(p.opt)el.querySelector('.price').insertAdjacentHTML('afterend','<div class="opt">от поддона '+S.fmt(p.opt)+'</div>');var m=el.querySelector('.meta');m.textContent=p.m})}).observe(document.getElementById('grid'),{childList:true});
})();
"""


def cfg():
    return {
        "slug": "shops/kladka", "images": IMG, "brand": "КЛАДКА",
        "logo": '<b style="background:#111;color:#ffd400;border-radius:4px">К</b>КЛАДКА',
        "title": "КЛАДКА — стройматериалы с доставкой манипулятором, Подмосковье",
        "desc": "Газобетон, кирпич, смеси, металл и инструмент оптом и в розницу. Калькулятор кладки, оптовые цены от поддона и доставка манипулятором на следующий день.",
        "variant": "mega", "favLetter": "К",
        "theme": {"bg": "#f3f3f1", "ink": "#111111", "soft": "#3b3b39", "mut": "#7a7a75", "line": "rgba(17,17,17,.12)", "line2": "rgba(17,17,17,.3)",
                  "card": "#e7e7e3", "ac": "#ffd400", "aci": "#111", "ac2": "#ffd400", "ok": "#1b7f3a", "rc": "10px", "rb": "8px", "rs": "16px",
                  "fh": '"Fira Sans Extra Condensed",Impact,sans-serif', "fb": '"IBM Plex Sans",system-ui,sans-serif', "fm": '"IBM Plex Sans",system-ui,sans-serif',
                  "hw": "800", "ht": "0", "hc": "uppercase", "emst": "normal", "lw": "800", "lt": ".02em", "ar": "1/1", "cardbg": "#fff", "cpad": "14px", "cpadb": "14px", "rl": "4px"},
        "fonts": [("Fira Sans Extra Condensed", "fira-sans-extra-condensed", [700, 800], "normal"), ("IBM Plex Sans", "ibm-plex-sans", [400, 500, 600], "normal")],
        "strip": "Доставка манипулятором <b>завтра</b> · оптовые цены от 1 поддона · работаем с НДС",
        "nav": [("Каталог", "catalog"), ("Калькулятор", "feat"), ("Доставка", "why"), ("Вопросы", "faq")],
        "searchPh": "Газоблок, цемент, арматура…",
        "hero": {"kicker": "Стройбаза в Мытищах · с 2009 года", "h1": "Материалы на коробку <em>за один заказ</em>", "img": "hero",
                 "lead": "Посчитаем блоки, клей и арматуру по размерам дома, привезём манипулятором завтра и выгрузим на участок.",
                 "cta": "Посчитать кладку", "ctaTo": "feat", "cta2": "Каталог", "cta2To": "catalog",
                 "stats": [("12 000 м²", "склад"), ("24 машины", "свой автопарк"), ("с НДС", "для юрлиц")],
                 "tiles": [{"k": "Опт", "t": "Газобетон от поддона — 280 ₽/шт.", "cat": "walls", "img": "bricks", "a": "Стеновые →"},
                           {"k": "Бригадам", "t": "Инструмент −15% до конца месяца", "cat": "tools", "img": "drill2", "a": "Инструмент →"}]},
        "cats": [{"id": "walls", "n": "Стеновые"}, {"id": "mix", "n": "Смеси и сетка"}, {"id": "metal", "n": "Металл"}, {"id": "tools", "n": "Инструмент"}, {"id": "finish", "n": "Отделка"}],
        "facets": {"brand": ("Производитель", ["Bonolit", "Кирово-Чепецк", "Ceresit", "Евроцемент", "Северсталь", "Зубр"])},
        "products": PRODUCTS, "pageSize": 12, "showStars": False, "cardSizes": "(max-width:860px) 50vw, 300px",
        "freeFrom": 0, "promo": {"code": "БРИГАДА", "pct": 3, "hint": "БРИГАДА — минус 3% на заказ"},
        "ship": [{"id": "man", "name": "Манипулятор с выгрузкой", "eta": "завтра, до 30 км от МКАД", "price": 6500},
                 {"id": "gaz", "name": "Газель до 1,5 т", "eta": "сегодня или завтра", "price": 2900},
                 {"id": "pick", "name": "Самовывоз со склада", "eta": "Мытищи, Осташковское ш., 14", "price": 0}],
        "addrNote": "участок или СНТ, номер дома",
        "slotNote": "Водитель позвонит за час. Нужен подъезд для машины шириной 2,5 м.",
        "commentPh": "Как проехать, есть ли место для разгрузки",
        "doneNote": "Менеджер позвонит в течение 20 минут, сверит расчёт и время машины.",
        "widget": {"nav": "Калькулятор", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS},
        "usp": [("Свой автопарк", "24 машины: манипуляторы, газели и длинномеры. Выгрузим, куда покажете."),
                ("Оптовые цены от поддона", "Не нужно быть оптовиком — цена ниже уже с одного поддона."),
                ("Возврат остатков", "Не пригодились целые блоки или мешки — примем обратно в течение 30 дней."),
                ("Работаем с НДС", "Счёт, договор и закрывающие документы для юрлиц и ИП.")],
        "uspTitle": "Стройка без простоев", "uspKick": "Почему мы",
        "faq": [("Как рассчитать количество блоков?", "Воспользуйтесь калькулятором выше: он учитывает проёмы и запас 5%. Пришлите проект — посчитаем бесплатно и точнее."),
                ("Можно вернуть лишнее?", "Да, целые блоки и непочатые мешки примем в течение 30 дней. Поддоны выкупаем обратно по 250 ₽."),
                ("Довезёте до участка без дороги?", "Манипулятор проходит по грунтовке. Если дорога размыта — подскажем, как разгрузиться у въезда и докинуть краном."),
                ("Есть отсрочка для бригад?", "Да, для постоянных клиентов — отсрочка до 14 дней и персональный менеджер.")],
        "footBig": "Привезём завтра — стройте спокойно",
        "contacts": {"addr": "Мытищи, Осташковское ш., 14", "hours": "Пн–Сб 7:00–20:00, Вс 8:00–18:00"},
        "order": ["catalog", "widget", "usp", "faq"], "gridTitle": "Склад сегодня",
        "css": ".hero h1{font-size:clamp(44px,6vw,92px);line-height:.92}.v-mega .hero h1 em{color:#ffd400}.add{background:#111;color:#ffd400}.chip[aria-pressed=true]{background:#111;color:#ffd400}"
               ".btn{color:#111}.strip b{color:#ffd400}",
    }
