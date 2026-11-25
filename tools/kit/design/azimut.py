"""«Азимут» — логотип и знак геодезической компании: идея, построение по шагам, версии, цвет, шрифт, носители."""

INK, ORANGE, PAPER = "#13202b", "#ff5a1f", "#f3f1ec"


def mark(fill=INK, cut=PAPER, dot=ORANGE, size=100):
    """Знак: треугольник-визир, меридиан и репер."""
    return (f'<path d="M50 8 L90 88 H10 Z" fill="{fill}"/>'
            f'<path d="M50 8 V88" stroke="{cut}" stroke-width="7"/>'
            f'<circle cx="50" cy="62" r="9.5" fill="{dot}" stroke="{cut}" stroke-width="5"/>')


def logo_h(fill=INK, cut=PAPER, dot=ORANGE, txt=None):
    t = txt or fill
    return (f'<g transform="translate(0 6) scale(.88)">{mark(fill, cut, dot)}</g>'
            f'<text x="104" y="74" font-family="Unbounded" font-weight="700" font-size="44" letter-spacing="0" fill="{t}">АЗИМУТ</text>'
            f'<text x="106" y="98" font-family="Inter Tight" font-weight="500" font-size="13.5" letter-spacing="3.1" fill="{t}" opacity=".72">ГЕОДЕЗИЯ И КАДАСТР</text>')


def svg(body, vb="0 0 400 300", bg=None):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg">' + (f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else "") + body + "</svg>"


HERO = svg(
    '<defs><pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#c9c4b8" stroke-width=".6"/></pattern></defs>'
    '<rect width="640" height="520" fill="url(#g)"/>'
    '<g stroke="#ff5a1f" stroke-width="1" fill="none" opacity=".75"><circle cx="320" cy="250" r="170" stroke-dasharray="3 6"/><path d="M320 40V470M110 250H530"/></g>'
    '<g font-family="Inter Tight" font-size="12" fill="#5d6670"><text x="330" y="56">N 0°</text><text x="490" y="244">90°</text><text x="330" y="462">180°</text></g>'
    '<g transform="translate(180 110) scale(2.8)">' + mark() + '</g>'
    '<text x="320" y="505" text-anchor="middle" font-family="Unbounded" font-weight="700" font-size="30" letter-spacing="2" fill="#13202b">АЗИМУТ</text>',
    "0 0 640 520", PAPER)

STEPS = ["Сетка 8 × 8 и окружность-лимб", "Равнобедренный треугольник — визир", "Меридиан делит знак по оси север—юг",
         "Репер на 2/3 высоты: точка, от которой ведётся съёмка", "Готовый знак и охранное поле"]
BUILD = ('<div class="bld"><div class="bld-a"><svg viewBox="-10 -10 120 120" id="bldSvg">'
         '<g data-k="0"><path d="' + " ".join(f"M{x} 0V100M0 {x}H100" for x in range(0, 101, 12)) + '" stroke="#c9c4b8" stroke-width=".35" fill="none"/>'
         '<circle cx="50" cy="56" r="42" fill="none" stroke="#ff5a1f" stroke-width=".5" stroke-dasharray="1.5 1.5"/></g>'
         '<g data-k="1"><path d="M50 8 L90 88 H10 Z" fill="none" stroke="#13202b" stroke-width=".9"/><g font-size="3.6" fill="#5d6670" font-family="Inter Tight"><text x="66" y="44">63,4°</text><text x="22" y="94">80 ед.</text></g></g>'
         '<g data-k="2"><path d="M50 2V96" stroke="#ff5a1f" stroke-width=".9"/></g>'
         '<g data-k="3"><circle cx="50" cy="62" r="9.5" fill="none" stroke="#ff5a1f" stroke-width=".9"/><path d="M38 62h24" stroke="#ff5a1f" stroke-width=".4"/><text x="64" y="64" font-size="3.6" fill="#5d6670" font-family="Inter Tight">⅔ h</text></g>'
         '<g data-k="4">' + mark() + '<rect x="-2" y="-4" width="104" height="104" fill="none" stroke="#ff5a1f" stroke-width=".5" stroke-dasharray="2 2"/></g>'
         '</svg></div><div class="bld-t"><div class="kick">Шаг <span id="bldN">1</span> из 5</div><h3 id="bldH">' + STEPS[0] + '</h3>'
         '<p id="bldP"></p><input type="range" id="bldR" min="0" max="4" value="0" aria-label="Шаг построения"><div class="bld-d" id="bldD"></div></div></div>')

