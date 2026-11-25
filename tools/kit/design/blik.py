"""«Блик» — фирменный стиль студии маникюра: знак-ноготь с бликом, палитра лаков, шрифты, носители, конструктор сертификата."""

CH, MILK, NUDE, GR, CHROME, PAPER = "#7a1630", "#f6e3e3", "#e3c2b1", "#231b1f", "#c9c9cf", "#fbf6f5"
FH, FB, FD = "Montserrat Alternates", "Mulish", "Jost"  # FH — только логотип: в нём кириллическая «т» похожа на «m»


def mark(x=0, y=0, s=1.0, fill=CH, hl="#fff"):
    """Ноготь с бликом: форма миндаля и короткий изогнутый отблеск."""
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M6 84 V34 C6 14 18 2 30 2 C42 2 54 14 54 34 V84 Z" style="fill:{fill}"/>'
            f'<path d="M18 30 C19 20 24 14 31 12" fill="none" style="stroke:{hl}" stroke-width="5" stroke-linecap="round"/>'
            f'<circle cx="17" cy="42" r="3" style="fill:{hl}"/></g>')


def logo(x=0, y=0, s=1.0, txt=GR, fill=CH, hl="#fff"):
    return (f'<g transform="translate({x} {y}) scale({s})">{mark(fill=fill, hl=hl)}'
            f'<text x="74" y="74" font-family="{FH}" font-weight="600" font-size="76" letter-spacing="-2" style="fill:{txt}">блик</text></g>')


def sv(body, vb="0 0 480 360", bg=MILK):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" style="fill:{bg}"/>{body}</svg>'


def bottle(x, y, s=1.0, fill=CH, name="№ 07 вишня"):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="48" y="0" width="94" height="150" rx="16" fill="{GR}"/>'
            f'<rect x="58" y="10" width="10" height="130" rx="5" fill="#fff" opacity=".12"/><rect x="62" y="146" width="66" height="22" fill="{GR}"/>'
            f'<rect x="0" y="160" width="190" height="224" rx="48" fill="{fill}"/>'
            f'<path d="M26 220 C30 192 46 178 70 174" fill="none" stroke="#fff" stroke-opacity=".38" stroke-width="10" stroke-linecap="round"/>'
            f'<text x="95" y="296" text-anchor="middle" font-family="{FH}" font-weight="600" font-size="44" fill="#fff">блик</text>'
            f'<text x="95" y="328" text-anchor="middle" font-family="{FB}" font-weight="600" font-size="15" fill="#fff" opacity=".8">{name}</text></g>')


HERO = sv('<circle cx="520" cy="110" r="190" fill="#fff" opacity=".45"/>' + bottle(60, 70, 1.0)
          + '<g transform="translate(300 250) rotate(-7)"><rect width="280" height="160" rx="14" fill="#231b1f"/>' + logo(26, 34, .5, txt="#fff", fill=MILK, hl=CH)
          + f'<text x="28" y="128" font-family="{FB}" font-size="14" fill="#c9c9cf">Большой пр. П.С., 41</text></g>'
          + f'<g transform="translate(300 96)">' + "".join(f'<circle cx="{k * 62}" cy="0" r="24" fill="{c}"/>' for k, c in enumerate([CH, NUDE, "#b9476a", GR]))
          + '</g>', "0 0 640 520", MILK)

BACKS = [("Молочный", MILK, GR, CH, "#fff"), ("Вишня", CH, "#fff", MILK, CH), ("Графит", GR, "#fff", MILK, CH), ("Нюд", NUDE, GR, CH, "#fff")]

GRID = sv('<g opacity=".55">' + "".join(f'<path d="M{x} 30 V330" stroke="#d6c2c4" stroke-dasharray="3 5"/>' for x in (96, 156, 230, 404))
          + "".join(f'<path d="M40 {y} H440" stroke="#d6c2c4" stroke-dasharray="3 5"/>' for y in (96, 180))
          + '</g>' + logo(96, 96, 1.0)
          + f'<text x="240" y="316" text-anchor="middle" font-family="{FB}" font-size="15" fill="#8f7f85">ширина знака = высота строчной «б» · отблеск под 35°</text>')

LOGO_BOX = ('<div class="lg"><div class="lg-v" id="lgV">' + sv(logo(70, 130, 1.0, txt="var(--lt)", fill="var(--lf)", hl="var(--lh)"), bg="var(--lb)") + '</div>'
            '<div class="lg-r"><h3>Знак работает на любом фоне</h3><p>Ноготь и отблеск — две простые фигуры: знак читается на аватарке 40 пикселей, '
            'на вывеске и на крышке флакона. Переключите фон.</p><div class="seg" id="lgS">'
            + "".join(f'<button type="button" data-b="{b}" data-t="{t}" data-f="{f}" data-h="{h}"{" class=on" if i == 0 else ""}>{n}</button>'
                      for i, (n, b, t, f, h) in enumerate(BACKS))
            + '</div><div class="lg-g">' + GRID + '</div></div></div>')


