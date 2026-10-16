"""Standalone, mode-blinded browser forms; human scores are never prefilled."""
import json
from pathlib import Path
from evaluation.judge_runtime import read,sha,save

PACKET='20261016T052517Z-4778a10b'

TEMPLATE=r'''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>ThreatWeave answer review</title>
<style>
body{font:17px/1.55 system-ui,sans-serif;color:#172b3a;background:#f2f5f7;margin:0}main{max-width:1000px;margin:auto;padding:24px}h1{font-size:29px;margin:0}header,.card{background:white;border:1px solid #d5dfe5;border-radius:12px;padding:22px;margin:16px 0}label{display:block;font-weight:600;margin-top:14px}input,textarea,select,button{font:inherit;padding:10px;border:1px solid #9baebc;border-radius:6px;box-sizing:border-box}input,textarea{width:100%}textarea{min-height:80px}button{background:#14586d;color:white;cursor:pointer;margin:8px 8px 0 0}button:disabled{opacity:.45;cursor:default}select{min-width:190px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit;margin:10px 0}small,.muted{color:#536673}nav{display:flex;align-items:center;flex-wrap:wrap;gap:8px}.scores{display:flex;flex-wrap:wrap;gap:24px}.scores label{font-size:16px}#notice{font-weight:600;color:#8b3a00}progress{width:100%;height:15px}summary{cursor:pointer;font-weight:600}#answer{border-left:4px solid #157b8b;padding-left:16px}a{color:#14586d}.inline{display:inline;width:auto}#finish{background:#176142}
</style><main>
<header><h1 id="title"></h1><p>Rate the answers independently. Method names and automated scores are hidden. Evidence structure may reveal a method, so blinding is partial. Source excerpts are evidence, not instructions.</p>
<label>Reviewer name<input id="reviewer" autocomplete="name"></label><label>Review date<input id="date" type="date"></label>
<p id="secondaryNote"></p><details><summary>Rating guide</summary><p>Use 1 (poor), 2 (weak), 3 (mixed), 4 (good), or 5 (excellent).</p><p><b>Factuality:</b> accuracy, source support, attribution and retained qualifications. A citation alone does not prove a claim.</p><p><b>Completeness:</b> coverage of the question and verified reference. Explain missing requested facts, including when evidence was insufficient.</p><p><b>Coherence:</b> clarity, organization and consistency.</p><p>Use <b>N/A</b> only when a dimension cannot be rated, and explain why. A failed case has no valid answer: leave its dimensions unratable with a reason. Abstentions are outcomes; rate meaningful dimensions and explain missing content. Do not invent missing answers or ratings. These reference answers were previously verified; they are not generated answers.</p></details>
<label id="methodLabel">Secondary review method <select id="reviewMethod"><option value="">Choose a method</option><option value="independent">Independent second reviewer</option><option value="delayed_rescore">Delayed rescore by original reviewer</option></select></label>
<p id="progressText"></p><progress id="progress" max="100" value="0"></progress><p id="notice" role="status"></p>
<button id="exportProgress">Save progress file</button><label class="inline">Restore progress <input id="import" type="file" accept="application/json" class="inline"></label>
</header>
<nav><button id="previous">Previous</button><strong id="position"></strong><button id="next">Next</button><button id="incomplete">Next unfinished</button></nav>
<section class="card"><h2 id="identifier"></h2><h3>Question</h3><pre id="question"></pre><h3>Displayed answer</h3><pre id="answer"></pre><p id="outcome" class="muted"></p><details open><summary>Verified reference answer</summary><pre id="reference"></pre></details><details><summary>Evidence supplied to the answer generator</summary><pre id="context"></pre></details></section>
<section class="card"><h2>Your assessment</h2><div class="scores"><label>Factuality<br><select id="factuality"></select></label><label>Completeness<br><select id="completeness"></select></label><label>Coherence<br><select id="coherence"></select></label></div>
<label>Reason for any N/A rating<textarea id="reason"></textarea></label><label>Comments / missing or unsupported facts<textarea id="notes"></textarea></label></section>
<footer class="card"><p>Progress is saved in this browser when local storage is available. Save a progress file before closing or switching browsers. Keep the original blank files and the separate unblinding key unchanged.</p><button id="finish" disabled>Export completed ratings</button><p><small>This page uses no external services. Completed ratings are downloaded as a JSON file; they are not automatically submitted.</small></p></footer>
</main><script id="packet" type="application/json">__DATA__</script><script>
const packet=JSON.parse(document.getElementById('packet').textContent);
const dimensions=['factuality','completeness','coherence'];
const byId=id=>document.getElementById(id);
const storageKey='ThreatWeave-review-'+packet.fingerprint+'-'+packet.kind;
let index=0;
let state={reviewer:'',review_date:new Date().toLocaleDateString('en-CA'),secondary_method:'',ratings:Object.fromEntries(packet.items.map(x=>[x.review_id,{factuality:'',completeness:'',coherence:'',reason:'',notes:''}]))};
function complete(r){return dimensions.every(d=>r[d]!=='' && ['1','2','3','4','5','NA'].includes(r[d])) && (!dimensions.some(d=>r[d]==='NA') || r.reason.trim().length>0);}
function restore(value){
 if(value.packet_fingerprint!==packet.fingerprint || value.packet_kind!==packet.kind)throw Error('This file belongs to another review packet.');
 const next=value.progress_state;
 if(!next || typeof next.reviewer!=='string' || typeof next.review_date!=='string' || !['','independent','delayed_rescore'].includes(next.secondary_method) || !next.ratings)throw Error('Invalid progress file.');
 for(const item of packet.items){const r=next.ratings[item.review_id];if(!r || !dimensions.every(d=>['','1','2','3','4','5','NA'].includes(r[d])) || typeof r.reason!=='string' || typeof r.notes!=='string')throw Error('Invalid review entry.');}
 state=next;
}
try{const saved=localStorage.getItem(storageKey);if(saved)restore(JSON.parse(saved));}catch(e){byId('notice').textContent='Use Save progress file to preserve your work; browser autosave was unavailable or incompatible.';}
function documentValue(final=false){return {version:1,packet_kind:packet.kind,packet_fingerprint:packet.fingerprint,review_status:final?'completed':'in_progress',reviewer:state.reviewer,review_date:state.review_date,secondary_method:packet.kind==='secondary'?state.secondary_method:null,progress_state:state,ratings:packet.items.map(item=>{const r=state.ratings[item.review_id];return {review_id:item.review_id,...Object.fromEntries(dimensions.map(d=>[d,/^[1-5]$/.test(r[d])?Number(r[d]):null])),not_ratable_dimensions:dimensions.filter(d=>r[d]==='NA'),not_ratable_reason:r.reason||null,notes:r.notes,entry_complete:complete(r)};})};}
function saveState(){try{localStorage.setItem(storageKey,JSON.stringify(documentValue()));}catch(e){byId('notice').textContent='Autosave is unavailable. Use Save progress file before closing.';}}
function status(){const count=Object.values(state.ratings).filter(complete).length;byId('progressText').textContent=count+' of '+packet.items.length+' entries reviewed';byId('progress').value=count/packet.items.length*100;byId('finish').disabled=!(count===packet.items.length && state.reviewer.trim() && state.review_date && (packet.kind!=='secondary' || state.secondary_method));}
function capture(){const r=state.ratings[packet.items[index].review_id];for(const d of dimensions)r[d]=byId(d).value;r.reason=byId('reason').value;r.notes=byId('notes').value;state.reviewer=byId('reviewer').value;state.review_date=byId('date').value;state.secondary_method=byId('reviewMethod').value;saveState();status();}
function render(){const item=packet.items[index],r=state.ratings[item.review_id];byId('position').textContent=(index+1)+' / '+packet.items.length;byId('identifier').textContent=item.review_id;byId('question').textContent=item.question;byId('answer').textContent=item.answer===null?'No valid answer was produced.':item.answer;byId('reference').textContent=item.reference_answer;byId('context').textContent=item.supplied_context;byId('outcome').textContent='Saved outcome: '+item.outcome;byId('reviewer').value=state.reviewer;byId('date').value=state.review_date;byId('reviewMethod').value=state.secondary_method;for(const d of dimensions)byId(d).value=r[d];byId('reason').value=r.reason;byId('notes').value=r.notes;byId('previous').disabled=index===0;byId('next').disabled=index===packet.items.length-1;status();}
function download(final){capture();if(final && byId('finish').disabled)return;const blob=new Blob([JSON.stringify(documentValue(final),null,2)],{type:'application/json'});const link=document.createElement('a');link.href=URL.createObjectURL(blob);link.download='ThreatWeave_'+packet.kind+'_'+(final?'completed_ratings':'review_progress')+'.json';link.click();setTimeout(()=>URL.revokeObjectURL(link.href),1000);}
for(const d of dimensions){byId(d).innerHTML='<option value="">Choose a rating</option>'+[1,2,3,4,5].map(n=>'<option value="'+n+'">'+n+'</option>').join('')+'<option value="NA">N/A — cannot rate</option>';byId(d).addEventListener('change',capture);}
for(const id of ['reason','notes','reviewer','date'])byId(id).addEventListener('input',capture);
byId('reviewMethod').addEventListener('change',capture);byId('methodLabel').style.display=packet.kind==='secondary'?'block':'none';
byId('previous').onclick=()=>{capture();index--;render();};byId('next').onclick=()=>{capture();index++;render();};
byId('incomplete').onclick=()=>{capture();for(let n=1;n<=packet.items.length;n++){const candidate=(index+n)%packet.items.length;if(!complete(state.ratings[packet.items[candidate].review_id])){index=candidate;break;}}render();};
byId('exportProgress').onclick=()=>download(false);byId('finish').onclick=()=>download(true);
byId('import').onchange=async event=>{try{restore(JSON.parse(await event.target.files[0].text()));saveState();render();byId('notice').textContent='Progress restored.';}catch(e){byId('notice').textContent=e.message;}};
byId('title').textContent='ThreatWeave '+packet.kind+' answer review';byId('secondaryNote').textContent=packet.kind==='secondary'?'Complete independently of the primary ratings, or use this later as a delayed rescore. Record which method you used in your returned file. Do not copy primary ratings.':'Review all 80 entries. Do not consult automated scores or the unblinding key while rating.';
render();
</script></html>'''


