"""Keep SKILL.md bodies under ~500 lines (Anthropic guidance): move trailing H2 sections into
references/extended.md and leave an index, so the core loads cheaply and detail loads on demand.
Usage: python -I tools/split_long.py <repo_dir> [max_lines]"""
import json, os, re, sys

R = sys.argv[1]
MAX = int(sys.argv[2]) if len(sys.argv) > 2 else 500
KEEP = 300  # target size of the core after splitting
inv = json.load(open(os.path.join(R, "tools", "inventory.json"), encoding="utf-8"))
for s in inv:
    if s["lines"] <= MAX:
        continue
    d = os.path.join(R, s["dom"], s["owner"], s["name"])
    t = open(os.path.join(d, "SKILL.md"), encoding="utf-8").read()
    m = re.match(r"^---\s*\n.*?\n---\s*\n", t, re.S)
    fm, body = t[: m.end()], t[m.end():]
    # H2 boundaries outside fenced code blocks
    lines, fence, cuts = body.split("\n"), False, []
    for i, l in enumerate(lines):
        if l.startswith("```"):
            fence = not fence
        elif not fence and l.startswith("## "):
            cuts.append(i)
    cut = next((c for c in cuts if c >= KEEP), None) or next((c for c in reversed(cuts) if c < len(lines) - 40), None)
    if not cut or cut < 60:
        print("skip (no usable heading)", s["name"])
        continue
    core, rest = lines[:cut], lines[cut:]
    heads = [l[3:].strip() for l in rest if l.startswith("## ")]
    os.makedirs(os.path.join(d, "references"), exist_ok=True)
    ext = os.path.join(d, "references", "extended.md")
    rel_fix = lambda x: re.sub(r"\]\((?!https?:|#|/)([^)]+)\)", r"](../\1)", x)  # links were relative to the skill root
    open(ext, "w", encoding="utf-8").write(f"# {s['name']} — extended reference\n\n" + rel_fix("\n".join(rest)).strip() + "\n")
    idx = "\n".join(f"- {h}" for h in heads)
    new = "\n".join(core).rstrip() + f"\n\n## Extended reference\n\nMore detail lives in [references/extended.md](references/extended.md). Read the section you need:\n\n{idx}\n"
    open(os.path.join(d, "SKILL.md"), "w", encoding="utf-8").write(fm + new)
    print(f"split {s['name']}: {s['lines']} -> {len(core)} core lines, {len(heads)} sections moved")
