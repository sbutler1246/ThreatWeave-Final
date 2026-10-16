// Offline DOM simulation: tests UI state without a browser or network.
const fs=require('node:fs');const vm=require('node:vm');const assert=require('node:assert/strict');
for(const path of process.argv.slice(2)){
 const html=fs.readFileSync(path,'utf8');
 const packetText=html.match(/<script id="packet" type="application\/json">([\s\S]*?)<\/script>/)[1];
 const packet=JSON.parse(packetText);const script=html.match(/<\/script><script>([\s\S]*?)<\/script>/)[1];
 const elements=new Map(),storage=new Map();
 const el=id=>{if(!elements.has(id))elements.set(id,{value:'',textContent:'',innerHTML:'',style:{},disabled:false,addEventListener(){}});return elements.get(id);};
 el('packet').textContent=packetText;
 const context=vm.createContext({document:{getElementById:el,createElement:()=>({click(){}})},localStorage:{getItem:k=>storage.get(k),setItem:(k,v)=>storage.set(k,v)},Blob,URL,setTimeout:()=>{}});
 vm.runInContext(script,context);
 const run=code=>vm.runInContext(code,context);
 assert.equal(packet.items.length,packet.kind==='primary'?80:20);
 assert.equal(el('finish').disabled,true);assert.equal(el('progress').value,0);
 assert.equal(el('question').textContent,packet.items[0].question);
 assert.equal(run('Object.values(state.ratings).every(r=>dimensions.every(d=>r[d]===""))'),true);
 assert.equal(run('complete({factuality:"NA",completeness:"NA",coherence:"NA",reason:""})'),false);
 assert.equal(run('complete({factuality:"NA",completeness:"NA",coherence:"NA",reason:"No valid answer"})'),true);
 for(const item of packet.items)for(const key of ['mode','repeat','case_id','question_id','automated_scores'])assert.equal(Object.hasOwn(item,key),false);
 el('factuality').value='4';el('completeness').value='3';el('coherence').value='5';run('capture()');
 assert.equal(run('documentValue().ratings[0].factuality'),4);assert.equal(run('documentValue().ratings[0].entry_complete'),true);
 assert.equal(run('documentValue().review_status'),'in_progress');assert.equal(el('finish').disabled,true);
 const exported=run('JSON.stringify(documentValue())');run('restore(JSON.parse('+JSON.stringify(exported)+'))');
 el('next').onclick();assert.equal(el('question').textContent,packet.items[1].question);
 el('previous').onclick();assert.equal(el('factuality').value,'4');
 assert.throws(()=>run('restore({packet_fingerprint:"wrong",packet_kind:packet.kind})'));
 run('for(const r of Object.values(state.ratings)){r.factuality="NA";r.completeness="NA";r.coherence="NA";r.reason="Test-only missing answer";} state.reviewer="Test Reviewer";status();');
 assert.equal(el('finish').disabled,packet.kind==='secondary');
 if(packet.kind==='secondary'){run('state.secondary_method="independent";status();');assert.equal(el('finish').disabled,false);}
 assert.equal(run('documentValue(true).review_status'),'completed');
 assert.equal(run('documentValue(true).ratings.every(r=>r.entry_complete && r.factuality===null)'),true);
 console.log('FORM CHECK PASSED:',packet.kind,'blank ratings, blinding, navigation state, N/A reasons, persistence, identity gate, completed export.');
}
