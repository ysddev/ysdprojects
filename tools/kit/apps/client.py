"""«Оттиск» — кабинет клиента типографии: заказы со статусами, утверждение макета, счета и оплата, документы, обращения."""

JS = r"""
(function(){var A=APP,D=A.D,esc=A.esc,money=A.money;
A.views.home=function(el){var act=D.orders.filter(function(o){return o.st!=='done'}),pay=D.inv.filter(function(i){return i.st!=='paid'}),proof=D.orders.filter(function(o){return o.st==='proof'});
 var next=act.filter(function(o){return o.st==='ready'||o.st==='print'}).sort(function(a,b){return a.due-b.due})[0];
 var h='<div class="kpis"><div class="kp ac"><span>Заказов в работе</span><b>'+act.length+'</b><small>'+proof.length+' ждут вашего решения</small></div>'+
  '<div class="kp"><span>К оплате</span><b class="num">'+money(pay.reduce(function(s,i){return s+i.sum},0))+'</b><small>'+pay.length+' '+(pay.length===1?'счёт':pay.length<5?'счёта':'счетов')+'</small></div>'+
  '<div class="kp"><span>Ближайшая отгрузка</span><b>'+(next?A.dfmt(next.due):'—')+'</b><small>'+(next?esc(next.name):'нет')+'</small></div>'+
  '<div class="kp"><span>Потрачено в 2026</span><b class="num">'+money(D.orders.filter(function(o){return o.st==='done'||o.paid}).reduce(function(s,o){return s+o.sum},0)+812400)+'</b><small>скидка постоянного клиента 7%</small></div></div>';
 var todo=proof.map(function(o){return'<li data-open="orders:'+o.id+'"><i>🖼</i><div><b>Утвердите макет: '+esc(o.name)+'</b><small style="display:block">Без утверждения не начнём печать · срок '+A.dfmt(o.due)+'</small></div><span class="bt sm">Открыть</span></li>'})
  .concat(pay.map(function(i){return'<li data-open="inv:'+i.id+'"><i>💳</i><div><b>Оплатите счёт № '+esc(i.id)+' на '+money(i.sum)+'</b><small style="display:block">'+(i.st==='late'?'Срок оплаты прошёл '+A.dfmt(i.due):'Оплатить до '+A.dfmt(i.due))+'</small></div><span class="bt sm'+(i.st==='late'?' dz':'')+'">Оплатить</span></li>'}));
 h+='<div class="g2"><div class="pane"><h3>Нужно ваше действие</h3>'+(todo.length?'<ul class="lg todo">'+todo.join('')+'</ul>':'<p class="em">Всё сделано, ждём вас с новым заказом</p>')+'</div>';
 h+='<div class="pane"><h3>Где сейчас заказы</h3>'+act.map(function(o){var st=['calc','proof','print','ready'].indexOf(o.st);return'<div class="trk" data-open="orders:'+o.id+'"><b>'+esc(o.name)+'</b><small>№ '+o.id+' · '+A.fmt(o.st,'pill:st')+'</small><div class="stp">'+['Расчёт','Макет','Печать','Готов'].map(function(x,j){return'<i class="'+(j<st?'d':j===st?'n':'')+'">'+x+'</i>'}).join('')+'</div></div>'}).join('')+'</div></div>';
 el.innerHTML=h};
A.hooks.pay=function(data,inv){inv.st='paid';inv.paid=0;inv.how=data.how;inv.hist=inv.hist||[];inv.hist.push(['сегодня','Оплачено: '+({card:'картой',sbp:'через СБП',bill:'по счёту с расчётного счёта'})[data.how]]);
 var o=A.find('orders',inv.order);if(o){o.paid=1;if(o.st==='wait')o.st='print';o.hist=o.hist||[];o.hist.push(['сегодня','Счёт № '+inv.id+' оплачен, заказ передан в печать']);o._fl=1}
 inv._fl=1;A.log('💳','Оплачен счёт № '+inv.id+' · '+money(inv.sum),o?'заказ № '+o.id+' передан в печать':'');A.toast(data.how==='bill'?'Платёжка принята, ждём поступления — обычно до 1 дня':'Оплата прошла. Спасибо!')};
A.hooks.approve=function(o){o.st='print';o.hist.push(['сегодня','Макет утверждён, заказ ушёл в печать']);o._fl=1;A.log('🖼','Макет утверждён: '+o.name,'№ '+o.id+' · печать займёт '+o.days+' дн.');A.toast('Макет утверждён. Печать начнём сегодня');A.close();A.render();A.badges()};
A.hooks.repeat=function(data,o){var L=D.orders,id=Math.max.apply(null,L.map(function(x){return+x.id}))+1;var q=+data.qty||o.qty,price=Math.round(o.sum/o.qty*q*0.93/10)*10;
 var r={id:String(id),name:o.name,kind:o.kind,qty:q,sum:price,st:'calc',due:o.days+3,days:o.days,paper:o.paper,mgr:o.mgr,hist:[['сегодня','Повтор заказа № '+o.id+', тираж '+q+' шт.']],_fl:1};L.unshift(r);
 A.log('🔁','Повтор заказа № '+o.id+' → № '+id,q+' шт. · '+money(price)+' со скидкой 7%');A.toast('Заказ № '+id+' создан. Менеджер подтвердит цену в течение часа');A.go('orders',1)};
A.hooks.mail=function(doc){doc.sent=1;doc._fl=1;A.log('✉️','Документ отправлен: '+doc.name,'на почту buh@bereg-coffee.ru');A.toast('Отправили на buh@bereg-coffee.ru');A.render()};
})();
"""

