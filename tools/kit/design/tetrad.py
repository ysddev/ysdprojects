"""«Тетрадь» — дизайн мобильного приложения онлайн-школы: расписание, урок, домашка с пометками учителя, прогресс, экран родителя."""

PEN, RED, PAPER, GRID, HL, INK = "#2346d1", "#e0413a", "#fbfbf7", "#dfe6f3", "#ffe066", "#18203a"
FB, FN = "Onest", "Gabriela"

ST = '<div class="st"><span>9:41</span><span>▮▮▮ ◖</span></div>'


def tabs(on):
    items = [("today", "Сегодня", "◷"), ("lesson", "Урок", "▶"), ("hw", "Домашка", "✎"), ("prog", "Успехи", "▦")]
    return '<nav class="tb">' + "".join(f'<button type="button" data-s="{k}" class="{"on" if k == on else ""}"><i>{i}</i>{n}</button>' for k, n, i in items) + "</nav>"


S_TODAY = (f'<div class="sc">{ST}<div class="hd"><div><small>Вторник, 24 ноября</small><h4>Привет, Миша</h4></div><i class="av">М</i></div>'
           '<div class="streak"><b>12 дней</b> подряд без пропусков</div><h5>Уроки сегодня</h5><ul class="tl">'
           + "".join(f'<li class="{c}"><time>{t}</time><div><b>{a}</b><span>{b}</span></div></li>'
                     for t, a, b, c in [("15:00", "Английский", "Present Perfect", "done"),
                                        ("16:30", "Математика", "дроби", "now"), ("18:00", "Программирование", "циклы в Python", "")])
           + '</ul><div class="due"><small>Сдать до четверга</small><b>Математика: 12 задач</b><span class="bar"><i style="width:58%"></i></span><span>7 из 12 решено</span></div>'
           + tabs("today") + "</div>")

S_LESSON = (f'<div class="sc">{ST}<div class="video"><span class="live">идёт урок</span><button type="button" aria-label="Смотреть">▶</button><em>Игорь Олегович</em></div>'
            '<div class="pad"><small>Математика · 6 класс</small><h4>Сложение дробей с разными знаменателями</h4>'
            '<ul class="mat">' + "".join(f'<li><i>{i}</i><div><b>{a}</b><span>{b}</span></div></li>' for i, a, b in
                                         [("▤", "Конспект урока", "PDF, 3 страницы"), ("✎", "Тренажёр", "10 примеров, ответ сразу"), ("?", "Вопрос учителю", "ответит до вечера")])
            + '</ul></div>' + tabs("lesson") + "</div>")

S_HW = (f'<div class="sc">{ST}<div class="hd"><div><small>Английский</small><h4>Домашка</h4></div><span class="mark">5</span></div><ul class="hw">'
        + "".join(f'<li class="{c}"><i></i><div><b>{a}</b>{n}</div></li>' for a, n, c in [
            ("I have already done my homework.", "", "ok"), ("She has never been to London.", "", "ok"),
            ("We have lived here since 2020.", '<em class="note">отлично, since — верно!</em>', "ok"),
            ("They has finished the project.", '<em class="note">have — они, а не он</em>', "err"), ("Have you ever seen snow?", "", "")])
        + '</ul><button type="button" class="send">Отправить учителю</button>' + tabs("hw") + "</div>")

SUBJ = [("Английский", 92, PEN), ("Математика", 74, PEN), ("Программирование", 86, PEN), ("Русский язык", 61, RED)]
S_PROG = (f'<div class="sc">{ST}<div class="hd"><div><small>Ноябрь</small><h4>Успехи</h4></div></div><div class="big"><b>4,6</b><span>средняя оценка, выше на 0,3 чем в октябре</span></div>'
          '<ul class="subj">' + "".join(f'<li><div><b>{n}</b><span>{p}%</span></div><span class="bar"><i style="width:{p}%;background:{c}"></i></span></li>' for n, p, c in SUBJ)
          + '</ul><p class="tip"><b>Совет учителя:</b> 10 минут на диктант в день — и русский догонит остальные.</p>' + tabs("prog") + "</div>")

S_PARENT = (f'<div class="sc">{ST}<div class="hd"><div><small>Родитель</small><h4>Миша, 6 класс</h4></div><i class="av b">М</i></div>'
            '<div class="cards2"><div><b>18 из 18</b><span>уроков посещено</span></div><div><b>4,6</b><span>средняя оценка</span></div></div>'
            '<div class="due"><small>Абонемент</small><b>Осталось 3 урока из 24</b><span class="bar"><i style="width:88%"></i></span>'
            '<button type="button" class="send">Продлить — 9 600 ₽</button></div>'
            '<div class="msg"><small>Елена Викторовна, вчера</small><p>Миша хорошо работал на уроке, домашку сдал вовремя.</p></div>' + tabs("today") + "</div>")

