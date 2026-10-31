"""Rewrite weak SKILL.md descriptions so Claude can route to them: say what the skill does AND when to use it.
Usage: python -I tools/descriptions.py <repo_dir>"""
import json, os, re, sys

R = sys.argv[1]
NEW = {
    "frontend-design": "Distinctive, intentional visual design for new or reshaped UI: aesthetic direction, typography, color, layout and details that don't read as templated defaults. Use when building a landing page, site, dashboard or component and the result must look designed rather than generic, or when the user says the UI looks bland, AI-made or like a template.",
    "theme-factory": "Apply one of 10 preset color/font themes, or generate a new theme, to any artifact: slides, docs, reports, HTML pages. Use when the user wants to restyle an existing artifact, pick a theme, or keep several artifacts visually consistent.",
    "design": "All-in-one design studio: brand identity, design tokens, UI styling, logo generation (55 styles), corporate identity program, HTML presentations, banners and SVG icons. Use when the user asks for a logo, brand kit, CIP mockups, icon set or presentation design, or needs several brand deliverables at once.",
    "brand": "Brand voice, visual identity, messaging frameworks, style guides and brand-compliance checks. Use when writing or reviewing branded content, defining tone of voice, building a style guide, or checking that assets stay on-brand.",
    "banner-design": "Design banners for social media, ads, website heroes and print, with several art-direction options and optional generated visuals. Use when the user needs a Facebook/X/LinkedIn/YouTube/Instagram banner, a Google Display ad, a website hero or a print banner.",
    "web-design-spec-first": "Spec-first web visual design: from a PRD, reference URL, screenshot or keywords, first write a standard DESIGN.md, get it approved, then generate web code that meets the UI/UX, visual, motion and responsive bar. Use when the user says 'build me a website', 'design a page', 'make it like X', 'turn this screenshot/PRD into a page', 'make a landing page' or 'write a design spec'. Not for backend, databases or logic bugs.",
    "design-md": "Analyze a Google Stitch project and synthesize its semantic design system into a DESIGN.md file. Use when the user works with Stitch and wants a reusable design spec, or needs Stitch screens to stay consistent.",
    "taste-design": "Generate an agent-friendly DESIGN.md for Google Stitch that enforces premium, anti-generic UI: strict typography, calibrated color, asymmetric layouts, micro-motion and hardware-accelerated performance. Use when starting a Stitch project or when Stitch output looks generic.",
    "enhance-prompt": "Turn a vague UI idea into a polished, Stitch-optimized prompt: adds specificity, UI/UX vocabulary and design-system context. Use before generating screens in Google Stitch, or when a Stitch generation came out off-target.",
    "extract-design-md": "Extract a complete design system (DESIGN.md) from frontend source: React, Vue, Svelte, Angular or HTML/CSS components, stylesheets, Tailwind config and tokens. Use when the user wants to document an existing UI's design system, migrate it to Stitch, or give agents a design reference for an existing codebase.",
    "shadcn-ui": "Build with shadcn/ui: find, install, compose and customize components following shadcn conventions. Use when a project uses or should use shadcn/ui, when adding a component (dialog, form, table, combobox…), or when theming shadcn with Tailwind.",
    "react-components": "Convert Google Stitch designs into modular Vite + React components, or sync existing components with the latest Stitch designs, with AST-based validation. Use when implementing Stitch screens in React or updating React code after a Stitch design change.",
    "remotion-motion-graphics": "Build motion graphics as real video with Remotion: title cards, lower thirds, logo stings, badges, stat reveals, countdowns, end screens, captions, animated charts, social reels; export MP4 or transparent ProRes/PNG sequences for Premiere, Final Cut or After Effects. Use when the user wants a broadcast-style graphic element or overlay rather than a full edited video.",
    "stitch-remotion": "Generate walkthrough videos of Google Stitch projects with Remotion: smooth transitions, zooms and text overlays. Use when the user wants a product demo or showcase video made from Stitch screens.",
    "blender-compositing-nodes": "Blender 5.x compositor via Python (bpy): post-processing, color grading, denoising, keying, glare, depth of field, render passes, multi-layer EXR output and scripted compositing pipelines (5.1 changes included). Use when grading or finishing renders inside Blender, keying green screen, splitting render passes or automating compositing.",
    "blender-python-scripting": "Blender 5.x Python (bpy, Python 3.13): custom operators, UI panels, add-ons, context management, handlers, timers, properties, batch processing and data access. Use when writing or debugging any bpy script, building a Blender tool, or automating repetitive Blender work. Works best through the official Blender Lab MCP server.",
    "ask-matt": "Router over Matt Pocock's engineering skills: tells you which skill or flow fits your situation. Use when unsure which of the planning, spec, TDD, triage or review skills to start with.",
    "grill-with-docs": "Relentless interview that sharpens a plan or design and writes ADRs and a glossary as it goes. Use when a design decision needs stress-testing and the outcome should be documented for the team.",
    "implement": "Implement a piece of work from a spec or a set of tickets. Use after /to-spec or /to-tickets, when the plan is agreed and it is time to write the code.",
    "implement-spec": "Implement the output of /to-spec and /to-tickets in code, ticket by ticket, respecting blocking edges. Use when a spec and its tickets exist and the user says to build it.",
    "improve-codebase-architecture": "Scan a codebase for deepening opportunities (shallow modules, leaky boundaries), present them as a visual HTML report, then grill through the one you pick. Use when the user wants to improve architecture, reduce complexity, or decide what to refactor first.",
    "pr": "Write a pull request body: what changed, why, how it was tested, risks. Use when opening or updating a PR, or when the user asks for a PR description.",
    "retro": "Run a retrospective on a coding session: what worked, what went wrong, what to change in prompts, skills or CLAUDE.md. Use at the end of a long session or after a failed attempt, to capture lessons.",
    "to-spec": "Turn the current conversation into a spec and publish it to the project's issue tracker: no interview, just synthesis of what was discussed. Use when the discussion has converged and the user wants it written down as a spec.",
    "to-tickets": "Break a plan, spec or conversation into tracer-bullet tickets with explicit blocking edges, published to the configured tracker (one file per ticket locally, or native links on a real tracker). Use when a spec is ready and the work must be split for one or more agents.",
    "triage": "Move issues and external PRs through a triage state machine: categorise, verify, grill if needed, and write agent-ready briefs. Use when processing an issue backlog or incoming PRs.",
    "wayfinder": "Plan work too big for one agent session as a shared map of decision tickets on the issue tracker, then resolve them one at a time. Use for multi-session projects, migrations or features whose path is still unclear.",
    "grill-me": "Relentless interview that sharpens a plan or design by asking the hard questions one at a time. Use when the user wants their idea stress-tested before committing to it.",
    "handoff": "Compact the current conversation into a handoff document another agent can pick up cold. Use before ending a long session, when context is near its limit, or when passing work to another agent or person.",
    "teach": "Teach the user a new skill or concept inside this workspace, with exercises grounded in their own code. Use when the user wants to learn something rather than have it done for them.",
    "to-questionnaire": "Turn a decision you cannot fully answer into a questionnaire for someone else to fill in. Use when progress is blocked on input from a stakeholder, client or teammate.",
    "wait-what": "Re-pitch the last message because it did not land: simpler words, the point first, a concrete example. Use when the user says they are confused, lost, or 'wait, what?'.",
    "ecc-autonomous-loops": "Patterns and architectures for autonomous Claude Code loops, from simple sequential pipelines to RFC-driven multi-agent DAGs, with stop conditions and cost guards. Use when designing an unattended agent loop, a long-running pipeline, or a multi-agent workflow.",
    "webapp-testing": "Test local web apps with Playwright: verify frontend behavior, debug UI, capture screenshots and read browser logs. Use when the user asks to test, check or debug a web app running locally, or to verify a UI change actually works.",
    "openai-gh-address-comments": "Address review and issue comments on the open GitHub PR for the current branch with the gh CLI (checks gh auth first). Use when the user asks to handle, answer or fix PR review comments.",
    "claude-api": "Reference for the Claude API / Anthropic SDK: model ids, pricing, params, streaming, tool use, MCP, agents, prompt caching, token counting, model migration. Use BEFORE editing code whenever the prompt names Claude/Anthropic (Claude, Opus, Sonnet, Haiku, anthropic, @anthropic-ai, claude-*), asks about LLM pricing, model choice, limits or caching, or the task is LLM-shaped with no provider stated (agent, MCP, tools, RAG, summarize/extract/classify). Skip when another provider (OpenAI, Gemini, Mistral, Ollama…) is clearly in use.",
}

