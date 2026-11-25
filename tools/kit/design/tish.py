"""«Тишь» — карточки маркетплейса для беспроводных наушников с шумоподавлением: обложка и пять слайдов, три цвета, выдача."""

FH, FB = "Unbounded", "Golos Text"
INK, MUT, ACC = "#f2f4f7", "#9aa3b2", "#ffb547"


def hp(x, y, s=1.0):
    """Наушники: оголовье, чашки и амбушюры; цвета — из CSS-переменных --c1/--c2."""
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M70 260 C70 40 430 40 430 260" fill="none" style="stroke:var(--c2)" stroke-width="34" stroke-linecap="round"/>'
            f'<path d="M100 250 C100 80 400 80 400 250" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="10"/>'
            f'<rect x="20" y="230" width="120" height="190" rx="56" style="fill:var(--c1)"/><rect x="360" y="230" width="120" height="190" rx="56" style="fill:var(--c1)"/>'
            f'<rect x="118" y="248" width="34" height="154" rx="17" fill="#000" opacity=".35"/><rect x="348" y="248" width="34" height="154" rx="17" fill="#000" opacity=".35"/>'
            f'<path d="M44 262 C44 250 60 244 70 246" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="6" stroke-linecap="round"/>'
            f'<circle cx="420" cy="380" r="6" fill="{ACC}"/></g>')


def card(inner):
    return (f'<svg viewBox="0 0 900 1200" xmlns="http://www.w3.org/2000/svg"><rect width="900" height="1200" style="fill:var(--bg1)"/>'
            f'<circle cx="720" cy="160" r="420" fill="#fff" opacity=".04"/>{inner}</svg>')


def h(y, *lines, size=64):
    return "".join(f'<text x="64" y="{y + k * (size + 12)}" font-family="{FH}" font-weight="700" font-size="{size}" style="fill:var(--ink)">{t}</text>'
                   for k, t in enumerate(lines))


def pill(x, y, t, w):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="70" rx="35" fill="#fff" fill-opacity=".1" stroke="#fff" stroke-opacity=".25"/>'
            f'<text x="{x + w / 2}" y="{y + 46}" text-anchor="middle" font-family="{FB}" font-weight="600" font-size="28" style="fill:var(--ink)">{t}</text>')


def bars(y, label, before, after):
    return (f'<g transform="translate(64 {y})"><text x="0" y="0" font-family="{FB}" font-weight="600" font-size="30" style="fill:var(--ink)">{label}</text>'
            f'<rect x="0" y="22" width="{before * 8.4:.0f}" height="34" rx="8" fill="#fff" opacity=".18"/><text x="{before * 8.4 + 14:.0f}" y="50" font-family="{FB}" font-size="26" fill="{MUT}">{before} дБ</text>'
            f'<rect x="0" y="66" width="{after * 8.4:.0f}" height="34" rx="8" fill="{ACC}"/><text x="{after * 8.4 + 14:.0f}" y="94" font-family="{FB}" font-weight="700" font-size="26" fill="{ACC}">{after} дБ</text></g>')


