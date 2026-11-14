"""«Дачник · поставщикам» — портал поставщиков сети садовых центров: запросы цен, заказы, запись на приёмку, оплаты, рейтинг."""

RFQ = [  # №, товар, объём, срок ответа (дн), статус, моя цена, лучшая цена
    ("Q-1184", "Грунт универсальный 50 л", "2 400 мешков", 2, "open", None, None),
    ("Q-1186", "Семена газона «Спортивный» 1 кг", "900 упаковок", 3, "open", None, None),
    ("Q-1179", "Торф верховой 250 л", "320 тюков", 1, "quoted", 615, 598),
    ("Q-1177", "Удобрение «Осеннее» 2,5 кг", "1 150 упаковок", -1, "won", 342, 342),
    ("Q-1172", "Кора сосны, фракция 15–25 мм, 60 л", "700 мешков", -4, "lost", 389, 361),
    ("Q-1188", "Дренаж керамзит 20 л", "1 600 мешков", 4, "open", None, None),
]
PO = [  # №, что, сумма, статус, поставка через дн, склад
    ("З-50417", "Грунт универсальный 50 л · 1 800 мешков", 619200, "new", 5, "РЦ Север"),
    ("З-50411", "Удобрение «Осеннее» 2,5 кг · 1 150 упак.", 393300, "confirmed", 3, "РЦ Юг"),
    ("З-50406", "Торф верховой 250 л · 240 тюков", 147600, "slot", 1, "РЦ Север"),
    ("З-50398", "Кора сосны 60 л · 400 мешков", 155600, "shipped", 0, "РЦ Юг"),
    ("З-50382", "Грунт для рассады 20 л · 2 200 мешков", 398200, "accepted", -6, "РЦ Север"),
    ("З-50371", "Песок кварцевый 25 кг · 600 мешков", 117000, "accepted", -11, "РЦ Юг"),
]
PAY = [("С-8812", "З-50382", 398200, 9, "wait"), ("С-8796", "З-50371", 117000, -2, "paid"), ("С-8770", "З-50355", 286450, -15, "paid"),
       ("С-8804", "З-50398", 155600, 21, "plan")]


