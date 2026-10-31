# Curation — doublons & améliorations

Passe du 2026-10-31 : 527 → **449 skills**, sans perte de contenu (les perdants sont fusionnés dans le gagnant sous `references/merged/`).

## Méthode

1. Inventaire + lint de chaque skill (`tools/inventory.py`) et similarité TF-IDF nom/description/corps (`tools/similar.py`).
2. Revue manuelle des clusters → gagnant = profondeur (références, scripts), source officielle/mainteneur, portabilité (pas couplé à un runtime tiers).
3. Perdant **fusionné** dans le gagnant : dossier copié dans `references/merged/<nom>/` + index « Merged references » dans le `SKILL.md` gagnant.
4. Améliorations sur **tous** les skills restants :
   - `name:` aligné sur le dossier (81 corrigés) ; frontmatter YAML valide partout (`tools/check_frontmatter.py`).
   - 59 liens cassés réparés (scripts/références restés dans le repo source, liens vers skills frères renommés).
   - 36 descriptions réécrites « quoi + quand l'utiliser » pour que Claude déclenche le bon skill.
   - 11 skills > 500 lignes découpés : cœur léger + `references/extended.md` chargé à la demande.
   - 24 micro-skills Owl-Listener regroupés en 3 skills à divulgation progressive (`ux-laws`, `gestalt-principles`, `visual-critique`).

Tout est reproductible : `tools/rebuild.sh <dossier-des-clones>`.

## Fusions (perdant → gagnant) (49)

- 01 Owl-Listener/designer-skills/motion-system -> affaan-m/everything-claude-code/ecc-motion-foundations (UI motion tokens: ECC version is code-level and complete)
- 01 Owl-Listener/designer-skills/animation-principles -> affaan-m/everything-claude-code/ecc-motion-foundations (subset of motion foundations)
- 01 iart-ai/web-animation-skills/gsap-web -> greensock/gsap-skills/gsap-core (official GreenSock skill wins)
- 01 iart-ai/webgl-animation-skills/threejs-animation -> CloudAI-X/threejs-skills/threejs-animation (CloudAI-X version is deeper)
- 01 Owl-Listener/designer-skills/micro-interaction-spec -> iart-ai/web-animation-skills/micro-interaction (iart version has code + refs)
- 01 Owl-Listener/designer-skills/responsive-design -> wshobson/agents/responsive-design (wshobson version has references)
- 01 Owl-Listener/designer-skills/accessibility-audit -> accesslint/claude-marketplace/accessibility-audit (accesslint follows WCAG-EM with tooling)
- 01 wshobson/agents/accessibility-compliance -> accesslint/claude-marketplace/accessibility-audit (same audit scope)
- 01 wshobson/agents/wcag-audit-patterns -> accesslint/claude-marketplace/accessibility-audit (same audit scope)
- 01 affaan-m/everything-claude-code/ecc-react-performance -> vercel-labs/agent-skills/react-best-practices (Vercel rules are the reference)
- 02 iart-ai/lower-thirds-skills/lower-thirds -> iart-ai/tiktok-video-skills/lower-thirds (tiktok version is 3x deeper)
- 02 affaan-m/everything-claude-code/ecc-manim-video -> iart-ai/manim-skills/manim (iart version is deeper)
- 02 haidrrrry/claude-remotion-skill/claude-remotion -> iart-ai/motion-design-skills/remotion-video (same scope, iart version tighter)
- 03 Jeffallan/claude-skills/debugging-wizard -> obra/superpowers/systematic-debugging (superpowers debugging is the reference)
- 03 wshobson/agents/debugging-strategies -> obra/superpowers/systematic-debugging (same scope)
- 03 Jeffallan/claude-skills/code-reviewer -> wshobson/agents/code-review-excellence (deeper)
- 03 wshobson/agents/api-design-principles -> Jeffallan/claude-skills/api-designer (same scope)
- 03 affaan-m/everything-claude-code/ecc-api-design -> Jeffallan/claude-skills/api-designer (kept as REST deep-dive reference)
- 03 affaan-m/everything-claude-code/ecc-architecture-decision-records -> wshobson/agents/architecture-decision-records (same scope)
- 03 affaan-m/everything-claude-code/ecc-postgres-patterns -> Jeffallan/claude-skills/postgres-pro (postgres-pro has references)
- 03 wshobson/agents/sql-optimization-patterns -> Jeffallan/claude-skills/database-optimizer (same scope)
- 03 wshobson/agents/database-migration -> affaan-m/everything-claude-code/ecc-database-migrations (ECC covers expand-contract + per-ORM)
- 03 affaan-m/everything-claude-code/ecc-kubernetes-patterns -> Jeffallan/claude-skills/kubernetes-specialist (progressive disclosure version wins)
- 03 affaan-m/everything-claude-code/ecc-deployment-patterns -> wshobson/agents/deployment-pipeline-design (same scope)
- 03 affaan-m/everything-claude-code/ecc-fastapi-patterns -> Jeffallan/claude-skills/fastapi-expert (same scope)
- 03 wshobson/agents/fastapi-templates -> Jeffallan/claude-skills/fastapi-expert (same scope)
- 03 affaan-m/everything-claude-code/ecc-nestjs-patterns -> Jeffallan/claude-skills/nestjs-expert (same scope)
- 03 affaan-m/everything-claude-code/ecc-rust-patterns -> Jeffallan/claude-skills/rust-engineer (same scope)
- 03 affaan-m/everything-claude-code/ecc-golang-patterns -> Jeffallan/claude-skills/golang-pro (same scope)
- 03 affaan-m/everything-claude-code/ecc-python-patterns -> Jeffallan/claude-skills/python-pro (same scope)
- 03 affaan-m/everything-claude-code/ecc-typescript-patterns -> Jeffallan/claude-skills/typescript-pro (same scope)
- 03 wshobson/agents/microservices-patterns -> Jeffallan/claude-skills/microservices-architect (same scope)
- 03 wshobson/agents/rag-implementation -> Jeffallan/claude-skills/rag-architect (same scope)
- 03 Jeffallan/claude-skills/mcp-developer -> anthropics/skills/mcp-builder (official Anthropic skill wins)
- 03 affaan-m/everything-claude-code/ecc-e2e-testing -> wshobson/agents/e2e-testing-patterns (same scope)
- 03 openai/skills/openai-playwright -> lackeyjb/playwright-skill/playwright-skill (Codex-oriented duplicate)
- 03 Jeffallan/claude-skills/security-reviewer -> affaan-m/everything-claude-code/ecc-security-review (same scope)
- 03 wshobson/agents/error-handling-patterns -> affaan-m/everything-claude-code/ecc-error-handling (ECC is broader)
- 03 affaan-m/everything-claude-code/ecc-git-workflow -> wshobson/agents/git-advanced-workflows (ECC version >700 lines)
- 03 affaan-m/everything-claude-code/ecc-tdd-workflow -> obra/superpowers/test-driven-development (superpowers TDD is the reference)
- 03 mattpocock/skills/claude-handoff -> mattpocock/skills/handoff (in-progress duplicate)
- 03 affaan-m/everything-claude-code/ecc-eval-harness -> muratcankoylan/Agent-Skills-for-Context-Engineering/evaluation (same scope)
- 03 affaan-m/everything-claude-code/ecc-plan-orchestrate -> obra/superpowers/writing-plans (ECC-coupled duplicate)
- 02 ra100/blender-claude-plugin/blender-lab-mcp--blender-animation-rigging -> EL4CTEO/blender-skills/blender-character-rigging (Blender Lab MCP API reference (official MCP, Blender 5.1+))
- 02 ra100/blender-claude-plugin/blender-lab-mcp--blender-geometry-nodes -> EL4CTEO/blender-skills/blender-geometry-nodes (Blender Lab MCP API reference (official MCP, Blender 5.1+))
- 02 ra100/blender-claude-plugin/blender-lab-mcp--blender-modeling-modifiers -> EL4CTEO/blender-skills/blender-hardsurface-modeling (Blender Lab MCP API reference (official MCP, Blender 5.1+))
- 02 ra100/blender-claude-plugin/blender-lab-mcp--blender-physics-simulation -> EL4CTEO/blender-skills/blender-simulation (Blender Lab MCP API reference (official MCP, Blender 5.1+))
- 02 ra100/blender-claude-plugin/blender-lab-mcp--blender-scene-rendering -> EL4CTEO/blender-skills/blender-rendering (Blender Lab MCP API reference (official MCP, Blender 5.1+))
- 02 ra100/blender-claude-plugin/blender-lab-mcp--blender-shader-nodes -> EL4CTEO/blender-skills/blender-pbr-materials (Blender Lab MCP API reference (official MCP, Blender 5.1+))

