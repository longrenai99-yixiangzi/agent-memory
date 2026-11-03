// Uses the installed browser/runtime; no model call or dependency installation.
const {chromium}=require('C:/Users/liu/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const {pathToFileURL}=require('node:url');
(async()=>{
  const browser=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true,args:['--disable-gpu','--disable-dev-shm-usage']});
  try {
    const page=await browser.newPage({viewport:{width:1760,height:1160},deviceScaleFactor:1});
    for(const name of ['SC04_camera-route_v1','SC05_camera-route_v1','SC06_camera-route_v1']){
      await page.goto(pathToFileURL(__dirname+'/'+name+'.svg').href);
      await page.screenshot({path:__dirname+'/'+name+'.png',timeout:20000,animations:'disabled'});
    }
    await page.goto(pathToFileURL(__dirname+'/index.html').href);
    const broken=await page.locator('img').evaluateAll(xs=>xs.filter(x=>!x.complete||!x.naturalWidth).length);
    if(broken)throw new Error('Broken review images: '+broken);
    console.log('3 PNGs rendered; HTML images loaded');
  } finally { await browser.close(); }
})().catch(e=>{console.error(e.message);process.exit(1)});
