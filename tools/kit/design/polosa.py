"""«Полоса» — упаковка шоколада: выбор вкуса, развёртка с линиями реза и сгиба, линейка и шоубокс."""

FL = [
    {"k": "dark", "n": "Тёмный", "s": "горький, без добавок", "p": 72, "bg": "#2a1d17", "st": "#c9a26b", "ink": "#f4e9da", "sub": "#c9a26b",
     "comp": "какао тёртое, сахар, какао-масло", "kcal": 563},
    {"k": "caramel", "n": "Солёная карамель", "s": "молочный, хрустящая карамель", "p": 38, "bg": "#ead8bd", "st": "#d0662f", "ink": "#2a1d17", "sub": "#8c5a35",
     "comp": "сахар, какао-масло, молоко сухое, карамель, соль", "kcal": 541},
    {"k": "buckthorn", "n": "Облепиха", "s": "горький, сушёная облепиха", "p": 64, "bg": "#ef8a26", "st": "#3a2a20", "ink": "#2a1d17", "sub": "#5a3418",
     "comp": "какао тёртое, сахар, какао-масло, облепиха сушёная", "kcal": 547},
    {"k": "raspberry", "n": "Малина", "s": "белый, сублимированная малина", "p": 31, "bg": "#f4c6cf", "st": "#b8234a", "ink": "#3b1020", "sub": "#8f2a45",
     "comp": "сахар, какао-масло, молоко сухое, малина сублимированная", "kcal": 552},
]

CSS = r"""
.hero h1{font-size:clamp(40px,5.8vw,84px)}
.pk{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:clamp(20px,3vw,40px);align-items:center}
.stage{min-height:420px;display:grid;place-items:center;border-radius:22px;background:radial-gradient(120% 90% at 50% 20%,#fff 0,#efe9e1 70%);box-shadow:0 0 0 1px var(--line);padding:clamp(16px,3vw,40px);overflow:hidden}
.stage .bar{width:min(560px,100%);transform:perspective(1400px) rotateY(-16deg) rotateX(9deg);filter:drop-shadow(0 30px 30px rgba(40,25,10,.28));transition:transform .5s}
.stage .bar:hover{transform:perspective(1400px) rotateY(-6deg) rotateX(4deg)}
.stage .net{width:100%}
.stage svg{display:block;width:100%;height:auto}
.side{display:grid;gap:16px}
.fls{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.fls button{display:grid;gap:4px;text-align:left;padding:12px;border-radius:14px;border:1px solid var(--line2);background:var(--card);cursor:pointer;font:500 14px var(--fb);color:var(--ink)}
.fls button i{width:100%;height:10px;border-radius:5px}.fls button small{color:var(--mut);font-weight:400}
.fls button.on{box-shadow:0 0 0 2px var(--ink);border-color:transparent}
.spec{display:grid;gap:8px;font-size:14px;color:var(--soft);padding:16px;border-radius:14px;background:var(--card);box-shadow:0 0 0 1px var(--line)}
.spec div{display:flex;justify-content:space-between;gap:12px}.spec b{color:var(--ink);font-weight:500;text-align:right}
.lg{display:flex;flex-wrap:wrap;gap:16px;font-size:13px;color:var(--mut)}.lg span{display:flex;align-items:center;gap:6px}.lg i{width:22px;height:0;border-top:2px solid #e2312d}.lg i.f{border-top:2px dashed #2b7bd8}.lg i.b{border-top:2px dotted #19a463}
.line{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}.line svg{display:block;width:100%;height:auto;border-radius:6px;box-shadow:0 18px 30px -18px rgba(40,25,10,.5)}
.line figure{margin:0;display:grid;gap:8px}.line figcaption{font-size:13px;color:var(--mut)}
@media (max-width:980px){.pk{grid-template-columns:1fr}.line{grid-template-columns:1fr 1fr}}
"""

