"""«Рейс» — мобильное приложение междугородних автобусов: поиск рейса, выбор места на схеме салона, оплата, билет с QR
и автобус на карте маршрута. Прототип в телефоне работает."""
from ..bots._k import qr_svg

QR = qr_svg("reys-ticket-0742")

SEATS_TAKEN = {1, 2, 5, 6, 9, 12, 13, 18, 21, 22, 25, 30, 33, 34, 37, 41}


def seats_html(chosen: int = 0) -> str:
    rows = []
    n = 1
    for r in range(11):
        cells = []
        for col in range(4):
            cls = "x" if n in SEATS_TAKEN else ("on" if n == chosen else "")
            cells.append(f'<button type="button" class="st {cls}" data-seat="{n}"{" disabled" if cls == "x" else ""}>{n}</button>')
            if col == 1:
                cells.append('<i class="ais"></i>')
            n += 1
        rows.append("".join(cells))
    return '<div class="bus"><div class="drv">Водитель · вход</div><div class="grid">' + "".join(rows) + "</div></div>"


SEARCH = """<div class="ah">Куда едем?</div>
<div class="acard rt"><div><small>Откуда</small><b>Казань</b><span>Центральный автовокзал</span></div>
<button type="button" class="swp" aria-label="Поменять местами">⇅</button>
<div><small>Куда</small><b>Набережные Челны</b><span>Автовокзал «Чаллы»</span></div></div>
<div class="chips" id="dates"><button type="button" class="on" data-d="0">Сегодня</button><button type="button" data-d="1">Завтра</button><button type="button" data-d="2">Пятница</button></div>
<div class="acard px"><span>Пассажиры</span><div class="stp"><button type="button" data-px="-1" aria-label="Меньше">−</button><b id="px">1</b><button type="button" data-px="1" aria-label="Больше">+</button></div></div>
<button type="button" class="abtn" data-go="list">Найти рейсы</button>
<p class="amut sm">Недавние: Казань → Альметьевск, Казань → Елабуга</p>"""

TRIPS = [("07:40", "11:35", "3 ч 55 мин", 890, "Комфорт · USB · кондиционер", 12),
         ("10:15", "14:20", "4 ч 05 мин", 790, "Стандарт", 4),
         ("13:30", "17:20", "3 ч 50 мин", 990, "Бизнес · 2+1 · Wi-Fi", 9)]

LIST = ('<div class="bk"><button type="button" data-go="search" aria-label="Назад">‹</button><div><b>Казань → Наб. Челны</b><span id="dline">Сегодня · 1 пассажир</span></div></div>'
        + "".join(f'<button type="button" class="trip" data-trip="{i}"><div class="tt"><b>{a}</b><i></i><b>{b}</b></div>'
                  f'<div class="tm"><span>{dur}</span><span>{note}</span></div><div class="tp"><b>{p}&nbsp;₽</b><span class="{"low" if left < 6 else ""}">осталось {left} мест</span></div></button>'
                  for i, (a, b, dur, p, note, left) in enumerate(TRIPS)))

SEATS = ('<div class="bk"><button type="button" data-go="list" aria-label="Назад">‹</button><div><b>Выберите место</b><span id="sline">07:40 · Комфорт</span></div></div>'
         '<div class="lg"><span><i class="f"></i>свободно</span><span><i class="x"></i>занято</span><span><i class="o"></i>ваше</span></div>'
         f'<div id="bus">{seats_html()}</div><button type="button" class="abtn" id="seatgo" disabled>Выберите место</button>')

