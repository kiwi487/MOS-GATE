# MOS Gate Oxide — v10.5 QA Report

## Scope

Minor Chapter 05 layout/readability update based on the user's v10.4 no-images package. The site remains a static offline HTML presentation of previously computed COMSOL results. The 6,344 source 2D images are **not included**; the image loader and manifest workflow remain available for the user to supply them separately.

## Change review

- `index.html` and `MOS_COMSOL_Offline.html`: matched exactly; only Chapter 05 styles and one lightweight height-reservation helper were added. No numerical formulas, quiz questions, answers, data arrays, or existing image paths changed.
- `README.md`: new version and image-free use instructions, with the previous v10.4 notes retained.
- `verify_package.py`: documentation string version updated, validation behavior unchanged.
- `QA_REPORT_v10_5.md`: this report.

## Scientific integrity

- Embedded `const COMSOL=...` line matches v10.4 **byte for byte**.
- Embedded COMSOL SHA-256: `afcb58fb695264fb1f3bdb48107c7a5ea34b1ead7d34abb2072dd96f09b01ca1`.
- Earlier CSV, graph and model source evidence remain unchanged in this patch; gate capacitance analytical data and plot logic were not modified.

## Browser regression

Headless Chromium via Playwright, with the full HTML inserted as a local document, tested across 10 viewport widths. At each width all **four answers (A–D) were exercised for each of the four questions** (16 question-answer interactions per viewport), with transition to the summary and restart on every run. This is 160 question-answer interactions total, plus 40 summaries and restarts. Measured absolute page position of the `Model / Reproducibility` block before and after every state, checked horizontal overflow and captured JavaScript errors.

| Viewport width | Stable card height | Model section shift | Horizontal overflow |
|---:|---:|---:|---:|
| 1920 px | 780 px | 0 px | 0 px |
| 1650 px | 780 px | 0 px | 0 px |
| 1280 px | 780 px | 0 px | 0 px |
| 810 px | 780 px | 0 px | 0 px |
| 720 px | 995 px | 0 px | 0 px |
| 600 px | 1060 px | 0 px | 0 px |
| 540 px | 1107 px | 0 px | 0 px |
| 480 px | 1189 px | 0 px | 0 px |
| 390 px | 1354 px | 0 px | 0 px |
| 360 px | 1515 px | 0 px | 0 px |

**All checked states: PASS**. No upward/downward jump of the following model section at the tested widths; no horizontal overflow; no JavaScript exceptions. Both a correct/incorrect answer path and reaching/escaping the summary were exercised. The original subtle CSS animations and reduced-motion rules are preserved.

## Out-of-scope

- No independent COMSOL solver rerun or quantitative mesh verification (the underlying v10.4 data were preserved, not recomputed).
- No validation of user-supplied `images/` because those frames were intentionally omitted.
- Browser coverage is Chromium/Chrome-compatible rendering, not an exhaustive test of every browser/OS combination.
