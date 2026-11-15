"""«Тропа» — авторские походы и джип-туры по Алтаю из Барнаула: подбор тура по месяцу, сложности и длительности,
места в группе, расчёт брони, что взять с собой."""

IMAGES = {
    "hero": ("1717506638083-d0f97fa52904", 16, 9, "800,1400,2000"),
    "lake": ("1673335055461-d39091a6533e", 3, 2, "600,1000"),
    "field": ("1619426288206-e678b4d09d2d", 3, 2, "600,1000"),
    "flowers": ("1619426186551-ecd958d08277", 3, 2, "600,1000"),
    "forest": ("1708173606478-2d3653033b77", 3, 2, "600,1000"),
    "peaks": ("1717506682221-9f8f384ae620", 3, 2, "600,1000"),
    "fire": ("1486679679458-629f321a617c", 3, 2, "600,1000"),
    "camp": ("1573111651692-39ec7f38fec9", 3, 2, "600,1000"),
    "tent": ("1618342965414-eef8c97dbcc9", 4, 5, "600,1000"),
    "valley": ("1717505833620-58ef0db8a67d", 3, 2, "600,1000"),
}

TOURS = [
    {"id": "kat", "n": "Катунь и Чемальские пороги", "img": "lake", "d": 4, "lvl": 1, "m": [5, 6, 7, 8, 9], "p": 27900, "left": 6,
     "s": "Лёгкий маршрут для первого похода: тропы вдоль Катуни, сплав на рафтах, баня на берегу."},
    {"id": "ukok", "n": "Плато Укок", "img": "field", "d": 8, "lvl": 2, "m": [6, 7, 8], "p": 74500, "left": 3,
     "s": "Джип-тур на высокогорное плато к границе четырёх стран. Ночёвки в юртах, звёздное небо без засветки."},
    {"id": "aktru", "n": "Ледники Актру", "img": "peaks", "d": 7, "lvl": 3, "m": [7, 8], "p": 58900, "left": 2,
     "s": "Пеший поход к леднику и Голубому озеру. Набор высоты до 3 100 м, нужна хорошая выносливость."},
    {"id": "tel", "n": "Телецкое озеро", "img": "forest", "d": 5, "lvl": 1, "m": [5, 6, 7, 8, 9, 10], "p": 36400, "left": 8,
     "s": "Катер до водопада Корбу, кедровый лес, рыбалка. Подходит для отдыха с детьми от 8 лет."},
    {"id": "mult", "n": "Мультинские озёра", "img": "valley", "d": 6, "lvl": 2, "m": [7, 8, 9], "p": 49800, "left": 5,
     "s": "Каскад озёр с водой цвета бирюзы. Пеший маршрут, рюкзаки везут лошади."},
    {"id": "winter", "n": "Зимний Алтай и Чуйский тракт", "img": "flowers", "d": 5, "lvl": 1, "m": [1, 2, 3, 11, 12], "p": 42300, "left": 7,
     "s": "Замёрзшие водопады, петроглифы, баня и горячие источники. Едем на внедорожниках."},
]

FIND = r"""
<div class="tf rv">
 <div class="row"><b>Когда</b><div class="chips" id="fM"></div></div>
 <div class="row"><b>Сложность</b><div class="chips" id="fL"><button type="button" data-v="0" class="on">Любая</button><button type="button" data-v="1">Лёгкий</button><button type="button" data-v="2">Средний</button><button type="button" data-v="3">Сложный</button></div></div>
 <div class="row rng"><div class="rh"><span>Не дольше</span><b id="fDv">8 дней</b></div><input type="range" id="fD" min="3" max="8" value="8"></div>
</div>
<div class="tours" id="tourList"></div>
<div class="bk panel rv" id="bk" hidden>
 <div><span class="kick" id="bkM"></span><h3 id="bkN"></h3></div>
 <div class="pp"><span>Участников</span><div class="st"><button type="button" id="bm">−</button><b id="bq">2</b><button type="button" id="bp">+</button></div></div>
 <div class="tot" id="bT"></div>
 <a class="btn" href="#lead" id="bGo">Забронировать места</a>
</div>
"""

