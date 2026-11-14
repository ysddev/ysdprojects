"""«Холод-Сервис» — система заявок сервисной службы: канбан заявок, сроки реакции, назначение мастера, закрытие с актом."""

TECHS = [{"id": "t1", "name": "Сергей Валиев", "zone": "Север", "skill": "сплит-системы, VRF"},
         {"id": "t2", "name": "Андрей Котов", "zone": "Центр", "skill": "холодильное оборудование"},
         {"id": "t3", "name": "Руслан Ибрагимов", "zone": "Юг", "skill": "вентиляция, чиллеры"},
         {"id": "t4", "name": "Павел Дёмин", "zone": "Запад", "skill": "сплит-системы"}]

T = [  # №, клиент, адрес, оборудование, неисправность, приоритет, статус, мастер, минут до срока, создана (мин назад)
    ("3418", "Кофейня «Зерно»", "ул. Ленина, 14", "Холодильная витрина Carboma", "Не держит температуру, +12 °C", "high", "work", "t2", 38, 96),
    ("3421", "Аптека «Здоровье»", "пр. Мира, 72", "Сплит-система 24 000 BTU", "Капает вода из внутреннего блока", "mid", "onway", "t4", 141, 52),
    ("3422", "ТЦ «Галерея», 2 этаж", "ул. Садовая, 3", "Приточная установка П1", "Шум и вибрация на высоких оборотах", "mid", "assigned", "t3", 205, 41),
    ("3424", "Ресторан «Печь»", "наб. Реки, 8", "Шкаф шоковой заморозки", "Ошибка E3, не включается", "high", "new", None, -17, 77),
    ("3425", "Офис «Вектор»", "ул. Гагарина, 51", "Кассетный кондиционер ×3", "Плановое ТО перед зимой", "low", "new", None, 1385, 24),
    ("3426", "Магазин «Ласточка»", "ул. Чехова, 19", "Холодильная камера", "Обмерзает испаритель", "high", "new", None, 64, 16),
    ("3427", "Клиника «Дента Плюс»", "пр. Победы, 110", "Сплит-система 12 000 BTU", "Не греет в режиме обогрева", "mid", "assigned", "t1", 272, 31),
    ("3410", "Пекарня «Колос»", "ул. Мельничная, 2", "Расстоечный шкаф", "Не набирает влажность", "mid", "done", "t2", None, 410),
    ("3412", "Гостиница «Волна»", "ул. Портовая, 7", "VRF-система", "Ошибка связи наружного блока", "high", "done", "t1", None, 355),
    ("3415", "Фитнес «Пульс»", "ул. Спортивная, 21", "Вентиляция зала", "Не работает вытяжка", "mid", "done", "t3", None, 288),
    ("3419", "Школа № 31", "ул. Школьная, 5", "Сплит-система 9 000 BTU", "Не включается с пульта", "low", "work", "t4", 312, 133),
]
HIST = {"new": "Заявка принята", "assigned": "Назначен мастер", "onway": "Мастер выехал", "work": "Мастер на объекте", "done": "Заявка закрыта"}


