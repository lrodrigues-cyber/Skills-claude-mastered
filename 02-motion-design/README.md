# 🎬 Motion Design & 3D (Remotion · Blender · Manim)

Vidéo en code (Remotion, HTML/canvas, Manim), principes d'animation, formats pub/TikTok/YouTube, Blender pro (modélisation → rigging → lookdev → rendu) piloté par Claude.

**100 skills** issus de 22 sources. Chaque dossier garde sa licence d'origine.

## Installation

```bash
cp -r 02-motion-design/<auteur>/<repo>/<skill> ~/.claude/skills/   # un skill
./install.sh 02-motion-design                                    # tout le pack
```

## [EL4CTEO/blender-skills](https://github.com/EL4CTEO/blender-skills) · 28

| Nom | Licence | Description |
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

## [charlie947/motion-graphics-skills](https://github.com/charlie947/motion-graphics-skills) · 15

| Nom | Licence | Description |
|---|---|---|
| [`animated-chart`](charlie947/motion-graphics-skills/animated-chart) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/animated-chart) | MIT | Make a looping animated chart for LinkedIn or a newsletter in code with Claude Code. Bars that become a line, a number that counts up, a before and after. Every value stays exactly… |
| [`apple-launch-film`](charlie947/motion-graphics-skills/apple-launch-film) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/apple-launch-film) | MIT | Rebuild an Apple-style Mac launch film entirely in code with Claude Code. A thin menu bar, the black notch growing into widgets one scene at a time, full-screen gradient wallpapers… |
| [`brand-intake`](charlie947/motion-graphics-skills/brand-intake) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/brand-intake) | MIT | The setup step every other skill in this pack reads. A short interview plus 3 to 5 reference frames becomes two files in your project, brand.md (who you are, what you sell, your as… |
| [`launch-video`](charlie947/motion-graphics-skills/launch-video) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/launch-video) | MIT | Make a 30-45 second product launch video in code with Claude Code, the kind SaaS companies post on launch day. One sentence split across scenes, real product screens with slow came… |
| [`loop-cover`](charlie947/motion-graphics-skills/loop-cover) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/loop-cover) | MIT | Turn a newsletter or blog cover into a seamless looping GIF at 896 x 640, 180 frames at 20fps. Only the one element you name moves, the loop is rotated so frame 1 shows the finishe… |
| [`milestone-reveal`](charlie947/motion-graphics-skills/milestone-reveal) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/milestone-reveal) | MIT | Make a 12-second looping milestone clip in code with Claude Code. Thousands of tiny points drift like a night sky, pull together into your real number (followers, subscribers, reve… |
| [`model-showdown`](charlie947/motion-graphics-skills/model-showdown) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/model-showdown) | MIT | Give the same motion brief to three AI models, keep each first try, render all three the same way and stack them into one comparison video with model names and logos. Makes a 16:9 … |
| [`motion-brief-writer`](charlie947/motion-graphics-skills/motion-brief-writer) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/motion-brief-writer) | MIT | Turns a rough idea for an animated graphic into a precise build brief for Claude Code, in your own brand. Asks for anything essential first (exact numbers, size, length, brand), ke… |
| [`motion-effects`](charlie947/motion-graphics-skills/motion-effects) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/motion-effects) | MIT | Build any of 16 premium motion effects from scratch in your own brand, as one 8-second looping HTML file with window.seek(seconds) so it exports frame-exact to MP4 or GIF. Interfac… |
| [`motion-prompt-writer`](charlie947/motion-graphics-skills/motion-prompt-writer) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/motion-prompt-writer) | MIT | Write a complete 8-part Claude Motion prompt (The bar, Format, The one rule, Look, Motion, Never, Before you finish, The scene) for one short looping motion graphic, in your own br… |
| [`newsletter-promo`](charlie947/motion-graphics-skills/newsletter-promo) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/newsletter-promo) | MIT | Turn a newsletter edition into a 12-20 second promo clip for LinkedIn, Instagram or X that drives people to read and subscribe. Hook question, three proof frames from the edition, … |
| [`reel-export`](charlie947/motion-graphics-skills/reel-export) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/reel-export) | MIT | Turn any horizontal or square motion video into a 1080 x 1920 Instagram Reel or TikTok that uploads cleanly. Headline and logos inside the safe zone, H.264, yuv420p, limited colour… |
| [`reference-to-motion`](charlie947/motion-graphics-skills/reference-to-motion) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/reference-to-motion) | MIT | Turn references you admire into a scene-by-scene Claude Motion prompt for your own topic and brand. Takes a video for the moves (screenshots, frames or a contact sheet of a reel or… |
| [`title-sequence-3d`](charlie947/motion-graphics-skills/title-sequence-3d) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/title-sequence-3d) | MIT | Make a cinematic 3D title sequence (8-15 seconds) in code with Claude Code and Three.js. A camera moves through a lit scene, such as a rainy street at night with brand names as neo… |
| [`vox-explainer`](charlie947/motion-graphics-skills/vox-explainer) · [src](https://github.com/charlie947/motion-graphics-skills/tree/HEAD/skills/vox-explainer) | MIT | Make a short Vox-style documentary explainer (30-60 seconds) entirely in code with Claude Code. Torn paper, halftone texture, bold condensed type, motion on twos. Use when someone … |

## [iart-ai/motion-design-skills](https://github.com/iart-ai/motion-design-skills) · 9

| Nom | Licence | Description |
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

## [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) · 9

| Nom | Licence | Description |
|---|---|---|
| [`ecc-blender-motion-state-inspection`](affaan-m/everything-claude-code/ecc-blender-motion-state-inspection) · [src](https://github.com/affaan-m/everything-claude-code/tree/HEAD/skills/blender-motion-state-inspection) | MIT | Use this skill when inspecting Blender characters, rigs, poses, animation retargeting, ground contact, facing direction, or model-vs-motion alignment where screenshots alone are no… |
| [`ecc-fal-ai-media`](affaan-m/everything-claude-code/ecc-fal-ai-media) · [src](https://github.com/affaan-m/everything-claude-code/tree/HEAD/skills/fal-ai-media) | MIT | Unified media generation via fal.ai MCP — image, video, and audio. Covers text-to-image (Nano Banana), text/image-to-video (Seedance, Kling, Veo 3), text-to-speech (CSM-1B), and vi… |
| [`ecc-manim-video`](affaan-m/everything-claude-code/ecc-manim-video) · [src](https://github.com/affaan-m/everything-claude-code/tree/HEAD/skills/manim-video) | MIT | Build reusable Manim explainers for technical concepts, graphs, system diagrams, and product walkthroughs, then hand off to the wider ECC video stack if needed. Use when the user w… |
| [`ecc-motion-advanced`](affaan-m/everything-claude-code/ecc-motion-advanced) · [src](https://github.com/affaan-m/everything-claude-code/tree/HEAD/skills/motion-advanced) | MIT | Advanced motion patterns for React / Next.js — drag & drop, gestures, text animations, SVG path drawing, custom hooks, imperative sequences (useAnimate), loaders, and the full API … |
| [`ecc-motion-foundations`](affaan-m/everything-claude-code/ecc-motion-foundations) · [src](https://github.com/affaan-m/everything-claude-code/tree/HEAD/skills/motion-foundations) | MIT | Motion tokens, spring presets, performance rules, device adaptation, accessibility enforcement, and SSR safety for React / Next.js using motion/react. Foundation layer — all other … |
| [`ecc-motion-patterns`](affaan-m/everything-claude-code/ecc-motion-patterns) · [src](https://github.com/affaan-m/everything-claude-code/tree/HEAD/skills/motion-patterns) | MIT | Production-ready animation patterns for React / Next.js — button, modal, toast, stagger, page transitions, exit animations, scroll, and layout — built on motion-foundations tokens … |
| [`ecc-remotion-video-creation`](affaan-m/everything-claude-code/ecc-remotion-video-creation) · [src](https://github.com/affaan-m/everything-claude-code/tree/HEAD/skills/remotion-video-creation) | MIT | Best practices for Remotion - Video creation in React. 29 domain-specific rules covering 3D, animations, audio, captions, charts, transitions, and more. Use when building video in … |
| [`ecc-tasteforge-video`](affaan-m/everything-claude-code/ecc-tasteforge-video) · [src](https://github.com/affaan-m/everything-claude-code/tree/HEAD/skills/tasteforge-video) | MIT | Use for file-driven multimodal image, video, and 3D-asset discovery; taste interviews; distill or apply workflows; style-pack validation; editable EDL/FCPXML export; provenance aud… |
| [`ecc-video-editing`](affaan-m/everything-claude-code/ecc-video-editing) · [src](https://github.com/affaan-m/everything-claude-code/tree/HEAD/skills/video-editing) | MIT | AI-assisted video editing workflows for cutting, structuring, and augmenting real footage. Covers the full pipeline from raw capture through FFmpeg, Remotion, ElevenLabs, fal.ai, a… |

## [ra100/blender-claude-plugin](https://github.com/ra100/blender-claude-plugin) · 8

| Nom | Licence | Description |
|---|---|---|
| [`blender-lab-mcp--blender-animation-rigging`](ra100/blender-claude-plugin/blender-lab-mcp--blender-animation-rigging) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-animation-rigging) | MIT | Blender 5.x animation and rigging — keyframes, FCurves, layered actions, drivers, constraints, armatures, IK/FK, shape keys, NLA editor, and bone collections via Python (bpy). Incl… |
| [`blender-lab-mcp--blender-compositing-nodes`](ra100/blender-claude-plugin/blender-lab-mcp--blender-compositing-nodes) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-compositing-nodes) | MIT | Blender 5.x compositor nodes — post-processing, color grading, denoising, keying, glare, depth of field, render pass separation, multi-layer EXR output, and scripting compositing p… |
| [`blender-lab-mcp--blender-geometry-nodes`](ra100/blender-claude-plugin/blender-lab-mcp--blender-geometry-nodes) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-geometry-nodes) | MIT | Blender 5.x geometry nodes — procedural modeling, scattering, mesh/curve/volume ops, simulation zones, repeat zones, Bone Info, Font socket, UV nodes, volume grid nodes, and script… |
| [`blender-lab-mcp--blender-modeling-modifiers`](ra100/blender-claude-plugin/blender-lab-mcp--blender-modeling-modifiers) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-modeling-modifiers) | MIT | Blender 5.x modifiers, bmesh API, mesh editing operators, sculpting setup — SubSurf, Boolean, Array, Mirror, Bevel, bmesh procedural mesh creation, and modeling pipelines via Pytho… |
| [`blender-lab-mcp--blender-physics-simulation`](ra100/blender-claude-plugin/blender-lab-mcp--blender-physics-simulation) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-physics-simulation) | MIT | Blender 5.x physics simulations — rigid body, cloth, fluid/smoke/fire (Mantaflow), soft body, particles, force fields, collisions, and simulation baking/caching via Python (bpy). |
| [`blender-lab-mcp--blender-python-scripting`](ra100/blender-claude-plugin/blender-lab-mcp--blender-python-scripting) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-python-scripting) | MIT | Blender 5.x Python scripting (bpy) — custom operators, UI panels, add-on development, context management, handlers, timers, property system, batch processing, and data model access… |
| [`blender-lab-mcp--blender-scene-rendering`](ra100/blender-claude-plugin/blender-lab-mcp--blender-scene-rendering) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-scene-rendering) | MIT | Blender 5.x scene setup, render engines (Cycles/EEVEE), output formats, import/export (FBX/glTF/OBJ/USD/Alembic), linking/appending, color management (AgX/Filmic), view layers, vie… |
| [`blender-lab-mcp--blender-shader-nodes`](ra100/blender-claude-plugin/blender-lab-mcp--blender-shader-nodes) · [src](https://github.com/ra100/blender-claude-plugin/tree/HEAD/skills/blender-shader-nodes) | MIT | Blender 5.x shader nodes — PBR materials, procedural textures, Principled BSDF, glass/metal/skin shaders, world/HDRI lighting, raycast shader node, and scripting material node tree… |

## [iart-ai/explainer-video-skills](https://github.com/iart-ai/explainer-video-skills) · 5

| Nom | Licence | Description |
|---|---|---|
| [`diagram-animation`](iart-ai/explainer-video-skills/diagram-animation) · [src](https://github.com/iart-ai/explainer-video-skills/tree/HEAD/skills/diagram-animation) | MIT | This skill should be used when the user asks to "animate this diagram", "build a flowchart that reveals step by step", "animate an architecture/sequence diagram", "make a chart ani… |
| [`explainer-video`](iart-ai/explainer-video-skills/explainer-video) · [src](https://github.com/iart-ai/explainer-video-skills/tree/HEAD/skills/explainer-video) | MIT | This skill should be used when the user asks to "make an explainer video", "turn this into a short explainer", "write a script and storyboard for a product video", "produce a how-i… |
| [`isometric-animation`](iart-ai/explainer-video-skills/isometric-animation) · [src](https://github.com/iart-ai/explainer-video-skills/tree/HEAD/skills/isometric-animation) | MIT | This skill should be used when the user asks to "make an isometric animation", "build a 2.5D isometric scene", "create an isometric infographic", "animate an exploded diagram", "do… |
| [`whiteboard-animation`](iart-ai/explainer-video-skills/whiteboard-animation) · [src](https://github.com/iart-ai/explainer-video-skills/tree/HEAD/skills/whiteboard-animation) | MIT | This skill should be used when the user asks to "make a whiteboard animation", "draw-on explainer", "VideoScribe style", "hand-drawn explainer video", "animate a sketch being drawn… |
| [`wrapped-video`](iart-ai/explainer-video-skills/wrapped-video) · [src](https://github.com/iart-ai/explainer-video-skills/tree/HEAD/skills/wrapped-video) | MIT | This skill should be used when the user asks to "make a Spotify Wrapped style video", "build a year in review / year-in-review video", "create a personalized data video", "generate… |

## [iart-ai/tiktok-video-skills](https://github.com/iart-ai/tiktok-video-skills) · 4

| Nom | Licence | Description |
|---|---|---|
| [`caption-animation`](iart-ai/tiktok-video-skills/caption-animation) · [src](https://github.com/iart-ai/tiktok-video-skills/tree/HEAD/skills/caption-animation) | MIT | This skill should be used when the user asks to "add animated captions", "make TikTok captions", "karaoke captions", "word-by-word subtitles", "auto subtitles", "highlight the acti… |
| [`countdown-video`](iart-ai/tiktok-video-skills/countdown-video) · [src](https://github.com/iart-ai/tiktok-video-skills/tree/HEAD/skills/countdown-video) | MIT | This skill should be used when the user asks to "make a countdown timer video", "create a countdown animation", "build a stream starting soon countdown", "do an event/launch/sale c… |
| [`lower-thirds`](iart-ai/tiktok-video-skills/lower-thirds) · [src](https://github.com/iart-ai/tiktok-video-skills/tree/HEAD/skills/lower-thirds) | MIT | This skill should be used when the user asks to "make an animated lower third", "add lower thirds", "create a name tag/name lower third", "build broadcast titles", "animate a title… |
| [`short-form-video`](iart-ai/tiktok-video-skills/short-form-video) · [src](https://github.com/iart-ai/tiktok-video-skills/tree/HEAD/skills/short-form-video) | MIT | This skill should be used when the user asks to "make a Reels/TikTok/YouTube Shorts video", "build a short-form video template", "write a hook for a short", "edit for retention", "… |

## [iart-ai/ad-video-skills](https://github.com/iart-ai/ad-video-skills) · 3

| Nom | Licence | Description |
|---|---|---|
| [`ad-creative-video`](iart-ai/ad-video-skills/ad-creative-video) · [src](https://github.com/iart-ai/ad-video-skills/tree/HEAD/skills/ad-creative-video) | MIT | This skill should be used when the user asks to "make a video ad", "create an animated ad", "build a performance/UGC-style ad", "batch-produce ad creative variations", "generate ad… |
| [`launch-video`](iart-ai/ad-video-skills/launch-video) · [src](https://github.com/iart-ai/ad-video-skills/tree/HEAD/skills/launch-video) | MIT | This skill should be used when the user asks to "make a launch video", "create a product hype/sizzle film", "build a teaser/trailer for a drop", "do a reveal montage with an end-ca… |
| [`testimonial-video`](iart-ai/ad-video-skills/testimonial-video) · [src](https://github.com/iart-ai/ad-video-skills/tree/HEAD/skills/testimonial-video) | MIT | This skill should be used when the user asks to "make an animated testimonial", "create a quote video", "build a review video", "turn a customer testimonial into a graphic", "anima… |

## [iart-ai/data-animation-skills](https://github.com/iart-ai/data-animation-skills) · 3

| Nom | Licence | Description |
|---|---|---|
| [`animated-infographic`](iart-ai/data-animation-skills/animated-infographic) · [src](https://github.com/iart-ai/data-animation-skills/tree/HEAD/skills/animated-infographic) | MIT | This skill should be used when the user asks to "make an animated infographic", "create an infographic video", "build an infographic animation", "animate an explainer infographic",… |
| [`chart-animation`](iart-ai/data-animation-skills/chart-animation) · [src](https://github.com/iart-ai/data-animation-skills/tree/HEAD/skills/chart-animation) | MIT | This skill should be used when the user asks to "make a bar chart race", "turn a CSV into a video", "build an animated data visualization", "create an animated statistics video", "… |
| [`presentation-video`](iart-ai/data-animation-skills/presentation-video) · [src](https://github.com/iart-ai/data-animation-skills/tree/HEAD/skills/presentation-video) | MIT | This skill should be used when the user asks to "make an animated presentation", "turn a pitch deck into a video", "convert slides/a deck to video", "make a presentation video", "b… |

## [iart-ai/youtube-video-skills](https://github.com/iart-ai/youtube-video-skills) · 2

| Nom | Licence | Description |
|---|---|---|
| [`audiogram`](iart-ai/youtube-video-skills/audiogram) · [src](https://github.com/iart-ai/youtube-video-skills/tree/HEAD/skills/audiogram) | MIT | This skill should be used when the user asks to "make an audiogram", "turn a podcast into a video", "create a waveform video", "make a podcast clip video", "convert audio to video"… |
| [`youtube-intro-outro`](iart-ai/youtube-video-skills/youtube-intro-outro) · [src](https://github.com/iart-ai/youtube-video-skills/tree/HEAD/skills/youtube-intro-outro) | MIT | This skill should be used when the user asks to "make a YouTube intro", "create a channel intro", "build a logo sting/bumper", "design an outro / end screen / end card", "add subsc… |

## [anthropics/skills](https://github.com/anthropics/skills) · 2

| Nom | Licence | Description |
|---|---|---|
| [`algorithmic-art`](anthropics/skills/algorithmic-art) · [src](https://github.com/anthropics/skills/tree/HEAD/skills/algorithmic-art) | Apache-2.0 | Creating algorithmic art using p5.js with seeded randomness and interactive parameter exploration. Use this when users request creating art using code, generative art, algorithmic … |
| [`slack-gif-creator`](anthropics/skills/slack-gif-creator) · [src](https://github.com/anthropics/skills/tree/HEAD/skills/slack-gif-creator) | Apache-2.0 | Knowledge and utilities for creating animated GIFs optimized for Slack. Provides constraints, validation tools, and animation concepts. Use when users request animated GIFs for Sla… |

## [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) · 2

| Nom | Licence | Description |
|---|---|---|
| [`ui-animation-principles`](Owl-Listener/designer-skills/ui-animation-principles) · [src](https://github.com/Owl-Listener/designer-skills/tree/HEAD/interaction-design/skills/animation-principles) | MIT | Apply animation principles — easing, staging, follow-through — to one specific UI motion. Use when tuning how an animation feels. For product-wide duration and easing tokens use `m… |
| [`ui-motion-system`](Owl-Listener/designer-skills/ui-motion-system) · [src](https://github.com/Owl-Listener/designer-skills/tree/HEAD/design-systems/skills/motion-system) | MIT | Define motion tokens — durations, easing vocabulary, and reduced-motion handling — for consistency product-wide. Use when standardising motion across a system. For crafting one spe… |

## [iart-ai/kinetic-typography-skills](https://github.com/iart-ai/kinetic-typography-skills) · 1

| Nom | Licence | Description |
|---|---|---|
| [`kinetic-typography`](iart-ai/kinetic-typography-skills/kinetic-typography) · [src](https://github.com/iart-ai/kinetic-typography-skills/tree/HEAD/skills/kinetic-typography) | MIT | This skill should be used when the user asks to "animate a headline", "make a kinetic typography video", "do a split-text reveal", "stagger text by character/word/line", "make a ly… |

## [iart-ai/manim-skills](https://github.com/iart-ai/manim-skills) · 1

| Nom | Licence | Description |
|---|---|---|
| [`manim`](iart-ai/manim-skills/manim) · [src](https://github.com/iart-ai/manim-skills/tree/HEAD/skills/manim) | MIT | This skill should be used when the user asks to "make a math animation", "animate an equation", "use Manim", "make a 3Blue1Brown-style video", "plot or animate a graph/function", "… |

## [iart-ai/b-roll-skills](https://github.com/iart-ai/b-roll-skills) · 1

| Nom | Licence | Description |
|---|---|---|
| [`talking-head-b-roll`](iart-ai/b-roll-skills/talking-head-b-roll) · [src](https://github.com/iart-ai/b-roll-skills/tree/HEAD/skills/talking-head-b-roll) | MIT | Add b-roll motion graphics to a talking-head video. Transcribes the recording with word timings, decides line by line when the speaker is shown, when a graphic is laid over them an… |

## [iart-ai/lower-thirds-skills](https://github.com/iart-ai/lower-thirds-skills) · 1

| Nom | Licence | Description |
|---|---|---|
| [`lower-thirds`](iart-ai/lower-thirds-skills/lower-thirds) · [src](https://github.com/iart-ai/lower-thirds-skills/tree/HEAD/skills/lower-thirds) | MIT | Make animated lower thirds and other broadcast overlays (name straps, corner bugs, subscribe reminders, scripture or song titles) as transparent video files, drawn frame by frame i… |

## [howseen-ai/claude-motion-design](https://github.com/howseen-ai/claude-motion-design) · 1

| Nom | Licence | Description |
|---|---|---|
| [`claude-motion-design`](howseen-ai/claude-motion-design/claude-motion-design) · [src](https://github.com/howseen-ai/claude-motion-design/tree/HEAD/skill/motion-design) | MIT | Code-only motion design pipeline (no After Effects) for Raphaël / Howseen: launch films, showreels, product promos, LinkedIn/X videos, meme clips. Use when asked to make a motion d… |

## [JakeB-5/motion-graphic-skill](https://github.com/JakeB-5/motion-graphic-skill) · 1

| Nom | Licence | Description |
|---|---|---|
| [`motion-graphic-canvas`](JakeB-5/motion-graphic-skill/motion-graphic-canvas) · [src](https://github.com/JakeB-5/motion-graphic-skill/tree/HEAD/skills/motion-graphic) | MIT | Create or revise single-file HTML motion graphics from briefs and reference material, with beat-synced canvas scenes, synthesized audio, a mobile player, and visual checks. Use for… |

## [fernandokaraka/remotion-motion-graphics-skill](https://github.com/fernandokaraka/remotion-motion-graphics-skill) · 1

| Nom | Licence | Description |
|---|---|---|
| [`remotion-motion-graphics`](fernandokaraka/remotion-motion-graphics-skill/remotion-motion-graphics) · [src](https://github.com/fernandokaraka/remotion-motion-graphics-skill/tree/HEAD/skills/remotion-motion-graphics) | MIT | Build animated motion graphics as real video with Remotion (React-based programmatic video) — title cards, lower thirds, logo stings, badges, stat reveals, countdowns, end screens,… |

## [haidrrrry/claude-remotion-skill](https://github.com/haidrrrry/claude-remotion-skill) · 1

| Nom | Licence | Description |
|---|---|---|
| [`claude-remotion`](haidrrrry/claude-remotion-skill/claude-remotion) · [src](https://github.com/haidrrrry/claude-remotion-skill/tree/HEAD/remotion-motion-graphics) | MIT | Create and edit professional motion graphics videos with Remotion (React-based video). Use this skill EVERY time the user wants to create a video, edit a video, animate something, … |

## [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) · 1

| Nom | Licence | Description |
|---|---|---|
| [`stitch-remotion`](google-labs-code/stitch-skills/stitch-remotion) · [src](https://github.com/google-labs-code/stitch-skills/tree/HEAD/plugins/stitch-build/skills/remotion) | Apache-2.0 | Generate walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays |

## [AndreiFlau/blender-mcp-skill](https://github.com/AndreiFlau/blender-mcp-skill) · 1

| Nom | Licence | Description |
|---|---|---|
| [`blender-mcp-bridge`](AndreiFlau/blender-mcp-skill/blender-mcp-bridge) · [src](https://github.com/AndreiFlau/blender-mcp-skill/tree/HEAD/.) | GPL-3.0 (README) | Execute Python inside a live Blender session via the official Blender Labs MCP extension (TCP localhost:9876) — for building/testing Blender addons, inspecting scenes, running oper… |

## 🔗 Référencés (non copiés — licence, format ou runtime)

- [Remotion — skills officiels](https://github.com/remotion-dev/skills) — Pas de licence → `npx skills add remotion-dev/skills`
- [Blender MCP (ahujasid) — serveur MCP](https://github.com/ahujasid/blender-mcp) — Serveur MCP à coupler avec les skills Blender
- [Blender Lab MCP officiel (Blender ≥ 5.1)](https://github.com/ra100/blender-claude-plugin) — Requis pour `blender-lab-mcp--*`
- [Claude Code Video Toolkit (Manim)](https://github.com/wilwaldon/Claude-Code-Video-Toolkit) — Pas de licence
- [Motion Video Director](https://github.com/Miftahul-Islam-Efaz/Motion-graphics-skill) — Repo indisponible au clonage
- [ElevenLabs MCP (voix, SFX, musique dans Claude)](https://github.com/elevenlabs/elevenlabs-mcp) — Vu sur TikTok (109M vues) — MCP, pas un skill
