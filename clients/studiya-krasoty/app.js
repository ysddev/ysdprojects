(function(){
"use strict";
var D={"cats": [{"id": "hair", "name": "Волосы", "img": "hair", "master": "anastasiya"}, {"id": "nails", "name": "Ногти", "img": "nails", "master": "yana"}, {"id": "makeup", "name": "Макияж и брови", "img": "makeup", "master": "albina"}, {"id": "care", "name": "Уход и косметика", "img": "care", "master": "natalya"}], "svc": [{"id": 0, "cat": "hair", "name": "Женская стрижка", "dur": 60, "price": 2500, "from": true}, {"id": 1, "cat": "hair", "name": "Укладка", "dur": 45, "price": 1800, "from": true}, {"id": 2, "cat": "hair", "name": "Окрашивание в один тон", "dur": 120, "price": 5500, "from": true}, {"id": 3, "cat": "hair", "name": "Сложное окрашивание: airtouch, шатуш", "dur": 240, "price": 9000, "from": true}, {"id": 4, "cat": "hair", "name": "Уход и восстановление волос", "dur": 60, "price": 3000, "from": true}, {"id": 5, "cat": "nails", "name": "Маникюр с покрытием гель-лак", "dur": 90, "price": 2800, "from": false}, {"id": 6, "cat": "nails", "name": "Маникюр без покрытия", "dur": 45, "price": 1500, "from": false}, {"id": 7, "cat": "nails", "name": "Педикюр с покрытием", "dur": 105, "price": 3500, "from": false}, {"id": 8, "cat": "nails", "name": "Наращивание ногтей", "dur": 150, "price": 4500, "from": true}, {"id": 9, "cat": "nails", "name": "Снятие покрытия и уход", "dur": 30, "price": 800, "from": false}, {"id": 10, "cat": "makeup", "name": "Дневной макияж", "dur": 60, "price": 3500, "from": false}, {"id": 11, "cat": "makeup", "name": "Вечерний макияж", "dur": 75, "price": 4500, "from": false}, {"id": 12, "cat": "makeup", "name": "Свадебный макияж с репетицией", "dur": 150, "price": 8000, "from": true}, {"id": 13, "cat": "makeup", "name": "Коррекция и окрашивание бровей", "dur": 45, "price": 1800, "from": false}, {"id": 14, "cat": "makeup", "name": "Урок макияжа «для себя»", "dur": 120, "price": 5000, "from": false}, {"id": 15, "cat": "care", "name": "Консультация по уходу за кожей лица", "dur": 45, "price": 1500, "from": false}, {"id": 16, "cat": "care", "name": "Подбор домашнего ухода для волос", "dur": 30, "price": 1000, "from": false}, {"id": 17, "cat": "care", "name": "Разбор косметички с рекомендациями", "dur": 60, "price": 2000, "from": false}, {"id": 18, "cat": "care", "name": "Уходовая процедура с подбором средств", "dur": 60, "price": 2500, "from": false}], "masters": [{"id": "anastasiya", "name": "Анастасия", "role": "Парикмахер-стилист", "cats": ["hair"], "exp": "10 лет", "img": "m-ana"}, {"id": "yana", "name": "Яна", "role": "Мастер ногтевого сервиса", "cats": ["nails"], "exp": "7 лет", "img": "m-yana"}, {"id": "albina", "name": "Альбина", "role": "Визажист", "cats": ["makeup"], "exp": "6 лет", "img": "m-alb"}, {"id": "natalya", "name": "Наталья", "role": "Консультант по косметике", "cats": ["care"], "exp": "8 лет", "img": "m-nat"}, {"id": "viktoriya", "name": "Виктория", "role": "Менеджер студии", "cats": [], "exp": "5 лет", "img": "m-vik"}]}, CATS=D.cats, SVC=D.svc, MASTERS=D.masters.filter(function(m){return m.cats.length}), BASE=document.body.getAttribute("data-base")||"";
var $=function(s,r){return (r||document).querySelector(s)}, $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
function rub(n){return n.toString().replace(/\B(?=(\d{3})+(?!\d))/g," ")+" ₽"}
function price(s){return (s.from?"от ":"")+rub(s.price)}
function dur(m){var h=Math.floor(m/60),r=m%60;return (h?h+" ч":"")+(h&&r?" ":"")+(r?r+" мин":"")}
function esc(t){return String(t).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function catById(id){return CATS.filter(function(c){return c.id===id})[0]}
function svcById(id){return SVC.filter(function(s){return s.id===+id})[0]}
function mById(id){return MASTERS.filter(function(m){return m.id===id})[0]}
var ARR='<svg><use href="#i-arrow"/></svg>';

/* ---- services (home) ---- */
var tabs=$("#tabs");
if(tabs){
  var plist=$("#plist"), photo=$("#svcPhoto");
  CATS.forEach(function(c){
    var b=document.createElement("button");b.className="tab";b.setAttribute("role","tab");b.textContent=c.name;b.dataset.cat=c.id;
    b.addEventListener("click",function(){setCat(c.id)});tabs.appendChild(b);
    var im=document.createElement("img");im.src=BASE+"img/"+c.img+"-800.webp";im.srcset=BASE+"img/"+c.img+"-500.webp 500w, "+BASE+"img/"+c.img+"-800.webp 800w";
    im.sizes="(min-width:900px) 40vw, 100vw";im.alt=c.name;im.dataset.cat=c.id;im.width=800;im.height=1000;photo.appendChild(im);
  });
  var cap=document.createElement("a");cap.className="cap";photo.appendChild(cap);
  var setCat=function(id){
    var c=catById(id), m=mById(c.master);
    $$(".tab",tabs).forEach(function(b){b.setAttribute("aria-selected",b.dataset.cat===id)});
    $$("img",photo).forEach(function(i){i.classList.toggle("on",i.dataset.cat===id)});
    cap.innerHTML=c.name+(m?'<small>Мастер — '+m.name+'</small>':'');cap.href=m?BASE+"mastera/"+m.id+"/":"#";
    plist.innerHTML=SVC.filter(function(s){return s.cat===id}).map(function(s){
      return '<li class="prow"><span class="prow-name">'+s.name+'</span><span class="prow-meta">'+dur(s.dur)+'</span><span class="prow-price"><b>'+price(s)+'</b><button class="prow-book" data-book-svc="'+s.id+'" aria-label="Записаться: '+esc(s.name)+'">'+ARR+'</button></span></li>';
    }).join("");
  };
  setCat(CATS[0].id);
}

/* ---- header / menu / sticky ---- */
var hdr=$("#hdr"), mcta=$("#mcta"), burger=$("#burger");
function onScroll(){var y=window.scrollY;hdr.classList.toggle("scrolled",y>10);if(mcta)mcta.classList.toggle("show",y>window.innerHeight*.6&&!document.body.classList.contains("menu-open"));}
window.addEventListener("scroll",onScroll,{passive:true});onScroll();
function menu(open){document.body.classList.toggle("menu-open",open);burger.setAttribute("aria-expanded",open);document.body.classList.toggle("lock",open||bkOpen());onScroll();}
burger.addEventListener("click",function(){menu(!document.body.classList.contains("menu-open"))});
$$("#mnav a").forEach(function(a){a.addEventListener("click",function(){menu(false)})});
window.addEventListener("resize",function(){if(window.innerWidth>=1024&&document.body.classList.contains("menu-open"))menu(false)});
$$(".yr").forEach(function(e){e.textContent=new Date().getFullYear()});

/* ---- reveal ---- */
if("IntersectionObserver" in window){
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}})},{rootMargin:"0px 0px -6% 0px",threshold:.06});
  $$(".rv").forEach(function(el){io.observe(el)});
}else{$$(".rv").forEach(function(el){el.classList.add("in")})}

