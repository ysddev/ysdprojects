"""ДЕТАЛЬ — автозапчасти: подбор по машине и VIN, наличие по складам, кросс-номера."""

IMG = {
    "hero": ("1615906655593-ad0386982a0f", 16, 9, "800,1400,2000"),
    "engine": ("1486262715619-67b85e0b08d3", 4, 3, "600,1000"),
    "oilfill": ("1487754180451-c456f719a1fc", 4, 3, "600,1000"),
    "brake": ("1760317890314-e964ffd7e6a6", 1, 1, "500,900"),
    "brake2": ("1760317890322-364a810cd4da", 1, 1, "500,900"),
    "caliper": ("1696494561430-de087dd0bd69", 1, 1, "500,900"),
    "rotor": ("1613214150384-14921ff659b2", 1, 1, "500,900"),
    "oil": ("1590227763209-821c686b932f", 1, 1, "500,900"),
    "cans": ("1771581136070-5322586211d6", 1, 1, "500,900"),
    "wheel": ("1444947295498-07f60c19a4ff", 1, 1, "500,900"),
    "tires": ("1571335746824-742511d49bce", 1, 1, "500,900"),
    "rim": ("1601411101851-ea0e07766235", 1, 1, "500,900"),
    "tirestack": ("1760836395760-9831facb4754", 1, 1, "500,900"),
    "headlight": ("1556448851-9359658faa54", 1, 1, "500,900"),
    "gauge": ("1517026575980-3e1e2dedeab4", 1, 1, "500,900"),
    "part": ("1537462715879-360eeb61a0ad", 1, 1, "500,900"),
    "mech": ("1767884162326-54d3e26d444a", 1, 1, "500,900"),
    "bay": ("1779263569890-ce0389630b10", 1, 1, "500,900"),
    "exhaust": ("1759419281419-b04552b2691a", 1, 1, "500,900"),
}

CARS = {
    "Kia": {"Rio IV": ["1.4 MPI", "1.6 MPI"], "Sportage IV": ["2.0 MPI", "2.4 GDI"], "Ceed III": ["1.6 MPI", "1.4 T-GDI"]},
    "Hyundai": {"Solaris II": ["1.4 MPI", "1.6 MPI"], "Creta I": ["1.6 MPI", "2.0 MPI"], "Tucson III": ["2.0 MPI"]},
    "Toyota": {"Camry XV70": ["2.5", "3.5"], "RAV4 XA50": ["2.0", "2.5"], "Corolla E210": ["1.6"]},
    "Volkswagen": {"Polo VI": ["1.6 MPI", "1.4 TSI"], "Tiguan II": ["1.4 TSI", "2.0 TSI"]},
    "Lada": {"Vesta": ["1.6", "1.8"], "Granta": ["1.6 8V", "1.6 16V"]},
    "Skoda": {"Octavia A7": ["1.4 TSI", "1.8 TSI"], "Rapid": ["1.6 MPI"]},
}

K = "Kia Rio IV|Hyundai Solaris II|Hyundai Creta I"
T = "Toyota Camry XV70|Toyota RAV4 XA50"
V = "Volkswagen Polo VI|Skoda Rapid|Skoda Octavia A7|Volkswagen Tiguan II"
L = "Lada Vesta|Lada Granta"


def P(id, n, cat, p, img, m, d, s, fits="", f=None, old=None, tag=None, sku="", stock=None, kw=""):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": s, "fits": fits, "f": f or {}, "sku": sku, "kw": kw}
    if old:
        x["old"] = old
    if tag:
        x["tag"] = tag
    x["stock"] = stock or "Склад на Каширке — 14 шт., самовывоз сегодня"
    return x