PAY = """<div class="bk"><button type="button" data-go="seats" aria-label="Назад">‹</button><div><b>Оплата</b><span>Билет придёт сюда и на почту</span></div></div>
<div class="acard sum"><div><span>Рейс</span><b id="p-trip">07:40 → 11:35</b></div><div><span>Место</span><b id="p-seat">7</b></div>
<div><span>Пассажир</span><b>Ильдар Х.</b></div><div><span>Сервисный сбор</span><b>0 ₽</b></div><div class="tot"><span>Итого</span><b id="p-sum">890 ₽</b></div></div>
<button type="button" class="abtn" id="paybtn">Оплатить через СБП</button><button type="button" class="abtn ghost">Картой</button>
<p class="amut sm">Вернуть билет можно в приложении до отправления: деньги придут на карту.</p>"""

TICKET = f"""<div class="ah">Билеты</div>
<div class="tix"><div class="tx-h"><span>Казань</span><i>⟶</i><span>Наб. Челны</span></div>
<div class="tx-r"><div><small>Отправление</small><b id="t-time">07:40</b></div><div><small>Место</small><b id="t-seat">7</b></div><div><small>Перрон</small><b>4</b></div></div>
<div class="tx-qr">{QR}<span>Покажите водителю при посадке</span></div></div>
<button type="button" class="abtn" data-go="track">Где автобус</button>"""

TRACK = """<div class="bk"><button type="button" data-go="ticket" aria-label="Назад">‹</button><div><b>Автобус А 742 ВК</b><span id="eta">Прибытие на перрон через 12 минут</span></div></div>
<div class="map"><svg viewBox="0 0 300 170" aria-hidden="true"><path d="M20 140 C 80 130, 70 60, 140 70 S 230 30, 280 30" fill="none" stroke="currentColor" stroke-opacity=".18" stroke-width="10" stroke-linecap="round"/>
<path id="rt" d="M20 140 C 80 130, 70 60, 140 70 S 230 30, 280 30" fill="none" stroke="var(--aac)" stroke-width="5" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset=".62"/>
<circle cx="20" cy="140" r="7" fill="var(--aac)"/><circle cx="280" cy="30" r="7" fill="var(--aink)"/><circle id="busdot" cx="98" cy="96" r="9" fill="#ffcf33" stroke="#1a1a1a" stroke-width="2"/></svg></div>
<ul class="stops"><li class="ok"><b>Казань, автовокзал</b><small>07:40</small></li><li class="ok"><b>Пестрецы</b><small>08:15</small></li>
<li class="now"><b>Мамадыш</b><small>09:35</small></li><li><b>Набережные Челны</b><small>11:35</small></li></ul>"""

PROFILE = """<div class="ah">Профиль</div><div class="acard"><b>Ильдар Хасанов</b><div class="amut">+7 9•• •••-45-67</div></div>
<div class="acard lst"><div>Пассажиры<span>2</span></div><div>Карты и СБП<span>1</span></div><div>Уведомления<span>вкл</span></div><div>Возврат билета<span>›</span></div></div>"""

