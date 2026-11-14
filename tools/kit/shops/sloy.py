"""СЛОЙ — streetwear-бренд: лукбук, дроп с таймером, подбор размера по росту и весу."""

IMG = {
    "hero": ("1523398002811-999ca8dec234", 16, 9, "800,1400,2000"),
    "h1": ("1620799140188-3b2a02fd9a77", 4, 5, "500,900"),
    "h2": ("1564557287817-3785e38ec1f5", 4, 5, "500,900"),
    "h3": ("1578768079052-aa76e52ff62e", 4, 5, "500,900"),
    "h4": ("1508216310976-c518daae0cdc", 4, 5, "500,900"),
    "h5": ("1578470507807-3fc541d5f544", 4, 5, "500,900"),
    "h6": ("1600923678350-bffdd369a828", 4, 5, "500,900"),
    "t1": ("1581655353564-df123a1eb820", 4, 5, "500,900"),
    "t2": ("1583743814966-8936f5b7be1a", 4, 5, "500,900"),
    "t3": ("1759572095384-1a7e646d0d4f", 4, 5, "500,900"),
    "t4": ("1618354691373-d851c5c3a990", 4, 5, "500,900"),
    "l1": ("1611955874253-78c6c3959c41", 4, 5, "500,900,1300"),
    "l2": ("1578854955076-970394ef2512", 4, 5, "500,900,1300"),
    "l3": ("1721637635502-b0abaaa75edb", 4, 5, "500,900,1300"),
    "l4": ("1623596305214-19f21cbf48ee", 4, 5, "500,900"),
    "l5": ("1588117260148-b47818741c74", 4, 5, "500,900"),
    "jeans": ("1739384994765-d44f7af12029", 4, 5, "500,900"),
    "fold": ("1562157873-818bc0726f68", 4, 5, "500,900"),
}
SZ = ["XS", "S", "M", "L", "XL"]
BW = [{"v": "Чёрный", "c": "#141414"}, {"v": "Молочный", "c": "#efe9de"}, {"v": "Графит", "c": "#5a5d61"}]


def P(id, n, cat, p, img, m, d, s, old=None, tag=None, nw=False, cols=None, sizes=SZ):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": s, "opts": {"Размер": sizes}}
    if cols:
        x["opts"] = {"Цвет": cols, "Размер": sizes}
    if old:
        x["old"] = old
    if tag:
        x["tag"] = tag
    if nw:
        x["nw"] = 1
    x["stock"] = "В наличии · отправим сегодня до 18:00"
    return x


