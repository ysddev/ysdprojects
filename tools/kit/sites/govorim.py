"""«Говорим» — языковая школа для взрослых в Тюмени (английский и китайский): тест уровня из 6 вопросов с подбором
группы и расписания, форматы и цены, пробный урок."""

IMAGES = {
    "cafe": ("1572075304903-a2dd9c50b1cd", 5, 4, "600,1000,1400"),
    "group": ("1758873271687-ec6b5bc28fe8", 2, 1, "600,1000,1400"),
    "cups": ("1526547319484-63dce467060b", 3, 4, "300,600,900"),
    "notes": ("1630011041146-04d179c6e215", 3, 4, "300,600,900"),
    "table": ("1764391797723-45f40835667b", 3, 4, "300,600,900"),
    "book": ("1543109740-4bdb38fda756", 1, 1, "300,600"),
    "cards": ("1788247835203-6f2e9694ad14", 4, 3, "450,900,1300"),
}

TEST = r"""
<div class="lt rv">
 <div class="panel ltq" id="ltQ"></div>
 <div class="panel ltr" id="ltR" hidden></div>
</div>
"""

CSS = r"""
.hero h1 em{font-style:normal;color:var(--ac);display:inline-block;transform:rotate(-2deg)}
.hph{border-radius:30px 30px 120px 30px}
.lt{max-width:860px}
.ltq .pr{height:6px;border-radius:3px;background:var(--line);margin-bottom:22px}.ltq .pr i{display:block;height:100%;border-radius:3px;background:var(--ac);transition:width .3s}
.ltq .n{font-size:13.5px;color:var(--mut);margin-bottom:8px}
.ltq h3{font-size:clamp(22px,2.4vw,30px);margin-bottom:20px}
.ltq .ops{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ltq .ops button{padding:16px 18px;border-radius:16px;box-shadow:inset 0 0 0 1.5px var(--line2);text-align:left;font-size:16px;background:var(--bg);transition:box-shadow .2s,background .2s}
.ltq .ops button:hover{box-shadow:inset 0 0 0 1.5px var(--ac)}
.ltq .ops button.ok{background:#e4f7ea;box-shadow:inset 0 0 0 1.5px #2fa35b}.ltq .ops button.no{background:#fdecea;box-shadow:inset 0 0 0 1.5px #d6493b}
.ltq .lang{display:flex;gap:10px;margin-bottom:22px}
.ltr{display:grid;gap:16px}
.ltr .lv{display:flex;align-items:center;gap:16px}.ltr .lv b{font:700 64px/1 var(--fh);color:var(--ac)}.ltr .lv span{font-size:18px;font-weight:600}
.ltr .grp{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.ltr .grp button{padding:14px;border-radius:14px;box-shadow:inset 0 0 0 1.5px var(--line2);text-align:left;font-size:14.5px;line-height:1.4}
.ltr .grp button.on{box-shadow:inset 0 0 0 2px var(--ac);background:color-mix(in srgb,var(--ac) 8%,transparent)}
.ltr .grp b{display:block;font-size:16px}
.ltr .act{display:flex;gap:10px;flex-wrap:wrap}
.fmt{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.fmt article{border-radius:26px;padding:28px;display:flex;flex-direction:column;gap:12px}
.fmt article:nth-child(1){background:#ffe8d6}.fmt article:nth-child(2){background:#dff1ff}.fmt article:nth-child(3){background:#e9f6df}
.fmt h3{font-size:24px}.fmt p{color:var(--soft);font-size:15px}
.fmt .pp{margin-top:auto;font:700 30px var(--fh)}.fmt .pp small{font:400 14px var(--fb);color:var(--soft)}
.fmt ul{margin:0;padding-left:18px;color:var(--soft);font-size:15px;display:grid;gap:5px}
@media (max-width:860px){.ltq .ops,.ltr .grp,.fmt{grid-template-columns:1fr}}
"""