## Regroupés (3)

- 11 Owl-Listener skills -> ux-laws
- 6 Owl-Listener skills -> gestalt-principles
- 7 Owl-Listener skills -> visual-critique

## Déplacés / renommés (11)

- affaan-m:ecc-motion-foundations -> 01-web-design/affaan-m/everything-claude-code/ecc-motion-foundations
- affaan-m:ecc-motion-patterns -> 01-web-design/affaan-m/everything-claude-code/ecc-motion-patterns
- affaan-m:ecc-motion-advanced -> 01-web-design/affaan-m/everything-claude-code/ecc-motion-advanced
- affaan-m:ecc-taste -> 02-motion-design/affaan-m/everything-claude-code/ecc-video-taste
- affaan-m:ecc-taste-application -> 02-motion-design/affaan-m/everything-claude-code/ecc-video-taste-application
- affaan-m:ecc-taste-distillation -> 02-motion-design/affaan-m/everything-claude-code/ecc-video-taste-distillation
- affaan-m:ecc-ui-demo -> 02-motion-design/affaan-m/everything-claude-code/ecc-ui-demo
- affaan-m:ecc-remotion-video-creation -> 02-motion-design/affaan-m/everything-claude-code/remotion-best-practices
- charlie947:launch-video -> 02-motion-design/charlie947/motion-graphics-skills/saas-launch-video
- ra100:blender-lab-mcp--blender-compositing-nodes -> 02-motion-design/ra100/blender-claude-plugin/blender-compositing-nodes
- ra100:blender-lab-mcp--blender-python-scripting -> 02-motion-design/ra100/blender-claude-plugin/blender-python-scripting

## Retirés (non autonomes / redondants) (8)

- 03 wshobson/agents/context-driven-development (needs the Conductor plugin commands)
- 03 wshobson/agents/track-management (needs the Conductor plugin commands)
- 03 wshobson/agents/workflow-patterns (needs the Conductor plugin commands)
- 01 affaan-m/everything-claude-code/ecc-frontend-design-direction (ECC-house style, covered by frontend-design/impeccable/taste-skill)
- 03 affaan-m/everything-claude-code/ecc-skill-stocktake (only audits an ECC install)
- 03 affaan-m/everything-claude-code/ecc-continuous-learning-v2 (requires ECC hook runtime)
- 02 Owl-Listener/designer-skills/ui-animation-principles (duplicate copy (kept iart-ai:animation-principles))
- 02 Owl-Listener/designer-skills/ui-motion-system (duplicate copy)
