"""«Переплёт» — баннеры и соцсети книжного магазина: одна кампания в шести форматах, живой заголовок, три темы кампаний."""

CAMPS = {
    "det": {"name": "Неделя детективов", "h": "Найдите того, кто всё это начал", "sub": "−20% на детективы до 23 ноября", "cta": "Выбрать книгу",
            "bg": "#141414", "fg": "#f2ece1", "ac": "#e8392b", "b": ["#e8392b", "#f2ece1", "#6f6a62", "#2c2b29", "#c9b48f"]},
    "ny": {"name": "Подарки к Новому году", "h": "Книга — подарок, который открывают дважды", "sub": "упакуем бесплатно · доставка за 2 часа", "cta": "Собрать подарок",
           "bg": "#0f3d33", "fg": "#f7f1e3", "ac": "#f2b33d", "b": ["#f2b33d", "#e45b3c", "#f7f1e3", "#2f7a62", "#b8d4c2"]},
    "night": {"name": "Ночь в книжном", "h": "Открыты до 2:00 — читайте до утра", "sub": "28 ноября · лекции, кофе, автограф-сессия", "cta": "Записаться",
              "bg": "#1d1b4d", "fg": "#f1eefe", "ac": "#ff9ed2", "b": ["#ff9ed2", "#7b6cf6", "#f1eefe", "#4136a3", "#ffd66e"]},
}


def spines(n=9):
    """Корешки книг — SVG, цвета из --b1..--b5."""
    out = ['<svg class="sp" viewBox="0 0 300 220" preserveAspectRatio="xMidYMax meet">']
    x = 6
    widths = [26, 34, 22, 40, 28, 36, 24, 30, 38]
    heights = [190, 160, 205, 176, 150, 198, 168, 184, 140]
    for i in range(n):
        w, h = widths[i % 9], heights[i % 9]
        tilt = ' transform="rotate(-9 %d 220)"' % (x + w) if i == 6 else ""
        out.append(f'<g{tilt}><rect x="{x}" y="{220 - h}" width="{w}" height="{h}" rx="3" style="fill:var(--b{i % 5 + 1})"/>'
                   f'<rect x="{x + 4}" y="{220 - h + 16}" width="{w - 8}" height="5" rx="2" fill="#000" opacity=".18"/>'
                   f'<rect x="{x + 4}" y="{220 - 30}" width="{w - 8}" height="4" rx="2" fill="#000" opacity=".18"/></g>')
        x += w + 3
    out.append('</svg>')
    return "".join(out)


def fr(cls, label, size, inner):
    return (f'<figure class="fm {cls}"><div class="bn">{inner}</div><figcaption><b>{label}</b> {size}</figcaption></figure>')


TXT = '<div class="tx"><small class="k"></small><b class="h"></b><span class="s"></span><i class="c"></i></div>'
FORMATS = (fr("st", "Сторис", "1080 × 1920", TXT + spines()) + fr("po", "Пост", "1080 × 1350", TXT + spines())
           + fr("sq", "Квадрат", "1080 × 1080", TXT + spines()) + fr("cv", "Обложка сообщества", "1590 × 400", TXT + spines())
           + fr("sk", "Баннер на сайт", "300 × 600", TXT + spines()) + fr("lb", "Растяжка", "728 × 90", TXT + spines()))

