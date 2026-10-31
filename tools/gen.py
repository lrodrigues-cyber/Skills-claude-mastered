"""Generate per-pack README catalogs + .claude-plugin/marketplace.json from .manifest.
Usage: python -I tools/gen.py <repo_dir>"""
import collections, json, os, re, sys

R = sys.argv[1]
DOM = {
    "01-web-design": ("🎨 Web Design & Interfaces", "Design de sites, UI/UX, design systems, accessibilité, animations web (GSAP, Motion.dev), 3D web (Three.js/WebGL)."),
    "02-motion-design": ("🎬 Motion Design & 3D (Remotion · Blender · Manim)", "Vidéo en code (Remotion, HTML/canvas, Manim), principes d'animation, formats pub/TikTok/YouTube, Blender pro (modélisation → rigging → lookdev → rendu) piloté par Claude."),
    "03-code-backend-workflow": ("⚙️ Code, Backend & Workflows de session", "Backend/API/DB, architecture, debugging, tests, sécurité, CI/CD, observabilité, context engineering, gestion du contexte/tokens et workflows d'agents (TDD, plans, handoff, sous-agents)."),
    "04-automations": ("🤖 Automations Claude Code (plugins · hooks · commands)", "Plugins complets : hooks (sécurité, coût, logs, format), slash commands, agents et règles. Installables via le marketplace de ce repo."),
}
LINKS = {
    "01-web-design": [
        ("Figma skills (OpenAI curated)", "https://github.com/openai/skills/tree/main/skills/.curated", "Figma Developer Terms → non redistribuable"),
        ("shadcn/ui skill officiel", "https://ui.shadcn.com/docs/skills", "Doc officielle"),
        ("ComposioHQ/awesome-claude-skills", "https://github.com/ComposioHQ/awesome-claude-skills", "864 skills, pas de licence racine → liste à explorer"),
    ],
    "02-motion-design": [
        ("Remotion — skills officiels", "https://github.com/remotion-dev/skills", "Pas de licence → `npx skills add remotion-dev/skills`"),
        ("Blender MCP (ahujasid) — serveur MCP", "https://github.com/ahujasid/blender-mcp", "Serveur MCP à coupler avec les skills Blender"),
        ("Blender Lab MCP officiel (Blender ≥ 5.1)", "https://github.com/ra100/blender-claude-plugin", "Requis pour `blender-lab-mcp--*`"),
        ("Claude Code Video Toolkit (Manim)", "https://github.com/wilwaldon/Claude-Code-Video-Toolkit", "Pas de licence"),
        ("Motion Video Director", "https://github.com/Miftahul-Islam-Efaz/Motion-graphics-skill", "Repo indisponible au clonage"),
        ("ElevenLabs MCP (voix, SFX, musique dans Claude)", "https://github.com/elevenlabs/elevenlabs-mcp", "Vu sur TikTok (109M vues) — MCP, pas un skill"),
    ],
    "03-code-backend-workflow": [
        ("Karpathy CLAUDE.md (andrej-karpathy-skills)", "https://github.com/forrestchang/andrej-karpathy-skills", "227k⭐, pas de licence → copier le CLAUDE.md à la main"),
        ("Get Shit Done (GSD)", "https://github.com/gsd-build/get-shit-done", "Système de commandes : `npx get-shit-done-cc`"),
        ("Excalidraw diagram skill", "https://github.com/coleam00/excalidraw-diagram-skill", "Pas de licence"),
        ("token-optimizer", "https://github.com/alexgreensh/token-optimizer", "Audit tokens, pas de licence"),
    ],
    "04-automations": [
        ("claude-mem — mémoire persistante entre sessions", "https://github.com/thedotmack/claude-mem", "107k⭐, plugin avec worker → `/plugin marketplace add thedotmack/claude-mem`"),
        ("RTK — proxy CLI qui réduit les tokens des commandes", "https://github.com/rtk-ai/rtk", "85k⭐, binaire Rust (Apache-2.0)"),
        ("Everything Claude Code (ECC) — setup complet", "https://github.com/affaan-m/everything-claude-code", "294k⭐ ; hooks liés aux scripts du repo → installer le plugin complet"),
        ("Claude Command Suite", "https://github.com/qdhenry/Claude-Command-Suite", "216 commands, pas de licence"),
        ("awesome-claude-code (hesreallyhim)", "https://github.com/hesreallyhim/awesome-claude-code", "Liste de référence hooks/commands/outils"),
        ("claude-plugins.dev", "https://claude-plugins.dev", "Registre : ~12k plugins, ~63k skills"),
    ],
}


