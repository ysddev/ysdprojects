"""«Палета» — мобильное приложение оптового поставщика для владельцев магазинов: каталог с ценой от объёма, сканер штрихкода
на полке, корзина с минимальной суммой и датой доставки, статус заказа и повтор. Прототип в телефоне работает."""

ITEMS = [("tea", "Чай чёрный «Беседа», 100 пак.", "коробка 12 шт.", 189, "🫖"),
         ("cof", "Кофе зерновой «Жокей», 1 кг", "коробка 6 шт.", 1090, "☕"),
         ("sug", "Сахар-рафинад, 1 кг", "мешок 20 шт.", 98, "◻"),
         ("cho", "Шоколад «Алёнка», 90 г", "блок 20 шт.", 84, "▦")]

CAT = ('<div class="ah">Каталог</div><label class="srch"><span>⌕</span><input placeholder="Поиск по 4 800 товарам" aria-label="Поиск"></label>'
       '<div class="chips"><button type="button" class="on">Бакалея</button><button type="button">Напитки</button><button type="button">Кондитерка</button></div>'
       '<div class="tier">От 15 коробок — −7% на всю категорию</div>'
       + "".join(f'<div class="it" data-id="{k}"><i>{ic}</i><div><b>{n}</b><span>{pk} · {p}&nbsp;₽/шт.</span></div>'
                 f'<button type="button" class="add" data-add="{k}" aria-label="В корзину">+</button></div>' for k, n, pk, p, ic in ITEMS)
       + '<button type="button" class="abtn ghost" data-go="scan">▣ Сканировать штрихкод на полке</button>')

SCAN = ('<div class="cam"><div class="shelf"><span></span><span></span><span></span><span class="bc"></span><span></span></div>'
        '<div class="vf"><i></i><i></i><i></i><i></i><b class="ln"></b></div><p id="scanmsg">Наведите камеру на штрихкод товара</p></div>'
        '<div class="found acard" id="found" hidden><div><b>Чай чёрный «Беседа», 100 пак.</b><span>на полке осталось 3 шт. · в прошлый раз брали 2 коробки</span></div>'
        '<div class="qty"><button type="button" data-q="-1" aria-label="Меньше">−</button><b id="sq">2</b><button type="button" data-q="1" aria-label="Больше">+</button></div>'
        '<button type="button" class="abtn" id="scanadd">Добавить 2 коробки</button></div>')

CART = ('<div class="ah">Корзина</div><div id="lines"></div>'
        '<div class="acard minb"><div><span>До бесплатной доставки</span><b id="left"></b></div><div class="bar"><i id="barf"></i></div></div>'
        '<div class="acard dl"><span>Доставка</span><div class="chips" id="dday"><button type="button" class="on">Завтра, 9–13</button><button type="button">Чт, 14–18</button></div></div>'
        '<div class="acard tot"><div><span>Товары</span><b id="c-sum"></b></div><div><span>Скидка за объём</span><b id="c-disc"></b></div><div class="big"><span>Итого</span><b id="c-tot"></b></div></div>'
        '<button type="button" class="abtn" id="order">Оформить заказ</button><p class="amut sm">Оплата по счёту с отсрочкой 14 дней или картой.</p>')

ORDERS = ('<div class="ah">Заказы</div><div class="acard ord"><div class="oh"><b>Заказ № 4182</b><span id="o-sum"></span></div>'
          '<ul class="tl2"><li class="ok"><b>Принят</b><small>сейчас</small></li><li class="now"><b>Собирается на складе</b><small>до 20:00</small></li>'
          '<li><b>В пути</b><small id="o-day">завтра, 9–13</small></li><li><b>Доставлен</b><small>подпись в приложении</small></li></ul></div>'
          '<div class="acard ord"><div class="oh"><b>Заказ № 4097</b><span>38 420 ₽</span></div><div class="amut">доставлен 14 ноября · 23 позиции</div>'
          '<button type="button" class="abtn ghost" data-go="cat">↻ Повторить заказ</button></div>')

PROF = ('<div class="ah">Магазин</div><div class="acard"><b>ИП Гарипова · «Продукты у дома»</b><div class="amut">Казань, ул. Чистопольская, 31</div></div>'
        '<div class="acard lst"><div>Отсрочка платежа<span>14 дней</span></div><div>Менеджер<span>Рустем</span></div><div>Документы ЭДО<span>›</span></div></div>')