SLIDES = [
    ("Обложка", card(h(130, "Тишь", size=96) + f'<text x="66" y="196" font-family="{FB}" font-size="34" style="fill:var(--mut)">беспроводные наушники с шумоподавлением</text>'
                     + hp(200, 300, 1.0) + pill(64, 1040, "−35 дБ шума", 270) + pill(354, 1040, "60 часов", 210) + pill(584, 1040, "LDAC", 150))),
    ("Шумоподавление", card(h(130, "Метро звучит", "как библиотека") + f'<text x="66" y="290" font-family="{FB}" font-size="28" style="fill:var(--mut)">громкость вокруг вас: без наушников и в «Тиши»</text>'
                            + bars(400, "Вагон метро", 82, 47) + bars(600, "Самолёт", 85, 50) + bars(800, "Опенспейс", 62, 29)
                            + f'<text x="64" y="1080" font-family="{FB}" font-size="26" style="fill:var(--mut)">замеры на стенде, режим «Максимум»</text>')),
    ("Батарея", card(h(130, "Заряжать", "раз в неделю")
                     + "".join(f'<g transform="translate(64 {330 + k * 260})"><rect width="640" height="180" rx="30" fill="none" stroke="#fff" stroke-opacity=".3" stroke-width="4"/>'
                               f'<rect x="644" y="60" width="24" height="60" rx="8" fill="#fff" opacity=".3"/>'
                               f'<rect x="14" y="14" width="{w}" height="152" rx="20" fill="{c}"/>'
                               f'<text x="40" y="112" font-family="{FH}" font-weight="700" font-size="64" fill="#0d1117">{t}</text>'
                               f'<text x="0" y="230" font-family="{FB}" font-size="28" style="fill:var(--mut)">{d}</text></g>'
                               for k, (w, c, t, d) in enumerate([(612, ACC, "60 ч", "без шумоподавления"), (408, "#c8d3e6", "40 ч", "с шумоподавлением"),
                                                                 (52, "#ffd166", "", "")]) if t)
                     + f'<g transform="translate(64 880)"><rect width="772" height="170" rx="30" fill="#fff" fill-opacity=".08"/>'
                       f'<text x="40" y="78" font-family="{FH}" font-weight="700" font-size="48" fill="{ACC}">10 минут</text>'
                       f'<text x="40" y="128" font-family="{FB}" font-size="30" style="fill:var(--ink)">зарядки — 5 часов музыки</text></g>')),
    ("Комплект", card(h(130, "Что в коробке") + hp(260, 210, .55)
                      + "".join(f'<g transform="translate({64 + (k % 2) * 396} {560 + (k // 2) * 200})"><rect width="376" height="176" rx="28" fill="#fff" fill-opacity=".08"/>'
                                f'<text x="32" y="78" font-family="{FB}" font-weight="700" font-size="32" style="fill:var(--ink)">{a}</text>'
                                f'<text x="32" y="122" font-family="{FB}" font-size="25" style="fill:var(--mut)">{b}</text></g>'
                                for k, (a, b) in enumerate([("Наушники", "складываются в кейс"), ("Жёсткий кейс", "с карманом для кабелей"),
                                                            ("Кабель USB-C", "зарядка и звук"), ("Переходник", "для кресла в самолёте")])))),
    ("Характеристики", card(h(130, "Коротко", "о главном") + "".join(
        f'<g transform="translate(64 {330 + k * 116})"><path d="M0 84 H772" stroke="#fff" stroke-opacity=".15" stroke-width="2"/>'
        f'<text x="0" y="56" font-family="{FB}" font-size="30" style="fill:var(--mut)">{a}</text>'
        f'<text x="772" y="56" text-anchor="end" font-family="{FB}" font-weight="700" font-size="32" style="fill:var(--ink)">{b}</text></g>'
        for k, (a, b) in enumerate([("Вес", "248 г"), ("Динамики", "40 мм"), ("Bluetooth", "5.3, два устройства сразу"), ("Кодеки", "SBC, AAC, LDAC"),
                                    ("Микрофоны", "6, с шумоподавлением"), ("Приложение", "эквалайзер и режимы"), ("Гарантия", "1 год")])))),
    ("Сравнение", card(h(130, "Какую модель", "выбрать") + "".join(
        f'<g transform="translate({64 + k * 396} 330)"><rect width="376" height="760" rx="32" fill="{"#fff" if k == 0 else "none"}" fill-opacity="{.1 if k == 0 else 0}" stroke="#fff" stroke-opacity=".25" stroke-width="3"/>'
        f'<text x="32" y="80" font-family="{FH}" font-weight="700" font-size="40" style="fill:var(--ink)">{n}</text>'
        f'<text x="32" y="140" font-family="{FH}" font-weight="700" font-size="44" fill="{ACC if k == 0 else INK}">{p}</text>'
        + "".join(f'<text x="32" y="{240 + j * 92}" font-family="{FB}" font-size="28" style="fill:var(--ink)">{r}</text>' for j, r in enumerate(rows))
        + "</g>" for k, (n, p, rows) in enumerate([("Тишь", "12 990 ₽", ["−35 дБ шума", "60 часов", "LDAC", "6 микрофонов", "кейс в комплекте"]),
                                                   ("Тишь Лайт", "7 490 ₽", ["−25 дБ шума", "45 часов", "AAC", "2 микрофона", "чехол-мешок"])])))),
]