inv = json.load(open(os.path.join(R, "tools", "inventory.json"), encoding="utf-8"))
done = 0
for s in inv:
    if s["name"] not in NEW:
        continue
    p = os.path.join(R, s["dom"], s["owner"], s["name"], "SKILL.md")
    t = open(p, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", t, re.S)
    fm = m.group(1)
    d = NEW[s["name"]]
    assert len(d) <= 1024, s["name"]
    line = "description: " + json.dumps(d, ensure_ascii=False)
    fm2, n = re.subn(r"^description:.*?(?=\n[a-zA-Z_-]+:|\Z)", lambda _: line, fm, count=1, flags=re.S | re.M)
    if not n:
        fm2 = fm + "\n" + line
    open(p, "w", encoding="utf-8").write(t[: m.start(1)] + fm2 + t[m.end(1):])
    done += 1
print("descriptions rewritten:", done, "/", len(NEW))

# Upstream frontmatter that is not valid YAML (unquoted ": " in description) -> quote it.
import yaml
quoted = 0
for s in inv:
    p = os.path.join(R, s["dom"], s["owner"], s["name"], "SKILL.md")
    t = open(p, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---", t, re.S)
    try:
        yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        t = re.sub(r"^description: (?![\"'])(.+)$", lambda x: "description: " + json.dumps(x.group(1).strip(), ensure_ascii=False), t, count=1, flags=re.M)
        open(p, "w", encoding="utf-8").write(t)
        quoted += 1
print("frontmatter quoted:", quoted)

# Body fixes: notes that point at skills this repo does not bundle.
BODY = {
    "ecc-autonomous-loops": r"> Compatibility note \(v1\.8\.0\).*?breaking existing workflows\.\n\n",
}
for s in inv:
    if s["name"] in BODY:
        p = os.path.join(R, s["dom"], s["owner"], s["name"], "SKILL.md")
        t = open(p, encoding="utf-8").read()
        open(p, "w", encoding="utf-8").write(re.sub(BODY[s["name"]], "", t, flags=re.S))
