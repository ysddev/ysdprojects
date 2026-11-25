"""«Ворс» — карточки маркетплейса для худи оверсайз: обложка и пять слайдов, четыре цвета, подбор размера по росту и груди."""

from .tish import CSS as MP_CSS

FH, FB = "Dela Gothic One", "Manrope"
INK, MUT = "#1c1a17", "#5f5a52"


def hoodie(x, y, s=1.0):
    """Худи спереди: корпус и рукава --c1, капюшон и резинки --c2."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M190 150 L70 215 L22 520 L104 540 L140 330 L140 690 H460 L460 330 L496 540 L578 520 L530 215 L410 150 Z" style="fill:var(--c1)"/>'
            f'<path d="M205 160 C190 40 410 40 395 160 C360 215 240 215 205 160 Z" style="fill:var(--c2)"/>'
            f'<path d="M232 165 C250 196 350 196 368 165" fill="none" stroke="#000" stroke-opacity=".25" stroke-width="6"/>'
            f'<path d="M268 196 V300 M332 196 V300" style="stroke:var(--c2)" stroke-width="6" stroke-linecap="round"/>'
            f'<rect x="200" y="470" width="200" height="110" rx="22" fill="#000" opacity=".1"/>'
            f'<rect x="140" y="650" width="320" height="40" style="fill:var(--c2)"/><rect x="22" y="500" width="82" height="34" transform="rotate(4 63 517)" style="fill:var(--c2)"/>'
            f'<rect x="496" y="500" width="82" height="34" transform="rotate(-4 537 517)" style="fill:var(--c2)"/>'
            f'<path d="M300 210 V650" stroke="#000" stroke-opacity=".06" stroke-width="3"/></g>')


def card(inner):
    return f'<svg viewBox="0 0 900 1200" xmlns="http://www.w3.org/2000/svg"><rect width="900" height="1200" style="fill:var(--bg1)"/>{inner}</svg>'


def h(y, *lines, size=70):
    return "".join(f'<text x="64" y="{y + k * (size + 10)}" font-family="{FH}" font-size="{size}" fill="{INK}">{t}</text>' for k, t in enumerate(lines))


def pill(x, y, t, w):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="68" rx="34" fill="#fff"/>'
            f'<text x="{x + w / 2}" y="{y + 44}" text-anchor="middle" font-family="{FB}" font-weight="800" font-size="27" fill="{INK}">{t}</text>')


ICONS = [  # маленькие рисунки деталей в квадрате 376 × 250
    '<path d="M108 210 C90 40 286 40 268 210 C240 250 136 250 108 210 Z" style="fill:var(--c1)"/><path d="M136 200 C150 228 226 228 240 200" fill="none" stroke="#000" stroke-opacity=".25" stroke-width="6"/>'
    '<path d="M168 225 V250 M208 225 V250" style="stroke:var(--c2)" stroke-width="6" stroke-linecap="round"/>',
    '<rect x="88" y="70" width="200" height="90" style="fill:var(--c1)"/><rect x="88" y="160" width="200" height="60" style="fill:var(--c2)"/>'
    + "".join(f'<path d="M{100 + k * 14} 166 V214" stroke="#000" stroke-opacity=".12" stroke-width="5"/>' for k in range(14)),
    '<rect x="68" y="50" width="240" height="190" rx="10" style="fill:var(--c1)"/><path d="M118 120 H258 L280 220 H96 Z" style="fill:var(--c2)"/>'
    '<path d="M118 120 L96 220 M258 120 L280 220" stroke="#000" stroke-opacity=".2" stroke-width="5"/>',
    '<rect x="68" y="50" width="240" height="190" rx="10" style="fill:var(--c1)"/><path d="M188 50 V240" stroke="#fff" stroke-width="6" stroke-dasharray="14 10"/>'
    '<path d="M174 50 V240 M202 50 V240" stroke="#000" stroke-opacity=".12" stroke-width="3"/>',
]

SIZES = [("XS–S", "до 172", "до 96", "68", "58"), ("M", "170–180", "96–104", "71", "60"), ("L", "178–188", "104–112", "74", "62"), ("XL", "от 186", "112–120", "77", "64")]

SLIDES = [
    ("Обложка", card(h(128, "Худи", "оверсайз", size=96) + hoodie(170, 260, 1.0) + pill(64, 1050, "футер 3-нитка", 260) + pill(344, 1050, "380 г/м²", 190)
                     + pill(554, 1050, "унисекс", 170))),
    ("Ткань", card(h(128, "Плотное,", "но не душное")
                   + '<g transform="translate(64 300)"><rect width="772" height="420" rx="36" style="fill:var(--c1)"/>'
                   + "".join(f'<path d="M0 {k * 16} H772" stroke="#fff" stroke-opacity=".08" stroke-width="5"/>' for k in range(2, 26))
                   + f'<circle cx="560" cy="210" r="150" fill="#fff"/><text x="560" y="214" text-anchor="middle" font-family="{FH}" font-size="86" fill="{INK}">380</text>'
                   f'<text x="560" y="268" text-anchor="middle" font-family="{FB}" font-weight="700" font-size="30" fill="{MUT}">г/м²</text></g>'
                   + "".join(f'<text x="64" y="{820 + k * 110}" font-family="{FB}" font-weight="800" font-size="34" fill="{INK}">{a}</text>'
                             f'<text x="64" y="{862 + k * 110}" font-family="{FB}" font-size="28" fill="{MUT}">{b}</text>'
                             for k, (a, b) in enumerate([("Хлопок 80%, полиэстер 20%", "не садится после стирки"), ("Мягкий начёс внутри", "тепло без свитера под низ"),
                                                         ("Не катышится", "выдержал 20 000 циклов истирания")])))),
    ("Посадка", card(h(128, "Свободно —", "на любой рост")
                     + "".join(f'<g transform="translate({90 + k * 390} 330)">'
                               + hoodie(0, 70, .5 + k * .04) + f'<rect x="110" y="{430 + k * 26}" width="30" height="{220 - k * 8}" fill="{MUT}" opacity=".45"/>'
                               f'<rect x="160" y="{430 + k * 26}" width="30" height="{220 - k * 8}" fill="{MUT}" opacity=".45"/>'
                               f'<text x="150" y="{720 + k * 20}" text-anchor="middle" font-family="{FB}" font-weight="800" font-size="30" fill="{INK}">{t}</text>'
                               f'<text x="150" y="{760 + k * 20}" text-anchor="middle" font-family="{FB}" font-size="26" fill="{MUT}">{d}</text></g>'
                               for k, (t, d) in enumerate([("рост 168, размер M", "длина до середины бедра"), ("рост 184, размер M", "длина до пояса джинсов")])))),
    ("Размеры", card(h(128, "Размерная", "сетка") + f'<g transform="translate(64 330)" font-family="{FB}">'
                     + "".join(f'<text x="{x}" y="0" font-weight="700" font-size="24" fill="{MUT}">{t}</text>' for x, t in [(0, "размер"), (170, "рост"), (340, "грудь"), (520, "длина"), (660, "рукав")])
                     + "".join(f'<rect x="-16" y="{30 + k * 120}" width="804" height="100" rx="22" fill="#fff" opacity="{.9 if k % 2 == 0 else .55}"/>'
                               f'<text x="0" y="{92 + k * 120}" font-family="{FH}" font-size="38" fill="{INK}">{z}</text>'
                               + "".join(f'<text x="{x}" y="{92 + k * 120}" font-weight="700" font-size="30" fill="{INK}">{v}</text>' for x, v in [(170, r), (340, c), (520, l), (660, sl)])
                               for k, (z, r, c, l, sl) in enumerate(SIZES))
                     + f'<text x="0" y="560" font-size="26" fill="{MUT}">все размеры в сантиметрах · между двумя — берите меньший</text></g>')),
    ("Детали", card(h(128, "Детали, которые", "видно вблизи", size=64) + "".join(
        f'<g transform="translate({64 + (k % 2) * 396} {300 + (k // 2) * 400})"><rect width="376" height="370" rx="32" fill="#fff"/>'
        + ICONS[k]
        + f'<text x="32" y="290" font-family="{FB}" font-weight="800" font-size="30" fill="{INK}">{a}</text>'
        f'<text x="32" y="330" font-family="{FB}" font-size="25" fill="{MUT}">{b}</text></g>'
        for k, (a, b) in enumerate([("Двойной капюшон", "держит форму"), ("Манжеты с лайкрой", "не растягиваются"),
                                    ("Карман-кенгуру", "с потайным отделом"), ("Плоские швы", "не трут под курткой")])))),
    ("Уход", card(h(128, "Стирать", "наизнанку") + "".join(
        f'<g transform="translate({64 + (k % 2) * 396} {320 + (k // 2) * 300})"><rect width="376" height="270" rx="32" fill="#fff"/>'
        f'<text x="188" y="130" text-anchor="middle" font-family="{FH}" font-size="64" fill="{INK}">{a}</text>'
        f'<text x="188" y="200" text-anchor="middle" font-family="{FB}" font-weight="700" font-size="27" fill="{MUT}">{b}</text></g>'
        for k, (a, b) in enumerate([("30°", "деликатная стирка"), ("800", "оборотов отжима"), ("без", "сушильной машины"), ("110°", "утюг через ткань")]))
        + f'<text x="64" y="1000" font-family="{FB}" font-weight="700" font-size="30" fill="{INK}">После 30 стирок цвет и размер</text>'
        f'<text x="64" y="1044" font-family="{FB}" font-weight="700" font-size="30" fill="{INK}">остаются прежними</text>')),
]

COLORS = [("Молоко", "#ece5d8", "#ddd3c2", "#f6f2ea"), ("Шалфей", "#9fae95", "#8a9a80", "#e7ebe2"), ("Кирпич", "#b4583f", "#9c4a34", "#f1e3dc"), ("Графит", "#3c3d40", "#2d2e30", "#e4e3e1")]

FIT = ('<div class="fit"><div class="fit-l"><label><span>Рост</span><b id="fH"></b><input type="range" id="fh" min="150" max="200" value="176" aria-label="Рост"></label>'
       '<label><span>Обхват груди</span><b id="fC"></b><input type="range" id="fc" min="80" max="124" value="100" aria-label="Обхват груди"></label>'
       '<div class="seg" id="fS"><button type="button" class="on" data-f="0">Как задумано</button><button type="button" data-f="1">Посвободнее</button></div></div>'
       '<div class="fit-r"><small>Ваш размер</small><b id="fZ">M</b><p id="fT"></p></div></div>')

CSS = MP_CSS + """
.hero h1{font-size:clamp(40px,5.2vw,80px);font-weight:400}.sh h2,.cta h2,.mp-r h3{font-weight:400}
.fit{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.8fr);gap:clamp(20px,4vw,56px);align-items:center;max-width:980px}
.fit-l{display:grid;gap:22px}.fit-l label{display:grid;grid-template-columns:1fr auto;gap:8px 12px;align-items:baseline}
.fit-l span{color:var(--soft)}.fit-l b{font:400 24px var(--fh)}.fit-l input{grid-column:1/-1;width:100%;accent-color:var(--ac)}
.fit-r{background:var(--ink);color:var(--bg);border-radius:24px;padding:28px}
.fit-r small{font-size:14px;opacity:.7}.fit-r b{display:block;font:400 clamp(64px,8vw,104px)/1 var(--fh);margin:8px 0 14px}.fit-r p{opacity:.85}
@media (max-width:980px){.fit{grid-template-columns:1fr}}
"""

JS = r"""
(function(){var C=""" + str([list(c) for c in COLORS]).replace("'", '"') + r""";
var root=document.getElementById('mp'),sw=document.getElementById('mpC'),big=document.getElementById('mpBig'),th=document.getElementById('mpTh');
function color(i){var c=C[i];root.style.setProperty('--c1',c[1]);root.style.setProperty('--c2',c[2]);root.style.setProperty('--bg1',c[3]);
 sw.querySelectorAll('button').forEach(function(b,k){b.classList.toggle('on',k===i)});document.getElementById('mpCn').textContent=c[0]}
sw.innerHTML=C.map(function(c){return'<button type="button" style="--s:'+c[1]+'" aria-label="'+c[0]+'"></button>'}).join('');
sw.addEventListener('click',function(e){var b=e.target.closest('button');if(b)color([].indexOf.call(sw.children,b))});
function show(i){var s=th.querySelectorAll('button');s.forEach(function(b,k){b.classList.toggle('on',k===i)});big.innerHTML=s[i].querySelector('.svgsrc').innerHTML;big.dataset.i=i;
 document.getElementById('mpN').textContent=(i+1)+' из '+s.length+': '+s[i].dataset.t}
th.addEventListener('click',function(e){var b=e.target.closest('button');if(b)show([].indexOf.call(th.querySelectorAll('button'),b))});
function step(d){var n=th.querySelectorAll('button').length;show(((+big.dataset.i||0)+d+n)%n)}
document.getElementById('mpPrev').addEventListener('click',function(){step(-1)});document.getElementById('mpNext').addEventListener('click',function(){step(1)});
var x0=null;big.addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});big.addEventListener('touchend',function(e){if(x0==null)return;var d=e.changedTouches[0].clientX-x0;if(Math.abs(d)>40)step(d<0?1:-1);x0=null});
color(1);show(0);
var Z=['XS–S','M','L','XL'],free=0,fs=document.getElementById('fS');
function fit(){var h=+document.getElementById('fh').value,c=+document.getElementById('fc').value;document.getElementById('fH').textContent=h+' см';document.getElementById('fC').textContent=c+' см';
 var bc=c<=96?0:c<=104?1:c<=112?2:3,bh=h<=172?0:h<=180?1:h<=188?2:3,k=Math.max(bc,bh-1);if(free)k=Math.min(3,k+1);
 var len=[68,71,74,77][k],t=(h<165?'Длина ниже бедра — так и задумано, рукав подвернуть один раз. ':h>188?'Длина до пояса, рукав ровно до запястья. ':'Длина до середины бедра, рукав с запасом. ')+'Длина изделия '+len+' см.';
 document.getElementById('fZ').textContent=Z[k];document.getElementById('fT').textContent=t}
