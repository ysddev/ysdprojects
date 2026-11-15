"""«Вера Ланская» — экспериментальный сайт-портфолио арт-директора: имя меняет начертания, проекты — стопка листов,
которые выдвигаются и раскрываются, маленькая дизайн-игра с перетаскиванием, хронология. Монохром, бумага и графит."""

PROJECTS = [
    {"n": "Утренний хлеб", "y": "2026", "k": "Айдентика пекарни", "art": "disc", "w": "Утро · хлеб · мёд",
     "d": "Знак-печать для штампа на крафте, три шрифта под три времени суток и пакет, на котором не нужна этикетка: "
          "надпись выдавлена прямо в бумаге. Работа на 6 недель, 41 носитель."},
    {"n": "Коломенский свет", "y": "2025", "k": "Плакаты фестиваля", "art": "poster", "w": "КОРОТКИЙ МЕТР",
     "d": "Серия из 9 плакатов фестиваля короткого метра. Каждый плакат — кадр, растянутый по вертикали в 14 раз: "
          "свет проектора вместо картинки. Тираж 300 экземпляров на сером картоне."},
    {"n": "Сад камней", "y": "2025", "k": "Упаковка чая", "art": "box", "w": "сад камней",
     "d": "Пять сортов — пять рисунков граблями по песку, нарисованных одной линией. Коробка открывается как книга, "
          "внутри — короткое стихотворение про сорт."},
    {"n": "Тихий час", "y": "2024", "k": "Каталог мебельной мастерской", "art": "book", "w": "Тихий час",
     "d": "Каталог на 112 страниц: мебель снята в комнатах, где живут люди, а не в студии. Текст набран так, чтобы его "
          "можно было читать вслух — с паузами."},
    {"n": "Лён и соль", "y": "2024", "k": "Бренд-платформа косметики", "art": "rings", "w": "лён · соль · вода",
     "d": "Платформа бренда, тон голоса и система упаковки из трёх материалов. Логотип написан от руки и пересобран "
          "в 4 начертания — для флакона, коробки, сайта и витрины."},
    {"n": "Частота", "y": "2026", "k": "ИИ-визуалы для лейбла", "art": "wave", "w": "ЧАСТОТА 88,3",
     "d": "Обложки синглов, собранные из сгенерированных фактур и живого набора. Для каждого релиза — своя частота "
          "волны, рассчитанная из темпа трека."},
    {"n": "Архив мод", "y": "2023", "k": "Независимый журнал", "art": "spread", "w": "Архив мод № 3",
     "d": "Журнал об одежде, которую носили 30 лет. Три номера, сетка из 7 колонок и правило: ни одной фотографии "
          "без подписи владельца вещи."},
    {"n": "Сквозняк", "y": "2023", "k": "Айдентика галереи", "art": "grid", "w": "СКВОЗНЯК",
     "d": "Галерея в бывшей котельной. Буквы логотипа «продувает» насквозь — на афишах они смещаются от выставки к "
          "выставке, как от сквозняка."},
]

