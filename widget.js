/* Ask-the-Archive floating voice widget — injected on every page of mas-wp.
   Talks back with browser voice, brain = /api/ask (grounded in the PBM brief). */
(function(){
  if(window.__saaWidget) return; window.__saaWidget=1;
  var css=`
  #saaBtn{position:fixed;right:20px;bottom:20px;z-index:99998;width:60px;height:60px;border-radius:50%;
    background:#c9a24b;color:#0a0c10;border:none;cursor:pointer;font-size:26px;box-shadow:0 6px 20px rgba(0,0,0,.45);
    display:flex;align-items:center;justify-content:center;transition:transform .15s}
  #saaBtn:hover{transform:scale(1.07)}
  #saaBtn .pulse{position:absolute;inset:0;border-radius:50%;box-shadow:0 0 0 0 rgba(201,162,75,.6);animation:saapulse 2.2s infinite}
  @keyframes saapulse{70%{box-shadow:0 0 0 16px rgba(201,162,75,0)}100%{box-shadow:0 0 0 0 rgba(201,162,75,0)}}
  #saaPanel{position:fixed;right:20px;bottom:92px;z-index:99999;width:min(380px,calc(100vw - 40px));height:min(560px,70vh);
    background:#12161d;border:1px solid #232c38;border-radius:16px;box-shadow:0 12px 40px rgba(0,0,0,.55);
    display:none;flex-direction:column;overflow:hidden;font-family:Inter,system-ui,sans-serif}
  #saaPanel.open{display:flex}
  #saaHead{background:#0a0c10;border-bottom:1px solid #232c38;padding:14px 16px;display:flex;align-items:center;justify-content:space-between}
  #saaHead .t{font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#c9a24b}
  #saaHead .x{background:none;border:none;color:#8c98a8;font-size:20px;cursor:pointer;line-height:1}
  #saaLog{flex:1;overflow-y:auto;padding:14px;display:flex;flex-direction:column;gap:10px}
  .saaMsg{max-width:88%;padding:10px 13px;border-radius:12px;font-size:14px;line-height:1.5;color:#e8edf4}
  .saaMe{align-self:flex-end;background:#1d2a3a;border:1px solid #2c3f57}
  .saaAi{align-self:flex-start;background:#161c24;border:1px solid #232c38}
  .saaAi .who{font-family:'IBM Plex Mono',ui-monospace,monospace;font-size:9px;letter-spacing:.14em;text-transform:uppercase;color:#c9a24b;margin-bottom:4px}
  .saaSpk{cursor:pointer;color:#8c98a8;font-size:11px;margin-top:5px;display:inline-block}
  .saaSpk:hover{color:#c9a24b}
  #saaChips{display:flex;gap:6px;flex-wrap:wrap;padding:0 14px 8px}
  .saaChip{font-size:11.5px;color:#e5c877;border:1px solid #232c38;border-radius:16px;padding:5px 9px;cursor:pointer;background:#0f1319}
  .saaChip:hover{border-color:#c9a24b}
  #saaBar{display:flex;gap:8px;align-items:center;border-top:1px solid #232c38;padding:12px}
  #saaQ{flex:1;background:#05060a;border:1px solid #232c38;border-radius:9px;padding:11px 12px;color:#e8edf4;font-size:14px;font-family:inherit;outline:none}
  #saaQ:focus{border-color:#c9a24b}
  #saaSend{background:#c9a24b;color:#0a0c10;border:none;border-radius:9px;padding:11px 13px;font-weight:650;cursor:pointer;font-family:inherit;font-size:13px}
  #saaMic{background:#0f1319;color:#e5c877;border:1px solid #232c38;border-radius:9px;padding:11px;cursor:pointer;font-size:16px;width:44px}
  #saaMic.live{background:#c9a24b;color:#0a0c10;animation:saapulse 1s infinite}`;
  var st=document.createElement('style'); st.textContent=css; document.head.appendChild(st);

  var btn=document.createElement('button'); btn.id='saaBtn'; btn.title='Ask the Archive'; btn.innerHTML='<span class="pulse"></span>✦';
  var panel=document.createElement('div'); panel.id='saaPanel';
  panel.innerHTML=''
   +'<div id="saaHead"><span class="t">✦ Ask the Archive</span><button class="x" title="Close">×</button></div>'
   +'<div id="saaLog"></div>'
   +'<div id="saaChips">'
     +'<span class="saaChip">Are the vouchers programmable money?</span>'
     +'<span class="saaChip">Where does the money come from?</span>'
     +'<span class="saaChip">Did Parliament ever debate this?</span>'
     +'<span class="saaChip">Who profits from this?</span>'
   +'</div>'
   +'<div id="saaBar"><button id="saaMic" title="Talk">🎙️</button>'
     +'<input id="saaQ" placeholder="Ask about this page or anything…" autocomplete="off">'
     +'<button id="saaSend">Ask</button></div>';
  document.body.appendChild(btn); document.body.appendChild(panel);

  var log=panel.querySelector('#saaLog'), q=panel.querySelector('#saaQ'),
      send=panel.querySelector('#saaSend'), mic=panel.querySelector('#saaMic'),
      chips=panel.querySelector('#saaChips'), closeb=panel.querySelector('.x');
  var greeted=false, voiceOn=true;
  function open(){ panel.classList.add('open'); if(!greeted){greeted=true;
    add("Hi — I can talk you through anything on Singapore's programmable-money record. Tap the mic and just ask.",'ai',false);} q.focus(); }
  function close(){ panel.classList.remove('open'); try{speechSynthesis.cancel();}catch(e){} }
  btn.onclick=function(){ panel.classList.contains('open')?close():open(); };
  closeb.onclick=close;
  function speak(t){ try{ if(!voiceOn)return; speechSynthesis.cancel(); var u=new SpeechSynthesisUtterance(t); u.rate=1.02;
    var vs=speechSynthesis.getVoices(); var p=vs.find(function(v){return /en-GB|Google UK|Daniel|Serena|Samantha/.test(v.name+v.lang)}); if(p)u.voice=p; speechSynthesis.speak(u);}catch(e){} }
  function add(text,who,speakable){ var d=document.createElement('div'); d.className='saaMsg '+(who==='me'?'saaMe':'saaAi');
    if(who==='ai'){ d.innerHTML='<div class="who">The Archivist</div>'+String(text).replace(/</g,'&lt;'); } else d.textContent=text;
    log.appendChild(d);
    if(who==='ai'&&speakable){ var s=document.createElement('span'); s.className='saaSpk'; s.textContent='🔊 replay'; s.onclick=function(){speak(text);}; d.appendChild(document.createElement('br')); d.appendChild(s); }
    log.scrollTop=log.scrollHeight; return d; }
  function ask(text){ if(!text||!text.trim())return; add(text,'me'); q.value='';
    var t=add('…','ai',false);
    fetch('/api/ask',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({question:text})})
      .then(function(r){return r.json();}).then(function(j){ var a=j.answer||'(no answer)';
        t.innerHTML='<div class="who">The Archivist</div>'+a.replace(/</g,'&lt;');
        var s=document.createElement('span'); s.className='saaSpk'; s.textContent='🔊 replay'; s.onclick=function(){speak(a);};
        t.appendChild(document.createElement('br')); t.appendChild(s); speak(a); log.scrollTop=log.scrollHeight; })
      .catch(function(){ t.innerHTML='<div class="who">The Archivist</div>Something went wrong — try again.'; });
  }
  send.onclick=function(){ ask(q.value); };
  q.addEventListener('keydown',function(e){ if(e.key==='Enter')ask(q.value); });
  chips.addEventListener('click',function(e){ if(e.target.classList.contains('saaChip'))ask(e.target.textContent); });
  var SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  if(SR){ var rec=new SR(); rec.lang='en-SG'; rec.interimResults=false; rec.maxAlternatives=1;
    mic.onclick=function(){ try{ speechSynthesis.cancel(); mic.classList.add('live'); rec.start(); }catch(e){} };
    rec.onresult=function(e){ mic.classList.remove('live'); ask(e.results[0][0].transcript); };
    rec.onerror=function(){ mic.classList.remove('live'); }; rec.onend=function(){ mic.classList.remove('live'); };
  } else { mic.style.display='none'; }
  try{ speechSynthesis.getVoices(); }catch(e){}
})();
