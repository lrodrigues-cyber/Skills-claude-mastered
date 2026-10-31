# Skills Claude Mastered

4 packs Claude Code (skills + automations), sélectionnés parmi les meilleurs publics — officiels + communauté — repérés sur GitHub, X, YouTube, TikTok, Instagram et les registres de skills. Base de travail → amélioration ultérieure.

| Pack | Contenu | Nb |
|---|---|---|
| [01-web-design](01-web-design) | Design web, UI/UX, design systems, accessibilité, GSAP, Motion.dev, Three.js/WebGL | 160 skills |
| [02-motion-design](02-motion-design) | Remotion, HTML/canvas motion, Manim, formats pub/TikTok/YouTube, Blender pro | 100 skills |
| [03-code-backend-workflow](03-code-backend-workflow) | Backend/API/DB, archi, debug, tests, sécurité, CI/CD, context engineering, tokens, workflows de session | 267 skills |
| [04-automations](04-automations) | Plugins : hooks (sécurité, coût, logs), slash commands, agents, auto-amélioration | 36 plugins |

## Installation

**Skills (packs 01–03)**
```bash
./install.sh 02-motion-design            # → ~/.claude/skills
```
```powershell
.\install.ps1 -Pack 02-motion-design
```
Ou copier un seul dossier de skill dans `~/.claude/skills/` (global) ou `.claude/skills/` (projet). Noms en double → le script garde le premier.

**Automations (pack 04)** — ce repo est un marketplace de plugins :
```text
/plugin marketplace add lrodrigues-cyber/Skills-claude-mastered
/plugin install block-dangerous-commands@skills-claude-mastered
```

## Structure

```
<pack>/<auteur>/<repo-source>/<skill|plugin>/   (+ LICENSE d'origine)
<pack>/README.md                                 catalogue : description, licence, lien source
.claude-plugin/marketplace.json                  plugins du pack 04
tools/build.sh · tools/gen.py · .manifest        reconstruction reproductible des packs
```

## Sources principales

- **Officiels** : [anthropics/skills](https://github.com/anthropics/skills), [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official), [openai/skills](https://github.com/openai/skills), [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills), [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills), [greensock/gsap-skills](https://github.com/greensock/gsap-skills)
- **Les plus suivis** : [mattpocock/skills](https://github.com/mattpocock/skills) (308k⭐), [everything-claude-code](https://github.com/affaan-m/everything-claude-code) (294k⭐, vu sur YouTube/TikTok), [obra/superpowers](https://github.com/obra/superpowers), [planning-with-files](https://github.com/OthmanAdi/planning-with-files)
- **Web** : [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), [impeccable](https://github.com/pbakaus/impeccable), [taste-skill](https://github.com/Leonxlnx/taste-skill), [interface-design](https://github.com/Dammyjay93/interface-design), [designer-skills](https://github.com/Owl-Listener/designer-skills), [accesslint](https://github.com/accesslint/claude-marketplace), [threejs-skills](https://github.com/CloudAI-X/threejs-skills), [motion-dev-animations](https://github.com/199-biotechnologies/motion-dev-animations-skill)
- **Motion / Blender** : [iart-ai](https://github.com/iart-ai) (10 repos), [charlie947/motion-graphics-skills](https://github.com/charlie947/motion-graphics-skills), [howseen-ai/claude-motion-design](https://github.com/howseen-ai/claude-motion-design), [EL4CTEO/blender-skills](https://github.com/EL4CTEO/blender-skills), [ra100/blender-claude-plugin](https://github.com/ra100/blender-claude-plugin), [AndreiFlau/blender-mcp-skill](https://github.com/AndreiFlau/blender-mcp-skill)
- **Code / workflow** : [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering), [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills), [wshobson/agents](https://github.com/wshobson/agents), [trailofbits/skills](https://github.com/trailofbits/skills)
- **Automations** : [karanb192/claude-code-hooks](https://github.com/karanb192/claude-code-hooks), [claude-reflect](https://github.com/BayramAnnakov/claude-reflect)

**Référencés, non copiés** (pas de licence, licence restrictive ou runtime dédié) : Remotion officiel, Figma, Karpathy CLAUDE.md, claude-mem, RTK, GSD, Excalidraw, Command Suite, ElevenLabs MCP → liens en bas de chaque README de pack.

## Licences & crédits

Chaque dossier garde sa licence d'origine (MIT, Apache-2.0, CC-BY-SA-4.0 pour Trail of Bits, GPL-3.0 pour blender-mcp-bridge). Tout le mérite revient aux auteurs. Les modifications futures d'un skill CC-BY-SA / GPL restent sous la même licence. Trois plugins sont renommés dans le marketplace (`setup`, `md-management`, `reflect`) car les noms `claude-*` sont réservés à Anthropic.

⚠️ Skills et hooks exécutent du code. Relire `SKILL.md`, `scripts/` et `hooks/` avant usage.

_Collecte : 2026-10-31._
