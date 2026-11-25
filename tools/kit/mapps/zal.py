"""«Сила» — мобильное приложение сети фитнес-клубов: вход по QR, загрузка зала сейчас, запись на групповые, заморозка
и продление абонемента. Прототип в телефоне работает."""

CLASSES = [("yoga", "Йога", "18:30", "Анна", 4, "зал 2"), ("hiit", "Функциональная", "19:00", "Тимур", 1, "зал 1"),
           ("pil", "Пилатес", "20:00", "Ольга", 7, "зал 2"), ("box", "Бокс", "20:15", "Ринат", 0, "ринг")]

def _places(n: int) -> str:
    return f"{n} место" if n % 10 == 1 and n % 100 != 11 else f"{n} места" if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14 else f"{n} мест"


HOME = ('<div class="ah">Привет, Марина</div>'
        '<button type="button" class="qr acard" data-go="pass"><span class="qic"></span><div><b>Вход в клуб</b><span>Покажите QR на турникете</span></div></button>'
        '<div class="acard load"><div class="lh"><b>Сейчас в клубе</b><span id="lnow">23 человека</span></div>'
        '<div class="bars">' + "".join(f'<i style="height:{h}%"{" class=now" if n == 6 else ""}></i>' for n, h in enumerate([18, 26, 40, 58, 72, 64, 38, 30, 52, 80, 92, 70, 44]))
        + '</div><div class="lx"><span>7:00</span><span>сейчас</span><span>22:00</span></div><p class="amut sm">Свободнее всего после 21:00</p></div>'
        '<div class="acard nx" id="nx"><span>Ближайшая запись</span><b>Нет записей на сегодня</b></div>'
        '<button type="button" class="abtn" data-go="sched">Записаться на тренировку</button>')

SCHED = ('<div class="ah">Расписание</div><div class="chips" id="days"><button type="button" class="on">Сегодня</button><button type="button">Завтра</button><button type="button">Пт</button><button type="button">Сб</button></div>'
         + "".join(f'<div class="cl" data-id="{k}"><div class="tm">{t}</div><div><b>{n}</b><span>{c} · {r}</span></div>'
                   f'<button type="button" class="bk{" full" if left == 0 else ""}" data-book="{k}"{" disabled" if left == 0 else ""}>{"Лист ожидания" if left == 0 else _places(left)}</button></div>'
                   for k, n, t, c, left, r in CLASSES))

PASS = ('<div class="ah">Абонемент</div><div class="card2"><small>Сила · Безлимит</small><b>до 14 марта 2027</b>'
        '<div class="qrbig"></div><span>Марина Ковалёва · № 004817</span></div>'
        '<div class="acard lst"><div>Осталось дней<span>109</span></div><div>Заморозка<span id="frz">14 дней доступно</span></div><div>Гостевые визиты<span>2</span></div></div>'
        '<button type="button" class="abtn ghost" id="freeze">❄ Заморозить на 7 дней</button>'
        '<button type="button" class="abtn" id="renew">Продлить на год — 32 900 ₽</button>')

DONE = ('<div class="ok2"><div class="tick">✓</div><b id="dt">Вы записаны</b><span id="ds"></span>'
        '<p class="amut sm">Напомним за 2 часа. Отменить можно до 3 часов до начала — без штрафа.</p>'
        '<button type="button" class="abtn" data-go="home">На главную</button></div>')

PROF = ('<div class="ah">Профиль</div><div class="acard"><b>Марина Ковалёва</b><div class="amut">клуб «Сила» на Баумана · с 2024 года</div></div>'
        '<div class="acard lst"><div>Тренировок в ноябре<span>14</span></div><div>Персональный тренер<span>Тимур</span></div><div>Уведомления<span>включены</span></div></div>')