HTML = r"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Вера Ланская — графический дизайнер и арт-директор</title>
<meta name="description" content="Вера Ланская — графический дизайнер и арт-директор. Айдентика, упаковка, издательский дизайн, ИИ-визуалы. Избранные работы 2023–2026.">
<meta property="og:title" content="Вера Ланская — портфолио">
<meta property="og:description" content="Айдентика, упаковка, издательский дизайн. Избранные работы 2023–2026.">
<meta name="theme-color" content="#eeece8">
<link rel="icon" href="{FAVICON}">
<style>
/*FONTS*/
:root{--paper:#eeece8;--paper2:#e6e3dd;--ink:#2d2c2a;--soft:#5d5a55;--mut:#8f8b84;--line:#cfcac1;--sheet:#f6f5f2;
--scr:"Great Vibes",cursive;--srf:"Cormorant",serif;--cap:"Forum",serif;--sans:"Inter Tight",system-ui,sans-serif}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;overflow-x:clip}
body{margin:0;background:var(--paper);color:var(--ink);font:400 14px/1.45 var(--sans);-webkit-font-smoothing:antialiased;overflow-x:clip}
button{font:inherit;color:inherit;background:none;border:0;padding:0;cursor:pointer}
a{color:inherit}
img,svg{display:block;max-width:100%}
:focus-visible{outline:1px dashed var(--ink);outline-offset:4px}
.page{display:grid;grid-template-columns:minmax(0,44fr) minmax(0,30fr) minmax(0,26fr);min-height:100vh}
.l{border-right:1px solid var(--line);text-align:center;padding:30px 0 60px}
.yr{font:400 14px var(--sans);letter-spacing:.55em;color:var(--soft)}
.yr .cp{letter-spacing:0;margin-right:.7em;font-size:17px}
.name{height:clamp(130px,13vw,190px);display:grid;place-items:center;margin:16px auto 2px;cursor:pointer;user-select:none;width:min(560px,92%)}
.name span{grid-area:1/1;transition:opacity .45s,filter .45s;opacity:0;filter:blur(6px);color:var(--soft);line-height:.92}
.name span.on{opacity:1;filter:none}
.name .v1{font:400 clamp(52px,5.6vw,84px) var(--scr)}
.name .v2{font:400 clamp(46px,5vw,76px) var(--cap);text-transform:uppercase;letter-spacing:.02em}
.name .v3{font:italic 500 clamp(54px,6vw,88px) var(--srf);color:transparent;-webkit-text-stroke:1px var(--soft)}
.name .v4{font:400 clamp(56px,6vw,90px) "Marck Script",cursive;transform:rotate(-4deg)}
.role{font:italic 500 21px var(--srf);color:var(--soft)}
.role b{font-weight:500;margin:0 .4em}
.lab{font:italic 500 18px var(--srf);color:var(--soft);margin:58px 0 12px}
.rule{border-top:1px solid var(--line)}
.list{display:flex;flex-wrap:wrap;justify-content:center;gap:6px 38px;padding:22px 7% 0;font:400 clamp(20px,1.6vw,25px)/1.25 var(--cap);text-transform:uppercase;color:var(--soft)}
.list sup{font:italic 400 12px var(--srf);margin-right:4px;vertical-align:10px}
.list button{text-transform:uppercase;transition:color .2s}
.list button:hover,.list button.on{color:var(--ink);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:5px}
.about{max-width:440px;margin:22px auto 0;color:var(--soft);font-size:14.5px}
.about a{text-underline-offset:3px}
.cl{height:78px;overflow:hidden;position:relative}
.cl .list{position:absolute;inset:0;transition:transform .8s cubic-bezier(.6,0,.2,1),opacity .8s}
.c{display:grid;gap:4px;margin-top:22px;font-size:14.5px;color:var(--soft)}
.c a{text-decoration:none}.c a:hover{text-decoration:underline}
.m{border-right:1px solid var(--line);text-align:center;padding:30px 20px 60px;position:relative}
.m .yr2{font:400 14px var(--sans);letter-spacing:.55em;color:var(--soft);display:flex;align-items:center;justify-content:center;gap:16px}
.m .yr2 i{display:block;width:44px;border-top:1px solid var(--soft)}
.sel{margin:96px 0 40px;font-size:15px;line-height:1.15;color:var(--soft)}
.objs{display:grid;gap:22px;justify-items:center}
.obj{width:min(220px,64%);aspect-ratio:1;transition:transform .6s cubic-bezier(.2,.8,.2,1)}
.obj:hover{transform:rotate(-12deg) scale(1.04)}
.hint{margin-top:34px;font:italic 500 16px var(--srf);color:var(--mut)}
.r{position:relative;padding:18px 0 0}
.deck{position:sticky;top:0;height:100vh;display:flex;justify-content:flex-end;padding-right:8px}
.sh{position:relative;height:calc(100% - 24px);margin-top:12px;width:34px;flex:none;background:var(--sheet);box-shadow:-1px 0 0 var(--line),-6px 0 14px -10px rgba(0,0,0,.25);
 transition:transform .45s cubic-bezier(.2,.8,.2,1),background .3s;cursor:pointer;margin-left:-3px}