JS = r"""
(function(){var $=function(s){return document.getElementById(s)};
var Q={en:[['She ___ to work by bus every day.',['go','goes','is go','going'],1],['I have lived here ___ 2019.',['for','since','from','at'],1],
 ['If I ___ more time, I would learn Chinese.',['have','had','will have','would have'],1],['The report ___ by Friday.',['must finish','must be finished','must finished','must be finishing'],1],
 ['He denied ___ the window.',['to break','break','breaking','broke'],2],['Hardly ___ the meeting started when the lights went out.',['had','has','did','was'],0]],
 zh:[['你好 означает…',['спасибо','здравствуйте','до свидания','извините'],1],['Как сказать «я пью чай»?',['我喝茶','我吃茶','我看茶','我茶喝'],0],
 ['了 после глагола обычно показывает…',['вопрос','завершённость','отрицание','будущее'],1],['Какой тон в слове mā?',['первый','второй','третий','четвёртый'],0],
 ['我们 означает…',['я','ты','мы','они'],2],['因为…所以… — это конструкция…',['причины и следствия','сравнения','уступки','времени'],0]]};
var LV={en:[['A1','Начинающий','с нуля и «помню школу»'],['A2','Элементарный','бытовые темы, простое прошлое'],['B1','Средний','говорите о работе и путешествиях'],['B2','Выше среднего','обсуждаете новости, пишете письма'],['C1','Продвинутый','свободно, работаем над нюансами']],
 zh:[['HSK 1','Первые шаги','тоны и 150 слов'],['HSK 2','Базовый','300 слов, простые диалоги'],['HSK 3','Средний','600 слов, путешествия и работа'],['HSK 4','Уверенный','1 200 слов, свободный разговор'],['HSK 5','Продвинутый','новости и деловая переписка']]};
var G={0:[['Пн и Чт','19:00–20:30','3 места'],['Вт и Пт','08:00–09:30','5 мест'],['Сб','11:00–14:00','2 места']],1:[['Пн и Ср','19:30–21:00','4 места'],['Вт и Чт','12:30–14:00','6 мест'],['Сб','15:00–18:00','1 место']],
 2:[['Вт и Чт','19:00–20:30','2 места'],['Ср и Пт','08:00–09:30','4 места'],['Вс','11:00–14:00','3 места']],3:[['Пн и Ср','20:00–21:30','5 мест'],['Сб','10:00–13:00','2 места'],['онлайн Вт и Чт','21:00–22:30','6 мест']],
 4:[['Ср','19:00–21:00','3 места'],['онлайн Сб','12:00–14:00','4 места'],['индивидуально','любое время','по записи']]};
var lang='en',i=0,score=0,grp=0;
function q(){var Qs=Q[lang];if(i>=Qs.length)return res();var x=Qs[i];
 $('ltQ').innerHTML='<div class="lang seg" id="ltL"><button type="button" data-l="en" class="'+(lang=='en'?'on':'')+'">Английский</button><button type="button" data-l="zh" class="'+(lang=='zh'?'on':'')+'">Китайский</button></div>'
  +'<div class="pr"><i style="width:'+(i/Qs.length*100)+'%"></i></div><div class="n">Вопрос '+(i+1)+' из '+Qs.length+'</div><h3>'+x[0]+'</h3><div class="ops">'+x[1].map(function(o,k){return'<button type="button" data-k="'+k+'">'+o+'</button>'}).join('')+'</div>';}
$('ltQ').addEventListener('click',function(e){var l=e.target.closest('[data-l]');if(l){lang=l.dataset.l;i=0;score=0;q();return}
 var b=e.target.closest('[data-k]');if(!b||this.dataset.lock)return;var ok=+b.dataset.k===Q[lang][i][2];if(ok)score++;b.classList.add(ok?'ok':'no');
 if(!ok)this.querySelector('[data-k="'+Q[lang][i][2]+'"]').classList.add('ok');this.dataset.lock=1;var self=this;setTimeout(function(){delete self.dataset.lock;i++;q()},650)});
function res(){var lv=Math.min(4,score<=1?0:score==2?1:score==3?2:score==4||score==5?3:4),L=LV[lang][lv];$('ltQ').hidden=true;var r=$('ltR');r.hidden=false;grp=0;
 r.innerHTML='<span class="kick">Ваш результат · '+score+' из 6</span><div class="lv"><b>'+L[0]+'</b><span>'+L[1]+'<br><small style="font-weight:400;color:var(--mut)">'+L[2]+'</small></span></div>'
  +'<p style="color:var(--soft)">Подобрали группы вашего уровня — выберите удобное время. На пробном уроке преподаватель уточнит уровень устно.</p>'
  +'<div class="grp" id="ltG">'+G[lv].map(function(g,k){return'<button type="button" data-g="'+k+'" class="'+(k==0?'on':'')+'"><b>'+g[0]+'</b>'+g[1]+'<br><small style="color:var(--mut)">свободно: '+g[2]+'</small></button>'}).join('')+'</div>'
  +'<div class="act"><a class="btn" href="#lead" id="ltGo">Записаться на пробный урок</a><button class="btn g" type="button" id="ltAgain">Пройти заново</button></div>';
 $('ltG').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;grp=+b.dataset.g;[].forEach.call(this.children,function(x){x.classList.toggle('on',x===b)})});
 $('ltAgain').onclick=function(){i=0;score=0;r.hidden=true;$('ltQ').hidden=false;q()};
 $('ltGo').onclick=function(){var t=document.querySelector('#lead textarea');var g=G[lv][grp];if(t)t.value=(lang=='en'?'Английский':'Китайский')+', уровень '+L[0]+', группа: '+g[0]+' '+g[1]}}
q()})();
"""

