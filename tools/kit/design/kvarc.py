"""«Кварц» — брендбук ИТ-компании: знак и охранное поле, цвета, типографика, тон голоса, шаблоны носителей."""

V, PINK, MINT, INK, PAPER = "#2b1f6b", "#f5c6d6", "#6ee7c8", "#14121f", "#f7f6fb"


def mark(a=V, b="#5a46c7", c=PINK, s=1.0, x=0, y=0):
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M50 4 L90 27 V73 L50 96 L10 73 V27 Z" fill="{a}"/>'
            f'<path d="M50 4 L90 27 L50 50 Z" fill="{b}"/><path d="M10 73 L50 50 L50 96 Z" fill="{b}"/><path d="M50 50 L90 27 V73 Z" fill="{c}" opacity=".9"/></g>')


def logo(x=0, y=0, s=1.0, txt=INK, **k):
    return (f'<g transform="translate({x} {y}) scale({s})">{mark(**k)}<text x="112" y="68" font-family="Geologica" font-weight="600" font-size="52" '
            f'letter-spacing="-1" fill="{txt}">кварц</text></g>')


def sv(body, vb="0 0 480 300", bg=PAPER):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="{bg}"/>{body}</svg>'


HERO = sv('<g opacity=".5">' + "".join(f'<path d="M{x} 0 L{x + 140} 520" stroke="#e1def0" stroke-width="1"/>' for x in range(0, 500, 46)) + '</g>'
          + mark(s=2.6, x=60, y=60) + '<text x="340" y="215" font-family="Geologica" font-weight="600" font-size="96" letter-spacing="-3" fill="#14121f">кварц</text>'
          '<text x="344" y="262" font-family="IBM Plex Mono" font-size="20" fill="#6a6585">брендбук · версия 1.3</text>'
          '<rect x="60" y="400" width="80" height="80" rx="12" fill="#2b1f6b"/><rect x="152" y="400" width="80" height="80" rx="12" fill="#f5c6d6"/><rect x="244" y="400" width="80" height="80" rx="12" fill="#6ee7c8"/><rect x="336" y="400" width="80" height="80" rx="12" fill="#14121f"/>',
          "0 0 640 520")

CLEAR = sv('<rect x="60" y="60" width="360" height="180" fill="none" stroke="#f5c6d6" stroke-width="2" stroke-dasharray="6 5"/>'
           '<rect x="60" y="60" width="38" height="38" fill="#f5c6d6" opacity=".55"/><text x="79" y="84" text-anchor="middle" font-family="IBM Plex Mono" font-size="14" fill="#2b1f6b">x</text>'
           + logo(98, 98, .95) + '<text x="240" y="276" text-anchor="middle" font-family="IBM Plex Mono" font-size="13" fill="#6a6585">x = высота буквы «к» · вокруг знака — свободно</text>')

VERS = [("Основной", sv(logo(70, 100, 1.0))), ("На фиолетовом", sv(logo(70, 100, 1.0, txt="#fff", a="#fff", b="#cfc8ff", c="#6ee7c8"), bg=V)),
        ("Монохром", sv(logo(70, 100, 1.0, a=INK, b="#3b3850", c="#77738c"), bg="#fff")), ("Знак — иконка", sv('<rect x="180" y="90" width="120" height="120" rx="28" fill="#2b1f6b"/>' + mark(s=.8, x=200, y=110, a="#fff", b="#cfc8ff", c="#6ee7c8"), bg="#ece9f8"))]