APP_CSS = r"""
.app{--abg:#f7f6f2;--aink:#16181a;--amut:#7a7d80;--aline:#e3e1da;--acard:#ffffff;--aac:#1f6f50;--aaci:#fff;--fa:"Arsenal",sans-serif;--fah:"Alumni Sans",sans-serif;--ahw:800;--arb:12px;--arc:14px}
.app .ah{font-size:34px;line-height:1;letter-spacing:0}
.app .sm{font-size:12.5px;margin-top:10px}
.rt{position:relative;display:grid;gap:12px}.rt small{display:block;font-size:11.5px;color:var(--amut)}.rt b{display:block;font-size:17px}.rt span{font-size:12px;color:var(--amut)}
.rt>div+.swp+div{padding-top:12px;border-top:1px solid var(--aline)}
.swp{position:absolute;right:12px;top:50%;transform:translateY(-50%);width:34px;height:34px;border-radius:50%;background:var(--abg);font-size:16px}
.chips{display:flex;gap:6px;margin:12px 0}.chips button{flex:1;padding:9px 0;border-radius:10px;background:var(--acard);font-size:13px;font-weight:700}
.chips button.on{background:var(--aink);color:#fff}
.px{display:flex;justify-content:space-between;align-items:center}.stp{display:flex;align-items:center;gap:12px}.stp button{width:32px;height:32px;border-radius:50%;background:var(--abg);font-size:18px}
.bk{display:flex;gap:10px;align-items:center;margin:2px 0 12px}.bk>button{width:34px;height:34px;border-radius:50%;background:var(--acard);font-size:22px;line-height:1;flex:none}
.bk b{display:block;font-size:15.5px}.bk span{font-size:12px;color:var(--amut)}
.trip{display:grid;gap:6px;width:100%;text-align:left;background:var(--acard);border-radius:14px;padding:12px 14px;margin-bottom:8px;box-shadow:0 0 0 1px var(--aline)}
.trip:active{transform:scale(.99)}
.tt{display:flex;align-items:center;gap:8px}.tt b{font:800 24px/1 var(--fah)}.tt i{flex:1;height:2px;background:repeating-linear-gradient(90deg,var(--aline) 0 6px,transparent 6px 10px)}
.tm{display:flex;justify-content:space-between;font-size:12px;color:var(--amut)}.tp{display:flex;justify-content:space-between;align-items:baseline}.tp b{font-size:17px}
.tp span{font-size:12px;color:var(--amut)}.tp span.low{color:#c2410c}
.lg{display:flex;gap:12px;font-size:11.5px;color:var(--amut);margin-bottom:8px}.lg i{display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:4px;vertical-align:-1px}
.lg .f{background:var(--acard);box-shadow:0 0 0 1px var(--aline)}.lg .x{background:#d6d4cc}.lg .o{background:var(--aac)}
.bus{background:var(--acard);border-radius:22px 22px 14px 14px;padding:10px 12px 12px;box-shadow:0 0 0 1px var(--aline)}
.drv{font-size:11px;color:var(--amut);text-align:center;padding-bottom:8px;margin-bottom:8px;border-bottom:1px dashed var(--aline)}
.grid{display:grid;grid-template-columns:1fr 1fr 14px 1fr 1fr;gap:5px}
.st{height:26px;border-radius:7px 7px 4px 4px;background:var(--abg);box-shadow:inset 0 -3px 0 var(--aline);font-size:11px;font-weight:700;color:var(--aink)}
.st.x{background:#d6d4cc;color:#9b998f;box-shadow:none}.st.on{background:var(--aac);color:#fff;box-shadow:none}
.abtn:disabled{opacity:.45}
.sum{display:grid;gap:9px}.sum div{display:flex;justify-content:space-between;font-size:13.5px}.sum span{color:var(--amut)}.sum .tot{padding-top:9px;border-top:1px dashed var(--aline);font-size:16px}
.tot span{color:var(--aink)!important}
.tix{background:#ffcf33;color:#1a1a1a;border-radius:18px;padding:14px;position:relative}
.tix::before,.tix::after{content:"";position:absolute;top:96px;width:18px;height:18px;border-radius:50%;background:var(--abg)}.tix::before{left:-9px}.tix::after{right:-9px}
.tx-h{display:flex;justify-content:space-between;align-items:center;font:800 24px/1 var(--fah)}
.tx-r{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:14px 0 16px;padding-bottom:14px;border-bottom:2px dashed rgba(0,0,0,.2)}.tx-r small{display:block;font-size:11px;opacity:.65}.tx-r b{font:800 26px/1 var(--fah)}
.tx-qr{display:grid;justify-items:center;gap:8px;font-size:12px}.tx-qr svg{width:120px;height:120px;background:#fff;border-radius:10px;padding:8px}
.map{background:var(--acard);border-radius:16px;padding:8px;color:var(--aink);box-shadow:0 0 0 1px var(--aline)}.map svg{width:100%;height:auto;display:block}
#rt{transition:stroke-dashoffset 1.4s}
.stops{list-style:none;margin:12px 0 0;padding:0 0 0 18px;border-left:2px solid var(--aline);display:grid;gap:12px}
.stops li{position:relative;display:flex;justify-content:space-between;font-size:13.5px}.stops li::before{content:"";position:absolute;left:-25px;top:3px;width:12px;height:12px;border-radius:50%;background:var(--abg);box-shadow:inset 0 0 0 2px var(--aline)}
.stops li.ok::before{background:var(--aac);box-shadow:none}.stops li.now::before{background:#ffcf33;box-shadow:0 0 0 4px rgba(255,207,51,.35)}.stops small{color:var(--amut)}
.lst{display:grid;gap:0;margin-top:10px;padding:4px 14px}.lst div{display:flex;justify-content:space-between;padding:11px 0;border-top:1px solid var(--aline);font-size:14px}.lst div:first-child{border-top:0}.lst span{color:var(--amut)}
.shot .mini>div{--abg:#f7f6f2;--aink:#16181a;--amut:#7a7d80;--aline:#e3e1da;--acard:#fff;--aac:#1f6f50;--aaci:#fff;--fa:"Arsenal",sans-serif;--fah:"Alumni Sans",sans-serif}
.mz{zoom:.68;pointer-events:none}
"""