VAR = [
    ("Горизонтальная — основная", svg('<g transform="translate(40 105)">' + logo_h() + '</g>', "0 0 440 300", PAPER), 6),
    ("Вертикальная — для квадратных носителей", svg('<g transform="translate(150 60) scale(1.4)">' + mark() + '</g><text x="220" y="250" text-anchor="middle" font-family="Unbounded" font-weight="700" font-size="34" fill="#13202b">АЗИМУТ</text>', "0 0 440 300", "#e8e4da"), 6),
    ("Инверсия на тёмном", svg('<g transform="translate(40 105)">' + logo_h("#f3f1ec", "#13202b") + '</g>', "0 0 440 300", INK), 4),
    ("Одноцветная — для гравировки и печати в один цвет", svg('<g transform="translate(40 105)">' + logo_h(INK, PAPER, INK) + '</g>', "0 0 440 300", "#ffffff"), 4),
    ("Знак — аватар и иконка", svg('<rect x="135" y="65" width="170" height="170" rx="38" fill="#ff5a1f"/><g transform="translate(160 88) scale(1.2)">' + mark("#13202b", "#ff5a1f", "#f3f1ec") + '</g>', "0 0 440 300", "#f6e3d8"), 4),
]

CARRIERS = [
    ("Визитка 90×50 мм", svg('<rect x="40" y="58" width="320" height="184" rx="6" fill="#fff" stroke="#e1ddd2"/>'
                             '<g transform="translate(64 84) scale(.32)">' + mark() + '</g><text x="64" y="176" font-family="Unbounded" font-weight="700" font-size="16" fill="#13202b">Олег Брагин</text>'
                             '<text x="64" y="196" font-family="Inter Tight" font-size="11" fill="#5d6670">кадастровый инженер · рег. № 31487</text>'
                             '<text x="64" y="220" font-family="Inter Tight" font-size="11" fill="#13202b">+7 912 •••-••-46 · azimut-geo.ru</text>'
                             '<rect x="330" y="58" width="30" height="184" fill="#ff5a1f"/>', "0 0 400 300", "#e8e4da"), 4, "4/3"),
    ("Наклейка на каску", svg('<path d="M90 210 Q90 90 200 80 Q310 90 310 210 Z" fill="#ff5a1f"/><rect x="74" y="205" width="252" height="22" rx="11" fill="#e64d15"/>'
                              '<circle cx="200" cy="150" r="42" fill="#f3f1ec"/><g transform="translate(176 124) scale(.48)">' + mark() + '</g>', "0 0 400 300", "#dfe3e6"), 4, "4/3"),
    ("Дверь автомобиля", svg('<rect x="30" y="70" width="340" height="170" rx="22" fill="#f7f7f5" stroke="#cfd4d8"/><path d="M60 70 L110 30 H300 L340 70" fill="#cfd8de" stroke="#b9c3ca"/>'
                             '<g transform="translate(58 120) scale(.62)">' + logo_h() + '</g><rect x="30" y="214" width="340" height="12" fill="#ff5a1f"/>'
                             '<text x="58" y="198" font-family="Inter Tight" font-size="12" fill="#13202b">Межевание · топосъёмка · вынос границ</text>', "0 0 400 300", "#e3e7ea"), 4, "4/3"),
    ("Бирка на межевой знак", svg('<rect x="160" y="40" width="80" height="230" rx="4" fill="#8a6a45"/><rect x="125" y="88" width="150" height="96" rx="10" fill="#ff5a1f"/>'
                                  '<circle cx="146" cy="136" r="6" fill="#8a6a45"/><g transform="translate(164 102) scale(.36)">' + mark("#13202b", "#ff5a1f", "#f3f1ec") + '</g>'
                                  '<text x="246" y="128" font-family="Unbounded" font-weight="700" font-size="11" fill="#13202b" text-anchor="end">№ 0417</text>'
                                  '<text x="262" y="150" font-family="Inter Tight" font-size="9" fill="#13202b" text-anchor="end">не трогать</text>', "0 0 400 300", "#d9dfc8"), 6, "4/3"),
    ("Шапка отчёта о съёмке", svg('<rect x="40" y="30" width="320" height="250" fill="#fff" stroke="#e1ddd2"/><g transform="translate(60 48) scale(.42)">' + logo_h() + '</g>'
                                  '<path d="M60 100H340" stroke="#13202b" stroke-width="1.5"/><text x="60" y="124" font-family="Unbounded" font-weight="700" font-size="13" fill="#13202b">Топографический план М 1:500</text>'
                                  '<g stroke="#9aa3ab" stroke-width=".8" fill="none"><path d="M70 230 C120 170 170 250 220 190 S300 160 330 200"/><path d="M70 250 C120 190 170 270 220 210 S300 180 330 220"/><path d="M70 210 C120 150 170 230 220 170 S300 140 330 180"/></g>'
                                  '<circle cx="230" cy="186" r="4" fill="#ff5a1f"/>', "0 0 400 300", "#e8e4da"), 6, "4/3"),
]

