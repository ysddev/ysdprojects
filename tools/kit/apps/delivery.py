"""«Шустрик» — панель доставки: заказы по этапам, курьеры и их загрузка, зоны доставки на карте с ценой и временем."""

ZONES = [
    {"id": "z1", "name": "Центр", "fee": 0, "min": 900, "eta": 35, "color": "#ff6b2c",
     "pts": "300,140 540,120 610,240 550,350 320,360 250,250", "lx": 430, "ly": 245},
    {"id": "z2", "name": "Северный", "fee": 149, "min": 1200, "eta": 50, "color": "#3a86ff",
     "pts": "40,30 830,30 830,190 610,240 540,120 300,140 250,250 40,230", "lx": 600, "ly": 80},
    {"id": "z3", "name": "Заречье", "fee": 249, "min": 1500, "eta": 65, "color": "#8338ec",
     "pts": "40,230 250,250 320,360 550,350 610,240 830,190 830,500 40,500", "lx": 430, "ly": 450},
]
COURIERS = [("k1", "Тимур", "вело", 410, 210), ("k2", "Даниил", "авто", 610, 150), ("k3", "Марат", "вело", 350, 300),
            ("k4", "Олег", "авто", 520, 420), ("k5", "Света", "самокат", 450, 180), ("k6", "Ильдар", "авто", 690, 330)]
O = [  # №, адрес, зона, состав, сумма, этап, курьер, мин в работе, x, y
    ("7731", "ул. Пушкина, 12, кв 45", "z1", "Пицца «Пепперони» ×2, морс", 1890, "new", None, 2, 380, 180),
    ("7730", "ул. Береговая, 3, офис 8", "z3", "Сет «Филадельфия», мисо ×2", 2460, "cooking", None, 9, 300, 410),
    ("7729", "пр. Победы, 40, кв 112", "z2", "Бургер «Гриль» ×3, картофель", 2235, "cooking", None, 14, 640, 120),
    ("7727", "ул. Садовая, 18, кв 7", "z1", "Пицца «Четыре сыра», салат", 1540, "ready", None, 21, 470, 260),
    ("7726", "ул. Лесная, 52", "z3", "Сет «Горячий» ×2, лимонад", 3870, "ready", None, 23, 600, 430),
    ("7724", "ул. Гагарина, 9, кв 31", "z1", "Пицца ×3, соус ×3", 2970, "onway", "k3", 31, 360, 300),
    ("7723", "пр. Мира, 101, кв 5", "z2", "Роллы «Калифорния» ×2", 1380, "onway", "k2", 38, 700, 70),
    ("7721", "ул. Кирова, 6, кв 90", "z1", "Бургер «Классик», шейк", 990, "onway", "k5", 46, 440, 150),
    ("7718", "ул. Речная, 24, кв 11", "z3", "Пицца «Маргарита», морс ×2", 1320, "done", "k1", 51, 220, 350),
    ("7716", "ул. Мира, 2, офис 401", "z1", "Сет «Обед» ×6", 4740, "done", "k4", 44, 500, 320),
    ("7712", "ул. Озёрная, 15, кв 3", "z2", "Пицца ×2, роллы", 2690, "done", "k2", 39, 590, 70),
]