def phone(inner, x=150, y=18):
    return (f'<g transform="translate({x} {y})"><rect width="180" height="330" rx="28" fill="{GR}"/><rect x="8" y="8" width="164" height="314" rx="22" fill="#fff"/>'
            f'<rect x="66" y="16" width="48" height="8" rx="4" fill="{GR}"/>{inner}</g>')


CARRIERS = [
    ("Визитка", sv(f'<g transform="translate(40 70) rotate(-4)"><rect width="250" height="146" rx="12" fill="{GR}"/>' + logo(24, 34, .5, txt="#fff", fill=MILK, hl=CH) + '</g>'
                   f'<g transform="translate(200 150) rotate(5)"><rect width="250" height="146" rx="12" fill="#fff"/><text x="22" y="40" font-family="{FD}" font-weight="600" font-size="21" fill="{GR}">Алина Мирова</text>'
                   f'<text x="22" y="62" font-family="{FB}" font-size="13" fill="#8f7f85">мастер маникюра</text><text x="22" y="106" font-family="{FB}" font-size="13" fill="{GR}">запись: blik.studio</text>'
                   f'<text x="22" y="126" font-family="{FB}" font-size="13" fill="{GR}">+7 812 000-00-41</text>' + mark(206, 22, .36) + '</g>'), 4, "4/3"),
    ("Вывеска", sv(f'<rect x="0" y="0" width="480" height="360" fill="#8d8f94"/><rect x="0" y="230" width="480" height="130" fill="#6f7176"/>'
                   + "".join(f'<rect x="{30 + k * 110}" y="140" width="80" height="200" fill="#3d3f44"/>' for k in range(4))
                   + f'<rect x="40" y="40" width="400" height="80" rx="10" fill="{GR}"/>' + logo(150, 50, .74, txt="#fff", fill=MILK, hl=CH)
                   + '<rect x="40" y="118" width="400" height="6" fill="#000" opacity=".25"/>', bg="#8d8f94"), 4, "4/3"),
    ("Аватар и сторис", sv(f'<circle cx="92" cy="180" r="62" fill="{CH}"/>' + mark(66, 136, 1.0, fill=MILK, hl=CH)
                           + phone(f'<rect x="8" y="8" width="164" height="314" rx="22" fill="{CH}"/>' + logo(20, 70, .52, txt="#fff", fill=MILK, hl=CH)
                                   + f'<text x="22" y="170" font-family="{FD}" font-weight="600" font-size="23" fill="#fff">Окна на</text>'
                                     f'<text x="22" y="196" font-family="{FD}" font-weight="600" font-size="23" fill="#fff">субботу</text>'
                                   + "".join(f'<rect x="22" y="{216 + k * 26}" width="136" height="20" rx="10" fill="#fff" opacity="{.95 - k * .3}"/>'
                                             f'<text x="34" y="{230 + k * 26}" font-family="{FB}" font-weight="700" font-size="11" fill="{CH}">{t}</text>'
                                             for k, t in enumerate(["11:00 · Алина", "14:30 · Вера", "18:00 · Алина"])), 230, 16)), 4, "4/3"),
    ("Прайс-лист A5", sv(f'<rect x="96" y="20" width="288" height="320" fill="#fff"/>' + logo(118, 40, .4)
                         + "".join(f'<text x="118" y="{124 + k * 34}" font-family="{FB}" font-size="13" fill="{GR}">{a}</text>'
                                   f'<text x="362" y="{124 + k * 34}" text-anchor="end" font-family="{FD}" font-weight="600" font-size="14" fill="{GR}">{b}</text>'
                                   f'<path d="M118 {132 + k * 34} H362" stroke="#eadcdc"/>'
                                   for k, (a, b) in enumerate([("Маникюр без покрытия", "1 400 ₽"), ("Маникюр + гель-лак", "2 600 ₽"), ("Укрепление", "+500 ₽"),
                                                               ("Педикюр + покрытие", "3 200 ₽"), ("Снятие и уход", "700 ₽"), ("Френч и дизайн", "от 300 ₽")]))
                         + f'<rect x="118" y="318" width="244" height="6" rx="3" fill="{CH}"/>'), 4, "4/3"),
    ("Пакет", sv(f'<path d="M180 70 C180 30 300 30 300 70" fill="none" stroke="{GR}" stroke-width="8"/><rect x="130" y="70" width="220" height="270" rx="6" fill="{NUDE}"/>'
                 + mark(214, 140, 1.0) + f'<text x="240" y="290" text-anchor="middle" font-family="{FH}" font-weight="600" font-size="30" fill="{GR}">блик</text>'), 4, "4/3"),
    ("Карта постоянной гостьи", sv(f'<g transform="translate(90 90)"><rect width="300" height="180" rx="16" fill="{CH}"/>' + logo(22, 20, .36, txt="#fff", fill=MILK, hl=CH)
                                   + f'<text x="22" y="92" font-family="{FB}" font-size="13" fill="#fff" opacity=".85">шестой маникюр — в подарок</text>'
                                   + "".join(f'<circle cx="{40 + k * 46}" cy="136" r="16" fill="{"#fff" if k < 3 else "none"}" stroke="#fff" stroke-width="2"/>' for k in range(6))
                                   + "".join(mark(32 + k * 46, 124, .27) for k in range(3)) + '</g>'), 4, "4/3"),
]