COLORS = [("Графит", "#3d4552", "#4a5262", "#0d1117", INK, MUT), ("Белый", "#e9ecf1", "#cfd5de", "#1a1f27", INK, MUT), ("Песок", "#c9b59a", "#a8957b", "#1b1814", INK, "#b3a690")]

SERP = ('<div class="serp">' + "".join(
    f'<div class="sp{" on" if k == 2 else ""}"><div class="sp-i">{c}</div><b>{p}</b><span>{t}</span></div>'
    for k, (c, p, t) in enumerate([
        ('<svg viewBox="0 0 300 400"><rect width="300" height="400" fill="#f1f1f1"/><text x="16" y="44" font-family="Golos Text" font-weight="800" font-size="30" fill="#e00">ХИТ!!!</text>'
         '<circle cx="150" cy="210" r="90" fill="#bbb"/><text x="16" y="370" font-family="Golos Text" font-size="18" fill="#222">✔ BASS ✔ HiFi ✔ TWS</text></svg>', "3 290 ₽", "Наушники беспроводные…"),
        ('<svg viewBox="0 0 300 400"><rect width="300" height="400" fill="#fff"/><circle cx="150" cy="200" r="100" fill="#d0d0d0"/><circle cx="240" cy="70" r="44" fill="#ffd600"/>'
         '<text x="240" y="80" text-anchor="middle" font-family="Golos Text" font-weight="800" font-size="24" fill="#e00">−70%</text></svg>', "4 990 ₽", "Наушники полноразмерные…"),
        ('<div style="--c1:#3d4552;--c2:#4a5262;--bg1:#0d1117;--ink:#f2f4f7;--mut:#9aa3b2">' + SLIDES[0][1] + '</div>', "12 990 ₽", "«Тишь» с шумоподавлением"),
        ('<svg viewBox="0 0 300 400"><rect width="300" height="400" fill="#eaeaea"/><rect x="60" y="100" width="180" height="200" rx="30" fill="#c3c3c3"/>'
         '<text x="16" y="370" font-family="Golos Text" font-weight="700" font-size="20" fill="#333">ПРЕМИУМ ЗВУК 5.3</text></svg>', "6 450 ₽", "Наушники с микрофоном…")]))
        + '</div>')

CSS = """
.hero h1{font-size:clamp(40px,5.2vw,80px)}
.mp{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.9fr);gap:clamp(24px,4vw,64px);align-items:start}
.mp-big{border-radius:18px;overflow:hidden;box-shadow:0 30px 60px -40px rgba(0,0,0,.6),0 0 0 1px var(--line);background:var(--bg1)}
.mp-big svg,.mp-th svg{width:100%;height:auto}
.mp-nav{display:flex;align-items:center;justify-content:space-between;margin-top:14px;gap:12px}
.mp-nav button{width:44px;height:44px;border-radius:50%;box-shadow:inset 0 0 0 1.5px var(--line2);font-size:18px}
.mp-nav span{font-size:14px;color:var(--mut)}
.mp-th{display:grid;grid-template-columns:repeat(6,1fr);gap:8px;margin-top:14px}
.mp-th button{border-radius:8px;overflow:hidden;opacity:.55;transition:opacity .2s;background:var(--bg1)}.mp-th button.on{opacity:1;box-shadow:0 0 0 2px var(--ac)}
.mp-r h3{font-size:clamp(24px,2.4vw,34px);margin-bottom:14px}.mp-r p{color:var(--soft);margin-bottom:20px}
.mp-c{display:flex;gap:12px;margin:10px 0 6px}.mp-c button{width:46px;height:46px;border-radius:50%;background:var(--s);box-shadow:0 0 0 3px var(--bg),0 0 0 4px var(--line2)}
.mp-c button.on{box-shadow:0 0 0 3px var(--bg),0 0 0 5px var(--ac)}
.mp-r small{color:var(--mut);font-size:14px}
.mp-r ul{margin:22px 0 0;padding:0;list-style:none;display:grid;gap:10px}.mp-r li{padding:14px 16px;border-radius:14px;background:var(--card);font-size:15px}
.serp{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;max-width:960px}
.sp{background:#fff;border-radius:14px;padding:10px;color:#1a1a1a;opacity:.55;transition:opacity .3s}.sp.on{opacity:1;box-shadow:0 0 0 3px var(--ac)}
.sp-i{border-radius:10px;overflow:hidden;aspect-ratio:3/4}.sp-i svg{width:100%;height:100%;display:block}
.sp b{display:block;margin-top:10px;font-size:17px}.sp span{display:block;font-size:14px;color:#666}
@media (max-width:980px){.mp{grid-template-columns:1fr}.serp{grid-template-columns:1fr 1fr}}
"""

