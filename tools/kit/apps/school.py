"""«Камертон» — кабинет музыкальной школы: ученики и абонементы, оплаты и долги, расписание кабинетов, посещения."""
import random

STUDENTS = ["Миша Орлов", "Аня Белова", "Лиза Карпова", "Тимофей Гусев", "Варя Соколова", "Даня Николаев", "Соня Ветрова",
            "Артём Лебедев", "Ева Морозова", "Кирилл Фролов", "Маша Зуева", "Полина Ким", "Глеб Тарасов", "Алиса Демина",
            "Егор Савельев", "Вика Павлова", "Лев Абрамов", "Ксюша Романова", "Федя Голубев", "Настя Комарова"]
PARENTS = ["Ольга", "Ирина", "Наталья", "Дмитрий", "Елена", "Андрей", "Татьяна", "Сергей", "Юлия", "Марина"]
INSTR = [("Фортепиано", "t1"), ("Гитара", "t2"), ("Вокал", "t3"), ("Скрипка", "t4"), ("Фортепиано", "t5"), ("Барабаны", "t6")]
TEACH = {"t1": "Анна Сергеевна", "t2": "Илья Котов", "t3": "Мария Лунёва", "t4": "Ольга Ремизова", "t5": "Вера Ланская", "t6": "Тимур Ахметов"}
ROOMS = [{"id": "r1", "name": "Кабинет 1", "sub": "рояль"}, {"id": "r2", "name": "Кабинет 2", "sub": "пианино"},
         {"id": "r3", "name": "Кабинет 3", "sub": "гитара, вокал"}, {"id": "r4", "name": "Студия", "sub": "барабаны, ансамбль"}]
ROOM_OF = {"Фортепиано": ["r1", "r2"], "Гитара": ["r3"], "Вокал": ["r3", "r2"], "Скрипка": ["r2", "r1"], "Барабаны": ["r4"]}
PRICE = 1450  # урок 45 минут по абонементу


def gen():
    rnd = random.Random(31)
    st = []
    for i, n in enumerate(STUDENTS):
        ins, t = INSTR[i % len(INSTR)]
        bal = rnd.choice([0, 1, 2, 3, 5, 6, 7, 8, 4, 2])
        status = "trial" if i in (6, 15) else ("pause" if i == 11 else "act")
        debt = 0 if bal > 0 or status != "act" else rnd.choice([2900, 4350])
        st.append({"id": f"s{i + 1}", "name": n, "parent": f"{rnd.choice(PARENTS)} ({['мама', 'папа'][rnd.random() < .25]})",
                   "phone": f"+7 9{rnd.randint(10, 99)} •••-••-{rnd.randint(10, 99)}", "ins": ins, "t": t, "bal": bal, "debt": debt,
                   "st": status, "age": rnd.randint(6, 15), "since": rnd.choice(["сентября 2024", "января 2025", "сентября 2025", "октября 2026"])})
    les, n = [], 1
    by_room = {r["id"]: [x for x in st if x["st"] != "pause" and r["id"] in ROOM_OF[x["ins"]]] for r in ROOMS}
    for d in range(0, 6):
        today = set()
        for r in ROOMS:
            t = 14 * 60 + rnd.choice([0, 15, 30])
            while t + 45 <= 21 * 60 + 15:
                free = [x for x in by_room[r["id"]] if x["id"] not in today]
                if rnd.random() < 0.7 and free:
                    x = rnd.choice(free)
                    today.add(x["id"])
                    les.append({"id": f"l{n}", "day": d, "room": r["id"], "start": t, "dur": 45, "sid": x["id"], "who": x["name"],
                                "ins": x["ins"], "teacher": TEACH[x["t"]], "st": "trial" if x["st"] == "trial" else "plan"})
                    n += 1
                    t += 45 + rnd.choice([0, 0, 15])
                else:
                    t += rnd.choice([30, 45, 60])
    pays = []
    for i in range(14):
        s = rnd.choice(st[:18])
        k = rnd.choice([4, 8, 8, 12])
        pays.append({"id": f"П-{5320 - i}", "sid": s["id"], "who": s["name"], "sum": k * PRICE - (k == 12) * 1740, "n": k,
                     "how": rnd.choice(["card", "sbp", "cash", "card"]), "day": -rnd.randint(0, 27)})
    pays.sort(key=lambda p: -p["day"])
    return st, les, pays


