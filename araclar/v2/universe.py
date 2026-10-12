import json,urllib.request,time,sys
G={'Books':6018,'Business':6000,'Education':6017,'Entertainment':6016,'Finance':6015,'Food':6023,'Health':6013,'Lifestyle':6012,'Medical':6020,'Music':6011,'Navigation':6010,'News':6009,'Photo':6008,'Productivity':6007,'Reference':6006,'Shopping':6024,'Social':6005,'Sports':6004,'Travel':6003,'Utilities':6002,'Weather':6001,'Graphics':6027}
CC=['us','gb','de','fr','es','it','nl','br','mx','ca','au','tr']
out={}
def get(u):
    for a in range(4):
        try: return json.loads(urllib.request.urlopen(u,timeout=25).read())
        except Exception: time.sleep(2+a*2)
    return {}
for cc in CC:
    for gn,g in G.items():
        for kind in ['topgrossingapplications','topfreeapplications']:
            d=get(f"https://itunes.apple.com/{cc}/rss/{kind}/limit=200/genre={g}/json")
            for i,e in enumerate(d.get('feed',{}).get('entry',[]) or [],1):
                aid=e['id']['attributes']['im:id']
                a=out.setdefault(aid,{'name':e['im:name']['label'],'artist':e['im:artist']['label'],'rd':e['im:releaseDate']['label'][:10],'genre':gn,'free':{},'gross':{}})
                a['gross' if 'gross' in kind else 'free'][f"{cc}-{gn}"]=i
            time.sleep(0.15)
    print(cc,len(out),flush=True,file=sys.stderr)
json.dump(out,open('universe.json','w'))
