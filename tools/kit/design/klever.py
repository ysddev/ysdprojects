"""«Клевер» — вывеска и наружная реклама цветочного магазина: фасад день/ночь, читаемость с расстояния, билборд, штендер."""

GREEN, DEEP, PINK, CREAM = "#2f7d4f", "#1d4a31", "#f29bb5", "#fbf6ee"


def mark(x, y, s=1.0, c=GREEN, st=None):
    st = st or c
    leaves = "".join(f'<g transform="rotate({a} 50 50)"><circle cx="42" cy="22" r="10" fill="{c}"/><circle cx="58" cy="22" r="10" fill="{c}"/>'
                     f'<path d="M32.6 27 L50 46 L67.4 27Z" fill="{c}"/></g>' for a in (0, 90, 180, 270))
    return f'<g transform="translate({x} {y}) scale({s})">{leaves}<path d="M50 52 C56 70 64 84 78 94" stroke="{st}" stroke-width="5" fill="none" stroke-linecap="round"/></g>'


def word(x, y, size, fill, anchor="start", extra=""):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Cormorant Garamond" font-weight="600" font-size="{size}" fill="{fill}" {extra}>клевер</text>'


def sv(body, vb="0 0 480 300", bg="#eef2ec"):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="{bg}"/>{body}</svg>'


FACADE = (
    '<svg viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg" class="fac">'
    '<defs><filter id="gl" x="-30%" y="-60%" width="160%" height="220%"><feGaussianBlur stdDeviation="9"/></filter>'
    '<linearGradient id="wn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" class="w1"/><stop offset="1" class="w2"/></linearGradient></defs>'
    '<rect width="960" height="540" class="sky"/>'
    '<rect x="80" y="40" width="800" height="440" class="wall"/>'
    + "".join(f'<rect x="{x}" y="60" width="120" height="80" class="up"/>' for x in (130, 300, 540, 710))
    + '<rect x="80" y="170" width="800" height="10" class="cor"/>'
    '<g class="sign"><rect x="250" y="196" width="460" height="92" rx="6" class="box"/>'
    '<g class="glow" filter="url(#gl)">' + mark(270, 205, .74, c="#7fe0a6") + word(370, 270, 74, "#9ff0c0") + '</g>'
    + mark(270, 205, .74, c=GREEN) + word(370, 270, 74, GREEN, extra='class="lt"') + '</g>'
    '<rect x="120" y="310" width="300" height="160" rx="4" fill="url(#wn)"/><rect x="540" y="310" width="300" height="160" rx="4" fill="url(#wn)"/>'
    + "".join(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" class="fl"/>' for cx, cy, r, c in [
        (170, 440, 22, "#f29bb5"), (212, 446, 18, "#f7c948"), (250, 436, 24, "#e86a8f"), (300, 444, 20, "#ffffff"), (350, 438, 22, "#f29bb5"), (390, 446, 16, "#b5d99c"),
        (590, 442, 20, "#f7c948"), (636, 436, 24, "#f29bb5"), (684, 446, 18, "#ffffff"), (728, 438, 22, "#e86a8f"), (776, 444, 20, "#b5d99c"), (812, 440, 16, "#f29bb5")])
    + '<rect x="440" y="310" width="80" height="160" class="door"/><circle cx="508" cy="392" r="4" fill="#c9a24a"/>'
    '<g class="brk"><rect x="842" y="200" width="6" height="64" fill="#3a3a3a"/><circle cx="878" cy="232" r="32" class="bb"/>' + mark(856, 210, .44, c="#fff") + '</g>'
    '<rect x="0" y="480" width="960" height="60" class="walk"/>'
    '<g transform="translate(560 488)"><path d="M0 44 L22 0 H54 L76 44" class="sh" stroke-width="3" fill="none"/><path d="M22 0 L10 44 M54 0 L66 44" stroke="#5a4636" stroke-width="2"/>'
    '<rect x="16" y="6" width="44" height="30" rx="2" fill="#1d4a31"/><text x="38" y="26" text-anchor="middle" font-family="Nunito Sans" font-size="8" fill="#fff">тюльпаны</text></g>'
    '</svg>'
)

