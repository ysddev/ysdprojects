"""«Руспирог» (Зеленоград) — первая версия главной для клиента: его логотип, фото, цены и условия доставки
с ruspirog.com; расчёт пирога на гостей и стоимости доставки по зонам, выбор времени доставки."""

B = "https://ruspirog.com/image/"
T = B + "cache/catalog/tovar/"


def U(url, a=1, b=1):
    return ("", a, b, "", url)


IMG = {
    "hero": U(B + "catalog/tovar/pirogisytnye/211021pirogsgovjadinojikapustoj.jpg", 3, 2),
    "sets": U(B + "catalog/tovar/pirogisytnye/211021pirogstreskoj.jpg", 3, 2),
    "sweet": U(B + "catalog/tovar/pirogisladkie/211021pirogvishnjatvorog.jpg", 3, 2),
    "beef": U(T + "pirogisytnye/211021pirogsgovjadinojikapustoj-500x500.jpg"),
    "cod": U(T + "pirogisytnye/211021pirogstreskoj-500x500.jpg"),
    "ham": U(T + "pirogisytnye/211021pirogvetchinasyr-500x500.jpg"),
    "curd": U(T + "pirogisladkie/211021pirogvishnjatvorog-500x500.jpg"),
    "cherry": U(T + "pirogisladkie/211021pirogsvishnej-500x500.jpg"),
    "kul": U(T + "kulebyaka/211021kulebjakastreska-500x500.jpg"),
    "pizza": U(T + "pizza/211021piccaohotnichja-500x500.jpg"),
    "pbeef": U(T + "pirozhki/211021pirojokcgovjadinoy-500x500.jpg"),
    "pcab": U(T + "pirozhki/211021pirojokskapustoj-500x500.jpg"),
    "pcabegg": U(T + "pirozhki/211021pirojokskapustojiyacom-500x500.jpg"),
    "bun": U(T + "bulochki/211021bulochkasvishney-500x500.jpg"),
    "ponion": U(T + "pirozhki/211021pirojoklookcyajcom-500x500.jpg"),
    "rasst": U(T + "pirozhki/211021pirojokstreskoj-500x500.jpg"),
    "pham": U(T + "pirozhki/211021pirojokvetchinaccyrom-500x500.jpg"),
}


def P(id, n, cat, p, img, m, d, tag=None):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": [["Вес", m]], "unit": "шт.", "f": {}}
    if tag:
        x["tag"] = tag
    x["stock"] = "Печём под заказ · доставка ко времени или самовывоз"
    return x


PRODUCTS = [
    P("beef1", "Пирог с говядиной 1 кг", "pies", 1347, "beef", "1 000 г", "Натуральный говяжий фарш, обжаренный с маслом.", "Лидер продаж"),
    P("curd1", "Пирог сладкий с творогом и ягодами 1 кг", "pies", 816, "curd", "1 000 г", "Натуральный творог 9% и ягоды.", "Лидер продаж"),
    P("beef05", "Пирог с говядиной 0,5 кг", "pies", 684, "beef", "500 г", "Натуральный говяжий фарш, обжаренный с маслом."),
    P("cod05", "Пирог с треской 0,5 кг", "pies", 516, "cod", "500 г", "Только натуральное филе трески, без готовых фаршей."),
    P("ham05", "Пирог с ветчиной и сыром 0,5 кг", "pies", 516, "ham", "500 г", "Ветчина из бедра индейки и сыр."),
    P("cherry05", "Пирог с вишней 0,5 кг", "pies", 410, "cherry", "500 г", "Вишня шоковой заморозки.", "Лидер продаж"),
    P("kul", "Кулебяка с рыбой (треска)", "kul", 484, "kul", "470 г", "Только натуральное филе.", "Лидер продаж"),
    P("pizza", "Пицца Охотничья 40 см", "pizza", 895, "pizza", "40 см", "Пицца Охотничья."),
    P("pbeef", "Пирожок с говядиной", "small", 105, "pbeef", "90 г", "Пирожок с говядиной.", "Хит"),
    P("rasst", "Расстегай с треской", "small", 126, "rasst", "120 г", "Расстегай с треской."),
    P("bun", "Булочка с вишней", "small", 84, "bun", "100 г", "Булочка с вишней."),
    P("pham", "Пирожок с ветчиной и сыром", "small", 74, "pham", "90 г", "Начинка запекается вместе с тестом."),
    P("pcabegg", "Пирожок с капустой и яйцом", "small", 68, "pcabegg", "90 г", "Пирожок с капустой и яйцом."),
    P("ponion", "Пирожок с луком и яйцом", "small", 68, "ponion", "90 г", "Зелёный лук с яйцом."),
    P("pcab", "Пирожок с капустой", "small", 61, "pcab", "90 г", "Пирожок с капустой."),
]