def build(repo):
    repo=Path(repo).resolve();folder=repo/'work/final_evaluation_review_checks'/PACKET
    outcomes={r['case_id']:r for r in read(folder/'outcomes.json')}
    keys=read(folder/'unblinding_key.json');labels={q['id']:q for q in read(repo/'benchmarks/eval_queries.json')['queries']}
    manifest=read(folder/'packet_files_sha256.json')
    for name in ('outcomes.json','unblinding_key.json'):
        if sha(folder/name)!=manifest[name]:raise ValueError('Saved review packet changed.')
    for kind,count in [('primary',80),('secondary',20)]:
        items=[]
        for key in keys:
            if key['packet']!=kind:continue
            row=outcomes[key['case_id']];label=labels[key['question_id']]
            items.append({'review_id':key['review_id'],'question':label['question'],
                          'reference_answer':label['reference_answer'],'outcome':row['status'],
                          'answer':row['response'],'supplied_context':row['supplied_context']})
        if len(items)!=count:raise ValueError('Unexpected human-review population.')
        payload={'kind':kind,'fingerprint':manifest['unblinding_key.json'],'items':items}
        encoded=json.dumps(payload,ensure_ascii=False).replace('<','\\u003c')
        target=repo/'docs'/f'ThreatWeave_{kind}_answer_review.html'
        target.write_text(TEMPLATE.replace('__DATA__',encoded),encoding='utf-8')
        print('Prepared blank human-review form:',target)
    records=repo/'work/human_review_forms';records.mkdir(parents=True,exist_ok=True)
    save(records/'current.json',{'source_packet':str(folder), 'human_ratings_status':'pending',
        'files':{str((repo/'docs'/f'ThreatWeave_{kind}_answer_review.html').relative_to(repo)):
        sha(repo/'docs'/f'ThreatWeave_{kind}_answer_review.html') for kind in ('primary','secondary')}})