BILL = sv('<rect x="20" y="40" width="440" height="200" fill="#fbf6ee"/><rect x="20" y="40" width="190" height="200" fill="#2f7d4f"/>'
          + mark(55, 80, 1.2, c="#fff") + '<text x="232" y="110" font-family="Cormorant Garamond" font-weight="600" font-size="38" fill="#1d4a31">Тюльпаны</text>'
          '<text x="232" y="146" font-family="Cormorant Garamond" font-weight="600" font-size="38" fill="#1d4a31">к 8 Марта</text>'
          '<text x="232" y="182" font-family="Nunito Sans" font-size="15" fill="#47614f">соберём букет за 15 минут</text>'
          '<rect x="232" y="198" width="160" height="26" rx="13" fill="#f29bb5"/><text x="312" y="216" text-anchor="middle" font-family="Nunito Sans" font-weight="700" font-size="12" fill="#1d4a31">ул. Садовая, 17 · 300 м</text>'
          '<rect x="226" y="240" width="8" height="50" fill="#6b6b6b"/><rect x="246" y="240" width="8" height="50" fill="#6b6b6b"/>', bg="#cfe3ee")
SAND = sv('<path d="M170 286 L208 30 H272 L310 286" fill="none" stroke="#5a4636" stroke-width="5"/><rect x="200" y="44" width="80" height="200" rx="4" fill="#1d4a31"/>'
          + mark(214, 54, .52, c="#9ff0c0") + '<text x="240" y="132" text-anchor="middle" font-family="Cormorant Garamond" font-weight="600" font-size="22" fill="#fff">Букет</text>'
          '<text x="240" y="154" text-anchor="middle" font-family="Cormorant Garamond" font-weight="600" font-size="22" fill="#fff">дня</text>'
          '<text x="240" y="186" text-anchor="middle" font-family="Nunito Sans" font-weight="700" font-size="17" fill="#f29bb5">1 490 ₽</text>'
          '<text x="240" y="222" text-anchor="middle" font-family="Nunito Sans" font-size="10" fill="#cfe3d6">заходите →</text>', bg="#e9e3da")
GLASS = sv('<rect x="60" y="30" width="360" height="250" fill="#bcd3dc"/><rect x="60" y="30" width="360" height="250" fill="url(#g)" opacity=".4"/>'
           '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>'
           + mark(205, 60, .7, c="#fff") + word(240, 196, 46, "#fff", "middle")
           + '<text x="240" y="228" text-anchor="middle" font-family="Nunito Sans" font-size="13" fill="#fff">ежедневно 8:00 — 22:00</text>'
           '<text x="240" y="252" text-anchor="middle" font-family="Nunito Sans" font-size="13" fill="#fff">доставка по району за 1 час</text>', bg="#dfe8e3")
POINT = sv('<rect x="232" y="60" width="16" height="230" fill="#6b6b6b"/><path d="M110 70 H330 L362 104 L330 138 H110Z" fill="#2f7d4f"/>' + mark(120, 78, .52, c="#fff")
           + '<text x="182" y="114" font-family="Cormorant Garamond" font-weight="600" font-size="30" fill="#fff">клевер</text>'
             '<text x="300" y="114" font-family="Nunito Sans" font-weight="700" font-size="14" fill="#f29bb5">120 м</text>', bg="#d9e7dc")