/* ---- schedule (demo) ---- */
var DAYS=["вс","пн","вт","ср","чт","пт","сб"], MON=["января","февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря"], MONN=["январь","февраль","март","апрель","май","июнь","июль","август","сентябрь","октябрь","ноябрь","декабрь"];
function hash(s){var h=2166136261;for(var i=0;i<s.length;i++){h^=s.charCodeAt(i);h=Math.imul(h,16777619)}return h>>>0}
function dayKey(d){return d.getFullYear()+"-"+(d.getMonth()+1)+"-"+d.getDate()}
function slots(date,masterId){
  var out=[],now=new Date(),today=dayKey(now)===dayKey(date);
  for(var t=10*60;t<=20*60;t+=30){
    var hh=Math.floor(t/60),mm=t%60,lbl=hh+":"+(mm?"30":"00");
    var busy=(hash(dayKey(date)+(masterId||"any")+lbl)%100)<(masterId?38:22);
    if(today&&t<=now.getHours()*60+now.getMinutes()+30)busy=true;
    out.push({t:lbl,busy:busy});
  }
  return out;
}
function dayName(d){var n=new Date();n.setHours(0,0,0,0);var x=new Date(d);x.setHours(0,0,0,0);var diff=Math.round((x-n)/864e5);return diff===0?"Сегодня":diff===1?"Завтра":d.getDate()+" "+MON[d.getMonth()]}
$$("[data-nearest]").forEach(function(el){
  var mid=el.getAttribute("data-nearest")||null, label=el.getAttribute("data-label")||"";
  for(var i=0;i<14;i++){var d=new Date();d.setDate(d.getDate()+i);var f=slots(d,mid).filter(function(s){return !s.busy})[0];if(f){el.textContent=dayName(d)+", "+f.t+label;return}}
});