PRODUCTS = [
    P("hd1", "Худи «Тишина» oversize", "hoodies", 7900, "h2", "Футер 3-нитка, 480 г/м²",
      "Плотный начёс, двойной капюшон без шнурков, спущенное плечо. Шьём в Иванове малой партией.",
      [["Состав", "80% хлопок, 20% полиэстер"], ["Посадка", "oversize"], ["Рост модели", "184 см, размер M"]], tag="Дроп 07", cols=BW),
    P("hd2", "Худи «Белый шум»", "hoodies", 7900, "h1", "Молочный · вышивка на спине",
      "Молочный оттенок, вышивка гладью на спине и потайной карман для телефона.",
      [["Состав", "80% хлопок, 20% полиэстер"], ["Плотность", "480 г/м²"]], nw=True),
    P("hd3", "Зип-худи «Город»", "hoodies", 8900, "h3", "Двусторонняя молния",
      "Молния YKK на два бегунка, карманы-кенгуру с кнопками.", [["Состав", "100% хлопок"]], cols=BW),
    P("hd4", "Худи «Утро» женское", "hoodies", 7400, "h4", "Укороченное · regular",
      "Укороченная модель с широкой резинкой — носите с джинсами высокой посадки.", [["Длина", "56 см (S)"]], old=8900, sizes=SZ[:4]),
    P("hd5", "Худи «Шум» розовое", "hoodies", 7400, "h6", "Пыльная роза",
      "Мягкий розовый, не выцветает после стирок — краситель Oeko-Tex.", [["Состав", "80% хлопок"]], tag="−17%", old=8900),
    P("hd6", "Худи «Капюшон»", "hoodies", 7900, "h5", "Двойной объёмный капюшон",
      "Капюшон в два слоя держит форму и закрывает от ветра.", [["Состав", "80% хлопок"]], cols=BW),
    P("ts1", "Футболка «База» белая", "tees", 2900, "t1", "Кулирка 220 г/м²",
      "Плотная футболка, не просвечивает и не тянется после стирки. Купите три — четвёртая в подарок.",
      [["Состав", "100% хлопок"], ["Плотность", "220 г/м²"]], tag="3+1"),
    P("ts2", "Футболка «База» чёрная", "tees", 2900, "t2", "Кулирка 220 г/м²",
      "Глубокий чёрный, усадка меньше 2% — проверяли 30 стирками.", [["Состав", "100% хлопок"]]),
    P("ts3", "Футболка «Хлопок» шалфей", "tees", 3200, "t3", "Органический хлопок",
      "Органический хлопок из Узбекистана, мягкий с первого дня.", [["Состав", "100% органический хлопок"]], nw=True),
    P("ts4", "Лонгслив «Кирпич»", "tees", 3900, "t4", "Рибана на манжетах",
      "Длинный рукав с рибаной, удобно под худи и сам по себе.", [["Состав", "95% хлопок, 5% эластан"]]),
    P("pt1", "Джинсы «Широкие» ретро", "pants", 8400, "jeans", "Деним 13 oz",
      "Высокая посадка, широкая штанина и необработанный низ — подрежем по вашей длине бесплатно.",
      [["Состав", "100% хлопок"], ["Посадка", "high-rise, wide"]], sizes=["28", "30", "32", "34", "36"]),
    P("pt2", "Карго «Склад»", "pants", 7600, "l4", "Рипстоп · 6 карманов",
      "Плотный рипстоп, карманы на кнопках и регулировка низа на кулиске.", [["Состав", "100% хлопок рипстоп"]], cols=BW, sizes=SZ),
    P("jk1", "Куртка «Овер» стёганая", "outer", 15900, "l1", "Утеплитель до −15 °C",
      "Стёганая куртка-рубашка: тёплая, но не пуховик. Внутренний карман на молнии.",
      [["Утеплитель", "Thinsulate, 100 г"], ["Температура", "до −15 °C"]], tag="Новинка", nw=True),
    P("jk2", "Ветровка «Огонь»", "outer", 9900, "l2", "Оранжевая · мембрана",
      "Ветро- и влагозащита 5000 мм, светоотражающие детали для вечерних прогулок.", [["Мембрана", "5000/5000"]], old=12400),
]

LOOK = """
<section class="sec" id="look" style="padding-top:0"><div class="wrap">
 <div class="sec-h reveal"><div><div class="kick">Лукбук · осень 2026</div><h2 style="margin-top:14px">Носится<br>слоями</h2></div>
 <p class="lead">Худи под куртку, лонгслив под худи. Всё из одной палитры — сочетается само.</p></div>
 <div class="lk">
  <figure class="reveal"><div class="ph">%L1%</div><figcaption><b>Куртка «Овер»</b> + худи «Тишина» + карго «Склад»<button class="add" type="button" data-open="jk1">Смотреть</button></figcaption></figure>
  <figure class="reveal" style="transition-delay:80ms"><div class="ph">%L3%</div><figcaption><b>Худи «Утро»</b> + джинсы «Широкие»<button class="add" type="button" data-open="hd4">Смотреть</button></figcaption></figure>
  <figure class="reveal" style="transition-delay:160ms"><div class="ph">%L2%</div><figcaption><b>Ветровка «Огонь»</b> + футболка «База»<button class="add" type="button" data-open="jk2">Смотреть</button></figcaption></figure>
 </div></div></section>"""

