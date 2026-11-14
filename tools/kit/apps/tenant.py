"""«Меридиан» — кабинет арендатора бизнес-центра: счета и оплата, показания счётчиков, заявки в управляющую компанию, пропуска."""


def cfg() -> dict:
    inv = [{"id": "Б-11/27", "what": "Аренда офиса 512, ноябрь", "sum": 186400, "due": 1, "st": "open", "kind": "rent"},
           {"id": "Б-11/28", "what": "Коммунальные услуги, октябрь", "sum": 14872, "due": 6, "st": "open", "kind": "util"},
           {"id": "Б-11/09", "what": "Парковка, 2 места, ноябрь", "sum": 9000, "due": -4, "st": "late", "kind": "park"},
           {"id": "Б-10/27", "what": "Аренда офиса 512, октябрь", "sum": 186400, "due": -30, "st": "paid", "kind": "rent"},
           {"id": "Б-10/28", "what": "Коммунальные услуги, сентябрь", "sum": 12935, "due": -25, "st": "paid", "kind": "util"}]
    meters = [{"id": "e1", "name": "Электричество, день", "unit": "кВт·ч", "prev": 48213, "rate": 9.84, "cur": None},
              {"id": "e2", "name": "Электричество, ночь", "unit": "кВт·ч", "prev": 17654, "rate": 4.17, "cur": None},
              {"id": "w1", "name": "Холодная вода", "unit": "м³", "prev": 1288.4, "rate": 61.2, "cur": None},
              {"id": "w2", "name": "Горячая вода", "unit": "м³", "prev": 402.7, "rate": 248.9, "cur": None}]
    req = [{"id": "У-3381", "cat": "Кондиционер", "text": "В переговорной шумит внутренний блок", "st": "work", "day": -1, "who": "инженер Павлов",
            "hist": [["вчера, 15:20", "Заявка создана"], ["вчера, 16:05", "Назначен инженер Павлов"]]},
           {"id": "У-3376", "cat": "Уборка", "text": "Генеральная уборка после переезда отдела", "st": "plan", "day": 2, "who": "клининг «Блеск»",
            "hist": [["12 ноября", "Заявка создана"], ["13 ноября", "Согласована дата"]]},
           {"id": "У-3364", "cat": "Электрика", "text": "Не горит свет в санузле на 5 этаже", "st": "done", "day": -5, "who": "электрик Сомов",
            "hist": [["9 ноября", "Заявка создана"], ["9 ноября", "Выполнено за 1 ч 40 мин"]], "rate": 5},
           {"id": "У-3359", "cat": "Мебель", "text": "Собрать 4 стола и 2 тумбы", "st": "done", "day": -7, "who": "служба эксплуатации",
            "hist": [["7 ноября", "Выполнено"]], "rate": 4}]
    passes = [{"id": "P-7781", "guest": "Иван Рыбаков", "day": 0, "time": "15:00", "car": "", "st": "act"},
              {"id": "P-7779", "guest": "Курьер СДЭК", "day": 0, "time": "весь день", "car": "", "st": "used"},
              {"id": "P-7783", "guest": "Ольга Ветрова", "day": 1, "time": "11:30", "car": "М428КТ 178", "st": "act"},
              {"id": "P-7770", "guest": "Сергей Мамонтов", "day": -2, "time": "10:00", "car": "", "st": "used"}]
    return {
        "slug": "apps/tenant", "brand": "Меридиан", "logo": "М", "org": "Бизнес-центр · кабинет арендатора",
        "title": "Меридиан — кабинет арендатора бизнес-центра",
        "desc": "Кабинет арендатора бизнес-центра: счета и оплата, передача показаний счётчиков с проверкой, заявки в управляющую "
                "компанию, пропуска для гостей и машин.",
        "user": ["ООО «Ростра Консалт»", "офис 512 · Анна Кириллова"],
        "theme": {"bg": "#eef0f3", "side": "#ffffff", "sink": "#1b2230", "sline": "#e3e6eb", "son": "#e9edf7", "sonk": "#2346c8",
                  "ink": "#1b2230", "mut": "#737c8c", "line": "#e3e6eb", "card": "#ffffff", "ac": "#2346c8", "aci": "#ffffff",
                  "fh": '"Wix Madefor Display",sans-serif', "fb": '"Wix Madefor Text",sans-serif', "fm": '"JetBrains Mono",monospace',
                  "hw": "700", "ht": "-.02em", "ok": "#1f9d6b", "warn": "#cf8b17", "bad": "#d8433f", "info": "#2346c8"},
        "fonts": [("Wix Madefor Display", "wix-madefor-display", [600, 700], "normal"), ("Wix Madefor Text", "wix-madefor-text", [400, 500, 600], "normal"),
                  ("JetBrains Mono", "jetbrains-mono", [500], "normal")],
        "css": """.org i{background:linear-gradient(135deg,#2346c8,#5b7cff)}
.qa{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:16px}
.qa button{display:flex;align-items:center;gap:12px;padding:16px;border-radius:var(--r);background:var(--card);box-shadow:var(--csh,0 0 0 1px var(--line));text-align:left;font-weight:600}
.qa button:hover{box-shadow:0 0 0 1.5px var(--ac)}.qa button i{width:40px;height:40px;border-radius:12px;background:#e9edf7;color:var(--ac);display:grid;place-items:center;font-style:normal;flex:none}
.qa small{display:block;font-weight:400;color:var(--mut);font-size:12.5px}
.ann{display:grid;gap:10px}.ann div{padding:12px 14px;border-radius:12px;background:#fff7e8;font-size:14px}.ann b{display:block}
.ann div.i{background:#eef2ff}
.qr{display:grid;justify-items:center;gap:8px;padding:12px;background:#f6f7f9;border-radius:12px;margin-bottom:14px}
.qr svg{width:150px;height:150px;background:#fff;padding:8px;border-radius:8px}
@media (max-width:760px){.qa{grid-template-columns:1fr}}""",
        "about": {"h": "Меридиан — кабинет арендатора",
                  "p": ["Арендатор оплачивает счета, передаёт показания и заказывает пропуска сам, без писем и звонков в управляющую "
                        "компанию. Управляющая компания получает заявки в одну очередь и видит, сколько времени уходит на каждую.",
                        "Попробуйте передать показания счётчиков — система проверит их и посчитает сумму."],
                  "f": ["Счета: аренда, коммунальные, парковка", "Показания счётчиков с проверкой ошибок", "Заявки в УК со статусами и оценкой",
                        "Пропуска для гостей и машин с QR-кодом", "Объявления управляющей компании", "Документы: акты, сверки, договор"]},
        "views": [
            {"id": "home", "label": "Главная", "icon": "home", "type": "custom", "title": "Офис 512", "sub": "ООО «Ростра Консалт» · договор аренды до 31.08.2027"},
            {"id": "inv", "label": "Счета", "icon": "money", "type": "table", "entity": "i", "title": "Счета", "sub": "Оплата картой или по счёту",
             "filter": "st", "pill": "ist", "badge": "D.i.filter(function(r){return r.st!=='paid'}).length",
             "kpis": [["К оплате", "sum(D.i.filter(function(r){return r.st!=='paid'}),'sum')", "money", "ac"],
                      ["Просрочено", "sum(D.i.filter(function(r){return r.st==='late'}),'sum')", "money"]],
             "cols": [["what", "Счёт", "b", "", "", "№ {id}"], ["sum", "Сумма", "money", "r"], ["due", "Оплатить до", "date"], ["st", "Статус", "pill:ist"]]},
            {"id": "meters", "label": "Показания", "icon": "gauge", "type": "table", "entity": "m", "title": "Показания счётчиков",
             "sub": "Передайте до 25 ноября — иначе начислим по среднему", "badge": "D.m.filter(function(r){return r.cur==null}).length",
             "kpis": [["Передано", "D.m.filter(function(r){return r.cur!=null}).length+' из '+D.m.length", "", "ac"],
                      ["Сумма по показаниям", "sum(D.m.filter(function(r){return r.cur!=null}),function(r){return(r.cur-r.prev)*r.rate})", "money"]],
             "cols": [["name", "Счётчик", "b", "", "", "тариф {rate} ₽ за {unit}"], ["prev", "Прошлые", "num", "r"],
                      ["cur", "Текущие", "html", "r", "r.cur==null?'<span class=\"pl warn\">передать</span>':'<span class=\"num\">'+A.num(r.cur)+'</span>'"],
                      ["d", "Расход", "num", "r", "r.cur==null?null:r.cur-r.prev"], ["s", "Сумма", "money", "r", "r.cur==null?null:(r.cur-r.prev)*r.rate"]]},
            {"id": "req", "label": "Заявки в УК", "icon": "tool", "type": "table", "entity": "r", "title": "Заявки в управляющую компанию",
             "sub": "Ремонт, уборка, кондиционеры, мебель", "filter": "st", "pill": "rst", "primary": ["Новая заявка", "req"],
             "cols": [["cat", "Заявка", "b", "", "", "№ {id} · {text}"], ["who", "Исполнитель"], ["day", "Дата", "date"], ["st", "Статус", "pill:rst"]]},
            {"id": "pass", "label": "Пропуска", "icon": "key", "type": "table", "entity": "p", "title": "Пропуска", "sub": "Для гостей и машин",
             "filter": "st", "pill": "pst", "primary": ["Заказать пропуск", "pass"],
             "cols": [["guest", "Гость", "b", "", "", "№ {id}"], ["day", "День", "date"], ["time", "Время"], ["car", "Машина"], ["st", "Статус", "pill:pst"]]},
            {"id": "log", "label": "Журнал", "icon": "log", "type": "log", "title": "Журнал", "sub": "Оплаты, показания, заявки и пропуска"},
        ],
        "pills": {"ist": {"open": ["Ждёт оплаты", "warn"], "late": ["Просрочен", "bad"], "paid": ["Оплачен", "ok"]},
                  "rst": {"new": ["Принята", "info"], "plan": ["Согласована дата", "warn"], "work": ["В работе", "ac"], "done": ["Выполнена", "ok"]},
                  "pst": {"act": ["Действует", "ok"], "used": ["Использован", "idle"], "cancel": ["Отменён", "idle"]}},
        "data": {"i": inv, "m": meters, "r": req, "p": passes},
        "cards": {
            "i": {"title": "{what}", "sub": "Счёт № {id}",
                  "note": "r.st==='late'?['Срок оплаты прошёл '+A.dfmt(r.due)+'. Пени 0,1% в день начисляются с завтрашнего дня.','bad']:null",
                  "fields": [["st", "Статус", "pill:ist"], ["sum", "Сумма", "money"], ["vat", "В том числе НДС 22%", "money", "Math.round(r.sum*22/122)"], ["due", "Оплатить до", "date"]],
                  "actions": [{"label": "Оплатить {sum:money}", "when": "r.st!=='paid'", "form": "pay"}]},
            "m": {"title": "{name}", "sub": "Тариф {rate} ₽ за {unit}",
                  "fields": [["prev", "Прошлые показания", "num"], ["cur", "Текущие", "num"], ["s", "К оплате", "money", "r.cur==null?null:(r.cur-r.prev)*r.rate"]],
                  "actions": [{"label": "Передать показания", "form": "meter"}]},
            "r": {"title": "{cat}", "sub": "Заявка № {id}", "hist": 1,
                  "fields": [["st", "Статус", "pill:rst"], ["text", "Описание"], ["who", "Исполнитель"], ["day", "Дата", "date"], ["rate", "Ваша оценка", "", "r.rate?'★'.repeat(r.rate):''"]],
                  "actions": [{"label": "Оценить работу", "when": "r.st==='done'&&!r.rate", "form": "rate"},
                              {"label": "Работа не выполнена", "when": "r.st==='done'", "set": {"st": "work"}, "log": "Заявка возвращена: {cat}", "logSub": "№ {id}", "style": "g", "icon": "↩"}]},
            "p": {"title": "Пропуск: {guest}", "sub": "№ {id}", "extra": "r.st==='act'?A.qr(r.id):''",
                  "fields": [["st", "Статус", "pill:pst"], ["day", "День", "date"], ["time", "Время"], ["car", "Машина"]],
                  "actions": [{"label": "Отменить пропуск", "when": "r.st==='act'", "set": {"st": "cancel"}, "log": "Пропуск отменён: {guest}", "style": "dz", "icon": "✖"}]}},
        "forms": {
            "pay": {"title": "Оплата: {what}", "hint": "Сумма {sum:money}.", "fields": [["how", "Способ", "select", [["card", "Картой"], ["bill", "Платёжкой с расчётного счёта"]]]],
                    "submit": "Оплатить", "set": {"st": "paid"}, "log": "Оплачен счёт № {id}", "logSub": "{what} · {sum:money}", "toast": "Оплата принята. Акт придёт в ЭДО", "icon": "💳"},
            "meter": {"title": "{name}", "hint": "Прошлые показания: {prev} {unit}.",
                      "fields": [["cur", "Текущие показания", "number", None, None, "", 1]],
                      "check": "+x.cur<r.prev?'Новые показания меньше прошлых ('+A.num(r.prev)+'). Проверьте цифры':(+x.cur-r.prev)>(r.prev*0.08)?'Расход почти втрое выше обычного. Если цифры верны, напишите в заявку — проверим счётчик':''",
                      "submit": "Передать", "log": "Показания: {name}", "logSub": "{cur} {unit}", "toast": "Показания приняты", "icon": "📟"},
            "rate": {"title": "Оценка: {cat}", "fields": [["rate", "Оценка", "select", [[5, "★★★★★ отлично"], [4, "★★★★ хорошо"], [3, "★★★ так себе"], [2, "★★ плохо"]]],
                                                        ["comm", "Комментарий", "textarea"]],
                     "submit": "Оценить", "log": "Оценка заявки № {id}: {rate} из 5", "toast": "Спасибо! Оценку увидит руководитель службы", "icon": "★"},
            "req": {"title": "Заявка в управляющую компанию", "entity": "r", "submit": "Отправить",
                    "fields": [["cat", "Что случилось", "select", ["Кондиционер", "Электрика", "Сантехника", "Уборка", "Мебель", "Доступ и ключи", "Другое"]],
                               ["text", "Описание", "textarea", None, None, "Где и что именно", 1]],
                    "add": {"st": "new", "who": "назначим в течение 30 минут", "day": 0},
                    "compute": {"id": "'У-'+(3382+D.r.filter(function(x){return +x.id.slice(2)>3381}).length)"},
                    "hist": "Заявка создана", "log": "Новая заявка: {cat}", "logSub": "{text}", "toast": "Заявка № {id} принята. Диспетчер назначит исполнителя", "icon": "🛠"},
            "pass": {"title": "Пропуск для гостя", "entity": "p", "submit": "Заказать",
                     "fields": [["guest", "Гость", "text", None, None, "Имя и фамилия", 1], ["day", "День", "select", "[0,1,2,3,4,5].map(function(d){return[d,A.dwd(d)]})", "half"],
                                ["time", "Время", "select", ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"], "half"],
                                ["car", "Госномер машины", "text", None, None, "Если гость на машине"]],
                     "add": {"st": "act"}, "compute": {"id": "'P-'+(7784+D.p.filter(function(x){return +x.id.slice(2)>7783}).length)", "day": "+r.day"},
                     "log": "Пропуск: {guest}", "logSub": "{day:dwd}, {time}", "toast": "Пропуск готов. QR-код ушёл гостю по СМС", "icon": "🔑"}},
        "log": [["вчера", "🛠", "Заявка № У-3381 в работе", "инженер Павлов"], ["12 ноя", "💳", "Оплачен счёт № Б-10/28", "14 872 ₽"],
                ["11 ноя", "📢", "Объявление УК: отключение горячей воды", "18 ноября, 10:00–14:00"]],
        "js": r"""
(function(){var A=APP,D=A.D;
A.hooks.changed=function(r,a){if(r.cur!=null&&D.m.indexOf(r)>=0){r.cur=+r.cur}};
A.qr=function(seed){var n=21,s=0,h='';for(var i=0;i<seed.length;i++)s=(s*31+seed.charCodeAt(i))>>>0;function rnd(){s=(s*1103515245+12345)>>>0;return s/4294967296}
 function f(x,y){return(x<7&&y<7)||(x>=n-7&&y<7)||(x<7&&y>=n-7)}function fo(x,y){var c=[[0,0],[n-7,0],[0,n-7]];for(var k=0;k<3;k++){var dx=x-c[k][0],dy=y-c[k][1];if(dx>=0&&dx<7&&dy>=0&&dy<7)return dx===0||dy===0||dx===6||dy===6||(dx>=2&&dx<=4&&dy>=2&&dy<=4)}return false}
 for(var y=0;y<n;y++)for(var x=0;x<n;x++){var on=f(x,y)?fo(x,y):rnd()<.48;if(on)h+='<rect x="'+x+'" y="'+y+'" width="1" height="1"/>'}
 return'<div class="qr"><svg viewBox="0 0 '+n+' '+n+'" fill="#1b2230">'+h+'</svg><small>Покажите код на ресепшене или у шлагбаума</small></div>'};
A.views.home=function(el){var due=D.i.filter(function(i){return i.st!=='paid'}),m=D.m.filter(function(x){return x.cur==null}).length,r=D.r.filter(function(x){return x.st!=='done'}).length;
 el.innerHTML='<div class="kpis"><div class="kp ac"><span>К оплате</span><b>'+A.money(due.reduce(function(s,i){return s+i.sum},0))+'</b><small>'+due.length+' счёта, ближайший — '+A.dfmt(Math.min.apply(null,due.map(function(i){return i.due}).concat([99])))+'</small></div>'+
 '<div class="kp"><span>Показания</span><b>'+(m?'не переданы: '+m:'переданы')+'</b><small>до 25 ноября</small></div><div class="kp"><span>Заявки в работе</span><b>'+r+'</b><small>среднее время решения 3 ч 20 мин</small></div><div class="kp"><span>Пропуска на сегодня</span><b>'+D.p.filter(function(p){return p.day===0&&p.st==='act'}).length+'</b><small>гости и машины</small></div></div>'+
 '<div class="qa"><button type="button" data-form="pass"><i>🔑</i><span>Пропуск для гостя<small>QR-код придёт гостю по СМС</small></span></button><button type="button" data-form="req"><i>🛠</i><span>Заявка в УК<small>ремонт, уборка, кондиционер</small></span></button><button type="button" data-go="meters"><i>📟</i><span>Передать показания<small>4 счётчика, до 25 ноября</small></span></button></div>'+
 '<div class="g2"><div class="pane"><h3>Счета к оплате</h3><ul class="lg">'+due.map(function(i){return'<li data-open="i:'+i.id+'" style="cursor:pointer"><i>💳</i><div>'+A.esc(i.what)+'<small style="display:block">'+(i.st==='late'?'просрочен '+A.dfmt(i.due):'до '+A.dfmt(i.due))+'</small></div><small class="num">'+A.money(i.sum)+'</small></li>'}).join('')+'</ul></div>'+
 '<div class="pane"><h3>Объявления управляющей компании</h3><div class="ann"><div><b>18 ноября, 10:00–14:00 — отключение горячей воды</b>Плановая промывка труб, корпус Б.</div><div class="i"><b>С 1 декабря — зимний режим парковки</b>Въезд с ул. Морской, шлагбаум 2.</div><div class="i"><b>Новогодний декор холла</b>Работы 20–22 декабря после 19:00.</div></div></div></div>'};
})();
""",
    }