APP_CSS = r"""
.app{--abg:#f2f2ee;--aink:#141414;--amut:#77776f;--aline:#e1e1da;--acard:#ffffff;--aac:#ff7a00;--aaci:#141414;--fa:"Onest",sans-serif;--fah:"Onest",sans-serif;--ahw:800;--arb:14px;--arc:16px}
.app .ah{font-size:26px}.app .sm{font-size:12.5px;margin-top:10px}
.srch{display:flex;gap:8px;align-items:center;background:var(--acard);border-radius:12px;padding:0 12px;height:42px;box-shadow:0 0 0 1px var(--aline)}
.srch input{border:0;background:none;outline:0;flex:1;min-width:0;font-size:14px}
.chips{display:flex;gap:6px;margin:10px 0;overflow-x:auto;scrollbar-width:none}.chips button{padding:8px 12px;border-radius:999px;background:var(--acard);font-size:13px;font-weight:600;white-space:nowrap;box-shadow:0 0 0 1px var(--aline)}
.chips button.on{background:var(--aink);color:#fff;box-shadow:none}
.tier{font-size:12.5px;font-weight:600;background:#fff1e0;color:#9a4a00;border-radius:10px;padding:8px 10px;margin-bottom:8px}
.it{display:grid;grid-template-columns:40px 1fr 36px;gap:10px;align-items:center;padding:10px 0;border-bottom:1px solid var(--aline)}
.it i{font-style:normal;width:40px;height:40px;border-radius:10px;background:var(--acard);display:grid;place-items:center;font-size:19px}
.it b{display:block;font-size:13.5px;line-height:1.25}.it span{font-size:12px;color:var(--amut)}
.add{width:36px;height:36px;border-radius:10px;background:var(--aac);color:var(--aaci);font-size:22px;font-weight:700;line-height:1}
.add.done{background:var(--aink);color:#fff;font-size:13px}
.cam{position:relative;height:330px;border-radius:18px;background:#1b1b19;overflow:hidden;color:#fff}
.shelf{position:absolute;left:14px;right:14px;top:70px;display:flex;gap:8px;align-items:flex-end}
.shelf span{flex:1;height:110px;border-radius:6px;background:linear-gradient(180deg,#5b4a3a,#3b2f25)}.shelf span:nth-child(2){height:140px;background:linear-gradient(180deg,#a6262a,#6e1416)}
.shelf span:nth-child(3){height:96px;background:linear-gradient(180deg,#e8c25a,#a07a1c)}.shelf span:nth-child(5){height:126px;background:linear-gradient(180deg,#3d6a8a,#213a4c)}
.shelf .bc{height:128px;background:#f4ede0;position:relative}.shelf .bc::after{content:"";position:absolute;left:12%;right:12%;bottom:14px;height:30px;background:repeating-linear-gradient(90deg,#111 0 2px,transparent 2px 4px,#111 4px 5px,transparent 5px 8px)}
.vf{position:absolute;left:50%;top:150px;width:150px;height:84px;transform:translate(-50%,-50%)}
.vf i{position:absolute;width:22px;height:22px;border:3px solid var(--aac)}.vf i:nth-child(1){left:0;top:0;border-right:0;border-bottom:0}.vf i:nth-child(2){right:0;top:0;border-left:0;border-bottom:0}
.vf i:nth-child(3){left:0;bottom:0;border-right:0;border-top:0}.vf i:nth-child(4){right:0;bottom:0;border-left:0;border-top:0}
.vf .ln{position:absolute;left:6px;right:6px;top:50%;height:2px;background:var(--aac);box-shadow:0 0 12px var(--aac);animation:scan 1.4s ease-in-out infinite alternate}
@keyframes scan{from{transform:translateY(-30px)}to{transform:translateY(30px)}}
.cam.ok .vf i{border-color:#3ddc84}.cam.ok .ln{display:none}
.cam p{position:absolute;left:0;right:0;bottom:16px;text-align:center;font-size:13px;opacity:.9}
.found{margin-top:10px;display:grid;gap:8px;animation:up .3s}.found b{display:block;font-size:14px}.found span{font-size:12px;color:var(--amut)}
@keyframes up{from{opacity:0;transform:translateY(10px)}}
.qty{display:flex;align-items:center;gap:12px}.qty button{width:34px;height:34px;border-radius:10px;background:var(--abg);font-size:18px}
.ln2{display:grid;grid-template-columns:1fr auto;gap:2px 10px;padding:10px 0;border-bottom:1px solid var(--aline);font-size:13.5px}
.ln2 span{font-size:12px;color:var(--amut)}.ln2 b{text-align:right}
.minb{margin-top:10px}.minb div:first-child{display:flex;justify-content:space-between;font-size:13px}.minb span{color:var(--amut)}
.minb .bar{height:8px;border-radius:4px;background:var(--abg);margin-top:8px;overflow:hidden}.minb .bar i{display:block;height:100%;background:var(--aac);border-radius:4px;transition:width .5s}
.dl{margin-top:8px}.dl>span{font-size:12px;color:var(--amut)}.dl .chips{margin:6px 0 0}
.tot{margin-top:8px;display:grid;gap:6px;font-size:13.5px}.tot div{display:flex;justify-content:space-between}.tot span{color:var(--amut)}.tot .big{font-size:17px;padding-top:6px;border-top:1px dashed var(--aline)}.tot .big span{color:var(--aink)}
.ord{margin-bottom:10px}.oh{display:flex;justify-content:space-between;margin-bottom:8px}.oh span{font-weight:700}
.tl2{list-style:none;margin:0;padding:0 0 0 16px;border-left:2px solid var(--aline);display:grid;gap:10px}
.tl2 li{position:relative;display:flex;justify-content:space-between;font-size:13px}.tl2 li::before{content:"";position:absolute;left:-23px;top:3px;width:12px;height:12px;border-radius:50%;background:var(--abg);box-shadow:inset 0 0 0 2px var(--aline)}
.tl2 li.ok::before{background:#3ddc84;box-shadow:none}.tl2 li.now::before{background:var(--aac);box-shadow:0 0 0 4px rgba(255,122,0,.25)}.tl2 small{color:var(--amut)}
.lst{display:grid;margin-top:10px;padding:4px 14px}.lst div{display:flex;justify-content:space-between;padding:11px 0;border-top:1px solid var(--aline);font-size:14px}.lst div:first-child{border-top:0}.lst span{color:var(--amut)}
.shot .mini>div{--abg:#f2f2ee;--aink:#141414;--amut:#77776f;--aline:#e1e1da;--acard:#fff;--aac:#ff7a00;--aaci:#141414;--fa:"Onest",sans-serif;--fah:"Onest",sans-serif}
.mz{zoom:.68;pointer-events:none}.mz .vf .ln{animation:none}
"""

