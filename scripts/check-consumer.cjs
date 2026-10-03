const fs=require('fs'),vm=require('vm'),assert=require('assert');
const elements=new Map();const get=s=>{if(!elements.has(s))elements.set(s,{innerHTML:'',textContent:'',style:{},value:'',dataset:{},classList:{toggle(){}},query:{value:''}});return elements.get(s)};
let registered;
const context=vm.createContext({document:{querySelector:get,querySelectorAll:()=>[],modelContext:{registerTool:t=>{registered=t;return Promise.resolve()}}},location:{hash:'#home'},window:{addEventListener(){},scrollTo(){}},crypto:require('crypto').webcrypto,Date,console,setTimeout:()=>{}});
const path=require('path'), root=path.resolve(__dirname,'..');
const source=process.argv.includes('--offline')?fs.readFileSync(path.join(root,'releases/마인갤러리-소비자웹-오프라인.html'),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1]:fs.readFileSync(path.join(root,'consumer-web/dist/app.js'),'utf8');
vm.runInContext(source,context);
const run=s=>vm.runInContext(s,context);
assert(get('#app').innerHTML.includes('나의 새로운 경험'));
run("filters.category='미술·공예'");assert.equal(run('matches().length'),1);
run("filters.q='없는체험'");assert.equal(run('matches().length'),0);
run('reset()');run("detail('pottery')");get('#date').value=run('localDate(3)');get('#time').value='14:00';get('#people').value='2';get('#reserve').onsubmit({preventDefault(){}});
assert.equal(run('draft.people'),2);run('checkout()');get('#name').value='<테스트>';get('#checkout').onsubmit({preventDefault(){}});
assert.equal(run('bookings.length'),1);assert.equal(run('bookings[0].total'),90000);
run('booking(bookings[0].id)');assert(get('#app').innerHTML.includes('&lt;테스트&gt;'));
run('cancel(bookings[0].id)');get('#cancel-form').onsubmit({preventDefault(){}});assert.equal(run('bookings[0].refund'),90000);assert.equal(run('bookings[0].status'),'cancelled');
for(const route of ['home','explore','bookings','profile','login','signup','help','policy','recover','unknown']){context.location.hash='#'+route;run('render()');assert(get('#app').innerHTML.length>20)}
(async()=>{const result=await registered.execute({query:'도자기'});assert.equal(result.results.length,1);await assert.rejects(()=>registered.execute({category:'invalid'}));console.log('PASS: categories, empty search, booking amount, escaping, cancellation/refund, 10 routes, WebMCP valid/invalid inputs.');})();
