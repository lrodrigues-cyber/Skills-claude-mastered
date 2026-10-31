# Skills Claude Mastered

3 packs de skills Claude Code, sélectionnés parmi les meilleurs skills publics (officiels + communauté), rangés par domaine. Base de travail → amélioration ultérieure.

| Pack | Contenu | Skills |
|---|---|---|
| [01-web-design](01-web-design) | Design web, UI/UX, design systems, accessibilité, GSAP, Three.js | 125 |
| [02-motion-design](02-motion-design) | Remotion (vidéo en code), principes motion, Blender pro (modélisation → rendu) | 53 |
| [03-code-backend-workflow](03-code-backend-workflow) | Backend/API/DB, archi, debug, tests, sécurité, CI/CD, context engineering, workflows de session | 180 |

## Structure

```
<pack>/<auteur>/<repo-source>/<skill>/SKILL.md   (+ LICENSE d'origine)
<pack>/README.md                                (catalogue : description, licence, lien source)
```

## Installation

```bash
./install.sh 02-motion-design            # → ~/.claude/skills
```
```powershell
.\install.ps1 -Pack 02-motion-design
```
Ou copier un seul dossier de skill dans `~/.claude/skills/` (global) ou `.claude/skills/` (projet). Les noms en double (`accessibility-audit`, `responsive-design` dans le pack web) sont ignorés par le script si déjà installés.

## Sources principales

- **Officiels** : [anthropics/skills](https://github.com/anthropics/skills), [openai/skills](https://github.com/openai/skills), [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills), [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills), [greensock/gsap-skills](https://github.com/greensock/gsap-skills)
- **Web** : [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill), [impeccable](https://github.com/pbakaus/impeccable), [taste-skill](https://github.com/Leonxlnx/taste-skill), [interface-design](https://github.com/Dammyjay93/interface-design), [designer-skills](https://github.com/Owl-Listener/designer-skills), [accesslint](https://github.com/accesslint/claude-marketplace), [threejs-skills](https://github.com/CloudAI-X/threejs-skills)
- **Motion / Blender** : [iart-ai/motion-design-skills](https://github.com/iart-ai/motion-design-skills), [EL4CTEO/blender-skills](https://github.com/EL4CTEO/blender-skills), [ra100/blender-claude-plugin](https://github.com/ra100/blender-claude-plugin), [AndreiFlau/blender-mcp-skill](https://github.com/AndreiFlau/blender-mcp-skill)
- **Code / workflow** : [obra/superpowers](https://github.com/obra/superpowers), [Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering), [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills), [wshobson/agents](https://github.com/wshobson/agents), [trailofbits/skills](https://github.com/trailofbits/skills)

Skills référencés mais **non copiés** (pas de licence ou licence restrictive : Remotion officiel, Figma, GSD, Excalidraw) → liens + commande d'install en bas de chaque README de pack.

## Licences & crédits

Chaque skill garde sa licence d'origine dans son dossier (MIT, Apache-2.0, CC-BY-SA-4.0 pour Trail of Bits, GPL-3.0 pour blender-mcp-bridge). Tout le mérite revient aux auteurs listés. Les modifications futures d'un skill CC-BY-SA / GPL doivent rester sous la même licence.

⚠️ Les skills peuvent exécuter du code (scripts). Relire `SKILL.md` + `scripts/` avant usage.

_Collecte : 2026-10-31._
