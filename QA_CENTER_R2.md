# v10.7 R2 — Simulation workflow centering

This is a narrowly scoped repackage of v10.7. Only the three CSS rules that lay out the **Simulation workflow** step row were adjusted: step text is centered horizontally and vertically; arrows align with the step centers; the overall row is centered. Max-width prevents a wrapped final step from stretching across the entire panel. The component remains responsive.

## Verification

- Both HTML entrypoints are byte-identical.
- Apart from those three workflow CSS rules, the HTML is identical to the original v10.7.
- The embedded COMSOL numerical data are byte-for-byte unchanged.
- Headless Chromium layout checks at 390, 720, 768, 1024, 1280, 1536, 1650, and 1920 px: PASS (no horizontal overflow, unchanged quiz/report nodes, no JavaScript page errors).
- `verify_package.py` passes without the optional large `images/` folder.
- HTML report and its local figure references are unchanged.
