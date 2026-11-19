NMOS COMSOL 5.3 Postprocess - R4
=================================

Problem
-------
R3 failed at line 69: model.result().numerical(intTag).setResult();
COMSOL reported ArrayIndexOutOfBoundsException: 2.
This proves that the failure is during numerical evaluation, not creation
of the R3 Cut Line / table / integral nodes. The exact internal cause cannot
be established from the popup alone.

Why R4 is different
-------------------
- Reuses an already created CutLine2D, previously proven to display the 4
  oxide-thickness curves from Study 2 / Solution 2 (dataset dset2).
- Creates an independent R4 Table and Line Integration (no tag collision
  with R2/R3).
- Preselects a single solution, not all 84 at once.
- Does not call setResult() automatically, avoiding the same failing path.
- Changes no physics, geometry, mesh, study settings, or saved solutions.

Install and test
----------------
1. Make a backup copy of your current .mph file.
2. Open the existing Model Method: NMOS_PostProcess.
3. REPLACE the entire method body with NMOS_PostProcess_53_R4.txt.
4. Check Syntax and run the method.
5. In the Debug Log, note the 'reusing Cut Line dataset tag' and label.
6. Confirm it is the SAME manual Cut Line previously used to plot the four
   curves (5, 10, 20, 30 nm).
7. Go to Results > Derived Values > NMOS Gate Center Electron Integral - R4.
8. Confirm Data Set is the valid manual Cut Line 2D; expression is
   -e_const*semi.N; unit is C/m^2.
9. With only First solution selected, click Evaluate. If that works,
   switch to All solutions and Evaluate again.
10. If evaluation still fails, capture the full COMSOL error and the
    actual R4 integration node settings. Avoid changing any Study.

Scope / limits
--------------
This is total electron sheet charge integrated over the existing cut line:
    Q_e,cut = -e * integral[n(y) dy]
It is not an exact inversion charge (requires background charge correction
and selection of a physically justified integration depth).

Verification
------------
Statically compared syntax/API entry points against COMSOL 5.3a documentation.
Actual COMSOL runtime verification unavailable in this environment.