CSS = r"""
.hero h1{font-size:clamp(44px,6.4vw,96px)}
.sc{display:grid;gap:16px}
.ctl{display:flex;flex-wrap:wrap;gap:14px 24px;align-items:center;justify-content:space-between}
.dist{display:flex;align-items:center;gap:14px;flex:1;min-width:260px;max-width:560px}
.dist input{flex:1;accent-color:#2f7d4f}.dist b{font:600 22px var(--fh);min-width:76px;text-align:right}
.view{aspect-ratio:16/9;border-radius:20px;overflow:hidden;display:grid;place-items:center;background:#cfe6f2;transition:background .6s;box-shadow:0 0 0 1px var(--line)}
.view .zoom{width:100%;transition:transform .25s,filter .25s;transform-origin:50% 55%}
.view svg{display:block;width:100%;height:auto}
.fac .sky{fill:#cfe6f2;transition:fill .6s}.fac .wall{fill:#efe6d8;transition:fill .6s}.fac .up{fill:#b9cdd8;transition:fill .6s}.fac .cor{fill:#d8ccb8}
.fac .box{fill:#fbf6ee;stroke:#e0d6c4;stroke-width:2;transition:fill .6s}.fac .glow{opacity:0;transition:opacity .6s}.fac .door{fill:#2c3b33}.fac .walk{fill:#c8c2b8;transition:fill .6s}
.fac .w1{stop-color:#dbe9ef;transition:stop-color .6s}.fac .w2{stop-color:#b7cfd9;transition:stop-color .6s}.fac .bb{fill:#2f7d4f}.fac .halo{fill:#ffd88a;opacity:0;transition:opacity .6s}.fac .sh{stroke:#5a4636}
.night .view{background:#0d1428}.night .fac .sky{fill:#0d1428}.night .fac .wall{fill:#2a2e38}.night .fac .up{fill:#f0c46a}.night .fac .box{fill:#1b2622}
.night .fac .glow{opacity:1}.night .fac .lt{fill:#d9ffe9}.night .fac .w1{stop-color:#ffe2a8}.night .fac .w2{stop-color:#f2b25c}.night .fac .walk{fill:#222632}.night .fac .halo{opacity:.35}
.night .fac .bb{fill:#36a368}
.rd{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.rd div{padding:16px;border-radius:14px;background:var(--card);box-shadow:0 0 0 1px var(--line);display:grid;gap:6px;transition:box-shadow .3s}
.rd small{color:var(--mut);font-size:13px}.rd b{font:600 22px var(--fh)}.rd span{font-size:14px;font-weight:600}
.rd .ok span{color:#2f7d4f}.rd .no span{color:#b8434f}.rd .no{box-shadow:0 0 0 2px #f2c2c8}
.spec{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.spec div{padding:18px;border-radius:16px;background:var(--card);box-shadow:0 0 0 1px var(--line);display:grid;gap:6px}
.spec b{font:600 30px var(--fh)}.spec small{color:var(--soft);font-size:14px}
@media (max-width:900px){.rd{grid-template-columns:1fr}.spec{grid-template-columns:1fr 1fr}}
"""

JS = r"""
(function(){var C=window.CASECFG,sc=document.getElementById('scn'),r=document.getElementById('dr'),out=document.getElementById('dv'),z=sc.querySelector('.zoom'),rd=document.getElementById('rd'),seg=document.getElementById('dn');
function draw(){var d=+r.value,s=Math.max(.12,Math.min(1,Math.pow(12/d,.75))),bl=d>70?((d-70)/45).toFixed(2):0;out.textContent=d+' м';z.style.transform='scale('+s+')';z.style.filter=bl?'blur('+bl+'px)':'none';
rd.innerHTML=C.parts.map(function(p){var ok=d<=p[2];return '<div class="'+(ok?'ok':'no')+'"><small>'+p[0]+'</small><b>'+p[1]+'</b><span>'+(ok?'читается':'уже не читается')+' · до '+p[2]+' м</span></div>'}).join('')}
r.addEventListener('input',draw);
seg.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;sc.classList.toggle('night',b.dataset.m==='n');seg.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)})});draw()})();
"""

PARTS = [("Вывеска над входом", "буквы 38 см", 121), ("Кронштейн у угла", "знак Ø 64 см", 57), ("Штендер на тротуаре", "текст 6 см", 17)]


