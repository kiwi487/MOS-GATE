# MOS Gate Oxide — v10.7 (No Images)

**R2 layout touch-up:** Centered the four-step *Simulation workflow* row and its arrows. All other sections and COMSOL values remain unchanged. Details: `QA_CENTER_R2.md`.

**Small, focused update to v10.6.** The five-chapter website, original COMSOL numerical arrays, four quiz questions, image-loading convention, and `.mph` Google Drive destination remain unchanged.

## Changes in v10.7

- **Open the report directly:** the Chapter 05 *View COMSOL model report (HTML)* link opens `report/Untitled.html` in a new browser tab. Its companion `report/Untitled_files/` contains all 71 embedded figures and `report.css`. **Extract the entire release ZIP first**; do not attempt to open the HTML from inside a ZIP viewer. The old nested `COMSOL_Report.zip` is no longer included.
- **Second model link:** *Original COMSOL model (.mph) · Google Drive* still opens the exact Google Drive URL supplied earlier. Sharing access is controlled by the owner.
- **Compact Summary:** desktop Chapter 05 white panel is now 670 px high, matching the existing Chapter 02 card; the four summary cards, readable text, gentle fade-in and correct/incorrect feedback remain. Quiz and Summary transitions retain the same height. On narrow screens, the panel expands only as needed to avoid clipping.
- **Chapter 04 electric field:** only the oxide-field chart viewport becomes taller (370 → 510 SVG viewBox units) to reduce visual blank space. Axes, plotted values, physics captions, and the other charts are unchanged.
- **No large map images included:** add your own `images/` folder beside `index.html` when needed. The small report's 71 figures are separate from the 6,344 optional COMSOL 2D frames.

## Quick start

1. Extract `MOS_COMSOL_v10_7_NoImages.zip` to a normal folder.
2. Open `MOS_COMSOL_v10_7/index.html` (or its identical `MOS_COMSOL_Offline.html`) using Chrome or Edge.
3. In **05 Challenge → Model / Reproducibility**, use **View COMSOL model report (HTML)** to see the report and its figures, or click the `.mph` Drive link.
4. To enable Channel Charge 2D maps, place your own `images/` folder alongside `index.html`; it is intentionally absent from this ZIP.
5. Optionally run `python verify_package.py` (no external dependencies) for a read-only verification. Details: `QA_REPORT_v10_7.md`.

**Data provenance:** The linked report is a 5 nm / 0.5 V example sweep, while the website charts use separate precomputed 1 nm / 0.1 V COMSOL data. The report describes a related example; it is not the exact numerical export of every website chart point.

---

## Previous v10.6 notes (historical)

# MOS Gate Oxide — v10.6 (No Images)

A focused update built **directly on v10.5**, with no changes to the COMSOL numerical arrays, charts, question content or Chapters 01–04. The original `images/` collection is not included.

## v10.6 changes

- Chapter 05 summary is slightly larger, with four subtle sequential card fades and gentle hover motion. The **quiz card keeps the same reserved-height behavior as v10.5** so the section below does not jump when switching between questions and summary. Reduced-motion settings disable the added animations.
- The bottom of *Simulation workflow* now has exactly **two visible links**: an offline download of the supplied `COMSOL_Report.zip` (the unmodified COMSOL 5.3 auto-generated HTML report, including its figures) and a Google Drive link to the `.mph` model file provided by the user. Drive access depends on the owner's sharing permissions. The former `.md` notes link is removed from the website; the historic notes file is retained only for archival compatibility.
- The current report documents a **5 nm / 0.5 V** example parameter study. The interactive website's embedded charts use the prior **1 nm / 0.1 V** COMSOL exports. These are separate evidence sets; the website's data are unchanged.

## Start v10.6

1. Open `index.html` (or the identical `MOS_COMSOL_Offline.html`) after extracting the ZIP.
2. At the bottom of Chapter 05, click **COMSOL model report (.zip)** to save the complete auto-report, or **Original COMSOL model (.mph) · Google Drive** to open the external model link.
3. To show 2D frames, put your own `images/` folder beside `index.html`; numerical plots and the quiz work without the images.
4. Run `python verify_package.py` to check the package and read `QA_REPORT_v10_6.md` for this version's regression results.

---

## Previous v10.5 release notes

# MOS Gate Oxide — v10.5 (No Images)

