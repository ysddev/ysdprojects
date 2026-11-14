"""«Лён и Луна» — карточки для маркетплейса: обложка и пять слайдов инфографики для льняного постельного белья, смена цвета."""

FONT_H, FONT_B = "Forum", "Manrope"


def stack(x, y, s=1.0):
    """Стопка сложенного белья: цвет берётся из CSS-переменных --c1/--c2/--c3."""
    g = f'<g transform="translate({x} {y}) scale({s})">'
    g += '<ellipse cx="300" cy="455" rx="300" ry="26" fill="#000" opacity=".12"/>'
    for i, (w, h, yy, var) in enumerate([(560, 120, 300, "--c3"), (520, 110, 196, "--c2"), (480, 104, 98, "--c1"), (430, 92, 10, "--c2")]):
        xx = 300 - w / 2
        g += (f'<rect x="{xx}" y="{yy}" width="{w}" height="{h}" rx="34" style="fill:var({var})"/>'
              f'<path d="M{xx + 26} {yy + h * .55} Q300 {yy + h * .85} {xx + w - 26} {yy + h * .55}" fill="none" stroke="#000" stroke-opacity=".08" stroke-width="3"/>'
              f'<path d="M{xx + 40} {yy + 18} H{xx + w - 40}" stroke="#fff" stroke-opacity=".25" stroke-width="3"/>')
        for k in range(9):
            g += f'<path d="M{xx + 50 + k * (w - 100) / 8} {yy + 26} v{h - 52}" stroke="#000" stroke-opacity=".035" stroke-width="2"/>'
    g += '<path d="M330 12 q20 40 0 90" fill="none" stroke="#000" stroke-opacity=".07" stroke-width="4"/>'
    g += '<rect x="250" y="22" width="100" height="40" rx="6" fill="#fffaf0" opacity=".92"/><text x="300" y="49" text-anchor="middle" font-family="Forum" font-size="20" fill="#3b3128">Лён и Луна</text>'
    return g + "</g>"


def card(inner, bg="var(--bg1)"):
    return (f'<svg viewBox="0 0 900 1200" xmlns="http://www.w3.org/2000/svg"><rect width="900" height="1200" style="fill:{bg}"/>'
            f'<rect x="0" y="0" width="900" height="1200" fill="url(#gr)" opacity=".35"/>{inner}</svg>')


DEFS = ('<svg width="0" height="0" style="position:absolute"><defs><linearGradient id="gr" x1="0" y1="0" x2="0" y2="1">'
        '<stop offset="0" stop-color="#fff" stop-opacity=".5"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient></defs></svg>')


def pill(x, y, t, w=None):
    w = w or 30 + len(t) * 17
    return (f'<rect x="{x}" y="{y}" width="{w}" height="62" rx="31" fill="#fffaf0"/>'
            f'<text x="{x + w / 2}" y="{y + 41}" text-anchor="middle" font-family="{FONT_B}" font-weight="700" font-size="26" fill="#3b3128">{t}</text>')