SCREENS = {"today": S_TODAY, "lesson": S_LESSON, "hw": S_HW, "prog": S_PROG, "parent": S_PARENT}

PROTO = ('<div class="pr"><div class="phone" id="ph">' + S_TODAY + '</div><div class="pr-r"><h3>Кликайте по вкладкам внизу экрана</h3>'
         '<p>Ученик видит уроки и домашку, родитель — посещаемость, оценки и сколько уроков осталось в абонементе. Один вход, две роли.</p>'
         '<div class="seg" id="role"><button type="button" class="on" data-r="kid">Ученик</button><button type="button" data-r="parent">Родитель</button></div>'
         '<ul class="pts"><li>Красная ручка учителя — прямо в строке с ошибкой, как в тетради</li><li>Ближайший дедлайн всегда на главном экране</li>'
         '<li>Оплата абонемента — в два касания из экрана родителя</li></ul></div></div>')

ROW = '<div class="row">' + "".join(f'<figure><div class="phone sm">{SCREENS[k]}</div><figcaption>{n}</figcaption></figure>'
                                    for k, n in [("today", "Сегодня"), ("lesson", "Урок"), ("hw", "Домашка"), ("prog", "Успехи"), ("parent", "Родитель")]) + "</div>"

CSS = """
.hero h1{font-size:clamp(42px,5.4vw,82px);font-weight:800}
.phone{--w:300px;width:var(--w);aspect-ratio:300/620;border-radius:44px;background:#0c0f1a;padding:10px;box-shadow:0 40px 80px -50px rgba(24,32,58,.6);flex:none}
.phone .sc{position:relative;height:100%;border-radius:36px;overflow:hidden;color:var(--ink);font-size:14px;
 background-color:#fbfbf7;background-image:linear-gradient(#e6ecf6 1px,transparent 1px),linear-gradient(90deg,#e6ecf6 1px,transparent 1px);background-size:22px 22px}
.st{display:flex;justify-content:space-between;padding:12px 22px 4px;font-size:14px;font-weight:600}
.hd{display:flex;justify-content:space-between;align-items:center;padding:8px 18px 6px}.hd small{color:#5b6383;font-size:14px}.hd h4{margin:2px 0 0;font-size:22px;font-weight:800}
.av{width:42px;height:42px;border-radius:50%;background:var(--ac);color:#fff;display:grid;place-items:center;font-style:normal;font-weight:700}.av.b{background:#e0413a}
.streak{margin:6px 18px;padding:9px 12px;background:#ffe066;border-radius:12px;font-size:14px}.streak b{font-weight:800}
h5{margin:12px 18px 4px;font-size:14px;color:#5b6383;font-weight:600}
.tl{list-style:none;margin:0;padding:0 18px}.tl li{display:grid;grid-template-columns:46px 1fr;gap:8px;padding:8px 0;border-bottom:1px dashed #c6d0e6}
.tl time{font-weight:700;font-size:14px}.tl b{display:block;font-size:15px}.tl span{font-size:14px;color:#5b6383}
.tl li.done{opacity:.5}.tl li.now b::after{content:" · сейчас";color:#e0413a;font-weight:700}
.due{margin:12px 18px;padding:12px;background:#fff;border-radius:16px;box-shadow:0 0 0 1px #dfe6f3}.due small{color:#5b6383;font-size:14px}.due b{display:block;font-size:16px;margin:2px 0 8px}
.due>span:last-child{font-size:14px;color:#5b6383}
.bar{display:block;height:8px;border-radius:4px;background:#e7ebf5;overflow:hidden;margin-bottom:6px}.bar i{display:block;height:100%;background:var(--ac);border-radius:4px}
.tb{position:absolute;left:0;right:0;bottom:0;display:grid;grid-template-columns:repeat(4,1fr);background:#fff;border-top:1px solid #dfe6f3;padding:6px 4px 16px}
.tb button{font-size:13px;color:#6b7390;display:grid;justify-items:center;gap:2px;padding:4px 0;min-height:44px}.tb i{font-style:normal;font-size:18px}.tb .on{color:var(--ac);font-weight:700}
.video{height:180px;background:linear-gradient(135deg,#2346d1,#18203a);position:relative;display:grid;place-items:center;color:#fff;margin:6px 10px;border-radius:20px}
.video button{width:58px;height:58px;border-radius:50%;background:#fff;color:var(--ac);font-size:22px}.video em{position:absolute;left:14px;bottom:10px;font-style:normal;font-size:14px}
.live{position:absolute;left:14px;top:12px;background:#e0413a;color:#fff;font-size:12px;font-weight:700;padding:3px 8px;border-radius:8px}
.pad{padding:6px 18px}.pad small{color:#5b6383;font-size:14px}.pad h4{margin:4px 0 10px;font-size:19px;line-height:1.25;font-weight:800}
.mat{list-style:none;margin:0;padding:0;display:grid;gap:8px}.mat li{display:grid;grid-template-columns:36px 1fr;gap:10px;align-items:center;background:#fff;border-radius:14px;padding:9px;box-shadow:0 0 0 1px #dfe6f3}
.mat i{width:36px;height:36px;border-radius:10px;background:#e8edfc;color:var(--ac);display:grid;place-items:center;font-style:normal}.mat b{display:block;font-size:15px}.mat span{font-size:14px;color:#5b6383}
.mark{font:700 40px/1 Gabriela,serif;color:#e0413a;transform:rotate(-8deg)}
.hw{list-style:none;margin:0;padding:4px 18px;display:grid;gap:4px}.hw li{display:grid;grid-template-columns:22px 1fr;gap:8px;padding:6px 0}
.hw i{width:20px;height:20px;border-radius:6px;border:2px solid #aab4cf;margin-top:2px}.hw .ok i{background:var(--ac);border-color:var(--ac)}.hw .err i{background:#e0413a;border-color:#e0413a}
.hw b{font-weight:500;font-size:15px}.hw .err b{text-decoration:underline wavy #e0413a;text-underline-offset:4px}
.note{display:block;font:400 16px/1.2 Gabriela,serif;color:#e0413a;margin-top:3px}
.send{display:block;margin:12px 18px;width:calc(100% - 36px);padding:12px;border-radius:14px;background:var(--ac);color:#fff;font-weight:700;font-size:15px}
.due .send{margin:10px 0 0;width:100%}
.big{margin:4px 18px 8px}.big b{font-size:52px;font-weight:800;color:var(--ac);line-height:1}.big span{display:block;font-size:14px;color:#5b6383}
.subj{list-style:none;margin:0;padding:0 18px;display:grid;gap:9px}.subj div{display:flex;justify-content:space-between;font-size:14px}
.tip{margin:12px 18px;padding:10px 12px;background:#fff;border-left:3px solid #e0413a;font-size:14px}
.cards2{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:8px 18px}.cards2 div{background:#fff;border-radius:14px;padding:10px;box-shadow:0 0 0 1px #dfe6f3}
.cards2 b{display:block;font-size:20px;font-weight:800}.cards2 span{font-size:14px;color:#5b6383}
.msg{margin:0 18px;padding:10px 12px;background:#e8edfc;border-radius:14px 14px 14px 4px}.msg small{font-size:14px;color:#5b6383}.msg p{margin:2px 0 0;font-size:14px}
.pr{display:grid;grid-template-columns:auto minmax(0,1fr);gap:clamp(28px,5vw,80px);align-items:center}
.pr-r h3{font-size:clamp(26px,2.6vw,38px);margin-bottom:12px}.pr-r p{color:var(--soft);margin-bottom:18px}
.pts{margin:20px 0 0;padding:0;list-style:none;display:grid;gap:10px}.pts li{padding:14px 16px;border-radius:14px;background:var(--card);font-size:15px;box-shadow:0 0 0 1px var(--line)}
.row{display:flex;gap:22px;overflow-x:auto;padding:6px 4px 18px;scroll-snap-type:x mandatory}.row figure{margin:0;scroll-snap-align:start}
.row figcaption{text-align:center;font-size:14px;color:var(--mut);margin-top:10px}.phone.sm{--w:250px;pointer-events:none}
.phone.sm .sc{zoom:.833}
@media (max-width:760px){.pr{grid-template-columns:1fr;justify-items:center}.phone{--w:min(300px,86vw)}}
"""