CSS = r"""
.hero.full h1{font-size:clamp(46px,7vw,100px);line-height:.95}
.hero.full h1 em{font-style:italic;color:#ffd38a}
.tf{display:grid;gap:16px;margin-bottom:26px;padding:22px;border-radius:var(--rc);background:var(--card);box-shadow:0 0 0 1px var(--line)}
.tf .row{display:grid;grid-template-columns:120px minmax(0,1fr);align-items:center;gap:16px}.tf .row>b{font-weight:600}
.tf .rng{grid-template-columns:120px minmax(0,1fr)}.tf .rng .rh{grid-column:1/-1}
.tours{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.tour{border-radius:var(--rc);overflow:hidden;background:var(--card);box-shadow:0 0 0 1px var(--line);display:flex;flex-direction:column}
.tour .ph{aspect-ratio:3/2;overflow:hidden;position:relative}.tour .ph img{width:100%;height:100%;object-fit:cover}
.tour .lv{position:absolute;left:12px;top:12px;background:rgba(255,255,255,.92);border-radius:99px;padding:5px 11px;font-size:13px;font-weight:600}
.tour .bd{padding:20px;display:flex;flex-direction:column;gap:10px;flex:1}
.tour h3{font-size:22px}.tour p{color:var(--soft);font-size:15px}
.tour .meta{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:13.5px;color:var(--mut)}
.tour .ft{margin-top:auto;display:flex;justify-content:space-between;align-items:center;gap:10px;padding-top:12px;border-top:1px solid var(--line)}
.tour .ft b{font:700 22px var(--fh)}.tour .ft small{display:block;font-size:12.5px;color:var(--ac2)}
.tour .ft button{padding:10px 16px;border-radius:var(--rb);background:var(--ac);color:var(--aci);font-weight:600;font-size:14.5px}
.tour.on{box-shadow:0 0 0 2px var(--ac)}
.empty{grid-column:1/-1;padding:30px;text-align:center;color:var(--soft)}
.bk{margin-top:18px;display:grid;grid-template-columns:minmax(0,1.4fr) auto minmax(0,1fr) auto;gap:20px;align-items:center}
.bk h3{font-size:24px;margin-top:6px}
.st{display:flex;align-items:center;gap:14px;margin-top:6px}.st button{width:40px;height:40px;border-radius:50%;box-shadow:inset 0 0 0 1.5px var(--line2);font-size:20px}.st b{font-size:20px;min-width:24px;text-align:center}
.pp span{font-size:13.5px;color:var(--mut)}
.tot{font-size:15px;color:var(--soft)}.tot b{display:block;font:700 26px var(--fh);color:var(--ink)}
.kit{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.kit label{display:flex;gap:10px;align-items:flex-start;padding:14px;border-radius:12px;background:rgba(255,255,255,.06);cursor:pointer;font-size:15px}
.kit input{accent-color:#ffd38a;margin-top:3px}
.kit label:has(input:checked){text-decoration:line-through;opacity:.6}
.kitp{margin-top:16px;color:rgba(255,255,255,.7);font-size:14.5px}
@media (max-width:980px){.tours{grid-template-columns:1fr 1fr}.bk{grid-template-columns:1fr 1fr}.kit{grid-template-columns:1fr 1fr}}
@media (max-width:620px){.tours,.kit{grid-template-columns:1fr}.bk{grid-template-columns:1fr}.tf .row{grid-template-columns:1fr}}
"""

