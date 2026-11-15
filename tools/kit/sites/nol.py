"""«Ноль» — банкротство физлиц и списание долгов в Екатеринбурге: тест «какой путь подходит», честная смета расходов,
рассрочка, что будет с имуществом."""

IMAGES = {
    "talk": ("1642522029691-029b5a432954", 4, 5, "700,1100"),
    "sign": ("1562564055-71e051d33c19", 3, 2, "700,1100"),
    "hands": ("1681505531034-8d67054e07f6", 3, 2, "700,1100"),
    "two": ("1714974528232-f62051870736", 3, 2, "700,1100"),
    "paper": ("1626105985445-6430a31f6f96", 4, 5, "600,1000"),
}

LOGO = ('<svg viewBox="0 0 32 32"><circle cx="16" cy="16" r="14" fill="none" stroke="#4b3fd6" stroke-width="3.4"/>'
        '<path d="M9 23 L23 9" stroke="#ff8a5c" stroke-width="3" stroke-linecap="round"/></svg>')

TEST = r"""
<div class="tst rv">
 <div class="panel tq">
  <div class="q rng"><div class="rh"><span>Сумма всех долгов</span><b id="tDebtV">640 000 ₽</b></div><input type="range" id="tDebt" min="30000" max="5000000" step="10000" value="640000"></div>
  <div class="q"><b>Пристав окончил производство, потому что взыскать нечего?</b><div class="seg" id="tFssp"><button type="button" data-v="1">Да</button><button type="button" data-v="0" class="on">Нет / не знаю</button></div></div>
  <div class="q"><b>Есть имущество, кроме единственного жилья?</b><div class="chips" id="tProp"><button type="button" data-v="none" class="on">Нет</button><button type="button" data-v="car">Машина</button><button type="button" data-v="flat2">Вторая квартира или доля</button><button type="button" data-v="mort">Ипотечное жильё</button></div></div>
  <div class="q rng"><div class="rh"><span>Официальный доход в месяц</span><b id="tIncV">38 000 ₽</b></div><input type="range" id="tInc" min="0" max="200000" step="1000" value="38000"></div>
 </div>
 <div class="panel tr" id="tRes"></div>
</div>
"""

CSS = r"""
.hero h1 em{font-style:normal;background:linear-gradient(transparent 62%,#ffd9c9 62%);color:inherit}
.tst{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:clamp(14px,2vw,22px);align-items:start}
.tq{display:grid;gap:26px}.tq .q{display:grid;gap:12px}.tq .q>b{font-weight:600;font-size:15.5px}
.tr{position:sticky;top:90px;display:grid;gap:14px;border:2px solid var(--ac)}
.tr .lab{font:700 13px var(--fb);letter-spacing:.08em;text-transform:uppercase;color:var(--ac)}
.tr h3{font-size:clamp(26px,2.6vw,34px)}
.tr p{color:var(--soft)}
.tr ul{margin:0;padding:0;list-style:none;display:grid;gap:8px}
.tr li{display:flex;justify-content:space-between;gap:12px;padding:10px 0;border-bottom:1px dashed var(--line2);font-size:15px}
.tr li b{white-space:nowrap}
.tr .tot{display:flex;justify-content:space-between;align-items:baseline;font-weight:700;font-size:18px}
.tr .tot b{font:700 30px var(--fh)}
.tr .warn{background:#fff3ee;color:#8a3a1c;border-radius:12px;padding:12px 14px;font-size:14px}
.tr .btn{width:100%}
.keep{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.keep div{border-radius:20px;padding:24px;background:var(--card);box-shadow:0 0 0 1px var(--line)}
.keep h3{font-size:22px;margin-bottom:12px;display:flex;align-items:center;gap:10px}
.keep h3 i{width:30px;height:30px;border-radius:50%;display:grid;place-items:center;font-style:normal;font-size:16px}
.keep .y h3 i{background:#e3f6ea;color:#1f7a45}.keep .n h3 i{background:#ffe7dd;color:#b1431c}
.keep ul{margin:0;padding-left:20px;display:grid;gap:7px;color:var(--soft)}
.myth{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.myth div{padding:22px;border-radius:20px;background:rgba(255,255,255,.06)}
.myth s{display:block;color:rgba(255,255,255,.55);font-size:15px;margin-bottom:10px}
.myth b{display:block;font:700 19px/1.3 var(--fh);color:#fff}
@media (max-width:860px){.tst,.keep,.myth{grid-template-columns:1fr}.tr{position:static}}
"""

