"""«Ось» — фирменный стиль студии дизайна интерьера: знак-план, палитра материалов, шрифты, носители, план со слоями."""

CON, GRN, OAK, INK, WHITE, BRASS = "#d9dbd6", "#24392f", "#b8916a", "#161816", "#f4f4f1", "#a88a5a"
FH, FB = "Tenor Sans", "Overpass"


def mark(x=0, y=0, s=1.0, c=INK, a=OAK):
    """Квадрат плана с осью, смещённой по золотому сечению."""
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="2" y="2" width="76" height="76" fill="none" style="stroke:{c}" stroke-width="4"/>'
            f'<path d="M49 2 V78" style="stroke:{c}" stroke-width="4"/><circle cx="49" cy="49" r="7" style="fill:{a}"/></g>')


def logo(x=0, y=0, s=1.0, c=INK, a=OAK, sub=True):
    t = (f'<g transform="translate({x} {y}) scale({s})">{mark(c=c, a=a)}<text x="104" y="62" font-family="{FH}" font-size="64" letter-spacing="10" '
         f'style="fill:{c}">ОСЬ</text>')
    if sub:
        t += f'<text x="107" y="84" font-family="{FB}" font-size="13" letter-spacing="3" style="fill:{c}" opacity=".7">ДИЗАЙН ИНТЕРЬЕРА</text>'
    return t + "</g>"


def sv(body, vb="0 0 480 360", bg=WHITE):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" style="fill:{bg}"/>{body}</svg>'


def swatch(x, y, w, h, fill, label, dark=False):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>'
            f'<text x="{x + 12}" y="{y + h - 14}" font-family="{FB}" font-size="13" fill="{"#fff" if dark else INK}">{label}</text>')


HERO = sv(swatch(0, 0, 330, 520, GRN, "", True) + swatch(330, 0, 310, 300, CON, "бетон, затирка") + swatch(330, 300, 160, 220, OAK, "дуб, масло")
          + swatch(490, 300, 150, 220, BRASS, "латунь", True) + logo(40, 214, .82, c=WHITE, a=OAK)
          + f'<text x="44" y="470" font-family="{FB}" font-size="15" fill="#fff" opacity=".7">Москва, Хамовники · с 2018 года</text>', "0 0 640 520")

ROOMS = [  # x, y, w, h, подпись, площадь
    (40, 40, 220, 170, "Гостиная", "24,6 м²"), (260, 40, 180, 110, "Спальня", "14,2 м²"), (260, 150, 180, 60, "Ванная", "5,1 м²"),
    (40, 210, 140, 110, "Кухня", "9,8 м²"), (180, 210, 260, 110, "Прихожая", "7,4 м²")]
PLAN = ('<svg viewBox="0 0 480 360" xmlns="http://www.w3.org/2000/svg"><rect width="480" height="360" fill="#fff"/>'
        + "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{INK}" stroke-width="5"/>' for x, y, w, h, *_ in ROOMS)
        + '<g class="ly" data-l="furn">'
        + f'<rect x="60" y="150" width="120" height="44" rx="6" fill="{CON}"/><rect x="190" y="70" width="40" height="40" rx="20" fill="{OAK}" opacity=".6"/>'
        + f'<rect x="300" y="56" width="90" height="70" rx="4" fill="{CON}"/><rect x="56" y="222" width="110" height="24" fill="{OAK}" opacity=".6"/>'
        + f'<rect x="372" y="160" width="56" height="40" rx="18" fill="#fff" stroke="{INK}"/></g>'
        + '<g class="ly" data-l="light">' + "".join(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{BRASS}"/><circle cx="{cx}" cy="{cy}" r="16" fill="none" stroke="{BRASS}" stroke-dasharray="3 3"/>'
                                                for cx, cy in [(80, 80), (410, 70), (70, 236), (420, 240), (290, 180)]) + '</g>'
        + '<g class="ly" data-l="dim" font-family="Overpass" font-size="12" fill="#5b6560">'
        + "".join(f'<text x="{x + w / 2}" y="{y + h / 2 + 4}" text-anchor="middle">{n}, {a}</text>' for x, y, w, h, n, a in ROOMS)
        + f'<path d="M40 28 H440" stroke="{GRN}"/><text x="240" y="22" text-anchor="middle" fill="{GRN}">11 400</text>'
        + f'<path d="M454 40 V320" stroke="{GRN}"/><text x="468" y="184" text-anchor="middle" fill="{GRN}" transform="rotate(90 468 184)">7 200</text></g>'
        + f'<g transform="translate(330 330)"><rect width="140" height="24" fill="{GRN}"/>' + mark(6, 4, .2, c="#fff", a=OAK)
        + f'<text x="30" y="17" font-family="{FB}" font-size="11" fill="#fff">ОСЬ · лист 3 из 18</text></g></svg>')

