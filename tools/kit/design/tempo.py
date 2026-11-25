"""«Темп» — дизайн мобильного приложения для бега: экраны, кликабельный прототип, светлая и тёмная тема, компоненты."""


def ring(p, size=148, w=12, col="var(--a)"):
    import math
    r = (size - w) / 2
    c = 2 * math.pi * r
    return (f'<svg viewBox="0 0 {size} {size}" class="ring"><circle cx="{size / 2}" cy="{size / 2}" r="{r}" fill="none" stroke="var(--l)" stroke-width="{w}"/>'
            f'<circle cx="{size / 2}" cy="{size / 2}" r="{r}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" '
            f'stroke-dasharray="{c * p:.1f} {c:.1f}" transform="rotate(-90 {size / 2} {size / 2})"/></svg>')


BARS = [3.2, 5.1, 0, 7.4, 4.0, 0, 12.6]
WEEK = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

S_TODAY = ('<div class="sc"><div class="st"><span>9:41</span><span>●●● ▮</span></div><div class="hd"><div><small>Суббота, 14 ноября</small><h4>Привет, Лена</h4></div><i class="av">Л</i></div>'
           '<div class="cardx hero2"><div class="rg">' + ring(.68) + '<div><b>21,7</b><small>из 32 км</small></div></div><div class="hs2"><div><b>3</b><small>пробежки</small></div><div><b>5:42</b><small>темп /км</small></div><div><b>2 ч 07</b><small>в движении</small></div></div></div>'
           '<div class="cardx"><div class="row"><b>Неделя</b><small>+18% к прошлой</small></div><div class="bars">'
           + "".join(f'<div><i style="height:{max(4, v / 12.6 * 64):.0f}px" class="{"t" if i == 5 else ""}"></i><small>{d}</small></div>' for i, (v, d) in enumerate(zip(BARS, WEEK))) +
           '</div></div><div class="cardx plan"><small>План на сегодня</small><b>Лёгкий бег 6 км</b><span>темп 6:10–6:30 · пульс до 145</span><button class="go" data-sc="run">Начать</button></div>'
           '<div class="tabs"><b class="on">Сегодня</b><b data-sc="plan">План</b><b data-sc="stats">Статистика</b><b data-sc="me">Профиль</b></div></div>')

ROUTE = "M30 250 C60 200 50 150 100 130 S170 120 190 80 S260 40 290 70 S330 150 300 190 S220 230 190 260"
S_RUN = ('<div class="sc dark2"><div class="st"><span>9:41</span><span>●●● ▮</span></div>'
         '<div class="map"><svg viewBox="0 0 340 300"><rect width="340" height="300" fill="var(--map)"/>'
         '<g stroke="var(--road)" stroke-width="10" fill="none" stroke-linecap="round"><path d="M-10 60 L350 120"/><path d="M80 -10 L140 310"/><path d="M-10 230 L350 200"/><path d="M250 -10 L230 310"/></g>'
         f'<path d="{ROUTE}" fill="none" stroke="var(--a)" stroke-width="6" stroke-linecap="round"/><circle cx="190" cy="260" r="10" fill="var(--a)" stroke="#fff" stroke-width="4"/></svg></div>'
         '<div class="live"><small>Дистанция</small><b class="big">4,28</b><small>км</small><div class="lg3"><div><b>24:17</b><small>время</small></div><div><b>5:40</b><small>темп</small></div><div><b>151</b><small>пульс</small></div></div>'
         '<div class="zone"><i style="width:62%"></i></div><small class="zl">Зона 3 — держите темп, до цели 1,72 км</small>'
         '<div class="ctl"><button class="sq" data-sc="today">■</button><button class="pz">❚❚</button><button class="sq">🔒</button></div></div></div>')