JS = r"""
(function(){var C=""" + str([list(c) for c in COLORS]).replace("'", '"') + r""";
var root=document.getElementById('mp'),sw=document.getElementById('mpC'),big=document.getElementById('mpBig'),th=document.getElementById('mpTh');
function color(i){var c=C[i];['--c1','--c2','--bg1','--ink','--mut'].forEach(function(k,j){root.style.setProperty(k,c[j+1])});
 sw.querySelectorAll('button').forEach(function(b,k){b.classList.toggle('on',k===i)});document.getElementById('mpCn').textContent=c[0]}
sw.innerHTML=C.map(function(c){return'<button type="button" style="--s:'+c[1]+'" aria-label="'+c[0]+'"></button>'}).join('');
sw.addEventListener('click',function(e){var b=e.target.closest('button');if(b)color([].indexOf.call(sw.children,b))});
function show(i){var s=th.querySelectorAll('button');s.forEach(function(b,k){b.classList.toggle('on',k===i)});big.innerHTML=s[i].querySelector('.svgsrc').innerHTML;big.dataset.i=i;
 document.getElementById('mpN').textContent=(i+1)+' из '+s.length+': '+s[i].dataset.t}
th.addEventListener('click',function(e){var b=e.target.closest('button');if(b)show([].indexOf.call(th.querySelectorAll('button'),b))});
function step(d){var n=th.querySelectorAll('button').length;show(((+big.dataset.i||0)+d+n)%n)}
document.getElementById('mpPrev').addEventListener('click',function(){step(-1)});document.getElementById('mpNext').addEventListener('click',function(){step(1)});
var x0=null;big.addEventListener('touchstart',function(e){x0=e.touches[0].clientX},{passive:true});big.addEventListener('touchend',function(e){if(x0==null)return;var d=e.changedTouches[0].clientX-x0;if(Math.abs(d)>40)step(d<0?1:-1);x0=null});
color(0);show(0);
})();
"""