WIDGET_HTML = """
<div class="rp">
 <div class="rp-c">
  <div class="kick">Пирог на компанию</div>
  <h2 style="margin:12px 0 8px">Сколько пирога <em>заказать</em>?</h2>
  <p class="muted" style="font-size:15px">Считаем по 300 г на гостя. Вес пирогов честный: 0,5 · 1 · 1,5 · 2 кг.</p>
  <div class="rp-row"><span>Гостей за столом</span><b id="rpN">6</b></div>
  <input type="range" id="rpG" min="2" max="24" value="6" aria-label="Число гостей">
  <div class="rp-res"><div><span class="muted">Нужно примерно</span><b id="rpKg"></b></div><div><span class="muted">Удобно взять</span><b id="rpSet"></b></div></div>
  <button class="btn" type="button" id="rpGo">Выбрать пироги</button>
 </div>
 <div class="rp-c alt">
  <div class="kick">Доставка</div>
  <h2 style="margin:12px 0 8px">Стоимость <em>по зонам</em></h2>
  <p class="muted" style="font-size:15px">В рабочей версии зона определится сама по адресу на карте.</p>
  <div class="rp-seg" id="rpZ"><button type="button" data-z="0" aria-pressed="true">до 10 км</button><button type="button" data-z="1" aria-pressed="false">10–15 км</button><button type="button" data-z="2" aria-pressed="false">15–30 км</button><button type="button" data-z="3" aria-pressed="false">дальше 30 км</button></div>
  <div class="rp-row"><span>Сумма заказа</span><b id="rpS"></b></div>
  <input type="range" id="rpSum" min="300" max="4000" step="50" value="1200" aria-label="Сумма заказа">
  <div class="rp-res"><div><span class="muted">Доставка</span><b id="rpD"></b></div><div><span class="muted" id="rpHintL"></span><b id="rpHint"></b></div></div>
 </div>
</div>"""

WIDGET_CSS = """
.rp{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.rp-c{background:var(--card);border-radius:var(--rs);padding:clamp(22px,3vw,40px);display:flex;flex-direction:column;gap:12px;min-width:0}
.rp-c.alt{background:#2a1a12;color:#fff7ea}
.rp-c.alt .muted{color:rgba(255,247,234,.66)}.rp-c.alt .kick{color:#ffd23c}
.rp-c h2{font-size:clamp(28px,3.4vw,44px)}
.rp-c h2 em{font-style:italic;color:var(--ac)}.rp-c.alt h2 em{color:#ffd23c}
.rp-row{display:flex;justify-content:space-between;align-items:baseline;margin-top:8px;font-size:15px}
.rp-row b{font-family:var(--fh);font-size:30px;font-weight:700;font-variant-numeric:tabular-nums}
.rp input[type=range]{width:100%;accent-color:var(--ac);height:28px}
.rp-c.alt input[type=range]{accent-color:#ffd23c}
.rp-res{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:6px 0 8px}
.rp-res div{background:rgba(255,255,255,.7);border-radius:14px;padding:14px;min-width:0}
.rp-c.alt .rp-res div{background:rgba(255,255,255,.08)}
.rp-res span{display:block;font-size:12.5px;min-height:16px}
.rp-res b{display:block;font-size:18px;line-height:1.25;margin-top:4px}
.rp-seg{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
.rp-seg button{height:40px;padding:0 14px;border-radius:999px;font-size:14px;color:#fff7ea;box-shadow:inset 0 0 0 1px rgba(255,247,234,.35)}
.rp-seg button[aria-pressed=true]{background:#ffd23c;color:#2a1a12;box-shadow:none;font-weight:600}
.rp .btn{align-self:flex-start;margin-top:auto}
@media (max-width:860px){.rp{grid-template-columns:1fr}}
"""