def cfg() -> dict:
    rows = []
    for n, cl, addr, eq, iss, pr, st, tech, sla, ago in T:
        steps = ["new", "assigned", "onway", "work", "done"]
        hist = [[f"{(ago - i * max(6, ago // 5)) // 60} ч {(ago - i * max(6, ago // 5)) % 60} мин назад".replace("0 ч ", ""), HIST[s]]
                for i, s in enumerate(steps[:steps.index(st) + 1])]
        rows.append({"id": n, "cl": cl, "addr": addr, "eq": eq, "iss": iss, "pr": pr, "st": st, "tech": tech, "sla0": sla, "ago": ago,
                     "sum": {"3410": 7350, "3412": 18900, "3415": 5650}.get(n), "hist": hist})
    return {
        "slug": "apps/service", "brand": "Холод-Сервис", "logo": "Х", "org": "Сервисная служба · 4 мастера",
        "title": "Холод-Сервис — система заявок сервисной службы",
        "desc": "Система заявок для сервисной службы: канбан заявок, сроки реакции по приоритету, назначение мастера по зоне, "
                "статусы выезда, закрытие с актом работ и суммой.",
        "user": ["Елена Гордеева", "диспетчер"],
        "theme": {"bg": "#eef2f6", "side": "#0f2235", "sink": "#e6eef6", "sline": "#1d3349", "son": "#1f3a56", "sonk": "#7fd4ff",
                  "ink": "#14212e", "mut": "#6a7b8c", "line": "#dbe3eb", "card": "#ffffff", "ac": "#0b79d0", "aci": "#ffffff",
                  "fh": '"Exo 2",sans-serif', "fb": '"Fira Sans",sans-serif', "fm": '"Fira Mono",monospace', "hw": "700", "ht": "0",
                  "colbg": "#e3e9f0", "ok": "#1f9d6b", "warn": "#e08a00", "bad": "#de3b3b", "info": "#0b79d0"},
        "fonts": [("Exo 2", "exo-2", [600, 700], "normal"), ("Fira Sans", "fira-sans", [400, 500, 600], "normal"),
                  ("Fira Mono", "fira-mono", [400, 500], "normal")],
        "css": ".sla{font:500 12px/1 var(--fm);padding:5px 8px;border-radius:6px;background:color-mix(in srgb,var(--ok) 13%,transparent);color:color-mix(in srgb,var(--ok) 80%,var(--ink));white-space:nowrap}"
               ".sla.w{background:color-mix(in srgb,var(--warn) 16%,transparent);color:color-mix(in srgb,var(--warn) 75%,var(--ink))}"
               ".sla.b{background:var(--bad);color:#fff}.sla.n{background:none;color:var(--mut);padding-left:0}"
               ".prio{font-size:11.5px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}.prio.high{color:var(--bad)}.prio.mid{color:var(--warn)}.prio.low{color:var(--mut)}",
        "about": {"h": "Холод-Сервис — заявки сервисной службы",
                  "p": ["Диспетчер принимает заявку, назначает мастера по зоне, видит, кто выехал и кто на объекте, и не пропускает "
                        "сроки реакции. Мастер закрывает заявку с телефона: что сделано, какие запчасти, сумма — клиенту уходит акт.",
                        "Перетащите карточку в другую колонку, назначьте мастера или закройте заявку — сроки и счётчики пересчитаются."],
                  "f": ["Канбан заявок с перетаскиванием", "Срок реакции по приоритету: 1, 4 или 24 часа",
                        "Назначение мастера с учётом зоны и загрузки", "Закрытие заявки с работами, запчастями и суммой",
                        "Заявки с сайта, почты и Telegram в одну очередь", "Отчёт по мастерам и просрочкам"]},
        "views": [
            {"id": "board", "label": "Заявки", "icon": "board", "type": "board", "entity": "t", "field": "st", "title": "Заявки",
             "sub": "Перетащите карточку, чтобы сменить статус", "cols": ["new", "assigned", "onway", "work", "done"],
             "card": ["{cl}", "{iss}", "<span class=\"prio {pr}\">{prl}</span>{slah}"], "primary": ["Новая заявка", "new"],
             "search": "Клиент, адрес, неисправность", "find": ["cl", "addr", "iss", "eq", "id"],
             "badge": "D.t.filter(function(r){return r.st==='new'}).length",
             "moves": {"done": {"form": "close"}},
             "kpis": [["Открыто заявок", "D.t.filter(function(r){return r.st!=='done'}).length"],
                      ["Сроки горят", "D.t.filter(function(r){return r.st!=='done'&&A.left(r)<60}).length", "", "ac", "'меньше часа или уже просрочено'"],
                      ["Закрыто сегодня", "D.t.filter(function(r){return r.st==='done'}).length"],
                      ["Выручка за день", "sum(D.t.filter(function(r){return r.st==='done'}),'sum')", "money"]]},
            {"id": "list", "label": "Все заявки", "icon": "list", "type": "table", "entity": "t", "title": "Все заявки",
             "sub": "Сортировка по сроку реакции", "filter": "st", "search": "Клиент, адрес, неисправность", "find": ["cl", "addr", "iss", "eq", "id"],
             "sort": ["left", 1],
             "cols": [["cl", "Клиент", "b", "", "", "№ {id} · {addr}"], ["iss", "Неисправность", "", "", "", "{eq}"],
                      ["pr", "Приоритет", "html", "", "'<span class=\"prio '+r.pr+'\">'+A.prl(r.pr)+'</span>'"],
                      ["tech", "Мастер", "", "", "A.tn(r.tech)"], ["left", "Срок реакции", "html", "", "A.slah(r)"], ["st", "Статус", "pill:st"]]},
            {"id": "techs", "label": "Мастера", "icon": "users", "type": "table", "entity": "tech", "title": "Мастера",
             "sub": "Кто где и сколько заявок в работе",
             "cols": [["name", "Мастер", "b", "", "", "{skill}"], ["zone", "Зона"],
                      ["now", "Сейчас", "", "", "(function(){var a=D.t.filter(function(t){return t.tech===r.id&&t.st!=='done'});var w=a.filter(function(t){return t.st==='work'||t.st==='onway'})[0];return w?(w.st==='work'?'на объекте: ':'едет: ')+w.cl:'свободен'})()"],
                      ["open", "В работе", "num", "r", "D.t.filter(function(t){return t.tech===r.id&&t.st!=='done'}).length"],
                      ["done", "Закрыто сегодня", "num", "r", "D.t.filter(function(t){return t.tech===r.id&&t.st==='done'}).length"],
                      ["rate", "Оценка клиентов", "", "r", "r.rate"]]},
            {"id": "log", "label": "Журнал", "icon": "log", "type": "log", "title": "Журнал", "sub": "Все действия по заявкам за смену"},
        ],
        "pills": {"st": {"new": ["Новая", "bad"], "assigned": ["Назначена", "warn"], "onway": ["Мастер едет", "info"],
                         "work": ["На объекте", "ac"], "done": ["Закрыта", "ok"]}},
        "data": {"t": rows, "tech": [dict(t, rate=r) for t, r in zip(TECHS, ["4,9", "4,8", "4,7", "4,9"])]},
        "cards": {
            "t": {"title": "{cl}", "sub": "Заявка № {id} · {addr}", "hist": 1,
                  "note": "r.st!=='done'&&A.left(r)<0?['Срок реакции прошёл '+A.dur(-A.left(r))+' назад. Позвоните клиенту и назначьте мастера.','bad']:r.st==='new'?['Срок реакции: '+A.dur(A.left(r))+'. Назначьте мастера.','']:null",
                  "fields": [["st", "Статус", "pill:st"], ["eq", "Оборудование"], ["iss", "Неисправность"], ["prl", "Приоритет", "", "A.prl(r.pr)"],
                             ["tech", "Мастер", "", "r.tech?A.tn(r.tech):''"], ["slah", "Срок реакции", "html", "r.st==='done'?'':A.slah(r)"],
                             ["work", "Что сделано"], ["sum", "Сумма по акту", "money"]],
                  "actions": [{"label": "Назначить мастера", "when": "r.st==='new'", "form": "assign"},
                              {"label": "Мастер выехал", "when": "r.st==='assigned'", "set": {"st": "onway"}, "log": "Мастер выехал: {cl}", "logSub": "заявка № {id}", "icon": "🚐"},
                              {"label": "Мастер на объекте", "when": "r.st==='onway'", "set": {"st": "work"}, "log": "Мастер на объекте: {cl}", "logSub": "заявка № {id}", "icon": "🔧"},
                              {"label": "Закрыть заявку", "when": "r.st==='work'", "form": "close"},
                              {"label": "Сменить мастера", "when": "r.st==='assigned'||r.st==='onway'", "form": "assign", "style": "g"},
                              {"label": "Вернуть в работу", "when": "r.st==='done'", "set": {"st": "work"}, "log": "Заявка возвращена в работу: {cl}", "style": "g", "icon": "↩"}]},
            "tech": {"title": "{name}", "sub": "{zone} · {skill}",
                     "fields": [["rate", "Оценка клиентов"], ["open", "Заявок в работе", "num", "D.t.filter(function(t){return t.tech===r.id&&t.st!=='done'}).length"]]}},
        "forms": {
            "assign": {"title": "Мастер на заявку № {id}", "hint": "{addr} · {eq}",
                       "fields": [["tech", "Мастер", "select", "D.tech.map(function(t){var n=D.t.filter(function(x){return x.tech===t.id&&x.st!=='done'}).length;return[t.id,t.name+' · '+t.zone+' · в работе '+n]})"]],
                       "set": {"st": "assigned"}, "submit": "Назначить", "log": "Назначен мастер: {cl}", "logSub": "заявка № {id}",
                       "hist": "Назначен мастер", "toast": "Мастеру ушло уведомление с адресом и описанием", "icon": "👷"},
            "close": {"title": "Закрыть заявку № {id}", "hint": "Клиент получит акт выполненных работ на почту.",
                      "fields": [["work", "Что сделано", "textarea", None, None, "Например: заменён датчик температуры, проверено давление", 1],
                                 ["sum", "Сумма по акту, ₽", "number", None, None, "4500", 1]],
                      "set": {"st": "done"}, "submit": "Закрыть и отправить акт", "log": "Заявка закрыта: {cl}", "logSub": "{work} · {sum:money}",
                      "hist": "Закрыта: {work}", "toast": "Акт на {sum:money} ушёл клиенту", "icon": "✅"},
            "new": {"title": "Новая заявка", "entity": "t", "submit": "Принять заявку",
                    "fields": [["cl", "Клиент", "text", None, None, "Компания или имя", 1], ["addr", "Адрес", "text", None, None, "Улица, дом", 1],
                               ["eq", "Оборудование", "text", None, None, "Например: сплит-система 12 000 BTU"],
                               ["iss", "Что случилось", "textarea", None, None, "Со слов клиента", 1],
                               ["pr", "Приоритет", "select", [["high", "Срочно — реакция 1 час"], ["mid", "Обычная — 4 часа"], ["low", "Плановая — 24 часа"]]]],
                    "defaults": {"pr": "mid"}, "add": {"st": "new", "tech": None, "ago": 0},
                    "compute": {"sla0": "({high:60,mid:240,low:1440})[r.pr]", "id": "String(3428+D.t.filter(function(x){return +x.id>=3428}).length)"},
                    "hist": "Заявка принята диспетчером", "log": "Новая заявка: {cl}", "logSub": "{iss}", "toast": "Заявка № {id} в очереди", "icon": "＋"}},
        "log": [["11:46", "🔧", "Мастер на объекте: Кофейня «Зерно»", "заявка № 3418"], ["11:20", "🌐", "Заявка с сайта: Магазин «Ласточка»", "Обмерзает испаритель"],
                ["10:58", "✅", "Заявка закрыта: Фитнес «Пульс»", "Заменён ремень вентилятора · 5 650 ₽"]],
        "js": r"""
(function(){var A=APP,T0=Date.now();
A.prl=function(p){return({high:'срочно',mid:'обычная',low:'плановая'})[p]};
A.tn=function(id){var t=A.D.tech.filter(function(x){return x.id===id})[0];return t?t.name:'не назначен'};
A.left=function(r){if(r.sla0==null||r.st==='done')return 1e9;if(r.st==='work')return 1e8;return Math.round(r.sla0-(Date.now()-T0)/60000-(r.st==='new'?0:0))};
A.dur=function(m){m=Math.abs(m);return m>=60?Math.floor(m/60)+' ч '+(m%60)+' мин':m+' мин'};
A.slah=function(r){if(r.st==='done')return'<span class="sla n">закрыта</span>';if(r.st==='work')return'<span class="sla n">на объекте</span>';var l=A.left(r);return'<span class="sla'+(l<0?' b':l<60?' w':'')+'">'+(l<0?'просрочено '+A.dur(l):'осталось '+A.dur(l))+'</span>'};
A.hooks.init=function(){A.D.t.forEach(function(r){r.prl=A.prl(r.pr)});};
A.hooks.before=function(){A.D.t.forEach(function(r){r.slah=A.slah(r);r.left=A.left(r);r.prl=A.prl(r.pr)})};
A.hooks.added=function(r){r.prl=A.prl(r.pr);r.slah=A.slah(r);r.left=A.left(r)};
var r0=A.render;setInterval(function(){if(!document.querySelector('.dr.on,.md.on'))A.render()},30000);
})();
""",
        "init": "D.t.forEach(function(r){r.prl=({high:'срочно',mid:'обычная',low:'плановая'})[r.pr]})",
    }