PLAN_BOX = ('<div class="pl"><div class="pl-v" id="plV">' + PLAN + '</div><div class="pl-r"><h3>Стиль работает и на чертежах</h3>'
            '<p>Рабочий проект — главное, что студия отдаёт клиенту. Штамп, цвета слоёв и подписи на планах — тоже часть фирменного стиля. '
            'Включайте слои, как на встрече с заказчиком.</p><div class="pl-l" id="plL">'
            + "".join(f'<label><input type="checkbox" value="{v}" checked><span>{n}</span></label>' for v, n in [("furn", "Мебель"), ("light", "Свет"), ("dim", "Размеры и площади")])
            + '</div></div></div>')

CARRIERS = [
    ("Визитки", sv(f'<g transform="translate(46 70)"><rect width="250" height="146" fill="{GRN}"/>' + logo(26, 34, .5, c=WHITE, a=OAK) + '</g>'
                   f'<g transform="translate(190 160)"><rect width="250" height="146" fill="#fff" stroke="#e3e4df"/>'
                   f'<text x="22" y="44" font-family="{FH}" font-size="19" fill="{INK}">Вера Остапенко</text><text x="22" y="66" font-family="{FB}" font-size="12" fill="#6b716d">архитектор, основатель</text>'
                   f'<text x="22" y="112" font-family="{FB}" font-size="12" fill="{INK}">os-studio.ru</text><text x="22" y="130" font-family="{FB}" font-size="12" fill="{INK}">+7 495 000-00-18</text>'
                   + mark(196, 22, .38) + '</g>', bg=CON), 4),
    ("Обложка проекта", sv(f'<rect x="90" y="24" width="300" height="312" fill="#fff"/><rect x="90" y="24" width="300" height="180" fill="{GRN}"/>'
                           + mark(116, 50, .5, c=WHITE) + f'<text x="116" y="248" font-family="{FH}" font-size="26" fill="{INK}">Квартира</text>'
                           f'<text x="116" y="280" font-family="{FH}" font-size="26" fill="{INK}">на Пречистенке</text>'
                           f'<text x="116" y="314" font-family="{FB}" font-size="12" fill="#6b716d">рабочий проект · 86 м² · 2026</text>', bg=CON), 4),
    ("Табличка у входа", sv(f'<rect width="480" height="360" fill="#8b8a84"/><rect x="0" y="0" width="480" height="360" fill="url(#brk)"/>'
                            f'<defs><pattern id="brk" width="60" height="26" patternUnits="userSpaceOnUse"><path d="M0 25 H60 M30 0 V13 M0 13 H60 M0 0 V13" stroke="#77766f" stroke-width="2"/></pattern></defs>'
                            f'<rect x="120" y="90" width="240" height="180" fill="{BRASS}"/><rect x="126" y="96" width="228" height="168" fill="none" stroke="#c9ab77"/>'
                            + logo(150, 150, .58, c=INK, a=GRN), bg="#8b8a84"), 4),
    ("Коробка образцов", sv(f'<path d="M90 140 L240 90 L390 140 L240 190 Z" fill="{OAK}"/><path d="M90 140 L240 190 V320 L90 270 Z" fill="{GRN}"/>'
                            f'<path d="M390 140 L240 190 V320 L390 270 Z" fill="#1c2e25"/>' + mark(140, 205, .5, c=WHITE)
                            + f'<text x="300" y="250" font-family="{FB}" font-size="13" fill="#fff" opacity=".8" transform="skewY(-18) translate(0 96)">образцы</text>', bg=CON), 4),
    ("Сетка постов", sv("".join(f'<rect x="{90 + (k % 3) * 102}" y="{24 + (k // 3) * 102}" width="98" height="98" fill="{c}"/>'
                                for k, c in enumerate([GRN, CON, OAK, CON, INK, CON, OAK, CON, GRN])) + mark(115, 49, .6, c=WHITE)
                        + f'<text x="339" y="80" text-anchor="middle" font-family="{FH}" font-size="14" fill="{INK}">до / после</text>'
                        + f'<text x="237" y="182" text-anchor="middle" font-family="{FH}" font-size="14" fill="#fff">86 м²</text>'
                        + f'<text x="339" y="284" text-anchor="middle" font-family="{FH}" font-size="13" fill="{INK}">совет недели</text>', bg=WHITE), 4),
    ("Бланк сметы", sv(f'<rect x="110" y="20" width="260" height="320" fill="#fff"/>' + logo(130, 40, .32, sub=False)
                       + "".join(f'<text x="130" y="{122 + k * 30}" font-family="{FB}" font-size="12" fill="{INK}">{a}</text>'
                                 f'<text x="350" y="{122 + k * 30}" text-anchor="end" font-family="{FB}" font-weight="700" font-size="12" fill="{INK}">{b}</text>'
                                 f'<path d="M130 {130 + k * 30} H350" stroke="#e3e4df"/>'
                                 for k, (a, b) in enumerate([("Обмерный план", "18 000 ₽"), ("Планировочное решение", "42 000 ₽"), ("Визуализации, 6 шт.", "96 000 ₽"),
                                                             ("Рабочие чертежи", "120 000 ₽"), ("Комплектация", "по договору"), ("Итого", "276 000 ₽")]))
                       + f'<rect x="130" y="310" width="220" height="4" fill="{GRN}"/>', bg=CON), 4),
]

