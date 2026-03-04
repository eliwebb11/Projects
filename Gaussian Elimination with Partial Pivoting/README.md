# Gaussian Elimination with Partial Pivoting

---

## Overview

This exercise manually implements Gaussian elimination with partial pivoting on a 5×5 linear system `Ax = b`. Each elimination step is printed as it runs, followed by back substitution, residual analysis, and comparison against NumPy's built-in solver.

---

## Files

| File | Description |
|------|-------------|
| `exercise5.py` | Single-file script; no external data files needed |

---

## Requirements

- Python 3
- NumPy (`pip install numpy`)

---

## Running

```bash
python exercise5.py
```

---

## Structure

The script solves a 5×5 system across six questions without using any built-in linear system solvers until Q6 (for verification only).

### Questions 0–3 — Gaussian Elimination Steps

For each of the 4 elimination columns, the script:

1. **Partial pivoting** — finds the row with the largest absolute value in the current column and builds a permutation matrix `P`
2. **Row swap** — applies `P` to `A` and `b`
3. **Elimination** — builds the elimination matrix `M` and zeros out all entries below the pivot
4. Prints `P`, `M`, the updated `A`, and the updated `b` after each step

After 4 steps, `A` is in upper triangular form.

### Question 4 — Back Substitution

Solves the upper triangular system using back substitution, computing each unknown `x[i]` from the bottom of the system up.

### Question 5 — Residual Check

Computes the residual `||A_original · x - b_original||` using the 2-norm to verify how close the computed solution is to satisfying the original system.

### Question 6 — Verification with NumPy

Solves the original system using `numpy.linalg.solve` and computes `||x_manual - x_numpy||` to confirm the manual elimination result matches the reference solver.

---

## Sample Output

```
Question 0, processing column 0
P)  ...
M)  ...
A)  ...
b)  ...

...

Question 4
x =  [ ... ]

Question 5
Residual Norm =  ...

Question 6
x  =  [ ... ]
Difference norm =  ...
```