JS = r"""
(function(){var $=function(s){return document.getElementById(s)};var fssp=0,prop='none';
function seg(id,cb){$(id).addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;[].forEach.call(this.children,function(x){x.classList.toggle('on',x===b)});cb(b.dataset.v);run()})}
seg('tFssp',function(v){fssp=+v});seg('tProp',function(v){prop=v});
['tDebt','tInc'].forEach(function(id){$(id).addEventListener('input',run)});
function run(){var d=+$('tDebt').value,inc=+$('tInc').value;$('tDebtV').textContent=rub(d);$('tIncV').textContent=rub(inc);var h='';
 if(d<300000&&!(fssp&&d>=25000)){h='<span class="lab">Скорее не нужно</span><h3>При таком долге банкротство дороже самого долга</h3><p>Поможем договориться с кредиторами о реструктуризации и снизить платёж. Первая консультация — бесплатно.</p>'
  +'<ul><li>Переговоры с банками и МФО<b>от 9 900 ₽</b></li></ul><a class="btn" href="#lead">Разобрать мою ситуацию</a>'}
 else if(fssp&&d>=25000&&d<=1000000&&prop=='none'){h='<span class="lab">Подходит внесудебное банкротство</span><h3>Через МФЦ — без суда и почти без расходов</h3>'
  +'<p>Долг от 25 тысяч до 1 миллиона и пристав окончил производство: можно подать заявление в МФЦ. Мы проверим основания и соберём список кредиторов — ошибка в нём оставит часть долгов.</p>'
  +'<ul><li>Подача в МФЦ<b>0 ₽</b></li><li>Проверка оснований и список кредиторов<b>14 900 ₽</b></li></ul><div class="tot"><span>Итого</span><b>14 900 ₽</b></div><div class="warn">Процедура длится 6 месяцев. Новые долги в это время не начисляются.</div><a class="btn" href="#lead">Проверить основания</a>'}
 else{var fee=d>2000000?94000:79000;var pub=21400,dep=25000,gp=2900;var tot=fee+pub+dep+gp;var mon=Math.round(fee/10/100)*100;
  var w=prop=='car'?'Машину, скорее всего, продадут: её стоимость пойдёт кредиторам. Обсудим, можно ли её сохранить.':prop=='flat2'?'Вторую квартиру или долю реализуют на торгах. Единственное жильё не тронут.':prop=='mort'?'Ипотечное жильё — отдельный разговор: есть законные способы сохранить его, если продолжать платить ипотеку.':'Единственное жильё и вещи для жизни не тронут.';
  if(inc>=25000&&d<700000)w+=' Доход выше прожиточного минимума — суд может предложить реструктуризацию вместо списания.';
  h='<span class="lab">Подходит судебное банкротство</span><h3>Через арбитражный суд за 7–9 месяцев</h3><p>Списываются долги по кредитам, займам, ЖКХ и налогам. Не списываются алименты и возмещение вреда.</p>'
  +'<ul><li>Наша работа под ключ (рассрочка на 10 мес)<b>'+rub(fee)+'</b></li><li>Вознаграждение финансового управляющего<b>'+rub(dep)+'</b></li><li>Публикации в реестре и газете<b>'+rub(pub)+'</b></li><li>Госпошлина и почтовые расходы<b>'+rub(gp)+'</b></li></ul>'
  +'<div class="tot"><span>Всего за процедуру</span><b>'+rub(tot)+'</b></div><p style="font-size:14px">Платёж нам — '+rub(mon)+' в месяц вместо '+rub(Math.max(d*0.045,3000))+' по кредитам.</p><div class="warn">'+w+'</div><a class="btn" href="#lead">Получить план процедуры</a>'}
 $('tRes').innerHTML=h}
run()})();
"""