CSS = """
.hero h1{font-size:clamp(40px,5.2vw,78px);font-weight:400}
.sh h2,.cta h2{font-weight:400}
.pl{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:clamp(24px,4vw,64px);align-items:center}
.pl-v{border-radius:6px;overflow:hidden;box-shadow:0 0 0 1px var(--line)}.pl-v svg{width:100%;height:auto}
.pl-v .ly{transition:opacity .35s}.pl-v .ly.off{opacity:0}
.pl-r h3{font-size:clamp(26px,2.6vw,38px);font-weight:400;margin-bottom:12px}.pl-r p{color:var(--soft);margin-bottom:22px}
.pl-l{display:grid;gap:10px}.pl-l label{display:flex;align-items:center;gap:12px;padding:14px 16px;background:var(--card);box-shadow:0 0 0 1px var(--line);cursor:pointer;font-size:16px}
.pl-l input{width:20px;height:20px;accent-color:var(--ac)}
.btn,.seg,.seg button{border-radius:2px}
@media (max-width:980px){.pl{grid-template-columns:1fr}}
"""

JS = r"""
(function(){var v=document.getElementById('plV');document.getElementById('plL').addEventListener('change',function(e){var i=e.target;
 v.querySelectorAll('.ly[data-l="'+i.value+'"]').forEach(function(g){g.classList.toggle('off',!i.checked)})})})();
"""