JS = r"""
(function(){var S=window.CASECFG.screens,ph=document.getElementById('ph'),role='kid';
ph.addEventListener('click',function(e){var b=e.target.closest('.tb button');if(!b)return;var k=b.dataset.s;if(k==='today'&&role==='parent')k='parent';ph.innerHTML=S[k]});
var r=document.getElementById('role');r.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;r.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b)});
 role=b.dataset.r;ph.innerHTML=S[role==='parent'?'parent':'today']});
})();
"""


def cfg() -> dict:
    return {
        "slug": "design/tetrad", "brand": "Тетрадь", "favLetter": "Т",
        "layout": 'side', "header": 'float', "secHead": 'split', "resStyle": 'band', "ctaStyle": 'ac',  # layout
        "title": "Тетрадь — дизайн приложения онлайн-школы · YSD DEV",
        "desc": "Дизайн мобильного приложения онлайн-школы: расписание, урок с материалами, домашка с пометками учителя красной ручкой, "
                "успехи по предметам и экран родителя с абонементом; кликабельный прототип.",
        "theme": {"bg": "#f4f6fb", "ink": INK, "soft": "#3d4566", "mut": "#5b6383", "line": GRID, "line2": "#c6d0e6", "card": "#fff", "alt": "#eaeef8",
                  "ac": PEN, "aci": "#fff", "fh": f'"{FB}",sans-serif', "fb": f'"{FB}",sans-serif', "hw": "800", "ht": "-.03em",
                  "cbg": PEN, "cink": "#fff", "cbtn": HL, "cbtni": INK, "kc": RED, "rc": PEN},
        "fonts": [(FB, "onest", [400, 500, 600, 700, 800], "normal"), (FN, "gabriela", [400], "normal")],
        "css": CSS + ".kick{text-transform:none;letter-spacing:0;font-size:15px}",
        "data": {"screens": SCREENS},
        "hero": {"kicker": "Дизайн мобильного приложения", "h1": "Школьная тетрадь, которая сама напоминает о домашке",
                 "lead": "Приложение онлайн-школы для учеников 5–9 классов и их родителей. Знакомый образ тетради в клетку и красная ручка учителя "
                         "вместо скучных таблиц электронного дневника.",
                 "art": '<div style="display:flex;justify-content:center;padding:28px 0;background:#eaeef8">' + f'<div class="phone">{S_HW}</div></div>',
                 "cta": "Открыть прототип", "go": "proto"},
        "facts": [("Клиент", "онлайн-школа «Тетрадь»"), ("Работа", "22 экрана, прототип, дизайн-система"),
                  ("Срок", "14 рабочих дней"), ("Платформы", "iOS и Android, макеты в Figma")],
        "sections": [
            {"type": "text3", "id": "task", "nav": "Задача", "kick": "Задача", "h2": "Ученик забывает, родитель не видит",
             "items": [("Ученики", "Пропускали дедлайны", "Домашка лежала в чате с учителем и терялась среди сообщений."),
                       ("Родители", "Звонили менеджеру", "Чтобы узнать оценки и сколько уроков осталось в абонементе. Десятки звонков в неделю."),
                       ("Учителя", "Проверяли в документах", "Комментарии к ошибкам писали отдельным сообщением, ученик не видел, где ошибся.")]},
            {"type": "html", "id": "proto", "nav": "Прототип", "kick": "Прототип", "h2": "Попробуйте сами", "alt": True, "html": PROTO},
            {"type": "html", "id": "screens", "nav": "Экраны", "kick": "Экраны", "h2": "Пять главных экранов из двадцати двух",
             "lead": "Листайте вбок. Клетка на фоне — фирменный элемент: экран выглядит как страница тетради.", "html": ROW},
            {"type": "palette", "id": "color", "nav": "Цвета", "kick": "Цвета", "h2": "Синяя ручка, красная ручка, маркер", "alt": True,
             "lead": "Цвета взяты из школьного пенала: каждый что-то значит. Нажмите, чтобы скопировать код.",
             "colors": [("Синяя ручка", PEN, "кнопки и выполненное"), ("Красная ручка", RED, "пометки учителя и ошибки"), ("Маркер", HL, "серия дней и важное"),
                        ("Бумага", PAPER, "фон экранов"), ("Клетка", GRID, "сетка и разделители"), ("Чернила", INK, "текст")]},
            {"type": "type", "id": "type", "kick": "Шрифты", "h2": "Интерфейс и почерк учителя",
             "fonts": [(FB, f"'{FB}'", "весь интерфейс", "Сложение дробей с разными знаменателями", "font-weight:700"),
                       (FN, f"'{FN}'", "только пометки учителя", "have — они, а не он", "color:#e0413a")]},
            {"type": "result", "id": "result", "nav": "Итог", "kick": "Итог", "h2": "Что получила школа",
             "stats": [("22", "экрана в макете"), ("2", "роли в одном приложении"), ("48", "компонентов дизайн-системы"), ("14 дней", "от брифа до прототипа")]},
        ],
        "ctaTitle": "Нужен дизайн приложения?",
        "js": JS,
    }