TONE = [
    ("Письмо клиенту о сбое",
     "Уважаемый клиент! Уведомляем Вас о том, что в связи с проведением технических работ возможны временные затруднения в работе сервиса.",
     "С 14:10 до 14:35 отчёты открывались с задержкой до минуты. Причина — перегрузка сервера выгрузок, мы добавили ещё один. Данные не потерялись."),
    ("Кнопка в интерфейсе", "Осуществить отправку", "Отправить"),
    ("Пост о новой функции", "🔥🔥🔥 МЫ ВЫПУСТИЛИ СУПЕР-ОБНОВЛЕНИЕ!!! Это просто бомба, такого вы ещё не видели!",
     "Теперь отчёт можно отправить в мессенджер прямо из таблицы. Раньше на это уходило 4 шага, теперь — один."),
    ("Ошибка в форме", "Ошибка валидации поля email (код 422)", "В адресе не хватает «@». Проверьте, пожалуйста"),
]


def card(body, vb="0 0 480 300", bg="#ece9f8"):
    return sv(body, vb, bg)


TPL = [
    ("Визитка 90 × 50", card('<rect x="70" y="60" width="340" height="190" rx="10" fill="#fff"/>' + logo(94, 84, .45) +
                             '<text x="94" y="178" font-family="Geologica" font-weight="600" font-size="18" fill="#14121f">Артём Ланской</text>'
                             '<text x="94" y="200" font-family="IBM Plex Mono" font-size="11.5" fill="#6a6585">руководитель разработки</text>'
                             '<text x="94" y="228" font-family="IBM Plex Mono" font-size="11.5" fill="#14121f">a.lanskoy@kvarc.dev</text><rect x="380" y="60" width="30" height="190" fill="#6ee7c8"/>'), 4),
    ("Бланк письма A4", card('<rect x="150" y="20" width="180" height="260" fill="#fff"/>' + logo(166, 34, .26) +
                             "".join(f'<rect x="166" y="{96 + k * 12}" width="{148 - (k % 3) * 22}" height="4" rx="2" fill="#d9d5ea"/>' for k in range(10)) +
                             '<rect x="166" y="250" width="60" height="4" rx="2" fill="#2b1f6b"/><rect x="150" y="272" width="180" height="8" fill="#f5c6d6"/>'), 4),
    ("Подпись в почте", card('<rect x="40" y="70" width="400" height="160" rx="12" fill="#fff"/>' + mark(s=.62, x=62, y=100) +
                             '<text x="140" y="126" font-family="Geologica" font-weight="600" font-size="18" fill="#14121f">Мира Ветрова</text>'
                             '<text x="140" y="148" font-family="IBM Plex Mono" font-size="12" fill="#6a6585">менеджер проектов · «Кварц»</text>'
                             '<text x="140" y="178" font-family="IBM Plex Mono" font-size="12" fill="#2b1f6b">kvarc.dev · +7 495 •••-••-18</text>'
                             '<rect x="140" y="194" width="210" height="18" rx="9" fill="#6ee7c8"/><text x="245" y="207" text-anchor="middle" font-family="IBM Plex Mono" font-size="10.5" fill="#14121f">ответим в течение 2 часов</text>'), 4),
    ("Слайд презентации", card('<rect x="30" y="40" width="420" height="236" rx="8" fill="#2b1f6b"/>' + mark(s=.3, x=48, y=56, a="#fff", b="#cfc8ff", c="#6ee7c8") +
                               '<text x="52" y="150" font-family="Geologica" font-weight="600" font-size="30" fill="#fff">Отчёты за 4 секунды</text>'
                               '<text x="52" y="180" font-family="IBM Plex Mono" font-size="13" fill="#cfc8ff">вместо 3 минут в прошлой версии</text>'
                               + "".join(f'<rect x="{300 + k * 26}" y="{250 - h}" width="18" height="{h}" rx="3" fill="{"#6ee7c8" if k == 4 else "#5a46c7"}"/>' for k, h in enumerate([40, 64, 52, 88, 120]))), 6),
    ("Бейдж на конференцию", card('<rect x="170" y="10" width="140" height="280" rx="14" fill="#fff"/><rect x="170" y="10" width="140" height="96" rx="14" fill="#2b1f6b"/>'
                                  '<rect x="228" y="22" width="24" height="8" rx="4" fill="#ece9f8"/>' + mark(s=.42, x=219, y=44, a="#fff", b="#cfc8ff", c="#6ee7c8") +
                                  '<text x="240" y="152" text-anchor="middle" font-family="Geologica" font-weight="600" font-size="20" fill="#14121f">Илья</text>'
                                  '<text x="240" y="174" text-anchor="middle" font-family="Geologica" font-weight="600" font-size="20" fill="#14121f">Сафронов</text>'
                                  '<text x="240" y="198" text-anchor="middle" font-family="IBM Plex Mono" font-size="11" fill="#6a6585">backend · «Кварц»</text>'
                                  '<rect x="186" y="236" width="108" height="34" rx="17" fill="#f5c6d6"/><text x="240" y="258" text-anchor="middle" font-family="IBM Plex Mono" font-size="11" fill="#2b1f6b">спросите про API</text>'), 6),
]