def front(p):
    try:
        return open(os.path.join(p, "SKILL.md"), encoding="utf-8", errors="ignore").read()
    except OSError:
        return ""


def desc(p, kind):
    if kind == "plugin":
        try:
            return json.load(open(os.path.join(p, ".claude-plugin", "plugin.json"), encoding="utf-8")).get("description", "")[:180]
        except (OSError, ValueError):
            pass
    t = front(p)
    m = re.search(r'^description:\s*(.+?)(?=\n[a-zA-Z_-]+:|\n---)', t, re.S | re.M)
    d = re.sub(r'\s+', ' ', m.group(1)).strip().strip('"\'>|- ') if m else ""
    return (d[:180] + "…") if len(d) > 180 else d


def lic(p):
    for f in os.listdir(p):
        if f.lower().startswith("licen"):
            h = open(os.path.join(p, f), encoding="utf-8", errors="ignore").read(400)
            for k, v in [("Apache", "Apache-2.0"), ("MIT", "MIT"), ("ShareAlike", "CC-BY-SA-4.0"), ("GNU GENERAL", "GPL-3.0")]:
                if k in h:
                    return v
            return "voir LICENSE"
    return "GPL-3.0 (README)" if "AndreiFlau" in p else "MIT (README)"


rows = collections.defaultdict(list)
for line in open(os.path.join(R, ".manifest"), encoding="utf-8"):
    dom, owner, name, url, kind = line.strip().split("|")
    rows[dom].append((owner, name, url, kind))

market = []
for dom, items in sorted(rows.items()):
    title, intro = DOM[dom]
    by = collections.defaultdict(list)
    for o, n, u, k in items:
        by[o].append((n, u, k))
    unit = "plugins" if dom == "04-automations" else "skills"
    out = [f"# {title}\n", f"{intro}\n",
           f"**{len(items)} {unit}** issus de {len(by)} sources. Chaque dossier garde sa licence d'origine.\n", "## Installation\n"]
    if dom == "04-automations":
        out += ["```text", "/plugin marketplace add lrodrigues-cyber/Skills-claude-mastered", "/plugin install <nom>@skills-claude-mastered", "```",
                "Ou en local : `claude --plugin-dir 04-automations/<auteur>/<repo>/<plugin>`\n"]
    else:
        out += ["```bash", f"cp -r {dom}/<auteur>/<repo>/<skill> ~/.claude/skills/   # un skill", f"./install.sh {dom}                                    # tout le pack", "```\n"]
    for o in sorted(by, key=lambda x: -len(by[x])):
        out.append(f"## [{o}](https://github.com/{o}) · {len(by[o])}\n")
        out.append("| Nom | Licence | Description |\n|---|---|---|")
        for n, u, k in sorted(by[o]):
            p = os.path.join(R, dom, o, n)
            out.append(f"| [`{n}`]({o}/{n}) · [src]({u}) | {lic(p)} | {desc(p, k).replace('|', '/')} |")
            if k == "plugin":
                mname = re.sub(r'^claude-', '', n)  # "claude-*" names are reserved for Anthropic in third-party marketplaces
                if mname != n:
                    pj = os.path.join(p, ".claude-plugin", "plugin.json")
                    meta = json.load(open(pj, encoding="utf-8"))
                    meta["name"] = mname
                    json.dump(meta, open(pj, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
                market.append({"name": mname, "source": f"./{dom}/{o}/{n}", "description": desc(p, k)})
        out.append("")
    out.append("## 🔗 Référencés (non copiés — licence, format ou runtime)\n")
    for t, u, why in LINKS[dom]:
        out.append(f"- [{t}]({u}) — {why}")
    open(os.path.join(R, dom, "README.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(dom, len(items))

os.makedirs(os.path.join(R, ".claude-plugin"), exist_ok=True)
json.dump({"name": "skills-claude-mastered", "owner": {"name": "lrodrigues-cyber"},
           "metadata": {"description": "Curated Claude Code automations (hooks, commands, plugins)"},
           "plugins": market}, open(os.path.join(R, ".claude-plugin", "marketplace.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("marketplace", len(market))