/* ---- booking ---- */
var bk=$("#bk"), st={}, lastFocus=null;
function bkOpen(){return bk&&bk.classList.contains("open")}
var LBL=["Услуга","Мастер","Дата и время","Контакты"];
function openBk(o){
  o=o||{};lastFocus=document.activeElement;
  st={step:0,cat:CATS[0].id,svc:null,master:null,date:null,time:null,lockMaster:false};
  if(o.master&&mById(o.master)){st.master=o.master;st.lockMaster=true;st.cat=mById(o.master).cats[0]}
  if(o.svc!=null&&svcById(o.svc)){var s=svcById(o.svc);st.svc=s.id;st.cat=s.cat;st.step=st.lockMaster?2:1}
  var d=new Date();d.setHours(0,0,0,0);st.date=d;st._scrollDay=true;
  if(document.body.classList.contains("menu-open"))menu(false);
  bk.classList.add("open");document.body.classList.add("lock");render();
  setTimeout(function(){try{$(".bk-x").focus({preventScroll:true})}catch(e){}},60);
}
function closeBk(){bk.classList.remove("open");document.body.classList.remove("lock");if(lastFocus)try{lastFocus.focus({preventScroll:true})}catch(e){}}
document.addEventListener("click",function(e){
  var t=e.target.closest("[data-book],[data-book-svc],[data-book-master],[data-close]");if(!t)return;
  if(t.hasAttribute("data-close")){closeBk();return}
  e.preventDefault();
  openBk({svc:t.getAttribute("data-book-svc"),master:t.getAttribute("data-book-master")});
});
document.addEventListener("keydown",function(e){if(e.key==="Escape"){if(lbOpen())closeLb();else if(bkOpen())closeBk()}});