FMT = ('<div class="fmt">' + "".join(
    f'<article class="rv"><h3>{h}</h3><p>{p}</p><ul>{"".join("<li>" + x + "</li>" for x in li)}</ul><div class="pp">{pr} <small>{u}</small></div></article>'
    for h, p, li, pr, u in [
        ("Группа", "6–8 человек одного уровня, два раза в неделю по 90 минут.", ["разговорный клуб по пятницам — бесплатно", "материалы входят в цену"], "7 400 ₽", "в месяц"),
        ("Индивидуально", "Программа под вашу цель: собеседование, переезд, экзамен.", ["время выбираете сами", "онлайн или в классе"], "1 950 ₽", "за 60 минут"),
        ("Интенсив", "Три недели каждый день перед поездкой или экзаменом.", ["15 занятий по 2 часа", "пробный экзамен в конце"], "23 900 ₽", "за курс")]) + "</div>")


def cfg() -> dict:
    return {
        "slug": "govorim", "brand": "Говорим", "legal": "Языковая школа «Говорим», Тюмень", "favLetter": "Г",
        "logo": '<svg viewBox="0 0 32 32"><path d="M4 7c0-2 1.6-3.5 3.5-3.5h17C26.4 3.5 28 5 28 7v12c0 2-1.6 3.5-3.5 3.5H14l-6.5 5v-5h0C5.6 22.5 4 21 4 19z" fill="#ff6b3d"/><circle cx="11" cy="13" r="1.8" fill="#fff"/><circle cx="16" cy="13" r="1.8" fill="#fff"/><circle cx="21" cy="13" r="1.8" fill="#fff"/></svg>',
        "title": "Говорим — английский и китайский для взрослых в Тюмени",
        "desc": "Языковая школа для взрослых в Тюмени: английский и китайский в группах и индивидуально. Тест уровня за 2 минуты, "
                "подбор группы и расписания, пробный урок бесплатно.",
        "theme": {"bg": "#fffaf3", "ink": "#1f1a17", "soft": "#57504a", "mut": "#9a9089", "line": "#f0e6d8", "line2": "#e3d5c2",
                  "card": "#ffffff", "alt": "#fff1e2", "ac": "#ff6b3d", "aci": "#ffffff", "fh": "Rubik,sans-serif", "fb": "Rubik,sans-serif",
                  "hw": "700", "ht": "-.02em", "dk": "#1f1a17", "dki": "#fff", "rc": "24px", "rb": "999px", "kls": ".1em"},
        "fonts": [("Rubik", "rubik", [400, 500, 600, 700], "normal")],
        "images": IMAGES,
        "phone": ("+73452000000", "+7 3452 00-00-00"),
        "mail": "hello@govorim.ysdprojects.space",
        "nav": [("test", "Тест уровня"), ("formats", "Форматы и цены"), ("method", "Как учим"), ("faq", "Вопросы")],
        "topCta": "Пробный урок",
        "hero": {"kicker": "Английский и китайский · для взрослых", "h1": "Через 3 месяца вы <em>заговорите</em>, а не просто «поймёте»",
                 "lead": "70% урока говорите вы, а не преподаватель. Группы по уровню, занятия утром, вечером и по выходным — в классе у "
                         "Цветного бульвара или онлайн.",
                 "cta": "Узнать свой уровень", "go": "test", "go2": ("formats", "Цены"),
                 "points": ["Пробный урок бесплатно", "Заморозка на время отпуска", "Возврат за непройденные занятия"],
                 "img": "cafe", "alt": "Занятие в языковой школе", "ar": "5/4",
                 "tag": "<b>1 184 выпускника</b>за 6 лет — от «помню школу» до собеседований на английском"},
        "sections": [
            {"type": "html", "id": "test", "kick": "Тест уровня", "h2": "Шесть вопросов — и мы подберём группу и время", "alt": True,
             "lead": "Неправильные ответы — это нормально: тест нужен, чтобы вы попали в группу своего уровня.", "html": TEST},
            {"type": "html", "id": "formats", "kick": "Форматы и цены", "h2": "Выберите, как вам удобнее учиться", "html": FMT},
            {"type": "steps", "id": "method", "kick": "Как учим", "h2": "Говорить с первого урока", "alt": True,
             "items": [("Разговор, а не правила", "Грамматику даём по ходу разговора, когда она нужна для фразы.", "70% урока — ваша речь"),
                       ("Жизненные темы", "Заказ в кафе, созвон с коллегой, жалоба в отеле — то, что пригодится.", "свои темы по запросу группы"),
                       ("Домашка за 15 минут", "Короткие задания в приложении: слова, аудио, одно голосовое.", "каждый день понемногу"),
                       ("Проверка уровня", "Раз в 2 месяца — устный тест и разбор с преподавателем.", "видно прогресс")]},
            {"type": "gallery", "id": "school", "kick": "Школа", "h2": "Классы на 8 человек и кофе на перемене",
             "items": [{"img": "group", "span": 8, "ar": "2/1", "alt": "Занятие в группе"}, {"img": "cups", "span": 4, "ar": "3/4", "alt": "Кофе на перемене"},
                       {"img": "notes", "span": 4, "ar": "3/4", "alt": "Конспекты"}, {"img": "cards", "span": 4, "ar": "3/4", "alt": "Карточки со словами"},
                       {"img": "table", "span": 4, "ar": "3/4", "alt": "Класс"}]},
            {"type": "faq", "id": "faq", "kick": "Вопросы", "h2": "Что спрашивают перед записью",
             "items": [("Я совсем ничего не помню. Мне можно?", "Да, у нас есть группы с нуля — и для английского, и для китайского. Половина студентов начинала так же."),
                       ("Что если пропущу занятие?", "Пришлём запись и задание. Можно прийти на тот же урок в параллельную группу."),
                       ("Можно ли вернуть деньги?", "Да, за непройденные занятия — в течение 5 рабочих дней. Пробный урок бесплатный."),
                       ("Кто преподаёт китайский?", "Два преподавателя из Китая и русскоязычный куратор, который объясняет грамматику по-русски.")]},
        ],
        "contact": {"kick": "Пробный урок", "h2": "Приходите на бесплатный пробный урок",
                    "lead": "45 минут в группе вашего уровня. После — расскажем, сколько времени уйдёт на вашу цель.",
                    "rows": [("Адрес", "Тюмень, ул. Республики, 14, 3 этаж"), ("Телефон", "+7 3452 00-00-00"), ("Часы", "Пн–пт 8:00–21:30, сб–вс 10:00–18:00")]},
        "form": {"fields": [("name", "Имя", "text", "", True), ("phone", "Телефон", "tel", "+7", True),
                            ("lang", "Язык", "select", ["Английский", "Китайский"]), ("goal", "Цель", "select", ["Путешествия", "Работа", "Переезд", "Экзамен", "Для себя"]),
                            ("msg", "Удобное время", "textarea", "Например: будни после 19:00")],
                 "ok": "Записали! Администратор позвонит, чтобы подтвердить время пробного урока.", "btn": "Записаться"},
        "css": CSS, "js": JS,
    }
