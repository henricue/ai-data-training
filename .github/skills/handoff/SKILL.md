---
name: handoff
description: Write a handoff document so that a fresh agent session can continue the work. Use for /handoff.
argument-hint: "What will the next session be used for?"
disable-model-invocation: true
---

Adapted from mattpocock/skills (MIT).

Write a handoff that summarises the current conversation so that a fresh session can
continue the work. Save it as `handoff.md` in the repository root (replace an older one)
and tell the user where it is.

- Include the goal, the current state, the decisions made and the next step.
- Do not repeat what other files already say (PROJECT.md, backlog, commits, diffs); refer
  to them by path instead.
- Leave out passwords, keys and personal data.
- If the user passed arguments, focus on what the next session will be used for.

Write in the user's language.
