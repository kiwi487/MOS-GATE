# MOS Gate Oxide v10.3 — Targeted Browser QA

## What changed

- Added chapter 05 to the existing four-chapter website with a four-question multiple-choice challenge.
- Per-choice feedback on both correct and incorrect answers, with a Next action and score counted only once per question.
- After question four: summary and graded result, plus Restart challenge.
- Accessible direct **Skip to summary** from the initial question (no artificial score).
- Model & Methods below the challenge: COMSOL 5.3 setup/workflow, 26 thicknesses × 61 Vg values, static HTML provenance, limitations, and accompanying COMSOL_Methodology.md handout.
- Updated chapter navigation and presentation guide to five chapters.

## Headless Chromium test

Tested at 1920×1080, 1440×900, 1280×720, 810×850, and 390×844. Each viewport passed 14 state assertions (70/70):

1. Wrong answer shows explanatory feedback and locks answer buttons.
2. Wrong answer does not increment score.
3. Proceeding to Q2 works.
4. Correct answers show explanatory feedback.
5. Final question displays "View summary" action.
6. Completed quiz displays summary and correct 3/4 score for the mixed-answer test.
7. COMSOL model/method section is visible.
8. Restart returns to Q1 with score zero and selectable answers.
9. Skip to summary shows a non-scoring summary.
10. Existing chapter 03 gm chart remains selectable.
11. Chapter 02 defaults to Hole concentration.
12. No uncaught JS exceptions or document-wide horizontal overflow.

The total 14 assertion names per viewport are recorded in `evidence/qa/MOS_v10_3_QA.json`. Screenshots were captured for start and completed summary at all five viewports in `evidence/screenshots/v10_3_challenge_start_*.png` and `v10_3_summary_*.png`.

**Browser environment limitation:** direct `file://` navigation was denied by the browser test environment. The tests loaded the exact same inline HTML with Playwright `set_content`, which validates JavaScript/UI behaviors but cannot directly validate local PNG file loading. The original 6,344 PNG paths and image bytes are unmodified and inherited from the previously verified v10.2 package. This is a focused new-chapter regression, not an independent full COMSOL physics audit.

## Scientific sources & limits

- Existing CSV exports inside `evidence/comsol_original_csv/`, including `Drain Current.csv` (COMSOL 5.3.0.316, mosfet_v2.mph), and previous website numerical datasets were used to ground the model table and concrete figures.
- 26 thicknesses (5–30 nm inclusive at 1 nm step) × 61 gate voltage values (−2 to +4 V at 0.1 V step) = 1,586 simulated conditions, Vd = 0.1 V.
- Ideal C′ox is analytical. gm is numerical derivative of exported current. Gate leakage and breakdown are **not** computed by this Thin Insulator Gate model.
- The original `.mph` is not distributed here. Fine details not evidenced by exported data (e.g., exact doping and solver tolerances) were not invented.

## Packaging

- `index.html` and `MOS_COMSOL_Offline.html` contain the same updated v10.3 website.
- `COMSOL_Methodology.md` contains a printable/editable setup summary.
- `COMSOL_Image_Manifest.csv` remains the validated manifest for **historical 654 × 480** images in the full ZIP, not the separate newer 1280 × 600 manifest.
- Historical QA remains under `evidence/qa/` for provenance.