APP_CSS = r"""
.app{--abg:#0f1012;--aink:#f2f2f0;--amut:#8d8f95;--aline:#24262b;--acard:#17191d;--aac:#c6f432;--aaci:#0f1012;--fa:"Manrope",sans-serif;--fah:"Manrope",sans-serif;--ahw:800;--arb:14px;--arc:18px}
.app .ah{font-size:26px}.app .sm{font-size:12.5px;margin-top:8px}
.qr{display:flex;gap:12px;align-items:center;width:100%;text-align:left;background:var(--aac);color:var(--aaci)}
.qr b{display:block;font-size:16px}.qr span{font-size:12.5px;opacity:.8}
.qic{width:44px;height:44px;border-radius:10px;background:conic-gradient(var(--aaci) 25%,transparent 0 50%,var(--aaci) 0 75%,transparent 0) 0 0/11px 11px;box-shadow:inset 0 0 0 3px var(--aaci)}
.load{margin-top:10px}.lh{display:flex;justify-content:space-between;font-size:14px}.lh span{color:var(--aac);font-weight:700}
.bars{display:flex;align-items:flex-end;gap:4px;height:70px;margin-top:10px}.bars i{flex:1;border-radius:4px 4px 0 0;background:#2b2e34}.bars i.now{background:var(--aac)}
.lx{display:flex;justify-content:space-between;font-size:11px;color:var(--amut);margin-top:4px}
.nx{margin:10px 0}.nx span{display:block;font-size:12px;color:var(--amut)}.nx b{font-size:15px}.nx.on{box-shadow:0 0 0 1px var(--aac)}
.chips{display:flex;gap:6px;margin:10px 0;overflow-x:auto;scrollbar-width:none}.chips button{padding:8px 12px;border-radius:999px;background:var(--acard);color:var(--aink);font-size:13px;font-weight:600;white-space:nowrap}
.chips button.on{background:var(--aink);color:var(--abg)}
.cl{display:grid;grid-template-columns:52px 1fr auto;gap:10px;align-items:center;padding:12px 0;border-bottom:1px solid var(--aline)}
.cl .tm{font-weight:800;font-size:15px}.cl b{display:block;font-size:14.5px}.cl span{font-size:12px;color:var(--amut)}
.bk{padding:8px 11px;border-radius:10px;background:var(--aac);color:var(--aaci);font-weight:700;font-size:12.5px;white-space:nowrap}
.bk.full{background:var(--acard);color:var(--amut)}.bk.done{background:var(--aink);color:var(--abg)}
.card2{border-radius:20px;padding:18px;background:linear-gradient(135deg,#c6f432,#7bd33a);color:#0f1012;display:grid;gap:4px;justify-items:start}
.card2 small{font-weight:700;opacity:.75}.card2 b{font-size:20px}.card2 span{font-size:12px;opacity:.8}
.qrbig{width:132px;height:132px;margin:10px 0;border-radius:12px;background:#fff;box-shadow:inset 0 0 0 10px #fff;
 background-image:conic-gradient(#0f1012 25%,transparent 0 50%,#0f1012 0 75%,transparent 0);background-size:16px 16px}
.lst{display:grid;margin-top:10px;padding:4px 14px}.lst div{display:flex;justify-content:space-between;padding:11px 0;border-top:1px solid var(--aline);font-size:14px}.lst div:first-child{border-top:0}.lst span{color:var(--amut)}
.app .abtn{margin-top:10px}
.ok2{display:grid;justify-items:center;text-align:center;gap:6px;padding-top:40px;animation:up .3s}.ok2 b{font-size:20px}.ok2 span{color:var(--amut);font-size:14px}
.tick{width:64px;height:64px;border-radius:50%;background:var(--aac);color:var(--aaci);display:grid;place-items:center;font-size:30px;font-weight:800}
@keyframes up{from{opacity:0;transform:translateY(10px)}}
.shot .mini>div{--abg:#0f1012;--aink:#f2f2f0;--amut:#8d8f95;--aline:#24262b;--acard:#17191d;--aac:#c6f432;--aaci:#0f1012;--fa:"Manrope",sans-serif;--fah:"Manrope",sans-serif}
.mz{zoom:.68;pointer-events:none}
"""