S_PLAN = ('<div class="sc"><div class="st"><span>9:41</span><span>●●● ▮</span></div><div class="hd"><div><small>Цель: полумарафон 26 апреля</small><h4>План на неделю</h4></div></div>'
          + "".join(f'<div class="pl2 {c}"><i>{d}</i><div><b>{t}</b><small>{s}</small></div><em>{e}</em></div>' for d, t, s, e, c in [
              ("Пн", "Отдых", "растяжка 15 мин", "✓", "dn"), ("Вт", "Интервалы 6 × 400 м", "темп 4:55, отдых 2 мин", "✓", "dn"),
              ("Ср", "Отдых", "", "", "rs"), ("Чт", "Темповый 8 км", "темп 5:20", "✓", "dn"), ("Пт", "Лёгкий бег 5 км", "пульс до 145", "✓", "dn"),
              ("Сб", "Лёгкий бег 6 км", "сегодня", "→", "nw"), ("Вс", "Длинная 14 км", "темп 6:15", "", "")])
          + '<div class="tabs"><b data-sc="today">Сегодня</b><b class="on">План</b><b data-sc="stats">Статистика</b><b data-sc="me">Профиль</b></div></div>')

MONTHS = [(84, "июл"), (96, "авг"), (71, "сен"), (112, "окт"), (127, "ноя")]
S_STATS = ('<div class="sc"><div class="st"><span>9:41</span><span>●●● ▮</span></div><div class="hd"><div><small>За 5 месяцев</small><h4>Статистика</h4></div></div>'
           '<div class="cardx"><div class="row"><b>Километры</b><small>490 км</small></div><div class="bars m">'
           + "".join(f'<div><i style="height:{v / 127 * 90:.0f}px" class="{"t" if i == 4 else ""}"></i><small>{m}</small></div>' for i, (v, m) in enumerate(MONTHS)) +
           '</div></div><div class="cardx"><div class="row"><b>Лучшие результаты</b></div>'
           + "".join(f'<div class="pr"><span>{a}</span><b>{b}</b><small>{c}</small></div>' for a, b, c in [("5 км", "26:41", "2 ноября"), ("10 км", "56:12", "19 октября"), ("21,1 км", "—", "цель 2:05")]) +
           '</div><div class="tabs"><b data-sc="today">Сегодня</b><b data-sc="plan">План</b><b class="on">Статистика</b><b data-sc="me">Профиль</b></div></div>')

S_ME = ('<div class="sc"><div class="st"><span>9:41</span><span>●●● ▮</span></div><div class="me2"><i class="av b">Л</i><h4>Лена Соколова</h4><small>бегает с марта 2025 · клуб «Набережная»</small></div>'
        '<div class="cardx"><div class="row"><b>Кроссовки</b><small>замена через 112 км</small></div><div class="zone"><i style="width:78%"></i></div><small class="zl">388 из 500 км</small></div>'
        + "".join(f'<div class="li"><span>{a}</span><small>{b}</small></div>' for a, b in [("Часы и пульсометр", "подключены"), ("Голосовые подсказки", "каждый км"), ("Тема", "как в системе"), ("Напоминания", "Вт, Чт, Сб в 7:30")])
        + '<div class="tabs"><b data-sc="today">Сегодня</b><b data-sc="plan">План</b><b data-sc="stats">Статистика</b><b class="on">Профиль</b></div></div>')

S_ONB = ('<div class="sc onb"><div class="st"><span>9:41</span><span>●●● ▮</span></div><div class="onb-a">' + ring(.42, 220, 18) + '<b>Темп</b></div>'
         '<h4>Бегайте по плану,<br>а не по настроению</h4><p>План под вашу цель, подсказки во время бега и честная статистика</p>'
         '<div class="opts">' + "".join(f'<span class="{c}">{t}</span>' for t, c in [("Первые 5 км", ""), ("10 км быстрее", ""), ("Полумарафон", "on"), ("Просто бегать", "")]) +
         '</div><button class="go w" data-sc="today">Составить план</button></div>')

SCREENS = {"onb": ("Знакомство", S_ONB), "today": ("Сегодня", S_TODAY), "run": ("Пробежка", S_RUN), "plan": ("План", S_PLAN),
           "stats": ("Статистика", S_STATS), "me": ("Профиль", S_ME)}