JS = r"""
(function(){var F=window.CASECFG.fl,cur=0,mode='bar',W=520,H=260;
function bars(x,y,w,h){var s='',p=x,k=0,ws=[2,1,3,1,2,1,1,3,2,1,2,3,1,1,2,1,3,1,2,2,1,3,1,2,1,1,2];while(p<x+w-4){var b=ws[k%ws.length];s+='<rect x="'+p+'" y="'+y+'" width="'+b+'" height="'+h+'" fill="#1a1410"/>';p+=b+(ws[(k+3)%ws.length]);k++}return s}
function front(f,x,y){return '<g transform="translate('+x+' '+y+')"><rect width="'+W+'" height="'+H+'" fill="'+f.bg+'"/>'+
'<path d="M330 0 H400 L360 '+H+' H290 Z" fill="'+f.st+'"/><path d="M406 0 H414 L374 '+H+' H366 Z" fill="'+f.st+'" opacity=".6"/>'+
'<text x="28" y="66" font-family="Unbounded" font-weight="700" font-size="40" letter-spacing="-1" fill="'+f.ink+'">полоса</text>'+
'<text x="30" y="96" font-family="Onest" font-size="15" fill="'+f.sub+'">шоколадная мастерская</text>'+
'<text x="30" y="'+(H-64)+'" font-family="Unbounded" font-weight="600" font-size="20" fill="'+f.ink+'">'+f.n+'</text>'+
'<text x="30" y="'+(H-38)+'" font-family="Onest" font-size="14" fill="'+f.sub+'">'+f.s+'</text>'+
'<circle cx="'+(W-58)+'" cy="70" r="40" fill="none" stroke="'+f.ink+'" stroke-width="2"/><text x="'+(W-58)+'" y="78" text-anchor="middle" font-family="Unbounded" font-weight="700" font-size="21" fill="'+f.ink+'">'+f.p+'%</text>'+
'<text x="'+(W-58)+'" y="128" text-anchor="middle" font-family="Onest" font-size="12" fill="'+f.sub+'">какао</text>'+
'<text x="'+(W-28)+'" y="'+(H-38)+'" text-anchor="end" font-family="Onest" font-weight="500" font-size="15" fill="'+f.ink+'">85 г</text></g>'}
function back(f,x,y){var t='<g transform="translate('+x+' '+y+')"><rect width="'+W+'" height="'+H+'" fill="'+f.bg+'"/><rect x="0" y="0" width="14" height="'+H+'" fill="'+f.st+'"/>'+
'<text x="36" y="44" font-family="Unbounded" font-weight="600" font-size="16" fill="'+f.ink+'">Состав</text><text x="36" y="68" font-family="Onest" font-size="12.5" fill="'+f.ink+'">'+f.comp+'</text>'+
'<text x="36" y="98" font-family="Onest" font-size="12" fill="'+f.sub+'">Пищевая ценность на 100 г: '+f.kcal+' ккал</text>';
['белки','жиры','углеводы'].forEach(function(n,i){t+='<rect x="36" y="'+(118+i*26)+'" width="250" height="20" rx="4" fill="'+f.ink+'" opacity=".08"/><text x="46" y="'+(132+i*26)+'" font-family="Onest" font-size="11.5" fill="'+f.ink+'">'+n+'</text>'});
t+='<rect x="'+(W-176)+'" y="'+(H-104)+'" width="150" height="80" rx="4" fill="#fff"/>'+bars(W-166,H-96,130,52)+'<text x="'+(W-101)+'" y="'+(H-32)+'" text-anchor="middle" font-family="Onest" font-size="10" fill="#1a1410">4 607 183 290 416</text>'+
'<text x="36" y="'+(H-30)+'" font-family="Onest" font-size="11" fill="'+f.sub+'">Хранить при +15…+18 °C · годен 9 месяцев</text></g>';return t}
function sideP(f,x,y,w,h,rot){return '<g transform="translate('+x+' '+y+')"><rect width="'+w+'" height="'+h+'" fill="'+f.st+'"/><text transform="translate('+(w/2+4)+' '+(h/2)+') rotate(90)" text-anchor="middle" font-family="Unbounded" font-weight="600" font-size="12" fill="'+f.bg+'">полоса · '+f.n.toLowerCase()+' · '+f.p+'%</text></g>'}
function net(f){var X=36,Y=50,G=26,S=40,cut='#e2312d',fold='#2b7bd8';var x1=X+G,x2=x1+W,x3=x2+S,x4=x3+W,x5=x4+S;
var s='<svg viewBox="0 0 '+(x5+36)+' '+(H+Y*2+20)+'"><rect width="100%" height="100%" fill="#faf7f2"/>';
s+='<g transform="translate(0 0)"><rect x="'+(X-8)+'" y="'+(Y-8)+'" width="'+(x5-X+16)+'" height="'+(H+16)+'" fill="none" stroke="#19a463" stroke-dasharray="2 4" stroke-width="1.5"/></g>';
s+='<path d="M'+x1+' '+(Y+10)+' H'+X+' V'+(Y+H-10)+' H'+x1+'" fill="'+f.st+'" opacity=".35"/>';
s+=front(f,x1,Y)+sideP(f,x2,Y,S,H)+back(f,x3,Y)+sideP(f,x4,Y,S,H);
[[x1,W],[x3,W]].forEach(function(a){s+='<path d="M'+a[0]+' '+Y+' L'+(a[0]+18)+' '+(Y-38)+' H'+(a[0]+a[1]-18)+' L'+(a[0]+a[1])+' '+Y+'" fill="'+f.bg+'" opacity=".55"/>';s+='<path d="M'+a[0]+' '+(Y+H)+' L'+(a[0]+18)+' '+(Y+H+38)+' H'+(a[0]+a[1]-18)+' L'+(a[0]+a[1])+' '+(Y+H)+'" fill="'+f.bg+'" opacity=".55"/>'});
s+='<path d="M'+x1+' '+(Y+10)+' H'+X+' V'+(Y+H-10)+' H'+x1+' M'+x1+' '+Y+' L'+(x1+18)+' '+(Y-38)+' H'+(x2-18)+' L'+x2+' '+Y+' H'+x3+' L'+(x3+18)+' '+(Y-38)+' H'+(x4-18)+' L'+x4+' '+Y+' H'+x5+' V'+(Y+H)+' H'+x4+' L'+(x4-18)+' '+(Y+H+38)+' H'+(x3+18)+' L'+x3+' '+(Y+H)+' H'+x2+' L'+(x2-18)+' '+(Y+H+38)+' H'+(x1+18)+' L'+x1+' '+(Y+H)+'" fill="none" stroke="'+cut+'" stroke-width="2"/>';
[x1,x2,x3,x4].forEach(function(x){s+='<path d="M'+x+' '+Y+' V'+(Y+H)+'" stroke="'+fold+'" stroke-width="2" stroke-dasharray="8 6"/>'});
[[x1,x2],[x3,x4]].forEach(function(a){s+='<path d="M'+a[0]+' '+Y+' H'+a[1]+' M'+a[0]+' '+(Y+H)+' H'+a[1]+'" stroke="'+fold+'" stroke-width="2" stroke-dasharray="8 6"/>'});
s+='<text x="'+X+'" y="'+(H+Y*2+12)+'" font-family="Onest" font-size="13" fill="#6b625a">Развёртка 1 : 1 · 186 × 82 мм в сложенном виде · картон 300 г/м²</text></svg>';return s}
function draw(){var f=F[cur],st=document.getElementById('stage');
st.innerHTML=mode==='bar'?'<div class="bar"><svg viewBox="0 0 '+W+' '+H+'">'+front(f,0,0)+'</svg></div>':'<div class="net">'+net(f)+'</div>';
document.getElementById('lg').style.display=mode==='net'?'flex':'none';
document.querySelectorAll('#fls button').forEach(function(b,i){b.classList.toggle('on',i===cur)});
document.querySelectorAll('#view button').forEach(function(b){b.classList.toggle('on',b.dataset.v===mode)});
document.getElementById('spec').innerHTML='<div>Вкус<b>'+f.n+'</b></div><div>Какао<b>'+f.p+'%</b></div><div>Энергия на 100 г<b>'+f.kcal+' ккал</b></div><div>Цвет пачки<b>'+f.bg.toUpperCase()+'</b></div>'}
document.getElementById('fls').addEventListener('click',function(e){var b=e.target.closest('button');if(b){cur=+b.dataset.i;draw()}});
document.getElementById('view').addEventListener('click',function(e){var b=e.target.closest('button');if(b){mode=b.dataset.v;draw()}});
document.getElementById('lineup').innerHTML=F.map(function(f){return '<figure><svg viewBox="0 0 '+W+' '+H+'">'+front(f,0,0)+'</svg><figcaption>'+f.n+' · '+f.p+'%</figcaption></figure>'}).join('');
draw()})();
"""