def cfg() -> dict:
    st, les, pays = gen()
    pk = [[4, "4 урока — 5 800 ₽"], [8, "8 уроков — 11 600 ₽"], [12, "12 уроков — 15 660 ₽ (скидка 10%)"]]
    return {
        "slug": "apps/school", "brand": "Камертон", "logo": "К", "org": "Музыкальная школа",
        "title": "Камертон — кабинет музыкальной школы: ученики, оплаты, расписание",
        "desc": "Кабинет музыкальной школы: ученики и остаток уроков, приём оплаты и долги, расписание кабинетов, отметка посещений "
                "и напоминания родителям.",
        "user": ["Ирина Павловна", "администратор школы"],
        "theme": {"bg": "#fbf8f2", "side": "#fbf8f2", "sink": "#2b2a33", "sline": "#ece6d9", "son": "#2b2a33", "sonk": "#fbf8f2",
                  "ink": "#2b2a33", "mut": "#837f8c", "line": "#ece6d9", "card": "#ffffff", "ac": "#5b3fd1", "aci": "#ffffff",
                  "fh": '"Bitter",serif', "fb": '"Manrope",sans-serif', "hw": "700", "ht": "-.01em",
                  "ok": "#2b9a66", "warn": "#d58b16", "bad": "#d2453f", "info": "#3b74d9"},
        "fonts": [("Bitter", "bitter", [600, 700], "normal"), ("Manrope", "manrope", [400, 500, 600, 700], "normal")],
        "css": ".org i{background:#ffcf4a;color:#2b2a33;border-radius:50%}.kp.ac{background:#2b2a33;color:#fbf8f2}"
               ".balz{font-weight:700}.balz.z{color:var(--bad)}.balz.l{color:var(--warn)}",
        "about": {"h": "Камертон — кабинет музыкальной школы",
                  "p": ["Администратор видит, у кого сколько уроков осталось, кто должен за абонемент и какие кабинеты свободны. "
                        "Оплату принимает в два нажатия, посещение отмечает прямо в расписании — остаток уроков пересчитывается сам.",
                        "Попробуйте принять оплату у ученика с долгом или отметить урок в расписании."],
                  "f": ["Ученики, абонементы и остаток уроков", "Приём оплаты: карта, СБП, наличные", "Долги и напоминания родителям",
                        "Расписание кабинетов по дням", "Посещения и пропуски по болезни", "Отчёт по выручке за месяц"]},
        "views": [
            {"id": "students", "label": "Ученики", "icon": "users", "type": "table", "entity": "s", "title": "Ученики",
             "sub": "Нажмите на ученика, чтобы принять оплату или напомнить родителю", "search": "Имя ученика или родителя",
             "find": ["name", "parent", "ins"], "filter": "st", "primary": ["Новый ученик", "new"], "sort": ["bal", 1],
             "badge": "D.s.filter(function(r){return r.debt>0}).length",
             "kpis": [["Учеников", "D.s.filter(function(r){return r.st!=='pause'}).length"],
                      ["Долг по абонементам", "sum(D.s,'debt')", "money", "ac", "(function(n){return n+' '+(n%10===1&&n%100!==11?'семья':n%10>=2&&n%10<=4&&(n%100<10||n%100>=20)?'семьи':'семей')})(D.s.filter(function(r){return r.debt>0}).length)"],
                      ["Остался 1 урок или меньше", "D.s.filter(function(r){return r.st==='act'&&r.bal<=1}).length"],
                      ["Пробные на неделе", "D.s.filter(function(r){return r.st==='trial'}).length"]],
             "cols": [["name", "Ученик", "b", "", "", "{age} лет · {parent}"], ["ins", "Инструмент", "", "", "", "{tn}"],
                      ["bal", "Уроков осталось", "html", "r", "'<span class=\"balz '+(r.bal===0?'z':r.bal<=1?'l':'')+'\">'+r.bal+'</span>'"],
                      ["debt", "Долг", "money", "r"], ["st", "Статус", "pill:st"]]},
            {"id": "sched", "label": "Расписание", "icon": "cal", "type": "grid", "entity": "l", "title": "Расписание кабинетов",
             "sub": "Нажмите на урок, чтобы отметить посещение", "days": [0, 1, 2, 3, 4, 5], "res": ROOMS, "resKey": "room",
             "from": 840, "to": 1275, "step": 15, "rh": 20, "tone": "st", "tonePill": "lst", "card": ["{who}", "{ins} · {teacher}"],
             "kpis": [["Уроков в день", "D.l.filter(function(r){return r.day===(A.S&&A.S.sched_d||0)}).length"],
                      ["Отмечено", "D.l.filter(function(r){return r.day===(A.S&&A.S.sched_d||0)&&r.st==='came'}).length"],
                      ["Пропуски", "D.l.filter(function(r){return r.day===(A.S&&A.S.sched_d||0)&&(r.st==='ill'||r.st==='miss')}).length"]]},
            {"id": "pays", "label": "Оплаты", "icon": "money", "type": "table", "entity": "p", "title": "Оплаты",
             "sub": "Абонементы за ноябрь", "search": "Ученик", "find": ["who", "id"], "filter": "how",
             "kpis": [["Получено в ноябре", "sum(D.p,'sum')", "money", "ac"], ["Оплат", "D.p.length"],
                      ["Средний абонемент", "Math.round(sum(D.p,'sum')/D.p.length)", "money"]],
             "cols": [["who", "Ученик", "b", "", "", "{id}"], ["n", "Уроков", "num", "r"], ["sum", "Сумма", "money", "r"],
                      ["how", "Способ", "pill:how"], ["day", "Дата", "date"]]},
            {"id": "log", "label": "Журнал", "icon": "log", "type": "log", "title": "Журнал", "sub": "Оплаты, посещения и напоминания"},
        ],
        "pills": {"st": {"act": ["Учится", "ok"], "trial": ["Пробный", "warn"], "pause": ["Пауза", "idle"]},
                  "how": {"card": ["Карта", "info"], "sbp": ["СБП", "ac"], "cash": ["Наличные", "idle"]},
                  "lst": {"plan": ["По расписанию", "info"], "trial": ["Пробный", "warn"], "came": ["Был", "ok"], "ill": ["Болеет", "idle"], "miss": ["Пропуск", "bad"]}},
        "data": {"s": st, "l": les, "p": pays},
        "cards": {
            "s": {"title": "{name}", "sub": "{ins} · {tn} · учится с {since}",
                  "note": "r.debt>0?['Абонемент закончился, долг '+A.money(r.debt)+'. Напомните родителю или примите оплату.','bad']:r.st==='act'&&r.bal<=1?['Остался '+r.bal+' урок — пора продлевать абонемент.','']:r.st==='trial'?['Пробный урок на этой неделе. После урока отметьте, остаётся ли ученик.','']:null",
                  "fields": [["st", "Статус", "pill:st"], ["parent", "Родитель"], ["phone", "Телефон"], ["bal", "Уроков осталось", "num"],
                             ["debt", "Долг", "money"], ["next", "Ближайший урок", "", "(function(){var l=D.l.filter(function(x){return x.sid===r.id&&x.st!=='came'}).sort(function(a,b){return a.day-b.day||a.start-b.start})[0];return l?A.dwd(l.day)+', '+A.hm(l.start):''})()"]],
                  "actions": [{"label": "Принять оплату", "when": "r.st!=='pause'", "form": "pay"},
                              {"label": "Напомнить об оплате", "when": "r.debt>0||(r.st==='act'&&r.bal<=1)", "fn": "remind", "style": "g"},
                              {"label": "Остаётся учиться", "when": "r.st==='trial'", "set": {"st": "act"}, "log": "После пробного остаётся: {name}", "logSub": "{ins}", "toast": "Отлично! Предложите абонемент на 8 уроков", "icon": "🎉"},
                              {"label": "Снять с паузы", "when": "r.st==='pause'", "set": {"st": "act"}, "log": "Снова учится: {name}", "icon": "▶"}]},
            "l": {"title": "{who}", "sub": "{ins} · {teacher} · {day:dwd}, {start:time}",
                  "fields": [["st", "Отметка", "pill:lst"], ["room", "Кабинет", "", "({r1:'Кабинет 1',r2:'Кабинет 2',r3:'Кабинет 3',r4:'Студия'})[r.room]"],
                             ["bal", "Уроков у ученика", "num", "(A.find('s',r.sid)||{}).bal"]],
                  "actions": [{"label": "Был на уроке", "when": "r.st==='plan'||r.st==='trial'", "fn": "came"},
                              {"label": "Болеет — перенести", "when": "r.st==='plan'", "set": {"st": "ill"}, "log": "Пропуск по болезни: {who}", "logSub": "урок не списан, перенесём", "toast": "Урок не списан. Предложим родителю новое время", "style": "g", "icon": "🤒"},
                              {"label": "Не пришёл", "when": "r.st==='plan'", "fn": "miss", "style": "g"}]},
            "p": {"title": "Оплата {id}", "sub": "{who}", "fields": [["sum", "Сумма", "money"], ["n", "Уроков", "num"], ["how", "Способ", "pill:how"], ["day", "Дата", "date"]]}},
        "forms": {
            "pay": {"title": "Оплата: {name}", "hint": "Урок по абонементу — 1 450 ₽. Чек уйдёт родителю на почту.",
                    "fields": [["n", "Абонемент", "select", pk], ["how", "Способ", "select", [["card", "Картой"], ["sbp", "Через СБП"], ["cash", "Наличными"]]]],
                    "submit": "Принять оплату", "fn": "pay"},
            "new": {"title": "Новый ученик", "entity": "s", "idp": "s", "submit": "Записать на пробный",
                    "fields": [["name", "Имя ученика", "text", None, None, "Например: Петя Иванов", 1], ["age", "Возраст", "number", None, "half", "8"],
                               ["ins", "Инструмент", "select", ["Фортепиано", "Гитара", "Вокал", "Скрипка", "Барабаны"], "half"],
                               ["parent", "Родитель", "text", None, None, "Имя (мама/папа)", 1], ["phone", "Телефон", "tel", None, None, "+7"]],
                    "defaults": {"age": 8}, "add": {"st": "trial", "bal": 1, "debt": 0, "since": "ноября 2026"},
                    "compute": {"t": "({'Фортепиано':'t1','Гитара':'t2','Вокал':'t3','Скрипка':'t4','Барабаны':'t6'})[r.ins]", "tn": "A.TN[r.t]"},
                    "log": "Новый ученик на пробный: {name}", "logSub": "{ins} · {tn}", "toast": "Записали на пробный урок. Родителю ушло приглашение", "icon": "＋"}},
        "log": [["13:05", "💳", "Оплата: Аня Белова, 8 уроков", "11 600 ₽ · карта"], ["12:40", "🔔", "Напоминание об оплате: Тимофей Гусев", "родителю в Telegram"],
                ["вчера", "🎉", "После пробного остаётся: Маша Зуева", "Фортепиано"]],
        "js": r"""
(function(){var A=APP,D=A.D;A.TN=""" + str(TEACH).replace("'", '"') + r""";
A.hooks.init=function(){D.s.forEach(function(s){s.tn=A.TN[s.t]})};
A.hooks.pay=function(x,s){var k=+x.n,sum=k*1450-(k===12?1740:0);var paidDebt=Math.min(s.debt,sum);s.debt-=paidDebt;s.bal+=k-Math.round(paidDebt/1450);if(s.st==='trial')s.st='act';s._fl=1;
 var id='П-'+(5321+D.p.filter(function(p){return +p.id.slice(2)>5320}).length);D.p.unshift({id:id,sid:s.id,who:s.name,sum:sum,n:k,how:x.how,day:0,_fl:1});
 A.log('💳','Оплата: '+s.name+', '+k+' уроков',A.money(sum)+(paidDebt?' · закрыт долг '+A.money(paidDebt):''));A.toast('Оплата принята. Осталось уроков: '+s.bal)};
A.hooks.remind=function(s){A.log('🔔','Напоминание об оплате: '+s.name,'родителю в Telegram');A.toast(s.parent.split(' ')[0]+' получит напоминание в Telegram')};
function mark(l,st,txt){var s=A.find('s',l.sid);l.st=st;l._fl=1;if(s&&st!=='ill'){if(s.bal>0)s.bal--;else if(s.st==='act')s.debt+=1450}A.log(st==='came'?'✓':'✖',txt+': '+l.who,l.ins+' · осталось уроков '+(s?s.bal:0));A.close();A.render();A.badges()}
A.hooks.came=function(l){mark(l,'came','Был на уроке')};A.hooks.miss=function(l){mark(l,'miss','Пропуск без предупреждения')};
})();
""",
    }