CSS = r"""
.hero h1{font-size:clamp(46px,6.6vw,100px)}
.toc{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.toc a{display:grid;gap:8px;padding:18px;border-radius:16px;background:var(--card);box-shadow:0 0 0 1px var(--line);text-decoration:none}
.toc a i{font:500 13px var(--fm);font-style:normal;color:var(--ac)}.toc a b{font:600 20px var(--fh)}.toc a span{font-size:14px;color:var(--soft)}
.toc a:hover{box-shadow:0 0 0 2px var(--ink)}
.two{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:clamp(20px,3vw,40px);align-items:center}
.two .art{border-radius:18px;box-shadow:0 0 0 1px var(--line)}
.two ul{margin:0;padding-left:20px;display:grid;gap:10px;color:var(--soft)}
.vers{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-top:20px}.vers figure{margin:0}.vers svg{border-radius:14px;box-shadow:0 0 0 1px var(--line)}
.vers figcaption{font-size:13px;color:var(--mut);margin-top:8px}
.scale{display:grid;gap:0}
.scale div{display:grid;grid-template-columns:110px minmax(0,1fr) 130px;gap:20px;align-items:baseline;padding:16px 0;border-top:1px solid var(--line)}
.scale small{font:500 13px var(--fm);color:var(--mut)}.scale span{overflow-wrap:anywhere;line-height:1.1}
.tone{display:grid;gap:14px}
.tone .seg{justify-self:start}
.tn{display:grid;grid-template-columns:200px minmax(0,1fr);gap:20px;padding:20px;border-radius:18px;background:var(--card);box-shadow:0 0 0 1px var(--line);align-items:start}
.tn small{font:500 13px var(--fm);color:var(--mut)}
.tn p{font-size:17px;padding:14px 16px;border-radius:12px;transition:background .3s}
.tone[data-m="no"] .tn p{background:#fdeaea;color:#8a2a2a}.tone[data-m="yes"] .tn p{background:#e5f9f2;color:#0f5a46}
@media (max-width:980px){.toc{grid-template-columns:1fr 1fr}.two{grid-template-columns:1fr}.vers{grid-template-columns:1fr 1fr}.tn{grid-template-columns:1fr}.scale div{grid-template-columns:80px 1fr}.scale div small:last-child{display:none}}
"""

JS = r"""
(function(){var T=window.CASECFG.tone,box=document.getElementById('toneBox'),seg=document.getElementById('toneSeg');
function draw(m){box.dataset.m=m;box.querySelectorAll('.tn p').forEach(function(p,i){p.textContent=T[i][m==='yes'?2:1]});seg.querySelectorAll('button').forEach(function(b){b.classList.toggle('on',b.dataset.m===m)})}
seg.addEventListener('click',function(e){var b=e.target.closest('button');if(b)draw(b.dataset.m)});draw('yes');
})();
"""