CERT = sv(f'<rect x="40" y="50" width="400" height="260" rx="18" style="fill:var(--cb)"/>'
          + logo(68, 78, .44, txt="var(--ct)", fill="var(--cf)", hl="var(--cb)")
          + f'<text x="68" y="190" font-family="{FB}" font-weight="600" font-size="16" style="fill:var(--ct)" opacity=".8">подарочный сертификат</text>'
          + f'<text x="68" y="252" font-family="{FD}" font-weight="600" font-size="60" letter-spacing="-1" style="fill:var(--ct)" id="cSum">3 000 ₽</text>'
          + f'<text x="412" y="286" text-anchor="end" font-family="{FB}" font-size="13" style="fill:var(--ct)" opacity=".7" id="cTill">действует до 31 мая 2027</text>'
          + '<path d="M300 50 C330 120 330 240 300 310" fill="none" stroke="#fff" stroke-opacity=".14" stroke-width="28"/>', bg=MILK)

CERT_BOX = ('<div class="ct"><div class="ct-v" id="ctV" style="--cb:#7a1630;--ct:#fff;--cf:#f6e3e3">' + CERT + '</div><div class="ct-r">'
            '<h3>Сертификат собирается за минуту</h3><p>Администратор выбирает сумму и цвет — макет сразу готов к печати и отправке в мессенджер.</p>'
            '<small>Сумма</small><div class="seg" id="ctS">' + "".join(f'<button type="button" data-v="{v}"{" class=on" if v == "3 000" else ""}>{v} ₽</button>'
                                                                       for v in ("2 000", "3 000", "5 000", "7 000"))
            + '</div><small>Цвет</small><div class="seg" id="ctC">' + "".join(
                f'<button type="button" data-b="{b}" data-t="{t}" data-f="{f}"{" class=on" if i == 0 else ""}>{n}</button>'
                for i, (n, b, t, f) in enumerate([("Вишня", CH, "#fff", MILK), ("Графит", GR, "#fff", MILK), ("Нюд", NUDE, GR, CH)])) + '</div></div></div>')

CSS = """
.hero h1{font-size:clamp(42px,5.6vw,84px)}
.lg,.ct{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(24px,4vw,64px);align-items:center}
.lg-v,.ct-v{border-radius:20px;overflow:hidden;box-shadow:0 0 0 1px var(--line)}
.lg-v svg,.ct-v svg,.lg-g svg{width:100%;height:auto}
.lg-r h3,.ct-r h3{font-size:clamp(26px,2.6vw,38px);margin-bottom:12px}.lg-r p,.ct-r p{color:var(--soft);margin-bottom:20px}
.lg-g{margin-top:22px;border-radius:14px;overflow:hidden;box-shadow:0 0 0 1px var(--line)}
.ct-r small{display:block;color:var(--mut);font-size:14px;margin:16px 0 8px}
.seg button{font-size:15px}
@media (max-width:980px){.lg,.ct{grid-template-columns:1fr}}
"""

JS = r"""
(function(){
function seg(id,fn){var s=document.getElementById(id);s.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
 s.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)});fn(b)})}
var v=document.getElementById('lgV');function lg(b){v.style.setProperty('--lb',b.dataset.b);v.style.setProperty('--lt',b.dataset.t);v.style.setProperty('--lf',b.dataset.f);v.style.setProperty('--lh',b.dataset.h)}
lg(document.querySelector('#lgS button'));seg('lgS',lg);
var c=document.getElementById('ctV');seg('ctS',function(b){document.getElementById('cSum').textContent=b.dataset.v+' ₽'});
seg('ctC',function(b){c.style.setProperty('--cb',b.dataset.b);c.style.setProperty('--ct',b.dataset.t);c.style.setProperty('--cf',b.dataset.f)});
})();
"""


