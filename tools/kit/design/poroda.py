"""«Порода» — фирменный стиль поставщика запчастей для горной техники: знак-грань, сигнальная палитра, этикетка-конструктор, носители."""

YEL, BAS, STEEL, RUST, WHITE, PAPER = "#f2c400", "#1d1f22", "#8a9097", "#b5532a", "#ffffff", "#eef0f1"
FH, FB = "Oswald", "PT Sans"


def mark(x=0, y=0, s=1.0, a=YEL, b=BAS):
    """Скол породы: шестигранник, рассечённый гранью."""
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M40 0 L80 22 V68 L40 90 L0 68 V22 Z" style="fill:{a}"/>'
            f'<path d="M40 0 L80 22 L46 46 Z" style="fill:{b}" opacity=".9"/><path d="M0 68 L46 46 L40 90 Z" style="fill:{b}" opacity=".35"/></g>')


def logo(x=0, y=0, s=1.0, c=BAS, a=YEL, b=BAS, sub=True):
    t = (f'<g transform="translate({x} {y}) scale({s})">{mark(a=a, b=b)}<text x="100" y="66" font-family="{FH}" font-weight="700" font-size="72" '
         f'letter-spacing="2" style="fill:{c}">ПОРОДА</text>')
    if sub:
        t += f'<text x="103" y="88" font-family="{FB}" font-weight="700" font-size="14" letter-spacing="1" style="fill:{c}" opacity=".75">ЗАПЧАСТИ ДЛЯ ГОРНОЙ ТЕХНИКИ</text>'
    return t + "</g>"


def sv(body, vb="0 0 480 360", bg=PAPER):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" style="fill:{bg}"/>{body}</svg>'


_HZ = [0]


def hazard(x, y, w, h, n=14):
    _HZ[0] += 1
    i = f"hz{_HZ[0]}"  # свой id у каждой полосы: на странице их много
    t = f'<g><clipPath id="{i}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath><g clip-path="url(#{i})"><rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{YEL}"/>'
    for k in range(-2, int(w / n) + 4):
        t += f'<path d="M{x + k * n * 2} {y + h} L{x + k * n * 2 + h} {y} h{n} L{x + k * n * 2 + n} {y + h} Z" fill="{BAS}"/>'
    return t + "</g></g>"


def truck(x, y, s=1.0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 60 H300 L330 20 H420 V120 H0 Z" fill="{YEL}"/>'
            f'<rect x="330" y="30" width="70" height="40" fill="{BAS}" opacity=".85"/><rect x="0" y="120" width="440" height="20" fill="{BAS}"/>'
            + "".join(f'<circle cx="{cx}" cy="150" r="34" fill="{BAS}"/><circle cx="{cx}" cy="150" r="14" fill="{STEEL}"/>' for cx in (70, 160, 360))
            + logo(24, 70, .42, c=BAS, a=BAS, b=YEL, sub=False) + "</g>")


HERO = sv(f'<rect width="640" height="520" fill="{BAS}"/>' + "".join(
    f'<path d="M{-40 + k * 80} 520 L{80 + k * 80} 300" stroke="#2a2d31" stroke-width="40"/>' for k in range(10))
          + logo(48, 90, 1.0, c=WHITE) + truck(150, 300, .95) + hazard(0, 490, 640, 30, 16), "0 0 640 520")

PARTS = {
    "pin": ("Палец ковша", "ПР-9204-118", "Komatsu PC400, PC450", "38,4 кг", "сталь 40ХН, закалка ТВЧ"),
    "teeth": ("Зуб ковша", "ПР-5531-207", "CAT 336, 349, 374", "11,2 кг", "литьё, твёрдость 52 HRC"),
    "filter": ("Фильтр гидравлики", "ПР-1180-034", "БелАЗ 7555, 7540", "2,6 кг", "тонкость 10 мкм"),
    "seal": ("Ремкомплект цилиндра", "ПР-7702-415", "Hitachi ZX330, ZX350", "0,9 кг", "полиуретан, 14 позиций"),
}