CSS = r"""
.hero h1{font-size:clamp(44px,6vw,92px)}
.ph{--a:#ff4f2e;--b:#fff;--t:#16181d;--m:#7b8190;--c:#f3f4f6;--l:#e7e9ee;--map:#e9ecef;--road:#fff;width:300px;max-width:100%;aspect-ratio:300/620;border-radius:44px;background:#0b0c0f;padding:10px;box-shadow:0 40px 80px -40px rgba(0,0,0,.6);position:relative;margin:0 auto}
.ph.dk{--b:#101216;--t:#f4f5f7;--m:#8b919c;--c:#1b1e24;--l:#2a2e36;--map:#1b1f26;--road:#2b3039}
.ph::before{content:"";position:absolute;top:16px;left:50%;transform:translateX(-50%);width:84px;height:24px;border-radius:14px;background:#0b0c0f;z-index:3}
.sc{height:100%;border-radius:35px;background:var(--b);color:var(--t);overflow:hidden;display:flex;flex-direction:column;gap:10px;padding:0 14px 0;position:relative;font:400 12px/1.35 var(--fb)}
.st{display:flex;justify-content:space-between;padding:14px 10px 0;font-weight:600;font-size:11px}
.hd{display:flex;justify-content:space-between;align-items:center;margin-top:16px}
.hd small{color:var(--m)}.hd h4,.me2 h4,.onb h4{margin:2px 0 0;font:700 21px/1.15 var(--fh);letter-spacing:-.02em}
.av{width:36px;height:36px;border-radius:50%;background:var(--a);color:#fff;display:grid;place-items:center;font-style:normal;font-weight:700}
.av.b{width:72px;height:72px;font-size:28px;margin:0 auto 8px}
.cardx{background:var(--c);border-radius:20px;padding:13px}
.hero2{display:grid;gap:12px}
.rg{display:flex;align-items:center;gap:14px}.rg .ring{width:96px;height:96px;flex:none}.rg b{display:block;font:700 30px/1 var(--fh)}.rg small{color:var(--m)}
.hs2{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}.hs2 b{display:block;font:700 15px var(--fh)}.hs2 small{color:var(--m);font-size:10.5px}
.row{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px}.row b{font-size:13px}.row small{color:var(--a);font-weight:600}
.bars{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;align-items:end;height:84px}.bars.m{grid-template-columns:repeat(5,1fr);height:112px}
.bars div{display:grid;justify-items:center;gap:4px;align-content:end;height:100%}.bars i{width:100%;max-width:22px;border-radius:6px;background:var(--l)}.bars i.t{background:var(--a)}
.bars small{color:var(--m);font-size:10px}
.plan{display:grid;gap:2px;background:var(--t);color:var(--b)}.plan small{opacity:.6}.plan b{font:700 17px var(--fh)}.plan span{opacity:.7;font-size:11px}
.go{margin-top:8px;height:40px;border-radius:12px;background:var(--a);color:#fff;font-weight:700;font-size:13px}.go.w{margin:auto 0 22px;height:48px}
.tabs{margin-top:auto;display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--l);padding:10px 0 20px;font-size:10.5px;color:var(--m);text-align:center}
.tabs b{font-weight:500;cursor:pointer}.tabs b.on{color:var(--a);font-weight:700}
.dark2{background:var(--b)}
.map{margin:6px -14px 0;height:44%;overflow:hidden}.map svg{width:100%;height:100%}
.live{display:grid;justify-items:center;text-align:center;gap:2px;padding:6px 0 0}.live small{color:var(--m)}.live .big{font:800 52px/1 var(--fh);letter-spacing:-.03em}
.lg3{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;width:100%;margin:10px 0}.lg3 b{display:block;font:700 18px var(--fh)}.lg3 small{font-size:10.5px}
.zone{height:8px;border-radius:4px;background:var(--l);overflow:hidden;width:100%}.zone i{display:block;height:100%;background:linear-gradient(90deg,#3fbf7f,#ffc83d,var(--a))}
.zl{display:block;margin-top:6px;font-size:11px;color:var(--m)}
.ctl{display:flex;gap:18px;align-items:center;margin-top:14px}.ctl button{width:52px;height:52px;border-radius:50%;background:var(--c);color:var(--t);font-size:16px}.ctl .pz{width:72px;height:72px;background:var(--a);color:#fff;font-size:20px}
.pl2{display:grid;grid-template-columns:30px 1fr auto;gap:10px;align-items:center;padding:9px 12px;border-radius:14px;background:var(--c)}
.pl2 i{font-style:normal;font-weight:700;color:var(--m);font-size:11px}.pl2 b{display:block;font-size:12.5px}.pl2 small{color:var(--m);font-size:10.5px}.pl2 em{font-style:normal;color:#3fbf7f;font-weight:700}
.pl2.rs{opacity:.55}.pl2.nw{background:var(--t);color:var(--b)}.pl2.nw em{color:var(--a)}.pl2.nw small{color:inherit;opacity:.65}
.pr{display:grid;grid-template-columns:1fr auto;gap:0 8px;padding:8px 0;border-top:1px solid var(--l)}.pr b{font:700 15px var(--fh)}.pr small{grid-column:1;color:var(--m);font-size:10.5px}
.me2{text-align:center;margin-top:22px}.me2 small{color:var(--m)}
.li{display:flex;justify-content:space-between;padding:12px 4px;border-bottom:1px solid var(--l);font-size:12.5px}.li small{color:var(--m)}
.onb{text-align:center}.onb-a{position:relative;width:170px;margin:34px auto 8px}.onb-a .ring{width:170px;height:170px}.onb-a b{position:absolute;inset:0;display:grid;place-items:center;font:800 30px var(--fh);color:var(--a)}
.onb p{color:var(--m);margin:8px 10px 14px}.opts{display:flex;flex-wrap:wrap;gap:6px;justify-content:center}.opts span{padding:8px 12px;border-radius:999px;background:var(--c);font-size:11.5px;font-weight:600}.opts span.on{background:var(--t);color:var(--b)}
.proto{display:grid;grid-template-columns:minmax(0,1fr) 320px minmax(0,1fr);gap:clamp(20px,4vw,56px);align-items:center}
.proto .pt h3{font-size:clamp(26px,2.6vw,36px);margin-bottom:12px}.proto .pt p{color:var(--soft)}
.flow{display:grid;gap:8px;margin-top:20px}.flow button{display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:14px;background:var(--card);text-align:left;box-shadow:0 0 0 1px var(--line)}
.flow button.on{box-shadow:0 0 0 2px var(--ac)}.flow button i{font-style:normal;font:700 13px var(--fm,var(--fb));color:var(--ac);width:22px}
.notes{display:grid;gap:12px}.notes div{padding:14px 16px;border-radius:14px;background:var(--card);box-shadow:0 0 0 1px var(--line);font-size:14.5px;color:var(--soft)}.notes b{color:var(--ink);display:block;margin-bottom:4px}
.phs{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:14px;justify-items:center}.phs .ph{width:300px;zoom:.62}
@media (max-width:1300px){.phs .ph{zoom:.55}}
.cmp{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}.cmp>div{background:var(--card);border-radius:18px;padding:18px;box-shadow:0 0 0 1px var(--line)}
.cmp h5{margin:0 0 12px;font:600 13px var(--fb);color:var(--mut);letter-spacing:.06em;text-transform:uppercase}
.btns{display:grid;gap:8px}.btns span{display:grid;place-items:center;height:44px;border-radius:12px;font-weight:700;font-size:14px}
@media (max-width:1100px){.proto{grid-template-columns:1fr}.proto .notes{order:3}.phs{grid-template-columns:repeat(3,minmax(0,1fr))}.cmp{grid-template-columns:1fr}}
@media (max-width:560px){.phs{grid-template-columns:repeat(2,minmax(0,1fr))}.phs .ph{zoom:.54}}
"""