APP_JS = r"""
(function(){var U=window.APP,trips=%s,st={d:0,px:1,trip:0,seat:0};
var dn=['Сегодня','Завтра','Пятница'];
function line(){var e=U.$('#dline');if(e)e.textContent=dn[st.d]+' · '+st.px+' '+(st.px===1?'пассажир':st.px<5?'пассажира':'пассажиров')}
U.$('#dates').addEventListener('click',function(ev){var b=ev.target.closest('button');if(!b)return;st.d=+b.dataset.d;U.$$('#dates button').forEach(function(x){x.classList.toggle('on',x===b)});line()});
U.$$('[data-px]').forEach(function(b){b.addEventListener('click',function(){st.px=Math.max(1,Math.min(4,st.px+(+b.dataset.px)));U.$('#px').textContent=st.px;line()})});
U.$$('.trip').forEach(function(b){b.addEventListener('click',function(){st.trip=+b.dataset.trip;st.seat=0;var t=trips[st.trip];U.$('#sline').textContent=t[0]+' · '+t[4].split(' · ')[0];
 U.$$('.st.on').forEach(function(x){x.classList.remove('on')});sg();U.go('seats')})});
var sgo=U.$('#seatgo');
function sg(){var t=trips[st.trip];if(st.seat){sgo.disabled=false;sgo.textContent='Место '+st.seat+' · '+U.money(t[3]*st.px)+' — дальше'}else{sgo.disabled=true;sgo.textContent='Выберите место'}}
U.$('#bus').addEventListener('click',function(ev){var b=ev.target.closest('.st');if(!b||b.disabled)return;U.$$('.st.on').forEach(function(x){x.classList.remove('on')});b.classList.add('on');st.seat=+b.dataset.seat;sg()});
sgo.addEventListener('click',function(){if(!st.seat)return;var t=trips[st.trip];U.$('#p-trip').textContent=t[0]+' → '+t[1];U.$('#p-seat').textContent=st.seat;U.$('#p-sum').textContent=U.money(t[3]*st.px);U.go('pay')});
var pb=U.$('#paybtn');pb.addEventListener('click',function(){pb.textContent='Проверяем оплату…';pb.disabled=true;setTimeout(function(){pb.textContent='Оплатить через СБП';pb.disabled=false;
 var t=trips[st.trip];U.$('#t-time').textContent=t[0];U.$('#t-seat').textContent=st.seat;var bd=U.$('#tbadge');bd.hidden=false;bd.textContent='1';U.go('ticket')},1100)});
U.on={track:function(){var r=U.$('#rt');r.style.strokeDashoffset='.62';setTimeout(function(){r.style.strokeDashoffset='.44'},60);var m=12,e=U.$('#eta');clearInterval(U.ti);U.ti=setInterval(function(){m=Math.max(1,m-1);e.textContent='Прибытие на перрон через '+m+' мин'},2200)}};
function seq(steps){var i=0;(function nx(){if(!U.auto||i>=steps.length)return;var s=steps[i++];setTimeout(function(){if(!U.auto)return;s();nx()},s.t||1500)})()}
function auto(f,t){f.t=t;return f}
U.start=function(){seq([auto(function(){U.$$('#dates button')[1].click()},1300),auto(function(){U.go('list')},1100),
 auto(function(){U.$$('.trip')[0].click()},1500),auto(function(){U.$('.st[data-seat="7"]').click()},1300),auto(function(){sgo.click()},1200),
 auto(function(){pb.click()},1500),auto(function(){U.go('track')},2400)])};
})();
"""