CSS = r"""
.hero h1{font-size:clamp(44px,6vw,92px)}
.st2{display:grid;grid-template-columns:minmax(0,320px) minmax(0,1fr);gap:clamp(20px,3vw,40px);align-items:start}
.ctl{position:sticky;top:80px;display:grid;gap:16px;background:var(--card);border-radius:20px;padding:20px;box-shadow:0 0 0 1px var(--line)}
.ctl label{display:grid;gap:6px;font-size:13px;color:var(--mut)}
.ctl textarea,.ctl input{border:1px solid var(--line);border-radius:12px;padding:10px 12px;font:500 15px var(--fb);background:var(--bg);color:var(--ink);resize:vertical}
.ctl textarea:focus,.ctl input:focus{outline:0;border-color:var(--ac)}
.ctl .seg{display:grid;gap:6px;background:none;padding:0}.ctl .seg button{text-align:left;border-radius:12px;box-shadow:inset 0 0 0 1px var(--line);padding:10px 12px;display:flex;gap:10px;align-items:center}
.ctl .seg button i{width:18px;height:18px;border-radius:50%;flex:none}
.ctl .seg button.on{background:var(--ink);color:var(--bg)}
.ctl small{color:var(--mut);font-size:12.5px}
.grid6{display:grid;grid-template-columns:repeat(6,1fr);gap:16px;align-items:start}
.fm{margin:0}.fm figcaption{font-size:13px;color:var(--mut);margin-top:8px}.fm figcaption b{color:var(--ink)}
.fm .bn{container-type:inline-size;position:relative;overflow:hidden;border-radius:12px;background:var(--cbg2);color:var(--cfg);box-shadow:0 20px 40px -30px rgba(0,0,0,.6)}
.fm.st{grid-column:span 2}.fm.po{grid-column:span 2}.fm.sq{grid-column:span 2}.fm.cv{grid-column:span 4}.fm.sk{grid-column:span 2;grid-row:span 2}.fm.lb{grid-column:span 4}
.st .bn{aspect-ratio:9/16}.po .bn{aspect-ratio:4/5}.sq .bn{aspect-ratio:1}.cv .bn{aspect-ratio:1590/400}.sk .bn{aspect-ratio:1/2}.lb .bn{aspect-ratio:728/90}
.tx{position:absolute;z-index:2;display:flex;flex-direction:column;gap:3cqw}
.tx .k{font:700 4.2cqw/1 var(--fb);letter-spacing:.14em;text-transform:uppercase;color:var(--cac)}
.tx .h{font:var(--hw) 11cqw/1.02 var(--fh);letter-spacing:-.01em;text-wrap:balance}
.tx .s{font:500 4.6cqw/1.3 var(--fb);opacity:.85}
.tx .c{font-style:normal;align-self:start;background:var(--cac);color:var(--cbg2);font:700 4.4cqw/1 var(--fb);padding:3.2cqw 5cqw;border-radius:99px;margin-top:2cqw}
.sp{position:absolute;z-index:1;width:100%;bottom:0;left:0}
.st .tx{inset:8cqw 8cqw auto}.st .sp{height:42%}
.po .tx,.sq .tx{inset:7cqw 7cqw auto 7cqw;gap:2.4cqw}.po .tx .h,.sq .tx .h{font-size:9.6cqw}.sq .tx .h{font-size:8.6cqw}.po .sp{height:34%;left:auto;right:0;width:66%}.sq .sp{height:30%;left:auto;right:0;width:56%}
.sq .tx .s{max-width:60%}
.sk .tx{inset:9cqw 9cqw auto}.sk .tx .h{font-size:13cqw}.sk .tx .k{font-size:5.6cqw}.sk .tx .s{font-size:6cqw}.sk .tx .c{font-size:6cqw}.sk .sp{height:40%}
.cv .tx{inset:5cqw auto auto 5cqw;width:56%;gap:1.2cqw}.cv .tx .h{font-size:4.4cqw}.cv .tx .k{font-size:1.5cqw}.cv .tx .s{font-size:1.7cqw}.cv .tx .c{display:none}.cv .sp{width:34%;height:96%;left:auto;right:4%}
.lb .tx{inset:0 auto 0 2.4cqw;flex-direction:row;align-items:center;gap:2cqw;width:84%}.lb .tx .k{display:none}.lb .tx .h{font-size:2.6cqw;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:62%}.lb .tx .s{display:none}
.lb .tx .c{font-size:1.6cqw;padding:1.2cqw 2cqw;margin:0;align-self:center;white-space:nowrap}.lb .sp{width:16%;height:120%;left:auto;right:1%;bottom:-10%}
.rules{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}.rules div{background:var(--card);border-radius:18px;padding:20px;box-shadow:0 0 0 1px var(--line)}
.rules b{display:block;font:var(--hw) 20px/1.2 var(--fh);margin-bottom:8px}.rules p{color:var(--soft);font-size:15px}
@media (max-width:1100px){.st2{grid-template-columns:1fr}.ctl{position:static}.grid6{grid-template-columns:repeat(4,1fr)}.fm.cv,.fm.lb{grid-column:span 4}.fm.st,.fm.po,.fm.sq,.fm.sk{grid-column:span 2}.fm.sk{grid-row:auto}}
@media (max-width:560px){.grid6{grid-template-columns:repeat(2,1fr);gap:12px}.fm.cv,.fm.lb{grid-column:span 2}.rules{grid-template-columns:1fr}}
"""

