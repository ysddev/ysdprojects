"""«Гофра 52» — производство гофрокоробов и упаковки с печатью в Нижнем Новгороде: калькулятор тиража с живым
превью коробки по размерам, сроки производства, образцы."""

IMAGES = {
    "stack": ("1624137527136-66e631bdaa0e", 4, 5, "700,1100"),
    "open": ("1700165644892-3dd6b67b25bc", 3, 2, "700,1100"),
    "box": ("1577705998148-6da4f3963bc8", 3, 2, "600,1000"),
    "line": ("1701328778019-e95dedbf5346", 16, 9, "800,1400"),
    "worker": ("1589792923962-537704632910", 4, 5, "600,1000"),
    "mach": ("1598299803204-b73796f43289", 3, 2, "600,1000"),
    "white": ("1573376670774-4427757f7963", 3, 2, "600,1000"),
}

CALC = r"""
<div class="gc rv">
 <div class="panel gq">
  <div class="q"><b>Тип</b><div class="chips" id="gT"></div></div>
  <div class="dims">
   <div class="rng"><div class="rh"><span>Длина</span><b id="gLv"></b></div><input type="range" id="gL" min="100" max="800" step="10" value="400"></div>
   <div class="rng"><div class="rh"><span>Ширина</span><b id="gWv"></b></div><input type="range" id="gW" min="80" max="600" step="10" value="300"></div>
   <div class="rng"><div class="rh"><span>Высота</span><b id="gHv"></b></div><input type="range" id="gH" min="50" max="600" step="10" value="200"></div>
  </div>
  <div class="q"><b>Картон</b><div class="chips" id="gM"></div></div>
  <div class="q"><b>Печать</b><div class="chips" id="gP"></div></div>
  <div class="q rng"><div class="rh"><span>Тираж</span><b id="gQv"></b></div><input type="range" id="gQ" min="0" max="7" step="1" value="3"></div>
 </div>
 <div class="panel gr">
  <div class="pv"><svg viewBox="0 0 300 230" id="gSvg"></svg></div>
  <div class="gl"><span>Цена за штуку</span><b id="gPc"></b></div>
  <div class="gl"><span>Тираж</span><b id="gSum"></b></div>
  <div class="gl"><span>Готовность</span><b id="gDays"></b></div>
  <p class="gn" id="gNote"></p>
  <a class="btn" href="#lead" id="gGo">Заказать образец</a>
 </div>
</div>
"""

CSS = r"""
.hero h1{text-transform:uppercase;letter-spacing:-.01em;line-height:.95}
.hero h1 em{font-style:normal;color:var(--ac)}
.kick{font-weight:700}
.gc{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:clamp(14px,2vw,22px);align-items:start}
.gq{display:grid;gap:24px}.gq .q{display:grid;gap:12px}.gq .q>b{font-weight:700;text-transform:uppercase;font-size:14px;letter-spacing:.06em}
.dims{display:grid;gap:16px}
.gr{position:sticky;top:90px;display:grid;gap:12px;background:#24201b;color:#f3ead9;box-shadow:none}
.gr .pv{background:#2f2a24;border-radius:14px;padding:10px}
.gl{display:flex;justify-content:space-between;align-items:baseline;gap:12px;padding:10px 0;border-bottom:1px solid rgba(243,234,217,.14)}
.gl span{color:rgba(243,234,217,.7)}.gl b{font:700 clamp(22px,2.4vw,30px) var(--fh);text-transform:uppercase}
.gn{font-size:13.5px;color:rgba(243,234,217,.7);min-height:2.4em}
.gr .btn{width:100%}
.facts{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1px;background:var(--line2);border-radius:var(--rc);overflow:hidden}
.facts div{background:var(--bg);padding:22px}.facts b{display:block;font:700 clamp(34px,3.6vw,52px)/1 var(--fh);color:var(--ac)}.facts span{display:block;margin-top:8px;color:var(--soft);font-size:14.5px}
@media (max-width:860px){.gc{grid-template-columns:1fr}.gr{position:static}.facts{grid-template-columns:1fr 1fr}}
"""