APP_JS = r"""
(function(){var U=window.APP,IT=%s,cart={},q=2,MIN=15000;
function badge(){var n=Object.keys(cart).length,b=U.$('#cbadge');b.hidden=!n;b.textContent=n}
function add(k,n){cart[k]=(cart[k]||0)+n;var b=U.$('[data-add="'+k+'"]');if(b){b.classList.add('done');b.textContent=cart[k]+' к.'}badge()}
U.$$('[data-add]').forEach(function(b){b.addEventListener('click',function(){add(b.dataset.add,1)})});
U.$$('.qty [data-q]').forEach(function(b){b.addEventListener('click',function(){q=Math.max(1,q+(+b.dataset.q));U.$('#sq').textContent=q;U.$('#scanadd').textContent='Добавить '+q+(q===1?' коробку':q<5?' коробки':' коробок')})});
U.$('#scanadd').addEventListener('click',function(){add('tea',q);U.go('cart')});
function chipset(sel){U.$(sel).addEventListener('click',function(ev){var b=ev.target.closest('button');if(!b)return;U.$$(sel+' button').forEach(function(x){x.classList.toggle('on',x===b)})})}
chipset('#dday');
function render(){var h='',s=0,boxes=0;Object.keys(cart).forEach(function(k){var it=IT[k],n=cart[k],sum=it[2]*it[1]*n;s+=sum;boxes+=n;
 h+='<div class="ln2"><b style="text-align:left">'+it[0]+'</b><b>'+U.money(sum)+'</b><span>'+n+' × '+it[1]+' шт.</span><span></span></div>'});
 if(!h)h='<p class="amut">Пока пусто: добавьте товары из каталога или отсканируйте полку.</p>';
 var d=boxes>=15?Math.round(s*.07):0;U.$('#lines').innerHTML=h;U.$('#c-sum').textContent=U.money(s);U.$('#c-disc').textContent=d?'−'+U.money(d):'от 15 коробок';
 U.$('#c-tot').textContent=U.money(s-d);var left=Math.max(0,MIN-(s-d));U.$('#left').textContent=left?U.money(left):'бесплатно ✓';U.$('#barf').style.width=Math.min(100,(s-d)/MIN*100)+'%';U.tot=s-d}
U.$('#order').addEventListener('click',function(){U.$('#o-sum').textContent=U.money(U.tot||0);U.$('#o-day').textContent=U.$('#dday .on').textContent;cart={};badge();
 U.$$('[data-add]').forEach(function(b){b.classList.remove('done');b.textContent='+'});U.go('orders')});
var tm;U.on={cart:render,scan:function(){var c=U.$('.cam');c.classList.remove('ok');U.$('#found').hidden=true;U.$('#scanmsg').textContent='Наведите камеру на штрихкод товара';clearTimeout(tm);
 tm=setTimeout(function(){c.classList.add('ok');U.$('#scanmsg').textContent='Штрихкод 4 607 0…12 — найден';U.$('#found').hidden=false},1600)}};
function seq(steps){var i=0;(function nx(){if(!U.auto||i>=steps.length)return;var s=steps[i++];setTimeout(function(){if(!U.auto)return;s();nx()},s.t||1500)})()}
function auto(f,t){f.t=t;return f}
U.start=function(){seq([auto(function(){U.$('[data-add="cof"]').click()},1300),auto(function(){U.$('[data-add="cof"]').click()},700),
 auto(function(){U.$('[data-add="cho"]').click()},800),auto(function(){U.go('scan')},1200),auto(function(){U.$('.qty [data-q="1"]').click()},2600),
 auto(function(){U.$('#scanadd').click()},900),auto(function(){U.$$('#dday button')[0].click()},2200),auto(function(){U.$('#order').click()},1600)])};
})();
"""


