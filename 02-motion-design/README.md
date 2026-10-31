# 🎬 Motion Design & 3D (Remotion · Blender)

Vidéo en code (Remotion), principes d'animation, direction artistique motion, Blender (modélisation, rigging, lookdev, rendu) piloté par Claude.

**53 skills** issus de 9 sources. Chaque skill = dossier autonome (`SKILL.md` + ressources) + sa licence d'origine.

## Installation

```bash
# un skill
cp -r 02-motion-design/<auteur>/<repo>/<skill> ~/.claude/skills/
# tout le pack
./install.sh 02-motion-design
```

## [EL4CTEO/blender-skills](https://github.com/EL4CTEO/blender-skills)  · 28 skills

| Skill | Licence | Description |
|---|---|---|
| [`blender-addon-development`](EL4CTEO/blender-skills/blender-addon-development) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-addon-development) | MIT | Write Blender 5.2 add-ons as extensions - blender_manifest.toml, operators/panels/menus/property groups/preferences, bpy.props rules after 5.0, undo/redo, modal and timer patterns,… |
| [`blender-animation`](EL4CTEO/blender-skills/blender-animation) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-animation) | MIT | Animation in Blender 5.2 - slotted/layered actions and the channelbag API, Python keyframing, F-curves, game loops with pop/hitch checks, NLA clips, pose library, mocap/BVH/Mixamo … |
| [`blender-asset-qa`](EL4CTEO/blender-skills/blender-asset-qa) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-asset-qa) | MIT | Mandatory review gate for any mesh or asset created or edited in Blender. Detects z-fighting, floating/detached parts, inverted or inconsistent normals, non-manifold/open geometry,… |
| [`blender-character-rigging`](EL4CTEO/blender-skills/blender-character-rigging) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-character-rigging) | MIT | Character rigging in Blender 5.2 - Rigify metarig fit/generate, bone naming/roll/collections, DEF/MCH/control layers, IK/FK, robust skinning (heat + proxy fallback), weight-paintin… |
| [`blender-clothing`](EL4CTEO/blender-skills/blender-clothing) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-clothing) | MIT | Game clothing in Blender 5.2 - garments from body regions (ease offset, thickness), skin-weight transfer, hiding covered body faces, cloth-sim draping for folds, body-morph shape k… |
| [`blender-core`](EL4CTEO/blender-skills/blender-core) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-core) | MIT | Foundation for any Blender 5.2+ task an agent drives - running bpy via MCP (live) or headless CLI, context overrides, locale-safe node lookup, enum discovery, 5.x API changes, veri… |
| [`blender-environment-kits`](EL4CTEO/blender-skills/blender-environment-kits) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-environment-kits) | MIT | Game environments in Blender 5.2 - terrain from noise or heightmaps (erosion, terraces, play areas, slope/height materials, 16-bit heightmaps + splat maps for UE/Unity), biome scat… |
| [`blender-export-pipelines`](EL4CTEO/blender-skills/blender-export-pipelines) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-export-pipelines) | MIT | Export from Blender 5.2 with verified presets - Roblox (FBX/glTF, cages, R15, SurfaceAppearance), Unity (FBX, Humanoid), Unreal (FBX skeletal, Nanite, UCX), Godot/web (GLB, meshopt… |
| [`blender-facial-shapekeys`](EL4CTEO/blender-skills/blender-facial-shapekeys) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-facial-shapekeys) | MIT | Facial rigs and shape keys in Blender 5.2 - ARKit 52 blendshapes, visemes for lip-sync, sculpting expressions, splitting symmetric shapes into Left/Right, mirroring, corrective and… |
| [`blender-game-optimization`](EL4CTEO/blender-skills/blender-game-optimization) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-game-optimization) | MIT | Optimize Blender assets for real-time engines - triangle/material/texture/bone budgets per platform (mobile, Roblox, web, VR, console, PC), LOD chains, decimation modes, mesh clean… |
| [`blender-geometry-nodes`](EL4CTEO/blender-skills/blender-geometry-nodes) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-geometry-nodes) | MIT | Geometry Nodes in Blender 5.2 - fields, domains, attributes, instancing, zones (simulation/repeat/for-each), closures/bundles, lists, SDF grids, node tools, baking, plus a JSON-to-… |
| [`blender-hair-grooming`](EL4CTEO/blender-skills/blender-hair-grooming) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-hair-grooming) | MIT | Hair and fur in Blender 5.2 - hair curves on a surface, guides + interpolated children with the bundled hair node assets (clump, curl, noise, droop), density masks, Principled Hair… |
| [`blender-hardsurface-modeling`](EL4CTEO/blender-skills/blender-hardsurface-modeling) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-hardsurface-modeling) | MIT | Hard-surface and prop modeling in Blender 5.2 - blockout-to-detail flow, non-destructive modifier stacks (Mirror, Boolean Exact/Manifold, Bevel, Weighted Normal, Smooth by Angle), … |
| [`blender-lighting-lookdev`](EL4CTEO/blender-skills/blender-lighting-lookdev) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-lighting-lookdev) | MIT | Lighting, cameras and look-dev in Blender 5.2 - studio 3-point and product lighting, HDRI environments, sun/sky exteriors, interiors, light linking, physically based light units, c… |
| [`blender-pbr-materials`](EL4CTEO/blender-skills/blender-pbr-materials) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-pbr-materials) | MIT | Physically based materials in Blender 5.2 - metal/roughness rules, Principled BSDF inputs, color spaces (sRGB vs Non-Color), measured albedo/F0 values, texture-set auto-wiring, ORM… |
| [`blender-pipeline-automation`](EL4CTEO/blender-skills/blender-pipeline-automation) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-pipeline-automation) | MIT | Automate Blender 5.2 at scale - headless CLI flags, batch convert/inventory/run-any-skill-script over folders of .blend/.fbx/.glb/.obj/.usd, sharding, bpy pip module, library linki… |
| [`blender-rendering`](EL4CTEO/blender-skills/blender-rendering) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-rendering) | MIT | Render with Blender 5.2 Cycles/EEVEE/Workbench - quality presets, GPU setup, adaptive sampling, denoising, light paths, color management (AgX, Khronos PBR Neutral, ACES), PNG/EXR/M… |
| [`blender-retopology-uv`](EL4CTEO/blender-skills/blender-retopology-uv) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-retopology-uv) | MIT | Retopology and UVs in Blender 5.2 - auto retopo (Quadriflow, Decimate, planar), deformation edge flow, seams, unwrap (Angle Based, Minimum Stretch, Smart), pixel-margin packing, te… |
| [`blender-scene-setup`](EL4CTEO/blender-skills/blender-scene-setup) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-scene-setup) | MIT | Set up and audit Blender scenes the way studios do - units and real-world scale, collection layout, naming conventions (SM_/SK_/T_/M_), origins, linking vs appending, library overr… |
| [`blender-sculpting`](EL4CTEO/blender-skills/blender-sculpting) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-sculpting) | MIT | Sculpting in Blender 5.2 - base-to-detail workflow, voxel remesh, dyntopo, multires, 5.x brush types, masks/face sets, symmetry, plus headless-safe procedural ops for agents (remes… |
| [`blender-simulation`](EL4CTEO/blender-skills/blender-simulation) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-simulation) | MIT | Physics in Blender 5.2 - rigid bodies (density mass, shapes, bake to keys), classic cloth presets and pinning, new node-based Cloth/Hair Dynamics (XPBD, Collider, effectors), Manta… |
| [`blender-stylized-npr`](EL4CTEO/blender-skills/blender-stylized-npr) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-stylized-npr) | MIT | Stylized / NPR looks in Blender 5.2 - toon and cel shading (bands, shadow tint, rim, hard specular), anime faces with custom normals, inverted-hull outlines with smoothed outline n… |
| [`blender-texture-baking`](EL4CTEO/blender-skills/blender-texture-baking) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-texture-baking) | MIT | Bake texture maps in Blender 5.2 Cycles - high-to-low normal maps with cage/extrusion, AO, curvature, ID, thickness, base color/roughness/metallic from procedurals, ORM packing, Op… |
| [`blender-texturing`](EL4CTEO/blender-skills/blender-texturing) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-texturing) | MIT | Texture authoring in Blender 5.2 - smart-material layers (edge wear, cavity grime, dust, rust, roughness breakup) from curvature/AO masks, z-fight-safe decal and sticker placement,… |
| [`blender-time-of-day`](EL4CTEO/blender-skills/blender-time-of-day) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-time-of-day) | MIT | Time of day and atmosphere in Blender 5.2 - measured sky + sun for dawn, morning, noon, golden hour, sunset, blue hour, overcast, night/moonlight with stars and city glow, exposure… |
| [`blender-video-editing`](EL4CTEO/blender-skills/blender-video-editing) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-video-editing) | MIT | Video in Blender 5.2 - Video Sequencer edits from Python (clips, image sequences, crossfades, titles, music fades, proxies, color management, H.264/AAC output) and motion tracking … |
| [`blender-weather-fx`](EL4CTEO/blender-skills/blender-weather-fx) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-weather-fx) | MIT | Weather effects in Blender 5.2 - looping Geometry Nodes rain, snow, dust, ash and embers with ground hits and splashes, wet surfaces, puddles with animated ripples, wall streaks, s… |
| [`blender-workflow-recipes`](EL4CTEO/blender-skills/blender-workflow-recipes) · [src](https://github.com/EL4CTEO/blender-skills/tree/HEAD/skills/blender-workflow-recipes) | MIT | End-to-end Blender 5.2 playbooks chaining the blender-* skills with QA gates - game props (mid-poly, high-to-low), game characters (sculpt/AI mesh to rigged, animated export), Robl… |

## [iart-ai/motion-design-skills](https://github.com/iart-ai/motion-design-skills)  · 9 skills

| Skill | Licence | Description |
|---|---|---|
| [`after-effects`](iart-ai/motion-design-skills/after-effects) · [src](https://github.com/iart-ai/motion-design-skills/tree/HEAD/skills/after-effects) | MIT | This skill should be used when the user asks anything about Adobe After Effects — to "write an After Effects expression", "make a wiggle / loopOut / inertial bounce", "rig a contro… |
| [`animation-principles`](iart-ai/motion-design-skills/animation-principles) · [src](https://github.com/iart-ai/motion-design-skills/tree/HEAD/skills/animation-principles) | MIT | This skill should be used when the user asks to "make this animation feel natural", "fix motion that feels stiff/floaty/cheap", "my animation looks robotic", "choose an easing curv… |
| [`beat-sync-editing`](iart-ai/motion-design-skills/beat-sync-editing) · [src](https://github.com/iart-ai/motion-design-skills/tree/HEAD/skills/beat-sync-editing) | MIT | This skill should be used when the user asks to "cut to the beat", "fix the pacing", "edit this sequence", "sync cuts to music/BPM", "add a match cut / J-cut / L-cut", "build a spe… |
| [`color-motion`](iart-ai/motion-design-skills/color-motion) · [src](https://github.com/iart-ai/motion-design-skills/tree/HEAD/skills/color-motion) | MIT | This skill should be used when the user asks to "build a color palette for a motion piece", "make a gradient background", "animate a color transition", "interpolate colors smoothly… |
| [`logo-animation`](iart-ai/motion-design-skills/logo-animation) · [src](https://github.com/iart-ai/motion-design-skills/tree/HEAD/skills/logo-animation) | MIT | This skill should be used when the user asks to "animate our logo", "make a logo intro/stinger", "build a brand reveal", "create an app splash animation", "loop a loader logo", "dr… |
| [`motion-art-direction`](iart-ai/motion-design-skills/motion-art-direction) · [src](https://github.com/iart-ai/motion-design-skills/tree/HEAD/skills/motion-art-direction) | MIT | This skill should be used when the user asks to "direct a motion graphics video", "do creative/art direction for a video", "define a motion language", "set the tone and pacing", "m… |
| [`motion-background`](iart-ai/motion-design-skills/motion-background) · [src](https://github.com/iart-ai/motion-design-skills/tree/HEAD/skills/motion-background) | MIT | This skill should be used when the user asks to "add an animated background", "build a mesh/gradient background", "make an aurora/shader background", "add constellation/particle ba… |
| [`remotion-video`](iart-ai/motion-design-skills/remotion-video) · [src](https://github.com/iart-ai/motion-design-skills/tree/HEAD/skills/remotion-video) | MIT | This skill should be used when the user asks to "make a video with Remotion", "create a programmatic/data-driven video in React", "render an MP4/GIF from code", "animate with useCu… |
| [`shot-composition`](iart-ai/motion-design-skills/shot-composition) · [src](https://github.com/iart-ai/motion-design-skills/tree/HEAD/skills/shot-composition) | MIT | This skill should be used when the user asks to "compose a frame", "set up a grid", "plan shot composition", "place the focal point", "decide where elements enter and exit", "add a… |

## [ra100/blender-claude-plugin](https://github.com/ra100/blender-claude-plugin)  · 8 skills

| Skill | Licence | Description |
|---|---|---|
| [`blender-lab-mcp--blender-animation-rigging`](ra100/blender-claude-plugin/blender-lab-mcp--blender-animation-rigging) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-animation-rigging) | MIT | Blender 5.x animation and rigging — keyframes, FCurves, layered actions, drivers, constraints, armatures, IK/FK, shape keys, NLA editor, and bone collections via Python (bpy). Incl… |
| [`blender-lab-mcp--blender-compositing-nodes`](ra100/blender-claude-plugin/blender-lab-mcp--blender-compositing-nodes) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-compositing-nodes) | MIT | Blender 5.x compositor nodes — post-processing, color grading, denoising, keying, glare, depth of field, render pass separation, multi-layer EXR output, and scripting compositing p… |
| [`blender-lab-mcp--blender-geometry-nodes`](ra100/blender-claude-plugin/blender-lab-mcp--blender-geometry-nodes) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-geometry-nodes) | MIT | Blender 5.x geometry nodes — procedural modeling, scattering, mesh/curve/volume ops, simulation zones, repeat zones, Bone Info, Font socket, UV nodes, volume grid nodes, and script… |
| [`blender-lab-mcp--blender-modeling-modifiers`](ra100/blender-claude-plugin/blender-lab-mcp--blender-modeling-modifiers) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-modeling-modifiers) | MIT | Blender 5.x modifiers, bmesh API, mesh editing operators, sculpting setup — SubSurf, Boolean, Array, Mirror, Bevel, bmesh procedural mesh creation, and modeling pipelines via Pytho… |
| [`blender-lab-mcp--blender-physics-simulation`](ra100/blender-claude-plugin/blender-lab-mcp--blender-physics-simulation) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-physics-simulation) | MIT | Blender 5.x physics simulations — rigid body, cloth, fluid/smoke/fire (Mantaflow), soft body, particles, force fields, collisions, and simulation baking/caching via Python (bpy). |
| [`blender-lab-mcp--blender-python-scripting`](ra100/blender-claude-plugin/blender-lab-mcp--blender-python-scripting) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-python-scripting) | MIT | Blender 5.x Python scripting (bpy) — custom operators, UI panels, add-on development, context management, handlers, timers, property system, batch processing, and data model access… |
| [`blender-lab-mcp--blender-scene-rendering`](ra100/blender-claude-plugin/blender-lab-mcp--blender-scene-rendering) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-scene-rendering) | MIT | Blender 5.x scene setup, render engines (Cycles/EEVEE), output formats, import/export (FBX/glTF/OBJ/USD/Alembic), linking/appending, color management (AgX/Filmic), view layers, vie… |
| [`blender-lab-mcp--blender-shader-nodes`](ra100/blender-claude-plugin/blender-lab-mcp--blender-shader-nodes) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-shader-nodes) | MIT | Blender 5.x shader nodes — PBR materials, procedural textures, Principled BSDF, glass/metal/skin shaders, world/HDRI lighting, raycast shader node, and scripting material node tree… |

## [anthropics/skills](https://github.com/anthropics/skills)  · 2 skills

| Skill | Licence | Description |
|---|---|---|
| [`algorithmic-art`](anthropics/skills/algorithmic-art) · [src](https://github.com/anthropics/skills/tree/HEAD/skills/algorithmic-art) | Apache-2.0 | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic … |
| [`slack-gif-creator`](anthropics/skills/slack-gif-creator) · [src](https://github.com/anthropics/skills/tree/HEAD/skills/slack-gif-creator) | Apache-2.0 | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Sla… |

## [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills)  · 2 skills

| Skill | Licence | Description |
|---|---|---|
| [`ui-animation-principles`](Owl-Listener/designer-skills/ui-animation-principles) · [src](https://github.com/Owl-Listener/designer-skills/tree/HEAD/interaction-design/skills/animation-principles) | MIT | Apply animation principles — easing, staging, follow-through — to one specific UI motion. Use when tuning how an animation feels. For product-wide duration and easing tokens use `m… |
| [`ui-motion-system`](Owl-Listener/designer-skills/ui-motion-system) · [src](https://github.com/Owl-Listener/designer-skills/tree/HEAD/design-systems/skills/motion-system) | MIT | Define motion tokens — durations, easing vocabulary, and reduced-motion handling — for consistency product-wide. Use when standardising motion across a system. For crafting one spe… |

## [fernandokaraka/remotion-motion-graphics-skill](https://github.com/fernandokaraka/remotion-motion-graphics-skill)  · 1 skills

| Skill | Licence | Description |
|---|---|---|
| [`remotion-motion-graphics`](fernandokaraka/remotion-motion-graphics-skill/remotion-motion-graphics) · [src](https://github.com/fernandokaraka/remotion-motion-graphics-skill/tree/HEAD/skills/remotion-motion-graphics) | MIT | Build animated motion graphics as real video with Remotion (React-based programmatic video) — title cards, lower thirds, logo stings, badges, stat reveals, countdowns, end screens,… |

## [haidrrrry/claude-remotion-skill](https://github.com/haidrrrry/claude-remotion-skill)  · 1 skills

| Skill | Licence | Description |
|---|---|---|
| [`claude-remotion`](haidrrrry/claude-remotion-skill/claude-remotion) · [src](https://github.com/haidrrrry/claude-remotion-skill/tree/HEAD/remotion-motion-graphics) | MIT | Create and edit professional motion graphics videos with Remotion (React-based video). Use this skill EVERY time the user wants to create a video, edit a video, animate something, … |

## [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)  · 1 skills

| Skill | Licence | Description |
|---|---|---|
| [`stitch-remotion`](google-labs-code/stitch-skills/stitch-remotion) · [src](https://github.com/google-labs-code/stitch-skills/tree/HEAD/plugins/stitch-build/skills/remotion) | Apache-2.0 | Generate walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays |

## [AndreiFlau/blender-mcp-skill](https://github.com/AndreiFlau/blender-mcp-skill)  · 1 skills

| Skill | Licence | Description |
|---|---|---|
| [`blender-mcp-bridge`](AndreiFlau/blender-mcp-skill/blender-mcp-bridge) · [src](https://github.com/AndreiFlau/blender-mcp-skill/tree/HEAD/.) | GPL-3.0 (README) | Execute Python inside a live Blender session via the official Blender Labs MCP extension (TCP localhost:9876) — for building/testing Blender addons, inspecting scenes, running oper… |

## 🔗 Référencés (non copiés — licence ou format)

- [Remotion — skills officiels (remotion-best-practices, render, captions…)](https://github.com/remotion-dev/skills) — Pas de licence publiée → installer : `npx skills add remotion-dev/skills`
- [Blender MCP (ahujasid) — serveur MCP](https://github.com/ahujasid/blender-mcp) — MCP serveur (pas un skill) : à coupler avec les skills Blender ci-dessous
- [Blender Lab MCP officiel (Blender ≥ 5.1)](https://github.com/ra100/blender-claude-plugin) — Requis pour les skills `blender-lab-mcp--*`