JS = r"""
(function(){var S=window.CASECFG.screens,ph=document.getElementById('pPh'),fl=document.getElementById('pFlow');
function show(k){ph.innerHTML=S[k];fl.querySelectorAll('button').forEach(function(b){b.classList.toggle('on',b.dataset.k===k)})}
ph.addEventListener('click',function(e){var t=e.target.closest('[data-sc]');if(t)show(t.dataset.sc)});
fl.addEventListener('click',function(e){var b=e.target.closest('button');if(b)show(b.dataset.k)});
document.getElementById('pTh').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;this.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)});
 document.querySelectorAll('.ph').forEach(function(p){p.classList.toggle('dk',b.dataset.t==='dk')})});
show('today');
})();
"""


def cfg() -> dict:
    flow = "".join(f'<button type="button" data-k="{k}"><i>0{i + 1}</i>{t}</button>' for i, (k, (t, _)) in enumerate(SCREENS.items()))
    proto = ('<div class="proto"><div class="pt"><h3>Нажимайте прямо на экран</h3><p>Кнопки и вкладки работают: начните пробежку, остановите её, '
             'откройте план или статистику. Это прототип из Figma, перенесённый на страницу.</p><div class="flow" id="pFlow">' + flow + '</div></div>'
             '<div class="ph" id="pPh"></div><div class="notes"><div class="seg" id="pTh" style="justify-self:start"><button type="button" class="on" data-t="lt">Светлая</button><button type="button" data-t="dk">Тёмная</button></div>'
             '<div><b>Старт в два касания</b>С главного экрана: «Начать» — и бег пошёл. В старом приложении было пять экранов настроек.</div>'
             '<div><b>Крупные цифры на бегу</b>Дистанция 52 pt, темп и пульс — 18 pt: читается на вытянутой руке при тряске.</div>'
             '<div><b>Тёмная тема для утра</b>Половина пробежек до рассвета: тёмная тема не слепит и экономит батарею на OLED.</div></div></div>')
    phs = '<div class="phs">' + "".join(f'<figure style="margin:0"><div class="ph">{h}</div><figcaption class="cap">{t}</figcaption></figure>' for t, h in SCREENS.values()) + '</div>'
    comp = ('<div class="cmp"><div><h5>Кнопки</h5><div class="btns"><span style="background:#ff4f2e;color:#fff">Начать</span><span style="background:#16181d;color:#fff">Составить план</span>'
            '<span style="box-shadow:inset 0 0 0 1.5px #d9dce3">Пропустить</span><span style="background:#f3f4f6;color:#9aa0ab">Недоступно</span></div></div>'
            '<div><h5>Пульсовые зоны</h5><div class="btns">' + "".join(f'<span style="background:{c};color:#fff;justify-content:start;padding-left:14px;display:flex">{t}</span>'
                                                                      for t, c in [("Зона 1 · до 125", "#7fb7ff"), ("Зона 2 · 125–145", "#3fbf7f"), ("Зона 3 · 145–160", "#ffc83d"), ("Зона 4 · 160+", "#ff4f2e")]) + '</div></div>'
            '<div><h5>Отступы и скругления</h5><div class="btns"><span style="background:#f3f4f6;border-radius:20px">карточка · 20</span><span style="background:#f3f4f6;border-radius:12px">кнопка · 12</span>'
            '<span style="background:#f3f4f6;border-radius:999px">чип · 999</span><span style="background:#f3f4f6;border-radius:6px">столбик · 6</span></div></div></div>')
    return {
        "slug": "design/tempo", "brand": "Темп", "favLetter": "Т",
        "layout": 'index', "header": 'ink', "secHead": 'stack', "resStyle": 'band', "ctaStyle": 'block',  # layout
        "title": "Темп — дизайн мобильного приложения для бега · YSD DEV",
        "desc": "Дизайн мобильного приложения для бега: кликабельный прототип, шесть экранов, светлая и тёмная тема, компоненты и пульсовые зоны.",
        "theme": {"bg": "#f4f4f1", "ink": "#16181d", "soft": "#4f5562", "mut": "#828896", "line": "#e2e3e0", "line2": "#c9cbc6",
                  "card": "#ffffff", "alt": "#ecebe6", "ac": "#ff4f2e", "aci": "#ffffff", "fh": '"Rubik",sans-serif', "fb": '"Rubik",sans-serif',
                  "fm": '"JetBrains Mono",monospace', "hw": "700", "ht": "-.03em", "cbg": "#ff4f2e", "cink": "#fff", "cbtn": "#16181d", "cbtni": "#fff"},
        "fonts": [("Rubik", "rubik", [400, 500, 600, 700, 800], "normal"), ("JetBrains Mono", "jetbrains-mono", [500], "normal")],
        "css": CSS,
        "hero": {"kicker": "Дизайн мобильного приложения", "h1": "Бег по плану <em>в два касания</em>",
                 "lead": "Приложение для бегунов-любителей: план под цель, подсказки во время пробежки и статистика без лишних графиков. "
                         "Шесть экранов, две темы и библиотека компонентов в Figma.",
                 "art": '<div style="padding:28px 0;background:linear-gradient(160deg,#ffe2d9,#f4f4f1)"><div class="ph" style="width:270px">' + S_TODAY + '</div></div>',
                 "cta": "Открыть прототип", "go": "proto"},
        "facts": [("Клиент", "«Темп», беговой клуб и приложение"), ("Работа", "UX, 6 экранов, 2 темы, компоненты"),
                  ("Срок", "3 недели"), ("Тест с бегунами", "11 человек, 2 итерации")],
        "data": {"screens": {k: v[1] for k, v in SCREENS.items()}},
        "sections": [
            {"type": "text3", "id": "task", "nav": "Задача", "kick": "Задача", "h2": "Что мешало бегать с приложением",
             "items": [("01", "Долгий старт", "Пять экранов настроек перед пробежкой. Люди запускали таймер на часах и забывали про приложение."),
                       ("02", "Мелкие цифры", "Темп и пульс не прочитать на бегу: телефон в руке трясётся, солнце бликует на экране."),
                       ("03", "План без смысла", "Тренировки шли списком без цели. Непонятно, зачем сегодня 6 км медленно, а завтра отдых.")]},
            {"type": "html", "id": "proto", "nav": "Прототип", "kick": "Прототип", "h2": "Попробуйте приложение", "html": proto, "alt": True},
            {"type": "html", "id": "screens", "nav": "Экраны", "kick": "Экраны", "h2": "Шесть ключевых экранов", "html": phs},
            {"type": "html", "id": "ui", "nav": "Компоненты", "kick": "Компоненты", "h2": "Библиотека для разработчиков", "alt": True,
             "lead": "Все элементы собраны в Figma с вариантами и токенами — разработчики забирают размеры и цвета без вопросов.", "html": comp},
            {"type": "palette", "id": "color", "kick": "Цвет", "h2": "Один акцент — оранжевый финиш",
             "colors": [("Финиш", "#FF4F2E", "кнопки, активный показатель"), ("Асфальт", "#16181D", "текст, тёмная тема"), ("Разметка", "#F3F4F6", "карточки"),
                        ("Зона 2", "#3FBF7F", "лёгкий бег, выполнено"), ("Зона 3", "#FFC83D", "темповый бег")]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что показал тест", "alt": True,
             "stats": [("2 касания", "от открытия до старта пробежки"), ("10 из 11", "бегунов прошли все задачи без подсказки"), ("−64%", "времени на старт"), ("38", "компонентов в библиотеке")]},
        ],
        "ctaTitle": "Нужен дизайн приложения?",
        "js": JS,
    }