PRODUCTS = [
    P("bp1", "Колодки тормозные передние, керамика", "brakes", 3290, "brake", "Brembo-аналог · TRW",
      "Керамический состав: меньше пыли на дисках, тихое торможение и ресурс до 45 000 км. Датчик износа в комплекте.",
      [["Артикул", "GDB3486"], ["Ось", "передняя"], ["Ресурс", "до 45 000 км"], ["Гарантия", "12 мес."]], K, {"brand": "TRW", "kind": "Оригинал-аналог"}, 3890, "Хит", "GDB3486", kw="колодки тормоза"),
    P("bp2", "Диск тормозной вентилируемый, 280 мм", "brakes", 4150, "rotor", "ATE · пара",
      "Вентилируемый диск с антикоррозийным покрытием ступицы. Продаётся парой, балансировка с завода.",
      [["Артикул", "24.0128-0213"], ["Диаметр", "280 мм"], ["Толщина", "23 мм"], ["Кол-во", "2 шт."]], K, {"brand": "ATE", "kind": "Оригинал-аналог"}, sku="24.0128-0213"),
    P("bp3", "Суппорт передний левый в сборе", "brakes", 7890, "caliper", "Восстановленный · с гарантией",
      "Суппорт после заводского восстановления: новые поршни, пыльники и направляющие. Залог за старый — 1 500 ₽.",
      [["Артикул", "58180-1R000"], ["Сторона", "левая"], ["Гарантия", "6 мес."]], K, {"brand": "Mando", "kind": "Восстановленный"}, sku="58180-1R000", tag="Обмен"),
    P("bp4", "Колодки задние барабанные", "brakes", 1890, "brake2", "Sangsin",
      "Колодки для барабанных тормозов, корейский производитель первичной комплектации.",
      [["Артикул", "SA144"], ["Ось", "задняя"]], K + "|" + L, {"brand": "Sangsin", "kind": "Оригинал-аналог"}, sku="SA144"),
    P("oil1", "Масло моторное 5W-30, синтетика, 4 л", "oil", 3490, "oil", "API SP · ACEA C3",
      "Полная синтетика для бензиновых двигателей с турбиной и без. Допуски VW 504/507, подходит для сажевых фильтров.",
      [["Вязкость", "5W-30"], ["Объём", "4 л"], ["Допуски", "VW 504 00 / 507 00, MB 229.51"]], K + "|" + V + "|" + T, {"brand": "Liqui", "kind": "Масла"}, 3990, "−12%", "LM-5W30-4", kw="масло 5w30"),
    P("oil2", "Масло моторное 0W-20 для гибридов, 4 л", "oil", 4290, "cans", "API SP · ILSAC GF-6A",
      "Низкая вязкость для современных атмосферных и гибридных моторов — быстрее прокачивается на холодном пуске.",
      [["Вязкость", "0W-20"], ["Объём", "4 л"]], T, {"brand": "Idemitsu", "kind": "Масла"}, sku="ID-0W20-4", tag="Новинка", kw="масло 0w20"),
    P("oil3", "Антифриз G12++ готовый, 5 л", "oil", 1290, "oilfill", "Розовый · до −40 °C",
      "Карбоксилатный антифриз, совместим с G12 и G12+. Ресурс 5 лет или 250 000 км.",
      [["Класс", "G12++"], ["Объём", "5 л"], ["Защита", "до −40 °C"]], K + "|" + V + "|" + L, {"brand": "Felix", "kind": "Масла"}, sku="FX-G12-5"),
    P("fl1", "Фильтр масляный", "filters", 490, "part", "Mann-Filter",
      "Фильтр с противодренажным клапаном — масло не стекает из системы после остановки мотора.",
      [["Артикул", "W 811/80"], ["Высота", "73 мм"]], K + "|" + L, {"brand": "Mann", "kind": "Оригинал-аналог"}, sku="W81180", kw="фильтр масляный"),
    P("fl2", "Фильтр салонный угольный", "filters", 890, "bay", "Mann-Filter",
      "Угольный слой задерживает запахи и выхлоп в пробках. Менять раз в год или каждые 15 000 км.",
      [["Артикул", "CUK 24 013"], ["Тип", "угольный"]], K + "|" + T, {"brand": "Mann", "kind": "Оригинал-аналог"}, sku="CUK24013", tag="Хит"),
    P("fl3", "Фильтр воздушный", "filters", 760, "mech", "Bosch",
      "Задерживает до 99,5% пыли, не снижает мощность мотора.",
      [["Артикул", "F 026 400 559"]], V, {"brand": "Bosch", "kind": "Оригинал-аналог"}, sku="F026400559"),
    P("wh1", "Шины зимние шипованные 205/55 R16, комплект", "wheels", 27960, "tires", "Nordman 8 · 4 шт.",
      "Финская разработка для снега и льда. 190 шипов на колесо, тихая на асфальте. Шиномонтаж в подарок при заказе комплекта.",
      [["Размер", "205/55 R16"], ["Индекс", "94T"], ["Шипы", "да"], ["Кол-во", "4 шт."]], K + "|" + V + "|" + L, {"brand": "Nordman", "kind": "Шины"}, 31960, "Сезон", "NM8-2055516", kw="шины зимние"),
    P("wh2", "Диски литые R17, 5×114,3, комплект", "wheels", 38400, "rim", "Скад · графит · 4 шт.",
      "Литые диски с центральным отверстием 67,1 — встают без колец на корейские и японские машины.",
      [["Размер", "7×17 ET45"], ["Сверловка", "5×114,3"], ["DIA", "67,1"]], K + "|" + T, {"brand": "Скад", "kind": "Диски"}, sku="SKAD-7017"),
    P("wh3", "Шины летние 225/45 R18, комплект", "wheels", 41200, "tirestack", "Continental · 4 шт.",
      "Короткий тормозной путь на мокром, низкий шум. Под заказ — привезём за 2 дня.",
      [["Размер", "225/45 R18"], ["Индекс", "95Y"]], T + "|" + V, {"brand": "Continental", "kind": "Шины"}, sku="CPC6-2254518", stock="Под заказ, 2 дня"),
    P("el1", "Фара передняя LED, левая", "light", 18900, "headlight", "Depo · E-маркировка",
      "Светодиодная фара с дневными ходовыми огнями, корректор в комплекте. Сертифицирована для РФ.",
      [["Артикул", "92101-H5600"], ["Тип", "LED"], ["Сторона", "левая"]], K, {"brand": "Depo", "kind": "Оригинал-аналог"}, sku="92101H5600"),
    P("el2", "Лампы H7 +150% света, пара", "light", 1890, "gauge", "Osram Night Breaker",
      "До 150 м света перед машиной, белее штатных. Законны, без доработок.",
      [["Цоколь", "H7"], ["Мощность", "55 Вт"]], K + "|" + V + "|" + T + "|" + L, {"brand": "Osram", "kind": "Оригинал-аналог"}, sku="64210NB200", kw="лампы h7"),
    P("su1", "Амортизатор передний газовый", "suspension", 5690, "wheel", "Kayaba Excel-G",
      "Газомасляный амортизатор, сохраняет управляемость на неровной дороге. Менять парой.",
      [["Артикул", "339275"], ["Тип", "газомасляный"], ["Гарантия", "2 года"]], K + "|" + L, {"brand": "Kayaba", "kind": "Оригинал-аналог"}, sku="339275"),
    P("ex1", "Катализатор-пламегаситель, универсальный", "engine", 9900, "exhaust", "Под сварку",
      "Замена убитого катализатора: нержавеющий корпус, не гремит. Установка в нашем сервисе — 2 часа.",
      [["Длина", "400 мм"], ["Диаметр", "55 мм"]], "", {"brand": "Polmostrow", "kind": "Оригинал-аналог"}, sku="PM-400-55"),
    P("en1", "Комплект ГРМ с помпой", "engine", 12450, "engine", "Gates PowerGrip",
      "Ремень, ролики и помпа одним комплектом — меняем всё сразу, чтобы не разбирать мотор дважды.",
      [["Артикул", "KP15565XS"], ["Состав", "ремень, 2 ролика, помпа"]], V + "|" + L, {"brand": "Gates", "kind": "Оригинал-аналог"}, 13990, sku="KP15565XS", kw="грм ремень"),
]