JS = r"""
(function(){var T=["Знак собран на модульной сетке 8 × 8 внутри окружности-лимба — как шкала угломерного инструмента. Сетка держит пропорции, когда знак уменьшают до 16 пикселей.",
"Визир — равнобедренный треугольник с углом при вершине 53,2°. Острый, но не агрессивный: читается как стрелка и как вешка на местности.",
"Меридиан проходит по оси и рассекает знак: направление на север — то, с чего начинается любая съёмка. Разрез виден и в одном цвете.",
"Репер — оранжевая точка на двух третях высоты. Так на чертежах отмечают пункт геодезической сети. Это единственный акцентный цвет в знаке.",
"Охранное поле — половина ширины знака со всех сторон. Внутри него нельзя ставить текст и другие логотипы."];
var r=document.getElementById('bldR'),G=document.querySelectorAll('#bldSvg [data-k]'),H=document.getElementById('bldH'),P=document.getElementById('bldP'),N=document.getElementById('bldN'),D=document.getElementById('bldD');
var S=""" + str(STEPS).replace("'", '"') + r""";
D.innerHTML=S.map(function(s,i){return'<button type="button" data-i="'+i+'">'+(i+1)+'</button>'}).join('');
function set(i){r.value=i;G.forEach(function(g){var k=+g.dataset.k;g.style.opacity=k<=i?(k<i&&i===4&&k<4?(k===0?.35:0):1):0});H.textContent=S[i];P.textContent=T[i];N.textContent=i+1;
 D.querySelectorAll('button').forEach(function(b){b.classList.toggle('on',+b.dataset.i===i)})}
r.addEventListener('input',function(){set(+r.value)});D.addEventListener('click',function(e){var b=e.target.closest('button');if(b)set(+b.dataset.i)});set(0);
var auto=0,tm=setInterval(function(){if(auto>=4){clearInterval(tm);return}var b=document.querySelector('.bld');var rc=b.getBoundingClientRect();if(rc.top<innerHeight*.7&&rc.bottom>0){auto++;set(auto)}},1400);
r.addEventListener('pointerdown',function(){clearInterval(tm)});D.addEventListener('pointerdown',function(){clearInterval(tm)});
var sz=document.getElementById('szR'),sb=document.getElementById('szBox'),sv=document.getElementById('szV');function size(){var v=+sz.value;sb.style.width=v+'px';sv.textContent=v+' px · '+(v<24?'только знак':'знак и надпись');sb.classList.toggle('only',v<24)}sz.addEventListener('input',size);size();
})();
"""