JS = r"""
(function(){var $=function(s){return document.getElementById(s)};
var T=[['four','Четырёхклапанный',1],['lid','Крышка-дно',1.45],['tray','Лоток',.78],['mail','Почтовый самосборный',1.22]];
var M=[['t23','Т-23 (трёхслойный)',1],['t24','Т-24 бурый',1.08],['p32','П-32 (пятислойный)',1.62],['white','Белый мелованный',1.35]];
var P=[['none','Без печати',0,0],['1c','1 цвет',1.6,2],['2c','2 цвета',2.6,3],['full','Полноцвет',5.4,4]];
var Q=[100,300,500,1000,3000,5000,10000,30000];
var t='four',m='t23',pr='1c';
function chips(id,arr,cur){$(id).innerHTML=arr.map(function(x){return'<button type="button" data-v="'+x[0]+'" class="'+(x[0]==cur?'on':'')+'">'+x[1]+'</button>'}).join('')}
function bind(id,set){$(id).addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;set(b.dataset.v);[].forEach.call(this.children,function(x){x.classList.toggle('on',x===b)});run()})}
chips('gT',T,t);chips('gM',M,m);chips('gP',P,pr);bind('gT',function(v){t=v});bind('gM',function(v){m=v});bind('gP',function(v){pr=v});
['gL','gW','gH','gQ'].forEach(function(id){$(id).addEventListener('input',run)});
function get(a,k){return a.filter(function(x){return x[0]==k})[0]}
function box(L,W,H){var s=Math.min(230/(L+W*.6),170/(H+W*.33)),l=L*s,w=W*s*.6,h=H*s,x0=150-(l+w)/2,y0=(222-h-w*.55)/2;var tc=get(M,m)[0]=='white'?'#f4f1ea':'#c49a63',sc=get(M,m)[0]=='white'?'#ddd8cc':'#a87f4c',fc=get(M,m)[0]=='white'?'#e9e4d8':'#b88b55';
 var front='M'+x0+' '+(y0+w*.55)+' h'+l+' v'+h+' h-'+l+'z',side='M'+(x0+l)+' '+(y0+w*.55)+' l'+w+' -'+(w*.55)+' v'+h+' l-'+w+' '+(w*.55)+'z',top='M'+x0+' '+(y0+w*.55)+' l'+w+' -'+(w*.55)+' h'+l+' l-'+w+' '+(w*.55)+'z';
 var print=pr=='none'?'':'<text x="'+(x0+l/2)+'" y="'+(y0+w*.55+h/2+6)+'" text-anchor="middle" font-family="Sofia Sans Condensed" font-weight="800" font-size="'+Math.max(10,Math.min(26,l/6))+'" fill="'+(pr=='full'?'#e8412c':'#1f1b17')+'">ВАШ ЛОГОТИП</text>';
 return'<path d="'+top+'" fill="'+tc+'"/><path d="'+side+'" fill="'+sc+'"/><path d="'+front+'" fill="'+fc+'"/>'+(t=='four'||t=='mail'?'<path d="M'+(x0+w/2)+' '+(y0+w*.28)+' h'+l+'" stroke="#7a5a33" stroke-width="1" opacity=".6"/>':'')+(t=='lid'?'<path d="M'+x0+' '+(y0+w*.55+h*.3)+' h'+l+' l'+w+' -'+(w*.55)+'" fill="none" stroke="#7a5a33" stroke-width="1.2"/>':'')+print
  +'<text x="'+(x0+l/2)+'" y="'+(y0+w*.55+h+16)+'" text-anchor="middle" font-size="11" fill="#cdbfa7" font-family="Ubuntu">'+L+' мм</text><text x="'+(x0-8)+'" y="'+(y0+w*.55+h/2)+'" text-anchor="end" font-size="11" fill="#cdbfa7" font-family="Ubuntu">'+H+'</text>'}
function run(){var L=+$('gL').value,W=+$('gW').value,H=+$('gH').value,q=Q[+$('gQ').value];$('gLv').textContent=L+' мм';$('gWv').textContent=W+' мм';$('gHv').textContent=H+' мм';$('gQv').textContent=q.toLocaleString('ru-RU')+' шт';
 var area=(2*(L+W)+50)*(W+H)/1e6;var k=get(T,t)[2]*get(M,m)[2];var p=get(P,pr);var base=area*31*k+p[2]*Math.max(1,area*4);var disc=q>=30000?.58:q>=10000?.64:q>=3000?.72:q>=1000?.84:q>=500?.93:1;
 var setup=pr=='none'?0:(p[3]*2900+(q<1000?1900:0));var pc=base*disc+setup/q;pc=Math.max(pc,area*12);var days=(q<=1000?3:q<=5000?5:q<=10000?7:10)+(pr=='full'?2:pr=='none'?0:1);
 $('gPc').textContent=(Math.round(pc*100)/100).toLocaleString('ru-RU',{minimumFractionDigits:2,maximumFractionDigits:2})+' ₽';$('gSum').textContent=rub(Math.round(pc*q/10)*10);
 $('gDays').textContent=days+' '+plural(days,'рабочий день','рабочих дня','рабочих дней');
 $('gNote').textContent=(setup?'Включены печатные формы '+rub(p[3]*2900)+' — при повторном заказе их не платите. ':'')+(q<500?'До 500 шт выгоднее взять стандартный размер со склада.':'Тираж больше '+(q>=10000?'10 тысяч':'1 000')+' — скидка уже учтена.');
 $('gSvg').innerHTML=box(L,W,H);$('gGo').dataset.v=get(T,t)[1]+' '+L+'×'+W+'×'+H+', '+get(M,m)[1]+', '+p[1]+', '+q+' шт — '+$('gSum').textContent}
$('gGo').addEventListener('click',function(){var a=document.querySelector('#lead textarea');if(a)a.value='Расчёт с сайта: '+this.dataset.v});run()})();
"""