def label(p="pin"):
    n, art, fit, w, mat = PARTS[p]
    return (f'<svg viewBox="0 0 480 300" xmlns="http://www.w3.org/2000/svg"><rect width="480" height="300" fill="#fff"/>' + hazard(0, 0, 480, 22, 12)
            + logo(24, 42, .36, sub=False) + f'<text x="456" y="72" text-anchor="end" font-family="{FB}" font-weight="700" font-size="14" fill="{STEEL}">в наличии · Кемерово</text>'
            f'<text x="24" y="132" font-family="{FH}" font-weight="600" font-size="34" fill="{BAS}" id="lbN">{n}</text>'
            f'<text x="24" y="166" font-family="{FB}" font-size="16" fill="{BAS}">Подходит: <tspan font-weight="700" id="lbF">{fit}</tspan></text>'
            f'<text x="24" y="192" font-family="{FB}" font-size="16" fill="{BAS}" id="lbM">{mat}</text>'
            f'<rect x="24" y="214" width="130" height="62" fill="{BAS}"/><text x="36" y="238" font-family="{FB}" font-size="12" fill="{YEL}">АРТИКУЛ</text>'
            f'<text x="36" y="264" font-family="{FH}" font-weight="600" font-size="20" fill="#fff" id="lbA">{art}</text>'
            f'<text x="176" y="238" font-family="{FB}" font-size="12" fill="{STEEL}">ВЕС</text><text x="176" y="264" font-family="{FH}" font-weight="600" font-size="20" fill="{BAS}" id="lbW">{w}</text>'
            + "".join(f'<rect x="{300 + k * 6}" y="214" width="{(k * 7) % 4 + 1}" height="62" fill="{BAS}"/>' for k in range(26)) + '</svg>')


LABEL_BOX = ('<div class="lb"><div class="lb-v" id="lbV">' + label() + '</div><div class="lb-r"><h3>Этикетка, которую читают в перчатках</h3>'
             '<p>На складе деталь ищут по артикулу и модели техники. Поэтому артикул — белым по чёрному, модель — сразу под названием, '
             'а сигнальная полоса видна с другого конца стеллажа. Выберите деталь.</p><div class="seg" id="lbS">'
             + "".join(f'<button type="button" data-p="{k}"{" class=on" if k == "pin" else ""}>{v[0]}</button>' for k, v in PARTS.items())
             + '</div></div></div>')

CARRIERS = [
    ("Каталог", sv(f'<rect x="120" y="20" width="240" height="320" fill="{BAS}"/>' + hazard(120, 20, 240, 18, 10) + logo(142, 64, .3, c=WHITE)
                   + f'<text x="142" y="190" font-family="{FH}" font-weight="700" font-size="34" fill="{YEL}">КАТАЛОГ</text>'
                   f'<text x="142" y="226" font-family="{FH}" font-weight="500" font-size="24" fill="#fff">2027</text>'
                   f'<text x="142" y="316" font-family="{FB}" font-size="13" fill="{STEEL}">4 800 позиций · 12 марок техники</text>'), 4),
    ("Ящик для отгрузки", sv(f'<path d="M80 130 L240 80 L400 130 L240 180 Z" fill="#c79a5b"/><path d="M80 130 L240 180 V320 L80 270 Z" fill="#b0854a"/>'
                             f'<path d="M400 130 L240 180 V320 L400 270 Z" fill="#9b7440"/>'
                             f'<g transform="translate(262 196) skewY(-17)"><rect width="110" height="70" fill="#fff"/>' + hazard(0, 0, 110, 8, 6)
                             + f'<text x="8" y="34" font-family="{FH}" font-weight="600" font-size="13" fill="{BAS}">ПР-9204-118</text>'
                             f'<text x="8" y="54" font-family="{FB}" font-size="10" fill="{BAS}">Komatsu PC400</text></g>'
                             + mark(130, 200, .6, a=BAS, b=YEL)), 4),
    ("Грузовик доставки", sv(truck(20, 110, 1.0) + f'<rect x="0" y="300" width="480" height="60" fill="#c9cdd1"/>'), 4),
    ("Каска и жилет", sv(f'<path d="M150 190 C150 110 330 110 330 190 Z" fill="{YEL}"/><rect x="130" y="186" width="220" height="18" rx="9" fill="#d9ad00"/>'
                         + mark(220, 132, .5, a=BAS, b=YEL) + f'<path d="M170 240 L210 230 L240 250 L270 230 L310 240 L318 350 H162 Z" fill="#ff7a1a"/>'
                         f'<rect x="166" y="290" width="148" height="12" fill="#e9eef2"/><rect x="166" y="316" width="148" height="12" fill="#e9eef2"/>'), 4),
    ("Визитка", sv(f'<g transform="translate(40 80)"><rect width="250" height="146" fill="{BAS}"/>' + logo(20, 30, .38, c=WHITE) + hazard(0, 134, 250, 12, 8) + '</g>'
                   f'<g transform="translate(200 150)"><rect width="250" height="146" fill="#fff"/><text x="20" y="40" font-family="{FH}" font-weight="600" font-size="20" fill="{BAS}">Олег Карпов</text>'
                   f'<text x="20" y="62" font-family="{FB}" font-size="12" fill="{STEEL}">инженер по подбору запчастей</text>'
                   f'<text x="20" y="104" font-family="{FB}" font-size="12" fill="{BAS}">+7 3842 00-00-77</text><text x="20" y="124" font-family="{FB}" font-size="12" fill="{BAS}">poroda-parts.ru</text>'
                   + mark(200, 22, .36) + '</g>'), 4),
    ("Баннер на выставку", sv(f'<rect x="150" y="10" width="180" height="340" fill="{BAS}"/>' + logo(164, 40, .25, c=WHITE)
                              + f'<text x="166" y="150" font-family="{FH}" font-weight="700" font-size="28" fill="{YEL}">ДЕТАЛЬ</text>'
                              f'<text x="166" y="184" font-family="{FH}" font-weight="700" font-size="28" fill="{YEL}">ЗА 48 ЧАСОВ</text>'
                              f'<text x="166" y="214" font-family="{FB}" font-size="12" fill="#fff">со склада в Кемерове</text>' + hazard(150, 320, 180, 30, 10)), 4),
]

