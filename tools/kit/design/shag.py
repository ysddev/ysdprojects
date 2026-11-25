"""«Шаг» — оформление сообщества ВКонтакте для студии танцев: обложка с безопасными зонами, аватар, меню, обложки услуг, посты и сторис."""

UM, PINK, SUN, INK, WHITE, LIL = "#2b1cff", "#ff3d8b", "#ffd23f", "#140f33", "#ffffff", "#e9e6ff"
F = "Rubik"


def sv(body, vb="0 0 480 360", bg=UM):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" style="fill:{bg}"/>{body}</svg>'


def foot(x, y, c):
    return (f'<g transform="translate({x} {y})"><ellipse cx="30" cy="66" rx="19" ry="32" style="fill:{c}"/>'
            + "".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" style="fill:{c}"/>' for cx, cy, r in [(13, 22, 6.5), (25, 15, 6.5), (37, 15, 5.5), (48, 22, 5)]) + "</g>")


def steps(x, y, s=1.0, c=PINK, c2=SUN):
    """Знак: два следа, второй — на шаг впереди и выше."""
    return f'<g transform="translate({x} {y}) scale({s})">{foot(0, 10, c)}{foot(58, -34, c2)}</g>'


def word(x, y, s=1.0, c=WHITE):
    return f'<text x="{x}" y="{y}" font-family="{F}" font-weight="900" font-style="italic" font-size="{120 * s:.0f}" letter-spacing="-4" style="fill:{c}">шаг</text>'


def dancer(x, y, s=1.0, c=WHITE):
    """Силуэт в прыжке: голова, корпус, руки и ноги — толстыми линиями."""
    return (f'<g transform="translate({x} {y}) scale({s})" style="stroke:{c}" stroke-width="22" stroke-linecap="round" fill="none">'
            f'<circle cx="120" cy="30" r="24" style="fill:{c}" stroke="none"/><path d="M118 62 L104 160"/><path d="M114 84 L40 40"/><path d="M116 88 L196 64"/>'
            f'<path d="M104 160 L40 190 L6 250"/><path d="M104 160 L170 200 L230 176"/></g>')


COVER = sv(f'<circle cx="1500" cy="380" r="420" fill="{PINK}"/><circle cx="1720" cy="110" r="140" fill="{SUN}"/>' + dancer(1300, 170, 1.5)
           + steps(300, 250, 2.2) + word(560, 430, 1.9) + f'<text x="566" y="520" font-family="{F}" font-weight="500" font-size="44" fill="{WHITE}">студия танцев в Люберцах</text>'
           + f'<rect x="566" y="560" width="420" height="78" rx="39" fill="{SUN}"/><text x="776" y="612" text-anchor="middle" font-family="{F}" font-weight="700" font-size="34" fill="{INK}">первое занятие — 0 ₽</text>'
           + '<g class="safe"><rect x="296" y="0" width="1328" height="768" fill="none" stroke="#fff" stroke-width="6" stroke-dasharray="24 16"/>'
             '<rect x="0" y="0" width="296" height="768" fill="#000" opacity=".45"/><rect x="1624" y="0" width="296" height="768" fill="#000" opacity=".45"/>'
             f'<text x="1600" y="740" text-anchor="end" font-family="{F}" font-size="30" fill="#fff">видно на телефоне</text></g>', "0 0 1920 768")

TILES = [("Расписание", UM, WHITE), ("Направления", PINK, WHITE), ("Цены", SUN, INK), ("Первое занятие", WHITE, UM), ("Педагоги", INK, WHITE), ("Концерты", LIL, UM)]


def tile(n, bg, ink, k):
    deco = [f'<path d="M24 196 H352" stroke="{ink}" stroke-width="3" opacity=".3"/>' + "".join(f'<rect x="{24 + j * 56}" y="{150 - j * 18}" width="40" height="{40 + j * 18}" rx="6" fill="{ink}" opacity=".25"/>' for j in range(6)),
            dancer(250, 40, .55, ink), f'<text x="352" y="200" text-anchor="end" font-family="{F}" font-weight="900" font-size="80" fill="{ink}" opacity=".25">₽</text>',
            f'<text x="352" y="200" text-anchor="end" font-family="{F}" font-weight="900" font-style="italic" font-size="96" fill="{PINK}">0 ₽</text>',
            f'<circle cx="300" cy="80" r="44" fill="{PINK}"/><circle cx="250" cy="120" r="44" fill="{SUN}"/>', steps(270, 90, .8, UM, PINK)][k]
    return (f'<svg viewBox="0 0 376 256" xmlns="http://www.w3.org/2000/svg"><rect width="376" height="256" rx="18" fill="{bg}"/>{deco}'
            f'<text x="24" y="236" font-family="{F}" font-weight="800" font-size="30" fill="{ink}">{n}</text></svg>')


MENU = '<div class="vk-menu">' + "".join(f'<div>{tile(n, b, i, k)}</div>' for k, (n, b, i) in enumerate(TILES)) + "</div>"


def page(mode):
    """Страница сообщества: обложка, аватар, кнопки, меню, пост — без логотипов соцсети, только раскладка."""
    return (f'<div class="vk vk-{mode}"><div class="vk-cov">{COVER}</div><div class="vk-head"><div class="vk-ava">'
            + sv(steps(28, 40, 1.0), "0 0 160 160", UM) + '</div><div><b>Студия танцев «Шаг»</b><span>Люберцы · 2 340 участников</span></div>'
            '<div class="vk-btn"><i>Записаться</i><i>Написать</i></div></div>' + MENU + "</div>")


VK_BOX = ('<div class="vkw"><div class="seg" id="vkS"><button type="button" class="on" data-m="d">Компьютер</button><button type="button" data-m="m">Телефон</button>'
          '<button type="button" data-m="z">Безопасные зоны</button></div><div class="vk-stage" id="vkV">' + page("d") + "</div></div>")


def post(title, sub, bg, ink, extra=""):
    return sv(extra + f'<text x="40" y="300" font-family="{F}" font-weight="900" font-style="italic" font-size="46" letter-spacing="-1" fill="{ink}">{title}</text>'
              f'<text x="42" y="340" font-family="{F}" font-weight="500" font-size="22" fill="{ink}" opacity=".85">{sub}</text>' + steps(400, 40, .5, ink, SUN if bg != SUN else PINK),
              "0 0 480 400", bg)


POSTS = [
    ("Анонс", post("Батл 14 декабря", "вход свободный · зал на Октябрьском", PINK, WHITE, dancer(150, 20, .9, WHITE))),
    ("Расписание недели", post("Неделя", "пн–вс · 6 направлений", WHITE, UM, "".join(
        f'<rect x="40" y="{30 + k * 40}" width="400" height="32" rx="8" fill="{LIL}"/><text x="56" y="{52 + k * 40}" font-family="{F}" font-weight="700" font-size="17" fill="{UM}">{t}</text>'
        for k, t in enumerate(["Пн 18:00 · хип-хоп, дети 7–10", "Вт 19:30 · contemporary", "Ср 18:00 · брейк-данс", "Чт 20:00 · high heels", "Сб 12:00 · семейный класс"])))),
    ("Знакомьтесь, педагог", post("Аня, хип-хоп", "12 лет в танце · ведёт группы 7–14 лет", SUN, INK, f'<circle cx="160" cy="130" r="100" fill="{UM}"/>' + dancer(80, 40, .7, SUN))),
]

STORY = ('<div class="story">' + sv(f'<rect width="270" height="480" fill="{UM}"/><circle cx="220" cy="90" r="120" fill="{PINK}"/>' + dancer(40, 60, .9)
                                     + f'<text x="22" y="360" font-family="{F}" font-weight="900" font-style="italic" font-size="44" fill="{WHITE}">Есть</text>'
                                     f'<text x="22" y="404" font-family="{F}" font-weight="900" font-style="italic" font-size="44" fill="{SUN}">3 места</text>'
                                     f'<rect x="22" y="424" width="226" height="40" rx="20" fill="{WHITE}"/><text x="135" y="450" text-anchor="middle" font-family="{F}" font-weight="700" font-size="16" fill="{UM}">в группу на вторник</text>',
                                     "0 0 270 480") + "</div>")

CSS = """
.hero h1{font-size:clamp(42px,5.6vw,86px);font-style:italic;font-weight:900;letter-spacing:-.03em}
.sh h2,.cta h2{font-style:italic;font-weight:900}
.vkw .seg{margin-bottom:20px}
.vk-stage{display:grid;place-items:center}
.vk{background:#fff;border-radius:16px;overflow:hidden;box-shadow:0 30px 60px -40px rgba(20,15,51,.5),0 0 0 1px var(--line);transition:max-width .4s;width:100%;max-width:1000px}
.vk-m{max-width:390px}
.vk-cov svg{width:100%;height:auto;display:block}.vk .safe{display:none}.vk-z .safe{display:inline}
.vk-m .vk-cov{aspect-ratio:1328/768;overflow:hidden;position:relative}.vk-m .vk-cov svg{width:144.6%;max-width:none;margin-left:-22.3%}
.vk-head{display:flex;align-items:center;gap:16px;padding:16px 20px;color:#141414;flex-wrap:wrap}
.vk-ava{width:84px;height:84px;border-radius:50%;overflow:hidden;margin-top:-52px;box-shadow:0 0 0 5px #fff;flex:none}.vk-ava svg{width:100%;height:100%}
.vk-head b{display:block;font-size:20px}.vk-head span{font-size:14px;color:#6b6b80}
.vk-btn{margin-left:auto;display:flex;gap:8px}.vk-btn i{font-style:normal;font-weight:600;font-size:15px;padding:10px 16px;border-radius:10px;background:#efeefe;color:var(--ac)}
.vk-btn i:first-child{background:var(--ac);color:#fff}
.vk-menu{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:0 20px 20px}.vk-menu svg{width:100%;height:auto;display:block}
.vk-m .vk-menu{grid-template-columns:repeat(2,1fr)}.vk-m .vk-btn{margin-left:0;width:100%}.vk-m .vk-btn i{flex:1;text-align:center}
.story{max-width:270px;border-radius:18px;overflow:hidden;margin:0 auto}.story svg{width:100%;height:auto;display:block}
@media (max-width:700px){.vk-menu{grid-template-columns:repeat(2,1fr)}.vk-btn{margin-left:0;width:100%}.vk-btn i{flex:1;text-align:center}}
"""

JS = r"""
(function(){var s=document.getElementById('vkS'),v=document.querySelector('#vkV .vk');s.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
 s.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)});v.className='vk vk-'+(b.dataset.m==='z'?'d vk-z':b.dataset.m)})})();
"""


def cfg() -> dict:
    return {
        "slug": "design/shag", "brand": "Шаг", "favLetter": "Ш",
        "layout": 'cover', "header": 'float', "secHead": 'center', "resStyle": 'line', "ctaStyle": 'block',  # layout
        "title": "Шаг — оформление сообщества ВКонтакте для студии танцев · YSD DEV",
        "desc": "Оформление сообщества ВКонтакте для студии танцев: обложка с безопасными зонами для телефона, аватар, меню из шести плиток, "
                "шаблоны постов и сторис; переключение вида компьютер / телефон.",
        "theme": {"bg": "#f6f5ff", "ink": INK, "soft": "#3c3760", "mut": "#6b6790", "line": "#e2dff7", "line2": "#c9c4ee", "card": "#fff", "alt": LIL,
                  "ac": UM, "aci": WHITE, "fh": f'"{F}",sans-serif', "fb": f'"{F}",sans-serif', "hw": "800", "ht": "-.02em",
                  "cbg": UM, "cink": WHITE, "cbtn": SUN, "cbtni": INK, "kc": PINK, "rc": UM},
        "fonts": [(F, "rubik", [400, 500, 700, 800, 900], "normal"), (F, "rubik", [800, 900], "italic")],
        "css": CSS + ".kick{text-transform:none;letter-spacing:0;font-size:15px}",
        "hero": {"kicker": "Оформление сообщества ВКонтакте", "h1": "Студия, в которую хочется зайти с телефона",
                 "lead": "Обложка, аватар, меню и шаблоны постов для студии танцев в Люберцах. Девять из десяти подписчиков открывают сообщество "
                         "с телефона, поэтому всё важное — в безопасной зоне обложки и в первых двух плитках меню.",
                 "art": '<div style="background:#fff">' + COVER.replace('<g class="safe">', '<g class="safe" style="display:none">') + "</div>", "cta": "Смотреть сообщество", "go": "page"},
        "facts": [("Клиент", "студия танцев «Шаг»"), ("Работа", "обложка, аватар, меню, 6 шаблонов постов, сторис"),
                  ("Срок", "6 рабочих дней"), ("Передали", "макеты в Figma и PNG под размеры ВКонтакте")],
        "sections": [
            {"type": "text3", "id": "task", "nav": "Задача", "kick": "Задача", "h2": "Яркая студия, а сообщество — серое",
             "items": [("Обложка", "Обрезалась на телефоне", "Название и кнопка оказались за краем экрана. Пришлось перекомпоновать всё под безопасную зону."),
                       ("Меню", "Ссылки списком", "Родители не находили расписание и цены. Теперь это две первые плитки."),
                       ("Посты", "Каждый раз с нуля", "Администратор делал картинки сам в разных стилях. Нужны шаблоны, которые заполняются за пять минут.")]},
            {"type": "html", "id": "page", "nav": "Сообщество", "kick": "Сообщество", "h2": "Страница целиком", "alt": True,
             "lead": "Переключите вид: на телефоне обложка обрезается по краям, поэтому название и кнопка стоят ближе к центру.", "html": VK_BOX},
            {"type": "gallery", "id": "posts", "nav": "Посты", "kick": "Посты", "h2": "Три шаблона из шести",
             "items": [{"html": h, "span": 4, "ar": "6/5", "cap": f"<b>{t}</b>"} for t, h in POSTS]},
            {"type": "html", "id": "story", "nav": "Сторис", "kick": "Сторис", "h2": "Сторис о свободных местах", "alt": True,
             "lead": "Самый частый пост студии — «освободилось место». Шаблон меняет только цифру и день недели.", "html": STORY},
            {"type": "palette", "id": "color", "nav": "Цвета", "kick": "Цвета", "h2": "Цвета сцены",
             "lead": "Ультрамарин узнаётся в ленте, розовый и солнечный — для акцентов. Нажмите, чтобы скопировать код.",
             "colors": [("Ультрамарин", UM, "фон обложки и постов"), ("Розовый софит", PINK, "акценты и анонсы"), ("Солнце", SUN, "цены и кнопки"),
                        ("Ночь", INK, "текст"), ("Сирень", LIL, "подложки и расписание")]},
            {"type": "type", "id": "type", "kick": "Шрифты", "h2": "Один шрифт, наклон — для движения", "alt": True,
             "fonts": [(F + " Black Italic", f"'{F}'", "заголовки постов и обложки", "Батл 14 декабря", "font-weight:900;font-style:italic"),
                       (F, f"'{F}'", "расписание и подписи", "Вт 19:30 · contemporary", "font-weight:500")]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что получила студия",
             "stats": [("1 обложка", "под компьютер и телефон"), ("6", "плиток меню"), ("6", "шаблонов постов и сторис"), ("6 дней", "от брифа до загрузки")]},
        ],
        "ctaTitle": "Оформим ваше сообщество?",
        "js": JS,
    }
