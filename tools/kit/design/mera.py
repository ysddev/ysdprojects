"""«Мера» — фирменный стиль магазина женской одежды: логотип с сантиметровой лентой, палитра, шрифты, носители, бирка-конструктор."""

CHALK, INK, KHAKI, POWDER, OLIVE, WHITE = "#eeede8", "#141414", "#6b6a3c", "#c9d6e3", "#3d3c1f", "#ffffff"
FH, FB = "Bona Nova", "Onest"


def tape(x, y, w, c=INK, n=None):
    """Сантиметровая лента: длинные деления через 5, короткие — каждый сантиметр."""
    n = n or int(w // 8)
    t = f'<g transform="translate({x} {y})"><path d="M0 0 H{w}" style="stroke:{c}" stroke-width="2"/>'
    for k in range(n + 1):
        h = 12 if k % 5 == 0 else 6
        t += f'<path d="M{k * w / n:.1f} 0 V{h}" style="stroke:{c}" stroke-width="1.6"/>'
    return t + "</g>"


def logo(x=0, y=0, s=1.0, c=INK):
    return (f'<g transform="translate({x} {y}) scale({s})"><text x="0" y="70" font-family="{FH}" font-size="92" letter-spacing="2" style="fill:{c}">мера</text>'
            + tape(4, 88, 214, c, 27) + "</g>")


def sv(body, vb="0 0 480 360", bg=CHALK):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" style="fill:{bg}"/>{body}</svg>'


def tag(x, y, s=1.0, bg="var(--tb)", ink="var(--ti)", size="M", price="7 900 ₽", name="Платье-рубашка", rot=0):
    sizes = ["XS", "S", "M", "L", "XL"]
    t = (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><path d="M60 0 H180 L240 60 V420 H0 V60 Z" style="fill:{bg}"/>'
         f'<circle cx="120" cy="44" r="12" fill="{CHALK}"/><path d="M120 32 C 110 -30 40 -40 10 -60" fill="none" stroke="#8b8a7d" stroke-width="2"/>'
         + logo(42, 92, .7, ink) + f'<text x="28" y="250" font-family="{FB}" font-size="17" style="fill:{ink}">{name}</text>'
         f'<text x="28" y="274" font-family="{FB}" font-size="13" style="fill:{ink}" opacity=".7">лён 100%, сделано в Иваново</text>')
    for k, z in enumerate(sizes):
        cx = 40 + k * 40
        on = z == size
        t += (f'<circle cx="{cx}" cy="318" r="16" style="fill:{ink if on else "none"};stroke:{ink}" stroke-width="1.4" data-z="{z}"/>'
              f'<text x="{cx}" y="323" text-anchor="middle" font-family="{FB}" font-size="12" font-weight="600" style="fill:{bg if on else ink}" data-zt="{z}">{z}</text>')
    t += f'<text x="28" y="388" font-family="{FH}" font-size="34" style="fill:{ink}" class="tp">{price}</text></g>'
    return t


HERO = sv(f'<rect x="360" y="0" width="280" height="520" fill="{KHAKI}"/>' + tag(84, 80, 1.0, bg=WHITE, ink=INK, rot=-6)
          + tag(330, 110, .9, bg=POWDER, ink=INK, size="S", price="5 400 ₽", name="Юбка миди", rot=7)
, "0 0 640 520")

TAG_BOX = ('<div class="tg"><div class="tg-v" id="tgV" style="--tb:#ffffff;--ti:#141414">' + sv(tag(120, 70, .64), "0 0 480 360") + '</div><div class="tg-r">'
           '<h3>Бирка — главный носитель магазина</h3><p>Покупательница держит её в руках дольше, чем смотрит на вывеску. На бирке — '
           'ткань, страна, размерная линейка и цена крупно. Выберите размер и цвет коллекции.</p><small>Размер</small><div class="seg" id="tgS">'
           + "".join(f'<button type="button" data-z="{z}"{" class=on" if z == "M" else ""}>{z}</button>' for z in ("XS", "S", "M", "L", "XL"))
           + '</div><small>Коллекция</small><div class="seg" id="tgC">'
           + "".join(f'<button type="button" data-b="{b}" data-i="{i}"{" class=on" if k == 0 else ""}>{n}</button>'
                     for k, (n, b, i) in enumerate([("Базовая", WHITE, INK), ("Лето", POWDER, INK), ("Осень", KHAKI, "#fff"), ("Вечер", INK, CHALK)]))
           + '</div></div></div>')

CARRIERS = [
    ("Пакет", sv(f'<path d="M190 80 C190 36 290 36 290 80" fill="none" stroke="{INK}" stroke-width="6"/><rect x="140" y="80" width="200" height="260" fill="{KHAKI}"/>'
                 + logo(176, 170, .58, c="#fff"), bg=POWDER), 4),
    ("Коробка с лентой", sv(f'<path d="M80 150 L240 100 L400 150 L240 200 Z" fill="#fff"/><path d="M80 150 L240 200 V310 L80 260 Z" fill="#e2e1da"/>'
                            f'<path d="M400 150 L240 200 V310 L400 260 Z" fill="#d4d3cb"/><path d="M160 125 L320 175" stroke="{KHAKI}" stroke-width="14"/>'
                            f'<path d="M160 175 L320 125" stroke="{KHAKI}" stroke-width="14" opacity=".9"/>' + tape(110, 228, 110, KHAKI, 14), bg=CHALK), 4),
    ("Вывеска", sv(f'<rect width="480" height="360" fill="#b8b6ad"/><rect x="40" y="40" width="400" height="90" fill="{INK}"/>' + logo(150, 46, .6, c=CHALK)
                   + f'<rect x="60" y="150" width="170" height="210" fill="#2b2b28"/><rect x="250" y="150" width="170" height="210" fill="#2b2b28"/>'
                   f'<rect x="70" y="160" width="150" height="190" fill="{POWDER}" opacity=".35"/><rect x="260" y="160" width="150" height="190" fill="{POWDER}" opacity=".35"/>', bg="#b8b6ad"), 4),
    ("Пост о новой коллекции", sv(f'<rect x="100" y="20" width="280" height="320" fill="{POWDER}"/><circle cx="240" cy="150" r="88" fill="#fff" opacity=".6"/>'
                                  f'<path d="M205 92 h70 l18 40 -18 8 v120 h-70 v-120 l-18 -8 z" fill="{KHAKI}"/>'
                                  f'<text x="122" y="296" font-family="{FH}" font-size="30" fill="{INK}">Лето в городе</text>'
                                  f'<text x="122" y="322" font-family="{FB}" font-size="13" fill="{INK}">12 моделей · лён и хлопок</text>' + logo(300, 36, .28), bg=CHALK), 4),
    ("Карта клиента", sv(f'<g transform="translate(90 90)"><rect width="300" height="180" rx="14" fill="{INK}"/>' + logo(24, 22, .5, c=CHALK)
                         + f'<text x="24" y="130" font-family="{FB}" font-size="13" fill="{CHALK}" opacity=".8">подгоним длину бесплатно</text>'
                         f'<text x="24" y="154" font-family="{FB}" font-weight="600" font-size="15" fill="{CHALK}">№ 0418 · 5% с покупок</text></g>', bg=KHAKI), 4),
    ("Наклейка на чек и упаковку", sv(f'<circle cx="240" cy="180" r="110" fill="{KHAKI}"/><circle cx="240" cy="180" r="96" fill="none" stroke="#fff" stroke-dasharray="2 5"/>'
                                      + logo(178, 140, .48, c="#fff"), bg=CHALK), 4),
]

CSS = """
.hero h1{font-size:clamp(44px,5.8vw,88px);font-weight:400}
.sh h2,.cta h2,.tg-r h3{font-weight:400}
.tg{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,4vw,64px);align-items:center}
.tg-v{border-radius:4px;overflow:hidden;box-shadow:0 0 0 1px var(--line)}.tg-v svg{width:100%;height:auto}
.tg-r h3{font-size:clamp(28px,2.8vw,40px);margin-bottom:12px}.tg-r p{color:var(--soft);margin-bottom:8px}
.tg-r small{display:block;color:var(--mut);font-size:14px;margin:18px 0 8px}
@media (max-width:980px){.tg{grid-template-columns:1fr}}
"""

JS = r"""
(function(){var v=document.getElementById('tgV'),P={XS:'7 900',S:'7 900',M:'7 900',L:'8 300',XL:'8 300'};
function seg(id,fn){var s=document.getElementById(id);s.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;
 s.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)});fn(b)})}
function size(z){v.querySelectorAll('[data-z]').forEach(function(c){var on=c.dataset.z===z;c.style.fill=on?'var(--ti)':'none'});
 v.querySelectorAll('[data-zt]').forEach(function(t){t.style.fill=t.dataset.zt===z?'var(--tb)':'var(--ti)'});v.querySelector('.tp').textContent=P[z]+' ₽'}
seg('tgS',function(b){size(b.dataset.z)});seg('tgC',function(b){v.style.setProperty('--tb',b.dataset.b);v.style.setProperty('--ti',b.dataset.i)});
})();
"""


def cfg() -> dict:
    return {
        "slug": "design/mera", "brand": "Мера", "favLetter": "М",
        "title": "Мера — фирменный стиль магазина женской одежды · YSD DEV",
        "desc": "Фирменный стиль магазина женской одежды: логотип с сантиметровой лентой, палитра коллекций, шрифты, бирка-конструктор, "
                "пакет, коробка, вывеска, пост, карта клиента и наклейка.",
        "theme": {"bg": CHALK, "ink": INK, "soft": "#4a4a44", "mut": "#7a796f", "line": "#dcdbd3", "line2": "#c3c2b8", "card": "#fff",
                  "alt": "#e4e3dc", "ac": KHAKI, "aci": "#fff", "fh": f'"{FH}",serif', "fb": f'"{FB}",sans-serif', "hw": "400", "ht": "-.01em",
                  "cbg": KHAKI, "cink": "#fff", "cbtn": INK, "cbtni": CHALK, "kc": OLIVE, "ra": "4px", "rb": "2px", "rs": "4px"},
        "fonts": [(FH, "bona-nova", [400], "normal"), (FB, "onest", [400, 500, 600], "normal")],
        "css": CSS + ".kick{text-transform:none;letter-spacing:0;font-size:15px}",
        "hero": {"kicker": "Фирменный стиль магазина одежды", "h1": "Одежда, которую подгоняют по мерке",
                 "lead": "Логотип, бирки и носители для магазина женской одежды в Казани. Главная идея магазина — бесплатная подгонка длины, "
                         "поэтому в знаке сантиметровая лента.",
                 "art": HERO, "cta": "Смотреть стиль", "go": "tag"},
        "facts": [("Клиент", "«Мера», магазин женской одежды"), ("Работа", "логотип, палитра, бирки, 8 носителей"),
                  ("Срок", "10 рабочих дней"), ("Передали", "брендбук и макеты для типографии")],
        "sections": [
            {"type": "text3", "id": "task", "nav": "Задача", "kick": "Задача", "h2": "Магазин с ателье внутри",
             "items": [("Отличие", "Подгонка в день покупки", "Портниха работает прямо в магазине. Об этом знали только постоянные покупательницы."),
                       ("Аудитория", "Женщины 28–45 лет", "Покупают базовые вещи из натуральных тканей и не любят кричащие витрины."),
                       ("Коллекции", "Четыре в год", "Каждой коллекции нужен свой цвет, но магазин должен оставаться узнаваемым.")]},
            {"type": "gallery", "id": "logo", "nav": "Логотип", "kick": "Логотип", "h2": "Слово и сантиметровая лента", "alt": True,
             "lead": "Длинные деления — каждые 5 сантиметров, как на настоящей ленте портнихи. Под ними удобно ставить название коллекции.",
             "items": [{"html": sv(logo(124, 120, 1.0)), "span": 6, "cap": "<b>Основная версия</b>"},
                       {"html": sv(logo(124, 120, 1.0, c="#fff"), bg=KHAKI), "span": 6, "cap": "<b>На хаки</b> — пакеты и вывеска"},
                       {"html": sv(logo(124, 120, 1.0, c=INK), bg=POWDER), "span": 6, "cap": "<b>Коллекция «Лето»</b>"},
                       {"html": sv(logo(124, 120, 1.0, c=CHALK), bg=INK), "span": 6, "cap": "<b>Коллекция «Вечер»</b>"}]},
            {"type": "html", "id": "tag", "nav": "Бирка", "kick": "Бирка", "h2": "Бирка-конструктор", "html": TAG_BOX},
            {"type": "palette", "id": "color", "nav": "Цвета", "kick": "Цвета", "h2": "Базовые цвета и цвета коллекций", "alt": True,
             "lead": "Мел и графит постоянны, цвет коллекции меняется. Нажмите, чтобы скопировать код.",
             "colors": [("Мел", CHALK, "фон, бирки"), ("Графит", INK, "логотип и текст"), ("Хаки", KHAKI, "осень, пакеты, вывеска"),
                        ("Пудра", POWDER, "лето"), ("Олива", OLIVE, "подписи и детали")]},
            {"type": "type", "id": "type", "kick": "Шрифты", "h2": "Антиква с характером и ровный гротеск",
             "fonts": [(FH, f"'{FH}'", "логотип, заголовки, цены", "Лето в городе", ""),
                       (FB, f"'{FB}'", "бирки, состав, тексты", "лён 100%, сделано в Иваново", "font-weight:400")]},
            {"type": "gallery", "id": "carriers", "nav": "Носители", "kick": "Носители", "h2": "От пакета до наклейки на чек", "alt": True,
             "items": [{"html": h, "span": sp, "cap": f"<b>{t}</b>"} for t, h, sp in CARRIERS]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что получил магазин",
             "stats": [("1 логотип", "и четыре цвета коллекций"), ("8", "носителей для печати"), ("1 бирка", "на все модели и размеры"), ("10 дней", "от брифа до макетов")]},
        ],
        "ctaTitle": "Нужен стиль для магазина?",
        "js": JS,
    }
