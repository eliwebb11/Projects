# CS 3513 — Exercise 1: Error Analysis & Floating Point

---

## Overview

This exercise covers numerical error propagation, IEEE 754 floating-point representation, and series approximation. Implemented as a Python script converted from a Jupyter notebook.

---

## Files

| File | Description |
|------|-------------|
| `exercise1.py` | Main script containing all three questions and helper functions |

---

## Requirements

- Python 3
- NumPy (`pip install numpy`)

---

## Running

```bash
python exercise1.py
```

---

## Question Summaries

### Question 1 — Error Propagation (10 pts)

Applies error propagation rules of thumb to estimate absolute and relative errors for `x = 75 ± 0.5`:

- **(a)** Absolute and relative error of `x`
- **(b)** Absolute and relative error of `x + x`
- **(c)** Absolute and relative error of `x * x`
- **(d)** Absolute and relative error of `y = f(x) = 4x³ - 3x² + 1` using `|Δy| ≈ |f'(x)| · |Δx|`

### Question 2 — Floating-Point Representation (5 pts)

Explores IEEE 754 double-precision gaps using `numpy.spacing()`:

- Computes the machine epsilon gap at `x = 1.0` and evaluates neighboring representable values
- Repeats at `x = 2^300`, identifying the next larger and previous smaller values using hex float notation

### Question 3 — Series Approximation of 1/e (8 pts)

Implements `EstimateEInverse(tolerance, maxIterations)` to approximate `1/e` via the alternating series:

```
1/e = 1 - 1/1! + 1/2! - 1/3! + ...
```

Iterates until the next term falls below the given tolerance. Compared against `math.exp(-1)` at tolerances of `1e-7` and `1e-12`.

---

## Sample Output

```
CS 3513, Spring 2025
Exercise 1
StudentName =  Eli Webb
GitHub Username =  eliwebb11
Question 1
  (a) abs_err_x = 0.50000000,         rel_err_x = 0.00666667
  (b) abs_err_x_plus_x = 1.00000000,  rel_err_x_plus_x = 0.00666667
  ...
Question 3
  Using tolerance 1.00e-07
     Estimate 1/e = 0.36787944... with absolute error ...
  Using tolerance 1.00e-12
     Estimate 1/e = 0.36787944117144... with absolute error ...
```