SLIDES = [
    ("Обложка", card(
        f'<text x="64" y="120" font-family="{FONT_H}" font-size="74" fill="#2d241d">Комплект</text><text x="64" y="196" font-family="{FONT_H}" font-size="74" fill="#2d241d">из чистого льна</text>'
        f'<text x="66" y="250" font-family="{FONT_B}" font-weight="600" font-size="28" fill="#5c4f43">евро · пододеяльник, простыня, 2 наволочки</text>'
        + stack(150, 380, 1.0) + pill(64, 1030, "100% лён", 210) + pill(292, 1030, "160 г/м²", 200) + pill(510, 1030, "4 цвета", 180))),
    ("Почему лён", card(
        f'<text x="64" y="130" font-family="{FONT_H}" font-size="70" fill="#2d241d">Спать прохладно</text><text x="64" y="206" font-family="{FONT_H}" font-size="70" fill="#2d241d">летом и тепло зимой</text>'
        + "".join(f'<g transform="translate(64 {300 + i * 205})"><rect width="772" height="176" rx="28" fill="#fffaf0"/><circle cx="92" cy="88" r="52" style="fill:var(--c1)"/>'
                  f'<text x="92" y="104" text-anchor="middle" font-family="{FONT_B}" font-weight="800" font-size="40" fill="#fffaf0">{n}</text>'
                  f'<text x="176" y="76" font-family="{FONT_B}" font-weight="800" font-size="34" fill="#2d241d">{a}</text><text x="176" y="122" font-family="{FONT_B}" font-size="26" fill="#6b5d50">{b}</text></g>'
                  for i, (n, a, b) in enumerate([("1", "Дышит", "впитывает влагу и сохнет за 2–3 часа"), ("2", "Не электризуется", "не липнет к телу и не собирает пыль"),
                                                 ("3", "Мягче с каждой стиркой", "ткань уже прошла стирку с камнями"), ("4", "Служит 10+ лет", "волокно в 2 раза прочнее хлопка")])))),
    ("Что в комплекте", card(
        f'<text x="64" y="130" font-family="{FONT_H}" font-size="70" fill="#2d241d">Что в комплекте</text>'
        '<g font-family="Manrope">'
        '<rect x="64" y="220" width="460" height="500" rx="20" style="fill:var(--c1)"/><text x="294" y="480" text-anchor="middle" font-weight="800" font-size="36" fill="#fffaf0">Пододеяльник</text><text x="294" y="526" text-anchor="middle" font-size="30" fill="#fffaf0" opacity=".9">200 × 220 см</text>'
        '<rect x="554" y="220" width="282" height="330" rx="20" style="fill:var(--c2)"/><text x="695" y="378" text-anchor="middle" font-weight="800" font-size="32" fill="#2d241d">Простыня</text><text x="695" y="420" text-anchor="middle" font-size="27" fill="#2d241d">240 × 260 см</text>'
        '<rect x="554" y="575" width="134" height="145" rx="16" style="fill:var(--c3)"/><rect x="702" y="575" width="134" height="145" rx="16" style="fill:var(--c3)"/>'
        '<text x="695" y="764" text-anchor="middle" font-weight="800" font-size="28" fill="#2d241d">Наволочки ×2</text><text x="695" y="800" text-anchor="middle" font-size="25" fill="#5c4f43">50 × 70 см, на запах</text>'
        '<rect x="64" y="880" width="772" height="210" rx="28" fill="#fffaf0"/><text x="104" y="960" font-weight="800" font-size="32" fill="#2d241d">Пододеяльник на пуговицах</text>'
        '<text x="104" y="1010" font-size="26" fill="#6b5d50">кокосовые пуговицы, 7 штук — одеяло не сбивается</text>'
        '<g transform="translate(700 950)">' + "".join(f'<circle cx="{k * 34}" cy="20" r="12" fill="#b28b62"/>' for k in range(4)) + '</g></g>')),
    ("Ткань", card(
        f'<text x="64" y="130" font-family="{FONT_H}" font-size="70" fill="#2d241d">Плотный лён</text><text x="64" y="206" font-family="{FONT_H}" font-size="70" fill="#2d241d">без синтетики</text>'
        '<g transform="translate(64 290)"><rect width="772" height="520" rx="28" style="fill:var(--c1)"/>'
        + "".join(f'<path d="M0 {y} H772" stroke="#fff" stroke-opacity=".10" stroke-width="3"/>' for y in range(14, 520, 14))
        + "".join(f'<path d="M{x} 0 V520" stroke="#000" stroke-opacity=".06" stroke-width="3"/>' for x in range(14, 772, 14))
        + '<circle cx="560" cy="260" r="170" fill="#fffaf0"/><text x="560" y="250" text-anchor="middle" font-family="Manrope" font-weight="800" font-size="92" fill="#2d241d">160</text>'
          '<text x="560" y="304" text-anchor="middle" font-family="Manrope" font-size="34" fill="#6b5d50">г/м²</text></g>'
        '<g font-family="Manrope"><text x="64" y="900" font-weight="800" font-size="34" fill="#2d241d">Стирка с камнями</text><text x="64" y="944" font-size="27" fill="#6b5d50">мягкий с первой ночи, не мнётся заломами</text>'
        '<text x="64" y="1030" font-weight="800" font-size="34" fill="#2d241d">Нить 100% лён</text><text x="64" y="1074" font-size="27" fill="#6b5d50">вырастили и соткали в Костромской области</text></g>')),
    ("Размеры и уход", card(
        f'<text x="64" y="130" font-family="{FONT_H}" font-size="70" fill="#2d241d">Размер под вашу</text><text x="64" y="206" font-family="{FONT_H}" font-size="70" fill="#2d241d">кровать</text>'
        '<g font-family="Manrope">' + "".join(
            f'<g transform="translate(64 {270 + i * 112})"><rect width="772" height="94" rx="20" fill="{"#fffaf0" if i % 2 == 0 else "rgba(255,250,240,.55)"}"/>'
            f'<text x="32" y="58" font-weight="800" font-size="30" fill="#2d241d">{a}</text><text x="300" y="58" font-size="27" fill="#5c4f43">{b}</text><text x="740" y="58" text-anchor="end" font-weight="800" font-size="30" fill="#2d241d">{c}</text></g>'
            for i, (a, b, c) in enumerate([("1,5-спальный", "145 × 215 · 220 × 240", "8 490 ₽"), ("2-спальный", "175 × 215 · 220 × 240", "9 790 ₽"),
                                           ("Евро", "200 × 220 · 240 × 260", "10 890 ₽"), ("Семейный", "2 × 145 × 215 · 240 × 260", "13 260 ₽")]))
        + '<text x="64" y="790" font-weight="800" font-size="34" fill="#2d241d">Уход</text>'
        + "".join(f'<g transform="translate({64 + i * 196} 830)"><rect width="176" height="220" rx="24" fill="#fffaf0"/><text x="88" y="104" text-anchor="middle" font-weight="800" font-size="46" style="fill:var(--c1)">{a}</text>'
                  f'<text x="88" y="160" text-anchor="middle" font-size="22" fill="#5c4f43">{b}</text><text x="88" y="190" text-anchor="middle" font-size="22" fill="#5c4f43">{c}</text></g>'
                  for i, (a, b, c) in enumerate([("40°", "деликатная", "стирка"), ("800", "оборотов", "отжим"), ("✕", "без", "отбеливателя"), ("~", "сушить", "расправленным")])) + '</g>')),
]