def cfg() -> dict:
    items_js = "{" + ",".join(f'"{k}":["{n.replace(chr(34), "")}",{int(pk.split()[1])},{p}]' for k, n, pk, p, _ in ITEMS) + "}"
    return {
        "slug": "apps/paleta", "brand": "Палета", "logoIcon": "▦", "layout": "wide",
        "title": "Палета — мобильное приложение оптового поставщика: заказ со сканера, цена от объёма, доставка и повтор заказа",
        "desc": "Мобильное приложение для iOS и Android, в котором владельцы магазинов заказывают товар у оптового поставщика: "
                "каталог с ценой от объёма, сканер штрихкода на полке, минимальная сумма и дата доставки, статус заказа и повтор в одно касание.",
        "theme": {"bg": "#f2f2ee", "ink": "#121212", "soft": "#4a4a45", "mut": "#7d7d76", "line": "#dfdfd8", "line2": "#cacac2",
                  "card": "#ffffff", "ac": "#ff7a00", "aci": "#121212", "fh": '"Onest",sans-serif', "fb": '"Onest",sans-serif',
                  "hw": "800", "ht": "-.035em", "rb": "14px", "rc": "20px", "rs": "28px", "stagebg": "#121212", "blob": "28px",
                  "cbg": "#ff7a00", "cink": "#121212"},
        "fonts": [("Onest", "onest", [400, 500, 600, 700, 800], "normal")],
        "css": ".hero h1{font-size:clamp(42px,5.6vw,84px);line-height:.98}.ph-stage{padding:28px 0}"
               ".ph-stage::before{inset:0;background:#121212 repeating-linear-gradient(90deg,transparent 0 58px,rgba(255,255,255,.05) 58px 60px)}"
               ".cta-b .btn{background:#121212;color:#fff}.tag{border-radius:12px}",
        "appCss": APP_CSS, "appJs": APP_JS.replace("%s", items_js, 1),
        "hero": {"kicker": "Мобильное приложение для оптовых продаж", "h1": "Магазин заказывает товар, пока стоит у полки",
                 "lead": "Владелец магазина сканирует штрихкод на пустой полке, видит цену от объёма и свой прошлый заказ, добавляет коробки "
                         "и выбирает время доставки. Повторить заказ прошлой недели — одно касание. Менеджер больше не собирает заявки по телефону.",
                 "cta": "Открыть прототип", "cta2": "Как делаем приложения",
                 "tags": [("Штрихкод найден", "чай «Беседа», брали 2 коробки"), ("−7% за объём", "от 15 коробок в категории")]},
        "platforms": ["iOS", "Android", "Связь с 1С:Управление торговлей"],
        "demoNote": "Прототип работает: добавьте товар, отсканируйте полку, оформите заказ",
        "screens": {"cat": {"tab": "c", "html": CAT}, "scan": {"tab": "s", "html": SCAN}, "cart": {"tab": "k", "html": CART},
                    "orders": {"tab": "o", "html": ORDERS}, "prof": {"tab": "p", "html": PROF}},
        "tabs": [("c", "cat", "▦", "Каталог"), ("s", "scan", "▣", "Сканер"), ("k", "cart", "◫", "Корзина", "cbadge"), ("o", "orders", "≡", "Заказы"), ("p", "prof", "○", "Магазин")],
        "shotsTitle": "Заказ без звонков менеджеру",
        "shots": [("Каталог", "цена за штуку, упаковка и скидка от объёма", '<div class="mz">' + CAT + "</div>"),
                  ("Сканер", "штрихкод с полки — и товар уже в корзине", '<div class="mz"><div class="cam ok">' + SCAN.split('<div class="cam">', 1)[1].split('</div><div class="found', 1)[0]
                   .replace('Наведите камеру на штрихкод товара', 'Штрихкод найден') + '</div></div>'),
                  ("Корзина", "минимальная сумма и дата доставки", '<div class="mz"><div class="ah">Корзина</div><div class="ln2"><b style="text-align:left">Кофе зерновой «Жокей», 1 кг</b><b>13 080 ₽</b><span>2 × 6 шт.</span><span></span></div>'
                   '<div class="ln2"><b style="text-align:left">Чай чёрный «Беседа»</b><b>6 804 ₽</b><span>3 × 12 шт.</span><span></span></div><div class="acard minb"><div><span>До бесплатной доставки</span><b>бесплатно ✓</b></div><div class="bar"><i style="width:100%"></i></div></div></div>'),
                  ("Статус заказа", "сборка, доставка и повтор в одно касание", '<div class="mz">' + ORDERS + "</div>")],
        "featsTitle": "Что получает поставщик и его клиенты",
        "feats": [("▣", "Сканер штрихкода", "Камера телефона находит товар по штрихкоду и показывает, сколько брали в прошлый раз."),
                  ("%", "Цена от объёма", "Скидки за количество коробок и персональные цены для каждого магазина — из 1С."),
                  ("↻", "Повтор заказа", "Прошлый заказ одним касанием: поправить количество и отправить."),
                  ("◷", "Доставка по слотам", "Свободные окна машин на неделю вперёд, минимальная сумма для бесплатной доставки."),
                  ("≡", "Статус и документы", "Сборка, отгрузка, доставка. Накладные и счета — по ЭДО в приложении."),
                  ("🔔", "Акции и новинки", "Пуш о скидке на категорию, которую магазин берёт каждую неделю, а не рассылка всем подряд.")],
        "stackTitle": "Работает с вашей учётной системой",
        "stack": [("Платформы", "iOS 15+ и Android 9+"), ("Технология", "React Native: один код на обе платформы"),
                  ("Учёт", "1С:Управление торговлей, МойСклад — остатки, цены, заказы"), ("Сканер", "камера телефона, штрихкоды EAN-13 и DataMatrix"),
                  ("Документы", "ЭДО через Диадок или СБИС"), ("Публикация", "App Store, Google Play и RuStore")],
        "stepsTitle": "Как запускаем",
        "steps": [("Прототип", "кликабельный, как этот: проверяем на трёх ваших клиентах", "1 неделя"),
                  ("Дизайн и обмен с 1С", "экраны, цены, остатки, статусы заказов", "3 недели"),
                  ("Разработка", "приложение, админка для менеджеров, пуши", "6–8 недель"),
                  ("Запуск", "сторы, обучение менеджеров, первые 50 магазинов", "2 недели")],
        "resTitle": "Что меняется в продажах",
        "results": [("+18%", "средний чек с подсказкой «брали в прошлый раз»"), ("−70%", "заявок по телефону и в мессенджерах"), ("3 мин", "на заказ вместо 20"), ("0", "ошибок при переносе заказа в 1С")],
        "faq": [("Сколько стоит такое приложение?", "Зависит от обмена с вашей учётной системой. Прототип и дизайн — первым этапом, разработку считаем после согласования экранов."),
                ("Цены у каждого магазина свои — это учтётся?", "Да. Цены, скидки и отсрочка берутся из карточки клиента в 1С или МойСклад."),
                ("Сканер работает на любом телефоне?", "Да, через камеру. Отдельный терминал сбора данных не нужен."),
                ("А если у клиента нет смартфона под рукой?", "Тот же каталог открывается в браузере на компьютере — заказ попадает в ту же систему.")],
        "ctaTitle": "Переведём заказы ваших клиентов в приложение", "ctaBtn": "Открыть прототип",
    }
