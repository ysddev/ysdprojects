"""«Пион» — цветочная мастерская: конструктор букета (цветы, размер, упаковка, открытка) и доставка ко времени."""

IMG = {
    "hero": ("1523694576729-dc99e9c0f9b4", 16, 9, "800,1400,2000"),
    "roses": ("1582794543139-8ac9cb0f7b11", 4, 5, "500,900"),
    "pinkwhite": ("1523693916903-027d144a2b7d", 4, 5, "500,900"),
    "wild": ("1763073064881-9bf81eadd3e2", 4, 5, "500,900"),
    "beige": ("1523694576729-dc99e9c0f9b4", 4, 5, "500,900"),
    "lot": ("1508808703020-ef18109db02f", 4, 5, "500,900"),
    "roses2": ("1487530811176-3780de880c2d", 4, 5, "500,900"),
    "vase": ("1776193550326-fb87ffba0442", 4, 5, "500,900"),
    "dried": ("1622658641558-235f26dd270b", 4, 5, "500,900"),
    "red": ("1533616688419-b7a585564566", 4, 5, "500,900"),
    "hold": ("1567696153798-9111f9cd3d0d", 4, 5, "500,900,1300"),
    "bright": ("1782647862359-9feecdd97933", 4, 5, "500,900"),
    "center": ("1561181286-d3fee7d55364", 4, 5, "500,900"),
    "glass": ("1572454591674-2739f30d8c40", 4, 5, "500,900"),
    "wild2": ("1762969217496-32d784e7e557", 4, 5, "500,900"),
    "assorted": ("1457089328109-e5d9bd499191", 4, 5, "500,900"),
}


def P(id, n, cat, p, img, m, d, s, old=None, tag=None, nw=False, size=True):
    x = {"id": id, "n": n, "cat": cat, "p": p, "img": img, "m": m, "d": d, "s": s}
    if size:
        x["opts"] = {"Размер": ["Как на фото", "Побольше (+40%)"]}
    if old:
        x["old"] = old
    if tag:
        x["tag"] = tag
    if nw:
        x["nw"] = 1
    x["stock"] = "Соберём за 1,5 часа · фото букета пришлём до отправки"
    return x


PRODUCTS = [
    P("b1", "Букет «Нежность» из кустовых роз", "bouquets", 4900, "pinkwhite", "21 роза · пудровые оттенки",
      "Кустовые и пионовидные розы в нежной гамме, перевязаны атласной лентой.", [["Высота", "45 см"], ["Цветов", "21"]], tag="Хит"),
    P("b2", "Букет «Полевой»", "bouquets", 3900, "wild", "Сезонные цветы",
      "Ромашки, васильки, гипсофила и злаки — будто только что с луга.", [["Высота", "40 см"]]),
    P("b3", "Букет «Утро» в крафте", "bouquets", 5600, "beige", "Эустома, розы, эвкалипт",
      "Светлый букет в крафтовой бумаге — уместен и маме, и коллеге.", [["Высота", "50 см"]]),
    P("b4", "51 красная роза", "roses", 12900, "roses2", "Эквадор · 60 см",
      "Крупный бутон 6 см, стоят 10–12 дней.", [["Длина стебля", "60 см"]], old=14900),
    P("b5", "Розы пионовидные, 15 шт.", "roses", 6900, "roses", "Сорт Pink O'Hara",
      "Ароматные, раскрываются как пион.", [["Цветов", "15"]], nw=True),
    P("b6", "Композиция в вазе «Лето»", "boxes", 7400, "vase", "С вазой",
      "Яркая композиция — ставите на стол и ничего не делаете.", [["Высота", "35 см"]]),
    P("b7", "Букет из сухоцветов", "dried", 3400, "dried", "Простоит год",
      "Лагурус, лимониум и хлопок в персиковой бумаге.", [["Срок", "до 12 месяцев"]], size=False, tag="Долго стоит"),
    P("b8", "Композиция «Гранат»", "boxes", 5900, "red", "Шляпная коробка",
      "Красные розы и гвоздики в шляпной коробке с влажной флористической губкой.", [["Цветов", "25"]]),
    P("b9", "Букет «Карнавал»", "bouquets", 4500, "bright", "Яркий микс",
      "Герберы, альстромерии и хризантемы — для настроения.", [["Высота", "45 см"]]),
    P("b10", "Пионы в стекле", "boxes", 8900, "center", "Сезонная поставка",
      "Розовые пионы в прозрачной вазе.", [["Цветов", "11"]], nw=True),
    P("b11", "Букет «Пастель» в вазе", "boxes", 6200, "glass", "Розы, гвоздики, эвкалипт",
      "Пастельный микс в низкой вазе.", [["Высота", "30 см"]]),
    P("b12", "Букет «Луг»", "bouquets", 3600, "wild2", "Маленький, но яркий",
      "Комплимент без повода: полевые цветы в бумаге.", [["Высота", "30 см"]], old=4200),
]