def cfg() -> dict:
    orders = [{"id": n, "addr": a, "zone": z, "items": it, "sum": s, "st": st, "kur": k, "age": age, "x": x, "y": y,
               "hist": [["", "Заказ принят с сайта"]]} for n, a, z, it, s, st, k, age, x, y in O]
    kur = [{"id": i, "name": n, "tr": t, "x": x, "y": y, "st": "off" if i == "k6" else "free"} for i, n, t, x, y in COURIERS]
    return {
        "slug": "apps/delivery", "brand": "Шустрик", "logo": "Ш", "org": "Доставка из 3 кухонь",
        "title": "Шустрик — панель доставки: заказы, курьеры, зоны",
        "desc": "Панель службы доставки: заказы по этапам от кухни до двери, назначение курьера, загрузка курьеров, карта зон "
                "с ценой доставки, минимальной суммой и временем.",
        "user": ["Артур Хасанов", "старший смены"],
        "theme": {"bg": "#141519", "side": "#0d0e11", "sink": "#e9e9ee", "sline": "#24262c", "son": "#25211d", "sonk": "#ff8a4c",
                  "ink": "#ececf1", "mut": "#8d8f99", "line": "#272930", "card": "#1c1e23", "ac": "#ff6b2c", "aci": "#ffffff",
                  "fh": '"Unbounded",sans-serif', "fb": '"Onest",sans-serif', "fm": '"JetBrains Mono",monospace', "hw": "600", "ht": "-.03em",
                  "colbg": "#191b20", "line2": "#3a3d46", "ok": "#2fc47f", "warn": "#f2b33d", "bad": "#ff4d5e", "info": "#4c9dff", "idle": "#6c707c",
                  "csh": "0 0 0 1px #272930"},
        "fonts": [("Unbounded", "unbounded", [500, 600], "normal"), ("Onest", "onest", [400, 500, 600], "normal"),
                  ("JetBrains Mono", "jetbrains-mono", [500], "normal")],
        "css": """
.ttl h1{font-size:20px}.kp b{font-size:22px}
.md input,.md select,.md textarea{background:#141519}
.mapw{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,1fr);gap:16px;align-items:start}
.map{background:#101114;border-radius:var(--r);box-shadow:0 0 0 1px var(--line);overflow:hidden}
.map svg{display:block;width:100%;height:auto}
.map .zn{cursor:pointer;transition:fill-opacity .2s}.map .zn:hover{fill-opacity:.3}
.map .rd{stroke:#2a2c33;stroke-width:6;fill:none;stroke-linecap:round}.map .rv{stroke:#1d3550;stroke-width:22;fill:none;stroke-linecap:round}
.map text{font:600 17px var(--fb);fill:#fff;pointer-events:none}
.map .kc{cursor:pointer}.map .op{cursor:pointer}
.lgd{display:flex;gap:14px;flex-wrap:wrap;font-size:12.5px;color:var(--mut);padding:10px 14px;border-top:1px solid var(--line)}
.lgd i{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px;vertical-align:-1px}
.zc{display:grid;gap:10px}
.zr{display:grid;grid-template-columns:12px 1fr auto;gap:12px;align-items:center;background:var(--card);border-radius:12px;padding:14px;box-shadow:0 0 0 1px var(--line);cursor:pointer}
.zr:hover{box-shadow:0 0 0 1px var(--ac)}
.zr>i{width:12px;height:12px;border-radius:50%}
.zr b{display:block}.zr small{color:var(--mut);font-size:12.5px}
.zr strong{font:500 15px var(--fm)}
@media (max-width:1100px){.mapw{grid-template-columns:1fr}}
""",
        "about": {"h": "Шустрик — панель доставки",
                  "p": ["Старший смены видит каждый заказ от кухни до двери, отдаёт готовые заказы свободным курьерам и следит, "
                        "чтобы никто не опаздывал. Зоны доставки, цена и минимальная сумма меняются здесь же и сразу работают на сайте.",
                        "Перетащите заказ в следующую колонку или откройте карточку: можно назначить курьера и закрыть доставку."],
                  "f": ["Заказы по этапам: принят, готовится, готов, в пути, доставлен", "Назначение свободного курьера",
                        "Опоздания: заказ в работе дольше обещанного", "Курьеры: где, что везут, сколько доставок",
                        "Карта зон с ценой, минимальной суммой и временем", "Заказы с сайта, приложения и агрегаторов в одной ленте"]},
        "views": [
            {"id": "orders", "label": "Заказы", "icon": "board", "type": "board", "entity": "o", "field": "st", "title": "Заказы",
             "sub": "Перетащите заказ в следующую колонку или откройте его", "cols": ["new", "cooking", "ready", "onway", "done"],
             "card": ["№ {id} · {addr}", "{items}", "<span class=\"num\">{sum:money}</span>{ageh}"], "colSum": "sum",
             "search": "Адрес или номер", "find": ["id", "addr", "items"], "moves": {"onway": {"form": "give"}},
             "badge": "D.o.filter(function(r){return r.st==='ready'}).length",
             "kpis": [["В работе", "D.o.filter(function(r){return r.st!=='done'}).length"],
                      ["Опаздывают", "D.o.filter(function(r){return r.st!=='done'&&A.late(r)>0}).length", "", "ac", "'дольше обещанного времени зоны'"],
                      ["Среднее время доставки", "Math.round(sum(D.o.filter(function(r){return r.st==='done'}),'age')/Math.max(1,D.o.filter(function(r){return r.st==='done'}).length))+' мин'"],
                      ["Выручка смены", "sum(D.o,'sum')+184630", "money"]]},
            {"id": "map", "label": "Карта и зоны", "icon": "map", "type": "custom", "title": "Карта и зоны",
             "sub": "Нажмите на зону, чтобы поменять цену доставки, минимальную сумму или время"},
            {"id": "kur", "label": "Курьеры", "icon": "truck", "type": "table", "entity": "k", "title": "Курьеры",
             "sub": "Кто свободен, кто везёт и сколько доставок за смену", "filter": "st",
             "cols": [["name", "Курьер", "b", "", "", "{tr}"], ["st", "Статус", "pill:kst"],
                      ["now", "Везёт", "", "", "D.o.filter(function(o){return o.kur===r.id&&o.st==='onway'}).map(function(o){return'№ '+o.id}).join(', ')||'—'"],
                      ["n", "Доставок за смену", "num", "r", "D.o.filter(function(o){return o.kur===r.id&&o.st==='done'}).length+({k1:6,k2:8,k3:5,k4:7,k5:4,k6:0})[r.id]"]],
             "pill": "kst"},
            {"id": "log", "label": "Журнал", "icon": "log", "type": "log", "title": "Журнал смены", "sub": "Заказы, курьеры и изменения зон"},
        ],
        "pills": {"st": {"new": ["Принят", "info"], "cooking": ["Готовится", "warn"], "ready": ["Готов", "ac"], "onway": ["В пути", "info"], "done": ["Доставлен", "ok"]},
                  "kst": {"free": ["Свободен", "ok"], "busy": ["Везёт заказ", "info"], "off": ["Не на смене", "idle"]}},
        "data": {"o": orders, "k": kur, "zones": ZONES},
        "cards": {
            "o": {"title": "Заказ № {id}", "sub": "{addr}", "hist": 1,
                  "note": "r.st!=='done'&&A.late(r)>0?['Опаздывает на '+A.late(r)+' мин: обещали '+A.zone(r.zone).eta+' мин. Предупредите клиента.','bad']:null",
                  "fields": [["st", "Этап", "pill:st"], ["items", "Состав"], ["sum", "Сумма", "money"], ["zn", "Зона", "", "A.zone(r.zone).name+' · '+A.zone(r.zone).eta+' мин'"],
                             ["age", "В работе", "", "r.age+' мин'"], ["kur", "Курьер", "", "r.kur?A.kn(r.kur):''"]],
                  "actions": [{"label": "Начать готовить", "when": "r.st==='new'", "set": {"st": "cooking"}, "log": "Готовим заказ № {id}", "icon": "🍳"},
                              {"label": "Заказ готов", "when": "r.st==='cooking'", "set": {"st": "ready"}, "log": "Готов к выдаче: № {id}", "icon": "📦"},
                              {"label": "Передать курьеру", "when": "r.st==='ready'", "form": "give"},
                              {"label": "Доставлен", "when": "r.st==='onway'", "fn": "done"}]},
            "k": {"title": "{name}", "sub": "{tr}", "fields": [["st", "Статус", "pill:kst"]],
                  "actions": [{"label": "Вывести на смену", "when": "r.st==='off'", "set": {"st": "free"}, "log": "Курьер на смене: {name}", "icon": "▶"},
                              {"label": "Снять со смены", "when": "r.st==='free'", "set": {"st": "off"}, "log": "Курьер ушёл со смены: {name}", "style": "g", "icon": "⏸"}]},
            "zones": {"title": "Зона «{name}»", "sub": "Изменения сразу работают на сайте и в приложении",
                      "fields": [["fee", "Доставка", "", "r.fee?A.money(r.fee):'бесплатно'"], ["min", "Минимальный заказ", "money"], ["eta", "Обещаем привезти за", "", "r.eta+' мин'"],
                                 ["n", "Заказов сейчас", "num", "D.o.filter(function(o){return o.zone===r.id&&o.st!=='done'}).length"]],
                      "actions": [{"label": "Изменить условия", "form": "zone"}]}},
        "forms": {
            "give": {"title": "Курьер для заказа № {id}", "hint": "{addr} · {items}",
                     "fields": [["kur", "Курьер", "select", "D.k.filter(function(k){return k.st!=='off'}).map(function(k){var n=D.o.filter(function(o){return o.kur===k.id&&o.st==='onway'}).length;return[k.id,k.name+' · '+k.tr+(n?' · везёт '+n:' · свободен')]})"]],
                     "set": {"st": "onway"}, "submit": "Передать", "log": "Заказ № {id} у курьера", "logSub": "{addr}", "hist": "Передан курьеру",
                     "toast": "Клиенту ушло: курьер в пути", "icon": "🛵"},
            "zone": {"title": "Зона «{name}»", "hint": "Цена доставки, минимальный заказ и время для клиентов.",
                     "fields": [["fee", "Доставка, ₽", "number", None, "half"], ["min", "Минимальный заказ, ₽", "number", None, "half"], ["eta", "Время доставки, мин", "number"]],
                     "submit": "Сохранить", "log": "Зона «{name}»: доставка {fee:money}, от {min:money}, {eta} мин", "toast": "Сохранено. На сайте уже новые условия", "icon": "🗺"}},
        "log": [["19:42", "🛵", "Заказ № 7721 у курьера", "ул. Кирова, 6"], ["19:30", "⚠", "Опоздание: заказ № 7712", "доставлен за 39 мин при обещанных 50 — в срок"],
                ["19:05", "🗺", "Зона «Заречье»: доставка 249 ₽", "было 199 ₽"]],
        "js": r"""
(function(){var A=APP,D=A.D,T0=Date.now();
A.zone=function(id){return D.zones.filter(function(z){return z.id===id})[0]};A.kn=function(id){return(A.find('k',id)||{}).name};
A.age=function(r){return r.st==='done'?r.age:r.age+Math.floor((Date.now()-T0)/60000)};
A.late=function(r){return A.age(r)-A.zone(r.zone).eta};
A.hooks.before=function(){D.o.forEach(function(r){var l=A.late(r);r.ageh=r.st==='done'?'<span class="pl ok">'+r.age+' мин</span>':'<span class="pl '+(l>0?'bad':l>-10?'warn':'idle')+'">'+A.age(r)+' мин</span>'});
 D.k.forEach(function(k){if(k.st!=='off')k.st=D.o.some(function(o){return o.kur===k.id&&o.st==='onway'})?'busy':'free'})};
A.hooks.done=function(o){o.st='done';o.age=A.age(o);o._fl=1;o.hist.push(['сегодня','Доставлен за '+o.age+' мин']);var l=A.late(o);
 A.log('✅','Доставлен № '+o.id+' за '+o.age+' мин',l>0?'опоздание '+l+' мин':'в срок');A.toast(l>0?'Доставлен с опозданием на '+l+' мин':'Доставлен вовремя');A.close();A.render();A.badges()};
A.views.map=function(el){var h='<div class="mapw"><div class="map"><svg viewBox="0 0 860 520" role="img" aria-label="Карта зон доставки">';
 h+='<rect width="860" height="520" fill="#101114"/><path class="rv" d="M-10 300 C 150 260 260 330 420 300 S 700 250 870 290"/>';
 ['M40 120 L820 160','M120 480 L760 60','M200 20 L260 510','M560 10 L620 510','M20 400 L840 380'].forEach(function(d){h+='<path class="rd" d="'+d+'"/>'});
 D.zones.slice().reverse().forEach(function(z){h+='<polygon class="zn" data-open="zones:'+z.id+'" points="'+z.pts+'" fill="'+z.color+'" fill-opacity=".16" stroke="'+z.color+'" stroke-width="2"/>'});
 D.zones.forEach(function(z){var p=z.pts.split(' ').map(function(x){return x.split(',').map(Number)}),cx=0,cy=0;p.forEach(function(q){cx+=q[0];cy+=q[1]});cx/=p.length;cy/=p.length;
  cx=z.lx;cy=z.ly;h+='<text x="'+cx+'" y="'+cy+'" text-anchor="middle">'+z.name+' · '+(z.fee?z.fee+' ₽':'бесплатно')+'</text>'});
 D.o.filter(function(o){return o.st!=='done'}).forEach(function(o){var l=A.late(o);h+='<g class="op" data-open="o:'+o.id+'"><circle cx="'+o.x+'" cy="'+o.y+'" r="9" fill="'+(l>0?'#ff4d5e':'#ffffff')+'"/><circle cx="'+o.x+'" cy="'+o.y+'" r="3.5" fill="#141519"/></g>'});
 D.k.filter(function(k){return k.st!=='off'}).forEach(function(k){h+='<g class="kc" data-open="k:'+k.id+'"><circle cx="'+k.x+'" cy="'+k.y+'" r="13" fill="'+(k.st==='busy'?'#4c9dff':'#2fc47f')+'" stroke="#0d0e11" stroke-width="3"/><text x="'+k.x+'" y="'+(k.y+4.5)+'" text-anchor="middle" style="font-size:11px">'+k.name[0]+'</text></g>'});
 h+='</svg><div class="lgd"><span><i style="background:#fff"></i>заказ</span><span><i style="background:#ff4d5e"></i>опаздывает</span><span><i style="background:#2fc47f"></i>курьер свободен</span><span><i style="background:#4c9dff"></i>курьер везёт</span></div></div><div class="zc">';
 D.zones.forEach(function(z){var n=D.o.filter(function(o){return o.zone===z.id&&o.st!=='done'}).length;h+='<div class="zr" data-open="zones:'+z.id+'"><i style="background:'+z.color+'"></i><div><b>'+z.name+'</b><small>от '+A.money(z.min)+' · '+z.eta+' мин · заказов сейчас '+n+'</small></div><strong>'+(z.fee?A.money(z.fee):'0 ₽')+'</strong></div>'});
 el.innerHTML=h+'</div></div>'};
var tick=setInterval(function(){if(!document.querySelector('.dr.on,.md.on'))A.render()},30000);
})();
""",
    }
