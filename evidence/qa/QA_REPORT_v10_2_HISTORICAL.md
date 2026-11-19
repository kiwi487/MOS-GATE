# Browser check — MOS Gate Oxide v10.2

## Changes

- Moved the existing dynamic `chargeRegime` state badge from the chapter heading to the Carrier distribution card header, replacing the `Conceptual cross-section` caption.
- Changed the 2D map dropdown order to Hole concentration, Electron concentration, Electric field, Electric potential, and made Hole the default.
- All physics arrays, regime() classification logic, numerical chart routines, PNG image bytes, and image organizer remain unchanged.

## Verified in headless Chromium

- 5 viewports: 1920×1080, 1440×900, 1280×720, 810×850, and 390×844.
- At tₒₓ = 11 nm: V_G = −2 V → `Hole accumulation`; V_G = 0 V → `Depletion / transition`; V_G = +4 V → `Electron-rich channel`. All 15 assertions passed.
- Hole concentration is the first dropdown item, selected by default; real historical hole PNG at 11 nm, +0.8 V loaded from the expected path in the test fixture.
- The badge was within the card bounds with no overlap against its heading; no document-wide horizontal overflow or uncaught JavaScript errors in the five tested viewports.
- Switching to Electron concentration, using the gₘ graph tab, and starting/stopping the voltage autoplay were exercised in all five viewports.
- Screenshots are under `evidence/screenshots/v10_2/`, and structured output is in `evidence/qa/MOS_v10_2_QA.json`.

## Evidence caveats

- The 6,344 historical PNGs remain at 654×480 px. The separately uploaded 1280×600 manifest does not provide the corresponding image files.
- These are targeted regression tests for v10.2, not a repeat of the entire v10.1 55-state review. See the retained v10.1 historical QA for prior scope.
