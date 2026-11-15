"""«Дарья Лён» — свадебный и семейный фотограф в Калининграде: портфолио с фильтром и просмотром на весь экран,
пакеты съёмки и свободные даты в календаре. Светлая плёночная эстетика, много воздуха."""

IMAGES = {
    "wed-walk": ("1525258706463-a8c77635beb1", 3, 2, "800,1400,2000"),
    "wed-window": ("1542764824-4cdbd6c92dbe", 3, 2, "600,1000,1600"),
    "wed-hands": ("1556302482-70b6e670e6b7", 3, 2, "600,1000,1600"),
    "fam-beach": ("1559561875-dbbdf3700044", 3, 2, "600,1000,1600"),
    "fam-field": ("1779590883480-b634324560d4", 3, 2, "600,1000,1600"),
    "fam-hands": ("1552819289-824d37ca69d2", 3, 2, "600,1000,1600"),
    "int-bedroom": ("1642204525589-978a8117a6e5", 2, 3, "600,1000,1600"),
    "int-window": ("1678511446570-5fc2f676e564", 4, 5, "600,1000,1600"),
    "obj-vases": ("1677761640321-b80251be00ca", 2, 3, "600,1000,1600"),
    "obj-amber": ("1701933810985-88288ca3e5d9", 3, 2, "600,1000,1600"),
    "land-fog": ("1525891618908-24765267dab7", 3, 2, "600,1000,1600"),
    "land-field": ("1527954513726-611b208be16a", 2, 3, "600,1000,1600"),
    "lens": ("1661702446411-c6579fe8ff03", 2, 3, "600,1000"),
}

WORKS = [("wed-window", "wed", "Утро невесты, Светлогорск", 3, 2), ("fam-beach", "fam", "Семья у моря, Зеленоградск", 3, 2),
         ("int-bedroom", "int", "Интерьер, апартаменты на Острове", 2, 3), ("wed-hands", "wed", "Регистрация в форте", 3, 2),
         ("land-field", "land", "Поле под Янтарным", 2, 3), ("fam-field", "fam", "Прогулка в июне", 3, 2),
         ("obj-vases", "obj", "Предметная съёмка для керамиста", 2, 3), ("wed-walk", "wed", "Свадебная прогулка", 3, 2),
         ("fam-hands", "fam", "Ожидание", 3, 2), ("int-window", "int", "Кухня в старом доме", 4, 5),
         ("obj-amber", "obj", "Янтарь для ювелира", 3, 2), ("land-fog", "land", "Туман над Куршской косой", 3, 2)]

PORT = r"""
<div class="pf"><div class="chips" id="pfF"><button type="button" data-f="all" class="on">Все</button><button type="button" data-f="wed">Свадьбы</button><button type="button" data-f="fam">Семьи</button><button type="button" data-f="int">Интерьеры</button><button type="button" data-f="obj">Предметы</button><button type="button" data-f="land">Пейзажи</button></div>
<span class="cnt" id="pfC"></span></div>
<div class="mas" id="mas">__ITEMS__</div>
<div class="lb" id="lb" hidden><button class="lx" type="button" id="lbX" aria-label="Закрыть">×</button><button class="lp" type="button" id="lbP" aria-label="Предыдущая">‹</button>
<figure><img id="lbI" alt=""><figcaption id="lbC"></figcaption></figure><button class="ln" type="button" id="lbN" aria-label="Следующая">›</button></div>
"""

BOOK = r"""
<div class="bk rv">
 <div class="pk" id="pk"></div>
 <div class="panel cal">
  <div class="ch"><button type="button" id="cP" aria-label="Предыдущий месяц">‹</button><b id="cM"></b><button type="button" id="cN" aria-label="Следующий месяц">›</button></div>
  <div class="cw"><span>пн</span><span>вт</span><span>ср</span><span>чт</span><span>пт</span><span>сб</span><span>вс</span></div>
  <div class="cd" id="cD"></div>
  <div class="cl"><span><i class="f"></i>свободно</span><span><i class="b"></i>занято</span></div>
  <div class="sum" id="bS">Выберите пакет и дату</div>
  <a class="btn" href="#lead" id="bGo">Забронировать дату</a>
 </div>
</div>
"""