JS = r"""
(function(){var C=window.CASECFG.camps,cur='det',root=document.getElementById('bnr'),h=document.getElementById('bH'),s=document.getElementById('bS'),c=document.getElementById('bC'),seg=document.getElementById('bCamp');
function paint(){var k=C[cur];root.style.setProperty('--cbg2',k.bg);root.style.setProperty('--cfg',k.fg);root.style.setProperty('--cac',k.ac);k.b.forEach(function(v,i){root.style.setProperty('--b'+(i+1),v)});
 root.querySelectorAll('.tx').forEach(function(t){t.querySelector('.k').textContent='Переплёт · '+k.name;t.querySelector('.h').textContent=h.value||k.h;t.querySelector('.s').textContent=s.value||k.sub;t.querySelector('.c').textContent=c.value||k.cta})}
seg.innerHTML=Object.keys(C).map(function(k){return'<button type="button" data-k="'+k+'"><i style="background:'+C[k].ac+';box-shadow:0 0 0 3px '+C[k].bg+'"></i>'+C[k].name+'</button>'}).join('');
seg.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;cur=b.dataset.k;seg.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)});h.value=C[cur].h;s.value=C[cur].sub;c.value=C[cur].cta;paint()});
[h,s,c].forEach(function(x){x.addEventListener('input',paint)});seg.querySelector('button').classList.add('on');h.value=C[cur].h;s.value=C[cur].sub;c.value=C[cur].cta;paint();
})();
"""


