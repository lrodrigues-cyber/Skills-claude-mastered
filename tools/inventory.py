"""Inventory every skill: frontmatter, size, resources, lint issues. -> tools/inventory.json"""
import json, os, re, sys
R = sys.argv[1]
out = []
for line in open(os.path.join(R, ".manifest"), encoding="utf-8"):
    dom, owner, name, url, kind = line.strip().split("|")
    if kind != "skill":
        continue
    p = os.path.join(R, dom, owner, name)
    t = open(os.path.join(p, "SKILL.md"), encoding="utf-8", errors="ignore").read()
    fm = re.match(r"^---\s*\n(.*?)\n---\s*\n", t, re.S)
    meta = {}
    if fm:
        for k in ("name", "description"):
            m = re.search(rf"^{k}:\s*(.+?)(?=\n[a-zA-Z_-]+:|\Z)", fm.group(1), re.S | re.M)
            meta[k] = re.sub(r"\s+", " ", m.group(1)).strip().strip("\"'>|- ") if m else ""
    body = t[fm.end():] if fm else t
    files = [os.path.relpath(os.path.join(a, f), p).replace("\\", "/") for a, _, fs in os.walk(p) for f in fs]
    refs = set(re.findall(r"\]\(((?!https?:|#|mailto:)[^)\s]+)\)", body)) | set(re.findall(r"`((?:references|scripts|assets|templates|examples|rules|data)/[^`\s]+)`", body))
    broken = sorted(r for r in refs if not os.path.exists(os.path.normpath(os.path.join(p, r.split("#")[0]))))
    issues = []
    if not fm: issues.append("no-frontmatter")
    if meta.get("name") and meta["name"] != name: issues.append("name-mismatch")
    if not meta.get("description"): issues.append("no-description")
    elif len(meta["description"]) > 1024: issues.append("desc>1024")
    elif len(meta["description"]) < 60: issues.append("desc-short")
    if body.count("\n") > 500: issues.append("body>500l")
    if broken: issues.append("broken-refs")
    out.append(dict(dom=dom, owner=owner, name=name, url=url, desc=meta.get("description", ""), fm_name=meta.get("name", ""),
                    lines=body.count("\n"), words=len(body.split()), nfiles=len(files), broken=broken[:10], issues=issues))
json.dump(out, open(os.path.join(R, "tools", "inventory.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
from collections import Counter
print(len(out), Counter(i for s in out for i in s["issues"]))