def cfg() -> dict:
    return {
        "slug": "design/blik", "brand": "Блик", "favLetter": "Б",
        "layout": 'frame', "header": 'bar', "secHead": 'stack', "resStyle": 'line', "ctaStyle": 'block',  # layout
        "title": "Блик — фирменный стиль студии маникюра · YSD DEV",
        "desc": "Фирменный стиль студии маникюра: знак-ноготь с бликом, палитра лаков, шрифты, визитка, вывеска, сторис, прайс, "
                "карта постоянной гостьи и конструктор подарочного сертификата.",
        "theme": {"bg": PAPER, "ink": GR, "soft": "#5d4d53", "mut": "#8f7f85", "line": "#eadcdc", "line2": "#d6c2c4", "card": "#fff",
                  "alt": "#f6e9e8", "ac": CH, "aci": "#fff", "fh": f'"{FD}",sans-serif', "fb": f'"{FB}",sans-serif', "hw": "500", "ht": "-.02em",
                  "cbg": GR, "cink": PAPER, "kc": CH},
        "fonts": [(FH, "montserrat-alternates", [600], "normal"), (FD, "jost", [500, 600], "normal"), (FB, "mulish", [400, 600, 700], "normal")],
        "css": CSS + ".kick{text-transform:none;letter-spacing:0;font-size:15px}",
        "hero": {"kicker": "Фирменный стиль студии маникюра", "h1": "Стиль, который узнают по одному ногтю",
                 "lead": "Логотип, палитра лаков и двенадцать носителей для студии на Петроградской. Задача — уйти от розовых завитушек и "
                         "выглядеть как место, где покрытие держится три недели.",
                 "art": HERO, "cta": "Смотреть стиль", "go": "logo"},
        "facts": [("Клиент", "«Блик», студия маникюра"), ("Работа", "логотип, палитра, шрифты, 12 носителей"),
                  ("Срок", "9 рабочих дней"), ("Передали", "брендбук в PDF и исходники")],
        "sections": [
            {"type": "text3", "id": "task", "nav": "Задача", "kick": "Задача", "h2": "Что мешало студии раньше",
             "items": [("Конкуренты", "Все розовые и с вензелями", "На одной улице четыре студии с похожими вывесками. Прохожий не запоминает, в какую заходил."),
                       ("Клиентки", "Выбирают по аккуратности", "Им важно, что мастер не спешит и покрытие не сколется. Стиль должен говорить об этом, а не о «роскоши»."),
                       ("Мастера", "Делают сторис сами", "Нужны шаблоны, которые мастер заполняет с телефона за минуту и не ломает стиль.")]},
            {"type": "html", "id": "logo", "nav": "Логотип", "kick": "Логотип", "h2": "Ноготь и отблеск на нём", "html": LOGO_BOX, "alt": True},
            {"type": "palette", "id": "color", "nav": "Цвета", "kick": "Цвета", "h2": "Палитра из реальных лаков",
             "lead": "Цвета подобраны по флаконам, которыми работают мастера. Нажмите, чтобы скопировать код.",
             "colors": [("Вишнёвый лак", CH, "акцент: знак, кнопки, сертификат"), ("Молочный розовый", MILK, "основной фон"),
                        ("Нюд", NUDE, "упаковка и подложки"), ("Графит", GR, "текст, вывеска, визитка"), ("Хром", CHROME, "второстепенный текст на тёмном")]},
            {"type": "type", "id": "type", "kick": "Шрифты", "h2": "Геометрия в заголовках, мягкость в тексте", "alt": True,
             "fonts": [(FH, f"'{FH}'", "только логотип", "блик", "font-weight:600"), (FD, f"'{FD}'", "заголовки и цифры", "Окна на субботу", "font-weight:500"),
                       (FB, f"'{FB}'", "прайс, тексты, подписи", "Маникюр + гель-лак — 2\u00a0600\u00a0₽", "font-weight:400")]},
            {"type": "gallery", "id": "carriers", "nav": "Носители", "kick": "Носители", "h2": "От визитки до вывески",
             "items": [{"html": h, "span": sp, "ar": ar, "cap": f"<b>{t}</b>"} for t, h, sp, ar in CARRIERS]},
            {"type": "html", "id": "cert", "nav": "Сертификат", "kick": "Сертификат", "h2": "Подарочный сертификат", "html": CERT_BOX, "alt": True},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что получила студия",
             "stats": [("1 знак", "и три версии логотипа"), ("12", "носителей в одном стиле"), ("6", "шаблонов сторис для мастеров"), ("9 дней", "от брифа до брендбука")]},
        ],
        "ctaTitle": "Нужен стиль, который запоминают?",
        "js": JS,
    }
