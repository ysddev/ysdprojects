"""«Пена» — шаблоны постов и сторис для клининговой компании: лента из 9 постов, обложки актуального, редактор шаблона в браузере."""

TEAL, LEMON, FOAM, CORAL, INK, MINT = "#0f4c4c", "#f3f07a", "#f4faf8", "#ff7a59", "#0b2626", "#bfe6dc"
F = "Nunito"


def bubbles(seed=0, n=7, w=480, h=480, c="#fff", op=".22"):
    import random
    r = random.Random(seed)
    return "".join(f'<circle cx="{r.randint(0, w)}" cy="{r.randint(0, h)}" r="{r.randint(10, 60)}" fill="{c}" opacity="{op}"/>' for _ in range(n))


def logo(x=0, y=0, s=1.0, c=TEAL, b=LEMON):
    return (f'<g transform="translate({x} {y}) scale({s})"><circle cx="22" cy="30" r="20" style="fill:{b}"/><circle cx="46" cy="16" r="12" style="fill:{b}"/>'
            f'<circle cx="48" cy="40" r="8" style="fill:{b}"/><text x="66" y="44" font-family="{F}" font-weight="900" font-size="40" style="fill:{c}">пена</text></g>')


def sv(body, bg=TEAL, vb="0 0 480 480"):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" style="fill:{bg}"/>{body}</svg>'


def t(x, y, txt, size, c, w=900, anchor="start", cls=""):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{F}" font-weight="{w}" font-size="{size}" style="fill:{c}"'
            + (f' class="{cls}"' if cls else "") + f">{txt}</text>")


# Девять постов ленты: тип, фон, содержимое
FEED = [
    sv(bubbles(1) + t(36, 260, "−20%", 130, LEMON) + t(40, 320, "на первую уборку", 34, "#fff", 800) + logo(36, 380, .9, "#fff")),
    sv(f'<rect width="240" height="480" fill="#8a8f86"/><rect x="240" width="240" height="480" fill="{MINT}"/>' + t(120, 440, "до", 34, "#fff", 900, "middle")
       + t(360, 440, "после", 34, TEAL, 900, "middle") + "".join(f'<circle cx="{60 + k * 37}" cy="{180 + (k % 3) * 40}" r="{8 + k % 3 * 4}" fill="#5f6359"/>' for k in range(5))
       + f'<path d="M300 200 h120 v120 h-120 z" fill="#fff" opacity=".7"/>', bg=MINT),
    sv(t(36, 90, "Чек-лист", 50, TEAL) + t(36, 140, "генеральной уборки", 30, TEAL, 700)
       + "".join(f'<rect x="36" y="{180 + k * 56}" width="34" height="34" rx="10" fill="{TEAL if k < 3 else "none"}" stroke="{TEAL}" stroke-width="3"/>'
                 + t(86, 207 + k * 56, s_, 26, TEAL, 700) for k, s_ in enumerate(["окна и рамы", "фасады кухни", "за холодильником", "люстры", "швы плитки"])), bg=LEMON),
    sv(bubbles(2, 9, op=".12") + t(36, 120, "Сколько", 56, "#fff") + t(36, 186, "стоит?", 56, LEMON)
       + "".join(t(36, 270 + k * 52, a, 26, "#fff", 700) + t(444, 270 + k * 52, b, 26, LEMON, 900, "end") for k, (a, b) in enumerate([("1-комнатная", "3 900 ₽"), ("2-комнатная", "5 400 ₽"), ("после ремонта", "от 9 000 ₽"), ("окна, створка", "450 ₽")]))),
    sv(t(36, 100, "Вопрос", 30, CORAL, 800) + t(36, 170, "Чем моете?", 56, INK) + t(36, 240, "Средства без хлора", 28, INK, 700) + t(36, 278, "и резкого запаха —", 28, INK, 700)
       + t(36, 316, "можно при детях", 28, INK, 700) + t(36, 354, "и животных", 28, INK, 700) + logo(36, 400, .8), bg=FOAM),
    sv(bubbles(3) + f'<circle cx="240" cy="200" r="120" fill="{LEMON}"/>' + t(240, 230, "3 ч", 90, TEAL, 900, "middle") + t(240, 380, "средняя уборка", 34, "#fff", 800, "middle")
       + t(240, 420, "двухкомнатной квартиры", 26, "#fff", 600, "middle")),
    sv(t(36, 110, "Команда", 54, "#fff") + "".join(f'<circle cx="{110 + k * 130}" cy="250" r="56" fill="{c}"/>' for k, c in enumerate([LEMON, MINT, CORAL]))
       + t(36, 400, "проверенные клинеры,", 28, "#fff", 700) + t(36, 438, "договор и страховка", 28, LEMON, 800), bg=TEAL),
    sv(t(36, 100, "Совет", 30, TEAL, 800) + t(36, 170, "Зеркало", 56, INK) + t(36, 228, "без разводов", 56, INK) + t(36, 300, "микрофибра + тёплая вода,", 26, INK, 600)
       + t(36, 336, "движения сверху вниз", 26, INK, 600) + bubbles(4, 5, c=TEAL, op=".15"), bg=MINT),
    sv(bubbles(5) + t(240, 220, "Запишитесь", 56, "#fff", 900, "middle") + t(240, 280, "на субботу", 56, LEMON, 900, "middle")
       + f'<rect x="110" y="330" width="260" height="64" rx="32" fill="{LEMON}"/>' + t(240, 372, "осталось 4 окна", 26, TEAL, 800, "middle"), bg=CORAL),
]