WIDGET_HTML = """
<div class="vf">
 <div>
  <div class="kick" style="color:var(--ac)">Подбор по машине</div>
  <h2 style="margin:14px 0 14px">Что подойдёт <em>именно</em> на вашу</h2>
  <p class="lead" style="color:rgba(255,255,255,.72)">Выберите машину или вставьте VIN — покажем только совместимые детали, а машину сохраним в «Мой гараж».</p>
  <div class="vf-tabs" role="tablist"><button role="tab" aria-selected="true" data-vt="car">По марке</button><button role="tab" aria-selected="false" data-vt="vin">По VIN</button></div>
  <div class="vf-car">
   <select id="vfMake" class="vsel" aria-label="Марка"><option value="">Марка</option></select>
   <select id="vfModel" class="vsel" aria-label="Модель" disabled><option>Модель</option></select>
   <select id="vfEng" class="vsel" aria-label="Двигатель" disabled><option>Двигатель</option></select>
   <button class="btn" type="button" id="vfGo" disabled>Показать детали</button>
  </div>
  <div class="vf-vin" hidden>
   <input id="vfVin" class="vsel" maxlength="17" placeholder="Например, Z94K241CBLR123456" aria-label="VIN" style="text-transform:uppercase;letter-spacing:.06em">
   <button class="btn" type="button" id="vfVinGo">Расшифровать</button>
   <p class="vf-hint">17 знаков, есть в СТС и под лобовым стеклом. Без I, O и Q.</p>
  </div>
 </div>
 <div class="vf-side">
  <div class="garage"><div class="kick" style="color:rgba(255,255,255,.55)">Мой гараж</div><div id="garage"><p class="vf-hint" style="margin-top:12px">Здесь появится ваша машина — подбор будет работать на всём сайте.</p></div></div>
  <div class="vf-res" id="vfRes" aria-live="polite"></div>
 </div>
</div>"""