WIDGET_JS = r"""
(function(){
var S=window.SHOP,$=function(s){return document.querySelector(s)};
function pies(kg){var out=[],left=kg;[2,1.5,1,0.5].forEach(function(w){var n=Math.floor((left+1e-9)/w);if(w===2&&n>3)n=3;if(n>0){out.push(n+' × '+String(w).replace('.',',')+' кг');left-=n*w}});return out.join(' + ')}
function guests(){var n=+$('#rpG').value,kg=Math.max(0.5,Math.ceil(n*0.3*2)/2);$('#rpN').textContent=n;$('#rpKg').textContent=String(kg).replace('.',',')+' кг';$('#rpSet').textContent=pies(kg)}
var zone=0;
function ship(){var sum=+$('#rpSum').value,d,h='',hl='';$('#rpS').textContent=S.fmt(sum);
 if(zone===0){d=sum>=1500?'Бесплатно':S.fmt(350);if(sum<1500){hl='До бесплатной';h='ещё '+S.fmt(1500-sum)}else{hl='Порог';h='от 1 500 ₽ пройден'}}
 else if(zone===1){d=S.fmt(600);hl='Сумма заказа';h='не влияет'}
 else if(zone===2){d=S.fmt(900);hl='Сумма заказа';h='не влияет'}
 else{d='Самовывоз';hl='Дальше 30 км';h='не возим'}
 $('#rpD').textContent=d;$('#rpHintL').textContent=hl;$('#rpHint').textContent=h}
$('#rpG').addEventListener('input',guests);$('#rpSum').addEventListener('input',ship);
$('#rpZ').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;zone=+b.dataset.z;this.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});ship()});
$('#rpGo').addEventListener('click',function(){S.setCat('pies');document.getElementById('catalog').scrollIntoView({behavior:'smooth'})});
guests();ship();
})();
"""


