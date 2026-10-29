(function(){var L=['es','en','fr','de'];var h=document.documentElement;
function pick(){try{var q=new URLSearchParams(location.search).get('lang');if(L.indexOf(q)>=0)return q;var s=localStorage.getItem('mjc-lang');if(L.indexOf(s)>=0)return s}catch(e){}
var n=((navigator.languages&&navigator.languages[0])||navigator.language||'es').slice(0,2).toLowerCase();if(n==='ca'||n==='gl'||n==='eu')n='es';return L.indexOf(n)>=0?n:'en'}
function set(l){h.setAttribute('data-lang',l);h.lang=l;try{localStorage.setItem('mjc-lang',l)}catch(e){}
document.querySelectorAll('nav.langs button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.set===l)});
var t=document.querySelector('meta[name=t-'+l+']');if(t)document.title=t.content}
set(pick());document.addEventListener('click',function(e){var b=e.target.closest('[data-set]');if(b)set(b.dataset.set)})})();
