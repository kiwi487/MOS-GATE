# Manifest provenance

- `COMSOL_Image_Manifest_654x480_VERIFIED.csv`: matches all **6,344 actual PNGs** bundled in `images/`, verified via full SHA-256 comparison with the source `Image.zip`.
- `COMSOL_Image_Manifest_1280x600_UPLOADED_UNVERIFIED.csv`: the uploaded future-resolution manifest, validated for row count, filenames, voltage and thickness sequences, and 1280x600 dimension claims **in its text fields only**; the corresponding 1280x600 PNGs were not provided.

These are not interchangeable; all 6,344 hash entries differ. Root `COMSOL_Image_Manifest.csv` always refers to the images actually bundled.