APP_JS = r"""
(function(){var U=window.APP,CL=%s,booked=null,frozen=false;
U.$$('[data-book]').forEach(function(b){b.addEventListener('click',function(){var c=CL[b.dataset.book];booked=c;
 U.$$('[data-book]').forEach(function(x){if(!x.disabled){x.classList.remove('done')}});b.classList.add('done');b.textContent='Вы записаны';
 U.$('#dt').textContent=c[0]+' в '+c[1];U.$('#ds').textContent='Сегодня · тренер '+c[2]+' · '+c[3];U.go('done')})});
U.$('#days').addEventListener('click',function(ev){var b=ev.target.closest('button');if(!b)return;U.$$('#days button').forEach(function(x){x.classList.toggle('on',x===b)})});
U.$('#freeze').addEventListener('click',function(){frozen=!frozen;U.$('#frz').textContent=frozen?'с завтра на 7 дней ✓':'14 дней доступно';
 U.$('#freeze').textContent=frozen?'Отменить заморозку':'❄ Заморозить на 7 дней'});
U.$('#renew').addEventListener('click',function(){U.$('#renew').textContent='Оплачено ✓ до 14 марта 2028'});
U.on={home:function(){var n=U.$('#nx');if(booked){n.classList.add('on');n.innerHTML='<span>Ближайшая запись</span><b>'+booked[0]+' · сегодня в '+booked[1]+'</b>'}}};
function seq(steps){var i=0;(function nx(){if(!U.auto||i>=steps.length)return;var s=steps[i++];setTimeout(function(){if(!U.auto)return;s();nx()},s.t||1500)})()}
function auto(f,t){f.t=t;return f}
U.start=function(){seq([auto(function(){U.go('sched')},1500),auto(function(){U.$('[data-book="yoga"]').click()},1500),
 auto(function(){U.go('home')},2400),auto(function(){U.go('pass')},2000),auto(function(){U.$('#freeze').click()},1500)])};
})();
"""