def sv(body, vb="0 0 480 300", bg="#efe9e1"):
    return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="{bg}"/>{body}</svg>'


def mini(f, x, y, w=120, h=60):
    k = w / 520
    return (f'<g transform="translate({x} {y})"><rect width="{w}" height="{h}" fill="{f["bg"]}"/>'
            f'<path d="M{330 * k} 0 H{400 * k} L{360 * k} {h} H{290 * k} Z" fill="{f["st"]}"/>'
            f'<text x="{w * .06}" y="{h * .3}" font-family="Unbounded" font-weight="700" font-size="{w * .08}" fill="{f["ink"]}">полоса</text></g>')


HERO = sv("".join(mini(f, 70 + i * 34, 330 - i * 70, 420, 210) for i, f in enumerate(FL)), "0 0 640 560", "#f3eee7")

SHOW = sv('<path d="M60 120 L420 120 L420 270 L60 270Z" fill="#2a1d17"/><path d="M60 120 L120 40 H420 V120Z" fill="#3a2a20"/>'
          '<text x="80" y="96" font-family="Unbounded" font-weight="700" font-size="30" fill="#f4e9da">полоса</text>'
          + "".join(mini(f, 76 + i * 86, 150 - (i % 2) * 6, 80, 112) for i, f in enumerate(FL))
          + '<text x="240" y="292" text-anchor="middle" font-family="Onest" font-size="12" fill="#6b625a">шоубокс на 24 плитки</text>')