KEEP = ('<div class="keep"><div class="y rv"><h3><i>✓</i>Останется с вами</h3><ul><li>Единственное жильё (кроме ипотечного)</li>'
        '<li>Одежда, мебель, бытовая техника для жизни</li><li>Доход в пределах прожиточного минимума на вас и детей</li>'
        '<li>Пенсия и детские пособия — в пределах минимума</li><li>Работа: о банкротстве не сообщают работодателю</li></ul></div>'
        '<div class="n rv"><h3><i>×</i>Могут продать</h3><ul><li>Вторую квартиру, дачу, гараж, доли</li><li>Машину, если она не нужна для работы инвалида</li>'
        '<li>Дорогие вещи: украшения, технику сверх необходимого</li><li>Имущество, подаренное или проданное за 3 года до процедуры</li></ul></div></div>')

MYTH = ('<div class="myth">' + "".join(f'<div class="rv"><s>{a}</s><b>{b}</b></div>' for a, b in [
    ("«Заберут квартиру»", "Единственное жильё не забирают, даже если в нём 100 метров — кроме ипотечного."),
    ("«Не выпустят за границу»", "Ограничение может быть только на время процедуры и снимается после."),
    ("«Нельзя будет брать кредиты»", "5 лет нужно сообщать банку о банкротстве — но кредиты брать можно."),
    ("«Посадят»", "Только при фиктивном банкротстве. Мы заранее проверяем сделки за 3 года."),
    ("«Долги перейдут родственникам»", "Нет. Ваши долги списываются, поручители и созаёмщики — отдельная история."),
    ("«Это позор и все узнают»", "Сведения публикуют в реестре, но соседи и работодатель туда не ходят.")]) + "</div>")