JS = r"""
(function(){var $=function(s){return document.getElementById(s)};var T=window.SITE.tours,IMG=window.SITE.img;
var MN=['янв','фев','мар','апр','май','июн','июл','авг','сен','окт','ноя','дек'],LV=['','Лёгкий','Средний','Сложный'];
var m=0,lv=0,dmax=8,cur=null,q=2;
$('fM').innerHTML='<button type="button" data-v="0" class="on">Любой месяц</button>'+[5,6,7,8,9,1,2].map(function(x){return'<button type="button" data-v="'+x+'">'+MN[x-1]+'</button>'}).join('');
function seg(id,cb){$(id).addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;[].forEach.call(this.children,function(x){x.classList.toggle('on',x===b)});cb(+b.dataset.v);list()})}
seg('fM',function(v){m=v});seg('fL',function(v){lv=v});$('fD').addEventListener('input',function(){dmax=+this.value;$('fDv').textContent=dmax+' '+plural(dmax,'дня','дней','дней');list()});
function list(){var r=T.filter(function(t){return(!m||t.m.indexOf(m)>=0)&&(!lv||t.lvl==lv)&&t.d<=dmax});
 $('tourList').innerHTML=r.length?r.map(function(t){return'<article class="tour'+(cur&&cur.id==t.id?' on':'')+'"><div class="ph">'+IMG[t.id]+'<span class="lv">'+LV[t.lvl]+'</span></div><div class="bd"><h3>'+t.n+'</h3><div class="meta"><span>'+t.d+' '+plural(t.d,'день','дня','дней')+'</span><span>'+t.m.map(function(x){return MN[x-1]}).join(', ')+'</span></div><p>'+t.s+'</p>'
  +'<div class="ft"><div><b>'+rub(t.p)+'</b><small>осталось '+t.left+' '+plural(t.left,'место','места','мест')+'</small></div><button type="button" data-id="'+t.id+'">Выбрать</button></div></div></article>'}).join('')
  :'<div class="empty">Под такие условия туров нет — попробуйте другой месяц или напишите нам: соберём индивидуальный маршрут.</div>'}
$('tourList').addEventListener('click',function(e){var b=e.target.closest('[data-id]');if(!b)return;cur=T.filter(function(t){return t.id==b.dataset.id})[0];q=Math.min(q,cur.left);list();bk();$('bk').scrollIntoView({behavior:'smooth',block:'center'})});
function bk(){if(!cur)return;$('bk').hidden=false;$('bkM').textContent=cur.d+' '+plural(cur.d,'день','дня','дней')+' · '+LV[cur.lvl];$('bkN').textContent=cur.n;$('bq').textContent=q;
 var tot=cur.p*q,dep=Math.round(tot*.2/100)*100;$('bT').innerHTML='<b>'+rub(tot)+'</b>предоплата '+rub(dep)+', остальное — за 10 дней до старта'}
$('bm').onclick=function(){if(q>1){q--;bk()}};$('bp').onclick=function(){if(cur&&q<cur.left){q++;bk()}else toast('В группе больше нет мест')};
$('bGo').addEventListener('click',function(){var t=document.querySelector('#lead textarea');if(t&&cur)t.value=cur.n+', участников: '+q});
list()})();
"""

KIT = ('<div class="kit">' + "".join(f'<label class="rv"><input type="checkbox"><span>{x}</span></label>' for x in [
    "Трекинговые ботинки, разношенные", "Мембранная куртка и штаны", "Флиска и термобельё", "Шапка и перчатки — даже в июле",
    "Налобный фонарь", "Солнцезащитный крем и очки", "Личная аптечка", "Паспорт — нужен пропуск в погранзону"]) + "</div>"
       '<p class="kitp">Палатки, спальники, коврики, котлы и еду везём мы. Отмечайте, что уже собрали, — список останется на этой странице до обновления.</p>')