def cfg() -> dict:
    thumbs = "".join(f'<button type="button" data-t="{t}" aria-label="Слайд {i + 1}: {t}">{s}<div class="svgsrc" hidden>{s}</div></button>' for i, (t, s) in enumerate(SLIDES))
    studio = ('<div class="mp" id="mp" style="--c1:#3d4552;--c2:#4a5262;--bg1:#0d1117;--ink:#f2f4f7;--mut:#9aa3b2"><div><div class="mp-big" id="mpBig"></div>'
              '<div class="mp-nav"><button type="button" id="mpPrev" aria-label="Назад">←</button><span id="mpN"></span>'
              '<button type="button" id="mpNext" aria-label="Вперёд">→</button></div><div class="mp-th" id="mpTh">' + thumbs + '</div></div>'
              '<div class="mp-r"><h3>Шесть слайдов — шесть вопросов покупателя</h3><p>Насколько тише, сколько держит батарея, что в коробке и чем модели '
              'отличаются друг от друга. Цвет корпуса меняется во всех слайдах сразу.</p><div class="mp-c" id="mpC"></div><small>Цвет: <b id="mpCn"></b></small>'
              '<ul><li>Цифры шумоподавления — на графике, а не словами «супер-тишина»</li><li>Батарея нарисована как батарея: понятно без чтения</li>'
              '<li>Сравнение со своей младшей моделью — покупатель не уходит к конкурентам</li></ul></div></div>')
    return {
        "slug": "design/tish", "brand": "Тишь", "favLetter": "Т",
        "layout": 'index', "header": 'bar', "secHead": 'center', "resStyle": 'line', "ctaStyle": 'ac',  # layout
        "title": "Тишь — карточки маркетплейса для наушников · YSD DEV",
        "desc": "Дизайн карточек маркетплейса для беспроводных наушников: обложка и пять слайдов инфографики — шумоподавление, батарея, комплект, "
                "характеристики, сравнение моделей; три цвета корпуса и вид в выдаче.",
        "theme": {"bg": "#e9edf2", "ink": "#0d1117", "soft": "#3b4350", "mut": "#5d6675", "line": "#d3d9e1", "line2": "#b8c0cc", "card": "#fff",
                  "alt": "#dfe4ea", "ac": "#0d1117", "aci": "#fff", "fh": f'"{FH}",sans-serif', "fb": f'"{FB}",sans-serif', "hw": "700", "ht": "-.03em",
                  "cbg": "#0d1117", "cink": INK, "cbtn": ACC, "cbtni": "#0d1117", "kc": "#8a5a00"},
        "fonts": [(FH, "unbounded", [500, 700], "normal"), (FB, "golos-text", [400, 600, 700], "normal")],
        "css": CSS + ".kick{text-transform:none;letter-spacing:0;font-size:15px}.hero h1,.sh h2{font-weight:600}",
        "hero": {"kicker": "Карточки для маркетплейса", "h1": "Наушники, которые не кричат в выдаче",
                 "lead": "Обложка и пять слайдов для полноразмерных наушников с шумоподавлением. Соседи по выдаче продают «ХИТ!!!» и «−70%», "
                         "мы — цифры, которые покупатель может проверить.",
                 "art": '<div style="--c1:#3d4552;--c2:#4a5262;--bg1:#0d1117;--ink:#f2f4f7;--mut:#9aa3b2">' + SLIDES[0][1] + "</div>", "cta": "Листать карточку", "go": "cards"},
        "facts": [("Клиент", "«Тишь», аудиотехника"), ("Работа", "обложка, 5 слайдов, 3 цвета"), ("Срок", "5 рабочих дней"), ("Формат", "900 × 1200, под оба крупных маркетплейса")],
        "sections": [
            {"type": "text3", "id": "task", "nav": "Задача", "kick": "Задача", "h2": "Дорогие наушники среди дешёвых",
             "items": [("Цена", "В 2–3 раза дороже соседей", "Покупатель должен за две секунды понять, за что платит, иначе листает дальше."),
                       ("Вопросы", "Одни и те же в отзывах", "Как глушит метро, сколько держит, есть ли кейс. Ответ на каждый — отдельный слайд."),
                       ("Модели", "Две, путали между собой", "Нужен слайд сравнения, чтобы покупатель выбрал у нас, а не у конкурента.")]},
            {"type": "html", "id": "cards", "nav": "Карточка", "kick": "Карточка", "h2": "Обложка и пять слайдов",
             "lead": "Листайте стрелками или свайпом, меняйте цвет справа.", "html": studio, "alt": True},
            {"type": "html", "id": "serp", "nav": "В выдаче", "kick": "В выдаче", "h2": "Как карточка выглядит среди соседей",
             "lead": "Тёмная обложка и три спокойные плашки выделяются среди белых карточек с «ХИТ!!!» и скидками.", "html": SERP},
            {"type": "palette", "id": "color", "nav": "Цвета", "kick": "Цвета", "h2": "Тёмные слайды и тёплый акцент", "alt": True,
             "lead": "Янтарный — только для цифр, которыми гордится товар. Нажмите, чтобы скопировать код.",
             "colors": [("Ночь", "#0d1117", "фон всех слайдов"), ("Янтарь", ACC, "главная цифра слайда"), ("Иней", INK, "заголовки"), ("Сталь", MUT, "пояснения"),
                        ("Графит", "#3d4552", "цвет корпуса"), ("Песок", "#c9b59a", "цвет корпуса")]},
            {"type": "type", "id": "type", "kick": "Шрифты", "h2": "Широкий для цифр, ровный для текста",
             "fonts": [(FH, f"'{FH}'", "заголовки и цифры", "−35 дБ · 60 ч", "font-weight:700"),
                       (FB, f"'{FB}'", "пояснения и характеристики", "Bluetooth 5.3, два устройства сразу", "font-weight:400")]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что получил продавец",
             "stats": [("6", "слайдов на одном шаблоне"), ("3", "цвета без перерисовки"), ("2", "модели на слайде сравнения"), ("5 дней", "от брифа до загрузки")]},
        ],
        "ctaTitle": "Нужны карточки для техники?",
        "js": JS,
    }
