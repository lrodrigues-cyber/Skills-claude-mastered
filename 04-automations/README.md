# 🤖 Automations Claude Code (plugins · hooks · commands)

Plugins complets : hooks (sécurité, coût, logs, format), slash commands, agents et règles. Installables via le marketplace de ce repo.

**36 plugins** issus de 4 sources. Chaque dossier garde sa licence d'origine.

## Installation

```text
/plugin marketplace add lrodrigues-cyber/Skills-claude-mastered
/plugin install <nom>@skills-claude-mastered
```
Ou en local : `claude --plugin-dir 04-automations/<auteur>/<repo>/<plugin>`

## [karanb192/claude-code-hooks](https://github.com/karanb192/claude-code-hooks) · 22

| Nom | Licence | Description |
|---|---|---|
| [`auto-stage`](karanb192/claude-code-hooks/auto-stage) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/auto-stage) | MIT | Automatic git staging for Claude Code. A PostToolUse hook on Edit/Write runs `git add` on every file Claude modifies, so `git status` always shows exactly what Claude touched and p |
| [`block-dangerous-commands`](karanb192/claude-code-hooks/block-dangerous-commands) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/block-dangerous-commands) | MIT | A PreToolUse guard for Bash that blocks dangerous shell commands before they execute: rm targeting home/root/system dirs, dd to disk devices, mkfs, fork bombs, curl/sh, force push  |
| [`bounty-board`](karanb192/claude-code-hooks/bounty-board) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/bounty-board) | MIT | Turns your repo's tech debt into an aging bounty economy. A SessionStart hook scans tracked files and prices each TODO/FIXME/HACK/skip as a wanted-poster bounty whose XP grows with |
| [`cache-tax`](karanb192/claude-code-hooks/cache-tax) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/cache-tax) | MIT | The comeback price of a cold prompt cache, shown before you pay it. A UserPromptSubmit guard warns (or refuses once) when your next message will re-write a lapsed 1-hour cache at u |
| [`case-insensitive-guard`](karanb192/claude-code-hooks/case-insensitive-guard) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/case-insensitive-guard) | MIT | Stops `rm -rf content` silently destroying `Content` on case-insensitive filesystems (APFS default, exFAT, NTFS). A PreToolUse hook on Bash that resolves the real target of destruc |
| [`config-guard`](karanb192/claude-code-hooks/config-guard) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/config-guard) | MIT | Who guards the guards: a PreToolUse hook that blocks the agent from tampering with its own guardrail configuration. Deny-by-default protection for settings.json, hook scripts and h |
| [`config-watch`](karanb192/claude-code-hooks/config-watch) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/config-watch) | MIT | Tripwire for out-of-band config changes in Claude Code. A ConfigChange hook fires whenever settings (user, project, local, policy) or skills change mid-session, from an installer s |
| [`context-hogs`](karanb192/claude-code-hooks/context-hogs) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/context-hogs) | MIT | A per-file context-cost leaderboard for Claude Code. A PostToolUse hook (async, zero added latency) attributes every tool result's tokens to the file(s) it pulled into context; at  |
| [`dead-end-registry`](karanb192/claude-code-hooks/dead-end-registry) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/dead-end-registry) | MIT | Approach-level negative-knowledge memory for Claude Code. Mines your transcripts (Stop/PreCompact, both async and zero added latency) for approaches you TRIED and then REVERTED (wi |
| [`dead-rules-audit`](karanb192/claude-code-hooks/dead-rules-audit) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/dead-rules-audit) | MIT | A CLAUDE.md compliance flight-recorder for Claude Code. At SessionStart it parses CLAUDE.md into numbered atomic rules; on every Edit/MultiEdit/Write a PostToolUse hook (async, zer |
| [`format-code`](karanb192/claude-code-hooks/format-code) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/format-code) | MIT | Auto-formats files the moment Claude writes them. A PostToolUse hook on Write/Edit runs ruff (check --fix + format, via uv) on Python and prettier (via npx) on JS/TS/JSON/MD/YAML/H |
| [`git-safety`](karanb192/claude-code-hooks/git-safety) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/git-safety) | MIT | Branch-aware git guardrails for Claude Code. A PreToolUse hook on Bash that denies destructive git and gh CLI operations before they run: pushing to main/master, deleting protected |
| [`guard-pack`](karanb192/claude-code-hooks/guard-pack) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/guard-pack) | MIT | All seven guard hooks in one Node process: subagent-spawn-cap, config-guard, block-dangerous-commands, protect-secrets, protect-tests, git-safety, and case-insensitive-guard, evalu |
| [`instructions-audit`](karanb192/claude-code-hooks/instructions-audit) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/instructions-audit) | MIT | A prompt-injection tripwire for instruction files. An InstructionsLoaded hook audits CLAUDE.md / .claude/rules/*.md content as it enters context and flags hidden or hostile directi |
| [`nerf-receipts`](karanb192/claude-code-hooks/nerf-receipts) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/nerf-receipts) | MIT | A personal flight recorder for Claude Code quality. Background hooks (async, zero added latency) record your own per-session signals keyed by model id and Claude Code version: tool |
| [`notify-permission`](karanb192/claude-code-hooks/notify-permission) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/notify-permission) | MIT | Slack alerts when Claude Code needs you. A Notification hook on permission_prompt/idle_prompt/elicitation_dialog classifies each notification (from notification_type when present,  |
| [`pr-provenance-stamp`](karanb192/claude-code-hooks/pr-provenance-stamp) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/pr-provenance-stamp) | MIT | Embeds a reviewer-facing provenance receipt into your PR body when Claude runs `gh pr create` (or `glab mr create`). A PostToolUse hook (async, zero added latency) records a per-se |
| [`protect-secrets`](karanb192/claude-code-hooks/protect-secrets) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/protect-secrets) | MIT | A secrets firewall for Claude Code. A PreToolUse hook screens every Read, Edit, Write, Bash, and Grep call against tiered patterns (critical/high/strict): sensitive files like .env |
| [`protect-tests`](karanb192/claude-code-hooks/protect-tests) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/protect-tests) | MIT | Stops the "fake green" failure mode for Claude Code. A PreToolUse guard on Bash/Edit/MultiEdit/Write that denies making a suite pass by deleting test files or directories (rm / git |
| [`session-logger`](karanb192/claude-code-hooks/session-logger) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/session-logger) | MIT | A durable, greppable markdown log of every Claude Code session. SessionStart seeds a note (timestamps, cwd, git repo/branch), an async PostToolUse hook appends every Edit/Write/Rea |
| [`standup-autopilot`](karanb192/claude-code-hooks/standup-autopilot) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/standup-autopilot) | MIT | Turns what your agents ACTUALLY did into a standup: captured from session transcripts (not commits/tickets, which miss uncommitted work, real test exit codes, and unresolved errors |
| [`subagent-spawn-cap`](karanb192/claude-code-hooks/subagent-spawn-cap) · [src](https://github.com/karanb192/claude-code-hooks/tree/HEAD/plugins/subagent-spawn-cap) | MIT | A total-spawns-per-session budget for subagents: a PreToolUse guard on the Agent tool that counts every spawn in a session (nested spawns from inside subagents included), asks for  |

## [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) · 12

| Nom | Licence | Description |
|---|---|---|
| [`claude-code-setup`](anthropics/claude-plugins-official/claude-code-setup) · [src](https://github.com/anthropics/claude-plugins-official/tree/HEAD/plugins/claude-code-setup) | Apache-2.0 | Analyze codebases and recommend tailored Claude Code automations such as hooks, skills, MCP servers, and subagents. |
| [`claude-md-management`](anthropics/claude-plugins-official/claude-md-management) · [src](https://github.com/anthropics/claude-plugins-official/tree/HEAD/plugins/claude-md-management) | Apache-2.0 | Tools to maintain and improve CLAUDE.md files - audit quality, capture session learnings, and keep project memory current. |
| [`code-simplifier`](anthropics/claude-plugins-official/code-simplifier) · [src](https://github.com/anthropics/claude-plugins-official/tree/HEAD/plugins/code-simplifier) | Apache-2.0 | Agent that simplifies and refines code for clarity, consistency, and maintainability while preserving functionality |
| [`commit-commands`](anthropics/claude-plugins-official/commit-commands) · [src](https://github.com/anthropics/claude-plugins-official/tree/HEAD/plugins/commit-commands) | Apache-2.0 | Streamline your git workflow with simple commands for committing, pushing, and creating pull requests |
| [`feature-dev`](anthropics/claude-plugins-official/feature-dev) · [src](https://github.com/anthropics/claude-plugins-official/tree/HEAD/plugins/feature-dev) | Apache-2.0 | Comprehensive feature development workflow with specialized agents for codebase exploration, architecture design, and quality review |
| [`hookify`](anthropics/claude-plugins-official/hookify) · [src](https://github.com/anthropics/claude-plugins-official/tree/HEAD/plugins/hookify) | Apache-2.0 | Easily create hooks to prevent unwanted behaviors by analyzing conversation patterns |
| [`mcp-server-dev`](anthropics/claude-plugins-official/mcp-server-dev) · [src](https://github.com/anthropics/claude-plugins-official/tree/HEAD/plugins/mcp-server-dev) | Apache-2.0 | Skills for designing and building MCP servers that work seamlessly with Claude — guides you through deployment models (remote HTTP, MCPB, local), tool design patterns, auth, and in |
| [`plugin-dev`](anthropics/claude-plugins-official/plugin-dev) · [src](https://github.com/anthropics/claude-plugins-official/tree/HEAD/plugins/plugin-dev) | Apache-2.0 | Plugin development toolkit with skills for creating agents, commands, hooks, MCP integrations, and comprehensive plugin structure guidance |
| [`pr-review-toolkit`](anthropics/claude-plugins-official/pr-review-toolkit) · [src](https://github.com/anthropics/claude-plugins-official/tree/HEAD/plugins/pr-review-toolkit) | Apache-2.0 | Comprehensive PR review agents specializing in comments, tests, error handling, type design, code quality, and code simplification |
| [`ralph-loop`](anthropics/claude-plugins-official/ralph-loop) · [src](https://github.com/anthropics/claude-plugins-official/tree/HEAD/plugins/ralph-loop) | Apache-2.0 | Continuous self-referential AI loops for interactive iterative development, implementing the Ralph Wiggum technique. Run Claude in a while-true loop with the same prompt until task |
| [`security-guidance`](anthropics/claude-plugins-official/security-guidance) · [src](https://github.com/anthropics/claude-plugins-official/tree/HEAD/plugins/security-guidance) | Apache-2.0 | Security review for Claude-generated code. Pattern-based warnings on edits, LLM-powered diff review on Stop, and an agentic commit reviewer that catches injection, XSS, SSRF, hardc |
| [`session-report`](anthropics/claude-plugins-official/session-report) · [src](https://github.com/anthropics/claude-plugins-official/tree/HEAD/plugins/session-report) | Apache-2.0 | Session usage report: tokens, cache, subagents, skills |

## [BayramAnnakov/claude-reflect](https://github.com/BayramAnnakov/claude-reflect) · 1

| Nom | Licence | Description |
|---|---|---|
| [`claude-reflect`](BayramAnnakov/claude-reflect/claude-reflect) · [src](https://github.com/BayramAnnakov/claude-reflect/tree/HEAD/.) | MIT | Self-learning system for Claude Code that captures corrections and updates CLAUDE.md automatically |

## [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) · 1

| Nom | Licence | Description |
|---|---|---|
| [`ecc-commands`](affaan-m/everything-claude-code/ecc-commands) · [src](https://github.com/affaan-m/everything-claude-code/tree/HEAD/commands) | MIT | Everything Claude Code slash commands (plan, tdd, code-review, multi-agent orchestration, quality gates) |

## 🔗 Référencés (non copiés — licence, format ou runtime)

- [claude-mem — mémoire persistante entre sessions](https://github.com/thedotmack/claude-mem) — 107k⭐, plugin avec worker → `/plugin marketplace add thedotmack/claude-mem`
- [RTK — proxy CLI qui réduit les tokens des commandes](https://github.com/rtk-ai/rtk) — 85k⭐, binaire Rust (Apache-2.0)
- [Everything Claude Code (ECC) — setup complet](https://github.com/affaan-m/everything-claude-code) — 294k⭐ ; hooks liés aux scripts du repo → installer le plugin complet
- [Claude Command Suite](https://github.com/qdhenry/Claude-Command-Suite) — 216 commands, pas de licence
- [awesome-claude-code (hesreallyhim)](https://github.com/hesreallyhim/awesome-claude-code) — Liste de référence hooks/commands/outils
- [claude-plugins.dev](https://claude-plugins.dev) — Registre : ~12k plugins, ~63k skills