['fh','fc'].forEach(function(id){document.getElementById(id).addEventListener('input',fit)});
fs.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;fs.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)});free=+b.dataset.f;fit()});fit();
})();
"""


def cfg() -> dict:
    thumbs = "".join(f'<button type="button" data-t="{t}" aria-label="Слайд {i + 1}: {t}">{s}<div class="svgsrc" hidden>{s}</div></button>' for i, (t, s) in enumerate(SLIDES))
    c0 = "--c1:#9fae95;--c2:#8a9a80;--bg1:#e7ebe2"
    studio = (f'<div class="mp" id="mp" style="{c0}"><div><div class="mp-big" id="mpBig"></div>'
              '<div class="mp-nav"><button type="button" id="mpPrev" aria-label="Назад">←</button><span id="mpN"></span>'
              '<button type="button" id="mpNext" aria-label="Вперёд">→</button></div><div class="mp-th" id="mpTh">' + thumbs + '</div></div>'
              '<div class="mp-r"><h3>Один шаблон на четыре цвета и 120 карточек</h3><p>Магазину нужно было оформить всю линейку: худи, свитшоты и брюки в четырёх цветах. '
              'Слайды собраны так, что цвет и модель меняются без перерисовки.</p><div class="mp-c" id="mpC"></div><small>Цвет: <b id="mpCn"></b></small>'
              '<ul><li>Посадка показана на двух ростах — главный вопрос в отзывах про оверсайз</li><li>Размерная сетка крупно, с советом «между двумя — берите меньший»</li>'
              '<li>Плотность ткани — одной цифрой на обложке</li></ul></div></div>')
    return {
        "slug": "design/vors", "brand": "Ворс", "favLetter": "В",
        "layout": 'frame', "header": 'center', "secHead": 'split', "resStyle": 'grid', "ctaStyle": 'line',  # layout
        "title": "Ворс — карточки маркетплейса для одежды · YSD DEV",
        "desc": "Дизайн карточек маркетплейса для худи оверсайз: обложка и пять слайдов — ткань, посадка на двух ростах, размерная сетка, детали, уход; "
                "четыре цвета и подбор размера по росту и обхвату груди.",
        "theme": {"bg": "#f3f0ea", "ink": INK, "soft": "#4a453e", "mut": MUT, "line": "#e0dbd1", "line2": "#c9c2b5", "card": "#fff", "alt": "#ebe6dc",
                  "ac": "#b4583f", "aci": "#fff", "fh": f'"{FH}",sans-serif', "fb": f'"{FB}",sans-serif', "hw": "400", "ht": "-.01em",
                  "cbg": INK, "cink": "#f3f0ea", "kc": "#9c4a34", "c1": "#ece5d8", "c2": "#ddd3c2", "bg1": "#f6f2ea"},
        "fonts": [(FH, "dela-gothic-one", [400], "normal"), (FB, "manrope", [400, 500, 700, 800], "normal")],
        "css": CSS + ".kick{text-transform:none;letter-spacing:0;font-size:15px}",
        "hero": {"kicker": "Карточки для маркетплейса", "h1": "Оверсайз, который не возвращают из-за размера",
                 "lead": "Обложка и пять слайдов для худи из плотного футера. Самый частый возврат в оверсайзе — «не та посадка», "
                         "поэтому половина карточки отвечает на вопрос «как сядет на мне».",
                 "art": f'<div style="{c0}">' + SLIDES[0][1] + "</div>", "cta": "Листать карточку", "go": "cards"},
        "facts": [("Клиент", "«Ворс», одежда из футера"), ("Работа", "шаблон из 6 слайдов, 4 цвета, 120 карточек"),
                  ("Срок", "8 рабочих дней"), ("Формат", "900 × 1200 для маркетплейсов")],
        "sections": [
            {"type": "text3", "id": "task", "nav": "Задача", "kick": "Задача", "h2": "Почему худи возвращали",
             "items": [("Посадка", "«Слишком большое»", "Покупатели не понимали, что оверсайз — это задумка, и брали размер меньше. Потом возвращали."),
                       ("Ткань", "Фото не передают плотность", "На снимке не видно, что футер плотный. Нужна цифра и сравнение, а не «премиум качество»."),
                       ("Объём", "120 карточек", "Худи, свитшоты и брюки в четырёх цветах. Шаблон должен собираться без дизайнера.")]},
            {"type": "html", "id": "cards", "nav": "Карточка", "kick": "Карточка", "h2": "Обложка и пять слайдов",
             "lead": "Листайте стрелками или свайпом, меняйте цвет справа.", "html": studio, "alt": True},
            {"type": "html", "id": "fit", "nav": "Размер", "kick": "Подбор размера", "h2": "Тот же подбор — в описании товара",
             "lead": "Логика размерной сетки, по которой написан слайд. Двигайте рост и обхват груди.", "html": FIT},
            {"type": "palette", "id": "color", "nav": "Цвета", "kick": "Цвета", "h2": "Фон карточки — светлый тон изделия", "alt": True,
             "lead": "Так карточки одной модели в разных цветах сразу видно в выдаче. Нажмите, чтобы скопировать код.",
             "colors": [(n, a, "цвет изделия") for n, a, b, c in COLORS] + [("Сажа", INK, "заголовки и цифры")]},
            {"type": "type", "id": "type", "kick": "Шрифты", "h2": "Тяжёлый заголовок и чёткие цифры",
             "fonts": [(FH, f"'{FH}'", "заголовки слайдов", "Худи оверсайз", ""),
                       (FB, f"'{FB}'", "размеры, состав, плашки", "380 г/м² · рост 170–180 · M", "font-weight:800")]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что получил продавец",
             "stats": [("6", "слайдов в шаблоне"), ("4", "цвета без перерисовки"), ("120", "карточек на одном шаблоне"), ("8 дней", "от брифа до загрузки")]},
        ],
        "ctaTitle": "Нужны карточки для одежды?",
        "js": JS,
    }
