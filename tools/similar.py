"""TF-IDF cosine over name+description (+ first 300 body words) -> candidate duplicate pairs per pack."""
import json, math, os, re, sys
from collections import Counter, defaultdict
R = sys.argv[1]; TH = float(sys.argv[2]) if len(sys.argv) > 2 else 0.35
inv = json.load(open(os.path.join(R, "tools", "inventory.json"), encoding="utf-8"))
STOP = set("the a an and or of to for in on with use when this that is are be by as from your you it its into via any all using skill skills claude code agent".split())
def toks(s):
    return [w for w in re.findall(r"[a-z][a-z0-9+]{2,}", s.lower()) if w not in STOP]
docs = []
for s in inv:
    body = open(os.path.join(R, s["dom"], s["owner"], s["name"], "SKILL.md"), encoding="utf-8", errors="ignore").read()
    words = toks(s["name"].replace("-", " ")) * 4 + toks(s["desc"]) * 2 + toks(" ".join(body.split()[:300]))
    docs.append(Counter(words))
df = Counter(w for d in docs for w in d)
N = len(docs)
vecs = []
for d in docs:
    v = {w: (1 + math.log(c)) * math.log(N / df[w]) for w, c in d.items()}
    n = math.sqrt(sum(x * x for x in v.values())) or 1
    vecs.append({w: x / n for w, x in v.items()})
pairs = []
for i in range(N):
    for j in range(i + 1, N):
        a, b = vecs[i], vecs[j]
        if len(a) > len(b): a, b = b, a
        sim = sum(x * b.get(w, 0) for w, x in a.items())
        if sim >= TH:
            pairs.append((round(sim, 2), i, j))
pairs.sort(reverse=True)
# union-find clusters
par = list(range(N))
def f(x):
    while par[x] != x: par[x] = par[par[x]]; x = par[x]
    return x
for _, i, j in pairs: par[f(i)] = f(j)
cl = defaultdict(list)
for i in range(N): cl[f(i)].append(i)
res = [[f"{inv[i]['dom'][:2]} {inv[i]['owner']}/{inv[i]['name']} ({inv[i]['lines']}l,{inv[i]['nfiles']}f)" for i in m] for m in cl.values() if len(m) > 1]
res.sort(key=len, reverse=True)
json.dump(res, open(os.path.join(R, "tools", "clusters.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(pairs), "pairs,", len(res), "clusters, sizes", [len(c) for c in res][:15])
