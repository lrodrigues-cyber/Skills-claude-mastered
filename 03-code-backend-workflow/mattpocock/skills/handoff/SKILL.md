---
name: handoff
description: "Compact the current conversation into a handoff document another agent can pick up cold. Use before ending a long session, when context is near its limit, or when passing work to another agent or person."
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS (`$TMPDIR`, else `/tmp`; `%TEMP%` on Windows) - not the current workspace.

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.

## Merged references

Deeper material folded in from overlapping skills. Read only the file that matches the task.
- [`claude-handoff`](references/merged/claude-handoff/README.md) — Hand the current conversation off to a fresh background agent that picks up the work immediately. _(from [mattpocock/skills](https://github.com/mattpocock/skills/tree/HEAD/skills/in-progress/claude-handoff))_
