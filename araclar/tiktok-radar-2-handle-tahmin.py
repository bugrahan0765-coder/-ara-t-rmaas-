# TikTok organik radar, adım 2: sitesinde TikTok linki olmayan uygulamalar için handle tahmin eder (isim+app, isim.app…).
# Takma ad veya bio uygulama adını içermiyorsa eşleşmeyi atar. Yine de bio linkini elle doğrula. Girdi: aynı klasördeki radar.jsonl
import json,re,urllib.request,time
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
def get(u):
    try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=15).read().decode('utf-8','ignore')
    except Exception: return ''
for l in open('radar.jsonl'):
    r=json.loads(l)
    if r['tt']: continue
    base=re.split(r'[:\-–|]',r['name'])[0].strip()
    slug=re.sub(r'[^a-z0-9]','',base.lower())
    if len(slug)<3: continue
    for h in [slug+'app',slug+'.app',slug,slug+'_app','get'+slug]:
        p=get(f"https://www.tiktok.com/@{h}")
        m=re.search(r'"uniqueId":"%s".{0,400}?"nickname":"([^"]*)"'%re.escape(h),p) or re.search(r'"nickname":"([^"]*)".{0,400}?"uniqueId":"%s"'%re.escape(h),p)
        if not m: continue
        nick=m.group(1); bio=(re.search(r'"signature":"([^"]*)"',p) or [0,''])[1]
        if slug[:5] not in re.sub(r'[^a-z0-9]','',(nick+bio).lower()): continue
        g=lambda k:int((re.search(rf'"{k}":(\d+)',p) or [0,0])[1])
        f,hc,v=g('followerCount'),g('heartCount'),g('videoCount')
        print(f"{r['name']} | {r['rd']} | {r.get('ratings')} | {','.join(r['hits'][:2])} | @{h} '{nick}' {f} fol {v} vid {hc//max(1,v)} heart/vid",flush=True)
        break
    time.sleep(0.3)