def cfg() -> dict:
    studio = ('<div class="st2"><div class="ctl"><b style="font:600 16px var(--fh)">Кампания</b><div class="seg" id="bCamp"></div>'
              '<label>Заголовок<textarea id="bH" rows="3" maxlength="60"></textarea></label><label>Подзаголовок<input id="bS" maxlength="60"></label>'
              '<label>Кнопка<input id="bC" maxlength="20"></label><small>Напишите свой текст — он встанет во все шесть форматов сразу. Так работает шаблон, который мы отдали магазину.</small></div>'
              '<div class="grid6" id="bnr">' + FORMATS + '</div></div>')
    k = CAMPS["det"]
    hero_art = (f'<div style="padding:clamp(18px,3vw,36px);background:#e9e2d4;--cbg2:{k["bg"]};--cfg:{k["fg"]};--cac:{k["ac"]};' + ";".join(f"--b{i + 1}:{v}" for i, v in enumerate(k["b"])) + '">'
                '<div class="grid6" style="grid-template-columns:repeat(4,1fr)">'
                + fr("po", "", "", f'<div class="tx"><small class="k">Переплёт · Неделя детективов</small><b class="h">{k["h"]}</b><span class="s">{k["sub"]}</span><i class="c">{k["cta"]}</i></div>' + spines()).replace("<figcaption><b></b> </figcaption>", "")
                + fr("st", "", "", f'<div class="tx"><small class="k">Переплёт</small><b class="h">−20% на детективы</b><span class="s">до 23 ноября</span><i class="c">{k["cta"]}</i></div>' + spines()).replace("<figcaption><b></b> </figcaption>", "")
                + '</div></div>')
    return {
        "slug": "design/pereplet", "brand": "Переплёт", "favLetter": "П",
        "title": "Переплёт — баннеры и соцсети книжного магазина · YSD DEV",
        "desc": "Баннеры и посты для книжного магазина: одна кампания в шести форматах — сторис, пост, квадрат, обложка сообщества, "
                "баннер и растяжка — и шаблон, в котором меняется текст.",
        "theme": {"bg": "#f1ece2", "ink": "#1d1a16", "soft": "#57514a", "mut": "#8a8378", "line": "#ddd5c6", "line2": "#c2b9a8",
                  "card": "#fbf8f2", "alt": "#e9e2d4", "ac": "#e8392b", "aci": "#fff", "fh": '"Cormorant Garamond",serif', "fb": '"Jost",sans-serif',
                  "hw": "600", "ht": "-.01em", "cbg": "#1d1a16", "cink": "#f1ece2",
                  "cbg2": "#141414", "cfg": "#f2ece1", "cac": "#e8392b", "b1": "#e8392b", "b2": "#f2ece1", "b3": "#6f6a62", "b4": "#2c2b29", "b5": "#c9b48f"},
        "fonts": [("Cormorant Garamond", "cormorant-garamond", [500, 600], "normal"), ("Jost", "jost", [400, 500, 600], "normal")],
        "css": CSS,
        "hero": {"kicker": "Баннеры и соцсети", "h1": "Одна кампания — <em>шесть форматов</em> за вечер",
                 "lead": "Шаблон рекламы для книжного магазина: сторис, пост, обложка сообщества, баннеры на сайт. Меняете заголовок — "
                         "он встаёт во все размеры, вёрстка не ломается. Магазин запускает акцию сам, без дизайнера.",
                 "art": hero_art, "cta": "Попробовать шаблон", "go": "studio"},
        "facts": [("Клиент", "«Переплёт», книжные магазины, 3 точки"), ("Работа", "Шаблон кампаний, 6 форматов, 3 темы"),
                  ("Срок", "7 рабочих дней"), ("Запуск акции", "за 15 минут вместо 2 дней")],
        "data": {"camps": CAMPS},
        "sections": [
            {"type": "text3", "id": "task", "nav": "Задача", "kick": "Задача", "h2": "Акций много, дизайнера нет",
             "items": [("01", "Каждую неделю — новая акция", "Детективы, детская полка, встречи с авторами. Раньше на каждую уходило по 2 дня работы фрилансера."),
                       ("02", "Шесть площадок", "Сторис, посты, обложка сообщества, баннеры на сайте и в рассылке — везде свои размеры."),
                       ("03", "Узнаваемость", "Посты выглядели по-разному, и магазин не узнавали в ленте. Нужен один язык на все форматы.")]},
            {"type": "html", "id": "studio", "nav": "Шаблон", "kick": "Шаблон", "h2": "Напишите свой заголовок",
             "lead": "Выберите кампанию слева и поменяйте текст — шесть форматов перестроятся сами.", "html": studio, "alt": True},
            {"type": "html", "id": "rules", "nav": "Правила", "kick": "Правила", "h2": "Три правила шаблона",
             "html": '<div class="rules"><div><b>Корешки вместо фото</b><p>Обложки книг защищены правами издательств. Корешки из цветных плашек узнаются сразу и подходят любой теме.</p></div>'
                     '<div><b>Заголовок до 60 знаков</b><p>В растяжке 728 × 90 помещается одна строка. Длиннее — текст аккуратно обрезается, а не залезает на кнопку.</p></div>'
                     '<div><b>Три цвета на кампанию</b><p>Фон, текст и акцент. Акцент — на кнопке и подписи сверху: глаз сразу находит, куда нажать.</p></div></div>'},
            {"type": "type", "id": "type", "nav": "Шрифты", "kick": "Шрифты", "h2": "Книжная антиква и гротеск", "alt": True,
             "fonts": [("Cormorant Garamond", '"Cormorant Garamond"', "заголовки", "Найдите того, кто всё это начал", "font-weight:600"),
                       ("Jost", "Jost", "подписи, кнопки", "−20% на детективы до 23 ноября", "font-weight:500")]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что изменилось",
             "stats": [("15 мин", "на запуск акции во всех форматах"), ("3,4%", "кликов по сторис вместо 1,6%"), ("11", "акций за первый месяц"), ("0 ₽", "на дизайнера за каждую акцию")]},
        ],
        "ctaTitle": "Нужен шаблон для рекламы?",
        "js": JS,
    }
