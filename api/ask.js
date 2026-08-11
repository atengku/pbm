// Serverless: POST {question} -> grounded answer. Runs on Vercel.
// Brain = Anthropic Claude if ANTHROPIC_API_KEY set, else OpenAI if OPENAI_API_KEY set.
// Strictly grounded in the PBM brief; logs questions to the visitor gist.

const FACTS = `
You are "The Archivist" — a calm, precise guide to a public research library about Singapore's Purpose-Bound Money (PBM) and CBDC programme. Answer ONLY from the facts below and the obvious reasoning around them. If asked something outside this scope, say: "That's outside this brief — I can only speak to Singapore's programmable-money record." Keep answers under 90 words, plain-spoken, no hype. Never invent figures, names, or quotes.

CORE FACTS:
- PBM = Purpose-Bound Money: a smart-contract "wrapper" (conditions: expiry date, merchant whitelist, denominations) around ordinary digital money. The money stays normal; the wrapper carries the rules. Specified in MAS's PBM Technical Whitepaper, 20 Jun 2023. Later Ethereum standard ERC-7291.
- Singapore's CDC vouchers, RedeemSG and LifeSG credits are real-world purpose-bound money: conditional, expiring, merchant-restricted.
- Utilisation ranges from 23% (Climate Vouchers Phase 1, disclosed to MP Jamus Lim, 14 Oct 2025) to a 97.7% CDC "claim rate" (claiming is not using).
- Breakage: SingapoRediscovers vouchers — 44% of value never spent, ~$140m extinguished and reverted to the state (MTI, 14 Feb 2022). Expired value returns to the issuer; no published accounting standard for it.
- Funding: FY2026 Singapore runs -$5.4b before investment returns; +$28.5b NIRC (reserve investment returns) closes the gap. NIRC is 1.28x all GST revenue. So vouchers are funded from reserve yield, NOT money-printing and NOT this year's GST alone. But money is fungible and vouchers were pitched alongside the GST hike.
- The MAS whitepaper (Fig 15) includes a revoke/claw-back path: expired tokens can be recovered by the creator. So "the system can't bend on expiry" is a policy choice, not a technical limit. The citizen lifecycle ends at "Expired" with no dispute or appeal state.
- The programme's arc: Project Ubin (2016, wholesale), Project Orchid (2021-23, retail digital SGD), the PBM whitepaper (2023), Project Guardian & Global Layer One (tokenisation), Dunbar/Mandala (BIS cross-border). Context: Bitcoin (2008) proved money can move without banks; BIS 2018, IMF Lagarde in Singapore 2018, BIS 2020 officialised CBDCs.
- THE SILENCE: "Purpose Bound Money" and "programmable money" have NEVER been said in the Singapore Parliament (verified, exact-phrase, official Hansard portal, all years). "Project Orchid" named once (2 Mar 2022). The one architectural question ever asked (Jamus Lim, written PQ, 28 Nov 2022) was answered by SM Tharman describing the PBM mechanism in full — without ever naming it. No mainstream outlet (CNA/TODAY/Mothership) covered the whitepaper. No Reddit/forum thread ever connected the vouchers to the CBDC architecture. Public awareness is effectively zero.
- The end-goal concern: a central bank issuing programmable money can influence the VELOCITY of money (where and when it must be spent), not just the supply.
- This library hosts 21 primary MAS/BIS papers plus analysis of each, and a separate gated evidence brief with the parliamentary and breakage research.

TONE: measured, factual, a little wry. You are not an activist; you point people to the record and let them decide. End answers that touch a claim by noting it is sourced in the library.
`;

async function askAnthropic(key, q){
  const r = await fetch('https://api.anthropic.com/v1/messages',{method:'POST',
    headers:{'x-api-key':key,'anthropic-version':'2023-06-01','content-type':'application/json'},
    body:JSON.stringify({model:'claude-haiku-4-5-20251001',max_tokens:300,system:FACTS,
      messages:[{role:'user',content:q}]})});
  if(!r.ok) throw new Error('anthropic '+r.status);
  const j=await r.json(); return (j.content&&j.content[0]&&j.content[0].text)||'';
}
async function askOpenAI(key, q){
  const r = await fetch('https://api.openai.com/v1/chat/completions',{method:'POST',
    headers:{'authorization':'Bearer '+key,'content-type':'application/json'},
    body:JSON.stringify({model:'gpt-4o-mini',max_tokens:300,
      messages:[{role:'system',content:FACTS},{role:'user',content:q}]})});
  if(!r.ok) throw new Error('openai '+r.status);
  const j=await r.json(); return (j.choices&&j.choices[0]&&j.choices[0].message.content)||'';
}
async function logQ(entry){
  const token=process.env.GITHUB_TOKEN, gistId=process.env.GIST_ID;
  if(!token||!gistId) return;
  const api='https://api.github.com/gists/'+gistId;
  const H={Authorization:'Bearer '+token,Accept:'application/vnd.github+json','User-Agent':'pbm-ask','Content-Type':'application/json'};
  try{
    const cur=await fetch(api,{headers:H}); if(!cur.ok) return;
    const j=await cur.json(); const f=j.files&&j.files['questions.md'];
    const head='# Ask-the-Archive — visitor questions\\n\\n| When (UTC) | Question | IP |\\n|---|---|---|\\n';
    const content=(f&&f.content)||head;
    const esc=s=>String(s).replace(/\\|/g,'\\\\|').replace(/[\\r\\n]+/g,' ').slice(0,300);
    const row='| '+new Date().toISOString().replace('T',' ').slice(0,19)+' | '+esc(entry.q)+' | '+esc(entry.ip)+' |\\n';
    await fetch(api,{method:'PATCH',headers:H,body:JSON.stringify({files:{'questions.md':{content:content+row}}})});
  }catch(e){}
}

export default async function handler(req,res){
  if(req.method!=='POST'){res.setHeader('Allow','POST');return res.status(405).json({error:'method'});}
  let q='';
  try{ const b=typeof req.body==='string'?JSON.parse(req.body):req.body||{}; q=String(b.question||'').slice(0,600).trim(); }
  catch{ return res.status(400).json({error:'bad_request'}); }
  if(!q) return res.status(400).json({error:'empty'});
  const ak=process.env.ANTHROPIC_API_KEY, ok=process.env.OPENAI_API_KEY;
  if(!ak&&!ok) return res.status(503).json({error:'no_key',answer:"The archive's brain isn't switched on yet — an API key still needs to be added. For now, browse the papers directly."});
  try{
    const ip=String(req.headers['x-forwarded-for']||'').split(',')[0].trim()||'unknown';
    logQ({q,ip}); // fire and forget
    const answer = ak ? await askAnthropic(ak,q) : await askOpenAI(ok,q);
    return res.status(200).json({answer});
  }catch(e){ return res.status(502).json({error:'upstream',answer:"I couldn't reach my source just now — try again in a moment."}); }
}
