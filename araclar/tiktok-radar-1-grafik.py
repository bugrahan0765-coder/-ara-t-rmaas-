# TikTok organik radar, adım 1: ABD ve GB kategori 'top free' listelerinden 2025-06 sonrası çıkan uygulamaları toplar,
# sitelerinden TikTok hesabını bulur, takipçi, kalp ve video sayılarını çeker. Kullanım: python3 -I tiktok-radar-1-grafik.py > radar.jsonl
import json,urllib.request,time,re,sys
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
def get(u,t=20):
    for a in range(3):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=t).read().decode('utf-8','ignore')
        except Exception: time.sleep(2)
    return ''
G={'Health':6013,'Lifestyle':6012,'Food':6023,'Photo':6008,'Utilities':6002,'Education':6017,'Productivity':6007,'Shopping':6024}
seen={}
for cc in ['us','gb']:
    for gn,g in G.items():
        try: d=json.loads(get(f"https://itunes.apple.com/{cc}/rss/topfreeapplications/limit=100/genre={g}/json"))
        except Exception: continue
        for rank,e in enumerate(d['feed'].get('entry',[]),1):
            rd=e['im:releaseDate']['label'][:10]; i=e['id']['attributes']['im:id']
            if rd>='2025-06-01' and rank<=60:
                seen.setdefault(i,{'name':e['im:name']['label'][:34],'rd':rd,'hits':[]})['hits'].append(f"{cc}-{gn}#{rank}")
ids=list(seen)
for k in range(0,len(ids),50):
    try: L=json.loads(get(f"https://itunes.apple.com/lookup?id={','.join(ids[k:k+50])}&country=us"))['results']
    except Exception: L=[]
    for x in L:
        s=seen[str(x['trackId'])]; s['url']=x.get('sellerUrl') or ''; s['ratings']=x.get('userRatingCount'); s['seller']=x.get('sellerName','')[:24]
for i,s in seen.items():
    h=''
    if s.get('url'):
        m=re.search(r'tiktok\.com/@([A-Za-z0-9._]+)',get(s['url'],15))
        if m: h=m.group(1)
    f=v=hc=''
    if h:
        p=get(f"https://www.tiktok.com/@{h}")
        g=lambda k:(re.search(rf'"{k}":(\d+)',p) or [None,''])[1]
        f,hc,v=g('followerCount'),g('heartCount'),g('videoCount')
    s.update(tt=h,fol=f,hearts=hc,vids=v)
    print(json.dumps({'id':i,**s}),flush=True)
