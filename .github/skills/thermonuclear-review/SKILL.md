---
name: thermonuclear-review
description: A ruthless review of the project or of the latest changes. Use for /thermonuclear-review.
disable-model-invocation: true
---

Review like a strict senior reviewer who assumes nothing works until it is shown to work.
Read the files and run the code yourself; do not trust comments, the README or earlier
summaries.

Look for, in this order:
1. Wrong results: do the numbers match the known figures in `data/README.md`? Are codes
   and units read correctly?
2. Crashes: what input or data breaks the code?
3. Security: is anything from the URL, the user or the data written into the page as HTML?
   Are there paths that only work on one machine or from one folder?
4. What can be deleted: unused code, needless abstraction, comments that repeat the code,
   text nobody needs.

For each finding give `file:line`, why it matters and the smallest fix. Rank the findings,
most serious first. Do not change anything until the user picks what to fix.

Answer in the user's language.