def cfg() -> dict:
    return {
        "slug": "design/os", "brand": "Ось", "favLetter": "О",
        "layout": 'index', "header": 'float', "secHead": 'split', "resStyle": 'band', "ctaStyle": 'line',  # layout
        "title": "Ось — фирменный стиль студии дизайна интерьера · YSD DEV",
        "desc": "Фирменный стиль студии дизайна интерьера: знак-план, палитра из отделочных материалов, шрифты, визитки, обложка проекта, "
                "табличка, коробка образцов, смета и чертёж со слоями.",
        "theme": {"bg": WHITE, "ink": INK, "soft": "#4c534f", "mut": "#7c827e", "line": "#e3e4df", "line2": "#c9cbc4", "card": "#fff",
                  "alt": "#eceee9", "ac": GRN, "aci": "#fff", "fh": f'"{FH}",serif', "fb": f'"{FB}",sans-serif', "hw": "400", "ht": "-.01em",
                  "cbg": GRN, "cink": WHITE, "cbtn": OAK, "cbtni": INK, "kc": GRN, "ra": "4px", "rb": "2px", "rs": "4px"},
        "fonts": [(FH, "tenor-sans", [400], "normal"), (FB, "overpass", [400, 600, 700], "normal")],
        "css": CSS + ".kick{text-transform:none;letter-spacing:0;font-size:15px}",
        "hero": {"kicker": "Фирменный стиль студии дизайна интерьера", "h1": "Стиль, собранный из тех же материалов, что и интерьеры",
                 "lead": "Знак, палитра и носители для студии из Хамовников. Цвета взяли с образцов, которые архитекторы приносят на встречи: "
                         "бетон, дуб, латунь и глубокий зелёный.",
                 "art": HERO, "cta": "Смотреть стиль", "go": "logo"},
        "facts": [("Клиент", "«Ось», студия дизайна интерьера"), ("Работа", "нейминг, логотип, палитра, 10 носителей"),
                  ("Срок", "12 рабочих дней"), ("Передали", "брендбук, шаблоны презентаций и штамп чертежей")],
        "sections": [
            {"type": "text3", "id": "task", "nav": "Задача", "kick": "Задача", "h2": "Студия росла, а выглядела как фрилансер",
             "items": [("Название", "Его не было", "Работали под фамилией основателя. Нужно короткое имя, которое не спутать с мебельным салоном."),
                       ("Клиенты", "Платят за порядок", "Заказчики ценят, что проект продуман до розетки. Стиль должен говорить о точности, а не о «роскоши»."),
                       ("Документы", "Каждый делал по-своему", "Сметы, планы и презентации выглядели по-разному. Нужны шаблоны, которые архитектор заполняет сам.")]},
            {"type": "gallery", "id": "logo", "nav": "Логотип", "kick": "Логотип", "h2": "План комнаты и ось через неё", "alt": True,
             "lead": "Знак — квадрат плана, разделённый осью в пропорции золотого сечения. Точка на пересечении — место, откуда начинается проект.",
             "items": [{"html": sv(logo(70, 130, 1.0)), "span": 6, "cap": "<b>Основная версия</b> на светлом"},
                       {"html": sv(logo(70, 130, 1.0, c=WHITE, a=OAK), bg=GRN), "span": 6, "cap": "<b>На зелёном</b> — обложки и вывески"},
                       {"html": sv(mark(160, 100, 2.0)), "span": 4, "cap": "<b>Знак</b> для аватара и штампа"},
                       {"html": sv(logo(70, 140, 1.0, c=INK, a=INK), bg=CON), "span": 4, "cap": "<b>Монохром</b> для печати и гравировки"},
                       {"html": sv(logo(84, 140, .9, c=INK, a=GRN, sub=False), bg=OAK), "span": 4, "cap": "<b>Без подписи</b> на мелких носителях"}]},
            {"type": "palette", "id": "color", "nav": "Цвета", "kick": "Цвета", "h2": "Палитра из отделочных материалов",
             "lead": "Каждый цвет назван по материалу, с которым его сверяли. Нажмите, чтобы скопировать код.",
             "colors": [("Глубокий зелёный", GRN, "главный цвет: обложки, вывеска"), ("Бетон", CON, "фон документов"), ("Дуб", OAK, "акцент и точка в знаке"),
                        ("Латунь", BRASS, "свет на планах, табличка"), ("Графит", INK, "текст и линии чертежей"), ("Известь", WHITE, "фон сайта")]},
            {"type": "type", "id": "type", "kick": "Шрифты", "h2": "Строгая антиква без засечек и технический гротеск", "alt": True,
             "fonts": [(FH, f"'{FH}'", "логотип и заголовки", "Квартира на Пречистенке", ""),
                       (FB, f"'{FB}'", "чертежи, сметы, тексты", "Гостиная, 24,6 м²", "font-weight:400")]},
            {"type": "html", "id": "plan", "nav": "Чертежи", "kick": "Чертежи", "h2": "План со слоями", "html": PLAN_BOX},
            {"type": "gallery", "id": "carriers", "nav": "Носители", "kick": "Носители", "h2": "Шесть носителей из десяти", "alt": True,
             "items": [{"html": h, "span": sp, "cap": f"<b>{t}</b>"} for t, h, sp in CARRIERS]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что получила студия",
             "stats": [("1 имя", "и знак, который не спутать"), ("10", "носителей и шаблонов"), ("1 штамп", "для всех чертежей проекта"), ("12 дней", "от брифа до брендбука")]},
        ],
        "ctaTitle": "Нужен стиль для студии?",
        "js": JS,
    }