def cfg() -> dict:
    trips_js = "[" + ",".join(f'["{a}","{b}","{d}",{p},"{n}",{l}]' for a, b, d, p, n, l in TRIPS) + "]"
    return {
        "slug": "apps/reys", "brand": "Рейс", "logoIcon": "Р", "layout": "split",
        "title": "Рейс — мобильное приложение междугородних автобусов: билет, место в салоне, автобус на карте",
        "desc": "Мобильное приложение перевозчика для iOS и Android: поиск рейса, выбор места на схеме салона, оплата через СБП, "
                "билет с QR-кодом для посадки и автобус на карте маршрута в реальном времени.",
        "theme": {"bg": "#f4f1ea", "ink": "#151515", "soft": "#4f4b44", "mut": "#837d72", "line": "#e2ddd1", "line2": "#cfc8b8",
                  "card": "#fbfaf6", "ac": "#1f6f50", "aci": "#ffffff", "fh": '"Alumni Sans",sans-serif', "fb": '"Arsenal",sans-serif',
                  "hw": "800", "ht": "0", "rb": "12px", "rc": "18px", "rs": "24px", "stagebg": "#ffcf33", "blob": "48% 52% 44% 56%/52% 46% 54% 48%"},
        "fonts": [("Alumni Sans", "alumni-sans", [700, 800], "normal"), ("Arsenal", "arsenal", [400, 700], "normal")],
        "css": ".hero h1{font-size:clamp(52px,7.6vw,118px);line-height:.9}h2{font-size:clamp(40px,5.4vw,76px);line-height:.95}"
               ".feat b{font-size:26px}.steps li::before{font-size:30px}.res b{font-size:clamp(40px,5vw,66px)}",
        "appCss": APP_CSS, "appJs": APP_JS % trips_js,
        "hero": {"kicker": "Мобильное приложение для перевозчика", "h1": "Билет на автобус за минуту — с местом у окна",
                 "lead": "Пассажир находит рейс, выбирает место на схеме салона и платит через СБП. Билет с QR-кодом остаётся в телефоне, "
                         "а в день поездки видно, где сейчас автобус и через сколько он подъедет к перрону.",
                 "cta": "Открыть прототип", "cta2": "Как делаем приложения",
                 "tags": [("Место 7 у окна", "07:40, Комфорт, 890 ₽"), ("Автобус через 12 минут", "перрон 4, А 742 ВК")]},
        "backScreen": '<div class="sb"><span>9:41</span><i>●●● ▮</i></div><div style="padding:6px 16px">' + TICKET.replace('id="t-time"', "").replace('id="t-seat"', "").replace(' data-go="track"', "") + "</div>",
        "platforms": ["iOS", "Android", "Веб-кабинет диспетчера"],
        "screens": {"search": {"tab": "s", "html": SEARCH}, "list": {"tab": "s", "html": LIST}, "seats": {"tab": "s", "html": SEATS},
                    "pay": {"tab": "s", "html": PAY}, "ticket": {"tab": "t", "html": TICKET}, "track": {"tab": "t", "html": TRACK},
                    "profile": {"tab": "p", "html": PROFILE}},
        "tabs": [("s", "search", "⌕", "Поиск"), ("t", "ticket", "▭", "Билеты", "tbadge"), ("p", "profile", "○", "Профиль")],
        "shotsTitle": "Четыре экрана, которые решают поездку",
        "shots": [("Поиск", "откуда, куда, дата и пассажиры на одном экране", '<div class="mz">' + SEARCH + "</div>"),
                  ("Схема салона", "место у окна или рядом с попутчиком", '<div class="mz"><div class="ah">Выберите место</div>' + seats_html(7) + "</div>"),
                  ("Билет с QR", "работает без интернета", '<div class="mz">' + TICKET.replace('id="t-time"', "").replace('id="t-seat"', "") + "</div>"),
                  ("Где автобус", "остановки и время до перрона", '<div class="mz">' + TRACK.replace('id="rt"', "").replace('id="busdot"', "").replace('id="eta"', "") + "</div>")],
        "featsTitle": "Что получает пассажир и перевозчик",
        "featsStyle": "list",
        "feats": [("⌕", "Поиск за три касания", "Недавние направления, дата кнопкой, число пассажиров — без календаря на весь экран."),
                  ("◫", "Схема салона", "Свободные и занятые места, у окна или рядом. Для бизнес-класса — схема 2+1."),
                  ("₽", "СБП и карты", "Оплата в два касания, возврат в приложении до отправления."),
                  ("▭", "Билет офлайн", "QR-код сохраняется в телефоне и открывается без интернета на автовокзале."),
                  ("◉", "Автобус на карте", "Координаты с трекера в автобусе: пассажир видит остановки и время до перрона."),
                  ("🔔", "Уведомления", "Перрон, задержка, смена автобуса — пушем, а не объявлением, которое не слышно.")],
        "stackTitle": "Одно приложение на iOS и Android",
        "stack": [("Платформы", "iOS 15+ и Android 9+"), ("Технология", "Flutter: один код на обе платформы"),
                  ("Оплата", "СБП и карты через ЮKassa или банк перевозчика"), ("Карта", "Яндекс MapKit, трекеры ГЛОНАСС в автобусах"),
                  ("Данные", "расписание и места из вашей системы продаж"), ("Публикация", "App Store, Google Play и RuStore")],
        "stepsTitle": "От идеи до приложения в сторах",
        "steps": [("Прототип", "кликабельные экраны, как этот, — согласуем путь пассажира", "1 неделя"),
                  ("Дизайн", "все экраны, светлая и тёмная тема", "2 недели"),
                  ("Разработка", "приложение, админка и связь с системой продаж", "6–8 недель"),
                  ("Публикация", "сторы, тестирование на реальных пассажирах", "1–2 недели")],
        "resTitle": "Что меняется для перевозчика",
        "results": [("68%", "билетов покупают в приложении, а не в кассе"), ("−40%", "звонков «где автобус?»"), ("4,8", "оценка в сторах"), ("2 мин", "от поиска до билета")],
        "faq": [("Сколько стоит такое приложение?", "Зависит от состава: прототип и дизайн — первым этапом, разработку считаем после согласования экранов. "
                                                    "Называем цену каждого этапа заранее."),
                ("Можно связать с нашей системой продаж?", "Да. Берём рейсы, места и цены из вашей системы через API, продажи из приложения уходят туда же."),
                ("Нужно ли два разных приложения?", "Нет. Делаем на Flutter: один код, приложения для iOS и Android выходят одновременно."),
                ("Кто публикует в сторы?", "Мы: готовим описание, скриншоты и проходим проверку App Store, Google Play и RuStore.")],
        "ctaTitle": "Покажем прототип вашего приложения за неделю", "ctaBtn": "Открыть прототип",
    }
