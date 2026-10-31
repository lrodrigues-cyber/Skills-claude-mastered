"""Deduplicate, merge, move and consolidate skills after tools/build.sh.
Usage: python -I tools/curate.py <repo_dir>
Skills are addressed as "<github-user>:<skill-dir-name>" (unique across packs).
merge(winner, loser): loser's whole folder -> winner/references/merged/<loser>/ (its SKILL.md
becomes README.md there, so its own relative links keep working) + an index section in the winner.
"""
import json, os, re, shutil, sys

R = sys.argv[1]
MAN = os.path.join(R, ".manifest")
rows = [l.rstrip("\n").split("|") for l in open(MAN, encoding="utf-8") if l.strip()]
log = []

# loser -> winner, reason
MERGE = {
    # 01 web
    "Owl-Listener:motion-system": ("affaan-m:ecc-motion-foundations", "UI motion tokens: ECC version is code-level and complete"),
    "Owl-Listener:animation-principles": ("affaan-m:ecc-motion-foundations", "subset of motion foundations"),
    "iart-ai:gsap-web": ("greensock:gsap-core", "official GreenSock skill wins"),
    "iart-ai:threejs-animation": ("CloudAI-X:threejs-animation", "CloudAI-X version is deeper"),
    "Owl-Listener:micro-interaction-spec": ("iart-ai:micro-interaction", "iart version has code + refs"),
    "Owl-Listener:responsive-design": ("wshobson:responsive-design", "wshobson version has references"),
    "Owl-Listener:accessibility-audit": ("accesslint:accessibility-audit", "accesslint follows WCAG-EM with tooling"),
    "wshobson:accessibility-compliance": ("accesslint:accessibility-audit", "same audit scope"),
    "wshobson:wcag-audit-patterns": ("accesslint:accessibility-audit", "same audit scope"),
    "affaan-m:ecc-react-performance": ("vercel-labs:react-best-practices", "Vercel rules are the reference"),
    # 02 motion
    "iart-ai:lower-thirds@lower-thirds-skills": ("iart-ai:lower-thirds@tiktok-video-skills", "tiktok version is 3x deeper"),
    "affaan-m:ecc-manim-video": ("iart-ai:manim", "iart version is deeper"),
    "haidrrrry:claude-remotion": ("iart-ai:remotion-video", "same scope, iart version tighter"),
    # 03 code
    "Jeffallan:debugging-wizard": ("obra:systematic-debugging", "superpowers debugging is the reference"),
    "wshobson:debugging-strategies": ("obra:systematic-debugging", "same scope"),
    "Jeffallan:code-reviewer": ("wshobson:code-review-excellence", "deeper"),
    "wshobson:api-design-principles": ("Jeffallan:api-designer", "same scope"),
    "affaan-m:ecc-api-design": ("Jeffallan:api-designer", "kept as REST deep-dive reference"),
    "affaan-m:ecc-architecture-decision-records": ("wshobson:architecture-decision-records", "same scope"),
    "affaan-m:ecc-postgres-patterns": ("Jeffallan:postgres-pro", "postgres-pro has references"),
    "wshobson:sql-optimization-patterns": ("Jeffallan:database-optimizer", "same scope"),
    "wshobson:database-migration": ("affaan-m:ecc-database-migrations", "ECC covers expand-contract + per-ORM"),
    "affaan-m:ecc-kubernetes-patterns": ("Jeffallan:kubernetes-specialist", "progressive disclosure version wins"),
    "affaan-m:ecc-deployment-patterns": ("wshobson:deployment-pipeline-design", "same scope"),
    "affaan-m:ecc-fastapi-patterns": ("Jeffallan:fastapi-expert", "same scope"),
    "wshobson:fastapi-templates": ("Jeffallan:fastapi-expert", "same scope"),
    "affaan-m:ecc-nestjs-patterns": ("Jeffallan:nestjs-expert", "same scope"),
    "affaan-m:ecc-rust-patterns": ("Jeffallan:rust-engineer", "same scope"),
    "affaan-m:ecc-golang-patterns": ("Jeffallan:golang-pro", "same scope"),
    "affaan-m:ecc-python-patterns": ("Jeffallan:python-pro", "same scope"),
    "affaan-m:ecc-typescript-patterns": ("Jeffallan:typescript-pro", "same scope"),
    "wshobson:microservices-patterns": ("Jeffallan:microservices-architect", "same scope"),
    "wshobson:rag-implementation": ("Jeffallan:rag-architect", "same scope"),
    "Jeffallan:mcp-developer": ("anthropics:mcp-builder", "official Anthropic skill wins"),
    "affaan-m:ecc-e2e-testing": ("wshobson:e2e-testing-patterns", "same scope"),
    "openai:openai-playwright": ("lackeyjb:playwright-skill", "Codex-oriented duplicate"),
    "Jeffallan:security-reviewer": ("affaan-m:ecc-security-review", "same scope"),
    "wshobson:error-handling-patterns": ("affaan-m:ecc-error-handling", "ECC is broader"),
    "affaan-m:ecc-git-workflow": ("wshobson:git-advanced-workflows", "ECC version >700 lines"),
    "affaan-m:ecc-tdd-workflow": ("obra:test-driven-development", "superpowers TDD is the reference"),
    "mattpocock:claude-handoff": ("mattpocock:handoff", "in-progress duplicate"),
    "affaan-m:ecc-eval-harness": ("muratcankoylan:evaluation", "same scope"),
    "affaan-m:ecc-plan-orchestrate": ("obra:writing-plans", "ECC-coupled duplicate"),
}
DROP = {
    "wshobson:context-driven-development": "needs the Conductor plugin commands",
    "wshobson:track-management": "needs the Conductor plugin commands",
    "wshobson:workflow-patterns": "needs the Conductor plugin commands",
    "affaan-m:ecc-frontend-design-direction": "ECC-house style, covered by frontend-design/impeccable/taste-skill",
    "affaan-m:ecc-skill-stocktake": "only audits an ECC install",
    "affaan-m:ecc-continuous-learning-v2": "requires ECC hook runtime",
    "Owl-Listener:ui-animation-principles": "duplicate copy (kept iart-ai:animation-principles)",
    "Owl-Listener:ui-motion-system": "duplicate copy",
}
MOVE = {  # skill -> (new pack, new name or None)
    "affaan-m:ecc-motion-foundations": ("01-web-design", None),
    "affaan-m:ecc-motion-patterns": ("01-web-design", None),
    "affaan-m:ecc-motion-advanced": ("01-web-design", None),
    "affaan-m:ecc-taste": ("02-motion-design", "ecc-video-taste"),
    "affaan-m:ecc-taste-application": ("02-motion-design", "ecc-video-taste-application"),
    "affaan-m:ecc-taste-distillation": ("02-motion-design", "ecc-video-taste-distillation"),
    "affaan-m:ecc-ui-demo": ("02-motion-design", None),
    "affaan-m:ecc-remotion-video-creation": ("02-motion-design", "remotion-best-practices"),
    "charlie947:launch-video": ("02-motion-design", "saas-launch-video"),
    "ra100:blender-lab-mcp--blender-compositing-nodes": ("02-motion-design", "blender-compositing-nodes"),
    "ra100:blender-lab-mcp--blender-python-scripting": ("02-motion-design", "blender-python-scripting"),
}
# Blender: EL4CTEO (5.2, scripts, MCP or headless) wins; ra100 deep API references merged in.
for a, b in [("animation-rigging", "blender-character-rigging"), ("geometry-nodes", "blender-geometry-nodes"),
             ("modeling-modifiers", "blender-hardsurface-modeling"), ("physics-simulation", "blender-simulation"),
             ("scene-rendering", "blender-rendering"), ("shader-nodes", "blender-pbr-materials")]:
    MERGE[f"ra100:blender-lab-mcp--blender-{a}"] = (f"EL4CTEO:{b}", "Blender Lab MCP API reference (official MCP, Blender 5.1+)")