This is the **official v10.5 minor update** built on the user's v10.4 website (which was itself patched directly from the supplied v10.3 Full package). Only Chapter 05 layout/readability and related QA documentation change. The four quiz questions, correct answers, explanations, other four chapters, COMSOL numerical data, formulas, and image-path behavior remain intact.

## Changes from v10.4

- **Stable Chapter 05 height:** the quiz card reserves enough space for either the answering view or the final summary. The model/reproducibility section below does not shift upward when the learner answers, skips to the summary, reaches the end, or restarts. Screen width changes recalculate the reservation.
- **Larger summary typography:** four brief takeaway cards have more legible headings and body text, slightly larger simple icons and summary takeaway text. The existing gentle summary fade-in and answer correct/incorrect animations remain unchanged.
- **No bulky image frames:** `images/` is deliberately absent. Copy your own `images/` folder next to `index.html` when you need interactive 2D COMSOL frames. All built-in numerical plots and the quiz work without it. Historical small screenshots in `evidence/screenshots/` are QA materials, **not** COMSOL frame collections.

## Start here

1. Extract the archive and open `MOS_COMSOL_v10_5/index.html` (or the identical `MOS_COMSOL_Offline.html`) with Chrome or Edge.
2. If needed, copy your existing **images/** folder inside `MOS_COMSOL_v10_5/`, alongside `index.html`. Preserve paths such as `images/hole/tox_11/vg_0.8.png`; no paths were renamed in v10.5.
3. Optionally run `python verify_package.py` to validate the site without requiring image frames. After providing your images, `python verify_package.py --require-images` additionally checks image presence and hashes against the matching included manifest.
4. See `QA_REPORT_v10_5.md` for the v10.5 browser checks, and `QA_REPORT_v10_4.md` for the prior release.

---

## Historical v10.4 release notes (retained)

# MOS Gate Oxide — v10.4 (No Images)

**This is a small patch directly on the user-supplied v10.3 Full package.** Its COMSOL numeric arrays, original CSV exports, earlier chapters, playback controls, four-stage quiz mechanism, and summary logic remain intact.

## Changes from v10.3

- Fixed Y-axis tick text for fractional increments (e.g. 2.5 and 7.5 MV/cm, 0.25 µC/cm²). Curve coordinates and COMSOL data are unchanged.
- Changed misleading `Measured` terms to `Simulated`. The Chapter 02 2D field selector is now explicitly *Electric field in silicon*; the Chapter 04 plot still shows *Gate-center oxide field* derived at the oxide interface.
- Chapter 05 keeps **four questions**, Next, answer locking, per-answer explanations, **Skip to summary**, score, Restart Challenge, and the model workflow. Its decorative right-side Learning Path panel is now hidden, the question/answers are larger, and correct/incorrect feedback has a very small, reduced-motion-aware animation. Q4 now asks the physical-thickness trade-off described in the earlier design discussion.
- Added the COMSOL Application Library source-model route under the existing model workflow (the installation path is not assumed).

## How to use this image-free package

1. Extract the ZIP; open `index.html` (or the identical `MOS_COMSOL_Offline.html`) in Chrome or Edge.
2. **The large `images/` directory is intentionally not bundled.** If desired, copy your existing `images/` folder alongside `index.html` with the same paths as v10.3, for example `images/hole/tox_11/vg_0.8.png`. The webpage automatically loads the matching frame.
3. If your images are not organized yet, the existing `Check_Images.bat`, `Run_Organize.bat` and `organize_images.py` are included. Place `Image.zip` alongside them and follow the original workflow.
4. The interactive 1,586-condition numerical charts work **without** the 2D images folder; the 2D panel displays a missing-image notice until its frames are supplied.
5. `python verify_package.py` validates the website without requiring images. After adding all PNG frames, it checks dimensions and per-file SHA against the matching historical manifest. Use `python verify_package.py --require-images` if you want missing images to be a hard failure.

**Manifest note:** `COMSOL_Image_Manifest.csv` is still the verified historical 654 × 480 manifest from v10.3. The alternative 1280 × 600 manifest in `evidence/manifests/` comes from the earlier upload and should only be treated as validated when the corresponding PNG files actually match its hashes. This v10.4 ZIP does not claim any new image verification.

For the targeted v10.4 checks, see `QA_REPORT_v10_4.md`. The older `QA_REPORT.md` and prior QA records are retained as historical v10.3 evidence.

---

## Historical v10.3 release notes (archived context)

The following section describes the **original v10.3 full ZIP**, which did include the large images directory. It does **not** describe the contents of this lean v10.4 ZIP.

# MOS Gate Oxide — v10.3

**New Chapter 05:** Four-step interactive question sequence on gate capacitance, channel carriers, thinner-oxide advantages and limits. Each choice receives immediate individualized physics feedback, and the learner can continue after an incorrect answer. Includes a non-scoring **Skip to summary** action, a graded summary after all four questions, and **Restart challenge**. A concise COMSOL workflow and parameters table are always below the quiz; detailed methodology in `COMSOL_Methodology.md`. Chapters 01–04 and COMSOL datasets are retained from v10.2.

# MOS Gate Oxide — v10.2 full offline package and evidence

## v10.2 changes (presentation only)

- Chapter 2: the `Conceptual cross-section` caption beside **Carrier distribution** has been replaced by the existing dynamic regime badge (`Hole accumulation`, `Depletion / transition`, or `Electron-rich channel`). The duplicate badge at the top right of the chapter has been removed. The existing classification based on COMSOL charge trends is unchanged; it is qualitative, not an extracted threshold voltage.
- Chapter 2 2D map quantity selector: **Hole concentration** now appears first and is the default, with **Electron concentration** second; field and potential follow unchanged.
- All previous COMSOL numerical data, image frames, calculations, playback controls, and organizer scripts are unchanged.
- `evidence/qa/MOS_v10_1_QA.json` and previous screenshots remain **historical v10.1 evidence**; refer to `evidence/qa/MOS_v10_2_QA.json` for current version testing.

## Starting the website

1. Extract the **entire** archive (do not open HTML directly from a ZIP viewer).
2. Open `index.html` or `MOS_COMSOL_Offline.html` in Chrome or Edge.
3. Keep the `images/` folder beside the HTML. Both HTML files refer to the same image directory.
4. For GitHub Pages, publish the extracted folder contents with `index.html` at the repository root.

## Images in this archive (fully verified)

- **6,344 existing images:** electron, hole, electric field, electric potential; **1,586 per quantity**.
- **654 × 480 px** PNGs, originally provided via the historical `Image.zip`.
- Path shape: `images/electron/tox_05/vg_-2.0.png`, etc.
- `COMSOL_Image_Manifest.csv` is the **verified 654 × 480 manifest**, matching these actual files.
- All 6,344 old source PNG hashes were checked against the verified manifest before packaging.
- The corresponding images are included **once** (no duplicate `Image.zip` inside the archive).

## Different uploaded manifest for 1280 × 600 images

`evidence/manifests/COMSOL_Image_Manifest_1280x600_UPLOADED_UNVERIFIED.csv` is the **user's uploaded file**, preserved without editing. It includes 6,344 expected website paths, but each of its 6,344 SHA-256 values differs from the available old-image content. The new 1280 × 600 PNGs are **not present in the available inputs**, so their content has **not** been authenticated or visually checked.

**Do not replace** the root verified manifest with this new manifest unless the matching new PNGs have actually been collected and validated.

When the new `Image.zip` arrives, put it beside `organize_images.py` and run `Check_Images.bat` (strict 1280 × 600 check) then `Run_Organize.bat` to replace `images/` and generate a new root manifest.

## Included evidence

- `evidence/qa/MOS_v10_1_QA.json` and `QA_REPORT.md`: previous v10.1 browser interaction/layout checks (historical evidence, not a new independent browser rerun).
- `evidence/qa/manifest_comparison.json`: independent old/new manifest structure and SHA comparison.
- `evidence/screenshots/`: actual v10.1 page previews across several viewports and plot modes.
- `evidence/comsol_original_csv/`: original exported COMSOL results used for the site.
- `evidence/comsol_processed/`: existing post-processed CSVs, scientific plots, and archive evidence.
- `evidence/postprocess/`: prior COMSOL 5.3 post-processing notes.
- `verify_package.py`: read-only validator for the extracted website's 6,344 PNGs and verified per-image SHA-256. Run `python verify_package.py`.

## Scientific and operational caveats

- The COMSOL Thin Insulator Gate model does not itself calculate direct oxide tunneling leakage or dielectric breakdown.
- Charge curves and drain current use exported COMSOL data. Ideal oxide capacitance is analytical. Transconductance is numerically differentiated from the saved I_D-V_G values.
- This package is intended for offline presentations; GitHub Pages deployment should include only website files and images, rather than the `evidence/` directory, if you want to minimize the online repository size.
