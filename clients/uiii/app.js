(function(){
  // Примеры товаров для демо — заменим на 15 товаров клиента
  var P=[
    {id:'alpine-shell',line:'UIII alpine',cat:'Куртки',name:'Мембранная куртка',price:24900,img:'zip',desc:'Трёхслойная мембрана, проклеенные швы, капюшон под шлем. Для склона и высоты, когда погода меняется за час.',sizes:['XS','S','M','L','XL']},
    {id:'sport-softshell',line:'UIII sport',cat:'Куртки',name:'Софтшелл',price:14900,img:'drops',desc:'Тянется вместе с вами, держит ветер и лёгкий дождь. Подходит для скал, яхты и города.',sizes:['XS','S','M','L','XL']},
    {id:'fleece',line:'UIII',cat:'Флис',name:'Флисовая кофта',price:8900,img:'fabrics',desc:'Тёплый средний слой: под мембрану в горах или сама по себе вечером у воды.',sizes:['S','M','L','XL']},
    {id:'base-layer',line:'UIII sport',cat:'Базовый слой',name:'Термолонгслив',price:5900,img:'blue-fabric',desc:'Первый слой из мериноса. Не холодит, когда промок, и не пахнет после долгого дня.',sizes:['XS','S','M','L','XL']},
    {id:'beanie',line:'UIII',cat:'Аксессуары',name:'Шапка из мериноса',price:2900,img:'spools',desc:'Тонкая вязка — помещается под шлем и в карман.',sizes:['One size']},
    {id:'neck',line:'UIII alpine',cat:'Аксессуары',name:'Баф',price:1900,img:'seam',desc:'Закрывает лицо от ветра и солнца на склоне и на палубе.',sizes:['One size']}
  ];
  var rub=function(n){return n.toLocaleString('ru-RU').replace(/ |,/g,' ')+' ₽'};
  var arrow='<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 7h10v10"/><path d="M7 17 17 7"/></svg>';

  // каталог
  document.querySelectorAll('[data-catalog]').forEach(function(box){
    box.innerHTML=P.map(function(p){
      return '<li class="card" data-cat="'+p.cat+'"><button type="button" class="card-btn" data-open="'+p.id+'" aria-label="'+p.name+', '+rub(p.price)+' — подробнее">'+
        '<span class="card-ph"><img src="img/'+p.img+'.webp" alt="" loading="lazy" width="1086" height="1448"></span>'+
        '<span class="card-tx"><span class="card-line">'+p.line+'</span><span class="card-name">'+p.name+'</span><span class="card-price">'+rub(p.price)+'</span></span>'+
        '<span class="card-go">'+arrow+'</span></button></li>';
    }).join('');
  });

  // фильтры
  document.querySelectorAll('[data-filter]').forEach(function(b){
    b.addEventListener('click',function(){
      var c=b.getAttribute('data-filter');
      document.querySelectorAll('[data-filter]').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
      document.querySelectorAll('[data-catalog] .card').forEach(function(card){
        card.hidden=!(c==='all'||card.getAttribute('data-cat')===c);
      });
    });
  });

  // всплывающая карточка
  var dlg=document.getElementById('pop'),cur=null,count=0;
  var cartB=document.querySelectorAll('[data-cart-count]');
  var toast=document.getElementById('toast'),tt;
  function say(t){if(!toast)return;toast.textContent=t;toast.classList.add('show');clearTimeout(tt);tt=setTimeout(function(){toast.classList.remove('show')},2600)}
  document.addEventListener('click',function(e){
    var o=e.target.closest('[data-open]');
    if(!o||!dlg)return;
    var p=P.filter(function(x){return x.id===o.getAttribute('data-open')})[0];cur=p;
    dlg.querySelector('.pop-ph img').src='img/'+p.img+'.webp';
    dlg.querySelector('.pop-line').textContent=p.line+' · '+p.cat;
    dlg.querySelector('h3').textContent=p.name;
    dlg.querySelector('.pop-price').textContent=rub(p.price);
    dlg.querySelector('.pop-desc').textContent=p.desc;
    dlg.querySelector('.sizes-in').innerHTML=p.sizes.map(function(s,i){return '<label><input type="radio" name="size" value="'+s+'"'+(i===Math.min(2,p.sizes.length-1)?' checked':'')+'><span>'+s+'</span></label>'}).join('');
    dlg.showModal();
  });
  if(dlg){
    dlg.querySelector('.pop-x').addEventListener('click',function(){dlg.close()});
    dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close()});
    dlg.querySelector('[data-add]').addEventListener('click',function(){
      var s=dlg.querySelector('input[name=size]:checked');
      count++;cartB.forEach(function(b){b.textContent=count});
      dlg.close();say(cur.name+(s&&s.value!=='One size'?', '+s.value:'')+' — в корзине');
    });
  }

  // меню на телефоне
  var mb=document.querySelector('[data-menu]'),nav=document.querySelector('.nav');
  if(mb&&nav){
    mb.addEventListener('click',function(){var o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o)});
    nav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){nav.classList.remove('open');mb.setAttribute('aria-expanded','false')})});
  }

  // форма (демо)
  document.querySelectorAll('form[data-lead]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var n=f.querySelector('.form-note');
      if(!f.checkValidity()){f.reportValidity();return}
      n.textContent='Это демо. На готовом сайте заявка сразу придёт вам на почту или в Telegram.';
    });
  });

  // шапка: фон после прокрутки
  var h=document.querySelector('.hdr');
  if(h){var on=function(){h.classList.toggle('scrolled',scrollY>40)};on();addEventListener('scroll',on,{passive:true})}

  document.documentElement.classList.add('ready');
})();
