# MOS Gate Oxide v10.7 — QA

## Scope

Small changes to v10.6 only: direct HTML report link with its figures, shorter Summary card, taller Chapter 04 oxide-field chart. The `.mph` Drive link, underlying COMSOL numerical arrays, questions and answers, all other chart sources and optional `images/` paths are unchanged.

## Static and provenance checks

- The HTML report was unpacked *without modifications* from `report(5).zip`. All 71 `<img>` references and its `report.css` resolve inside `report/Untitled_files/` relative to `report/Untitled.html`.
- The original nested `COMSOL_Report.zip` was removed. The model report link is a normal `href="report/Untitled.html"` with `target="_blank"`; visitors must first extract the website ZIP.
- The `.mph` model link remains the user-provided Drive URL, not a bundled model file. Live sharing permissions are unverified.
- `index.html` and `MOS_COMSOL_Offline.html` are byte-identical.
- All 1,586 simulation combinations are preserved. SHA-256 of the embedded COMSOL numerical dataset: `cb92f440a2c066ce8b07dcb2cbb71264dbb39fd5b4a238ee700f0ebee676c29f`, matching v10.6.
- Only Chapter 04 graph viewport height changed, from 370 to 510 in SVG coordinate units. `render4` data fields, labels, markers, y scale and x scale remain unchanged.

## Browser regression checks

Chromium was used with the actual site HTML passed as page content for the in-page interactive tests, at **360, 390, 600, 720, 810, 1024, 1280, 1536, 1650, 1920 px**.

At each width: Skip to Summary, Restart, four questions answered (correct and incorrect), next/feedback, final graded Summary and Restart again (12 sampled layout states per viewport). All passed:

- Quiz card height drift: **0 px** within each viewport.
- Method / Reproducibility heading position drift: **0 px** within each viewport.
- Summary text and Restart remained inside the white card.
- Horizontal overflow and JavaScript errors: **none**.
- Desktop (1280–1920 px): Chapter 05 card = **670 px**, equal to the existing Chapter 02 card.
- Narrow screens adapt naturally: 360 px = 1242 px, 390 px = 1145 px to avoid clipping.

**Limitation:** The sandbox Chromium environment blocks navigating to local `file://` and local HTTP URLs, so the live popup click could not be browser-verified. Instead, every report image and stylesheet reference was checked against the extracted files and the link target/target attributes were verified in the website DOM. The report is intended to open when the release is extracted and opened normally on Windows or hosted on a static site.

## Exclusions

- No re-simulation or independent `.mph` solver audit.
- No 6,344-image `images/` collection bundled; the user supplies it separately.