GIFT = sv('<rect x="110" y="70" width="260" height="190" rx="6" fill="#2a1d17"/>' + "".join(f'<rect x="{110 + i * 65}" y="70" width="65" height="190" fill="{f["bg"]}" opacity=".95"/>' for i, f in enumerate(FL))
          + '<rect x="110" y="140" width="260" height="50" fill="#f4e9da"/><text x="240" y="173" text-anchor="middle" font-family="Unbounded" font-weight="700" font-size="22" fill="#2a1d17">полоса · 4 вкуса</text>')
STICK = sv('<circle cx="160" cy="150" r="88" fill="#d0662f"/><text x="160" y="140" text-anchor="middle" font-family="Unbounded" font-weight="700" font-size="22" fill="#fff">новый</text>'
           '<text x="160" y="170" text-anchor="middle" font-family="Unbounded" font-weight="700" font-size="22" fill="#fff">вкус</text>'
           '<rect x="290" y="80" width="130" height="140" rx="10" fill="#fff"/><text x="355" y="128" text-anchor="middle" font-family="Unbounded" font-weight="700" font-size="28" fill="#2a1d17">64%</text>'
           '<text x="355" y="156" text-anchor="middle" font-family="Onest" font-size="13" fill="#6b625a">какао</text><rect x="306" y="176" width="98" height="20" rx="10" fill="#ef8a26"/>')