def cfg() -> dict:
    rfq = [{"id": a, "item": b, "qty": c, "due": d, "st": e, "my": f, "best": g, "hist": [["", "Запрос опубликован"]]} for a, b, c, d, e, f, g in RFQ]
    po = [{"id": a, "what": b, "sum": c, "st": d, "day": e, "wh": f, "hist": [["", "Заказ размещён"]]} for a, b, c, d, e, f in PO]
    pay = [{"id": a, "po": b, "sum": c, "due": d, "st": e} for a, b, c, d, e in PAY]
    return {
        "slug": "apps/supplier", "brand": "Дачник", "logo": "Д", "org": "Портал поставщиков",
        "title": "Дачник — портал поставщиков сети садовых центров",
        "desc": "Портал поставщиков розничной сети: запросы цен и предложения, заказы на поставку, запись на приёмку на склад, "
                "оплаты по отсрочке и рейтинг поставщика.",
        "user": ["ООО «Агро-Сад»", "Константин Белов, менеджер"],
        "theme": {"bg": "#f3f6ef", "side": "#1f3a24", "sink": "#e7efe1", "sline": "#2c4a31", "son": "#2f5435", "sonk": "#d6f28a",
                  "ink": "#1d2a1f", "mut": "#6f7e70", "line": "#dfe6d9", "card": "#ffffff", "ac": "#2f7d3c", "aci": "#ffffff",
                  "fh": '"Montserrat",sans-serif', "fb": '"Golos Text",sans-serif', "fm": '"IBM Plex Mono",monospace', "hw": "700", "ht": "-.02em",
                  "ok": "#2f9d55", "warn": "#cf8a14", "bad": "#d0463e", "info": "#3a77c9"},
        "fonts": [("Montserrat", "montserrat", [600, 700], "normal"), ("Golos Text", "golos-text", [400, 500, 600], "normal"),
                  ("IBM Plex Mono", "ibm-plex-mono", [500], "normal")],
        "css": """.org i{background:#d6f28a;color:#1f3a24}.kp.ac{background:#1f3a24}
.rt{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-bottom:16px}
.rt .kp b{font-size:30px}.rt .kp small b{display:inline;font:inherit;color:var(--ok)}
.bars{display:grid;grid-template-columns:repeat(6,1fr);gap:12px;align-items:end;height:200px;padding:10px 4px 0}
.bars div{display:grid;gap:6px;justify-items:center;font-size:12px;color:var(--mut);height:100%;align-content:end}
.bars i{display:block;width:100%;max-width:46px;border-radius:8px 8px 3px 3px;background:var(--ac)}
.bars i.low{background:var(--warn)}.bars b{color:var(--ink);font:500 12px var(--fm)}
.tips{display:grid;gap:10px;margin:0;padding:0;list-style:none}.tips li{padding:12px 14px;border-radius:12px;background:#f3f6ef;font-size:14px}
@media (max-width:760px){.rt{grid-template-columns:1fr}.bars{gap:6px}}""",
        "about": {"h": "Дачник — портал поставщиков",
                  "p": ["Поставщики сами отвечают на запросы цен, подтверждают заказы, записываются на приёмку и видят, когда им "
                        "заплатят. Закупщикам сети не нужно собирать предложения по почте и обзванивать склады.",
                        "Попробуйте отправить предложение на запрос цен, подтвердить заказ и записаться на приёмку."],
                  "f": ["Запросы цен: предложение и итог отбора", "Заказы: подтверждение объёма и даты", "Запись на приёмку в свободное окно склада",
                        "Оплаты по отсрочке с датами", "Рейтинг поставщика: сроки, комплектность, претензии", "Электронные документы через ЭДО"]},
        "views": [
            {"id": "rfq", "label": "Запросы цен", "icon": "doc", "type": "table", "entity": "q", "title": "Запросы цен",
             "sub": "Отправьте цену до окончания приёма предложений", "filter": "st", "pill": "qst", "search": "Товар или номер",
             "find": ["id", "item"], "badge": "D.q.filter(function(r){return r.st==='open'}).length",
             "kpis": [["Ждут вашей цены", "D.q.filter(function(r){return r.st==='open'}).length", "", "ac"],
                      ["Выиграно в ноябре", "D.q.filter(function(r){return r.st==='won'}).length+2"], ["Доля побед", "'41%'"]],
             "cols": [["item", "Товар", "b", "", "", "{id} · {qty}"], ["due", "Приём до", "html", "", "A.dueh(r)"],
                      ["my", "Ваша цена", "money", "r"], ["st", "Статус", "pill:qst"]]},
            {"id": "po", "label": "Заказы", "icon": "box", "type": "table", "entity": "o", "title": "Заказы на поставку",
             "sub": "Подтвердите заказ и запишитесь на приёмку", "filter": "st", "pill": "ost", "search": "Номер или товар", "find": ["id", "what"],
             "badge": "D.o.filter(function(r){return r.st==='new'||r.st==='confirmed'}).length",
             "kpis": [["Заказов в работе", "D.o.filter(function(r){return r.st!=='accepted'}).length"],
                      ["На сумму", "sum(D.o.filter(function(r){return r.st!=='accepted'}),'sum')", "money", "ac"],
                      ["Ближайшая приёмка", "(function(){var s=D.o.filter(function(r){return r.st==='slot'}).sort(function(a,b){return a.day-b.day})[0];return s?A.dfmt(s.day)+(s.slot?', '+s.slot:''):'—'})()"]],
             "cols": [["what", "Заказ", "b", "", "", "{id} · {wh}"], ["sum", "Сумма", "money", "r"], ["day", "Поставка", "date"], ["st", "Статус", "pill:ost"]]},
            {"id": "pay", "label": "Оплаты", "icon": "money", "type": "table", "entity": "p", "title": "Оплаты",
             "sub": "Отсрочка 30 дней с даты приёмки", "filter": "st", "pill": "pst",
             "kpis": [["Ждём оплату", "sum(D.p.filter(function(r){return r.st!=='paid'}),'sum')", "money", "ac"],
                      ["Ближайший платёж", "(function(){var s=D.p.filter(function(r){return r.st==='wait'}).sort(function(a,b){return a.due-b.due})[0];return s?A.dfmt(s.due):'—'})()"],
                      ["Получено в ноябре", "sum(D.p.filter(function(r){return r.st==='paid'}),'sum')", "money"]],
             "cols": [["id", "Счёт", "b", "", "", "по заказу {po}"], ["sum", "Сумма", "money", "r"], ["due", "Дата оплаты", "date"], ["st", "Статус", "pill:pst"]]},
            {"id": "rating", "label": "Рейтинг", "icon": "chart", "type": "custom", "title": "Ваш рейтинг поставщика",
             "sub": "От рейтинга зависит доля в запросах цен и отсрочка"},
            {"id": "log", "label": "Журнал", "icon": "log", "type": "log", "title": "Журнал", "sub": "Предложения, заказы и приёмка"},
        ],
        "pills": {"qst": {"open": ["Ждёт цену", "warn"], "quoted": ["Цена отправлена", "info"], "won": ["Выиграли", "ok"], "lost": ["Не выбраны", "idle"]},
                  "ost": {"new": ["Подтвердите", "bad"], "confirmed": ["Запишитесь на приёмку", "warn"], "slot": ["Окно на приёмку", "info"],
                          "shipped": ["Отгружен", "ac"], "accepted": ["Принят складом", "ok"]},
                  "pst": {"plan": ["По графику", "idle"], "wait": ["Ждёт оплаты", "warn"], "paid": ["Оплачен", "ok"]}},
        "data": {"q": rfq, "o": po, "p": pay},
        "cards": {
            "q": {"title": "{item}", "sub": "Запрос {id} · {qty}", "hist": 1,
                  "note": "r.st==='open'?['Приём предложений '+(r.due<=0?'сегодня до 18:00':'до '+A.dfmt(r.due))+'. Цена — за единицу с доставкой до склада, с НДС.','']:r.st==='lost'?['Выбрали цену '+A.money(r.best)+'. Ваша была на '+Math.round((r.my/r.best-1)*1000)/10+'% выше.','']:r.st==='won'?['Ваше предложение выбрано. Заказ уже в разделе «Заказы».','ok']:null",
                  "fields": [["st", "Статус", "pill:qst"], ["qty", "Объём"], ["due", "Приём до", "date"], ["my", "Ваша цена за ед.", "money"], ["lead", "Срок поставки", "", "r.lead?r.lead+' дн.':''"]],
                  "actions": [{"label": "Отправить цену", "when": "r.st==='open'", "form": "quote"},
                              {"label": "Изменить цену", "when": "r.st==='quoted'", "form": "quote", "style": "g"}]},
            "o": {"title": "Заказ {id}", "sub": "{wh}", "hist": 1,
                  "note": "r.st==='new'?['Подтвердите объём и дату поставки до конца дня, иначе заказ уйдёт другому поставщику.','bad']:r.st==='confirmed'?['Выберите окно на приёмку: без записи склад машину не примет.','']:null",
                  "fields": [["st", "Статус", "pill:ost"], ["what", "Состав"], ["sum", "Сумма", "money"], ["day", "Поставка", "date"], ["slot", "Окно приёмки"], ["upd", "УПД"]],
                  "actions": [{"label": "Подтвердить заказ", "when": "r.st==='new'", "set": {"st": "confirmed"}, "log": "Заказ {id} подтверждён", "logSub": "{what}", "toast": "Подтверждено. Теперь запишитесь на приёмку", "icon": "✓"},
                              {"label": "Записаться на приёмку", "when": "r.st==='confirmed'", "form": "slot"},
                              {"label": "Отгрузили", "when": "r.st==='slot'", "form": "ship"},
                              {"label": "Перенести окно", "when": "r.st==='slot'", "form": "slot", "style": "g"}]},
            "p": {"title": "Счёт {id}", "sub": "по заказу {po}", "fields": [["st", "Статус", "pill:pst"], ["sum", "Сумма", "money"], ["due", "Дата оплаты", "date"]]}},
        "forms": {
            "quote": {"title": "Цена: {item}", "hint": "Объём {qty}. Укажите цену за единицу с доставкой до склада, с НДС.",
                      "fields": [["my", "Цена за единицу, ₽", "number", None, "half", "", 1], ["lead", "Срок поставки, дней", "number", None, "half", "5", 1],
                                 ["note", "Комментарий закупщику", "textarea", None, None, "Например: отгрузка партиями по 400 мешков"]],
                      "set": {"st": "quoted"}, "submit": "Отправить предложение", "log": "Отправлена цена: {item}", "logSub": "{my:money} за ед. · {lead} дн.",
                      "hist": "Предложение: {my:money} за ед.", "toast": "Предложение у закупщика. Итог — после окончания приёма", "icon": "💬"},
            "slot": {"title": "Приёмка: заказ {id}", "hint": "Склад {wh}. Окна по 1 часу, разгрузка до 40 минут.",
                     "fields": [["day", "День", "select", "[1,2,3,4,5].map(function(d){return[d,A.dwd(d)]})", "half"],
                                ["slot", "Окно", "select", ["08:00–09:00", "09:00–10:00", "11:00–12:00", "13:00–14:00", "15:00–16:00"], "half"],
                                ["car", "Машина", "text", None, None, "Госномер, например А123ВС 178", 1]],
                     "check": "(+x.day===2&&x.slot==='09:00–10:00')||(+x.day===1&&x.slot==='08:00–09:00')?'Это окно уже занято другим поставщиком. Выберите другое':''",
                     "set": {"st": "slot"}, "submit": "Записаться", "log": "Запись на приёмку: {id}", "logSub": "{wh} · {day:dwd}, {slot} · {car}",
                     "hist": "Окно приёмки: {slot}", "toast": "Записали. Пропуск для машины придёт на почту", "icon": "🚚"},
            "ship": {"title": "Отгрузка: заказ {id}", "fields": [["upd", "Номер УПД", "text", None, None, "Например: 1187", 1]],
                     "set": {"st": "shipped"}, "submit": "Отправить УПД через ЭДО", "log": "Отгружен заказ {id}", "logSub": "УПД № {upd} отправлен через ЭДО",
                     "hist": "Отгружен, УПД № {upd}", "toast": "УПД ушёл через ЭДО. Склад ждёт машину", "icon": "📦"}},
        "log": [["12:14", "🏆", "Предложение выбрано: Удобрение «Осеннее»", "заказ З-50411 на 393 300 ₽"],
                ["10:02", "📨", "Новый запрос цен: Дренаж керамзит 20 л", "1 600 мешков"],
                ["вчера", "✓", "Заказ З-50382 принят складом", "расхождений нет"]],
        "js": r"""
(function(){var A=APP;
A.dueh=function(r){if(r.st!=='open')return A.esc(A.dfmt(r.due));return'<span class="pl '+(r.due<=1?'bad':r.due<=2?'warn':'idle')+'">'+(r.due<=0?'сегодня':A.dfmt(r.due))+'</span>'};
A.views.rating=function(el){var m=[['июн',91.2],['июл',93.8],['авг',89.6],['сен',95.1],['окт',96.4],['ноя',94.7]];
 el.innerHTML='<div class="rt"><div class="kp ac"><span>Поставки в срок</span><b>94,7%</b><small>норма сети — от 92%</small></div><div class="kp"><span>Комплектность</span><b>98,1%</b><small>привезли столько, сколько заказали</small></div><div class="kp"><span>Претензии по качеству</span><b>2</b><small>за 6 месяцев, обе закрыты</small></div></div>'+
 '<div class="g2"><div class="pane"><h3>Поставки в срок по месяцам</h3><div class="bars">'+m.map(function(x){return'<div><b>'+String(x[1]).replace('.',',')+'%</b><i class="'+(x[1]<92?'low':'')+'" style="height:'+((x[1]-80)*7)+'px"></i>'+x[0]+'</div>'}).join('')+'</div></div>'+
 '<div class="pane"><h3>Как поднять рейтинг</h3><ul class="tips"><li>Записывайтесь на приёмку минимум за 2 дня: в августе 3 поставки сдвинули окно в последний момент.</li><li>Рейтинг выше 95% — отсрочка сокращается с 30 до 21 дня.</li><li>Отвечайте на запросы цен в первые сутки: такие предложения закупщики смотрят первыми.</li></ul></div></div>'};
})();
""",
    }
