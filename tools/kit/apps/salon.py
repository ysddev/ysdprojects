"""«Локон» — онлайн-запись салона: расписание мастеров по дням, запись в свободное окно, перенос, подтверждение, клиенты."""
import random

SERVICES = [  # название, минут, цена, кто делает
    ("Женская стрижка", 60, 2400, "hair"), ("Мужская стрижка", 45, 1600, "hair"), ("Окрашивание в один тон", 120, 5200, "color"),
    ("Сложное окрашивание", 180, 8900, "color"), ("Укладка", 45, 1800, "hair"), ("Маникюр с покрытием", 90, 2300, "nails"),
    ("Педикюр", 75, 2700, "nails"), ("Брови: коррекция и окрашивание", 45, 1450, "brows")]
MASTERS = [{"id": "m1", "name": "Алина", "sub": "стилист", "kind": "hair"}, {"id": "m2", "name": "Виктория", "sub": "колорист", "kind": "color"},
           {"id": "m3", "name": "Денис", "sub": "барбер-стилист", "kind": "hair"}, {"id": "m4", "name": "Ксения", "sub": "мастер маникюра", "kind": "nails"},
           {"id": "m5", "name": "Мадина", "sub": "бровист", "kind": "brows"}]
CLIENTS = ["Анна Ковалёва", "Ирина Белова", "Ольга Тихонова", "Мария Лебедева", "Екатерина Орлова", "Светлана Жукова", "Наталья Морозова",
           "Юлия Соловьёва", "Татьяна Крылова", "Дарья Фомина", "Полина Егорова", "Вера Никитина", "Алексей Громов", "Игорь Савин",
           "Роман Ершов", "Ксения Петрова", "Людмила Зайцева", "Евгения Голубева", "Марина Кузнецова", "Алёна Медведева"]


def gen():
    rnd = random.Random(17)
    rows, n = [], 1
    for d in range(-3, 7):
        for m in MASTERS:
            svc = [s for s in SERVICES if s[3] == m["kind"] or (m["kind"] == "hair" and s[3] == "hair")]
            t = 600 + rnd.choice([0, 30, 60])
            fill = 0.78 if d in (4, 5) else 0.62
            while t < 1230:
                s = rnd.choice(svc)
                if t + s[1] > 1260:
                    break
                if rnd.random() < fill:
                    st = "came" if d < 0 or (d == 0 and t < 720) else ("new" if d <= 3 and rnd.random() < 0.07 else "ok")
                    if d < 0 and rnd.random() < 0.06:
                        st = "noshow"
                    c = rnd.choice(CLIENTS)
                    rows.append({"id": f"z{n}", "day": d, "m": m["id"], "start": t, "dur": s[1], "svc": s[0], "price": s[2],
                                 "cl": c, "src": rnd.choice(["сайт", "сайт", "Telegram", "звонок", "повторно"]), "st": st,
                                 "hist": [["", "Запись создана: " + rnd.choice(["через сайт", "администратором", "в Telegram-боте"])]]})
                    n += 1
                    t += s[1] + rnd.choice([0, 0, 15, 30])
                else:
                    t += rnd.choice([30, 45, 60])
    clients = []
    for i, c in enumerate(CLIENTS):
        mine = [r for r in rows if r["cl"] == c]
        past = [r for r in mine if r["day"] < 0 or r["st"] == "came"]
        fut = sorted([r for r in mine if r["st"] in ("ok", "new")], key=lambda r: (r["day"], r["start"]))
        visits = len(past) + rnd.randint(2, 19)
        clients.append({"id": f"c{i + 1}", "name": c, "phone": f"+7 9{rnd.randint(10, 99)} •••-••-{rnd.randint(10, 99)}",
                        "visits": visits, "spent": visits * rnd.randint(1700, 4300) // 10 * 10,
                        "last": -rnd.randint(3, 64), "next": fut[0]["day"] if fut else None,
                        "seg": "vip" if visits > 14 else ("new" if visits < 4 else "reg")})
    return rows, clients