WIDGET_HTML = """
<div class="bq">
 <div class="bq-view"><svg viewBox="0 0 400 460" id="bqSvg" aria-hidden="true"><g id="bqF"></g>
  <path id="bqWrap" d="M110 250 L200 440 L290 250 Z" fill="#e9d2c4"/><path d="M110 250 L200 440 L200 250 Z" fill="#000" opacity=".06"/>
  <path d="M170 380 q30 -20 60 0 q-30 18 -60 0z" id="bqBow" fill="#c8506a"/></svg>
  <div class="bq-card" id="bqCardPrev" hidden></div></div>
 <div class="bq-f">
  <div class="kick">Конструктор букета</div>
  <h2 style="margin:12px 0 10px">Соберите <em>свой</em> букет</h2>
  <p class="lead" style="font-size:17px">Выберите цветы, размер и упаковку — флорист соберёт точно так и пришлёт фото до отправки.</p>
  <div class="bq-g"><b>Цветы</b><div class="chips2" id="bqFl"></div></div>
  <div class="bq-g"><b>Размер</b><div class="seg" data-k="size"><button data-v="s">S · 15 цветов</button><button data-v="m" aria-pressed="true">M · 25</button><button data-v="l">L · 41</button></div></div>
  <div class="bq-g"><b>Упаковка</b><div class="seg" data-k="wrap"><button data-v="craft" aria-pressed="true">Крафт</button><button data-v="pink">Пудровая плёнка</button><button data-v="box">Шляпная коробка</button></div></div>
  <div class="bq-g"><b>Открытка</b><input id="bqCard" class="bq-in" maxlength="120" placeholder="Напишем от руки, например: «С днём рождения, мама!»"></div>
  <div class="bq-sum"><div><div class="muted" style="font-size:13px" id="bqWhen"></div><div class="price" id="bqPrice" style="font-size:32px"></div></div><button class="btn" type="button" id="bqAdd">Заказать букет</button></div>
 </div>
</div>"""

WIDGET_CSS = """
#feat .feat{--fbg:#f5e6e0}
.bq{display:grid;grid-template-columns:.9fr 1.1fr;gap:clamp(24px,4vw,64px);align-items:center}
.bq-view{position:relative;background:radial-gradient(80% 70% at 50% 35%,#fff7f3,#f0d9cf);border-radius:220px 220px 24px 24px;aspect-ratio:4/5;display:grid;place-items:center}
#bqSvg{width:84%}
#bqF circle{transition:r .4s,fill .4s}
.bq-card{position:absolute;right:6%;bottom:8%;width:42%;background:#fff;border-radius:6px;padding:12px;font-family:var(--fh);font-style:italic;font-size:16px;line-height:1.3;box-shadow:0 14px 30px -18px rgba(0,0,0,.4);transform:rotate(-4deg)}
.bq-f h2 em{font-style:italic;color:var(--ac)}
.bq-g{margin-top:20px}
.bq-g b{display:block;font-size:13px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:var(--mut);margin-bottom:10px}
.chips2{display:flex;gap:8px;flex-wrap:wrap}
.chips2 button{display:inline-flex;align-items:center;gap:8px;height:42px;padding:0 14px 0 8px;border-radius:999px;background:#fff;font-size:14px;box-shadow:inset 0 0 0 1px var(--line)}
.chips2 button i{width:26px;height:26px;border-radius:50%}
.chips2 button[aria-pressed=true]{box-shadow:inset 0 0 0 2px var(--ink)}
.seg{display:flex;gap:6px;flex-wrap:wrap}
.seg button{height:42px;padding:0 16px;border-radius:999px;font-size:14px;box-shadow:inset 0 0 0 1px var(--line2)}
.seg button[aria-pressed=true]{background:var(--ink);color:#fff;box-shadow:none}
.bq-in{width:100%;height:48px;border-radius:999px;border:0;padding:0 18px;background:#fff;font-size:15px}
.bq-sum{display:flex;justify-content:space-between;align-items:end;gap:16px;margin-top:24px;padding-top:20px;border-top:1px solid var(--line2);flex-wrap:wrap}
@media (max-width:860px){.bq{grid-template-columns:1fr}.bq-view{max-width:420px;margin:0 auto;width:100%}}
"""