CSS = """
.hero h1{font-size:clamp(40px,5.6vw,84px)}
.bld{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,4vw,64px);align-items:center}
.bld-a{background:#fff;border-radius:20px;padding:clamp(18px,3vw,40px);box-shadow:0 0 0 1px var(--line)}
.bld-a g{transition:opacity .5s}
.bld-t h3{font-size:clamp(26px,3vw,40px);margin:12px 0 14px}
.bld-t p{color:var(--soft);min-height:5.2em}
.bld-t input{width:100%;accent-color:#ff5a1f;margin:22px 0 14px}
.bld-d{display:flex;gap:8px}.bld-d button{width:40px;height:40px;border-radius:50%;box-shadow:inset 0 0 0 1.5px var(--line2);font-weight:600}
.bld-d button.on{background:#13202b;color:#f3f1ec;box-shadow:none}
.sz{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:clamp(20px,4vw,56px);align-items:center;background:#fff;border-radius:20px;padding:clamp(20px,3vw,40px);box-shadow:0 0 0 1px var(--line)}
.sz-v{height:220px;display:grid;place-items:center;background:repeating-linear-gradient(0deg,#f6f4ef 0 1px,transparent 1px 16px),repeating-linear-gradient(90deg,#f6f4ef 0 1px,transparent 1px 16px);border-radius:12px}
#szBox svg .w{transition:opacity .2s}#szBox.only svg .w{opacity:0}
.sz input{width:100%;accent-color:#ff5a1f}
.sz b{font:600 22px var(--fh)}.sz p{color:var(--soft);margin-top:8px}
.no{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-top:20px}
.no figure{margin:0;background:#fff;border-radius:14px;padding:16px;box-shadow:0 0 0 1px var(--line);position:relative}
.no figure::after{content:"✕";position:absolute;top:10px;right:12px;width:24px;height:24px;border-radius:50%;background:#e5484d;color:#fff;font-size:13px;display:grid;place-items:center}
.no figcaption{font-size:13px;color:var(--soft);margin-top:10px}
@media (max-width:980px){.bld,.sz{grid-template-columns:1fr}.no{grid-template-columns:1fr 1fr}}
"""