HL = [("Цены", "₽"), ("До/после", "✦"), ("Отзывы", "★"), ("Команда", "☺"), ("Вопросы", "?")]
HIGHLIGHTS = '<div class="hl">' + "".join(
    f'<div><svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="48" fill="{TEAL}"/><circle cx="50" cy="50" r="40" fill="{LEMON}"/>'
    f'<text x="50" y="64" text-anchor="middle" font-family="{F}" font-weight="900" font-size="40" fill="{TEAL}">{i}</text></svg><span>{n}</span></div>' for n, i in HL) + "</div>"

FEED_BOX = ('<div class="feed"><div class="fd-h">' + sv(logo(10, 26, 1.0, TEAL), FOAM, "0 0 200 100") + '<div><b>Пена — уборка квартир</b><span>Москва · уборка за 3 часа</span></div></div>'
            + HIGHLIGHTS + '<div class="fd-g">' + "".join(f"<div>{p}</div>" for p in FEED) + "</div></div>")

THEMES = [("Морская волна", TEAL, "#fff", LEMON), ("Лимон", LEMON, TEAL, TEAL), ("Коралл", CORAL, "#fff", LEMON), ("Пена", FOAM, INK, CORAL)]
EDIT_SVG = sv(f'<g class="ed-b">{bubbles(7)}</g>' + t(36, 210, "Уберём к приезду", 42, "var(--e2)", 900, cls="ed-t1") + t(36, 266, "гостей", 42, "var(--e3)", 900, cls="ed-t2")
              + t(36, 330, "приедем завтра с 9:00", 28, "var(--e2)", 700, cls="ed-s") + logo(36, 390, .9, "var(--e2)", "var(--e3)"), "var(--e1)")

EDITOR = ('<div class="ed"><div class="ed-v" id="edV" style="--e1:#0f4c4c;--e2:#fff;--e3:#f3f07a">' + EDIT_SVG + '</div><div class="ed-r"><h3>Администратор собирает пост сам</h3>'
          '<p>Шаблон держит стиль: шрифт, отступы, пузыри и логотип на месте, меняются только слова и цвет. Попробуйте.</p>'
          '<label>Заголовок, первая строка<input id="edA" maxlength="16" value="Уберём к приезду"></label>'
          '<label>Вторая строка — акцентом<input id="edB" maxlength="16" value="гостей"></label>'
          '<label>Подпись<input id="edC" maxlength="30" value="приедем завтра с 9:00"></label><small>Цвет</small><div class="seg" id="edS">'
          + "".join(f'<button type="button" data-a="{a}" data-b="{b}" data-c="{c}"{" class=on" if k == 0 else ""}>{n}</button>' for k, (n, a, b, c) in enumerate(THEMES))
          + '</div></div></div>')