def cfg() -> dict:
    return {
        "slug": "nol", "brand": "Ноль", "legal": "ООО «Ноль», Екатеринбург", "favLetter": "0", "logo": LOGO,
        "title": "Ноль — банкротство физических лиц в Екатеринбурге, списание долгов",
        "desc": "Банкротство физлиц в Екатеринбурге: тест «какой путь подходит», честная смета расходов, рассрочка на 10 месяцев. "
                "Внесудебное банкротство через МФЦ и через арбитражный суд.",
        "theme": {"bg": "#faf8f5", "ink": "#1d1b33", "soft": "#4a4860", "mut": "#86849a", "line": "#ebe7e0", "line2": "#d9d4ca",
                  "card": "#ffffff", "alt": "#f1eefb", "ac": "#4b3fd6", "aci": "#ffffff", "fh": "Manrope,sans-serif", "fb": "Manrope,sans-serif",
                  "hw": "800", "ht": "-.03em", "dk": "#1d1b33", "dki": "#fff", "rc": "22px", "rb": "14px", "kls": ".08em"},
        "fonts": [("Manrope", "manrope", [400, 600, 700, 800], "normal")],
        "images": IMAGES,
        "phone": ("+73430000000", "+7 343 000-00-00"),
        "mail": "help@nol.ysdprojects.space",
        "nav": [("test", "Подходит ли мне"), ("keep", "Что останется"), ("how", "Как проходит"), ("myths", "Страхи"), ("faq", "Вопросы")],
        "topCta": "Бесплатная консультация",
        "hero": {"kicker": "Банкротство физлиц · Екатеринбург", "h1": "Долги можно <em>списать законно</em> — и жить дальше",
                 "lead": "За 7 лет довели до конца 1 318 процедур. Сначала честно скажем, подходит ли вам банкротство, сколько оно стоит "
                         "целиком и что будет с имуществом. Если не подходит — так и скажем.",
                 "cta": "Пройти тест за минуту", "go": "test", "go2": ("lead", "Консультация бесплатно"),
                 "points": ["Рассрочка на 10 месяцев", "Цена в договоре не меняется", "Коллекторы перестанут звонить после подачи"],
                 "img": "talk", "alt": "Консультация юриста", "ar": "4/5",
                 "tag": "<b>от 79 000 ₽</b>под ключ, платёж от 7 900 ₽ в месяц"},
        "sections": [
            {"type": "html", "id": "test", "kick": "Тест", "h2": "Подходит ли вам банкротство и сколько оно стоит", "alt": True,
             "lead": "Четыре вопроса — и вы увидите свой путь и полную смету, включая расходы, о которых обычно молчат.", "html": TEST},
            {"type": "html", "id": "keep", "kick": "Имущество", "h2": "Что останется, а что могут продать", "html": KEEP},
            {"type": "steps", "id": "how", "kick": "Как проходит", "h2": "Семь–девять месяцев от заявления до справки о списании", "alt": True,
             "items": [("Бесплатный разбор", "Смотрим кредиты, имущество и сделки за 3 года. Говорим, подходит ли процедура.", "1 встреча, 60 минут"),
                       ("Документы и подача", "Собираем справки сами по доверенности и подаём в арбитражный суд.", "3–4 недели"),
                       ("Процедура", "Финансовый управляющий описывает имущество, кредиторы заявляют требования. Звонки коллекторов прекращаются.", "6–8 месяцев"),
                       ("Списание", "Суд завершает процедуру и освобождает от долгов. Отдаём решение и справку.", "долги — ноль")]},
            {"type": "html", "id": "myths", "dark": True, "kick": "Страхи", "h2": "Чего боятся — и как на самом деле", "html": MYTH},
            {"type": "gallery", "id": "office", "kick": "Офис", "h2": "Разговор без осуждения", "lead": "Приходите в офис на Малышева или разберём всё по видеосвязи.",
             "items": [{"img": "sign", "span": 7, "ar": "16/10", "alt": "Подписание документов"}, {"img": "paper", "span": 5, "ar": "4/5", "alt": "Юрист с документами"},
                       {"img": "two", "span": 6, "ar": "3/2", "alt": "Консультация"}, {"img": "hands", "span": 6, "ar": "3/2", "alt": "Договор"}]},
            {"type": "faq", "id": "faq", "kick": "Вопросы", "h2": "Что спрашивают на первой встрече", "alt": True,
             "items": [("Что если я не потяну рассрочку?", "Договоримся о паузе. Процедуру не прекращаем из-за просрочки нашего платежа на месяц-два."),
                       ("Можно ли сохранить машину?", "Иногда да: если она нужна для работы или стоит меньше расходов на продажу. Скажем после разбора."),
                       ("Узнают ли на работе?", "Работодатель узнает, только если финансовый управляющий попросит перечислять часть зарплаты на ваш счёт — это обычная бухгалтерия."),
                       ("Что будет с ипотекой?", "Если платите ипотеку без просрочек, есть законный путь сохранить квартиру. Это отдельный план — расскажем на встрече."),
                       ("Почему вы называете полную стоимость?", "Потому что иначе в середине процедуры всплывают «ещё 40 тысяч на публикации» — и человек бросает процедуру.")]},
        ],
        "contact": {"kick": "Консультация", "h2": "Разберём вашу ситуацию бесплатно",
                    "lead": "Юрист перезвонит в течение 30 минут в рабочее время. Без обязательств — решение принимаете вы.",
                    "rows": [("Адрес", "Екатеринбург, ул. Малышева, 51, офис 1106"), ("Телефон", "+7 343 000-00-00"), ("Часы", "Пн–сб 9:00–20:00")]},
        "form": {"fields": [("name", "Имя", "text", "Можно без фамилии", True), ("phone", "Телефон", "tel", "+7", True),
                            ("debt", "Сумма долгов", "select", ["до 300 000 ₽", "300 000 – 1 000 000 ₽", "1–3 млн ₽", "больше 3 млн ₽"]),
                            ("when", "Когда удобно позвонить", "select", ["Сейчас", "Сегодня вечером", "Завтра"])],
                 "ok": "Спасибо. Юрист перезвонит в течение 30 минут в рабочее время. Разговор ни к чему не обязывает.", "btn": "Записаться на разбор"},
        "css": CSS, "js": JS,
    }