# Owl-Listener ships ~1 small skill per law: fold them into 3 skills with progressive disclosure.
CONSOLIDATE = {
    "ux-laws": ("Laws of UX for interface decisions: Fitts, Hick, Jakob, Miller, Tesler, Doherty threshold, peak-end, serial position, Von Restorff, Zeigarnik, aesthetic-usability. Use when choosing layouts, menus, CTAs, flows or loading feedback, or when justifying a UX decision with an established law.",
                ["fitts-law", "hicks-law", "jakobs-law", "millers-law", "teslers-law", "doherty-threshold", "peak-end-rule", "serial-position-effect", "von-restorff-effect", "zeigarnik-effect", "aesthetic-usability"]),
    "gestalt-principles": ("Gestalt principles for visual grouping: proximity, similarity, common region, continuity, closure, figure-ground. Use when grouping UI elements, fixing cluttered layouts, designing cards/forms/navigation, or explaining why a layout reads wrong.",
                ["law-of-proximity", "law-of-similarity", "law-of-common-region", "law-of-continuity", "law-of-closure", "law-of-figure-ground"]),
    "visual-critique": ("Structured visual design critique across affordance, brand consistency, color, composition, information density, typography and visual hierarchy. Use when reviewing a screenshot, mockup or built UI and you need prioritized, actionable design feedback.",
                ["critique-affordance", "critique-brand-consistency", "critique-color", "critique-composition", "critique-information-density", "critique-typography", "critique-visual-hierarchy"]),
}


def find(key):
    user, name = key.split(":", 1)
    repo = None
    if "@" in name:
        name, repo = name.split("@")
    hits = [r for r in rows if r[1].split("/")[0] == user and r[2] == name and (repo is None or r[1].split("/")[1] == repo)]
    if len(hits) != 1:
        raise SystemExit(f"lookup {key}: {len(hits)} hits")
    return hits[0]