CSS = r"""
.hero.full h1{font-weight:400;font-size:clamp(46px,7vw,104px);line-height:.98}
.hero.full h1 em{font-style:italic;color:#fff}
.hero.full .kick{color:#f4ece0}
.sh h2{font-weight:400}
.pf{display:flex;justify-content:space-between;align-items:center;gap:14px;flex-wrap:wrap;margin-bottom:22px}
.pf .cnt{color:var(--mut);font-size:14.5px}
.mas{columns:3 280px;column-gap:14px}
.mas figure{margin:0 0 14px;break-inside:avoid;position:relative;cursor:zoom-in;border-radius:4px;overflow:hidden;background:var(--card)}
.mas figure img{width:100%;height:auto;transition:transform .8s}
.mas figure:hover img{transform:scale(1.03)}
.mas figcaption{position:absolute;left:0;right:0;bottom:0;padding:30px 14px 12px;color:#fff;font-size:13.5px;background:linear-gradient(transparent,rgba(0,0,0,.5));opacity:0;transition:opacity .3s}
.mas figure:hover figcaption{opacity:1}
.mas figure.hide{display:none}
.lb{position:fixed;inset:0;z-index:70;background:rgba(20,17,14,.94);display:grid;place-items:center;padding:20px}
.lb figure{margin:0;max-width:min(1200px,100%);text-align:center}
.lb img{max-height:82vh;width:auto;margin:auto}
.lb figcaption{color:#e9e1d6;margin-top:12px;font:italic 400 18px var(--fh)}
.lb button{position:absolute;color:#fff;font-size:44px;line-height:1;width:56px;height:56px}
.lx{top:16px;right:16px}.lp{left:10px;top:50%;transform:translateY(-50%)}.ln{right:10px;top:50%;transform:translateY(-50%)}
.bk{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:clamp(14px,2vw,24px);align-items:start}
.pk{display:grid;gap:12px}
.pk button{display:grid;grid-template-columns:1fr auto;gap:4px 16px;text-align:left;padding:22px 24px;border-radius:4px;background:var(--card);box-shadow:inset 0 0 0 1px var(--line);transition:box-shadow .2s}
.pk button.on{box-shadow:inset 0 0 0 1.5px var(--ink)}
.pk b{font:400 26px var(--fh)}.pk em{font-style:normal;font:400 26px var(--fh);text-align:right}
.pk span{grid-column:1/-1;color:var(--soft);font-size:15px}
.cal{border-radius:4px}
.ch{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}.ch b{font:400 24px var(--fh);text-transform:capitalize}
.ch button{width:40px;height:40px;font-size:24px;border-radius:50%}.ch button:hover{background:var(--alt)}
.cw,.cd{display:grid;grid-template-columns:repeat(7,1fr);gap:4px;text-align:center}
.cw span{font-size:12.5px;color:var(--mut);padding:6px 0}
.cd button,.cd span{aspect-ratio:1;display:grid;place-items:center;border-radius:50%;font-size:14.5px}
.cd .f{box-shadow:inset 0 0 0 1px var(--line2)}.cd .f:hover{background:var(--alt)}
.cd .b{color:var(--mut);text-decoration:line-through;opacity:.55}
.cd .on{background:var(--ink)!important;color:var(--bg)}
.cl{display:flex;gap:18px;margin:12px 0 18px;font-size:13px;color:var(--mut)}.cl i{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px;vertical-align:-1px}
.cl .f{box-shadow:inset 0 0 0 1px var(--line2)}.cl .b{background:var(--line2)}
.sum{padding:14px 0;border-top:1px solid var(--line);margin-bottom:14px;font-size:15px}
.cal .btn{width:100%}
.quote{font:italic 400 clamp(26px,3.2vw,42px)/1.3 var(--fh);max-width:30ch;margin:0 auto;text-align:center;text-wrap:balance}
.quote small{display:block;font:400 14px var(--fb);color:var(--mut);margin-top:16px;font-style:normal}
@media (max-width:860px){.bk{grid-template-columns:1fr}}
"""

