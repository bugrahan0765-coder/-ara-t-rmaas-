import json,urllib.request,time
G={'Books':6018,'Education':6017,'Entertainment':6016,'Finance':6015,'Food':6023,'Health':6013,'Lifestyle':6012,'Medical':6020,'Music':6011,'Navigation':6010,'Photo':6008,'Productivity':6007,'Reference':6006,'Shopping':6024,'Social':6005,'Sports':6004,'Travel':6003,'Utilities':6002,'Graphics':6027,'Business':6000}
def get(u):
    for a in range(4):
        try: return json.loads(urllib.request.urlopen(u,timeout=25).read())
        except Exception: time.sleep(2+2*a)
    return {}
apps={}
for gn,g in G.items():
    d=get(f"https://itunes.apple.com/us/rss/topgrossingapplications/limit=200/genre={g}/json")
    for i,e in enumerate(d.get('feed',{}).get('entry',[]) or [],1):
        rd=e['im:releaseDate']['label'][:10]
        if rd>='2025-01-01' and i<=150:
            apps[e['id']['attributes']['im:id']]={'name':e['im:name']['label'][:40],'rd':rd,'g':gn,'usgross':i}
ids=list(apps); print('young US grossing',len(ids),flush=True)
CC=['us','gb','de','fr','es','it','nl','mx','br','tr','jp','kr']
for cc in CC:
    for k in range(0,len(ids),100):
        L=get(f"https://itunes.apple.com/lookup?id={','.join(ids[k:k+100])}&country={cc}").get('results',[])
        for x in L:
            a=apps[str(x['trackId'])]; a[cc]=x.get('userRatingCount',0)
            if cc=='us': a['langs']=x.get('languageCodesISO2A',[]); a['seller']=x.get('sellerName','')[:22]; a['url']=x.get('sellerUrl') or ''; a['price']=x.get('price')
        time.sleep(0.5)
json.dump(apps,open('locgap.json','w'))
rows=[]
for i,a in apps.items():
    us=a.get('us',0) or 0
    if us<300: continue
    nonen=sum(a.get(c,0) or 0 for c in ['de','fr','es','it','nl','mx','br','tr','jp','kr'])
    rows.append((nonen/us,i,a,nonen))
rows.sort(key=lambda r:-r[0])
for r,i,a,n in rows[:60]:
    print(f"{a['name']:40} | {a['g']:9} | US#{a['usgross']:<3} | {a['rd']} | US {a.get('us')} | nonEN {n} ({r:.2f}) | DE {a.get('de')} FR {a.get('fr')} ES {a.get('es')} MX {a.get('mx')} BR {a.get('br')} JP {a.get('jp')} | langs {len(a.get('langs',[]))} {','.join(a.get('langs',[]))[:20]}")