def cfg() -> dict:
    toc = '<div class="toc">' + "".join(f'<a href="#{h}"><i>0{i + 1}</i><b>{t}</b><span>{d}</span></a>' for i, (h, t, d) in enumerate([
        ("logo", "Логотип", "охранное поле, версии"), ("color", "Цвет", "4 основных, коды"), ("type", "Типографика", "шкала размеров"),
        ("tone", "Тон голоса", "как мы пишем"), ("tpl", "Шаблоны", "визитка, бланк, слайд"), ("ui", "Иконка и аватар", "соцсети, приложение"),
        ("color", "Иллюстрации", "грани и сетка"), ("tpl", "Файлы", "SVG, PDF, Figma")])) + '</div>'
    logo_sec = ('<div class="two"><div class="art">' + CLEAR + '</div><div><ul><li>Знак — кристалл кварца из шести граней: три цвета показывают, что продукт '
                'собран из модулей.</li><li>Название пишем строчными: «кварц», а не «КВАРЦ» — бренд говорит спокойно.</li>'
                '<li>Охранное поле — высота буквы «к». Внутри нельзя ставить другие логотипы и текст.</li><li>Минимальная ширина: 88 px на экране, 22 мм в печати.</li></ul></div></div>'
                '<div class="vers">' + "".join(f'<figure>{s}<figcaption>{t}</figcaption></figure>' for t, s in VERS) + '</div>')
    scale = '<div class="scale">' + "".join(f'<div><small>{a}</small><span style="font:{f}">{t}</span><small>{b}</small></div>' for a, f, t, b in [
        ("H1 · 64", '600 clamp(34px,5vw,64px)/1.05 Geologica', "Отчёты за 4 секунды", "межстрочный 1,05"),
        ("H2 · 40", '600 clamp(26px,3.4vw,40px)/1.1 Geologica', "Интеграция с учётной системой", "межстрочный 1,1"),
        ("H3 · 24", '600 24px/1.2 Geologica', "Как устроена выгрузка данных", "межстрочный 1,2"),
        ("Текст · 17", '400 17px/1.55 Geologica', "Сервис собирает данные из учётных систем и строит отчёты, которые руководитель открывает с телефона.", "межстрочный 1,55"),
        ("Код · 14", '500 14px/1.5 "IBM Plex Mono"', "GET /v2/reports?period=2026-11", "моноширинный")]) + '</div>'
    tone = ('<div class="tone" id="toneBox" data-m="yes"><div class="seg" id="toneSeg"><button type="button" data-m="yes" class="on">Так пишем</button><button type="button" data-m="no">Так не пишем</button></div>'
            + "".join(f'<div class="tn"><small>{t}</small><p></p></div>' for t, _, _ in TONE) + '</div>')
    ui = ('<div class="vers" style="grid-template-columns:repeat(3,minmax(0,1fr))">'
          + "".join(f'<figure>{s}<figcaption>{t}</figcaption></figure>' for t, s in [
              ("Аватар в соцсетях", sv('<circle cx="240" cy="150" r="100" fill="#2b1f6b"/>' + mark(s=1.1, x=185, y=95, a="#fff", b="#cfc8ff", c="#6ee7c8"), bg="#ece9f8")),
              ("Иконка приложения", sv('<rect x="160" y="70" width="160" height="160" rx="38" fill="#14121f"/>' + mark(s=1.0, x=190, y=100, a="#6ee7c8", b="#2b9d84", c=PINK), bg="#f7f6fb")),
              ("Фавикон 32 px", sv('<rect x="220" y="130" width="40" height="40" rx="8" fill="#2b1f6b"/>' + mark(s=.3, x=225, y=135, a="#fff", b="#cfc8ff", c="#6ee7c8")
                                    + '<text x="240" y="210" text-anchor="middle" font-family="IBM Plex Mono" font-size="13" fill="#6a6585">читается и в 16 px</text>', bg="#fff"))]) + '</div>')
    return {
        "slug": "design/kvarc", "brand": "Кварц", "favLetter": "К",
        "title": "Кварц — брендбук ИТ-компании · YSD DEV",
        "desc": "Брендбук ИТ-компании: логотип и охранное поле, цвета с кодами, шкала типографики, тон голоса с примерами и шаблоны "
                "носителей — визитка, бланк, подпись в почте, слайд, бейдж.",
        "theme": {"bg": "#f7f6fb", "ink": "#14121f", "soft": "#4f4b63", "mut": "#7c7891", "line": "#e2dfee", "line2": "#c7c2dc",
                  "card": "#ffffff", "alt": "#efedf7", "ac": "#2b1f6b", "aci": "#ffffff", "fh": "Geologica,sans-serif", "fb": "Geologica,sans-serif",
                  "fm": '"IBM Plex Mono",monospace', "hw": "600", "ht": "-.03em", "cbg": "#2b1f6b", "cink": "#fff", "cbtn": "#6ee7c8", "cbtni": "#14121f", "rc": "#2b1f6b"},
        "fonts": [("Geologica", "geologica", [400, 500, 600], "normal"), ("IBM Plex Mono", "ibm-plex-mono", [400, 500], "normal")],
        "css": CSS,
        "hero": {"kicker": "Брендбук", "h1": "Правила, по которым <em>«Кварц»</em> узнают",
                 "lead": "Брендбук для ИТ-компании, которая делает сервис отчётов для бизнеса. Дизайнеры, маркетологи и разработчики "
                         "собирают носители по одним правилам — без согласований на каждую мелочь.",
                 "art": HERO, "cta": "Открыть брендбук", "go": "toc"},
        "facts": [("Клиент", "«Кварц», сервис отчётов для бизнеса"), ("Работа", "Брендбук на 46 страниц и библиотека в Figma"),
                  ("Срок", "4 недели"), ("Шаблонов носителей", "17")],
        "data": {"tone": TONE},
        "sections": [
            {"type": "html", "id": "toc", "nav": "Содержание", "kick": "Содержание", "h2": "Восемь глав брендбука", "html": toc},
            {"type": "html", "id": "logo", "nav": "Логотип", "kick": "01 · Логотип", "h2": "Кристалл из трёх граней", "html": logo_sec, "alt": True},
            {"type": "palette", "id": "color", "nav": "Цвет", "kick": "02 · Цвет", "h2": "Четыре цвета и их роли",
             "lead": "Нажмите на цвет — код скопируется. Фиолетовый занимает до 30% носителя, мятный — только акценты.",
             "colors": [("Фиолетовый кварц", V, "основной, до 30% площади"), ("Розовый кварц", PINK, "поддерживающий, фоны"),
                        ("Мята", MINT, "акцент: кнопки, рост"), ("Графит", INK, "текст"), ("Туман", PAPER, "фон страниц")]},
            {"type": "html", "id": "type", "nav": "Типографика", "kick": "03 · Типографика", "h2": "Один шрифт, пять размеров", "html": scale, "alt": True},
            {"type": "html", "id": "tone", "nav": "Тон", "kick": "04 · Тон голоса", "h2": "Пишем, как говорит толковый инженер",
             "lead": "Переключайте, чтобы сравнить: коротко, по делу, с цифрами и без канцелярита.", "html": tone},
            {"type": "gallery", "id": "tpl", "nav": "Шаблоны", "kick": "05 · Шаблоны", "h2": "Носители готовы к работе", "alt": True,
             "items": [{"html": s, "cap": f"<b>{t}</b>", "span": sp, "ar": "8/5"} for t, s, sp in TPL]},
            {"type": "html", "id": "ui", "kick": "06 · Иконка и аватар", "h2": "Знак работает и в 16 пикселях", "html": ui},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что дал брендбук", "alt": True,
             "stats": [("46", "страниц правил и примеров"), ("17", "шаблонов носителей в Figma"), ("1 день", "на новый носитель вместо недели"), ("0", "согласований на мелочи")]},
        ],
        "ctaTitle": "Нужен брендбук?",
        "js": JS,
    }