def cfg() -> dict:
    no = [("Не поворачивать", '<g transform="rotate(-18 200 150) translate(40 105)">' + logo_h() + '</g>'),
          ("Не менять цвет репера", '<g transform="translate(40 105)">' + logo_h(INK, PAPER, "#2f8cff") + '</g>'),
          ("Не растягивать", '<g transform="translate(40 105) scale(1.35 .7)">' + logo_h() + '</g>'),
          ("Не ставить на пёстрый фон", '<rect width="440" height="300" fill="#ff5a1f"/><circle cx="90" cy="70" r="80" fill="#f2c14e"/><circle cx="380" cy="260" r="110" fill="#2f8cff"/><g transform="translate(40 105)">' + logo_h() + '</g>')]
    size_svg = ('<div id="szBox" style="width:240px"><svg viewBox="0 0 420 110" style="width:100%"><g transform="translate(0 6) scale(.88)">' + mark() +
                '</g><g class="w"><text x="104" y="74" font-family="Unbounded" font-weight="700" font-size="44" fill="#13202b">АЗИМУТ</text></g></svg></div>')
    return {
        "slug": "design/azimut", "brand": "Азимут", "favLetter": "А",
        "layout": 'stack', "header": 'center', "secHead": 'split', "resStyle": 'line', "ctaStyle": 'ac',  # layout
        "title": "Азимут — логотип и знак геодезической компании · YSD DEV",
        "desc": "Логотип и знак для геодезической компании: идея, построение на сетке по шагам, версии, цвета, шрифт и носители — "
                "визитка, каска, автомобиль, межевой знак, отчёт.",
        "theme": {"bg": "#f3f1ec", "ink": "#13202b", "soft": "#4c5761", "mut": "#7c858d", "line": "#dcd8cd", "line2": "#b9b4a7",
                  "card": "#ffffff", "alt": "#e9e6de", "ac": "#ff5a1f", "aci": "#ffffff", "fh": "Unbounded,sans-serif",
                  "fb": '"Inter Tight",sans-serif', "hw": "700", "ht": "-.02em", "cbg": "#13202b", "cink": "#f3f1ec"},
        "fonts": [("Unbounded", "unbounded", [500, 700], "normal"), ("Inter Tight", "inter-tight", [400, 500, 600], "normal")],
        "css": CSS,
        "hero": {"kicker": "Логотип и знак · геодезия", "h1": "Знак, который <em>показывает север</em>",
                 "lead": "Логотип для геодезической компании из Перми: межевание, топосъёмка, вынос границ. Знак должен "
                         "читаться на каске за 20 метров, на бирке межевого знака и в шапке отчёта.",
                 "art": HERO, "cta": "Смотреть построение", "go": "build"},
        "facts": [("Клиент", "«Азимут», геодезия и кадастр, Пермь"), ("Работа", "Знак, логотип, правила, носители"),
                  ("Срок", "9 рабочих дней"), ("Направлений на старте", "3, выбран второй")],
        "sections": [
            {"type": "text3", "id": "idea", "nav": "Идея", "kick": "Задача", "h2": "Три требования к знаку",
             "lead": "Прошлый логотип — теодолит на треноге — сливался в пятно меньше 3 см и не печатался в один цвет на бирках.",
             "items": [("01", "Читается издалека", "На каске и на борту машины знак видят с 20–30 метров. Значит, никаких тонких линий и мелких деталей."),
                       ("02", "Один цвет", "Межевые бирки гравируют, документы печатают на ч/б принтере. Знак обязан работать без цвета."),
                       ("03", "Про точность", "Не «строительная» каска и не карта. Нужен символ измерения: направление, точка отсчёта, угол.")]},
            {"type": "html", "id": "build", "nav": "Построение", "kick": "Построение", "h2": "Знак собран на сетке",
             "lead": "Пять шагов — от сетки до готового знака. Двигайте ползунок.", "html": BUILD, "alt": True},
            {"type": "gallery", "id": "versions", "nav": "Версии", "kick": "Версии", "h2": "Пять версий на все случаи",
             "items": [{"html": v, "cap": f"<b>{c}</b>", "span": s, "ar": "22/15"} for c, v, s in VAR]},
            {"type": "html", "id": "size", "kick": "Минимальный размер", "h2": "Читается от 16 пикселей",
             "html": '<div class="sz"><div class="sz-v">' + size_svg + '</div><div><b id="szV"></b><p>Меньше 24 пикселей надпись убираем и оставляем только знак: треугольник с меридианом узнаётся даже на вкладке браузера.</p>'
                     '<input type="range" id="szR" min="16" max="320" value="220" aria-label="Размер логотипа"></div></div>'
                     '<div class="no">' + "".join(f'<figure><svg viewBox="0 0 440 300">{b}</svg><figcaption>{t}</figcaption></figure>' for t, b in no) + '</div>'},
            {"type": "palette", "id": "color", "nav": "Цвет", "kick": "Цвет", "h2": "Два основных цвета и бумага",
             "lead": "Нажмите на цвет, чтобы скопировать код.", "alt": True,
             "colors": [("Полевой графит", "#13202B", "знак, текст · CMYK 85 65 45 60"), ("Сигнальный", "#FF5A1F", "репер, акценты · Pantone 1655 C"),
                        ("Калька", "#F3F1EC", "фон документов и сайта"), ("Ватман", "#E8E4DA", "плашки, подложки"), ("Нивелир", "#7C858D", "второстепенный текст")]},
            {"type": "type", "id": "type", "nav": "Шрифт", "kick": "Шрифты", "h2": "Широкий гротеск и рабочий текст",
             "fonts": [("Unbounded Bold", "Unbounded", "логотип, заголовки", "АЗИМУТ 59°57′ с. ш.", "font-weight:700"),
                       ("Inter Tight", '"Inter Tight"', "отчёты, сайт, визитки", "Топографическая съёмка М 1:500, 2,4 га — за 3 дня", "font-weight:500")]},
            {"type": "gallery", "id": "use", "nav": "Носители", "kick": "Носители", "h2": "Там, где работает компания", "alt": True,
             "items": [{"html": h, "cap": f"<b>{c}</b>", "span": s, "ar": a} for c, h, s, a in CARRIERS]},
            {"type": "result", "id": "result", "kick": "Итог", "h2": "Что изменилось",
             "stats": [("16 px", "минимальный размер знака"), ("1 цвет", "для гравировки и печати"), ("7", "носителей в первую партию"), ("9 дней", "от брифа до файлов")]},
        ],
        "ctaTitle": "Нужен логотип, который работает везде?",
        "js": JS,
    }
