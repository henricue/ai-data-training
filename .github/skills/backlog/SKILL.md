---
name: backlog
description: Keeps the project's task backlog as Markdown files in backlog/. Use for /backlog, when the user asks where the project stands or what to work on next, or asks to add, start, finish or drop a task.
---

# Backlog

Tasks are Markdown files in `backlog/` named `NNNN-short-title.md` (next ID = highest + 1),
committed together with the work they describe. Each starts with front matter
`status: todo|doing|done|dropped` and an optional `priority: high|low`, then a `# Title`,
a few lines on what and why, and dated notes under `## Notes`.

- `/backlog` or "what's next?": list `doing` tasks, then `todo` tasks by priority and ID.
- `add <title>`: create a `todo` task; write the body only from what the user said.
- `start <id>`, `done <id>`, `drop <id>`: set the status and add a dated note.

Change task files in the same commit as the work. Answer in the user's language.