def cfg():
    return {
        "slug": "clients/ruspirog", "images": IMG, "brand": "Руспирог",
        "logo": '<img src="' + B + 'catalog/logo/ruspirog_logo_very_small.jpg" alt="Руспирог" width="388" height="143" style="height:46px;width:auto;display:block">',
        "title": "Руспирог — пироги с доставкой ко времени, Зеленоград",
        "desc": "Русские и сладкие пироги честного веса, кулебяки, пирожки и пицца. Доставка по Зеленограду ко времени и самовывоз из кафе-пекарни.",
        "variant": "mega", "favLetter": "Р",
        "theme": {"bg": "#ffffff", "ink": "#2a1a12", "soft": "#5c463a", "mut": "#9a8474", "line": "rgba(42,26,18,.1)", "line2": "rgba(42,26,18,.26)",
                  "card": "#fbf3e2", "ac": "#d7092f", "aci": "#fff", "ac2": "#ffd23c", "ok": "#2f8a4c", "rc": "18px", "rb": "12px", "rs": "26px",
                  "fh": '"Literata",Georgia,serif', "fe": '"Literata",Georgia,serif', "fb": '"Golos Text",system-ui,sans-serif', "fm": '"Golos Text",system-ui,sans-serif',
                  "hw": "700", "ht": "-.02em", "hc": "none", "lw": "700", "lt": "0", "ar": "3/2", "cardbg": "#fbf3e2", "cpad": "14px", "cpadb": "16px", "rl": "8px"},
        "fonts": [("Literata", "literata", [700], "normal"), ("Literata", "literata", [700], "italic"), ("Golos Text", "golos-text", [400, 500, 600], "normal")],
        "strip": "Доставка <b>бесплатно от 1 500 ₽</b> в пределах 10 км · постное меню в любой пост · скидка 10% в день рождения",
        "nav": [("Меню", "catalog"), ("Рассчитать", "feat"), ("Доставка", "why"), ("Вопросы", "faq")],
        "searchPh": "Пирог с вишней, кулебяка, пирожки…",
        "hero": {"kicker": "Сеть пекарен · Зеленоград", "h1": "Пироги честного веса <em>ко времени</em>", "img": "hero",
                 "lead": "Сытные и сладкие пироги, кулебяки, пирожки и пицца. Выберите день и получасовое окно доставки или заберите заказ в кафе-пекарне.",
                 "cta": "Выбрать пироги", "ctaTo": "catalog", "cta2": "Рассчитать на гостей", "cta2To": "feat",
                 "stats": [("0,5–2 кг", "честный вес пирога"), ("30 минут", "окно доставки"), ("от 1 500 ₽", "доставка бесплатно")],
                 "tiles": [{"k": "Сеты", "t": "5 пирогов по 1 кг или по 0,5 кг", "cat": "pies", "img": "sets", "a": "К пирогам →"},
                           {"k": "Постное меню", "t": "Напишите «пост» в комментарии к заказу", "cat": "pies", "img": "sweet", "a": "Выбрать →"}]},
        "cats": [{"id": "pies", "n": "Пироги"}, {"id": "kul", "n": "Кулебяки"}, {"id": "small", "n": "Пирожки и булочки"}, {"id": "pizza", "n": "Пицца"}],
        "products": PRODUCTS, "pageSize": 15, "showStars": False, "cardSizes": "(max-width:860px) 50vw, 300px",
        "freeFrom": 0, "promo": {"code": "ИМЕНИННИК", "pct": 10, "hint": "ИМЕНИННИК — минус 10% в день рождения"},
        "ship": [{"id": "z1", "name": "Курьер, до 10 км от пекарни", "eta": "ко времени, окно 30 минут", "price": 350, "free": 1500},
                 {"id": "z2", "name": "Курьер, 10–15 км", "eta": "ко времени, окно 30 минут", "price": 600},
                 {"id": "z3", "name": "Курьер, 15–30 км", "eta": "ко времени, окно 30 минут", "price": 900},
                 {"id": "pick", "name": "Самовывоз из кафе-пекарни", "eta": "Зеленоград, к выбранному времени", "price": 0}],
        "addrNote": "улица, дом, корпус, подъезд",
        "slotNote": "Заказ уходит на производство к выбранному времени. Если окно занято, сайт предложит соседнее.",
        "commentPh": "Постное меню, домофон, пожелания к заказу",
        "doneNote": "Заказ передан на производство. За час до доставки придёт напоминание.",
        "addLabel": "В корзину",
        "widget": {"nav": "Рассчитать", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS},
        "usp": [("Честный вес", "Вес пирога привычный: 0,5, 1, 1,5 и 2 кг. Сколько заказали, столько и привезём."),
                ("Ко времени", "Выбираете день и получасовое окно. Заказ на завтра не теряется и сразу виден производству."),
                ("Постное меню", "В любой православный пост печём постные пироги и пирожки, достаточно написать в комментарии."),
                ("10% в день рождения", "Промокод «именинник» действует за день до, в день и на следующий день после праздника.")],
        "uspTitle": "Как мы работаем", "uspKick": "Сервис",
        "faq": [("Сколько стоит доставка?", "До 10 км от пекарни: бесплатно при заказе от 1 500 ₽, иначе 350 ₽. От 10 до 15 км: 600 ₽. От 15 до 30 км: 900 ₽. Дальше 30 км не возим, можно забрать заказ самовывозом."),
                ("Сколько пирога брать на компанию?", "Примерно 300 г на человека. На шестерых хватит двух килограммов: например, сытный и сладкий пирог по 1 кг."),
                ("Как заказать постные пироги?", "Напишите в комментарии к заказу «пост» или «постная продукция» до начала приготовления."),
                ("Можно заказать на завтра или к празднику?", "Да. Выберите день и время при оформлении: заказ сразу попадёт в план производства на этот день.")],
        "footBig": "Пироги к вашему столу",
        "contacts": {"addr": "Зеленоград, кафе-пекарня «Руспирог»", "hours": "Заказы на сайте и по телефону", "phone": "+7 (495) 966-12-45"},
        "order": ["catalog", "widget", "usp", "faq"], "gridTitle": "Меню", "gridKick": "Печём под заказ",
        "css": ".hero h1{font-size:clamp(40px,5.4vw,84px);line-height:.98}.v-mega .hero h1 em{color:#ffd23c;font-style:italic}.strip b{color:#ffd23c}"
               ".badge{background:#ffd23c;color:#2a1a12}.card .nm{font-weight:600}.v-mega .hero .tile{background:#2a1a12;color:#fff7ea}"
               ".top .bar{height:76px}h1,h2,h3{hyphens:manual;-webkit-hyphens:manual}.rp-c h2{font-size:clamp(26px,2.8vw,38px)}"
               "@media (max-width:560px){.hero h1{font-size:38px}}"
               ".line .ph{aspect-ratio:3/2;width:96px}.pv .gal{min-height:0;aspect-ratio:3/2;align-self:start}"
               "@media (max-width:860px){.pv .gal{min-height:0;aspect-ratio:3/2}}",
    }