def cfg() -> dict:
    scene = ('<div class="sc" id="scn"><div class="ctl"><div class="seg" id="dn"><button type="button" data-m="d" class="on">День</button><button type="button" data-m="n">Ночь</button></div>'
             '<label class="dist"><span>Расстояние</span><input type="range" id="dr" min="12" max="150" step="1" value="12"><b id="dv">12 м</b></label></div>'
             '<div class="view" data-ox><div class="zoom">' + FACADE + '</div></div><div class="rd" id="rd"></div></div>')
    spec = '<div class="spec">' + "".join(f'<div><b>{a}</b><small>{b}</small></div>' for a, b in [
        ("38 см", "высота строчных букв, объёмные, лицевая подсветка"), ("8 см", "глубина букв, борт из алюминия"),
        ("4 000 K", "тёплый белый свет: цветы не синеют вечером"), ("47 Вт", "потребление вывески, таймер 7:30 — 23:00")]) + '</div>'
    return {
        "slug": "design/klever", "brand": "Клевер", "favLetter": "К",
        "layout": 'cover', "header": 'bar', "secHead": 'stack', "resStyle": 'grid', "ctaStyle": 'ac',  # layout
        "title": "Клевер — вывеска и наружная реклама · YSD DEV",
        "desc": "Вывеска и наружная реклама цветочного магазина: фасад днём и ночью, проверка читаемости с расстояния, "
                "кронштейн, штендер, билборд 3 × 6, оклейка витрины и указатель.",
        "theme": {"bg": "#f6f7f2", "ink": "#16241b", "soft": "#46574b", "mut": "#7b8a7f", "line": "#e1e6dd", "line2": "#c9d3c6",
                  "card": "#ffffff", "alt": "#ecf1e8", "ac": "#2f7d4f", "aci": "#ffffff", "fh": '"Cormorant Garamond",serif', "fb": '"Nunito Sans",sans-serif',
                  "fm": '"Nunito Sans",sans-serif', "hw": "600", "ht": "-.01em", "cbg": "#1d4a31", "cink": "#fff", "cbtn": "#f29bb5", "cbtni": "#1d4a31", "rc": "#2f7d4f"},
        "fonts": [("Cormorant Garamond", "cormorant-garamond", [600], "normal"), ("Nunito Sans", "nunito-sans", [400, 600, 700], "normal")],
        "css": CSS,
        "hero": {"kicker": "Вывеска и наружная реклама", "h1": "Магазин, который <em>видно с перекрёстка</em>",
                 "lead": "Вывеска, кронштейн и наружная реклама для цветочного магазина на первом этаже жилого дома. "
                         "Проверили, как фасад читается днём, ночью и с другой стороны улицы, — до того, как заказывать производство.",
                 "art": sv(FACADE.replace('id="gl"', 'id="gl2"').replace("url(#gl)", "url(#gl2)").replace('id="wn"', 'id="wn2"').replace("url(#wn)", "url(#wn2)").replace('<svg viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg" class="fac">', '<g>').replace('</svg>', '</g>'), "0 0 960 540", "#cfe6f2").replace('<svg viewBox', '<svg class="fac" viewBox', 1),
                 "cta": "Проверить фасад", "go": "scene"},
        "facts": [("Клиент", "«Клевер», цветочный магазин у дома"), ("Работа", "Вывеска, кронштейн, витрина, штендер, билборд"),
                  ("Срок", "3 недели до сдачи макетов в производство"), ("Носителей", "6")],
        "data": {"parts": PARTS},
        "sections": [
            {"type": "html", "id": "scene", "nav": "Фасад", "kick": "Фасад", "h2": "Днём, ночью и издалека",
             "lead": "Переключите время суток и отодвиньтесь от магазина ползунком — видно, какой носитель с какого расстояния ещё читается.", "html": scene},
            {"type": "html", "id": "spec", "nav": "Конструкция", "kick": "Конструкция", "h2": "Вывеска в цифрах", "html": spec, "alt": True,
             "lead": "Размер букв посчитан от ширины улицы: с противоположного тротуара и из машины на светофоре."},
            {"type": "palette", "id": "color", "nav": "Цвет", "kick": "Цвет", "h2": "Зелёный, который не спорит с цветами",
             "lead": "Нажмите на цвет — код скопируется. Сами букеты — главный яркий акцент, поэтому фирменные цвета спокойные.",
             "colors": [("Клевер", GREEN, "буквы, кронштейн"), ("Глубокий зелёный", DEEP, "штендер, ночь"), ("Розовый", PINK, "цены и адрес"),
                        ("Сливки", CREAM, "короб вывески"), ("Неон", "#9ff0c0", "свечение ночью")]},
            {"type": "gallery", "id": "ooh", "nav": "Реклама", "kick": "Наружная реклама", "h2": "От билборда до указателя", "alt": True,
             "items": [{"html": BILL, "cap": "<b>Билборд 3 × 6 м</b> к сезону тюльпанов", "span": 6, "ar": "8/5"},
                       {"html": SAND, "cap": "<b>Штендер</b> с букетом дня", "span": 6, "ar": "8/5"},
                       {"html": GLASS, "cap": "<b>Оклейка витрины</b>: режим работы и доставка", "span": 6, "ar": "8/5"},
                       {"html": POINT, "cap": "<b>Указатель</b> во двор", "span": 6, "ar": "8/5"}]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что дала новая вывеска",
             "stats": [("121 м", "дальность чтения вывески"), ("+31%", "покупателей с улицы за 2 месяца"), ("1 раз", "согласовали фасад с управляющей компанией"), ("0", "переделок в производстве")]},
        ],
        "ctaTitle": "Нужна вывеска или наружная реклама?",
        "js": JS,
    }
