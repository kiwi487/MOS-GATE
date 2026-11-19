# MOS Gate Oxide — COMSOL Simulation Notes (v10.4)

## Purpose and provenance

This handout describes the setup evidenced by the earlier COMSOL 5.3 result exports and the corresponding interactive website. It is not an independently verified full `.mph` reconstruction, and the `.mph` model is not included in this release. The webpage replays precomputed numerical results.

## Original COMSOL Application Library model

- **File → Application Libraries → Semiconductor Module → Devices → mosfet**
- Template relative path (installation location can differ): `applications/Semiconductor_Module/Devices/mosfet.mph`.
- For modifications, use **Save As** to a separately named `.mph` file rather than editing the shipped template. The webpage does not include the `.mph` model.

## Model and boundary conditions

- Device: 2D NMOS in p-type silicon, with source, drain, gate and gate dielectric represented in the semiconductor simulation.
- Software: COMSOL Multiphysics 5.3 (export header: COMSOL 5.3.0.316); model identified in exported CSV as `mosfet_v2.mph`.
- Semiconductor physics interface, with a **Thin Insulator Gate** gate boundary condition.
- Dielectric: SiO₂, modeled with relative dielectric constant εr = 3.9.
- Drain voltage: Vd = +0.1 V, held fixed.
- Gate voltage: Vg = −2 to +4 V, in 0.1 V increments (61 values).
- Oxide thickness: tox = 5 to 30 nm, in 1 nm increments (26 values).
- Unique combinations: 26 × 61 = **1,586**.

The full mesh, doping concentrations, detailed source/drain contact settings, and solver tolerances cannot be completely reconstructed from the supplied CSV exports; consult the original model for those. This note does not invent them.

## Reproducing the plotting and numerical workflow

1. Open the original 2D NMOS model in COMSOL 5.3 and verify the semiconductor interface, material assignments, and gate boundary setup.
2. Define parameters for `tox`, `Vg`, and `Vd`, and use SiO₂ relative permittivity 3.9. Check the physical meaning and units of the gate oxide thickness in the **Thin Insulator Gate** condition.
3. Apply the intended gate/drain biases and perform parameter sweeps over the 26 oxide thicknesses and 61 gate voltages with `Vd = 0.1 V`.
4. Export the simulated drain terminal current, electron and hole charge measures, surface and bulk potentials, and the gate-boundary oxide field. Use the original result files and corresponding dataset selections; a CSV alone does not fully specify the geometry/integration features.
5. Export four image sequences (electron, hole, electric field, potential) in the same thickness/voltage order. The website accepts 1280 × 600 PNGs using the included `organize_images.py` script; the historical v10.3 examples were 654 × 480; this v10.4 release intentionally omits the large `images/` directory.
6. Load the website with its `images/` directory beside `index.html`; browser sliders select existing COMSOL results, they do not start new COMSOL calculations.

## Data interpretation

- Ideal oxide capacitance per area is computed analytically: `C'ox = ε0 εr / tox`.
- Transconductance is calculated by numerical differentiation: `gm = d(ID) / d(Vg)` at fixed drain voltage.
- The exported electron charge is a **total integrated electron sheet charge over a specified cut**, not a background-subtracted, independently extracted inversion charge. The hole-change curve is referenced to the relevant baseline.
- Gate oxide field is evaluated from boundary-normal displacement field; the webpage quotes approximately **7.29 MV/cm** for 5 nm and **1.27 MV/cm** for 30 nm at Vg=4 V.
- At Vg=4 V and Vd=0.1 V, exported ID is approximately **201.04 µA** at 5 nm and **25.27 µA** at 30 nm.
- This Thin Insulator Gate model **does not simulate direct gate tunneling leakage or dielectric breakdown**; these are physical design concerns rather than computed outcomes here.

## Original data

The full evidence package includes `evidence/comsol_original_csv/` with eight COMSOL result CSV files, including `Drain Current.csv`, `Electron_Charge.csv`, `Hole_Charge.csv`, `Surface_Potential.csv`, and `Oxide Field Boundary.csv`. The package contains manifests and separate browser test evidence. A separately uploaded **1280 × 600** manifest is not the same as the bundled **654 × 480** PNG content; do not substitute it for the verified bundled manifest unless the actual new PNGs are supplied.