def path(r):
    return os.path.join(R, r[0], r[1], r[2])


def split_fm(t):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", t, re.S)
    return (m.group(1), t[m.end():]) if m else ("", t)


def desc_of(fm):
    m = re.search(r"^description:\s*(.+?)(?=\n[a-zA-Z_-]+:|\Z)", fm, re.S | re.M)
    return re.sub(r"\s+", " ", m.group(1)).strip().strip("\"'>|- ") if m else ""


def add_merged_index(winner_dir, entries):
    sk = os.path.join(winner_dir, "SKILL.md")
    t = open(sk, encoding="utf-8").read()
    head = "## Merged references"
    lines = [f"- [`{n}`](references/merged/{n}/README.md) — {d} _(from [{src}]({url}))_" for n, d, src, url in entries]
    if head not in t:
        t = t.rstrip() + f"\n\n{head}\n\nDeeper material folded in from overlapping skills. Read only the file that matches the task.\n\n"
    t = t.rstrip() + "\n" + "\n".join(lines) + "\n"
    open(sk, "w", encoding="utf-8").write(t)


merged_into = {}
for loser, (winner, why) in MERGE.items():
    lr, wr = find(loser), find(winner)
    src, dst = path(lr), os.path.join(path(wr), "references", "merged", lr[2])
    shutil.copytree(src, dst, dirs_exist_ok=True)
    os.replace(os.path.join(dst, "SKILL.md"), os.path.join(dst, "README.md"))
    fm, _ = split_fm(open(os.path.join(dst, "README.md"), encoding="utf-8").read())
    merged_into.setdefault(tuple(wr), []).append((lr[2], desc_of(fm)[:160], lr[1], lr[3]))
    shutil.rmtree(src)
    rows.remove(lr)
    log.append(f"merge  {lr[0][:2]} {lr[1]}/{lr[2]} -> {wr[1]}/{wr[2]} ({why})")
for wr, entries in merged_into.items():
    add_merged_index(path(list(wr)), entries)

for key, why in DROP.items():
    r = find(key)
    shutil.rmtree(path(r))
    rows.remove(r)
    log.append(f"drop   {r[0][:2]} {r[1]}/{r[2]} ({why})")

for key, (dom, new) in MOVE.items():
    r = find(key)
    old = path(r)
    r[0], r[2] = dom, new or r[2]
    os.makedirs(os.path.dirname(path(r)), exist_ok=True)
    shutil.move(old, path(r))
    log.append(f"move   {key} -> {dom}/{r[1]}/{r[2]}")

for new, (desc, parts) in CONSOLIDATE.items():
    srcs = [find(f"Owl-Listener:{p}") for p in parts]
    owner = srcs[0][1]
    dst = os.path.join(R, "01-web-design", owner, new)
    os.makedirs(os.path.join(dst, "references"), exist_ok=True)
    table = []
    for r in srcs:
        fm, body = split_fm(open(os.path.join(path(r), "SKILL.md"), encoding="utf-8").read())
        open(os.path.join(dst, "references", f"{r[2]}.md"), "w", encoding="utf-8").write(body.strip() + "\n")
        table.append(f"| [{r[2].replace('-', ' ')}](references/{r[2]}.md) | {desc_of(fm).split('. Use')[0][:150]} |")
        if not os.path.exists(os.path.join(dst, "LICENSE")):
            shutil.copy(os.path.join(path(r), "LICENSE"), os.path.join(dst, "LICENSE"))
        shutil.rmtree(path(r))
        rows.remove(r)
    title = new.replace("-", " ").title()
    open(os.path.join(dst, "SKILL.md"), "w", encoding="utf-8").write(
        f"---\nname: {new}\ndescription: {json.dumps(desc, ensure_ascii=False)}\n---\n\n# {title}\n\n"
        "Pick the principle(s) that match the decision at hand, read only those reference files, then apply them:\n\n"
        "1. Name the principle and the concrete UI element it constrains.\n"
        "2. State the expected user effect (speed, error rate, recall, perceived grouping…).\n"
        "3. Propose the change, and flag any principle it trades off against.\n\n"
        "| Principle | What it says |\n|---|---|\n" + "\n".join(table) + "\n")
    rows.append(["01-web-design", owner, new, f"https://github.com/{owner}", "skill"])
    log.append(f"fold   {len(parts)} Owl-Listener skills -> {new}")

with open(MAN, "w", encoding="utf-8") as f:
    f.writelines("|".join(r) + "\n" for r in rows)
open(os.path.join(R, "tools", "CURATION.log"), "w", encoding="utf-8").write("\n".join(log) + "\n")
print(len(log), "operations;", sum(r[4] == "skill" for r in rows), "skills,", sum(r[4] == "plugin" for r in rows), "plugins")