def cfg() -> dict:
    from ..common import img
    imgs = {t["id"]: img(t["img"], IMAGES, "(max-width:620px) 100vw, 33vw", t["n"]) for t in TOURS}
    return {
        "slug": "tropa", "brand": "Тропа", "legal": "ООО «Тропа», Барнаул", "favLetter": "Т",
        "logo": '<svg viewBox="0 0 32 32"><path d="M2 26l9-14 5 7 4-5 10 12z" fill="#2f5b3a"/><path d="M10 26c3-4 7-6 13-7" fill="none" stroke="#ffd38a" stroke-width="2" stroke-linecap="round" stroke-dasharray="2 3"/></svg>',
        "title": "Тропа — авторские походы и джип-туры по Алтаю",
        "desc": "Походы и джип-туры по Алтаю из Барнаула: Катунь, Укок, Актру, Телецкое озеро. Подбор тура по месяцу и сложности, "
                "группы до 12 человек, предоплата 20%.",
        "theme": {"bg": "#f5f3ee", "ink": "#1c2a20", "soft": "#4d5a50", "mut": "#86918a", "line": "#e2e0d6", "line2": "#cfcbbd",
                  "card": "#ffffff", "alt": "#ebe8de", "ac": "#2f5b3a", "aci": "#ffffff", "ac2": "#c0602c", "fh": "Bitter,serif",
                  "fb": '"Fira Sans",sans-serif', "hw": "700", "ht": "-.02em", "dk": "#1c2a20", "dki": "#f5f3ee", "rc": "16px", "rb": "10px",
                  "shade": "linear-gradient(180deg,rgba(10,20,14,.18) 15%,rgba(10,20,14,.55) 48%,rgba(10,20,14,.78))"},
        "fonts": [("Bitter", "bitter", [600, 700], "normal"), ("Fira Sans", "fira-sans", [400, 600], "normal")],
        "images": IMAGES,
        "phone": ("+73852000000", "+7 3852 00-00-00"),
        "mail": "go@tropa.ysdprojects.space",
        "nav": [("tours", "Туры"), ("how", "Как едем"), ("kit", "Что взять"), ("faq", "Вопросы")],
        "topCta": "Подобрать тур",
        "data": {"tours": TOURS, "img": imgs},
        "hero": {"full": True, "img": "hero", "alt": "Горы Алтая", "kicker": "Авторские туры по Алтаю · из Барнаула",
                 "h1": "Алтай, который <em>не видно</em> из окна автобуса",
                 "lead": "Пешие походы и джип-туры малыми группами до 12 человек. Ведут гиды, которые выросли в этих горах.",
                 "cta": "Подобрать тур", "go": "tours", "go2": ("how", "Как всё устроено"),
                 "points": ["11 сезонов", "4 812 туристов", "Ни одного отменённого тура из-за нас"]},
        "sections": [
            {"type": "html", "id": "tours", "kick": "Туры сезона", "h2": "Подберите маршрут под себя",
             "lead": "Выберите месяц, сложность и сколько дней готовы провести в горах — покажем подходящие туры и свободные места.", "html": FIND},
            {"type": "steps", "id": "how", "kick": "Как едем", "h2": "Встретим в Барнауле — дальше всё на нас", "alt": True,
             "items": [("Встреча", "Забираем из аэропорта или с вокзала Барнаула в день старта.", "до 10:00"),
                       ("Дорога", "Едем по Чуйскому тракту с остановками у смотровых и водопадов.", "6–9 часов"),
                       ("Маршрут", "Гид, повар и снаряжение. Каждый вечер — горячий ужин и баня там, где она есть.", "по программе"),
                       ("Возвращение", "Привозим в Барнаул к вечернему рейсу или поезду.", "до 18:00")]},
            {"type": "gallery", "id": "gal", "kick": "Фото с маршрутов", "h2": "Так выглядит ваш отпуск",
             "items": [{"img": "fire", "span": 7, "ar": "16/10", "alt": "Вечер у костра"}, {"img": "tent", "span": 5, "ar": "4/5", "alt": "Лагерь"},
                       {"img": "camp", "span": 4, "ar": "3/2", "alt": "Стоянка у озера"}, {"img": "flowers", "span": 4, "ar": "3/2", "alt": "Цветущая долина"},
                       {"img": "lake", "span": 4, "ar": "3/2", "alt": "Озеро"}]},
            {"type": "html", "id": "kit", "dark": True, "kick": "Что взять", "h2": "Список вещей — отмечайте, что уже собрали", "html": KIT},
            {"type": "faq", "id": "faq", "kick": "Вопросы", "h2": "Что спрашивают перед первым походом",
             "items": [("Я ни разу не ходил в походы. Мне можно?", "Да, туры с отметкой «Лёгкий» — для новичков: переходы до 12 км в день без тяжёлого рюкзака."),
                       ("Что если пойдёт дождь?", "Маршрут не отменяем: у нас тенты, сменная одежда сушится у костра. При опасной погоде гид меняет маршрут."),
                       ("Можно ли вернуть предоплату?", "Да, полностью — при отмене за 30 дней до старта. Позже — переносим на любой тур сезона."),
                       ("Нужен ли пропуск в погранзону?", "Для Укока и Чуйского тракта — да. Оформляем сами, нужны только паспортные данные за 30 дней.")]},
        ],
        "contact": {"kick": "Бронирование", "h2": "Оставьте заявку — придержим места на сутки",
                    "lead": "Менеджер ответит в течение часа, пришлёт программу по дням и реквизиты для предоплаты.",
                    "rows": [("Офис", "Барнаул, пр. Ленина, 61"), ("Телефон", "+7 3852 00-00-00"), ("Сезон", "май – октябрь и зимние туры")]},
        "form": {"fields": [("name", "Имя", "text", "", True), ("phone", "Телефон", "tel", "+7", True),
                            ("people", "Сколько вас", "select", ["1", "2", "3–4", "5 и больше"]), ("month", "Когда", "select", ["Май", "Июнь", "Июль", "Август", "Сентябрь", "Зима"]),
                            ("msg", "Комментарий", "textarea", "Какой тур выбрали, есть ли дети")],
                 "ok": "Придержали места на сутки. Менеджер пришлёт программу и реквизиты в течение часа.", "btn": "Забронировать"},
        "css": CSS, "js": JS,
    }
