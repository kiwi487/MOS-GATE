# MOS Gate Oxide v10.4 — Targeted Verification

**Baseline:** Exact user-uploaded `MOS_COMSOL_v10_3_Full.zip` (not reconstructed from v10.2).

## Scope: no major revisions

Only `index.html`, its byte-identical mirror `MOS_COMSOL_Offline.html`, `README.md`, `COMSOL_Methodology.md`, and `verify_package.py` were edited. Existing extracted original and processed COMSOL CSVs, organizer scripts, historical QA, and prior screenshots are preserved byte-for-byte. New v10.4 QA reports are additive. The original large `images/` tree is intentionally not shipped.

### Website fixes

1. `tickLabel()` now formats fractional Y-axis steps correctly (e.g., 2.5, 7.5 and 0.25). Graph points and chart math are unchanged.
2. `Measured` is changed to `Simulated` in two places; Chapter 02's 2D field choice is labeled **Electric field in silicon** to distinguish it from Chapter 04's **Gate-center oxide field**.
3. Chapter 05 retains the four-stage quiz, score, Next, individual explanations, Skip, Restart and the existing summary. The right Learning Path panel is hidden, question/answer targets are larger, four subtle progress dots replace the earlier progress bar, and correct/incorrect feedback uses restrained colors/motion (with reduced-motion support). The fourth question now directly compares stronger control with electric-field stress.
4. The COMSOL Application Library menu route is given below the existing model workflow, without a speculative absolute installation path.

## Numerical provenance & invariants

- **1,586** `t_ox`–`V_G` conditions, with fixed `V_D = 0.1 V`.
- The site-embedded `COMSOL` JSON block is **byte-for-byte identical** to the user-provided v10.3 baseline.
- Its contents were independently compared against the original COMSOL 5.3 CSV exports for drain current, electron integrated sheet charge, hole charge change relative to `V_G = 0`, surface-minus-bulk potential, and the gate-center oxide field. **7,930 of 7,930 values matched** within displayed/serialization precision.
- Ideal SiO₂ capacitance was recomputed independently for all 26 thicknesses using `eps0*3.9/t_ox`; all matched stored values. Exact tolerances and maximum differences are in `evidence/qa/MOS_v10_4_Data_QA.json`.
- The gate-center oxide field continues to use the **Cut Point 2D at (1.5, 0.7 μm)**. The distinct Gate boundary Line Average is not silently substituted.
- No COMSOL solution was rerun. This QA checks data consistency, not solver convergence or grid independence.

## Browser regression (Chromium, Playwright)

Four viewports: 1920×1080, 1280×720, 810×850, and 390×844. **25/25 assertions passed per viewport (100/100)**, covering chapter count and navigation, fifth-chapter layout, quiz options, feedback/locking/scoring, Q4 content, skip/restart, gm graph switch, initial Hole view, missing-image fallback, correct electric-field label, model path, fractional axis labels, absence of horizontal document overflow, and absence of uncaught JavaScript errors.

**Browser limitation:** This browser environment blocks direct `file://` navigation. Tests use Playwright `set_content` on the exact site HTML (matching the v10.3 QA methodology), so they exercise JS and DOM but cannot establish disk-based PNG loading here. The image lookup paths and `organize_images.py` were not changed; the user will supply PNGs separately. The image-free default displays an intentional missing-frame message.

## Packaging validation

- Both HTML entrypoints are byte-identical.
- The ZIP integrity test passes.
- The output explicitly excludes the complete `images/` collection of 6,344 PNGs (over 200 MB in the uploaded full package).
- `python verify_package.py` succeeds without images and verifies images when later provided. To require images, run `python verify_package.py --require-images`.

Existing `QA_REPORT.md`, the earlier test JSON, and historical screenshots remain prior-version evidence and are **not** represented as fresh v10.4 screenshots.