WIDGET_JS = r"""
(function(){
var S=window.SHOP,$=function(s){return document.querySelector(s)};
var FL=[['Пионовидные розы','#f2a7b5',190],['Эустома','#e9e0f2',150],['Ранункулюсы','#f6b98d',220],['Гортензия','#b9c8ea',350],['Эвкалипт','#9fb5a2',90],['Ромашки','#fff7e6',70]],sel=[0,1,4];
var SZ={s:15,m:25,l:41},WR={craft:['#d9b58d',0,'Крафт'],pink:['#f2c9cf',300,'Пудровая плёнка'],box:['#2f2a2a',900,'Шляпная коробка']},st={size:'m',wrap:'craft'};
$('#bqFl').innerHTML=FL.map(function(f,i){return'<button type="button" data-f="'+i+'" aria-pressed="'+(sel.indexOf(i)>=0)+'"><i style="background:'+f[1]+'"></i>'+f[0]+'</button>'}).join('');
function price(){var n=SZ[st.size],avg=sel.reduce(function(a,i){return a+FL[i][2]},0)/sel.length;return Math.round((n*avg+WR[st.wrap][1]+500)/100)*100}
function draw(){var n=SZ[st.size],g='',R=st.size==='l'?150:st.size==='m'?125:100,k=0;
 for(var i=0;i<n;i++){var a=i*2.39996,r=Math.sqrt(i/n)*R,x=200+Math.cos(a)*r,y=170+Math.sin(a)*r*.82,f=FL[sel[k++%sel.length]];g+='<circle cx="'+x.toFixed(1)+'" cy="'+y.toFixed(1)+'" r="'+(f[0]==='Эвкалипт'?11:f[0]==='Гортензия'?22:17)+'" fill="'+f[1]+'" stroke="rgba(0,0,0,.08)"/>'}
 $('#bqF').innerHTML=g;$('#bqWrap').setAttribute('fill',WR[st.wrap][0]);$('#bqBow').setAttribute('fill',st.wrap==='box'?'#f2c9cf':'#c8506a');
 $('#bqPrice').textContent=S.fmt(price());var d=new Date(Date.now()+105*60000);$('#bqWhen').textContent='Привезём сегодня к '+d.toLocaleTimeString('ru-RU',{hour:'2-digit',minute:'2-digit'})+' или ко времени';
 var c=$('#bqCard').value.trim(),p=$('#bqCardPrev');p.hidden=!c;p.textContent=c}
$('#bqFl').onclick=function(e){var b=e.target.closest('button');if(!b)return;var i=+b.dataset.f,j=sel.indexOf(i);if(j>=0){if(sel.length>1)sel.splice(j,1)}else sel.push(i);
 this.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',sel.indexOf(+x.dataset.f)>=0)});draw()};
document.querySelectorAll('.bq .seg').forEach(function(g){g.querySelectorAll('button').forEach(function(b){if(!b.hasAttribute('aria-pressed'))b.setAttribute('aria-pressed','false')});
 g.onclick=function(e){var b=e.target.closest('button');if(!b)return;st[g.dataset.k]=b.dataset.v;g.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});draw()}});
$('#bqCard').addEventListener('input',draw);
$('#bqAdd').onclick=function(){var c=$('#bqCard').value.trim();S.add('b1',{'Состав':sel.map(function(i){return FL[i][0].toLowerCase()}).join(', ')+', '+SZ[st.size]+' цветов, '+WR[st.wrap][2].toLowerCase()+(c?', открытка':'')},1,{price:price(),name:'Букет по вашему выбору'})};
draw();
})();
"""


