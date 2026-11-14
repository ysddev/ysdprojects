"""«Кампус» — система бронирования переговорных коворкинга: сетка комнат по часам, бронь с проверкой вместимости и пересечений,
пакеты часов резидентов, продление и отмена."""
import random

ROOMS = [{"id": "a", "name": "Байкал", "sub": "4 места · 900 ₽/ч", "cap": 4, "price": 900},
         {"id": "b", "name": "Ладога", "sub": "6 мест · 1 200 ₽/ч", "cap": 6, "price": 1200},
         {"id": "c", "name": "Онега", "sub": "8 мест · экран · 1 600 ₽/ч", "cap": 8, "price": 1600},
         {"id": "d", "name": "Селигер", "sub": "12 мест · ВКС · 2 400 ₽/ч", "cap": 12, "price": 2400},
         {"id": "e", "name": "Телефонная", "sub": "1 место · 300 ₽/ч", "cap": 1, "price": 300}]
COMP = [("r1", "Студия «Пиксель»", "Резидент 20", 20), ("r2", "Юристы «Норма»", "Резидент 10", 10), ("r3", "Финтех «Сдвиг»", "Резидент 40", 40),
        ("r4", "Агентство «Шум»", "Резидент 10", 10), ("r5", "Школа «Дельта»", "Разовые", 0), ("r6", "HR «Найм»", "Резидент 20", 20)]
WHAT = ["Планёрка", "Встреча с клиентом", "Собеседование", "Созвон с инвестором", "Ретро спринта", "Обучение", "Презентация макетов", "Переговоры"]


