import json,re,urllib.request,time,statistics
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36"}
def get(u,t=15):
    for a in range(2):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=t).read().decode('utf-8','ignore')
        except Exception: time.sleep(1)
    return ''
def embed(h):
    s=get(f"https://www.tiktok.com/embed/@{h}")
    m=re.search(r'<script[^>]*id="__FRONTITY_CONNECT_STATE__"[^>]*>(.*?)</script>',s,re.S)
    if not m: return None
    try: d=json.loads(m.group(1))['source']['data']
    except Exception: return None
    for k,v in d.items():
        if k.startswith('/embed/@') and v.get('userInfo',{}).get('uniqueId'):
            return v
    return None
def stats(v):
    u=v['userInfo']; vl=v.get('videoList') or []
    pc=[x.get('playCount',0) for x in vl]
    ts=[int(x['id'])>>32 for x in vl if x.get('id','').isdigit()]
    span=(max(ts)-min(ts))/86400 if len(ts)>1 else 0
    slides=sum(1 for x in vl if 'photomode' in (x.get('coverUrl') or ''))
    now=time.time()
    return dict(handle=u['uniqueId'],nick=u.get('nickname',''),bio=u.get('signature','')[:120],fol=u.get('followerCount',0),hearts=u.get('heartCount',0),
        n=len(vl),med=int(statistics.median(pc)) if pc else 0,mx=max(pc) if pc else 0,slides=slides,
        posts_wk=round(len(ts)/max(span/7,0.14),1) if span else 0, last_days=round((now-max(ts))/86400) if ts else None,
        top_desc=(max(vl,key=lambda x:x.get('playCount',0)).get('desc','')[:100] if vl else ''))
def norm(x): return re.sub(r'[^a-z0-9]','',x.lower())
def find(name,url):
    base=re.split(r'[:\-–|—]',name)[0].strip(); slug=norm(base)
    cands=[]
    if url:
        m=re.findall(r'tiktok\.com/@([A-Za-z0-9._]+)',get(url))
        cands+= [x for x in m if x.lower() not in ('tiktok',)][:2]
    if len(slug)>=3: cands+=[slug+'app',slug+'.app',slug,slug+'_app','get'+slug,slug+'.ai',slug+'ai',slug+'hq']
    seen=set()
    for i,h in enumerate(cands):
        if h.lower() in seen: continue
        seen.add(h.lower())
        v=embed(h)
        if not v: continue
        u=v['userInfo']
        fromsite = i < len(cands)-8 if len(slug)>=3 else True
        if not fromsite and slug[:5] not in norm(u.get('nickname','')+u.get('signature','')+u.get('uniqueId','')): continue
        st=stats(v); st['src']='site' if fromsite else 'guess'; return st
    return None
