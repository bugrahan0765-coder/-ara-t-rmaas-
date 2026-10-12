import json, sys, re, threading
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, '.')
import tt

src, out = sys.argv[1], sys.argv[2]
apps = json.load(open(src))
done = set()
try:
    for l in open(out):
        done.add(json.loads(l)['id'])
except FileNotFoundError:
    pass
lock = threading.Lock()
f = open(out, 'a')


def work(item):
    i, a = item
    name = a['name']; url = a.get('url', '')
    base = re.split(r'[:\-–|—]', name)[0].strip(); slug = tt.norm(base)
    cands = []
    if url:
        cands += re.findall(r'tiktok\.com/@([A-Za-z0-9._]+)', tt.get(url))[:2]
    nsite = len(cands)
    if len(slug) >= 3:
        cands += [slug + 'app', slug + '.app', slug, slug + '.ai']
    res = None; seen = set()
    for k, h in enumerate(cands):
        if h.lower() in seen:
            continue
        seen.add(h.lower())
        v = tt.embed(h)
        if not v:
            continue
        u = v['userInfo']
        if k >= nsite and slug[:5] not in tt.norm(u.get('nickname', '') + u.get('signature', '') + u.get('uniqueId', '')):
            continue
        res = tt.stats(v); res['src'] = 'site' if k < nsite else 'guess'
        break
    with lock:
        f.write(json.dumps({'id': i, 'name': name, 'tt': res}) + '\n'); f.flush()


with ThreadPoolExecutor(8) as ex:
    list(ex.map(work, [(i, a) for i, a in apps.items() if i not in done]))