WIDGET_HTML = """
<div class="drop">
 <div>
  <div class="kick" style="color:var(--ac)">Дроп 08 · «Ноябрь»</div>
  <h2 style="margin:16px 0 18px;color:#fff">Выйдет через</h2>
  <div class="timer" id="timer"><div><b id="tD">00</b><span>дней</span></div><div><b id="tH">00</b><span>часов</span></div><div><b id="tM">00</b><span>минут</span></div><div><b id="tS">00</b><span>секунд</span></div></div>
  <p class="lead" style="color:rgba(255,255,255,.7);margin-top:20px">150 худи и 300 футболок, повторного тиража не будет. Подпишитесь — пришлём ссылку за час до старта.</p>
  <form class="dsub" id="dsub"><input type="tel" inputmode="tel" placeholder="+7 Telegram или WhatsApp" aria-label="Телефон" required><button class="btn" type="submit">Напомнить</button></form>
 </div>
 <div class="fit">
  <div class="kick" style="color:rgba(255,255,255,.55)">Подбор размера</div>
  <h3 style="margin:12px 0 18px;color:#fff;font-size:28px">Какой размер мой?</h3>
  <label>Рост <output id="oH">178 см</output><input type="range" id="fH" min="150" max="200" value="178"></label>
  <label>Вес <output id="oW">72 кг</output><input type="range" id="fW" min="40" max="120" value="72"></label>
  <div class="seg2" id="fFit"><button type="button" data-f="0" aria-pressed="false">В облипку</button><button type="button" data-f="1" aria-pressed="true">Как на фото</button><button type="button" data-f="2" aria-pressed="false">Свободнее</button></div>
  <div class="fres"><span>Ваш размер</span><b id="fRes">M</b><small id="fNote">Длина худи 74 см — до середины бедра</small></div>
 </div>
</div>"""

WIDGET_CSS = """
#feat .feat{--fbg:#0d0d0d;color:#fff;border-radius:0}
.drop{display:grid;grid-template-columns:1.2fr 1fr;gap:clamp(24px,5vw,72px)}
.timer{display:flex;gap:clamp(10px,2vw,22px)}
.timer div{background:rgba(255,255,255,.06);border-radius:14px;padding:16px 10px;min-width:clamp(70px,9vw,120px);text-align:center;box-shadow:inset 0 0 0 1px rgba(255,255,255,.1)}
.timer b{display:block;font-family:var(--fh);font-weight:800;font-size:clamp(40px,6vw,84px);line-height:.9;color:var(--ac);font-variant-numeric:tabular-nums}
.timer span{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.55)}
.dsub{display:flex;gap:8px;margin-top:22px;max-width:480px}
.dsub input{flex:1;height:52px;border-radius:var(--rb);border:0;padding:0 16px;background:rgba(255,255,255,.08);color:#fff;box-shadow:inset 0 0 0 1px rgba(255,255,255,.14)}
.fit{background:rgba(255,255,255,.05);border-radius:20px;padding:clamp(20px,3vw,32px);box-shadow:inset 0 0 0 1px rgba(255,255,255,.1)}
.fit label{display:block;margin-bottom:18px;color:rgba(255,255,255,.75);font-size:14px}
.fit output{float:right;color:#fff;font-weight:600}
.fit input[type=range]{width:100%;margin-top:10px;accent-color:var(--ac)}
.seg2{display:flex;gap:6px;flex-wrap:wrap;margin:6px 0 20px}
.seg2 button{height:40px;padding:0 14px;border-radius:999px;font-size:14px;color:rgba(255,255,255,.75);box-shadow:inset 0 0 0 1px rgba(255,255,255,.2)}
.seg2 button[aria-pressed=true]{background:#fff;color:#0d0d0d}
.fres{display:grid;grid-template-columns:auto 1fr;align-items:center;gap:4px 16px;padding-top:18px;border-top:1px solid rgba(255,255,255,.12)}
.fres span{font-size:13px;color:rgba(255,255,255,.55)}
.fres b{grid-row:span 2;order:-1;font-family:var(--fh);font-weight:800;font-size:72px;line-height:.9;color:var(--ac)}
.fres small{color:rgba(255,255,255,.75);font-size:14px}
@media (max-width:860px){.drop{grid-template-columns:1fr}}
.lk{display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:16px;align-items:end}
.lk figure{margin:0}
.lk .ph{aspect-ratio:3/4;border-radius:0}
.lk figure:first-child .ph{aspect-ratio:4/5}
.lk figcaption{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:14px 0;font-size:14px;color:var(--soft)}
.lk figcaption b{color:var(--ink)}
@media (max-width:860px){.lk{grid-template-columns:1fr}}
"""