FACTS = ('<div class="facts rv">' + "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in [
    ("3 дня", "минимальный срок на тираж до 1 000 шт"), ("от 100 шт", "делаем малые тиражи для интернет-магазинов"),
    ("2 640 м²", "собственный цех и склад в Сормове"), ("7 линий", "вырубка, печать, склейка, ламинация")]) + "</div>")


def cfg() -> dict:
    return {
        "slug": "gofra", "brand": "Гофра 52", "legal": "ООО «Гофра 52», Нижний Новгород", "favLetter": "Г",
        "logo": '<svg viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#e8412c"/><path d="M6 11l10-5 10 5v11l-10 5-10-5z" fill="none" stroke="#fff" stroke-width="2"/><path d="M6 11l10 5 10-5M16 16v11" fill="none" stroke="#fff" stroke-width="2"/></svg>',
        "title": "Гофра 52 — гофрокоробы и упаковка с печатью от 100 штук, Нижний Новгород",
        "desc": "Производство гофрокоробов, лотков и почтовых коробок с печатью от 100 штук. Калькулятор цены по размерам, "
                "тираж за 3–10 рабочих дней, доставка по России.",
        "theme": {"bg": "#f4efe6", "ink": "#1f1b17", "soft": "#544b41", "mut": "#8f8476", "line": "#e2d8c8", "line2": "#cfc1aa",
                  "card": "#fbf8f2", "alt": "#ebe2d2", "ac": "#e8412c", "aci": "#ffffff", "fh": '"Sofia Sans Condensed",sans-serif',
                  "fb": "Ubuntu,sans-serif", "hw": "800", "ht": "-.005em", "dk": "#24201b", "dki": "#f3ead9", "rc": "10px", "rb": "8px",
                  "h1s": "clamp(48px,7vw,104px)"},
        "fonts": [("Sofia Sans Condensed", "sofia-sans-condensed", [700, 800], "normal"), ("Ubuntu", "ubuntu", [400, 500, 700], "normal")],
        "images": IMAGES,
        "phone": ("+78310000000", "+7 831 000-00-00"),
        "mail": "zakaz@gofra.ysdprojects.space",
        "nav": [("calc", "Калькулятор"), ("types", "Виды упаковки"), ("prod", "Производство"), ("faq", "Вопросы")],
        "topCta": "Рассчитать тираж",
        "hero": {"kicker": "Производство упаковки · Нижний Новгород", "h1": "Коробки с вашим логотипом <em>от 100 штук</em> за 3 дня",
                 "lead": "Гофрокоробы, лотки и почтовые коробки по вашим размерам. Сами режем, печатаем и клеим — без посредников и "
                         "наценки за маленький тираж.",
                 "cta": "Рассчитать цену", "go": "calc", "go2": ("types", "Виды упаковки"),
                 "points": ["Бесплатный образец за 2 дня", "Доставка по России", "Работаем с НДС"],
                 "img": "stack", "alt": "Гофрокоробы", "ar": "4/5",
                 "tag": "<b>9,57 ₽ за коробку</b>четырёхклапанный 300×200×150 без печати, тираж 1 000"},
        "sections": [
            {"type": "html", "id": "calc", "kick": "Калькулятор", "h2": "Задайте размер — коробка соберётся на экране", "alt": True,
             "lead": "Цена с печатными формами и скидкой за тираж. Менеджер подтвердит её в течение часа.", "html": CALC},
            {"type": "cards", "id": "types", "kick": "Виды упаковки", "h2": "Пять видов на все задачи", "cols": 3,
             "items": [{"img": "box", "t": "Четырёхклапанный", "d": "Классика для склада и переездов. Выдерживает до 30 кг.", "price": "от 9,57 ₽", "unit": "за штуку"},
                       {"img": "white", "t": "Самосборный почтовый", "d": "Для интернет-магазинов: собирается за 5 секунд без скотча.", "price": "от 21,40 ₽", "unit": "за штуку"},
                       {"img": "open", "t": "Лотки и ящики", "d": "Для овощей, выпечки и витрин. Перфорация под ручки.", "price": "от 11,70 ₽", "unit": "за штуку"},
                       {"t": "Крышка-дно", "d": "Подарочная упаковка: обувь, наборы, сувениры. Ламинация и тиснение.", "list": ["мелованный картон", "печать до 4 цветов"], "price": "от 38,50 ₽", "unit": "за комплект"},
                       {"t": "Ложементы", "d": "Вставки, которые держат товар внутри коробки и не дают ему биться.", "list": ["гофрокартон или пенополиэтилен", "под ваш товар"], "price": "от 6,20 ₽", "unit": "за штуку"},
                       {"t": "Печать на готовой", "d": "Нанесём логотип на коробки со склада — если размер стандартный.", "list": ["1–2 цвета", "от 100 штук"], "price": "от 4,80 ₽", "unit": "за оттиск"}]},
            {"type": "html", "id": "prod", "kick": "Производство", "h2": "Свой цех — поэтому и 3 дня", "dark": True,
             "html": FACTS.replace('class="facts rv"', 'class="facts rv" style="--bg:#2f2a24"')},
            {"type": "gallery", "id": "gal", "kick": "Цех", "h2": "Как делаем вашу упаковку",
             "items": [{"img": "line", "span": 8, "ar": "16/9", "alt": "Линия производства"}, {"img": "worker", "span": 4, "ar": "4/5", "alt": "Склад готовой продукции"},
                       {"img": "mach", "span": 12, "ar": "21/9", "alt": "Оператор станка"}]},
            {"type": "steps", "id": "how", "kick": "Заказ", "h2": "От расчёта до отгрузки", "alt": True,
             "items": [("Расчёт", "Подтверждаем цену по калькулятору или по вашему ТЗ.", "1 час"),
                       ("Образец", "Делаем коробку-образец без печати и отправляем курьером.", "2 дня, бесплатно"),
                       ("Макет", "Дизайнер готовит развёртку с вашим логотипом.", "1 день"),
                       ("Тираж", "Производство и отгрузка: самовывоз или доставка.", "3–10 рабочих дней")]},
            {"type": "faq", "id": "faq", "kick": "Вопросы", "h2": "Что спрашивают закупщики",
             "items": [("Какой минимальный тираж?", "100 штук для коробок без печати и с печатью в 1 цвет. Для полноцвета — от 300."),
                       ("Можно ли без своего макета?", "Да, дизайнер сделает развёртку с логотипом бесплатно при заказе от 1 000 штук."),
                       ("Как доставляете?", "По Нижнему — своя машина, по России — транспортные компании до склада или до двери."),
                       ("Работаете с маркетплейсами?", "Да, делаем коробки под требования складов маркетплейсов и маркировку.")]},
        ],
        "contact": {"kick": "Заявка", "h2": "Пришлём расчёт и бесплатный образец",
                    "lead": "Менеджер свяжется в течение часа в рабочее время и уточнит детали.",
                    "rows": [("Производство", "Нижний Новгород, Сормовское шоссе, 21"), ("Телефон", "+7 831 000-00-00"), ("Часы", "Пн–пт 8:00–18:00, отгрузка до 20:00")]},
        "form": {"fields": [("name", "Имя", "text", "", True), ("phone", "Телефон", "tel", "+7", True),
                            ("company", "Компания", "text", ""), ("inn", "ИНН (для счёта)", "text", ""),
                            ("msg", "Что нужно упаковать", "textarea", "Размеры, тираж, нужна ли печать")],
                 "ok": "Спасибо! Менеджер позвонит в течение часа и подтвердит расчёт.", "btn": "Получить расчёт"},
        "css": CSS, "js": JS,
    }