JS = r"""
(function(){var $=function(s){return document.getElementById(s)};
// фильтр и просмотр
var figs=[].slice.call(document.querySelectorAll('#mas figure'));
function filt(f){var n=0;figs.forEach(function(x){var on=f=='all'||x.dataset.f==f;x.classList.toggle('hide',!on);if(on)n++});$('pfC').textContent=n+' '+plural(n,'кадр','кадра','кадров')}
$('pfF').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;[].forEach.call(this.children,function(x){x.classList.toggle('on',x===b)});filt(b.dataset.f)});filt('all');
var cur=0;function vis(){return figs.filter(function(x){return!x.classList.contains('hide')})}
function show(i){var v=vis();cur=(i+v.length)%v.length;var im=v[cur].querySelector('img');$('lbI').src=im.currentSrc||im.src;$('lbI').alt=im.alt;$('lbC').textContent=im.alt;$('lb').hidden=false}
$('mas').addEventListener('click',function(e){var f=e.target.closest('figure');if(f)show(vis().indexOf(f))});
$('lbX').onclick=function(){$('lb').hidden=true};$('lbP').onclick=function(){show(cur-1)};$('lbN').onclick=function(){show(cur+1)};
$('lb').addEventListener('click',function(e){if(e.target===this)this.hidden=true});
document.addEventListener('keydown',function(e){if($('lb').hidden)return;if(e.key=='Escape')$('lb').hidden=true;if(e.key=='ArrowRight')show(cur+1);if(e.key=='ArrowLeft')show(cur-1)});
// пакеты и календарь
var PK=[['Прогулка',14500,'1,5 часа, 60 кадров в цвете, одна локация'],['Семейная история',23700,'3 часа дома и на улице, 140 кадров, фотокнига 20×20'],['Свадебный день',64900,'8 часов от сборов до первого танца, 450 кадров, превью через 3 дня']];
var pk=1,sel=null,base=new Date(2026,10,1),mo=0;
$('pk').innerHTML=PK.map(function(p,i){return'<button type="button" data-i="'+i+'" class="'+(i==pk?'on':'')+'"><b>'+p[0]+'</b><em>'+rub(p[1])+'</em><span>'+p[2]+'</span></button>'}).join('');
$('pk').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;pk=+b.dataset.i;[].forEach.call(this.children,function(x){x.classList.toggle('on',x===b)});sum()});
function busy(d){var k=d.getMonth()*31+d.getDate();return d.getDay()==6&&d.getDate()<20||[3,9,14,21,27,40,45,52,58,66,71].indexOf(k%73)>=0}
function cal(){var d=new Date(base.getFullYear(),base.getMonth()+mo,1);$('cM').textContent=d.toLocaleString('ru-RU',{month:'long',year:'numeric'});
 var off=(d.getDay()+6)%7,days=new Date(d.getFullYear(),d.getMonth()+1,0).getDate(),h='';for(var i=0;i<off;i++)h+='<span></span>';
 for(var x=1;x<=days;x++){var dt=new Date(d.getFullYear(),d.getMonth(),x),past=dt<new Date(2026,10,16),b=past||busy(dt),key=dt.toDateString();
  h+=b?'<span class="b">'+x+'</span>':'<button type="button" class="f'+(sel==key?' on':'')+'" data-k="'+key+'">'+x+'</button>'}
 $('cD').innerHTML=h;$('cP').disabled=mo<=0;$('cN').disabled=mo>=5}
$('cD').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;sel=b.dataset.k;cal();sum()});
$('cP').onclick=function(){if(mo>0){mo--;cal()}};$('cN').onclick=function(){if(mo<5){mo++;cal()}};
function sum(){var p=PK[pk];$('bS').innerHTML=sel?'<b>'+p[0]+'</b> · '+new Date(sel).toLocaleDateString('ru-RU',{day:'numeric',month:'long',weekday:'long'})+' · '+rub(p[1])+'<br><span style="color:var(--mut);font-size:13.5px">Бронь даты — предоплата '+rub(Math.round(p[1]*.3/100)*100)+', остальное в день съёмки</span>':'Выберите дату — свободные обведены'}
$('bGo').addEventListener('click',function(){var t=document.querySelector('#lead textarea');if(t&&sel)t.value=PK[pk][0]+', '+new Date(sel).toLocaleDateString('ru-RU')});
cal();sum()})();
"""