WIDGET_CSS = """
#feat .feat{--fbg:#121417;--fink:#fff;background:radial-gradient(120% 140% at 100% 0%,#2a2f36 0%,#121417 55%)}
.vf{display:grid;grid-template-columns:1.1fr .9fr;gap:clamp(24px,4vw,56px);align-items:start}
.vf h2 em{font-style:normal;color:var(--ac)}
.vf-tabs{display:inline-flex;background:rgba(255,255,255,.08);border-radius:999px;padding:4px;margin:26px 0 16px}
.vf-tabs button{height:38px;padding:0 18px;border-radius:999px;font-size:14px;font-weight:600;color:rgba(255,255,255,.7)}
.vf-tabs button[aria-selected=true]{background:#fff;color:#121417}
.vf-car,.vf-vin{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.vf-car .btn,.vf-vin .btn{grid-column:1/-1}
.vf-vin input{grid-column:1/-1}
.vsel{height:54px;border-radius:14px;border:0;padding:0 16px;background:rgba(255,255,255,.08);color:#fff;font-size:16px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.12);appearance:none}
.vsel option{color:#111}
.vsel:disabled{opacity:.45}
.vsel:focus{outline:0;box-shadow:inset 0 0 0 1.5px var(--ac)}
.vf-hint{grid-column:1/-1;font-size:13px;color:rgba(255,255,255,.55)}
.vf-side{display:grid;gap:14px}
.garage,.vf-res{background:rgba(255,255,255,.06);border-radius:20px;padding:20px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)}
.vf-res:empty{display:none}
.gcar{display:flex;align-items:center;gap:14px;margin-top:12px;padding:12px;border-radius:14px;background:rgba(255,255,255,.07)}
.gcar b{display:block;font-size:17px}
.gcar span{font-size:13px;color:rgba(255,255,255,.6)}
.gcar .ico{width:44px;height:44px;border-radius:12px;background:var(--ac);color:var(--aci);display:grid;place-items:center;font-weight:800}
.gcar button{margin-left:auto;font-size:13px;color:rgba(255,255,255,.6);text-decoration:underline}
.vf-res h3{font-size:22px;margin-bottom:6px}
.vf-res ul{list-style:none;margin:14px 0 16px;padding:0;display:grid;gap:8px}
.vf-res li{display:flex;justify-content:space-between;gap:10px;font-size:14px;padding:10px 12px;border-radius:12px;background:rgba(255,255,255,.05);cursor:pointer}
.vf-res li:hover{background:rgba(255,255,255,.1)}
.vf-res li b{white-space:nowrap}
@media (max-width:860px){.vf{grid-template-columns:1fr}.vf-car{grid-template-columns:1fr}}
.card .fit{font-size:12px;font-weight:600;color:var(--ok)}
.card .stockline{font-size:12px;color:var(--mut)}
"""