STORIES = [sv(bubbles(8, 8) + t(30, 310, "Свободно", 40, "#fff") + t(30, 358, "завтра:", 40, LEMON) + "".join(
    f'<rect x="30" y="{400 + k * 62}" width="210" height="48" rx="24" fill="#fff"/>' + t(135, 432 + k * 62, s_, 22, TEAL, 800, "middle") for k, s_ in enumerate(["10:00", "14:30", "18:00"])),
    TEAL, "0 0 270 600"),
           sv(t(30, 120, "Как мы", 38, INK) + t(30, 164, "моем окна", 38, INK) + "".join(f'<rect x="30" y="{220 + k * 90}" width="210" height="70" rx="16" fill="{FOAM}"/>'
                                                                                        + t(44, 262 + k * 90, f"{k + 1}. {s_}", 17, TEAL, 800) for k, s_ in enumerate(["снимаем сетки", "моем рамы", "стекло без разводов", "сушим подоконник"])),
              LEMON, "0 0 270 600"),
           sv(f'<circle cx="135" cy="220" r="100" fill="{LEMON}"/>' + t(135, 250, "−20%", 64, TEAL, 900, "middle") + t(135, 400, "первая уборка", 30, "#fff", 800, "middle")
              + t(135, 440, "по промокоду ПЕНА", 22, LEMON, 700, "middle") + bubbles(9, 6), CORAL, "0 0 270 600")]

CSS = """
.hero h1{font-size:clamp(42px,5.6vw,84px);font-weight:900}
.feed{max-width:560px;margin:0 auto;background:#fff;border-radius:22px;padding:18px;box-shadow:0 30px 60px -40px rgba(11,38,38,.4),0 0 0 1px var(--line)}
.fd-h{display:flex;align-items:center;gap:14px}.fd-h svg{width:110px;height:auto;border-radius:12px}.fd-h b{display:block;font-size:17px}.fd-h span{font-size:14px;color:var(--mut)}
.hl{display:flex;gap:14px;margin:18px 0;overflow-x:auto}.hl div{text-align:center;flex:none}.hl svg{width:64px;height:64px}.hl span{display:block;font-size:14px;margin-top:4px}
.fd-g{display:grid;grid-template-columns:repeat(3,1fr);gap:3px}.fd-g svg{width:100%;height:auto;display:block}
.ed{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,4vw,64px);align-items:center}
.ed-v{border-radius:20px;overflow:hidden;max-width:520px;box-shadow:0 0 0 1px var(--line)}.ed-v svg{width:100%;height:auto;display:block}
.ed-r h3{font-size:clamp(26px,2.6vw,38px);margin-bottom:12px}.ed-r p{color:var(--soft);margin-bottom:18px}
.ed-r label{display:grid;gap:6px;font-size:14px;color:var(--mut);margin-bottom:12px}
.ed-r input{font-size:17px;padding:12px 14px;border-radius:12px;border:1.5px solid var(--line2);background:#fff;color:var(--ink)}
.ed-r input:focus{outline:2px solid var(--ac);outline-offset:1px}
.ed-r small{display:block;color:var(--mut);font-size:14px;margin:8px 0}
.sto{display:grid;grid-template-columns:repeat(3,minmax(0,220px));gap:16px;justify-content:center}.sto svg{width:100%;height:auto;border-radius:16px;display:block}
@media (max-width:980px){.ed{grid-template-columns:1fr}}
@media (max-width:560px){.sto{grid-template-columns:repeat(3,1fr);gap:8px}}
"""

JS = r"""
(function(){var v=document.getElementById('edV');function q(s){return v.querySelector(s)}
[['edA','.ed-t1'],['edB','.ed-t2'],['edC','.ed-s']].forEach(function(p){var i=document.getElementById(p[0]);i.addEventListener('input',function(){q(p[1]).textContent=i.value||' '})});
var s=document.getElementById('edS');s.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;s.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)});
 v.style.setProperty('--e1',b.dataset.a);v.style.setProperty('--e2',b.dataset.b);v.style.setProperty('--e3',b.dataset.c)});
})();
"""