def cfg() -> dict:
    from ..common import img
    items = "".join(f'<figure data-f="{f}">{img(k, IMAGES, "(max-width:620px) 100vw, 33vw", cap)}<figcaption>{cap}</figcaption></figure>'
                    for k, f, cap, a, b in WORKS)
    return {
        "slug": "dlen", "brand": "Дарья Лён", "legal": "Дарья Лён, фотограф. Калининград", "favLetter": "Д",
        "title": "Дарья Лён — свадебный и семейный фотограф в Калининграде",
        "desc": "Свадебная, семейная и интерьерная съёмка в Калининграде и области. Портфолио, пакеты от 14 500 ₽, "
                "свободные даты в календаре, бронь с предоплатой 30%.",
        "theme": {"bg": "#f7f3ee", "ink": "#26211c", "soft": "#5c544b", "mut": "#958a7d", "line": "#e7ded2", "line2": "#d5c9b9",
                  "card": "#fffdf9", "alt": "#efe8de", "ac": "#26211c", "aci": "#f7f3ee", "fh": '"Cormorant Garamond",serif', "fb": "Jost,sans-serif",
                  "hw": "500", "ht": "-.01em", "rc": "4px", "rb": "2px", "kls": ".22em", "kc": "#958a7d",
                  "shade": "linear-gradient(180deg,rgba(20,16,12,.05) 30%,rgba(20,16,12,.55))"},
        "fonts": [("Cormorant Garamond", "cormorant-garamond", [400, 500, 600], "normal"), ("Cormorant", "cormorant", [400], "italic"),
                  ("Jost", "jost", [400, 500], "normal")],
        "images": IMAGES,
        "css": CSS.replace("italic 400 18px var(--fh)", 'italic 400 18px "Cormorant",serif').replace("font:italic 400 clamp(26px,3.2vw,42px)/1.3 var(--fh)", 'font:italic 400 clamp(26px,3.2vw,42px)/1.3 "Cormorant",serif')
               + '.hero.full h1 em{font-family:"Cormorant",serif}',
        "phone": ("+74012000000", "+7 4012 00-00-00"),
        "mail": "hello@dlen.ysdprojects.space",
        "nav": [("works", "Портфолио"), ("book", "Пакеты и даты"), ("about", "Обо мне"), ("faq", "Вопросы")],
        "topCta": "Забронировать дату",
        "hero": {"full": True, "img": "wed-walk", "alt": "Свадебная прогулка", "kicker": "Фотограф · Калининград и побережье",
                 "h1": "Снимаю так, чтобы <em>через двадцать лет</em> было что вспомнить",
                 "lead": "Свадьбы, семьи и дома. Без постановочных поз «посмотрите друг на друга» — просто вы, свет и Балтика.",
                 "cta": "Свободные даты", "go": "book", "go2": ("works", "Портфолио"),
                 "points": ["9 лет снимаю", "312 свадеб и семей", "Превью через 3 дня"]},
        "sections": [
            {"type": "html", "id": "works", "kick": "Портфолио", "h2": "Нажмите на кадр — откроется во весь экран",
             "html": PORT.replace("__ITEMS__", items)},
            {"type": "html", "id": "book", "kick": "Пакеты и даты", "h2": "Выберите съёмку и свободный день", "alt": True,
             "lead": "Даты на лето разбирают с января. Бронь — предоплата 30%, если съёмку переносите больше чем за 14 дней, деньги переходят на новую дату.", "html": BOOK},
            {"type": "html", "id": "about", "html": '<p class="quote rv">«Я не ставлю людей в позы. Я ищу свет и жду момент — а вы просто разговариваете, гуляете и обнимаетесь.»<small>Дарья Лён</small></p>'},
            {"type": "steps", "id": "how", "kick": "Как проходит", "h2": "От звонка до фотокниги", "alt": True,
             "items": [("Знакомство", "Созвон на 20 минут: какие вы, где снимаем, что важно не пропустить.", "бесплатно"),
                       ("Подготовка", "Пришлю подсказки по одежде и тайминг под свет — золотой час на побережье в июле в 21:40.", "за неделю"),
                       ("Съёмка", "Без жёстких поз: подсказываю, где встать, и жду живые моменты.", "в день съёмки"),
                       ("Кадры", "Превью — через 3 дня, вся съёмка в галерее — через 3 недели. Книга — ещё через 10 дней.", "до 31 дня")]},
            {"type": "faq", "id": "faq", "kick": "Вопросы", "h2": "Что спрашивают перед бронью",
             "items": [("Можно ли выехать за пределы Калининграда?", "Да, по всей области без доплаты. В другие города — по дороге и проживанию."),
                       ("Сколько кадров вы отдаёте?", "Все удачные — в цвете с авторской обработкой. Число в пакете — минимум, обычно получается больше."),
                       ("А если будет дождь?", "Снимем в доме, в кафе или под зонтами — дождливые кадры часто самые тёплые. Или перенесём дату без доплаты."),
                       ("Можно ли купить ретушь отдельно?", "Да: глубокая ретушь — 900 ₽ за кадр, обычная обработка уже входит.")]},
        ],
        "contact": {"kick": "Связаться", "h2": "Напишите — расскажу, какие даты ещё свободны",
                    "lead": "Отвечаю в течение дня. Если дата занята, предложу коллегу со схожим стилем.",
                    "rows": [("Город", "Калининград и побережье"), ("Телефон", "+7 4012 00-00-00"), ("Отвечаю", "ежедневно, 10:00–21:00")]},
        "form": {"fields": [("name", "Имя", "text", "", True), ("phone", "Телефон или мессенджер", "text", "", True),
                            ("kind", "Съёмка", "select", ["Свадьба", "Семейная", "Интерьер", "Предметная"]), ("date", "Желаемая дата", "date", ""),
                            ("msg", "Пара слов о вас", "textarea", "Где хотите снимать, сколько вас")],
                 "ok": "Спасибо! Отвечу в течение дня и пришлю свободные даты.", "btn": "Отправить", "pairs": True},
        "css_extra": "",
        "js": JS,
    }