WIDGET_JS = r"""
(function(){
var CARS=%CARS%,S=window.SHOP,$=function(s){return document.querySelector(s)};
var mk=$('#vfMake'),md=$('#vfModel'),en=$('#vfEng'),go=$('#vfGo');
Object.keys(CARS).forEach(function(m){mk.insertAdjacentHTML('beforeend','<option>'+m+'</option>')});
mk.onchange=function(){md.innerHTML='<option value="">Модель</option>'+(mk.value?Object.keys(CARS[mk.value]).map(function(x){return'<option>'+x+'</option>'}).join(''):'');md.disabled=!mk.value;en.disabled=true;en.innerHTML='<option>Двигатель</option>';go.disabled=true};
md.onchange=function(){en.innerHTML='<option value="">Двигатель</option>'+(md.value?CARS[mk.value][md.value].map(function(x){return'<option>'+x+'</option>'}).join(''):'');en.disabled=!md.value;go.disabled=true};
en.onchange=function(){go.disabled=!en.value};
document.querySelectorAll('[data-vt]').forEach(function(b){b.onclick=function(){document.querySelectorAll('[data-vt]').forEach(function(x){x.setAttribute('aria-selected',x===b)});$('.vf-car').hidden=b.dataset.vt!=='car';$('.vf-vin').hidden=b.dataset.vt!=='vin'}});
var car=null;try{car=JSON.parse(localStorage.getItem('detal-car')||'null')}catch(_){}
function fits(p){return!car||!p.fits||p.fits.split('|').indexOf(car.make+' '+car.model)>=0}
function setCar(c){car=c;try{localStorage.setItem('detal-car',JSON.stringify(c))}catch(_){}drawGarage();result()}
function drawGarage(){var g=$('#garage');if(!car){g.innerHTML='<p class="vf-hint" style="margin-top:12px">Здесь появится ваша машина — подбор будет работать на всём сайте.</p>';return}
 g.innerHTML='<div class="gcar"><div class="ico">'+car.make[0]+'</div><div><b>'+car.make+' '+car.model+'</b><span>'+car.eng+(car.year?' · '+car.year:'')+(car.vin?' · VIN …'+car.vin.slice(-6):'')+'</span></div><button type="button" id="gDel">Убрать</button></div>';
 $('#gDel').onclick=function(){car=null;try{localStorage.removeItem('detal-car')}catch(_){}drawGarage();$('#vfRes').innerHTML='';S.filter(null)}}
function result(){var r=S.products.filter(function(p){return p.fits&&fits(p)});
 $('#vfRes').innerHTML='<h3>'+r.length+' деталей на '+car.make+' '+car.model+'</h3><p class="vf-hint">Проверено по каталогу производителя, '+car.eng+'.</p><ul>'+r.slice(0,5).map(function(p){return'<li data-open="'+p.id+'"><span>'+S.esc(p.n)+'</span><b>'+S.fmt(p.p)+'</b></li>'}).join('')+'</ul><button class="btn wide" type="button" id="vfAll">Все '+r.length+' в каталоге</button>';
 $('#vfAll').onclick=function(){S.filter(function(p){return p.fits&&fits(p)},'Показаны детали для '+car.make+' '+car.model)}}
go.onclick=function(){setCar({make:mk.value,model:md.value,eng:en.value})};
$('#vfVinGo').onclick=function(){var v=$('#vfVin').value.toUpperCase().replace(/\s/g,'');
 if(!/^[A-HJ-NPR-Z0-9]{17}$/.test(v)){S.toast('Проверьте VIN: нужно 17 знаков без I, O и Q');$('#vfVin').focus();return}
 var w=v.slice(0,3),dict={Z94:['Hyundai','Solaris II','1.6 MPI'],XWE:['Kia','Rio IV','1.6 MPI'],XW8:['Volkswagen','Polo VI','1.6 MPI'],XTA:['Lada','Vesta','1.6'],JTN:['Toyota','Camry XV70','2.5'],TMB:['Skoda','Octavia A7','1.4 TSI']},
 c=dict[w]||['Kia','Rio IV','1.6 MPI'],yr=2010+'ABCDEFGHJKLMNPRSTVWXY'.indexOf(v[9])%30;
 setCar({make:c[0],model:c[1],eng:c[2],year:yr>2009&&yr<2027?yr:'',vin:v});S.toast('VIN расшифрован: '+c[0]+' '+c[1])};
drawGarage();if(car)result();
/* подпись совместимости и склада на карточках */
new MutationObserver(function(){document.querySelectorAll('#grid .card:not([data-x])').forEach(function(el){el.dataset.x=1;var p=S.byId[el.dataset.id],b=el.querySelector('.meta');
 if(car&&p.fits){b.insertAdjacentHTML('beforebegin',fits(p)?'<div class="fit">✓ Подходит на '+car.model+'</div>':'<div class="fit" style="color:var(--mut)">Не подходит на '+car.model+'</div>')}
 el.querySelector('.body').insertAdjacentHTML('beforeend','<div class="stockline">'+S.esc((p.stock||'').split(',')[0])+'</div>')})}).observe(document.getElementById('grid'),{childList:true});
})();
"""