BEFORE = ('<svg viewBox="0 0 900 1200"><rect width="900" height="1200" fill="#eef0f2"/><rect x="120" y="260" width="660" height="560" fill="#c9cdd2"/>'
          '<text x="450" y="560" text-anchor="middle" font-family="Manrope" font-size="34" fill="#7d848c">фото на кровати, вид сверху</text>'
          '<text x="40" y="110" font-family="Manrope" font-weight="800" font-size="52" fill="#d0021b">ХИТ!!! ЛЁН ЛЮКС ПРЕМИУМ</text>'
          '<text x="40" y="180" font-family="Manrope" font-weight="700" font-size="36" fill="#222">КПБ евро 100% натуральный лён</text>'
          '<g font-family="Manrope" font-size="30" fill="#222"><text x="40" y="900">✔ качество ✔ доставка ✔ гарантия ✔ скидка</text>'
          '<text x="40" y="960">✔ подарок ✔ упаковка ✔ отзывы ✔ размеры</text></g><circle cx="770" cy="1060" r="90" fill="#ffd600"/>'
          '<text x="770" y="1076" text-anchor="middle" font-family="Manrope" font-weight="800" font-size="40" fill="#d0021b">-50%</text></svg>')

COLORS = [("Песок", "#cdb79a", "#e3d4bf", "#b59c7c", "#efe6da"), ("Шалфей", "#9aa98c", "#c5cdb9", "#7f8f72", "#e8ebe2"),
          ("Графит", "#5f6266", "#8c8f93", "#47494d", "#e6e4e1"), ("Терракота", "#c27b5a", "#dba68c", "#a8603f", "#f1e2d8")]

JS = r"""
(function(){var C=""" + str([[n, a, b, c, d] for n, a, b, c, d in COLORS]).replace("'", '"') + r""";
var root=document.getElementById('mp'),sw=document.getElementById('mpC'),big=document.getElementById('mpBig'),th=document.getElementById('mpTh');
function color(i){var c=C[i];root.style.setProperty('--c1',c[1]);root.style.setProperty('--c2',c[2]);root.style.setProperty('--c3',c[3]);root.style.setProperty('--bg1',c[4]);
 sw.querySelectorAll('button').forEach(function(b,k){b.classList.toggle('on',k===i)});document.getElementById('mpCn').textContent=c[0]}
sw.innerHTML=C.map(function(c,i){return'<button type="button" style="--s:'+c[1]+'" aria-label="'+c[0]+'"></button>'}).join('');
sw.addEventListener('click',function(e){var b=e.target.closest('button');if(b)color([].indexOf.call(sw.children,b))});
function show(i){var s=th.querySelectorAll('button');s.forEach(function(b,k){b.classList.toggle('on',k===i)});big.innerHTML=s[i].querySelector('.svgsrc').innerHTML;big.dataset.i=i;
 document.getElementById('mpN').textContent=(i+1)+' / '+s.length+' · '+s[i].dataset.t}
th.addEventListener('click',function(e){var b=e.target.closest('button');if(b)show([].indexOf.call(th.querySelectorAll('button'),b))});
document.getElementById('mpPrev').addEventListener('click',function(){var n=th.querySelectorAll('button').length;show(((+big.dataset.i||0)-1+n)%n)});
document.getElementById('mpNext').addEventListener('click',function(){var n=th.querySelectorAll('button').length;show(((+big.dataset.i||0)+1)%n)});
var x0=null;big.addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});big.addEventListener('touchend',function(e){if(x0==null)return;var d=e.changedTouches[0].clientX-x0;if(Math.abs(d)>40)document.getElementById(d<0?'mpNext':'mpPrev').click();x0=null});
color(0);show(0);
var ba=document.getElementById('baR'),bw=document.getElementById('baW');ba.addEventListener('input',function(){bw.style.clipPath='inset(0 '+(100-ba.value)+'% 0 0)'});
})();
"""

