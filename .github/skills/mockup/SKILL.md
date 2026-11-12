---
name: mockup
description: Sketch 2–3 alternative designs of a page or report side by side on one canvas where the user can pin comments. Use for /mockup or when the user wants to compare layouts before building.
---

# Mockup

1. Copy `canvas.html` from this folder to `prototypes/<short-name>.html` in the repository.
2. Set the `<title>` and `<h1 id="title">`. Replace the example inside `<div id="screens">`
   with one `<template class="screen" data-id="a" data-title="A · …" data-w="1100" data-h="800">`
   per alternative. Put a `<style>` block and the markup inside each template.
3. Make the alternatives structurally different (layout, order, what is shown first), not
   just different colours. Use the project's real data; label invented numbers as invented.
4. No external resources: no CDN, fonts, images from the web or API calls. Inline SVG is fine.
5. Do not change the canvas itself (toolbar, script, styles).
6. Tell the user to open the file by double-clicking it, pin comments with "Kommentoi" and
   paste the result of "Kopioi kommentit agentille" back into the chat.
7. When revising, keep the `data-id` values so that existing comments stay in place.

Do not publish anything. Answer in the user's language.