.sh:hover,.sh:focus-visible{transform:translateX(-26px);background:#fff}
.sh span{position:absolute;top:22px;left:50%;writing-mode:vertical-rl;transform:translateX(-50%) rotate(180deg);font:400 13.5px var(--sans);letter-spacing:.06em;color:var(--soft);white-space:nowrap}
.sh small{position:absolute;bottom:20px;left:50%;transform:translateX(-50%);writing-mode:vertical-rl;font:italic 500 15px var(--srf);color:var(--mut)}
.sh.top{width:auto;flex:1;max-width:330px;cursor:default;padding:26px 22px;background:#fff;margin-left:0}
.sh.top:hover{transform:none}
.sh.top h3{font:400 30px/1 var(--scr);color:var(--soft);margin:0 0 12px}
.sh.top p{font-size:13.5px;color:var(--soft);margin:0}
.sh.top ol{list-style:none;padding:0;margin:18px 0 0;display:grid;gap:0;border-top:1px solid var(--line)}
.sh.top li{display:flex;justify-content:space-between;gap:10px;padding:9px 0;border-bottom:1px solid var(--line);font-size:13.5px}
.sh.top li button{text-align:left}.sh.top li button:hover{text-decoration:underline}
.sh.top li em{font:italic 500 15px var(--srf);color:var(--mut)}
.ov{position:fixed;inset:0;z-index:40;pointer-events:none;visibility:hidden;transition:visibility 0s .6s}
.ov .bg{position:absolute;inset:0;background:rgba(45,44,42,.18);opacity:0;transition:opacity .4s}
.ov .pane{position:absolute;top:0;right:0;bottom:0;width:min(780px,100%);background:#fff;box-shadow:-30px 0 60px -30px rgba(0,0,0,.35);transform:translateX(102%);transition:transform .6s cubic-bezier(.2,.8,.2,1);overflow:auto;padding:38px clamp(22px,4vw,56px) 60px}
.ov.on{pointer-events:auto;visibility:visible;transition:none}.ov.on .bg{opacity:1}.ov.on .pane{transform:none}
.pane .x{position:absolute;top:22px;right:24px;font:italic 500 18px var(--srf);color:var(--mut)}
.pane .x:hover{color:var(--ink)}
.pane .no{font:400 13px var(--sans);letter-spacing:.5em;color:var(--mut)}
.pane h2{font:400 clamp(54px,7vw,86px)/.95 var(--scr);color:var(--ink);margin:26px 0 6px;font-weight:400}
.pane .k{font:italic 500 20px var(--srf);color:var(--soft)}
.pane .art{margin:30px 0;background:var(--paper);aspect-ratio:4/3;display:grid;place-items:center;overflow:hidden}
.pane .art svg{width:100%;height:100%}
.pane p{font-size:15.5px;color:var(--soft);max-width:56ch;line-height:1.6}
.pane .nav{display:flex;justify-content:space-between;margin-top:34px;padding-top:16px;border-top:1px solid var(--line);font:italic 500 17px var(--srf);color:var(--soft)}
.pane .nav button:hover{color:var(--ink)}
.game{border-top:1px solid var(--line);padding:70px 0 0;text-align:center}
.game h2{font:400 clamp(44px,5vw,70px) var(--scr);font-weight:400;color:var(--soft);margin:0}
.game .sub{font:italic 500 19px var(--srf);color:var(--soft);margin-top:6px}
.game .tools{display:flex;gap:26px;justify-content:center;margin:20px 0 0;font:italic 500 17px var(--srf);color:var(--mut)}
.game .tools button:hover{color:var(--ink);text-decoration:underline;text-underline-offset:4px}
.board{position:relative;height:clamp(420px,52vw,620px);margin-top:28px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);overflow:hidden;touch-action:pan-y;
 background-image:radial-gradient(circle,rgba(45,44,42,.16) 1px,transparent 1.2px);background-size:24px 24px}
.it{position:absolute;left:0;top:0;cursor:grab;user-select:none;-webkit-user-select:none;touch-action:none;color:var(--soft);transition:filter .2s}
.it.dr{cursor:grabbing;filter:drop-shadow(0 12px 14px rgba(0,0,0,.18));z-index:5}
.it.t1{font:400 120px/1 var(--scr)}.it.t2{font:400 96px/1 var(--cap);text-transform:uppercase}
.it.t3{font:italic 500 110px/1 var(--srf);color:transparent;-webkit-text-stroke:1px var(--soft)}
.it.t4{font:400 15px/1 var(--sans);letter-spacing:.5em}
.it svg{width:140px;height:140px}
.tl{padding:70px 7% 30px;border-top:1px solid var(--line);margin-top:70px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px}
.tl h3{grid-column:1/-1;font:italic 500 18px var(--srf);color:var(--soft);text-align:center;margin:0 0 20px;font-weight:500}
.tl div{border-top:1px solid var(--ink);padding-top:14px}
.tl b{display:block;font:400 30px var(--cap);color:var(--soft)}
.tl p{margin:8px 0 0;color:var(--soft);font-size:14px}
.foot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding:30px 7% 40px;font-size:13px;color:var(--mut);border-top:1px solid var(--line)}
.foot a{color:var(--soft)}
.full{grid-column:1/-1}
@media (max-width:1100px){.page{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}.r{display:none}.mob{display:block!important}}
@media (max-width:760px){.cl{height:150px}.page{grid-template-columns:1fr}.m{border-right:0;border-top:1px solid var(--line)}.sel{margin-top:40px}.l{border-right:0}
 .tl{grid-template-columns:1fr 1fr}.it.t1{font-size:70px}.it.t2{font-size:54px}.it.t3{font-size:62px}.it svg{width:92px;height:92px}.hint .d{display:none}.hint .mo{display:inline}}
.hint .mo{display:none}
.mob{display:none;grid-column:1/-1;border-top:1px solid var(--line);padding:50px 6% 20px}
.mob h3{font:400 44px var(--scr);color:var(--soft);text-align:center;margin:0 0 20px;font-weight:400}
.mob ol{list-style:none;padding:0;margin:0;border-top:1px solid var(--line)}
.mob li button{display:flex;justify-content:space-between;width:100%;padding:16px 0;border-bottom:1px solid var(--line);font:400 20px var(--cap);text-transform:uppercase;color:var(--soft);text-align:left;gap:12px}
.mob li em{font:italic 500 17px var(--srf);text-transform:none;color:var(--mut)}
@media (prefers-reduced-motion:reduce){*{transition-duration:.01ms!important}}
</style>
</head>
<body>
<div class="page">
 <section class="l" aria-label="О дизайнере">
  <div class="yr"><span class="cp">©</span>2 0 2 6</div>
  <button class="name" id="nm" type="button" aria-label="Вера Ланская — нажмите, чтобы сменить начертание">
   <span class="v1 on">Вера Ланская</span><span class="v2">Вера Ланская</span><span class="v3">Вера Ланская</span><span class="v4">Вера Ланская</span>
  </button>
  <div class="role">Графический дизайнер <b>+</b> арт-директор</div>
  <div class="lab">Сферы работы:</div>
  <div class="rule"></div>
  <div class="list" id="spheres"></div>
  <p class="about">Меня зовут Вера Ланская. Я графический дизайнер и арт-директор, живу и работаю в Москве. Делаю айдентику,
  упаковку и издательский дизайн — системы, которые выдерживают десятки носителей и не теряют характер.
  Нажмите на сферу — в списке работ останутся только её проекты.</p>
  <div class="lab">Клиенты:</div>
  <div class="rule"></div>
  <div class="cl"><div class="list" id="cl"></div></div>
  <p class="about">В большинстве проектов я работала внутри уже существующего стиля и развивала его под новые носители;
  в остальных — собирала бренд с нуля, от имени до витрины.</p>
  <div class="lab">Контакты:</div>
  <div class="rule"></div>
  <div class="c"><a href="#" id="ml">hello@lanskaya.ysdprojects.space</a><a href="tel:+74950000000">+7 495 000-00-00</a><span>Москва · проекты по всему миру</span></div>
 </section>
 <section class="m" aria-label="Избранные работы">
  <div class="yr2">2 0 2 3<i></i>2 0 2 6</div>
  <div class="sel">Избранные работы<br>Портфолио</div>
  <div class="objs" id="objs"></div>
  <p class="hint"><span class="d">Листы справа выдвигаются — откройте любой</span><span class="mo">Все проекты — списком ниже, нажмите на любой</span></p>
 </section>
 <aside class="r" aria-label="Проекты"><div class="deck" id="deck"></div></aside>
 <section class="mob" aria-label="Проекты (список)"><h3>Работы</h3><ol id="mlist"></ol></section>
 <section class="game full" id="game">
  <h2>Маленькая дизайн-игра</h2>
  <p class="sub">Перетаскивайте буквы и знаки — соберите свою обложку</p>
  <div class="tools"><button type="button" id="mix">перемешать</button><button type="button" id="back">собрать как было</button><button type="button" id="ink">сменить чернила</button></div>
  <div class="board" id="board" aria-label="Поле для игры"></div>
 </section>
 <section class="tl full" aria-label="Хронология"><h3>Хронология:</h3>
  <div><b>2019</b><p>Окончила факультет коммуникационного дизайна, первые плакаты для театра.</p></div>
  <div><b>2021</b><p>Дизайнер в брендинговом бюро: 23 айдентики за два года.</p></div>
  <div><b>2023</b><p>Ушла в самостоятельную практику, первый журнал — «Архив мод».</p></div>
  <div><b>2026</b><p>Арт-директор пяти брендов, преподаю типографику по субботам.</p></div>
 </section>
 <footer class="foot full"><span>© 2026 Вера Ланская</span><span>Сайт разработан <a href="https://ysddev.com" target="_blank" rel="noopener">YSD DEV</a></span></footer>
</div>
<div class="ov" id="ov" aria-hidden="true"><div class="bg" id="ovbg"></div><article class="pane" role="dialog" aria-modal="true" aria-labelledby="pt">
 <button class="x" type="button" id="cls">закрыть ×</button><div class="no" id="pno"></div><h2 id="pt"></h2><div class="k" id="pk"></div>
 <div class="art" id="pa"></div><p id="pd"></p><div class="nav"><button type="button" id="prv">← предыдущая</button><button type="button" id="nxt">следующая →</button></div></article></div>
<script>
var P=__PROJECTS__;
var SP=[["Айдентика",[0,4,7]],["Издательский дизайн",[3,6]],["Упаковка",[2,4]],["ИИ-визуалы",[5]],["Бренд-платформа",[4,0]],["Плакаты",[1,7]]];
var CL=[["Галерея «Сквозняк»","Пекарня «Утренний хлеб»","Чайный дом «Сад камней»","Фестиваль «Коломенский свет»"],["Мастерская «Тихий час»","Лейбл «Частота»","Журнал «Архив мод»","Косметика «Лён и соль»"]];
var $=function(s){return document.getElementById(s)};
// имя: начертания по кругу
var vs=[].slice.call(document.querySelectorAll('#nm span')),vi=0,auto;
function nx(){vs[vi].classList.remove('on');vi=(vi+1)%vs.length;vs[vi].classList.add('on')}
$('nm').addEventListener('click',function(){nx();clearInterval(auto);auto=setInterval(nx,2600)});auto=setInterval(nx,2600);
// искусство: SVG-«объекты» проектов
var uid=0;
function art(p,s,tone){uid++;var id='f'+uid,c=tone||'#5d5a55',t=p.w.toUpperCase(),o='';
 var flt='<defs><filter id="'+id+'" x="-20%" y="-20%" width="140%" height="140%"><feTurbulence type="fractalNoise" baseFrequency="'+(p.art=='wave'?'.012 .08':'.022')+'" numOctaves="2" seed="'+(uid*7)+'"/><feDisplacementMap in="SourceGraphic" scale="'+(s?16:10)+'"/><feGaussianBlur stdDeviation=".35"/></filter>'
  +'<path id="'+id+'c" d="M100,100 m-66,0 a66,66 0 1,1 132,0 a66,66 0 1,1 -132,0"/></defs>';
 if(p.art=='disc'||p.art=='rings'){o=flt+'<g filter="url(#'+id+')"><circle cx="100" cy="100" r="88" fill="'+(p.art=='disc'?'#b9b5ad':'none')+'" stroke="'+c+'" stroke-width="'+(p.art=='disc'?0:1)+'"/>'
  +(p.art=='rings'?[78,64,50,36].map(function(r,i){return'<circle cx="100" cy="100" r="'+r+'" fill="none" stroke="'+c+'" stroke-width="'+(4-i*.7)+'" stroke-dasharray="'+(i*3+1)+' '+(i*2+2)+'"/>'}).join(''):'')
  +'<text font-family="Cormorant" font-style="italic" font-size="17" fill="'+(p.art=='disc'?'#f6f5f2':c)+'" letter-spacing="3"><textPath href="#'+id+'c">'+t+' · '+t+' · </textPath></text>'
  +'<text x="100" y="110" text-anchor="middle" font-family="Great Vibes" font-size="34" fill="'+(p.art=='disc'?'#fff':c)+'">'+p.n+'</text><circle cx="100" cy="100" r="5" fill="'+c+'"/></g>'}
 else if(p.art=='poster'){o=flt+'<rect x="40" y="8" width="120" height="184" fill="#d8d4cc"/><g filter="url(#'+id+')"><rect x="92" y="8" width="16" height="184" fill="'+c+'" opacity=".85"/>'
  +'<text x="100" y="60" text-anchor="middle" font-family="Forum" font-size="20" fill="'+c+'" transform="scale(1 2.2) translate(0 -32)">'+t.split(' ')[0]+'</text>'
  +'<text x="100" y="176" text-anchor="middle" font-family="Cormorant" font-style="italic" font-size="14" fill="'+c+'">'+(t.split(' ')[1]||'')+'</text></g>'}
 else if(p.art=='box'){o=flt+'<g filter="url(#'+id+')"><path d="M44 66 L100 40 L156 66 L156 150 L100 176 L44 150Z" fill="#dcd8d0" stroke="'+c+'"/><path d="M44 66 L100 92 L156 66 M100 92 V176" fill="none" stroke="'+c+'"/>'
  +[0,1,2,3,4].map(function(i){return'<path d="M'+(52+i*2)+' '+(98+i*9)+' q 20 -10 40 '+(4+i)+'" fill="none" stroke="'+c+'" stroke-width=".8"/>'}).join('')
  +'<text x="128" y="122" text-anchor="middle" font-family="Great Vibes" font-size="19" fill="'+c+'" transform="rotate(-24 128 122)">'+p.n+'</text></g>'}
 else if(p.art=='book'||p.art=='spread'){o=flt+'<g filter="url(#'+id+')"><rect x="22" y="40" width="78" height="118" fill="#f6f5f2" stroke="'+c+'" stroke-width=".8"/><rect x="100" y="40" width="78" height="118" fill="#e2ded6" stroke="'+c+'" stroke-width=".8"/>'
  +'<text x="61" y="100" text-anchor="middle" font-family="Great Vibes" font-size="'+(p.art=='book'?24:20)+'" fill="'+c+'">'+p.n+'</text>'
  +[0,1,2,3,4,5,6].map(function(i){return'<rect x="'+(110+(i%2)*30)+'" y="'+(52+Math.floor(i/2)*22)+'" width="24" height="16" fill="'+c+'" opacity="'+(.2+i*.08)+'"/>'}).join('')+'</g>'}
 else if(p.art=='wave'){o=flt+'<g filter="url(#'+id+')">'+[0,1,2,3,4,5,6,7,8].map(function(i){return'<path d="M10 '+(40+i*15)+' C 60 '+(20+i*15)+', 140 '+(70+i*15)+', 190 '+(40+i*15)+'" fill="none" stroke="'+c+'" stroke-width="'+(.6+i*.25)+'"/>'}).join('')
  +'<text x="100" y="108" text-anchor="middle" font-family="Forum" font-size="26" fill="'+c+'" letter-spacing="2">'+t+'</text></g>'}
 else {o=flt+'<g filter="url(#'+id+')">'+t.split('').map(function(ch,i){return'<text x="'+(16+i*22)+'" y="'+(110+Math.sin(i)*30)+'" font-family="Forum" font-size="40" fill="'+c+'">'+ch+'</text>'}).join('')+'</g>'}
 return '<svg viewBox="0 0 200 200" role="img" aria-label="'+p.n+'">'+o+'</svg>'}
$('objs').innerHTML=[0,5,2].map(function(i){return'<button class="obj" type="button" data-i="'+i+'">'+art(P[i])+'</button>'}).join('');
// листы
function deck(filter){mlist(filter);var html='<div class="sh top"><h3>Содержание</h3><p>Восемь проектов 2023–2026. Наведите на лист — он выдвинется.</p><ol>'
 +P.map(function(p,i){return(!filter||filter.indexOf(i)>=0)?'<li><button type="button" data-i="'+i+'">'+p.n+'</button><em>'+p.y+'</em></li>':''}).join('')+'</ol></div>';
 P.forEach(function(p,i){if(!filter||filter.indexOf(i)>=0)html+='<button class="sh" type="button" data-i="'+i+'" aria-label="'+p.n+', '+p.y+'"><span>'+p.n+'</span><small>'+p.y+'</small></button>'});
 $('deck').innerHTML=html}
deck();
function mlist(f){$('mlist').innerHTML=P.map(function(p,i){return(!f||f.indexOf(i)>=0)?'<li><button type="button" data-i="'+i+'">'+p.n+'<em>'+p.k+', '+p.y+'</em></button></li>':''}).join('')}
$('spheres').innerHTML=SP.map(function(s,i){return'<button type="button" data-s="'+i+'"><sup>'+(i+1)+'.</sup>'+s[0]+'</button>'}).join('');
$('spheres').addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;var on=!b.classList.contains('on');
 [].forEach.call(this.children,function(x){x.classList.remove('on')});if(on){b.classList.add('on');deck(SP[+b.dataset.s][1])}else deck()});
