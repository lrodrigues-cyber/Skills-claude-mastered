---
name: ecc-autonomous-loops
description: "Patterns and architectures for autonomous Claude Code loops, from simple sequential pipelines to RFC-driven multi-agent DAGs, with stop conditions and cost guards. Use when designing an unattended agent loop, a long-running pipeline, or a multi-agent workflow."
metadata:
  origin: ECC
---

# Autonomous Loops Skill

Patterns, architectures, and reference implementations for running Claude Code autonomously in loops. Covers everything from simple `claude -p` pipelines to full RFC-driven multi-agent DAG orchestration.

## When to Use

- Setting up autonomous development workflows that run without human intervention
- Choosing the right loop architecture for your problem (simple vs complex)
- Building CI/CD-style continuous development pipelines
- Running parallel agents with merge coordination
- Implementing context persistence across loop iterations
- Adding quality gates and cleanup passes to autonomous workflows

## Loop Pattern Spectrum

From simplest to most sophisticated:

| Pattern | Complexity | Best For |
|---------|-----------|----------|
| [Sequential Pipeline](#1-sequential-pipeline-claude--p) | Low | Daily dev steps, scripted workflows |
| [NanoClaw REPL](#2-nanoclaw-repl) | Low | Interactive persistent sessions |
| [Infinite Agentic Loop](#3-infinite-agentic-loop) | Medium | Parallel content generation, spec-driven work |
| [Continuous Claude PR Loop](#4-continuous-claude-pr-loop) | Medium | Multi-day iterative projects with CI gates |
| [De-Sloppify Pattern](#5-the-de-sloppify-pattern) | Add-on | Quality cleanup after any Implementer step |
| [Ralphinho / RFC-Driven DAG](#6-ralphinho--rfc-driven-dag-orchestration) | High | Large features, multi-unit parallel work with merge queue |

---

## 1. Sequential Pipeline (`claude -p`)

**The simplest loop.** Break daily development into a sequence of non-interactive `claude -p` calls. Each call is a focused step with a clear prompt.

### Core Insight

> If you can't figure out a loop like this, it means you can't even drive the LLM to fix your code in interactive mode.

The `claude -p` flag runs Claude Code non-interactively with a prompt, exits when done. Chain calls to build a pipeline:

```bash
#!/bin/bash
# daily-dev.sh — Sequential pipeline for a feature branch

set -e

# Step 1: Implement the feature
claude -p "Read the spec in docs/auth-spec.md. Implement OAuth2 login in src/auth/. Write tests first (TDD). Do NOT create any new documentation files."

# Step 2: De-sloppify (cleanup pass)
claude -p "Review all files changed by the previous commit. Remove any unnecessary type tests, overly defensive checks, or testing of language features (e.g., testing that TypeScript generics work). Keep real business logic tests. Run the test suite after cleanup."

# Step 3: Verify
claude -p "Run the full build, lint, type check, and test suite. Fix any failures. Do not add new features."

# Step 4: Commit
claude -p "Create a conventional commit for all staged changes. Use 'feat: add OAuth2 login flow' as the message."
```

### Key Design Principles

1. **Each step is isolated** — A fresh context window per `claude -p` call means no context bleed between steps.
2. **Order matters** — Steps execute sequentially. Each builds on the filesystem state left by the previous.
3. **Negative instructions are dangerous** — Don't say "don't test type systems." Instead, add a separate cleanup step (see [De-Sloppify Pattern](#5-the-de-sloppify-pattern)).
4. **Exit codes propagate** — `set -e` stops the pipeline on failure.

### Variations

**With model routing:**
```bash
# Research with Opus (deep reasoning)
claude -p --model opus "Analyze the codebase architecture and write a plan for adding caching..."

# Implement with Sonnet (fast, capable)
claude -p "Implement the caching layer according to the plan in docs/caching-plan.md..."

# Review with Opus (thorough)
claude -p --model opus "Review all changes for security issues, race conditions, and edge cases..."
```

**With environment context:**
```bash
# Pass context via files, not prompt length
echo "Focus areas: auth module, API rate limiting" > .claude-context.md
claude -p "Read .claude-context.md for priorities. Work through them in order."
rm .claude-context.md
```

**With `--allowedTools` restrictions:**
```bash
# Read-only analysis pass
claude -p --allowedTools "Read,Grep,Glob" "Audit this codebase for security vulnerabilities..."

# Write-only implementation pass
claude -p --allowedTools "Read,Write,Edit,Bash" "Implement the fixes from security-audit.md..."
```

---

## 2. NanoClaw REPL

**ECC's built-in persistent loop.** A session-aware REPL that calls `claude -p` synchronously with full conversation history.

```bash
# Use the configured plugin root or standalone install (~/.claude or
# $CLAUDE_CONFIG_DIR). For a reviewed and explicitly authorized ECC checkout:
# export CLAUDE_PLUGIN_ROOT="/absolute/path/to/reviewed/ECC"
ECC_ROOT="${CLAUDE_PLUGIN_ROOT:-${CLAUDE_CONFIG_DIR:-$HOME/.claude}}"
[ -f "$ECC_ROOT/scripts/claw.js" ] || { echo "ECC scripts not found in the selected root (set CLAUDE_PLUGIN_ROOT to an authorized ECC checkout)" >&2; exit 1; }

# Start the default session
node "$ECC_ROOT/scripts/claw.js"

# Named session with skill context
CLAW_SESSION=my-project CLAW_SKILLS=tdd-workflow,security-review node "$ECC_ROOT/scripts/claw.js"
```

### How It Works

1. Loads conversation history from `~/.claude/claw/{session}.md`
2. Each user message is sent to `claude -p` with full history as context
3. Responses are appended to the session file (Markdown-as-database)
4. Sessions persist across restarts

### When NanoClaw vs Sequential Pipeline

| Use Case | NanoClaw | Sequential Pipeline |
|----------|----------|-------------------|
| Interactive exploration | Yes | No |
| Scripted automation | No | Yes |
| Session persistence | Built-in | Manual |
| Context accumulation | Grows per turn | Fresh each step |
| CI/CD integration | Poor | Excellent |

See the `/claw` command documentation for full details.

---

## 3. Infinite Agentic Loop

**A two-prompt system** that orchestrates parallel sub-agents for specification-driven generation. Developed by disler (credit: @disler).

### Architecture: Two-Prompt System

```
PROMPT 1 (Orchestrator)              PROMPT 2 (Sub-Agents)
┌─────────────────────┐             ┌──────────────────────┐
│ Parse spec file      │             │ Receive full context  │
│ Scan output dir      │  deploys   │ Read assigned number  │
│ Plan iteration       │────────────│ Follow spec exactly   │
│ Assign creative dirs │  N agents  │ Generate unique output │
│ Manage waves         │             │ Save to output dir    │
└─────────────────────┘             └──────────────────────┘
```

### The Pattern

1. **Spec Analysis** — Orchestrator reads a specification file (Markdown) defining what to generate
2. **Directory Recon** — Scans existing output to find the highest iteration number
3. **Parallel Deployment** — Launches N sub-agents, each with:
   - The full spec
   - A unique creative direction
   - A specific iteration number (no conflicts)
   - A snapshot of existing iterations (for uniqueness)
4. **Wave Management** — For infinite mode, deploys waves of 3-5 agents until context is exhausted

### Implementation via Claude Code Commands

Create `.claude/commands/infinite.md`:

```markdown
Parse the following arguments from $ARGUMENTS:
1. spec_file — path to the specification markdown
2. output_dir — where iterations are saved
3. count — integer 1-N or "infinite"

PHASE 1: Read and deeply understand the specification.
PHASE 2: List output_dir, find highest iteration number. Start at N+1.
PHASE 3: Plan creative directions — each agent gets a DIFFERENT theme/approach.
PHASE 4: Deploy sub-agents in parallel (Task tool). Each receives:
  - Full spec text
  - Current directory snapshot
  - Their assigned iteration number
  - Their unique creative direction
PHASE 5 (infinite mode): Loop in waves of 3-5 until context is low.
```

**Invoke:**
```bash
/project:infinite specs/component-spec.md src/ 5
/project:infinite specs/component-spec.md src/ infinite
```

### Batching Strategy

| Count | Strategy |
|-------|----------|
| 1-5 | All agents simultaneously |
| 6-20 | Batches of 5 |
| infinite | Waves of 3-5, progressive sophistication |

### Key Insight: Uniqueness via Assignment

Don't rely on agents to self-differentiate. The orchestrator **assigns** each agent a specific creative direction and iteration number. This prevents duplicate concepts across parallel agents.

---

## 4. Continuous Claude PR Loop

**A production-grade shell script** that runs Claude Code in a continuous loop, creating PRs, waiting for CI, and merging automatically. Created by AnandChowdhary (credit: @AnandChowdhary).

### Core Loop

```
┌─────────────────────────────────────────────────────┐
│  CONTINUOUS CLAUDE ITERATION                        │
│                                                     │
│  1. Create branch (continuous-claude/iteration-N)   │
│  2. Run claude -p with enhanced prompt              │
│  3. (Optional) Reviewer pass — separate claude -p   │
│  4. Commit changes (claude generates message)       │
│  5. Push + create PR (gh pr create)                 │
│  6. Wait for CI checks (poll gh pr checks)          │
│  7. CI failure? → Auto-fix pass (claude -p)         │
│  8. Merge PR (squash/merge/rebase)                  │
│  9. Return to main → repeat                         │
│                                                     │
│  Limit by: --max-runs N | --max-cost $X             │
│            --max-duration 2h | completion signal     │
└─────────────────────────────────────────────────────┘
```

### Installation

> **Warning:** Install continuous-claude from its repository after reviewing the code. Do not pipe external scripts directly to bash.

### Usage

```bash
# Basic: 10 iterations
continuous-claude --prompt "Add unit tests for all untested functions" --max-runs 10

# Cost-limited
continuous-claude --prompt "Fix all linter errors" --max-cost 5.00

# Time-boxed
continuous-claude --prompt "Improve test coverage" --max-duration 8h

# With code review pass
continuous-claude \
  --prompt "Add authentication feature" \
  --max-runs 10 \
  --review-prompt "Run npm test && npm run lint, fix any failures"

# Parallel via worktrees
continuous-claude --prompt "Add tests" --max-runs 5 --worktree tests-worker &
continuous-claude --prompt "Refactor code" --max-runs 5 --worktree refactor-worker &
wait
```

### Cross-Iteration Context: SHARED_TASK_NOTES.md

The critical innovation: a `SHARED_TASK_NOTES.md` file persists across iterations:

```markdown
## Progress
- [x] Added tests for auth module (iteration 1)
- [x] Fixed edge case in token refresh (iteration 2)
- [ ] Still need: rate limiting tests, error boundary tests

## Next Steps
- Focus on rate limiting module next
- The mock setup in tests/helpers.ts can be reused
```

Claude reads this file at iteration start and updates it at iteration end. This bridges the context gap between independent `claude -p` invocations.

### CI Failure Recovery

When PR checks fail, Continuous Claude automatically:
1. Fetches the failed run ID via `gh run list`
2. Spawns a new `claude -p` with CI fix context
3. Claude inspects logs via `gh run view`, fixes code, commits, pushes
4. Re-waits for checks (up to `--ci-retry-max` attempts)

### Completion Signal

Claude can signal "I'm done" by outputting a magic phrase:

```bash
continuous-claude \
  --prompt "Fix all bugs in the issue tracker" \
  --completion-signal "CONTINUOUS_CLAUDE_PROJECT_COMPLETE" \
  --completion-threshold 3  # Stops after 3 consecutive signals
```

Three consecutive iterations signaling completion stops the loop, preventing wasted runs on finished work.

### Key Configuration

| Flag | Purpose |
|------|---------|
| `--max-runs N` | Stop after N successful iterations |
| `--max-cost $X` | Stop after spending $X |
| `--max-duration 2h` | Stop after time elapsed |
| `--merge-strategy squash` | squash, merge, or rebase |
| `--worktree <name>` | Parallel execution via git worktrees |
| `--disable-commits` | Dry-run mode (no git operations) |
| `--review-prompt "..."` | Add reviewer pass per iteration |
| `--ci-retry-max N` | Auto-fix CI failures (default: 1) |

---

## Extended reference

More detail lives in [references/extended.md](references/extended.md). Read the section you need:

- 5. The De-Sloppify Pattern
- 6. Ralphinho / RFC-Driven DAG Orchestration
- MERGE CONFLICT — RESOLVE BEFORE NEXT LANDING
- Choosing the Right Pattern
- Anti-Patterns
- References