function render(){
  $$(".pane",bk).forEach(function(p){p.classList.toggle("on",+p.dataset.pane===st.step)});
  $$("#bkProg i").forEach(function(i,k){i.classList.toggle("on",k<=Math.min(st.step,3))});
  $("#bkLbl").textContent=st.step<4?"Шаг "+(st.step+1)+" из 4 · "+LBL[st.step]:"Готово";
  $("#bkFoot").style.display=st.step===4?"none":"flex";
  $("#bkBack").style.display=st.step===0?"none":"";
  $("#bkNext").textContent=st.step===3?"Записаться":"Далее";
  [rSvc,rMasters,rTime,rForm,function(){}][st.step]();
  valid();$("#bkBody").scrollTop=0;
}
function valid(){var ok=[st.svc!=null,!!st.master,!!st.time,$("#iAgree").checked][st.step];$("#bkNext").disabled=!ok}
function rSvc(){
  var allowed=st.lockMaster?mById(st.master).cats:CATS.map(function(c){return c.id});
  if(allowed.indexOf(st.cat)<0)st.cat=allowed[0];
  var chips=CATS.filter(function(c){return allowed.indexOf(c.id)>=0});
  $("#bkCats").style.display=chips.length>1?"flex":"none";
  $("#bkCats").innerHTML=chips.map(function(c){return '<button class="tab" data-c="'+c.id+'" aria-selected="'+(c.id===st.cat)+'">'+c.name+'</button>'}).join("");
  $("#bkSvc").innerHTML=(st.lockMaster?'<div class="bk-who"><img src="'+BASE+'img/'+mById(st.master).img+'-500.webp" alt=""><span>Запись к мастеру<b>'+mById(st.master).name+'</b></span></div>':'')+SVC.filter(function(s){return s.cat===st.cat}).map(function(s){
    return '<button class="opt'+(st.svc===s.id?' sel':'')+'" data-s="'+s.id+'"><span class="radio"></span><span class="o-main"><span class="o-name">'+s.name+'</span><span class="o-meta">'+dur(s.dur)+'</span></span><span class="o-price">'+price(s)+'</span></button>';
  }).join("");
}
function rMasters(){
  var s=svcById(st.svc), list=MASTERS.filter(function(m){return m.cats.indexOf(s.cat)>=0});
  if(st.master&&st.master!=="any"&&list.every(function(m){return m.id!==st.master}))st.master=null;
  var html=list.map(function(m){return '<button class="opt'+(st.master===m.id?' sel':'')+'" data-m="'+m.id+'"><img class="ava" src="'+BASE+'img/'+m.img+'-500.webp" alt=""><span class="o-main"><span class="o-name">'+m.name+'</span><span class="o-meta">'+m.role+' · стаж '+m.exp+'</span></span><span class="radio"></span></button>'}).join("");
  html+='<button class="opt'+(st.master==="any"?' sel':'')+'" data-m="any"><span class="ava ava-any"><svg><use href="#i-user"/></svg></span><span class="o-main"><span class="o-name">Любой свободный мастер</span><span class="o-meta">Подберём ближайшее время</span></span><span class="radio"></span></button>';
  $("#bkMasters").innerHTML=html;
}
function rTime(){
  var html="",base=new Date();base.setHours(0,0,0,0);
  for(var i=0;i<14;i++){var d=new Date(base);d.setDate(base.getDate()+i);var sel=dayKey(d)===dayKey(st.date);
    html+='<button class="day'+(sel?' sel':'')+'" data-d="'+i+'"><small>'+(i===0?"сег":DAYS[d.getDay()])+'</small><b>'+d.getDate()+'</b></button>';}
  $("#bkDays").innerHTML=html;
  $("#bkMonth").textContent=MONN[st.date.getMonth()]+" "+st.date.getFullYear();
  var sl=slots(st.date,st.master==="any"?null:st.master), free=sl.filter(function(x){return !x.busy}).length;
  $("#bkTimes").innerHTML=free?'<div class="times-lbl">'+dayName(st.date)+' · свободно окон: '+free+'</div><div class="times">'+sl.map(function(x){return '<button class="time'+(st.time===x.t?' sel':'')+'" data-t="'+x.t+'"'+(x.busy?' disabled':'')+'>'+x.t+'</button>'}).join("")+'</div>':'<div class="empty">На этот день всё занято. Выберите другую дату — ближайшие окна есть уже завтра.</div>';
  if(st._scrollDay){var d0=$(".day.sel",bk);if(d0)$("#bkDays").scrollLeft=0;st._scrollDay=false}
}
function sumHTML(){
  var s=svcById(st.svc), m=st.master==="any"?"Любой свободный":mById(st.master).name;
  return '<div><span>Услуга</span><b>'+s.name+'</b></div><div><span>Мастер</span><b>'+m+'</b></div><div><span>Когда</span><b>'+dayName(st.date)+', '+st.time+'</b></div><div><span>Стоимость</span><b>'+price(s)+'</b></div>';
}
function rForm(){$("#bkSum").innerHTML=sumHTML()}
if(bk){
bk.addEventListener("click",function(e){
  var t;
  if(t=e.target.closest("[data-c]")){st.cat=t.dataset.c;rSvc();valid();return}
  if(t=e.target.closest("[data-s]")){st.svc=+t.dataset.s;rSvc();valid();setTimeout(next,200);return}
  if(t=e.target.closest("[data-m]")){st.master=t.dataset.m;st.time=null;rMasters();valid();setTimeout(next,200);return}
  if(t=e.target.closest("[data-d]")){var d=new Date();d.setHours(0,0,0,0);d.setDate(d.getDate()+ +t.dataset.d);st.date=d;st.time=null;var sl=$("#bkDays").scrollLeft;rTime();$("#bkDays").scrollLeft=sl;valid();return}
  if(t=e.target.closest("[data-t]")){st.time=t.dataset.t;$$(".time",bk).forEach(function(b){b.classList.toggle("sel",b===t)});valid();return}
});
}
function next(){
  if(st.step===3){submit();return}
  if($("#bkNext").disabled)return;
  st.step++;
  if(st.step===1&&st.lockMaster)st.step=2;
  if(st.step===2)st._scrollDay=true;
  render();
}
if(bk){
$("#bkNext").addEventListener("click",next);
$("#bkBack").addEventListener("click",function(){st.step--;if(st.step===1&&st.lockMaster)st.step=0;render()});
var ph=$("#iPhone");
var fmt=function(v){var d=v.replace(/\D/g,"");if(d[0]==="8")d="7"+d.slice(1);if(d[0]!=="7")d="7"+d;d=d.slice(0,11);var r="+7";if(d.length>1)r+=" ("+d.slice(1,4);if(d.length>=4)r+=")";if(d.length>4)r+=" "+d.slice(4,7);if(d.length>7)r+="-"+d.slice(7,9);if(d.length>9)r+="-"+d.slice(9,11);return r};
ph.addEventListener("focus",function(){if(!ph.value)ph.value="+7 ("});
ph.addEventListener("input",function(){var n=ph.value.replace(/\D/g,"");ph.value=n.length<=1?"+7 (":fmt(ph.value);$("#fPhone").classList.remove("err")});
ph.addEventListener("blur",function(){if(ph.value.replace(/\D/g,"").length<=1)ph.value=""});
$("#iName").addEventListener("input",function(){$("#fName").classList.remove("err")});
$("#iAgree").addEventListener("change",valid);
}
function submit(){
  var n=$("#iName").value.trim(), p=$("#iPhone").value.replace(/\D/g,""), ok=true;
  if(n.length<2){$("#fName").classList.add("err");ok=false}
  if(p.length!==11){$("#fPhone").classList.add("err");ok=false}
  if(!$("#iAgree").checked)ok=false;
  if(!ok){var f=$(".field.err",bk);if(f)f.querySelector("input").focus();return}
  $("#doneSum").innerHTML=sumHTML()+'<div><span>Имя</span><b>'+esc(n)+'</b></div><div><span>Телефон</span><b>'+esc($("#iPhone").value)+'</b></div>';
  $("#doneTxt").textContent=n.split(" ")[0]+", спасибо! Администратор подтвердит запись в течение 15 минут, а накануне мы напомним о визите.";
  st.step=4;render();
}