def cfg():
    return {
        "slug": "shops/pion", "images": IMG, "brand": "Пион",
        "logo": '<span style="font-family:var(--fh);font-style:italic;font-weight:400;font-size:28px">Пион</span><span style="font:500 10px/1 var(--fb);letter-spacing:.2em;text-transform:uppercase;color:var(--mut);margin-left:8px">цветы</span>',
        "title": "Пион — авторские букеты с доставкой за 2 часа",
        "desc": "Букеты из свежих сезонных цветов: конструктор букета, открытка от руки, фото перед отправкой и доставка по Москве за 2 часа или к точному времени.",
        "variant": "lookbook", "favLetter": "П",
        "theme": {"bg": "#fbf6f3", "ink": "#3a2a2c", "soft": "#6b5558", "mut": "#a08e8f", "line": "rgba(58,42,44,.1)", "line2": "rgba(58,42,44,.25)",
                  "card": "#f3e7e1", "ac": "#c8506a", "aci": "#fff", "ok": "#3f8a5a", "rc": "18px", "rb": "999px", "rs": "28px",
                  "fh": '"Cormorant Garamond",Georgia,serif', "fe": '"Cormorant Garamond",Georgia,serif', "fb": '"Commissioner",system-ui,sans-serif', "fm": '"Commissioner",system-ui,sans-serif',
                  "hw": "500", "ht": "-.01em", "hc": "none", "lw": "400", "lt": "0", "ar": "4/5", "fot": "#3a2a2c"},
        "fonts": [("Cormorant Garamond", "cormorant-garamond", [400, 500], "italic"), ("Commissioner", "commissioner", [400, 500, 600], "normal")],
        "strip": "Доставка по Москве <b>за 2 часа</b> · фото букета перед отправкой · открытка от руки бесплатно",
        "nav": [("Букеты", "catalog"), ("Собрать свой", "feat"), ("Доставка", "why"), ("Вопросы", "faq")],
        "searchPh": "Розы, пионы, в коробке…",
        "hero": {"kicker": "Цветочная мастерская · Патриаршие", "h1": "Цветы, после которых <em>звонят сказать спасибо</em>", "img": "hero",
                 "lead": "Сезонные букеты от флористов, которые сами ездят на цветочный рынок в 5 утра. Привезём за 2 часа и пришлём фото до отправки.",
                 "cta": "Выбрать букет", "cta2": "Собрать свой", "cta2To": "feat",
                 "stats": [("2 часа", "доставка по Москве"), ("7 дней", "гарантия свежести"), ("фото", "до отправки")]},
        "cats": [{"id": "bouquets", "n": "Букеты"}, {"id": "roses", "n": "Розы"}, {"id": "boxes", "n": "В вазе и коробке"}, {"id": "dried", "n": "Сухоцветы"}],
        "products": PRODUCTS, "pageSize": 8, "showStars": False, "cardSizes": "(max-width:860px) 50vw, 25vw",
        "freeFrom": 5000, "promo": {"code": "ЦВЕТЫ", "pct": 10, "hint": "ЦВЕТЫ — минус 10% на первый заказ"},
        "ship": [{"id": "fast", "name": "Курьер за 2 часа", "eta": "сегодня, с 8 до 23", "price": 490, "free": 5000},
                 {"id": "exact", "name": "К точному времени", "eta": "окно 30 минут", "price": 790},
                 {"id": "pick", "name": "Самовывоз из мастерской", "eta": "Малая Бронная, 20 — через час", "price": 0}],
        "slotNote": "Если получатель не дома — позвоним и привезём повторно бесплатно.",
        "commentPh": "Имя и телефон получателя, сюрприз или нет",
        "doneNote": "Флорист пришлёт фото букета в мессенджер до отправки.",
        "addLabel": "В корзину",
        "widget": {"nav": "Собрать свой", "html": WIDGET_HTML, "css": WIDGET_CSS, "js": WIDGET_JS},
        "usp": [("Фото перед отправкой", "Пришлём фото готового букета — можно попросить поменять."),
                ("7 дней свежести", "Завянет раньше — заменим бесплатно, пришлите фото."),
                ("Открытка от руки", "Подпишем вашим текстом на дизайнерской открытке."),
                ("Ко времени", "Привезём в окно 30 минут — к началу праздника или свидания.")],
        "uspTitle": "Чтобы всё случилось вовремя", "uspKick": "Сервис",
        "faq": [("Можно доставить анонимно?", "Конечно. Курьер не скажет, от кого букет, если вы об этом попросите в комментарии."),
                ("Что если получателя нет дома?", "Позвоним, договоримся о другом времени и привезём повторно бесплатно в пределах МКАД."),
                ("Букет будет как на фото?", "Да, по составу и гамме. Цветы живые, поэтому оттенок может чуть отличаться — мы пришлём фото до отправки."),
                ("Как продлить жизнь букету?", "Подрезайте стебли наискосок раз в 2 дня и меняйте воду. Пакетик подкормки положим в каждый заказ.")],
        "footBig": "Повод не нужен",
        "contacts": {"addr": "Москва, Малая Бронная, 20", "hours": "Ежедневно 8:00–23:00"},
        "order": ["catalog", "widget", "usp", "faq"], "gridTitle": "Букеты сегодня", "gridKick": "Свежая поставка",
        "css": ".hero h1{font-size:clamp(50px,7.4vw,118px);line-height:.92;font-style:italic}.v-lookbook .hero h1 em{color:#ffd3dc}.card .nm{font-family:var(--fh);font-style:italic;font-size:22px}"
               ".price{font-weight:500}",
    }
