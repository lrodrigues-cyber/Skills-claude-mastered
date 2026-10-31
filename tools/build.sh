#!/usr/bin/env bash
# Rebuild all packs from cloned sources.  Usage: tools/build.sh <src_dir> <repo_dir>
# <src_dir> holds shallow clones named <owner>_<repo>.
set -uo pipefail
S="${1:?src dir}"; R="${2:?repo dir}"
W=01-web-design; M=02-motion-design; C=03-code-backend-workflow; A=04-automations
: > "$R/.manifest"

_copy(){ # kind dom src path name
  local kind=$1 dom=$2 src=$3 p=$4 name=$5 owner=${3/_//}
  local dst="$R/$dom/$owner/$name"
  mkdir -p "$dst"; (cd "$S/$src/$p" && tar cf - --exclude=.git .) | (cd "$dst" && tar xf -)
  ls "$dst" | grep -qiE '^licen' || { f=$(ls "$S/$src" | grep -iE '^(license|licence)' | head -1); [ -n "$f" ] && cp "$S/$src/$f" "$dst/LICENSE"; }
  echo "$dom|$owner|$name|https://github.com/$owner/tree/HEAD/${p#./}|$kind" >> "$R/.manifest"
}
cp_skill(){ local p=$3; [ -f "$S/$2/$p/SKILL.md" ] || { echo "MISS $2/$p" >&2; return; }; _copy skill "$1" "$2" "$p" "${4:-$(basename "$p")}"; }
cp_plugin(){ [ -d "$S/$2/$3" ] || { echo "MISS $2/$3" >&2; return; }; _copy plugin "$1" "$2" "$3" "${4:-$(basename "$3")}"; }
root(){ (cd "$S/$1" && dirname "$(find . -name SKILL.md -not -path './.git/*' | head -1)"); }
each(){ (cd "$S/$1" && ls -d $2 2>/dev/null); }   # glob of skill dirs
allin(){ (cd "$S/$1" && find . -name SKILL.md -not -path './.git/*' -printf '%h\n' | sed 's|^\./||'); }

# ---------------- 01 WEB DESIGN
for s in frontend-design web-artifacts-builder canvas-design theme-factory; do cp_skill $W anthropics_skills skills/$s; done
for s in ui-ux-pro-max design-system ui-styling design brand banner-design; do cp_skill $W nextlevelbuilder_ui-ux-pro-max-skill .claude/skills/$s; done
cp_skill $W Leonxlnx_taste-skill "$(root Leonxlnx_taste-skill)" taste-skill
cp_skill $W Dammyjay93_interface-design "$(root Dammyjay93_interface-design)" interface-design
cp_skill $W pbakaus_impeccable .claude/skills/impeccable
cp_skill $W KAOPU-XiaoPu_web-design "$(root KAOPU-XiaoPu_web-design)" web-design-spec-first
for s in web-design-guidelines react-best-practices composition-patterns react-view-transitions; do cp_skill $W vercel-labs_agent-skills skills/$s; done
for s in stitch-utilities/skills/design-md stitch-utilities/skills/taste-design stitch-utilities/skills/enhance-prompt stitch-design/skills/extract-design-md stitch-build/skills/shadcn-ui stitch-build/skills/react-components; do cp_skill $W google-labs-code_stitch-skills plugins/$s; done
for s in accessibility-audit accessibility-diff accessibility-fix accessibility-inspect accessibility-scan; do cp_skill $W accesslint_claude-marketplace plugins/accesslint/skills/$s; done
for p in $(each Owl-Listener_designer-skills "ui-design/skills/* interaction-design/skills/* design-systems/skills/* visual-critique/skills/*") prototyping-testing/skills/heuristic-evaluation design-ops/skills/design-qa-checklist; do cp_skill $W Owl-Listener_designer-skills $p; done
for p in $(each wshobson_agents "plugins/ui-design/skills/*") plugins/frontend-mobile-development/skills/tailwind-design-system plugins/frontend-mobile-development/skills/nextjs-app-router-patterns plugins/brand-landingpage/skills/brand-landingpage plugins/accessibility-compliance/skills/wcag-audit-patterns; do cp_skill $W wshobson_agents $p; done
for p in $(each CloudAI-X_threejs-skills "skills/*"); do cp_skill $W CloudAI-X_threejs-skills $p; done
for p in $(each greensock_gsap-skills "skills/gsap-*"); do cp_skill $W greensock_gsap-skills $p; done
for r in web-animation-skills webgl-animation-skills javascript-animation-skills; do for p in $(allin iart-ai_$r); do cp_skill $W iart-ai_$r "$p"; done; done
cp_skill $W 199-biotechnologies_motion-dev-animations-skill "$(root 199-biotechnologies_motion-dev-animations-skill)" motion-dev-animations
cp_skill $W alonw0_web-asset-generator "$(root alonw0_web-asset-generator)" web-asset-generator
cp_skill $W zarazhangrui_frontend-slides "$(root zarazhangrui_frontend-slides)" frontend-slides
for s in accessibility frontend-a11y frontend-design-direction frontend-patterns design-system liquid-glass-design make-interfaces-feel-better taste taste-application taste-distillation react-patterns react-performance nextjs-turbopack vite-patterns seo ui-demo dashboard-builder browser-qa click-path-audit; do cp_skill $W affaan-m_everything-claude-code skills/$s ecc-$s; done

# ---------------- 02 MOTION DESIGN
for p in $(each iart-ai_motion-design-skills "skills/*"); do cp_skill $M iart-ai_motion-design-skills $p; done
for r in kinetic-typography-skills ad-video-skills tiktok-video-skills youtube-video-skills manim-skills data-animation-skills explainer-video-skills b-roll-skills lower-thirds-skills; do
  for p in $(allin iart-ai_$r); do if [ "$p" = "." ]; then cp_skill $M iart-ai_$r . ${r%-skills}; else cp_skill $M iart-ai_$r "$p"; fi; done; done
for p in $(each charlie947_motion-graphics-skills "skills/*"); do cp_skill $M charlie947_motion-graphics-skills $p; done
cp_skill $M howseen-ai_claude-motion-design "$(root howseen-ai_claude-motion-design)" claude-motion-design
cp_skill $M JakeB-5_motion-graphic-skill "$(root JakeB-5_motion-graphic-skill)" motion-graphic-canvas
cp_skill $M fernandokaraka_remotion-motion-graphics-skill "$(root fernandokaraka_remotion-motion-graphics-skill)" remotion-motion-graphics
cp_skill $M haidrrrry_claude-remotion-skill "$(root haidrrrry_claude-remotion-skill)" claude-remotion
cp_skill $M google-labs-code_stitch-skills plugins/stitch-build/skills/remotion stitch-remotion
for s in remotion-video-creation manim-video motion-foundations motion-patterns motion-advanced video-editing tasteforge-video fal-ai-media blender-motion-state-inspection; do cp_skill $M affaan-m_everything-claude-code skills/$s ecc-$s; done
for p in $(each EL4CTEO_blender-skills "skills/*"); do cp_skill $M EL4CTEO_blender-skills $p; done
for p in $(each ra100_blender-claude-plugin "skills/*"); do cp_skill $M ra100_blender-claude-plugin $p blender-lab-mcp--$(basename $p); done
cp_skill $M AndreiFlau_blender-mcp-skill . blender-mcp-bridge
for s in algorithmic-art slack-gif-creator; do cp_skill $M anthropics_skills skills/$s; done
for s in design-systems/skills/motion-system interaction-design/skills/animation-principles; do cp_skill $M Owl-Listener_designer-skills $s ui-$(basename $s); done

# ---------------- 03 CODE / BACKEND / WORKFLOW
for p in $(each obra_superpowers "skills/*"); do cp_skill $C obra_superpowers $p; done
for p in $(each mattpocock_skills "skills/engineering/* skills/productivity/*") skills/misc/git-guardrails-claude-code skills/misc/setup-pre-commit skills/in-progress/claude-handoff; do cp_skill $C mattpocock_skills $p; done
cp_skill $C OthmanAdi_planning-with-files skills/planning-with-files
for p in $(each muratcankoylan_Agent-Skills-for-Context-Engineering "skills/*"); do cp_skill $C muratcankoylan_Agent-Skills-for-Context-Engineering $p; done
for s in backend-patterns api-design api-connector-builder architecture-decision-records hexagonal-architecture contract-first database-migrations postgres-patterns redis-patterns prisma-patterns docker-patterns kubernetes-patterns deployment-patterns error-handling fastapi-patterns nestjs-patterns golang-patterns python-patterns typescript-patterns rust-patterns latency-critical-systems security-review security-scan tdd-workflow verification-loop e2e-testing ai-regression-testing context-budget strategic-compact token-budget-advisor prompt-caching-strategy continuous-learning-v2 autonomous-loops agentic-engineering agent-harness-construction parallel-execution-optimizer search-first iterative-retrieval codebase-onboarding code-tour git-workflow github-ops production-audit plan-orchestrate dmux-workflows team-agent-orchestration safety-guard gateguard cost-aware-llm-pipeline eval-harness skill-stocktake rules-distill config-gc context-and-decisions coding-standards benchmark; do cp_skill $C affaan-m_everything-claude-code skills/$s ecc-$s; done
for s in api-designer architecture-designer chaos-engineer cli-developer cloud-architect code-documenter code-reviewer database-optimizer debugging-wizard devops-engineer django-expert fastapi-expert feature-forge fullstack-guardian golang-pro graphql-architect java-architect kubernetes-specialist laravel-specialist legacy-modernizer mcp-developer microservices-architect monitoring-expert nestjs-expert postgres-pro python-pro rag-architect rails-expert rust-engineer secure-code-guardian security-reviewer spec-miner spring-boot-engineer sql-pro sre-engineer terraform-engineer test-master the-fool typescript-pro websocket-engineer; do cp_skill $C Jeffallan_claude-skills skills/$s; done
for p in $(each wshobson_agents/plugins "backend-development/skills/* developer-essentials/skills/* python-development/skills/* conductor/skills/* agent-teams/skills/* cicd-automation/skills/* observability-monitoring/skills/* incident-response/skills/* systems-programming/skills/* documentation-generation/skills/*") javascript-typescript/skills/nodejs-backend-patterns javascript-typescript/skills/typescript-advanced-types database-design/skills/postgresql-table-design framework-migration/skills/database-migration framework-migration/skills/dependency-upgrade payment-processing/skills/stripe-integration shell-scripting/skills/bash-defensive-patterns before-you-build/skills/before-you-build skill-forge-essentials/skills/session-guard skill-forge-essentials/skills/ai-debt-detector llm-application-dev/skills/rag-implementation llm-application-dev/skills/prompt-engineering-patterns api-scaffolding/skills/fastapi-templates; do cp_skill $C wshobson_agents plugins/$p; done
for p in differential-review/skills/differential-review static-analysis/skills/semgrep static-analysis/skills/codeql static-analysis/skills/sarif-parsing property-based-testing/skills/property-based-testing mutation-testing/skills/mutation-testing modern-python/skills/modern-python gh-cli/skills/gh-cli second-opinion/skills/second-opinion sharp-edges/skills/sharp-edges supply-chain-risk-auditor/skills/supply-chain-risk-auditor code-improver/skills/code-improver code-improver/skills/pr-improver devcontainer-setup/skills/devcontainer-setup entry-point-analyzer/skills/entry-point-analyzer variant-analysis/skills/variant-analysis fp-check/skills/fp-check patching-bugs/skills/patching-bugs regression-hunt/skills/regression-hunt; do cp_skill $C trailofbits_skills plugins/$p; done
for s in mcp-builder skill-creator webapp-testing claude-api; do cp_skill $C anthropics_skills skills/$s; done
for s in gh-fix-ci gh-address-comments security-best-practices security-threat-model sentry playwright cli-creator; do cp_skill $C openai_skills skills/.curated/$s openai-$s; done
cp_skill $C lackeyjb_playwright-skill "$(root lackeyjb_playwright-skill)" playwright-skill

# ---------------- 04 AUTOMATIONS (plugins = hooks + commands + agents + skills)
for p in hookify claude-code-setup claude-md-management session-report security-guidance commit-commands pr-review-toolkit feature-dev code-simplifier ralph-loop plugin-dev mcp-server-dev; do cp_plugin $A anthropics_claude-plugins-official plugins/$p; done
for p in $(each karanb192_claude-code-hooks "plugins/*"); do cp_plugin $A karanb192_claude-code-hooks $p; done
cp_plugin $A BayramAnnakov_claude-reflect . claude-reflect
cp_plugin $A affaan-m_everything-claude-code commands ecc-commands

# plugin manifests for folders that ship without one
mkp(){ [ -f "$1/.claude-plugin/plugin.json" ] || { mkdir -p "$1/.claude-plugin"; printf '{\n  "name": "%s",\n  "description": "%s"\n}\n' "$2" "$3" > "$1/.claude-plugin/plugin.json"; }; }
mkp "$R/$A/affaan-m/everything-claude-code/ecc-commands" ecc-commands "Everything Claude Code slash commands (plan, tdd, code-review, multi-agent orchestration, quality gates)"
mkp "$R/$A/anthropics/claude-plugins-official/session-report" session-report "Session usage report: tokens, cache, subagents, skills"
