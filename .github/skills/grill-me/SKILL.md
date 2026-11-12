---
name: grill-me
description: Interview the user about a plan, task or vague request until it is clear what to do. Use for /grill-me.
disable-model-invocation: true
---

Adapted from mattpocock/skills (MIT).

Interview the user until you both understand the request the same way. Every decision opens
further decisions; ask first about the ones that do not depend on unanswered questions.

Ask in rounds. Number each question, give your recommended answer, and word the question so
that "yes" accepts it:

    ❓ **Q1 – <short title>**: <question>

    ➡️ <your recommended answer>

Wait for the answers before the next round. When you refer to an earlier question, use its
title, not just its number.

Find facts yourself from the repository (data, README, backlog); ask the user only for decisions.

Ask at most 8 questions in total. Then write a short summary: what was decided, what is left
out, and how we will know the work is done. Do not start the work until the user confirms
the summary.

Answer in the user's language.