def cfg() -> dict:
    rows, clients = gen()
    svc_opts = [[s[0], f"{s[0]} · {s[1]} мин · {s[2]:,} ₽".replace(",", " ")] for s in SERVICES]
    return {
        "slug": "apps/salon", "brand": "Локон", "logo": "Л", "org": "Салон на Петроградской",
        "title": "Локон — онлайн-запись и расписание мастеров салона",
        "desc": "Сервис записи для салона красоты: расписание мастеров по дням, запись в свободное окно, перенос и подтверждение, "
                "неявки, клиенты и загрузка мастеров.",
        "user": ["Софья Миронова", "администратор"],
        "theme": {"bg": "#f7f3f1", "side": "#ffffff", "sink": "#3b2d33", "sline": "#ece4e0", "son": "#f5e6ea", "sonk": "#a4335a",
                  "ink": "#2c2226", "mut": "#8b7d82", "line": "#ece4e0", "card": "#ffffff", "ac": "#a4335a", "aci": "#ffffff",
                  "fh": '"Raleway",sans-serif', "fb": '"Nunito Sans",sans-serif', "hw": "700", "ht": "-.01em",
                  "ok": "#2e9d6a", "info": "#4a72d9", "warn": "#d6911f", "bad": "#d14a4a"},
        "fonts": [("Raleway", "raleway", [600, 700], "normal"), ("Nunito Sans", "nunito-sans", [400, 600, 700], "normal")],
        "css": ".ttl h1{font-weight:700}.org i{border-radius:50%}.kp.ac{background:linear-gradient(135deg,#a4335a,#d0577d)}",
        "about": {"h": "Локон — запись и расписание салона",
                  "p": ["Администратор видит всех мастеров на одном экране, записывает клиента в свободное окно за пару нажатий, "
                        "переносит и подтверждает визиты. Клиенты записываются сами через сайт и Telegram — записи падают сюда же.",
                        "Нажмите на пустую клетку в расписании, чтобы записать клиента, или на запись — чтобы перенести, подтвердить "
                        "или отметить визит."],
                  "f": ["Расписание мастеров по дням с текущим временем", "Запись в свободное окно с проверкой занятости",
                        "Подтверждение, перенос, отмена и неявки", "Клиенты: визиты, сумма, ближайшая запись",
                        "Загрузка и выручка мастеров", "Запись с сайта и из Telegram-бота в то же расписание"]},
        "views": [
            {"id": "sched", "label": "Расписание", "icon": "cal", "type": "grid", "entity": "z", "title": "Расписание",
             "sub": "Нажмите на свободное время, чтобы записать клиента", "days": list(range(0, 7)), "res": MASTERS,
             "resKey": "m", "from": 600, "to": 1260, "step": 30, "rh": 34, "tone": "st", "form": "book",
             "card": ["{cl}", "{svc}"], "primary": ["Записать", "book"],
             "badge": "D.z.filter(function(r){return r.st==='new'}).length",
             "kpis": [["Записей на день", "D.z.filter(function(r){return r.day===(A.S&&A.S.sched_d||0)&&r.st!=='cancel'}).length"],
                      ["Загрузка мастеров", "Math.round(sum(D.z.filter(function(r){return r.day===(A.S&&A.S.sched_d||0)&&r.st!=='cancel'}),'dur')/(5*660)*100)+'%'"],
                      ["Выручка дня", "sum(D.z.filter(function(r){return r.day===(A.S&&A.S.sched_d||0)&&r.st!=='cancel'&&r.st!=='noshow'}),'price')", "money"],
                      ["Ждут подтверждения", "D.z.filter(function(r){return r.st==='new'}).length", "", "ac"]]},
            {"id": "list", "label": "Записи", "icon": "list", "type": "table", "entity": "z", "title": "Все записи",
             "sub": "Сегодня и на неделю вперёд", "where": "r.day>=0&&r.st!=='cancel'", "search": "Клиент или услуга",
             "find": ["cl", "svc"], "filter": "st", "sort": ["day", 1],
             "cols": [["cl", "Клиент", "b", "", "", "{svc}"], ["day", "День", "date"], ["start", "Время", "time"],
                      ["m", "Мастер", "", "", "({m1:'Алина',m2:'Виктория',m3:'Денис',m4:'Ксения',m5:'Мадина'})[r.m]"],
                      ["price", "Сумма", "money", "r"], ["st", "Статус", "pill:st"], ["src", "Откуда", "", "hm"]]},
            {"id": "clients", "label": "Клиенты", "icon": "users", "type": "table", "entity": "cl", "title": "Клиенты",
             "sub": "Постоянные, новые и VIP", "search": "Имя или телефон", "find": ["name", "phone"], "filter": "seg",
             "sort": ["spent", -1],
             "kpis": [["Клиентов в базе", "D.cl.length"], ["Вернулись за 60 дней", "Math.round(D.cl.filter(function(c){return c.last>-60}).length/D.cl.length*100)+'%'"],
                      ["Средний чек", "Math.round(sum(D.cl,'spent')/sum(D.cl,'visits'))", "money"]],
             "cols": [["name", "Клиент", "b", "", "", "{phone}"], ["visits", "Визитов", "num", "r"], ["spent", "Потратил", "money", "r"],
                      ["last", "Был", "date"], ["next", "Следующий визит", "date"], ["seg", "Тип", "pill:seg"]]},
            {"id": "team", "label": "Мастера", "icon": "chart", "type": "table", "entity": "ms", "title": "Мастера",
             "sub": "Загрузка и выручка на неделю вперёд",
             "cols": [["name", "Мастер", "b", "", "", "{sub}"], ["load", "Загрузка", "bar:100", "", "Math.round(sum(D.z.filter(function(z){return z.m===r.id&&z.day>=0&&z.st!=='cancel'}),'dur')/(7*660)*100)"],
                      ["pct", "%", "pct", "r", "Math.round(sum(D.z.filter(function(z){return z.m===r.id&&z.day>=0&&z.st!=='cancel'}),'dur')/(7*660)*100)"],
                      ["rev", "Записано на сумму", "money", "r", "sum(D.z.filter(function(z){return z.m===r.id&&z.day>=0&&z.st!=='cancel'}),'price')"],
                      ["ns", "Неявок за 3 дня", "num", "r", "D.z.filter(function(z){return z.m===r.id&&z.st==='noshow'}).length"]]},
            {"id": "log", "label": "Журнал", "icon": "log", "type": "log", "title": "Журнал", "sub": "Записи, переносы и отмены за сегодня"},
        ],
        "pills": {"st": {"new": ["Новая", "warn"], "ok": ["Подтверждена", "info"], "came": ["Пришёл", "ok"], "noshow": ["Не пришёл", "bad"],
                         "cancel": ["Отменена", "idle"]},
                  "seg": {"vip": ["VIP", "ac"], "reg": ["Постоянный", "info"], "new": ["Новый", "warn"]}},
        "data": {"z": rows, "cl": clients, "ms": [dict(m) for m in MASTERS]},
        "cards": {
            "z": {"title": "{cl}", "sub": "{svc} · {day:dwd}, {start:time}", "hist": 1,
                  "note": "r.st==='new'?['Клиент записался сам. Подтвердите визит: клиенту уйдёт сообщение с адресом.','']:r.st==='noshow'?['Клиент не пришёл. Окно можно отдать листу ожидания.','bad']:null",
                  "fields": [["st", "Статус", "pill:st"], ["svc", "Услуга"], ["m", "Мастер", "", "({m1:'Алина',m2:'Виктория',m3:'Денис',m4:'Ксения',m5:'Мадина'})[r.m]"],
                             ["day", "День", "dwd"], ["t", "Время", "", "A.hm(r.start)+' – '+A.hm(r.start+r.dur)"], ["price", "Стоимость", "money"], ["src", "Записался через"]],
                  "actions": [{"label": "Подтвердить", "when": "r.st==='new'", "set": {"st": "ok"}, "log": "Запись подтверждена: {cl}",
                               "logSub": "{svc} · {day:dwd}, {start:time}", "toast": "Клиенту ушло сообщение с адресом и временем", "icon": "✓"},
                              {"label": "Клиент пришёл", "when": "r.st==='ok'&&r.day<=0", "set": {"st": "came"}, "log": "Визит: {cl}, {svc}",
                               "logSub": "{price:money}", "toast": "Визит отмечен, {price:money} в кассе", "icon": "💇"},
                              {"label": "Перенести", "when": "r.st==='ok'||r.st==='new'", "form": "move", "style": "g"},
                              {"label": "Не пришёл", "when": "r.st==='ok'&&r.day<=0", "set": {"st": "noshow"}, "log": "Неявка: {cl}", "style": "g", "icon": "✖"},
                              {"label": "Отменить", "when": "r.st==='ok'||r.st==='new'", "set": {"st": "cancel"}, "log": "Запись отменена: {cl}",
                               "logSub": "{svc} · {day:dwd}, {start:time} — окно свободно", "toast": "Окно свободно, предложим его листу ожидания", "style": "dz", "icon": "✖"}]},
            "cl": {"title": "{name}", "sub": "{phone}",
                   "fields": [["seg", "Тип", "pill:seg"], ["visits", "Визитов", "num"], ["spent", "Потратил", "money"],
                              ["avg", "Средний чек", "money", "Math.round(r.spent/r.visits)"], ["last", "Последний визит", "date"], ["next", "Следующая запись", "date"]],
                   "actions": [{"label": "Записать", "fn": "bookcl"}]},
            "ms": {"title": "{name}", "sub": "{sub}",
                   "fields": [["n", "Записей на неделю", "num", "D.z.filter(function(z){return z.m===r.id&&z.day>=0&&z.st!=='cancel'}).length"],
                              ["rev", "Записано на сумму", "money", "sum(D.z.filter(function(z){return z.m===r.id&&z.day>=0&&z.st!=='cancel'}),'price')"]],
                   "actions": [{"label": "Открыть расписание", "fn": "tosched"}]}},
        "forms": {
            "book": {"title": "Новая запись", "entity": "z", "idp": "z", "submit": "Записать",
                     "fields": [["cl", "Клиент", "text", None, None, "Имя и фамилия", 1], ["svc", "Услуга", "select", svc_opts],
                                ["m", "Мастер", "select", [[m["id"], f"{m['name']}, {m['sub']}"] for m in MASTERS], "half"],
                                ["day", "День", "select", "[0,1,2,3,4,5,6].map(function(d){return[d,A.dwd(d)]})", "half"],
                                ["start", "Время", "select", "Array.from({length:22},function(_,i){var t=600+i*30;return[t,A.hm(t)]})"]],
                     "defaults": {"m": "m1", "day": 0, "start": 720},
                     "check": "(function(){var s=({" + ",".join(f"'{s[0]}':{s[1]}" for s in SERVICES) + "})[x.svc],st=+x.start,d=+x.day;if(st+s>1260)return'Салон работает до 21:00 — выберите время раньше';"
                              "var c=D.z.filter(function(z){return z.m===x.m&&z.day===d&&z.st!=='cancel'&&z.start<st+s&&st<z.start+z.dur})[0];"
                              "return c?'У мастера в это время '+c.cl+' ('+A.hm(c.start)+'–'+A.hm(c.start+c.dur)+'). Выберите другое время или мастера':''})()",
                     "add": {"st": "ok", "src": "администратор"},
                     "compute": {"day": "+r.day", "start": "+r.start", "dur": "({" + ",".join(f"'{s[0]}':{s[1]}" for s in SERVICES) + "})[r.svc]",
                                 "price": "({" + ",".join(f"'{s[0]}':{s[2]}" for s in SERVICES) + "})[r.svc]"},
                     "hist": "Записал администратор", "log": "Новая запись: {cl}", "logSub": "{svc} · {day:dwd}, {start:time}",
                     "toast": "Записали на {day:dwd}, {start:time}. Клиенту ушло подтверждение", "icon": "＋"},
            "move": {"title": "Перенос: {cl}", "hint": "Сейчас {day:dwd}, {start:time}. Клиент получит сообщение с новым временем.",
                     "fields": [["day", "День", "select", "[0,1,2,3,4,5,6].map(function(d){return[d,A.dwd(d)]})", "half"],
                                ["start", "Время", "select", "Array.from({length:22},function(_,i){var t=600+i*30;return[t,A.hm(t)]})", "half"]],
                     "check": "(function(){var st=+x.start,d=+x.day;if(st+r.dur>1260)return'Салон работает до 21:00';var c=D.z.filter(function(z){return z!==r&&z.m===r.m&&z.day===d&&z.st!=='cancel'&&z.start<st+r.dur&&st<z.start+z.dur})[0];"
                              "return c?'У мастера в это время '+c.cl+' ('+A.hm(c.start)+'–'+A.hm(c.start+c.dur)+')':''})()",
                     "submit": "Перенести",
                     "log": "Перенос: {cl} на {day:dwd}, {start:time}", "toast": "Перенесли. Клиент получил новое время", "icon": "🔁"}},
        "log": [["09:12", "🤖", "Запись из Telegram-бота: Юлия Соловьёва", "Маникюр с покрытием · завтра"],
                ["08:47", "🌐", "Запись с сайта: Полина Егорова", "Женская стрижка · сегодня"],
                ["вчера", "✖", "Неявка: Роман Ершов", "Мужская стрижка"]],
        "js": r"""
(function(){var A=APP;
A.hooks.bookcl=function(c){A.close();A.form('book',null,{cl:c.name})};
A.hooks.tosched=function(){A.close();A.go('sched')};
A.hooks.init=function(){var n=new Date();var nm=n.getHours()*60+n.getMinutes();A.D.z.forEach(function(r){if(r.day===0&&r.start+r.dur<=nm&&r.st==='ok')r.st='came';
 r.hist[0][0]=r.day<0?A.dfmt(r.day-2):'сегодня, 08:'+(10+(+r.id.slice(1))%49)})};
})();
""",
    }