// клиенты: две строки по очереди
var ci=0;function cl(){$('cl').innerHTML=CL[ci].map(function(c,i){return'<span><sup>'+(ci*4+i+1)+'.</sup>'+c+'</span>'}).join('');ci=(ci+1)%CL.length}
cl();setInterval(function(){var l=$('cl');l.style.opacity=0;l.style.transform='translateY(-16px)';setTimeout(function(){cl();l.style.transform='translateY(16px)';requestAnimationFrame(function(){requestAnimationFrame(function(){l.style.opacity=1;l.style.transform='none'})})},800)},4200);
// лист проекта
var cur=0,ov=$('ov');
function open(i){cur=(i+P.length)%P.length;var p=P[cur];$('pno').textContent=('0'+(cur+1)).slice(-2)+' / 0'+P.length+' · '+p.y;$('pt').textContent=p.n;$('pk').textContent=p.k;
 $('pa').innerHTML=art(p,1);$('pd').textContent=p.d;ov.classList.add('on');ov.setAttribute('aria-hidden','false');$('cls').focus()}
function close(){ov.classList.remove('on');ov.setAttribute('aria-hidden','true')}
document.addEventListener('click',function(e){var b=e.target.closest('[data-i]');if(b&&!e.target.closest('.it'))open(+b.dataset.i)});
$('cls').onclick=close;$('ovbg').onclick=close;$('prv').onclick=function(){open(cur-1)};$('nxt').onclick=function(){open(cur+1)};
document.addEventListener('keydown',function(e){if(!ov.classList.contains('on'))return;if(e.key=='Escape')close();if(e.key=='ArrowRight')open(cur+1);if(e.key=='ArrowLeft')open(cur-1)});
$('ml').onclick=function(e){e.preventDefault();try{navigator.clipboard.writeText(this.textContent)}catch(x){}var t=this.textContent;this.textContent='адрес скопирован';var a=this;setTimeout(function(){a.textContent=t},1400)};
// дизайн-игра
var B=$('board'),items=[["Л","t1"],["А","t2"],["Н","t3"],["С","t1"],["К","t2"],["А","t3"],["Я","t1"],["вера","t4"],["2 0 2 6","t4"]],inks=['#5d5a55','#2a3cff','#a8432f','#2d2c2a'],ii=0,els=[];
function layout(mix){var w=B.clientWidth,h=B.clientHeight,nar=w<640;els.forEach(function(el,i){var x,y,ew=el.offsetWidth,eh=el.offsetHeight;
 if(mix){x=Math.random()*Math.max(0,w-ew);y=Math.random()*Math.max(0,h-eh)}
 else if(nar){var row=i<4?0:1,col=i<4?i:i-4,cnt=row?3:4,step=Math.min(86,(w-24)/4);
  if(i<7){x=w/2-step*cnt/2+col*step+(step-ew)/2;y=row?h*.36:h*.08}else if(i<9){x=i==7?16:w-ew-16;y=h*.66}else{x=i==9?w*.18:w*.56;y=h*.72}}
 else{var n=7,step=Math.min(130,(w-80)/n);x=i<7?w/2-step*3.5+i*step:w/2+(i==7?-160:40);y=i<7?h/2-80:h/2+70}
 x=Math.min(Math.max(0,x),Math.max(0,w-ew));y=Math.min(Math.max(0,y),Math.max(0,h-eh))
 el.style.transform='translate('+x+'px,'+y+'px) rotate('+(mix?(Math.random()*40-20):0)+'deg)';el.dataset.x=x;el.dataset.y=y})}