WIDGET_JS = r"""
(function(){
var $=function(s){return document.querySelector(s)};
var end=new Date();end.setDate(end.getDate()+((5-end.getDay()+7)%7||7));end.setHours(19,0,0,0);
function tick(){var s=Math.max(0,Math.floor((end-Date.now())/1000)),p=function(n){return String(n).padStart(2,'0')};$('#tD').textContent=p(Math.floor(s/86400));$('#tH').textContent=p(Math.floor(s%86400/3600));$('#tM').textContent=p(Math.floor(s%3600/60));$('#tS').textContent=p(s%60)}
tick();setInterval(tick,1000);
$('#dsub').addEventListener('submit',function(e){e.preventDefault();this.innerHTML='<p style="color:var(--ac);font-weight:600">Готово — напомним за час до старта дропа.</p>'});
var fit=1;
function calc(){var h=+$('#fH').value,w=+$('#fW').value;$('#oH').textContent=h+' см';$('#oW').textContent=w+' кг';
 var bmi=w/Math.pow(h/100,2),i=h<162?0:h<170?1:h<180?2:h<188?3:4;if(bmi>27)i++;if(bmi<19)i--;i+=fit-1;i=Math.max(0,Math.min(4,i));
 var S=['XS','S','M','L','XL'],len=[68,70,72,74,76][i];$('#fRes').textContent=S[i];
 $('#fNote').textContent='Худи '+len+' см в длину — '+(h-len*2>40?'до середины бедра':'чуть ниже бедра')+'. '+(fit===2?'Свободный силуэт, плечо спущено сильнее.':fit===0?'Будет сидеть по фигуре, как базовая кофта.':'Как на модели: 184 см, M.')}
['fH','fW'].forEach(function(id){$('#'+id).addEventListener('input',calc)});
$('#fFit').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;fit=+b.dataset.f;this.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});calc()});
calc();
})();
"""