def gen():
    rnd = random.Random(5)
    rows, n = [], 1
    for d in range(-2, 7):
        if d % 7 in (2, 3) and d > 0 and rnd.random() < .3:
            pass
        for r in ROOMS:
            t = 8 * 60 + rnd.choice([0, 30, 60])
            while t < 20 * 60:
                dur = rnd.choice([60, 60, 90, 120]) if r["id"] != "e" else rnd.choice([30, 30, 60])
                if t + dur > 21 * 60:
                    break
                if rnd.random() < (0.55 if d not in (5, 6) else 0.25):
                    c = rnd.choice(COMP)
                    ppl = min(r["cap"], max(1, rnd.randint(r["cap"] // 2, r["cap"])))
                    rows.append({"id": f"b{n}", "day": d, "room": r["id"], "start": t, "dur": dur, "comp": c[0], "cn": c[1],
                                 "what": rnd.choice(WHAT) if r["id"] != "e" else "Звонок", "ppl": ppl,
                                 "sum": r["price"] * dur // 60, "pay": "hours" if c[3] else ("paid" if rnd.random() < .6 else "wait"),
                                 "st": "ok", "hist": [["", "Бронь создана"]]})
                    n += 1
                    t += dur + rnd.choice([0, 30])
                else:
                    t += rnd.choice([30, 60, 90])
    comps = []
    for cid, name, plan, hrs in COMP:
        used = sum(b["dur"] for b in rows if b["comp"] == cid and b["day"] <= 0) / 60
        comps.append({"id": cid, "name": name, "plan": plan, "hrs": hrs, "used": round(used + rnd.randint(2, 9) if hrs else 0, 1),
                      "desks": {"r1": 6, "r2": 3, "r3": 14, "r4": 2, "r5": 0, "r6": 5}[cid], "seg": "res" if hrs else "one"})
    return rows, comps


def cfg() -> dict:
    rows, comps = gen()
    room_js = "{" + ",".join(f"{r['id']}:{{n:'{r['name']}',c:{r['cap']},p:{r['price']}}}" for r in ROOMS) + "}"
    return {
        "slug": "apps/rooms", "brand": "Кампус", "logo": "К", "org": "Коворкинг на Васильевском",
        "title": "Кампус — бронирование переговорных коворкинга",
        "desc": "Система бронирования переговорных: сетка комнат по часам, бронь с проверкой вместимости и пересечений, пакеты "
                "часов резидентов, продление, отмена и оплата разовых броней.",
        "user": ["Мила Чернова", "комьюнити-менеджер"],
        "theme": {"bg": "#f2f2ee", "side": "#111111", "sink": "#f2f2ee", "sline": "#262626", "son": "#d7ff3a", "sonk": "#111111",
                  "ink": "#111111", "mut": "#6e6e68", "line": "#dcdcd4", "card": "#ffffff", "ac": "#111111", "aci": "#d7ff3a",
                  "fh": '"Sofia Sans Condensed",sans-serif', "fb": '"Inter Tight",sans-serif', "hw": "800", "ht": "-.01em",
                  "ok": "#1f9d5a", "warn": "#d99100", "bad": "#e0453c", "info": "#3a6ff0", "idle": "#9a9a92",
                  "r": "6px", "rs": "6px", "csh": "0 0 0 1.5px #111"},
        "fonts": [("Sofia Sans Condensed", "sofia-sans-condensed", [700, 800], "normal"), ("Inter Tight", "inter-tight", [400, 500, 600, 700], "normal")],
        "css": """.ttl h1{font-size:28px;text-transform:uppercase}.kp b{font-size:30px}.kp.ac{background:#d7ff3a;color:#111}
.org i{background:#d7ff3a;color:#111;border-radius:4px}.bk{border-radius:4px}.pl{border-radius:4px}.ch,.dt button{border-radius:4px}
.bk{background:color-mix(in srgb,var(--tc,var(--ac)) 12%,#fff);box-shadow:inset 0 0 0 1.5px var(--tc,#111)}
.hrs{display:flex;align-items:center;gap:8px}.hrs .bar2{flex:1;min-width:80px}""",
        "about": {"h": "Кампус — бронирование переговорных",
                  "p": ["Резиденты бронируют переговорные сами с сайта и из Telegram, а менеджер видит загрузку всех комнат на одном экране. "
                        "Система не даст занять комнату дважды и посадить 9 человек в комнату на 6, а часы из пакета резидента считает сама.",
                        "Нажмите на свободное время, чтобы забронировать, или на бронь, чтобы продлить или отменить."],
                  "f": ["Сетка комнат по получасам на неделю", "Проверка пересечений и вместимости", "Пакеты часов резидентов и разовая оплата",
                        "Продление на 30 минут, если комната свободна", "Бесплатная отмена за 2 часа", "Бронь с сайта, из Telegram и с планшета у двери"]},
        "views": [
            {"id": "grid", "label": "Переговорные", "icon": "cal", "type": "grid", "entity": "b", "title": "Переговорные",
             "sub": "Нажмите на свободное время, чтобы забронировать", "days": list(range(0, 7)), "res": ROOMS, "resKey": "room", "where": "r.st==='ok'",
             "from": 480, "to": 1260, "step": 30, "rh": 26, "tone": "pay", "tonePill": "pay", "form": "book",
             "card": ["{cn}", "{what} · {ppl} чел."], "primary": ["Забронировать", "book"],
             "kpis": [["Броней на день", "D.b.filter(function(r){return r.day===(A.S&&A.S.grid_d||0)&&r.st==='ok'}).length"],
                      ["Загрузка комнат", "Math.round(sum(D.b.filter(function(r){return r.day===(A.S&&A.S.grid_d||0)&&r.st==='ok'}),'dur')/(5*780)*100)+'%'", "", "ac"],
                      ["Разовые к оплате", "sum(D.b.filter(function(r){return r.st==='ok'&&r.pay==='wait'}),'sum')", "money"]]},
            {"id": "list", "label": "Брони", "icon": "list", "type": "table", "entity": "b", "title": "Брони", "sub": "С сегодняшнего дня",
             "where": "r.day>=0", "filter": "pay", "search": "Компания или повод", "find": ["cn", "what"], "sort": ["day", 1],
             "badge": "D.b.filter(function(r){return r.st==='ok'&&r.pay==='wait'}).length",
             "cols": [["cn", "Компания", "b", "", "", "{what} · {ppl} чел."], ["room", "Комната", "", "", "A.RM[r.room].n"], ["day", "День", "date"],
                      ["t", "Время", "", "", "A.hm(r.start)+'–'+A.hm(r.start+r.dur)"], ["sum", "Стоимость", "money", "r"], ["pay", "Оплата", "pill:pay"],
                      ["st", "Статус", "pill:st", "hm"]]},
            {"id": "res", "label": "Резиденты", "icon": "users", "type": "table", "entity": "c", "title": "Резиденты и гости",
             "sub": "Пакеты часов переговорных на ноябрь", "filter": "seg",
             "cols": [["name", "Компания", "b", "", "", "{plan} · мест: {desks}"],
                      ["h", "Часы пакета", "html", "", "r.hrs?'<div class=\"hrs\"><div class=\"bar2\"><i style=\"width:'+Math.min(100,r.used/r.hrs*100)+'%;background:'+(r.used>r.hrs?'var(--bad)':'var(--ac)')+'\"></i></div><span class=\"num\">'+A.num(r.used)+' / '+r.hrs+'</span></div>':'—'"],
                      ["left", "Осталось часов", "num", "r", "r.hrs?Math.max(0,r.hrs-r.used):null"], ["seg", "Тип", "pill:seg"]]},
            {"id": "log", "label": "Журнал", "icon": "log", "type": "log", "title": "Журнал", "sub": "Брони, продления и отмены"},
        ],
        "pills": {"pay": {"hours": ["Из пакета часов", "info"], "paid": ["Оплачено", "ok"], "wait": ["Ждёт оплаты", "warn"]},
                  "st": {"ok": ["Активна", "ok"], "cancel": ["Отменена", "idle"]},
                  "seg": {"res": ["Резидент", "ac"], "one": ["Разовые брони", "idle"]}},
        "data": {"b": rows, "c": comps},
        "cards": {
            "b": {"title": "{cn}", "sub": "{what} · {day:dwd}", "hist": 1,
                  "note": "r.st==='cancel'?['Бронь отменена, комната свободна.','']:r.pay==='wait'?['Разовая бронь: оплата '+A.money(r.sum)+' по ссылке до начала встречи.','']:null",
                  "fields": [["room", "Комната", "", "A.RM[r.room].n+' · '+A.RM[r.room].c+' мест'"], ["t", "Время", "", "A.hm(r.start)+' – '+A.hm(r.start+r.dur)"],
                             ["ppl", "Участников", "num"], ["sum", "Стоимость", "money"], ["pay", "Оплата", "pill:pay"]],
                  "actions": [{"label": "Продлить на 30 минут", "when": "r.st==='ok'", "fn": "extend"},
                              {"label": "Отметить оплату", "when": "r.st==='ok'&&r.pay==='wait'", "set": {"pay": "paid"}, "log": "Оплачена бронь: {cn}", "logSub": "{sum:money}", "icon": "💳", "style": "g"},
                              {"label": "Отменить", "when": "r.st==='ok'", "fn": "cancel", "style": "dz"}]},
            "c": {"title": "{name}", "sub": "{plan}", "fields": [["hrs", "Часов в пакете", "num"], ["used", "Использовано", "num"], ["desks", "Рабочих мест", "num"]],
                  "actions": [{"label": "Забронировать для них", "fn": "bookc"}]}},
        "forms": {
            "book": {"title": "Бронь переговорной", "entity": "b", "idp": "b", "submit": "Забронировать",
                     "fields": [["comp", "Кто бронирует", "select", [[c[0], c[1]] for c in COMP]],
                                ["room", "Комната", "select", [[r["id"], f"{r['name']} · {r['sub']}"] for r in ROOMS]],
                                ["day", "День", "select", "[0,1,2,3,4,5,6].map(function(d){return[d,A.dwd(d)]})", "half"],
                                ["start", "Начало", "select", "Array.from({length:25},function(_,i){var t=480+i*30;return[t,A.hm(t)]})", "half"],
                                ["dur", "Длительность", "select", [[30, "30 минут"], [60, "1 час"], [90, "1,5 часа"], [120, "2 часа"], [180, "3 часа"]], "half"],
                                ["ppl", "Участников", "number", None, "half"], ["what", "Повод", "text", None, None, "Например: встреча с клиентом"]],
                     "defaults": {"comp": "r1", "room": "b", "day": 0, "start": 600, "dur": 60, "ppl": 4, "what": "Встреча"},
                     "check": "(function(){var R=A.RM[x.room],st=+x.start,d=+x.day,du=+x.dur;if(+x.ppl>R.c)return'«'+R.n+'» вмещает '+R.c+' чел., а участников '+x.ppl+'. Выберите комнату побольше';"
                              "if(st+du>1260)return'Коворкинг работает до 21:00';var c=D.b.filter(function(b){return b.room===x.room&&b.day===d&&b.st==='ok'&&b.start<st+du&&st<b.start+b.dur})[0];"
                              "return c?'«'+R.n+'» занята с '+A.hm(c.start)+' до '+A.hm(c.start+c.dur)+' ('+c.cn+'). Выберите другое время или комнату':''})()",
                     "add": {"st": "ok"},
                     "compute": {"day": "+r.day", "start": "+r.start", "dur": "+r.dur", "ppl": "+r.ppl", "cn": "A.find('c',r.comp).name",
                                 "sum": "A.RM[r.room].p*r.dur/60", "pay": "A.find('c',r.comp).hrs?'hours':'wait'"},
                     "hist": "Бронь создана менеджером", "log": "Новая бронь: {cn}", "logSub": "{day:dwd}, {start:time} · {what}",
                     "toast": "Забронировано. Приглашение ушло в календарь участникам", "icon": "＋"}},
        "log": [["11:32", "📱", "Бронь с сайта: Финтех «Сдвиг»", "Селигер · 14:00–16:00"], ["10:05", "⏩", "Продление: Юристы «Норма»", "Ладога до 11:30"],
                ["вчера", "✖", "Отмена: Агентство «Шум»", "за 3 часа, бесплатно"]],
        "js": r"""
(function(){var A=APP,D=A.D;A.RM=""" + room_js + r""";
A.hooks.added=function(r){var c=A.find('c',r.comp);if(c&&c.hrs)c.used=Math.round((c.used+r.dur/60)*10)/10};
A.hooks.extend=function(b){var e=b.start+b.dur,c=D.b.filter(function(x){return x!==b&&x.room===b.room&&x.day===b.day&&x.st==='ok'&&x.start<e+30&&e<x.start+x.dur})[0];
 if(c||e+30>1260){A.toast(c?'Не продлить: с '+A.hm(c.start)+' комнату занимает '+c.cn:'Коворкинг работает до 21:00');return}
 b.dur+=30;b.sum=A.RM[b.room].p*b.dur/60;b._fl=1;b.hist.push(['сегодня','Продлена до '+A.hm(b.start+b.dur)]);var cc=A.find('c',b.comp);if(cc&&cc.hrs)cc.used=Math.round((cc.used+.5)*10)/10;
 A.log('⏩','Продление: '+b.cn,A.RM[b.room].n+' до '+A.hm(b.start+b.dur));A.toast('Продлили до '+A.hm(b.start+b.dur));A.render();A.open('b',b.id)};
A.hooks.cancel=function(b){var n=new Date(),nm=n.getHours()*60+n.getMinutes(),free=b.day>0||b.start-nm>=120;b.st='cancel';b._fl=1;
 b.hist.push(['сегодня','Отменена'+(free?' бесплатно':' позже чем за 2 часа')]);var cc=A.find('c',b.comp);if(free&&cc&&cc.hrs)cc.used=Math.max(0,Math.round((cc.used-b.dur/60)*10)/10);
 A.log('✖','Отмена: '+b.cn,A.RM[b.room].n+' · '+A.dwd(b.day)+', '+A.hm(b.start)+(free?' · бесплатно':' · час списан'));A.toast(free?'Отменили. Часы вернулись в пакет':'Отменили. Позже чем за 2 часа — время списано');A.close();A.render()};
A.hooks.bookc=function(c){A.close();A.go('grid');A.form('book',null,{comp:c.id})};
})();
""",
    }