/* ---- lightbox ---- */
var lb=$("#lb"), lbList=[], lbI=0;
function lbOpen(){return lb&&lb.classList.contains("open")}
function showLb(){var b=lbList[lbI];$("#lbImg").src=b.getAttribute("data-full");$("#lbImg").alt=b.querySelector("img").alt;$("#lbC").textContent=(lbI+1)+" / "+lbList.length}
function closeLb(){lb.classList.remove("open");if(!bkOpen())document.body.classList.remove("lock")}
if(lb){
  $$("[data-full]").forEach(function(b){b.addEventListener("click",function(){lbList=$$("[data-full]",b.parentNode);lbI=lbList.indexOf(b);showLb();lb.classList.add("open");document.body.classList.add("lock")})});
  $("#lbX").addEventListener("click",closeLb);
  $("#lbP").addEventListener("click",function(){lbI=(lbI-1+lbList.length)%lbList.length;showLb()});
  $("#lbN").addEventListener("click",function(){lbI=(lbI+1)%lbList.length;showLb()});
  lb.addEventListener("click",function(e){if(e.target===lb)closeLb()});
  document.addEventListener("keydown",function(e){if(!lbOpen())return;if(e.key==="ArrowLeft")$("#lbP").click();if(e.key==="ArrowRight")$("#lbN").click()});
  var sx=null;lb.addEventListener("touchstart",function(e){sx=e.touches[0].clientX},{passive:true});
  lb.addEventListener("touchend",function(e){if(sx==null)return;var dx=e.changedTouches[0].clientX-sx;if(Math.abs(dx)>50)(dx<0?$("#lbN"):$("#lbP")).click();sx=null});
}
})();