CSS = """
.todo li{grid-template-columns:34px 1fr auto;cursor:pointer}
.todo li b{font-weight:600;font-size:14px}
.trk{padding:12px 0;border-bottom:1px solid var(--line);cursor:pointer}
.trk:last-child{border-bottom:0}
.trk b{display:block;font-size:14px}.trk small{display:flex;gap:8px;align-items:center;color:var(--mut);font-size:12.5px;margin:3px 0 8px}
.stp{display:grid;grid-template-columns:repeat(4,1fr);gap:4px}
.stp i{font-style:normal;font-size:11px;color:var(--mut);padding-top:7px;border-top:3px solid var(--line)}
.stp i.d{border-color:var(--ac);color:var(--ink)}.stp i.n{border-color:var(--ac2);color:var(--ink);font-weight:600}
.mk{display:grid;gap:8px}.mk small{color:var(--mut);font-size:12.5px}
.mkp{aspect-ratio:210/297;max-width:230px;background:#f6efe3;border-radius:6px;box-shadow:0 10px 30px -14px rgba(0,0,0,.45),0 0 0 1px #e8dcc7;padding:22px 20px;display:flex;flex-direction:column;gap:9px;color:#2b2118}
.mkp b{font:800 26px/1 var(--fh);letter-spacing:.18em;color:#b8381f}.mkp span{font-size:11px;letter-spacing:.2em;text-transform:uppercase;opacity:.65;margin-bottom:10px}
.mkp i span{font-size:inherit;letter-spacing:0;text-transform:none;opacity:1;margin:0}
.mkp i{font-style:normal;font-size:12.5px;display:flex;justify-content:space-between;border-bottom:1px dotted #c9b79c;padding-bottom:4px}
"""


