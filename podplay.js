/* Two-host read-aloud, shared by the analysis pages and the listings.
 *
 * The scripts are marked up as `Host A:` / `Host B:` turns. Reading the
 * paragraph's raw textContent speaks those labels out loud - "Host A colon" -
 * in a single voice, which is worse than no audio at all. This splits on the
 * markers, drops them, and alternates two distinct voices so it sounds like
 * the conversation it is.
 *
 * Browser speech is the fallback. When a recorded episode exists for a page,
 * pods.json carries its path in `mp3` and the <audio> element takes over.
 *
 *   window.SAAPod.play(scriptText, buttonElement)
 *   window.SAAPod.stop()
 */
(function () {
  'use strict';
  if (window.SAAPod) return;

  var TURN = /Host\s+([AB])\s*:\s*/i;
  var TURN_G = /Host\s+([AB])\s*:\s*/gi;
  var current = null;

  function usVoices() {
    var all = window.speechSynthesis ? speechSynthesis.getVoices() : [];
    var us = all.filter(function (v) {
      return /en[-_]US/.test(v.lang) && !/GB|UK|Australia|India/.test(v.name);
    });
    return us.length ? us : all;
  }

  // Two voices that are actually different from each other. Named female
  // first, named male second, then anything rather than nothing.
  function pair() {
    var vs = usVoices();
    function find(re) { return vs.filter(function (v) { return re.test(v.name); })[0]; }
    var a = find(/Samantha|Jenny|Aria|Ava|Michelle|Zira|Google US English/) || vs[0];
    var b = find(/Guy|Eric|Christopher|Brian|Roger|David|Mark|Alex/) ||
            vs.filter(function (v) { return v !== a; })[0] || a;
    return [a, b];
  }

  /* [{who,text}] with the markers removed. Any lead-in before the first
     marker belongs to A, which is how the pages read on screen. */
  function turns(script) {
    if (!TURN.test(script)) return [{ who: 'A', text: script }];
    var parts = script.split(TURN_G);
    var out = [];
    var lead = (parts[0] || '').trim();
    if (lead) out.push({ who: 'A', text: lead });
    for (var i = 1; i < parts.length - 1; i += 2) {
      var who = (parts[i] || 'A').toUpperCase();
      var text = (parts[i + 1] || '').trim();
      if (!text) continue;
      if (out.length && out[out.length - 1].who === who) {
        out[out.length - 1].text += ' ' + text;
      } else {
        out.push({ who: who, text: text });
      }
    }
    return out;
  }

  function reset() {
    try { speechSynthesis.cancel(); } catch (e) {}
    if (current && current.btn) {
      current.btn.classList.remove('on', 'saa-playing');
      if (current.label !== undefined) current.btn.innerHTML = current.label;
    }
    current = null;
  }

  function play(script, btn) {
    if (!window.speechSynthesis) return false;
    if (current && current.script === script) { reset(); return false; }
    reset();

    var seq = turns(script);
    var vo = pair();
    current = { script: script, btn: btn, label: btn ? btn.innerHTML : undefined };
    if (btn) { btn.classList.add('on', 'saa-playing'); btn.innerHTML = '&#9632;'; }

    var i = 0;
    (function next() {
      if (!current || i >= seq.length) { reset(); return; }
      var t = seq[i++];
      var u = new SpeechSynthesisUtterance(t.text);
      var v = t.who === 'B' ? vo[1] : vo[0];
      if (v) u.voice = v;
      // A touch of separation between the hosts even when only one voice
      // is available, so the turns do not run together.
      u.rate = t.who === 'B' ? 1.0 : 1.04;
      u.pitch = t.who === 'B' ? 0.94 : 1.06;
      u.onend = next;
      u.onerror = function () { reset(); };
      speechSynthesis.speak(u);
    })();
    return true;
  }

  // Voice lists load asynchronously in most browsers.
  if (window.speechSynthesis && speechSynthesis.onvoiceschanged !== undefined) {
    speechSynthesis.onvoiceschanged = function () { usVoices(); };
  }
  window.addEventListener('beforeunload', reset);

  window.SAAPod = { play: play, stop: reset, turns: turns };
})();