CSS = """
.hero h1{font-size:clamp(46px,6.4vw,96px);font-weight:400}
.mp{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.9fr);gap:clamp(24px,4vw,64px);align-items:start}
.mp-s{position:relative}
.mp-big{border-radius:18px;overflow:hidden;box-shadow:0 30px 60px -40px rgba(60,40,20,.5),0 0 0 1px var(--line);background:var(--bg1)}
.mp-big svg{width:100%;height:auto}
.mp-nav{display:flex;align-items:center;justify-content:space-between;margin-top:14px;gap:12px}
.mp-nav button{width:44px;height:44px;border-radius:50%;box-shadow:inset 0 0 0 1.5px var(--line2);font-size:18px}
.mp-nav span{font-size:14px;color:var(--mut)}
.mp-th{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-top:14px}
.mp-th button{border-radius:8px;overflow:hidden;box-shadow:0 0 0 1px var(--line);opacity:.6;transition:opacity .2s}
.mp-th button.on{opacity:1;box-shadow:0 0 0 2px var(--ink)}
.mp-th svg{width:100%;height:auto}
.mp-r h3{font-size:clamp(26px,2.8vw,40px);margin-bottom:14px;font-weight:400}
.mp-r p{color:var(--soft);margin-bottom:22px}
.mp-c{display:flex;gap:10px;margin:10px 0 6px}.mp-c button{width:46px;height:46px;border-radius:50%;background:var(--s);box-shadow:0 0 0 3px var(--bg),0 0 0 4px var(--line2)}
.mp-c button.on{box-shadow:0 0 0 3px var(--bg),0 0 0 5px var(--ink)}
.mp-r small{color:var(--mut);font-size:14px}
.mp-r ul{margin:22px 0 0;padding:0;list-style:none;display:grid;gap:10px}.mp-r li{padding:14px 16px;border-radius:14px;background:var(--card);font-size:15px}
.ba{position:relative;max-width:560px;margin:0 auto;border-radius:18px;overflow:hidden;box-shadow:0 0 0 1px var(--line)}
.ba>div{position:absolute;inset:0}.ba svg{width:100%;height:auto;display:block}
.ba-l{display:flex;justify-content:space-between;max-width:560px;margin:12px auto 0;font-size:14px;color:var(--mut)}
.ba-r{display:block;width:100%;max-width:560px;margin:14px auto 0;accent-color:var(--ac)}
@media (max-width:980px){.mp{grid-template-columns:1fr}}
"""


