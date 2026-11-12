---
name: grill-analyysi
description: Interview the user about an analysis request before any numbers are computed. Use for /grill-analyysi.
disable-model-invocation: true
---

Interview the user before computing anything. Ask in rounds: number each question, give your
recommended answer and wait for the answers. Ask at most 8 questions, and cover at least these:

- Source: where does the data come from and what does it leave out? Read `data/README.md`.
- Coverage: which years, places and cases are included, and has the recording changed?
- Comparison: compared with what? A count alone rarely answers "more" or "safer".
- Unit: count, share or rate per something? Who will read the number?

End with a summary that names the answer's limitations in one sentence. Answer in the user's
language.