def cfg() -> dict:
    return {
        "slug": "design/pena", "brand": "Пена", "favLetter": "П",
        "title": "Пена — шаблоны постов и сторис для клининга · YSD DEV",
        "desc": "Шаблоны постов и сторис для продвижения услуг клининговой компании: лента из девяти постов, обложки актуального, "
                "редактор шаблона прямо в браузере, три сторис и правила цвета.",
        "theme": {"bg": FOAM, "ink": INK, "soft": "#2f4a48", "mut": "#5c7472", "line": "#d6e8e3", "line2": "#b5d3cb", "card": "#fff", "alt": "#e6f3ef",
                  "ac": TEAL, "aci": "#fff", "fh": f'"{F}",sans-serif', "fb": f'"{F}",sans-serif', "hw": "900", "ht": "-.02em",
                  "cbg": TEAL, "cink": "#fff", "cbtn": LEMON, "cbtni": TEAL, "kc": "#d4542f", "rc": TEAL},
        "fonts": [(F, "nunito", [400, 600, 700, 800, 900], "normal")],
        "css": CSS + ".kick{text-transform:none;letter-spacing:0;font-size:15px}",
        "hero": {"kicker": "Шаблоны постов для продвижения услуг", "h1": "Посты, которые администратор делает за пять минут",
                 "lead": "Девять шаблонов постов, три сторис и обложки актуального для компании, которая убирает квартиры. "
                         "Лента выглядит как работа дизайнера, хотя каждый пост собирает администратор.",
                 "art": '<div class="fd-g" style="border-radius:20px;overflow:hidden">' + "".join(f"<div>{p}</div>" for p in FEED) + "</div>", "cta": "Смотреть ленту", "go": "feed"},
        "facts": [("Клиент", "«Пена», уборка квартир"), ("Работа", "9 шаблонов постов, 3 сторис, 5 обложек"),
                  ("Срок", "5 рабочих дней"), ("Передали", "шаблоны в Figma и Canva")],
        "sections": [
            {"type": "text3", "id": "task", "nav": "Задача", "kick": "Задача", "h2": "Нужны заявки, а не красивая картинка",
             "items": [("Охват", "Посты не досматривали", "Сплошной текст на фото уборки. Человек не понимал за секунду, о чём пост."),
                       ("Доверие", "Чужие люди в доме", "Клиенты боятся пускать незнакомцев. В ленте нужны команда, договор и ответы на страхи."),
                       ("Время", "Нет дизайнера", "Публикует администратор между звонками. Шаблон должен заполняться без навыков дизайна.")]},
            {"type": "html", "id": "feed", "nav": "Лента", "kick": "Лента", "h2": "Девять постов — девять поводов", "alt": True,
             "lead": "Акция, до и после, чек-лист, цены, вопрос, цифра, команда, совет и запись. Цвета чередуются, лента не сливается.", "html": FEED_BOX},
            {"type": "html", "id": "editor", "nav": "Редактор", "kick": "Редактор", "h2": "Шаблон, который не сломать", "html": EDITOR},
            {"type": "html", "id": "stories", "nav": "Сторис", "kick": "Сторис", "h2": "Три сторис на каждую неделю", "alt": True,
             "lead": "Свободное время, как мы работаем, промокод. Кнопки и время крупно — их нажимают с телефона.",
             "html": '<div class="sto">' + "".join(f"<div>{x}</div>" for x in STORIES) + "</div>"},
            {"type": "palette", "id": "color", "nav": "Цвета", "kick": "Цвета", "h2": "Четыре фона на всю ленту",
             "lead": "Соседние посты — разного цвета, поэтому лента читается как сетка, а не как пятно. Нажмите, чтобы скопировать код.",
             "colors": [("Морская волна", TEAL, "главный фон"), ("Лимон", LEMON, "акценты и чек-листы"), ("Коралл", CORAL, "запись и срочное"),
                        ("Мята", MINT, "советы"), ("Пена", FOAM, "вопросы и ответы")]},
            {"type": "type", "id": "type", "kick": "Шрифты", "h2": "Один круглый шрифт", "alt": True,
             "fonts": [(F + " Black", f"'{F}'", "заголовки постов", "Уберём к приезду гостей", "font-weight:900"),
                       (F, f"'{F}'", "подписи и списки", "приедем завтра с 9:00", "font-weight:700")]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что получила компания",
             "stats": [("9", "шаблонов постов"), ("3", "сторис на неделю"), ("5", "обложек актуального"), ("5 минут", "на один пост у администратора")]},
        ],
        "ctaTitle": "Нужны шаблоны для ваших соцсетей?",
        "js": JS,
    }
