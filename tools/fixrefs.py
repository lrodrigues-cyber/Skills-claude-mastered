"""Repair relative links that broke when skills were lifted out of their source repos,
and make every SKILL.md `name:` match its folder.
Usage: python -I tools/fixrefs.py <repo_dir> <src_dir>
For a missing ref, look in the original skill dir, then the source repo root; copy what is found
into the skill (refs that climb with ../ land under _shared/) and rewrite the link.
"""
import json, os, re, shutil, sys

R, S = sys.argv[1], os.path.normpath(sys.argv[2])
inv = json.load(open(os.path.join(R, "tools", "inventory.json"), encoding="utf-8"))
fixed, left, renamed = [], [], 0


def src_dir(s):
    owner, repo = s["owner"].split("/")
    sub = s["url"].split("/tree/HEAD/", 1)[1] if "/tree/HEAD/" in s["url"] else ""
    return os.path.join(S, f"{owner}_{repo}"), os.path.normpath(os.path.join(S, f"{owner}_{repo}", sub))


def copy(a, b):
    os.makedirs(os.path.dirname(b), exist_ok=True)
    (shutil.copytree(a, b, dirs_exist_ok=True) if os.path.isdir(a) else shutil.copy(a, b))


for s in inv:
    d = os.path.join(R, s["dom"], s["owner"], s["name"])
    sk = os.path.join(d, "SKILL.md")
    t = open(sk, encoding="utf-8").read()
    t2 = re.sub(r"^(---\s*\nname:\s*)(.+)$", lambda m: m.group(1) + s["name"], t, count=1, flags=re.M)
    if t2 != t:
        renamed += 1
    t = t2
    root, orig = src_dir(s)
    for ref in s["broken"]:
        if re.search(r"[<>{}*]|^link$", ref):  # placeholders / template syntax, not real paths
            continue
        rel = ref.split("#")[0].rstrip("/")
        # sibling skill link (../x/SKILL.md): point at the bundled sibling (possibly renamed ecc-x) or unlink
        m = re.match(r"\.\./([\w.-]+)/SKILL\.md$", rel)
        if m:
            sib = next((n for n in (m.group(1), "ecc-" + m.group(1)) if os.path.isfile(os.path.join(os.path.dirname(d), n, "SKILL.md"))), None)
            t = t.replace(f"]({ref})", f"](../{sib}/SKILL.md)" if sib else f"](#) <!-- sibling skill `{m.group(1)}` not bundled -->")
            fixed.append(f"{s['name']}: sibling {ref} -> {sib}")
            continue
        hit = None
        for base in (orig, root):
            cand = os.path.normpath(os.path.join(base, rel))
            if os.path.exists(cand) and cand.startswith(root):
                hit = cand
                break
        if not hit:
            left.append(f"{s['name']}: {ref}")
            continue
        if rel.startswith("../"):
            new = "_shared/" + re.sub(r"^(\.\./)+", "", rel)
            copy(hit, os.path.join(d, new))
            t = t.replace(ref.rstrip("/"), new)
        else:
            top = rel.split("/")[0]  # bring the whole top-level folder (e.g. scripts/) so helpers travel together
            base = hit[: len(hit) - len(os.path.normpath(rel))]
            copy(os.path.join(base, top), os.path.join(d, top))
        fixed.append(f"{s['name']}: {ref}")
    open(sk, "w", encoding="utf-8").write(t)

print(f"name fixed: {renamed}, refs fixed: {len(fixed)}, unresolved: {len(left)}")
print("\n".join(left))