def cfg() -> dict:
    return {
        "slug": "apps/client", "brand": "Оттиск", "logo": "О", "org": "Кабинет клиента типографии",
        "title": "Оттиск — личный кабинет клиента типографии",
        "desc": "Кабинет клиента типографии: заказы и их этапы, утверждение макета, счета и оплата, закрывающие документы, "
                "повтор заказа в два клика.",
        "user": ["Кофейни «Берег»", "Ирина Соколова, закупки"],
        "theme": {"bg": "#f4f2ee", "side": "#1d1b19", "sink": "#f4f2ee", "sline": "#2e2b28", "son": "#3a342c", "sonk": "#ffd27a",
                  "ink": "#1d1b19", "mut": "#77716a", "line": "#e2ddd5", "card": "#ffffff", "ac": "#e2462c", "aci": "#ffffff",
                  "ac2": "#f0a23a", "fh": '"Commissioner",sans-serif', "fb": '"Commissioner",sans-serif', "fm": '"Fira Mono",monospace',
                  "hw": "700", "ht": "-.02em"},
        "fonts": [("Commissioner", "commissioner", [400, 500, 600, 700], "normal"), ("Fira Mono", "fira-mono", [400, 500], "normal")],
        "css": CSS,
        "about": {"h": "Оттиск — кабинет клиента типографии",
                  "p": ["Клиент сам видит, на каком этапе заказ, утверждает макет, оплачивает счета и забирает документы. Менеджеру "
                        "больше не нужно отвечать на «когда будет готово» и пересылать акты.",
                        "Всё, что здесь можно нажать, работает: утвердите макет, оплатите счёт, повторите прошлый заказ."],
                  "f": ["Заказы с этапами: расчёт, макет, печать, отгрузка", "Утверждение макета одной кнопкой",
                        "Счета, оплата картой, по СБП и по счёту", "Акты, УПД и договор — на почту бухгалтеру",
                        "Повтор заказа со скидкой постоянного клиента", "Связка с 1С и CRM типографии"]},
        "views": [
            {"id": "home", "label": "Главная", "icon": "home", "type": "custom", "title": "Добрый день, Ирина",
             "sub": "Кабинет кофеен «Берег» в типографии «Оттиск»", "primary": ["Новый заказ", "new"]},
            {"id": "orders", "label": "Заказы", "icon": "box", "type": "table", "entity": "orders", "title": "Заказы",
             "sub": "Нажмите на заказ, чтобы увидеть этапы, утвердить макет или повторить", "search": "Поиск по заказам",
             "find": ["id", "name", "kind"], "filter": "st", "primary": ["Новый заказ", "new"], "sort": ["due", -1],
             "badge": "D.orders.filter(function(o){return o.st==='proof'}).length",
             "cols": [["name", "Заказ", "b", "", "", "№ {id} · {kind} · {qty} шт."], ["sum", "Сумма", "money", "r"],
                      ["st", "Этап", "pill:st"], ["due", "Отгрузка", "date"]]},
            {"id": "inv", "label": "Счета", "icon": "money", "type": "table", "entity": "inv", "title": "Счета и оплата",
             "sub": "Оплачивайте картой, по СБП или по счёту с расчётного счёта", "filter": "st", "pill": "ist",
             "badge": "D.inv.filter(function(i){return i.st!=='paid'}).length",
             "kpis": [["К оплате", "sum(D.inv.filter(function(i){return i.st!=='paid'}),'sum')", "money", "ac"],
                      ["Просрочено", "sum(D.inv.filter(function(i){return i.st==='late'}),'sum')", "money"],
                      ["Оплачено в ноябре", "sum(D.inv.filter(function(i){return i.st==='paid'}),'sum')", "money"]],
             "cols": [["id", "Счёт", "b", "", "'№ '+r.id", "по заказу № {order}"], ["sum", "Сумма", "money", "r"], ["st", "Статус", "pill:ist"],
                      ["due", "Оплатить до", "date"]]},
            {"id": "docs", "label": "Документы", "icon": "doc", "type": "table", "entity": "docs", "title": "Документы",
             "sub": "Акты, УПД и договор — отправим бухгалтеру на почту", "search": "Найти документ", "find": ["name", "order"],
             "filter": "kind",
             "cols": [["name", "Документ", "b", "", "", "{date:date}"], ["order", "Заказ"], ["sum", "Сумма", "money", "r"],
                      ["kind", "Вид", "pill:kind"], ["sent", "Почта", "", "", "r.sent?'отправлен':'—'"]]},
            {"id": "log", "label": "Журнал", "icon": "log", "type": "log", "title": "Журнал действий",
             "sub": "Всё, что вы и типография сделали по вашим заказам"},
        ],
        "pills": {"st": {"calc": ["Расчёт", "idle"], "proof": ["Макет на утверждении", "warn"], "wait": ["Ждём оплату", "bad"],
                         "print": ["В печати", "info"], "ready": ["Готов к отгрузке", "ac"], "done": ["Отгружен", "ok"]},
                  "ist": {"paid": ["Оплачен", "ok"], "open": ["Ждёт оплаты", "warn"], "late": ["Просрочен", "bad"]},
                  "kind": {"act": ["Акт", "info"], "upd": ["УПД", "ac"], "contract": ["Договор", "idle"]}},
        "data": {
            "orders": [
                {"id": "4817", "name": "Меню на зиму", "kind": "Меню A4, ламинация", "qty": 120, "sum": 18960, "st": "proof", "due": 3, "days": 2,
                 "paper": "Мелованная 300 г", "mgr": "Олег Пчёлкин", "hist": [["10 ноября", "Заказ создан"], ["11 ноября", "Расчёт подтверждён"], ["вчера", "Макет загружен на утверждение"]]},
                {"id": "4809", "name": "Стаканы 350 мл", "kind": "Бумажные стаканы, 2 цвета", "qty": 5000, "sum": 41250, "st": "print", "due": 2, "days": 5,
                 "paper": "Картон 280 г", "mgr": "Олег Пчёлкин", "paid": 1, "hist": [["3 ноября", "Заказ создан"], ["5 ноября", "Макет утверждён"], ["6 ноября", "Счёт оплачен"], ["8 ноября", "Передан в печать"]]},
                {"id": "4822", "name": "Карты лояльности", "kind": "Пластик, номер и штрихкод", "qty": 2000, "sum": 37400, "st": "wait", "due": 7, "days": 4,
                 "paper": "ПВХ 0,76 мм", "mgr": "Олег Пчёлкин", "hist": [["12 ноября", "Заказ создан"], ["вчера", "Макет утверждён, выставлен счёт"]]},
                {"id": "4826", "name": "Стикеры на крышки", "kind": "Наклейки ⌀ 40 мм", "qty": 3000, "sum": 6870, "st": "calc", "due": 6, "days": 2,
                 "paper": "Самоклейка", "mgr": "Олег Пчёлкин", "hist": [["сегодня", "Заказ создан, менеджер считает цену"]]},
                {"id": "4791", "name": "Пакеты крафт с логотипом", "kind": "Крафт-пакеты, 1 цвет", "qty": 1500, "sum": 28350, "st": "ready", "due": 1, "days": 4,
                 "paper": "Крафт 80 г", "mgr": "Олег Пчёлкин", "paid": 1, "hist": [["28 октября", "Заказ создан"], ["30 октября", "Макет утверждён"], ["вчера", "Тираж готов, ждёт отгрузки"]]},
                {"id": "4774", "name": "Визитки бариста", "kind": "Визитки 90×50", "qty": 600, "sum": 4280, "st": "done", "due": -9, "days": 1,
                 "paper": "Дизайнерская 350 г", "mgr": "Олег Пчёлкин", "paid": 1, "hist": [["1 ноября", "Отгружен"]]},
                {"id": "4752", "name": "Меню на осень", "kind": "Меню A4, ламинация", "qty": 110, "sum": 17380, "st": "done", "due": -41, "days": 2,
                 "paper": "Мелованная 300 г", "mgr": "Олег Пчёлкин", "paid": 1, "hist": [["4 октября", "Отгружен"]]},
                {"id": "4738", "name": "Таблички «Wi-Fi»", "kind": "Таблички A6 на подставке", "qty": 24, "sum": 3120, "st": "done", "due": -55, "days": 2,
                 "paper": "Акрил 3 мм", "mgr": "Олег Пчёлкин", "paid": 1, "hist": [["20 сентября", "Отгружен"]]}],
            "inv": [
                {"id": "С-2291", "order": "4822", "sum": 37400, "st": "open", "due": 2, "hist": [["вчера", "Счёт выставлен"]]},
                {"id": "С-2277", "order": "4791", "sum": 9450, "st": "late", "due": -2, "note": "доплата за срочность", "hist": [["30 октября", "Счёт выставлен"]]},
                {"id": "С-2268", "order": "4809", "sum": 41250, "st": "paid", "due": -8, "hist": [["6 ноября", "Оплачено картой"]]},
                {"id": "С-2254", "order": "4791", "sum": 18900, "st": "paid", "due": -14, "hist": [["31 октября", "Оплачено по счёту"]]},
                {"id": "С-2240", "order": "4774", "sum": 4280, "st": "paid", "due": -15, "hist": [["30 октября", "Оплачено через СБП"]]}],
            "docs": [
                {"id": 1, "name": "УПД № 1931", "order": "4774", "sum": 4280, "kind": "upd", "date": -9},
                {"id": 2, "name": "Акт № 1907", "order": "4752", "sum": 17380, "kind": "act", "date": -41},
                {"id": 3, "name": "УПД № 1880", "order": "4738", "sum": 3120, "kind": "upd", "date": -55},
                {"id": 4, "name": "Договор № 118/25", "order": "все заказы", "sum": None, "kind": "contract", "date": -213},
                {"id": 5, "name": "Акт сверки за III квартал", "order": "все заказы", "sum": 64380, "kind": "act", "date": -44}]},
        "cards": {
            "orders": {"title": "{name}", "sub": "Заказ № {id} · менеджер {mgr}", "hist": 1,
                       "note": "r.st==='proof'?['Макет ждёт вашего утверждения. Проверьте текст и цены: после утверждения правки платные.','']:r.st==='wait'?['Печать начнём после оплаты счёта.','bad']:r.st==='ready'?['Тираж готов. Отгрузим '+A.dfmt(r.due)+' с 10 до 18.','ok']:null",
                       "fields": [["st", "Этап", "pill:st"], ["kind", "Изделие"], ["qty", "Тираж", "num"], ["paper", "Материал"],
                                  ["sum", "Стоимость", "money"], ["due", "Отгрузка", "date"]],
                       "extra": "r.st==='proof'?'<h4>Макет</h4><div class=\"mk\"><div class=\"mkp\"><b>БЕРЕГ</b><span>Зимнее меню</span><i><span>Раф с хвоей</span>340</i><i><span>Глинтвейн б/а</span>290</i><i><span>Какао с маршмеллоу</span>260</i><i><span>Пряный латте</span>320</i></div><small>menu-zima-v3.pdf · 2 стр.</small></div>':''",
                       "actions": [{"label": "Утвердить макет", "when": "r.st==='proof'", "fn": "approve"},
                                   {"label": "Нужны правки", "when": "r.st==='proof'", "form": "fix", "style": "g"},
                                   {"label": "Оплатить счёт", "when": "r.st==='wait'", "fn": "payo"},
                                   {"label": "Повторить заказ", "when": "r.st==='done'||r.st==='ready'", "form": "repeat", "style": "g"}]},
            "inv": {"title": "Счёт № {id}", "sub": "по заказу № {order}", "hist": 1,
                    "note": "r.st==='late'?['Срок оплаты прошёл '+A.dfmt(r.due)+'. Отгрузку придержим до оплаты.','bad']:r.st==='paid'?['Счёт оплачен.','ok']:null",
                    "fields": [["st", "Статус", "pill:ist"], ["sum", "Сумма", "money"], ["vat", "В том числе НДС 22%", "money", "Math.round(r.sum*22/122)"],
                               ["due", "Оплатить до", "date"], ["note", "Назначение"]],
                    "actions": [{"label": "Оплатить {sum:money}", "when": "r.st!=='paid'", "form": "pay"}]},
            "docs": {"title": "{name}", "sub": "по заказу {order}",
                     "fields": [["kind", "Вид", "pill:kind"], ["date", "Дата", "date"], ["sum", "Сумма", "money"]],
                     "actions": [{"label": "Отправить бухгалтеру", "fn": "mail", "when": "!r.sent"}]}},
        "forms": {
            "pay": {"title": "Оплата счёта № {id}", "hint": "Сумма {sum:money}. Деньги поступят типографии сразу, по счёту — до 1 дня.",
                    "fields": [["how", "Способ", "select", [["card", "Картой"], ["sbp", "Через СБП"], ["bill", "По счёту с расчётного счёта"]]]],
                    "submit": "Оплатить", "fn": "pay"},
            "fix": {"title": "Правки к макету: {name}", "fields": [["fix", "Что поправить", "textarea", None, None, "Например: заменить цену на раф 340 → 350", 1]],
                    "submit": "Отправить дизайнеру", "set": {"st": "proof"}, "log": "Правки к макету: {name}", "hist": "Отправлены правки: {fix}",
                    "toast": "Дизайнер пришлёт новый макет сегодня до 18:00", "icon": "✏️"},
            "repeat": {"title": "Повторить: {name}", "hint": "Те же материалы и макет, скидка постоянного клиента 7%.",
                       "fields": [["qty", "Тираж, шт.", "number"]], "submit": "Повторить заказ", "fn": "repeat"},
            "new": {"title": "Новый заказ", "hint": "Менеджер подтвердит цену и срок в течение часа.", "entity": "orders",
                    "fields": [["name", "Что печатаем", "text", None, None, "Например: листовки к открытию", 1],
                               ["kind", "Изделие", "select", ["Листовки A5", "Меню A4, ламинация", "Наклейки ⌀ 40 мм", "Бумажные стаканы, 2 цвета", "Крафт-пакеты, 1 цвет", "Визитки 90×50"]],
                               ["qty", "Тираж, шт.", "number", None, "half", "1000", 1], ["due", "Нужно через, дней", "number", None, "half", "5", 1]],
                    "defaults": {"qty": 1000, "due": 5},
                    "add": {"st": "calc", "mgr": "Олег Пчёлкин", "paper": "подберёт менеджер", "days": 3},
                    "compute": {"sum": "Math.round(({'Листовки A5':4.1,'Меню A4, ламинация':158,'Наклейки ⌀ 40 мм':2.29,'Бумажные стаканы, 2 цвета':8.25,'Крафт-пакеты, 1 цвет':18.9,'Визитки 90×50':7.13})[r.kind]*r.qty/10)*10", "due": "+r.due"},
                    "hist": "Заказ создан: {kind}, {qty} шт.", "log": "Новый заказ № {id}: {name}", "logSub": "{kind} · {qty} шт. · около {sum:money}",
                    "toast": "Заказ № {id} создан. Предварительно {sum:money}", "go": "orders", "submit": "Отправить в расчёт", "icon": "＋"}},
        "log": [["вчера", "🖼", "Загружен макет на утверждение: Меню на зиму", "№ 4817 · версия 3"],
                ["вчера", "📦", "Тираж готов: Пакеты крафт с логотипом", "№ 4791 · ждёт отгрузки"],
                ["13 ноя", "🧾", "Выставлен счёт № С-2291 на 37 400 ₽", "Карты лояльности"],
                ["8 ноя", "🖨", "Передан в печать: Стаканы 350 мл", "№ 4809 · 5 000 шт."]],
        "js": JS + r"""
APP.hooks.payo=function(o){var inv=APP.D.inv.filter(function(i){return i.order===o.id&&i.st!=='paid'})[0];if(inv)APP.form('pay',inv)};
""",
        "init": "0",
    }