def cfg() -> dict:
    thumbs = "".join(f'<button type="button" data-t="{t}" aria-label="Слайд {i + 1}: {t}">{s}<template class="svgsrc">{s}</template></button>'
                     for i, (t, s) in enumerate(SLIDES))
    thumbs = thumbs.replace('<template class="svgsrc">', '<div class="svgsrc" hidden>').replace("</template>", "</div>")
    studio = ('<div class="mp" id="mp">' + DEFS + '<div class="mp-s"><div class="mp-big" id="mpBig"></div><div class="mp-nav"><button type="button" id="mpPrev" aria-label="Назад">←</button>'
              '<span id="mpN"></span><button type="button" id="mpNext" aria-label="Вперёд">→</button></div><div class="mp-th" id="mpTh">' + thumbs + '</div></div>'
              '<div class="mp-r"><h3>Один шаблон — четыре цвета</h3><p>Покупатель листает карточку как каталог: обложка, польза, состав, ткань, размеры. '
              'Цвет меняется во всех слайдах сразу — так мы собрали 20 карточек за 2 дня.</p>'
              '<div class="mp-c" id="mpC"></div><small>Цвет: <b id="mpCn"></b></small>'
              '<ul><li>Текст на обложке читается в выдаче на телефоне — 4 слова и 3 плашки</li><li>Каждый слайд отвечает на один вопрос из отзывов</li>'
              '<li>Размеры с ценой — на отдельном слайде, чтобы не ошибиться с кроватью</li></ul></div></div>')
    return {
        "slug": "design/linen", "brand": "Лён и Луна", "favLetter": "Л",
        "title": "Лён и Луна — карточки товара для маркетплейса · YSD DEV",
        "desc": "Дизайн карточек товара для маркетплейса: обложка и инфографика для льняного постельного белья, единый шаблон в "
                "четырёх цветах, было и стало.",
        "theme": {"bg": "#f6f1e9", "ink": "#2d241d", "soft": "#5c4f43", "mut": "#8c7d6f", "line": "#e5dccf", "line2": "#cbbfae",
                  "card": "#fffaf0", "alt": "#efe7da", "ac": "#a8603f", "aci": "#fffaf0", "fh": "Forum,serif", "fb": "Manrope,sans-serif",
                  "hw": "400", "ht": "0", "cbg": "#2d241d", "cink": "#f6f1e9", "c1": "#cdb79a", "c2": "#e3d4bf", "c3": "#b59c7c", "bg1": "#efe6da"},
        "fonts": [("Forum", "forum", [400], "normal"), ("Manrope", "manrope", [400, 500, 600, 700, 800], "normal")],
        "css": CSS,
        "hero": {"kicker": "Карточки для маркетплейса", "h1": "Карточка, которую <em>листают до конца</em>",
                 "lead": "Обложка и пять слайдов инфографики для льняного постельного белья. Задача — выделиться в выдаче среди "
                         "кричащих «ХИТ!!!» и ответить на вопросы, из-за которых комплекты возвращали.",
                 "art": '<div style="background:var(--bg1)">' + DEFS + SLIDES[0][1] + '</div>', "cta": "Листать карточку", "go": "cards"},
        "facts": [("Клиент", "«Лён и Луна», домашний текстиль"), ("Работа", "Обложка, 5 слайдов, 4 цвета, 20 карточек"),
                  ("Срок", "6 рабочих дней"), ("Площадки", "два крупных маркетплейса")],
        "sections": [
            {"type": "text3", "id": "task", "nav": "Задача", "kick": "Задача", "h2": "Почему старые карточки не работали",
             "items": [("01", "Терялись в выдаче", "Капслок, восклицательные знаки и «−50%» — как у всех соседей. Глаз на этом не останавливается."),
                       ("02", "Не отвечали на вопросы", "В вопросах к товару повторялось одно и то же: какой размер простыни, мнётся ли, как стирать."),
                       ("03", "Возвраты из-за размера", "Каждый четвёртый возврат — «не подошёл размер». Размеры были мелко в описании, а не на слайде.")]},
            {"type": "html", "id": "cards", "nav": "Карточка", "kick": "Карточка", "h2": "Обложка и пять слайдов",
             "lead": "Листайте стрелками или свайпом, меняйте цвет справа.", "html": studio, "alt": True},
            {"type": "html", "id": "before", "nav": "Было и стало", "kick": "Было и стало", "h2": "Тише — значит заметнее",
             "lead": "Двигайте ползунок, чтобы сравнить.",
             "html": '<div class="ba">' + BEFORE + '<div id="baW" style="clip-path:inset(0 50% 0 0)"><div style="--c1:#cdb79a;--c2:#e3d4bf;--c3:#b59c7c;--bg1:#efe6da">' + SLIDES[0][1] + '</div></div></div>'
                     '<div class="ba-l"><span>стало</span><span>было</span></div><input class="ba-r" id="baR" type="range" min="0" max="100" value="50" aria-label="Было и стало"></div>'},
            {"type": "palette", "id": "color", "nav": "Цвета", "kick": "Цвета", "h2": "Палитра льна", "alt": True,
             "lead": "Фон каждой карточки — светлый оттенок цвета ткани. Нажмите, чтобы скопировать код.",
             "colors": [(n, a, "основной цвет ткани") for n, a, b, c, d in COLORS] + [("Сливки", "#FFFAF0", "плашки и подложки"), ("Мокко", "#2D241D", "заголовки")]},
            {"type": "type", "id": "type", "kick": "Шрифты", "h2": "Антиква и чёткий гротеск",
             "fonts": [("Forum", "Forum", "заголовки слайдов", "Спать прохладно летом", ""),
                       ("Manrope ExtraBold", "Manrope", "цифры и плашки", "160 г/м² · 200 × 220 см · 40°", "font-weight:800")]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что изменилось за месяц",
             "stats": [("2,3 → 5,1%", "кликабельность обложки в выдаче"), ("+41%", "добавлений в корзину"), ("−27%", "возвратов из-за размера"), ("20", "карточек на одном шаблоне")]},
        ],
        "ctaTitle": "Нужны карточки, которые продают?",
        "js": JS,
    }