def cfg():
    import json
    return {
        "slug": "shops/detal",
        "images": IMG,
        "brand": "ДЕТАЛЬ",
        "logo": "<b>Д</b>ДЕТАЛЬ",
        "title": "ДЕТАЛЬ — автозапчасти с подбором по VIN, Москва",
        "desc": "Автозапчасти для иномарок и Lada: подбор по марке и VIN, оригиналы и проверенные аналоги, 4 склада в Москве, самовывоз через час и доставка по России.",
        "variant": "mega",
        "favLetter": "Д",
        "theme": {"bg": "#f4f4f2", "ink": "#121417", "soft": "#41454c", "mut": "#7c8189", "line": "rgba(18,20,23,.1)", "line2": "rgba(18,20,23,.24)",
                  "card": "#e9e9e6", "ac": "#ff5a1f", "aci": "#fff", "ok": "#1f9d55", "rc": "18px", "rb": "12px", "rs": "28px",
                  "fh": '"Geologica",system-ui,sans-serif', "fb": '"Geologica",system-ui,sans-serif', "fm": '"Geist Mono",ui-monospace,monospace',
                  "hw": "700", "ht": "-.03em", "hc": "none", "emst": "normal", "ar": "1/1", "cardbg": "#fff", "cpad": "16px", "cpadb": "16px"},
        "fonts": [("Geologica", "geologica", [400, 500, 600, 700], "normal"), ("Geist Mono", "geist-mono", [400, 500], "normal")],
        "strip": "Самовывоз через 1 час с <b>4 складов в Москве</b> · доставка по России от 1 дня · возврат 30 дней",
        "nav": [("Каталог", "catalog"), ("Подбор по авто", "feat"), ("Доставка", "why"), ("Вопросы", "faq")],
        "searchPh": "Артикул, VIN или название",
        "hero": {"kicker": "Автозапчасти · 120 000 позиций", "h1": "Нужная деталь — <em>сегодня</em>", "img": "hero",
                 "lead": "Оригиналы и проверенные аналоги для иномарок и Lada. Подбор по VIN за минуту, цены дешевле дилера в среднем на 30%.",
                 "cta": "Подобрать по машине", "ctaTo": "feat", "cta2": "Каталог", "cta2To": "catalog",
                 "stats": [("4 склада", "в Москве"), ("1 час", "до самовывоза"), ("30 дней", "на возврат")],
                 "tiles": [{"k": "Сезон", "t": "Зимние шины со скидкой до 15%", "cat": "wheels", "img": "tires", "a": "Выбрать шины →"},
                           {"k": "ТО за 1 визит", "t": "Масло, фильтры и колодки комплектом", "cat": "oil", "img": "oil", "a": "Собрать ТО →"}]},
        "cats": [{"id": "brakes", "n": "Тормозная система"}, {"id": "oil", "n": "Масла и жидкости"}, {"id": "filters", "n": "Фильтры"},
                 {"id": "wheels", "n": "Шины и диски"}, {"id": "light", "n": "Свет"}, {"id": "suspension", "n": "Подвеска"}, {"id": "engine", "n": "Двигатель и выхлоп"}],
        "facets": {"brand": ("Производитель", ["TRW", "ATE", "Mann", "Bosch", "Kayaba", "Gates", "Nordman", "Liqui", "Osram"]),
                   "kind": ("Тип", ["Оригинал-аналог", "Восстановленный", "Масла", "Шины", "Диски"])},
        "products": PRODUCTS,
        "pageSize": 12,
        "showStars": True,
        "cardSizes": "(max-width:860px) 50vw, 300px",
        "freeFrom": 5000,
        "promo": {"code": "ТО2026", "pct": 7, "hint": "ТО2026 — минус 7% на заказ"},
        "ship": [{"id": "pick", "name": "Самовывоз со склада", "eta": "через 1 час, Каширское ш., 61", "price": 0},
                 {"id": "cour", "name": "Курьер по Москве", "eta": "сегодня или завтра", "price": 390, "free": 5000},
                 {"id": "cdek", "name": "СДЭК по России", "eta": "1–5 дней", "price": 490}],
        "addrNote": "для самовывоза можно не заполнять",
        "slotNote": "Привезём в 3-часовой интервал, курьер позвонит за 30 минут.",
        "doneNote": "Менеджер проверит совместимость по VIN и позвонит в течение 15 минут.",
        "widget": {"nav": "Подбор по авто", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS.replace("%CARS%", json.dumps(CARS, ensure_ascii=False))},
        "usp": [("Подбор по VIN бесплатно", "Сверим деталь с каталогом производителя до оплаты. Не подошла — заберём за наш счёт."),
                ("Оригинал или аналог", "Показываем оба варианта рядом: аналоги только проверенных марок первичной комплектации."),
                ("Самовывоз за час", "4 склада по Москве: Каширка, Алтуфьево, Солнцево и Люберцы. Держим заказ 3 дня."),
                ("Установка рядом", "Партнёрские сервисы у каждого склада: скидка 10% на работы с нашими деталями.")],
        "uspTitle": "Без ошибок с подбором",
        "faq": [("Как понять, что деталь подойдёт?", "Укажите VIN в подборе или в комментарии к заказу — менеджер сверит деталь с каталогом производителя и позвонит до сборки заказа."),
                ("Можно вернуть, если не подошло?", "Да, 30 дней без объяснения причин, если деталь не устанавливали и сохранена упаковка. По браку — в любой момент гарантийного срока."),
                ("Чем аналог хуже оригинала?", "Ничем, если это производитель первичной комплектации: многие детали в коробке с логотипом марки делает тот же завод. Такие аналоги мы и отмечаем."),
                ("Есть оплата для юрлиц?", "Да, по счёту с НДС. Для автосервисов и автопарков — отсрочка платежа и персональные цены от 50 000 ₽ в месяц.")],
        "footBig": "Подберём деталь, пока вы пьёте кофе",
        "contacts": {"addr": "Москва, Каширское ш., 61, склад 3", "hours": "Ежедневно 8:00–22:00"},
        "css": ".v-mega .hero .main{min-height:clamp(420px,42vw,560px)}.logo b{border-radius:10px}",
        "order": ["catalog", "widget", "usp", "faq"],
        "gridTitle": "Запчасти в наличии",
    }
