import json, urllib.request, time
U = json.load(open('universe.json'))
young = {}
for i, a in U.items():
    if a['rd'] < '2025-01-01':
        continue
    g = {k: v for k, v in a['gross'].items() if v <= 100}
    if not g:
        continue
    countries = sorted({k.split('-')[0] for k in g})
    best_g = min(g.values())
    # conversion: for each country-genre with both lists, gross rank minus free rank
    conv = [a['gross'][k] - a['free'][k] for k in a['gross'] if k in a['free']]
    young[i] = dict(name=a['name'][:40], artist=a['artist'][:24], rd=a['rd'], genre=a['genre'], countries=countries,
                    nc=len(countries), best_g=best_g, gross=g,
                    conv=(sorted(conv)[len(conv) // 2] if conv else None))
print('young apps in some top-100 grossing:', len(young))
json.dump(young, open('young.json', 'w'))
# apps strong outside US but absent/weak in US
nonus = [(i, y) for i, y in young.items() if 'us' not in y['countries'] and y['nc'] >= 2]
print('young winners not in US top100 grossing (>=2 countries):', len(nonus))
for i, y in sorted(nonus, key=lambda x: (-x[1]['nc'], x[1]['best_g']))[:40]:
    print(f"{y['name']:40} {y['genre'][:9]:9} {y['rd']} best#{y['best_g']:<3} conv{y['conv']} {','.join(y['countries'])}")