def cfg() -> dict:
    pk = ('<div class="pk"><div class="stage" id="stage" data-ox></div><div class="side">'
          '<div class="seg" id="view"><button type="button" data-v="bar" class="on">Пачка</button><button type="button" data-v="net">Развёртка</button></div>'
          '<div class="fls" id="fls">' + "".join(f'<button type="button" data-i="{i}"><i style="background:linear-gradient(90deg,{f["bg"]} 60%,{f["st"]} 60%)"></i>{f["n"]}<small>{f["p"]}% какао</small></button>' for i, f in enumerate(FL)) + '</div>'
          '<div class="spec" id="spec"></div>'
          '<div class="lg" id="lg"><span><i></i>рез</span><span><i class="f"></i>сгиб</span><span><i class="b"></i>вылет под обрез 3 мм</span></div></div></div>')
    return {
        "slug": "design/polosa", "brand": "Полоса", "favLetter": "П",
        "layout": 'stack', "header": 'float', "secHead": 'stack', "resStyle": 'grid', "ctaStyle": 'line',  # layout
        "title": "Полоса — упаковка шоколада · YSD DEV",
        "desc": "Дизайн упаковки шоколада: четыре вкуса в одной системе, развёртка с линиями реза и сгиба для типографии, "
                "оборот с составом и штрихкодом, шоубокс, подарочный набор и стикер.",
        "theme": {"bg": "#f6f2ec", "ink": "#2a1d17", "soft": "#5a4c42", "mut": "#8a7c70", "line": "#e6ddd2", "line2": "#d3c6b7",
                  "card": "#ffffff", "alt": "#efe8de", "ac": "#2a1d17", "aci": "#f4e9da", "fh": "Unbounded,sans-serif", "fb": "Onest,sans-serif",
                  "fm": "Onest,sans-serif", "hw": "700", "ht": "-.03em", "cbg": "#2a1d17", "cink": "#f4e9da", "cbtn": "#ef8a26", "cbtni": "#2a1d17", "rc": "#d0662f"},
        "fonts": [("Unbounded", "unbounded", [600, 700], "normal"), ("Onest", "onest", [400, 500], "normal")],
        "css": CSS,
        "hero": {"kicker": "Упаковка продукта", "h1": "Одна полоса — <em>четыре вкуса</em>",
                 "lead": "Упаковка для небольшой шоколадной мастерской. Покупатель на полке различает вкусы по цвету издалека, "
                         "а типография получает развёртку, готовую к печати без доработок.",
                 "art": HERO, "cta": "Собрать пачку", "go": "pack"},
        "facts": [("Клиент", "«Полоса», шоколадная мастерская"), ("Работа", "Упаковка 4 вкусов, шоубокс, подарочный набор"),
                  ("Срок", "5 недель"), ("Формат плитки", "85 г, 186 × 82 мм")],
        "data": {"fl": FL},
        "sections": [
            {"type": "html", "id": "pack", "nav": "Пачка", "kick": "Конструктор", "h2": "Выберите вкус и откройте развёртку",
             "lead": "Полоса меняет наклон и цвет вместе со вкусом. В режиме развёртки видны линии реза и сгиба — так файл уходит в печать.", "html": pk},
            {"type": "html", "id": "line", "nav": "Линейка", "kick": "Линейка", "h2": "На полке вкусы не путаются", "alt": True,
             "lead": "Название и процент какао всегда на одном месте, меняется только цвет — покупатель, который нашёл «свой» вкус, узнаёт его с двух метров.",
             "html": '<div class="line" id="lineup"></div>'},
            {"type": "palette", "id": "color", "nav": "Цвет", "kick": "Цвет", "h2": "Цвет — это вкус", "lead": "Нажмите на цвет — код скопируется.",
             "colors": [(f["n"], f["bg"], f'{f["p"]}% какао') for f in FL] + [("Полоса", "#d0662f", "акцент линейки")]},
            {"type": "gallery", "id": "pos", "nav": "Носители", "kick": "Вокруг пачки", "h2": "Шоубокс, набор и стикер", "alt": True,
             "items": [{"html": SHOW, "cap": "<b>Шоубокс на кассу</b>", "span": 4, "ar": "8/5"}, {"html": GIFT, "cap": "<b>Подарочный набор</b>", "span": 4, "ar": "8/5"},
                       {"html": STICK, "cap": "<b>Стикер для новинки</b>", "span": 4, "ar": "8/5"}]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что дала новая упаковка",
             "stats": [("4", "вкуса в одной системе"), ("0", "правок от типографии"), ("+23%", "продаж в первый месяц на полке"), ("11 дней", "на печать тиража")]},
        ],
        "ctaTitle": "Нужна упаковка для продукта?",
        "js": JS,
    }