CSS = """
.hero h1{font-size:clamp(44px,6vw,92px);text-transform:uppercase;letter-spacing:.01em;line-height:1.02}
.sh h2,.cta h2{text-transform:uppercase;letter-spacing:.01em;line-height:1.1}
.lb{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(24px,4vw,64px);align-items:center}
.lb-v{box-shadow:0 0 0 1px var(--line);background:#fff}.lb-v svg{width:100%;height:auto}
.lb-r h3{font-size:clamp(26px,2.6vw,38px);margin-bottom:12px;text-transform:uppercase}.lb-r p{color:var(--soft);margin-bottom:22px}
.btn,.seg,.seg button,.sw,.res,.cta{border-radius:0!important}
.seg button.on{background:var(--ac);color:var(--aci)}
@media (max-width:980px){.lb{grid-template-columns:1fr}}
"""

JS = r"""
(function(){var P=""" + str({k: list(v) for k, v in PARTS.items()}).replace("'", '"') + r""";
var s=document.getElementById('lbS');s.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
 s.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)});var p=P[b.dataset.p];
 [['lbN',0],['lbA',1],['lbF',2],['lbW',3],['lbM',4]].forEach(function(r){document.getElementById(r[0]).textContent=p[r[1]]})});
})();
"""


def cfg() -> dict:
    return {
        "slug": "design/poroda", "brand": "Порода", "favLetter": "П",
        "title": "Порода — фирменный стиль поставщика запчастей для горной техники · YSD DEV",
        "desc": "Фирменный стиль поставщика запчастей для горной техники: знак-грань, сигнальная палитра, этикетка-конструктор для склада, "
                "каталог, ящик, грузовик, каска и жилет, визитка, выставочный баннер.",
        "theme": {"bg": PAPER, "ink": BAS, "soft": "#40444a", "mut": "#6d737a", "line": "#d8dcdf", "line2": "#b9bfc4", "card": "#fff",
                  "alt": "#e3e6e8", "ac": BAS, "aci": YEL, "fh": f'"{FH}",sans-serif', "fb": f'"{FB}",sans-serif', "hw": "600", "ht": "0",
                  "cbg": BAS, "cink": WHITE, "cbtn": YEL, "cbtni": BAS, "kc": "#8a6d00", "ra": "0px", "rb": "0px", "rs": "0px", "rc": BAS},
        "fonts": [(FH, "oswald", [500, 600, 700], "normal"), (FB, "pt-sans", [400, 700], "normal")],
        "css": CSS + ".kick{text-transform:none;letter-spacing:0;font-size:15px}",
        "hero": {"kicker": "Фирменный стиль поставщика запчастей", "h1": "Видно с другого конца карьера",
                 "lead": "Знак, этикетки и носители для поставщика запчастей к экскаваторам и самосвалам из Кемерова. Стиль работает "
                         "в пыли, на морозе и в рабочих перчатках.",
                 "art": HERO, "cta": "Смотреть стиль", "go": "label"},
        "facts": [("Клиент", "«Порода», запчасти для горной техники"), ("Работа", "логотип, палитра, этикетки, 9 носителей"),
                  ("Срок", "11 рабочих дней"), ("Передали", "брендбук, шаблон этикеток для склада")],
        "sections": [
            {"type": "text3", "id": "task", "nav": "Задача", "kick": "Задача", "h2": "Поставщик, которого путали с перекупщиками",
             "items": [("Рынок", "Одинаковые прайсы", "Клиенты получают десятки предложений в одинаковых таблицах. Компанию не отличали от посредников."),
                       ("Склад", "Ошибки при отгрузке", "Самодельные этикетки, артикул мелко: детали к разным моделям путали при сборке заказа."),
                       ("Выставки", "Нужно заметить стенд", "На отраслевой выставке сотни стендов в жёлтом. Нужен свой жёлтый со своим рисунком.")]},
            {"type": "gallery", "id": "logo", "nav": "Логотип", "kick": "Логотип", "h2": "Скол породы и тяжёлое слово", "alt": True,
             "lead": "Шестигранник — и гайка, и кристалл. Грань рассекает его, как скол камня. Название набрано узким шрифтом, чтобы помещаться на борт грузовика.",
             "items": [{"html": sv(logo(50, 130, .9)), "span": 6, "cap": "<b>Основная версия</b>"},
                       {"html": sv(logo(50, 130, .9, c=WHITE), bg=BAS), "span": 6, "cap": "<b>На тёмном</b> — каталог, визитка, баннер"},
                       {"html": sv(logo(50, 130, .9, c=BAS, a=BAS, b=YEL), bg=YEL), "span": 6, "cap": "<b>На жёлтом</b> — техника и спецодежда"},
                       {"html": sv(hazard(0, 0, 480, 360, 24) + f'<rect x="150" y="90" width="180" height="180" fill="{BAS}"/>' + mark(198, 135, 1.0), bg=YEL),
                        "span": 6, "cap": "<b>Сигнальная полоса</b> со знаком — для стенда и упаковки"}]},
            {"type": "html", "id": "label", "nav": "Этикетка", "kick": "Этикетка", "h2": "Этикетка для склада", "html": LABEL_BOX},
            {"type": "palette", "id": "color", "nav": "Цвета", "kick": "Цвета", "h2": "Сигнальные цвета техники", "alt": True,
             "lead": "Жёлтый — по стандарту сигнальной окраски, базальт — цвет породы. Нажмите, чтобы скопировать код.",
             "colors": [("Сигнальный жёлтый", YEL, "техника, полосы, акценты"), ("Базальт", BAS, "основной тёмный, текст"), ("Сталь", STEEL, "второстепенный текст"),
                        ("Ржавчина", RUST, "предупреждения и скидки"), ("Бетон", PAPER, "фон документов")]},
            {"type": "type", "id": "type", "kick": "Шрифты", "h2": "Узкий заголовочный и рабочий текстовый",
             "fonts": [(FH, f"'{FH}'", "логотип, заголовки, артикулы", "ПР-9204-118 · ПАЛЕЦ КОВША", "font-weight:600"),
                       (FB, f"'{FB}'", "описания, документы, сайт", "Подходит: Komatsu PC400, PC450", "font-weight:400")]},
            {"type": "gallery", "id": "carriers", "nav": "Носители", "kick": "Носители", "h2": "От каталога до каски", "alt": True,
             "items": [{"html": h, "span": sp, "cap": f"<b>{t}</b>"} for t, h, sp in CARRIERS]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что получила компания",
             "stats": [("1 знак", "для техники, упаковки и сайта"), ("9", "носителей и шаблонов"), ("4 800", "этикеток по одному шаблону"), ("11 дней", "от брифа до брендбука")]},
        ],
        "ctaTitle": "Нужен стиль для производства?",
        "js": JS,
    }