def cfg():
    from ..common import img
    sz = "(max-width:860px) 100vw, 33vw"
    return {
        "slug": "shops/sloy", "images": IMG, "brand": "СЛОЙ",
        "logo": 'СЛОЙ<span style="color:var(--ac);font-size:30px;line-height:0">.</span>',
        "title": "СЛОЙ — одежда малыми тиражами, дропы раз в месяц",
        "desc": "Худи, футболки и карго из плотного хлопка. Шьём в Иванове малыми партиями, новые дропы раз в месяц, подбор размера по росту и весу.",
        "variant": "lookbook", "favLetter": "С",
        "theme": {"bg": "#f1f0ec", "ink": "#0d0d0d", "soft": "#3c3c3a", "mut": "#86857f", "line": "rgba(13,13,13,.12)", "line2": "rgba(13,13,13,.3)",
                  "card": "#e5e4df", "ac": "#c6ff3d", "aci": "#0d0d0d", "ok": "#2f9e44", "rc": "0px", "rb": "0px", "rs": "0px",
                  "fh": '"Fira Sans Extra Condensed",Impact,sans-serif', "fb": '"Geist",system-ui,sans-serif', "fm": '"Geist Mono",ui-monospace,monospace',
                  "hw": "800", "ht": "-.005em", "hc": "uppercase", "emst": "normal", "lw": "800", "lt": "0", "ar": "3/4"},
        "fonts": [("Fira Sans Extra Condensed", "fira-sans-extra-condensed", [700, 800], "normal"), ("Geist", "geist", [400, 500, 600], "normal"),
                  ("Geist Mono", "geist-mono", [400], "normal")],
        "strip": "Доставка по России <b>бесплатно от 7 000 ₽</b> · примерка перед оплатой · возврат 14 дней",
        "nav": [("Каталог", "catalog"), ("Лукбук", "look"), ("Дроп 08", "feat"), ("Доставка", "why")],
        "searchPh": "Худи, футболка, карго…",
        "hero": {"kicker": "Дроп 07 · уже в продаже", "h1": "Тёплый <em>слой</em><br>на холодный сезон", "img": "hero",
                 "lead": "Худи 480 г/м², карго из рипстопа и куртки до −15 °C. Шьём в Иванове по 150 штук — повторов не делаем.",
                 "cta": "Смотреть дроп", "cta2": "Подобрать размер", "cta2To": "feat",
                 "stats": [("480 г/м²", "плотность худи"), ("150 шт.", "тираж модели"), ("14 дней", "на возврат")]},
        "marquee": ["Дроп 07 в продаже", "Шьём в Иванове", "Худи 480 г/м²", "Примерка перед оплатой", "Тираж 150 штук"],
        "cats": [{"id": "hoodies", "n": "Худи"}, {"id": "tees", "n": "Футболки"}, {"id": "pants", "n": "Штаны"}, {"id": "outer", "n": "Куртки"}],
        "products": PRODUCTS, "pageSize": 8, "showStars": False, "addLabel": "В корзину", "cardSizes": "(max-width:860px) 50vw, 25vw",
        "freeFrom": 7000, "promo": {"code": "СЛОЙ10", "pct": 10, "hint": "СЛОЙ10 — минус 10% на первый заказ"},
        "ship": [{"id": "cour", "name": "Курьер с примеркой", "eta": "Москва и СПб, 1–2 дня", "price": 390, "free": 7000},
                 {"id": "pvz", "name": "Пункт выдачи СДЭК", "eta": "2–6 дней по России", "price": 290, "free": 7000},
                 {"id": "pick", "name": "Самовывоз из шоурума", "eta": "Москва, Хлебозавод №9", "price": 0}],
        "slotNote": "Курьер подождёт 15 минут, пока вы меряете — платите только за то, что оставите.",
        "doneNote": "Ссылку на отслеживание пришлём в Telegram, когда посылка уедет.",
        "widget": {"nav": "Дроп 08", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS},
        "sections": [LOOK.replace("%L1%", img("l1", IMG, sz)).replace("%L2%", img("l2", IMG, sz)).replace("%L3%", img("l3", IMG, sz))],
        "usp": [("Примерка перед оплатой", "Курьер ждёт 15 минут: не подошло — не платите."),
                ("Плотные ткани", "Футер 480 г/м² и кулирка 220 г/м² — не скатываются и не тянутся."),
                ("Малые тиражи", "Каждая модель — не больше 150 штук. На улице двойника не встретите."),
                ("Обмен размера бесплатно", "Привезём другой размер и заберём старый за наш счёт.")],
        "uspTitle": "Почему СЛОЙ", "uspKick": "Сервис",
        "faq": [("Как понять размер?", "Воспользуйтесь подбором выше: учитываем рост, вес и то, как вы любите носить. Если сомневаетесь между двумя — берите оба, лишний вернёте курьеру."),
                ("Будет ли повтор дропа?", "Нет. Тираж каждой модели фиксированный, после него делаем новую. Подпишитесь на напоминание, чтобы не пропустить."),
                ("Как стирать худи?", "Наизнанку при 30 °C, без отбеливателя, сушить на горизонтальной поверхности. Так начёс останется мягким."),
                ("Есть ли у вас магазин?", "Шоурум на Хлебозаводе №9 в Москве, по выходным с 12 до 20. Можно примерить всё и забрать сразу.")],
        "footBig": "Новый дроп каждый месяц",
        "contacts": {"addr": "Москва, Новодмитровская, 1, Хлебозавод №9", "hours": "Сб–Вс 12:00–20:00"},
        "order": ["marquee", "catalog", "extra", "widget", "usp", "faq"],
        "gridTitle": "Дроп 07", "gridKick": "В продаже",
        "css": ".hero h1{font-size:clamp(56px,10vw,168px);line-height:.86}.v-lookbook .hero h1 em{color:var(--ac)}.card .nm{font-weight:600;text-transform:uppercase;font-size:14px;letter-spacing:.04em}.add{border-radius:0}.logo{font-size:30px}",
    }