def cfg() -> dict:
    cl_js = "{" + ",".join(f'"{k}":["{n}","{t}","{c}","{r}"]' for k, n, t, c, _l, r in CLASSES) + "}"
    return {
        "slug": "apps/zal", "brand": "Сила", "logoIcon": "◆", "layout": "wide",
        "title": "Сила — мобильное приложение фитнес-клуба: вход по QR, загрузка зала, запись на групповые, заморозка абонемента",
        "desc": "Мобильное приложение для iOS и Android для сети фитнес-клубов: вход по QR без карты, сколько людей в зале прямо сейчас, "
                "запись на групповые тренировки и лист ожидания, заморозка и продление абонемента.",
        "theme": {"bg": "#f3f4f1", "ink": "#0f1012", "soft": "#45474c", "mut": "#7c7e84", "line": "#dfe1dc", "line2": "#c8cbc4",
                  "card": "#ffffff", "ac": "#0f1012", "aci": "#c6f432", "fh": '"Manrope",sans-serif', "fb": '"Manrope",sans-serif',
                  "hw": "800", "ht": "-.04em", "rb": "999px", "rc": "22px", "rs": "30px", "stagebg": "#0f1012", "blob": "30px",
                  "cbg": "#c6f432", "cink": "#0f1012"},
        "fonts": [("Manrope", "manrope", [400, 500, 600, 700, 800], "normal")],
        "css": ".hero h1{font-size:clamp(42px,5.8vw,88px);line-height:.96}.ph-stage{padding:28px 0}"
               ".ph-stage::before{inset:0;background:radial-gradient(60% 60% at 70% 30%,rgba(198,244,50,.22),transparent 70%),#0f1012}"
               ".tag{border-radius:16px}",
        "appCss": APP_CSS, "appJs": APP_JS.replace("%s", cl_js, 1),
        "hero": {"kicker": "Мобильное приложение для фитнес-клубов", "h1": "Клуб в телефоне: вход, запись и абонемент",
                 "lead": "Гость проходит турникет по QR, видит, сколько людей в зале прямо сейчас, и записывается на йогу в два касания. "
                         "Заморозка и продление — без звонка администратору. Клуб видит загрузку и продлевает абонементы вовремя.",
                 "cta": "Открыть прототип", "cta2": "Как делаем приложения",
                 "tags": [("23 человека в зале", "свободнее после 21:00"), ("Йога в 18:30", "осталось 4 места")]},
        "platforms": ["iOS", "Android", "Связь с 1С:Фитнес клуб"],
        "demoNote": "Прототип работает: запишитесь на тренировку, откройте QR, заморозьте абонемент",
        "screens": {"home": {"tab": "h", "html": HOME}, "sched": {"tab": "s", "html": SCHED}, "pass": {"tab": "a", "html": PASS},
                    "prof": {"tab": "p", "html": PROF}, "done": {"tab": "s", "html": DONE}},
        "tabs": [("h", "home", "◆", "Главная"), ("s", "sched", "☰", "Расписание"), ("a", "pass", "▣", "Абонемент"), ("p", "prof", "○", "Профиль")],
        "shotsTitle": "Всё, ради чего раньше звонили на ресепшен",
        "shots": [("Главная", "QR для входа и загрузка зала по часам", '<div class="mz">' + HOME + "</div>"),
                  ("Расписание", "свободные места и лист ожидания", '<div class="mz">' + SCHED + "</div>"),
                  ("Абонемент", "QR, остаток дней, заморозка и продление", '<div class="mz">' + PASS + "</div>")],
        "featsTitle": "Что получает клуб и гости",
        "feats": [("▣", "Вход по QR", "Турникет читает код с телефона — пластиковые карты и очередь на ресепшене не нужны."),
                  ("▮", "Загрузка зала", "Сколько людей сейчас и график по часам: гости сами выбирают время, когда свободнее."),
                  ("☰", "Запись на групповые", "Места в зале, лист ожидания, напоминание за 2 часа и отмена без звонка."),
                  ("❄", "Заморозка и продление", "Гость замораживает и продлевает абонемент сам, оплата картой или СБП."),
                  ("◎", "Персональные тренировки", "Свободные окна тренера и пакеты занятий с остатком."),
                  ("🔔", "Пуши по делу", "Абонемент заканчивается — напоминание со скидкой на продление, а не спам всем.")],
        "stackTitle": "Работает с вашей системой клуба",
        "stack": [("Платформы", "iOS 15+ и Android 9+"), ("Технология", "React Native: один код на обе платформы"),
                  ("Учёт", "1С:Фитнес клуб, Mobifitness API, YCLIENTS — абонементы, расписание, оплаты"), ("Турникеты", "QR и NFC через вашу СКУД"),
                  ("Оплата", "ЮKassa, СБП, рекуррентные платежи"), ("Публикация", "App Store, Google Play и RuStore")],
        "stepsTitle": "Как запускаем",
        "steps": [("Прототип", "кликабельный, как этот: проверяем на гостях клуба", "1 неделя"),
                  ("Дизайн и интеграции", "экраны, обмен с 1С или CRM клуба, турникеты", "3 недели"),
                  ("Разработка", "приложение, админка, пуши и оплата", "6–8 недель"),
                  ("Запуск", "сторы, QR-наклейки на ресепшене, обучение администраторов", "2 недели")],
        "resTitle": "Что меняется в клубе",
        "results": [("+22%", "продлений вовремя"), ("−40%", "звонков на ресепшен"), ("0", "пластиковых карт"), ("2 касания", "до записи на тренировку")],
        "faq": [("Сколько стоит приложение для клуба?", "Зависит от интеграций с вашей системой и турникетами. Прототип и дизайн — первым этапом, разработку считаем после согласования экранов."),
                ("Наши турникеты прочитают QR?", "Большинство современных СКУД умеют. Если нет — ставим недорогой считыватель рядом с турникетом."),
                ("Можно ли для сети из нескольких клубов?", "Да: гость выбирает клуб, загрузка и расписание показываются по каждому."),
                ("А если гость без приложения?", "Вход и запись остаются как раньше — приложение добавляет удобство, а не отнимает привычное.")],
        "ctaTitle": "Сделаем приложение для вашего клуба", "ctaBtn": "Открыть прототип",
    }