items.forEach(function(t){var d=document.createElement('div');d.className='it '+t[1];d.textContent=t[0];B.appendChild(d);els.push(d)});
[P[0],P[5]].forEach(function(p){var d=document.createElement('div');d.className='it';d.innerHTML=art(p);B.appendChild(d);els.push(d)});
layout(false);window.addEventListener('resize',function(){layout(false)});
var drag=null;
B.addEventListener('pointerdown',function(e){var el=e.target.closest('.it');if(!el)return;drag={el:el,sx:e.clientX,sy:e.clientY,x:+el.dataset.x,y:+el.dataset.y};el.classList.add('dr');B.appendChild(el);el.setPointerCapture(e.pointerId)});
B.addEventListener('pointermove',function(e){if(!drag)return;var x=drag.x+e.clientX-drag.sx,y=drag.y+e.clientY-drag.sy;drag.el.style.transform='translate('+x+'px,'+y+'px) rotate(-3deg)';drag.nx=x;drag.ny=y});
function up(){if(!drag)return;if(drag.nx!=null){drag.el.dataset.x=drag.nx;drag.el.dataset.y=drag.ny;drag.el.style.transform='translate('+drag.nx+'px,'+drag.ny+'px)'}drag.el.classList.remove('dr');drag=null}
B.addEventListener('pointerup',up);B.addEventListener('pointercancel',up);
$('mix').onclick=function(){layout(true)};$('back').onclick=function(){layout(false)};
$('ink').onclick=function(){ii=(ii+1)%inks.length;B.style.setProperty('--soft',inks[ii]);els.forEach(function(el){el.style.color=inks[ii];el.style.webkitTextStrokeColor=inks[ii]})};
</script>
</body>
</html>
"""


def cfg() -> dict:
    import json
    return {
        "slug": "lanskaya",
        "fonts": [("Great Vibes", "great-vibes", [400], "normal"), ("Cormorant", "cormorant", [500], "italic"),
                  ("Forum", "forum", [400], "normal"), ("Inter Tight", "inter-tight", [400], "normal"),
                  ("Marck Script", "marck-script", [400], "normal")],
        "fav": ("В", "#2d2c2a", "#eeece8"),
        "html": HTML.replace("__PROJECTS__", json.dumps(PROJECTS, ensure_ascii=False)),
    }
