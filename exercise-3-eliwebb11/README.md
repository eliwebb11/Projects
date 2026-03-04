# Root Finding Methods

---

## Overview

This exercise compares numerical root-finding methods from SciPy on two test functions — `bar(t)` and `baz(t)` — across three known root intervals. It also generates plots to visually examine function behavior near roots.

---

## Files

| File | Description |
|------|-------------|
| `exercise3.py` | Main script containing all four questions |
| `Q3-a-bar.pdf` | Plot of `bar(t)` over [5.0, 9.0] |
| `Q3-b-baz.pdf` | Plot of `baz(t)` over [5.0, 9.0] |
| `Q3-c-bar.pdf` | Plot of `bar(t)` over [7.0, 7.5] |
| `Q3-d-baz.pdf` | Plot of `baz(t)` over [7.0, 7.5] |

---

## Requirements

- Python 3
- NumPy, SciPy, Matplotlib

```bash
pip install numpy scipy matplotlib
```

---

## Running

```bash
python exercise3.py
```

PDF plots are saved to the working directory automatically.

---

## Test Functions

Both functions share roots at approximately `t = 1/3`, `t = 7 + 1/3`, and `t = 1024 - 2/3`, tested over the intervals `(0,1)`, `(7,8)`, and `(1023,1024)`.

- **`bar(t)`** — product of three linear factors times `cos(t/600)`. Simple roots; well-behaved for all methods.
- **`baz(t)`** — same roots but each factor is cubed, creating triple roots. Methods that rely on sign changes struggle here since the function does not cross zero — it only touches it.

Analytic first derivatives (`diff_bar`, `diff_baz`) are provided for Newton's method.

---

## Question Summaries

### Question 1 — Bisection on `bar(t)`

Applies `scipy.optimize.bisect` to each of the three intervals with tolerance `1e-16`. Prints a table showing convergence, root location, iteration count, and function call count.

### Question 2 — Method Comparison on `bar(t)`

Applies three methods to each interval and compares their efficiency:

| Method | Strategy |
|--------|----------|
| `ridder` | Bracketing method using a midpoint trick; faster than bisection |
| `brentq` | Hybrid of bisection, secant, and inverse quadratic; generally fastest |
| `newton` | Uses analytic derivative (`diff_bar`); quadratic convergence near the root |

### Question 3 — Plotting

Generates four PDF plots to visually compare `bar` and `baz` over the interval around the middle root (`t ≈ 7.33`):

- Wide view `[5.0, 9.0]` shows the overall shape of the crossing/touch
- Zoomed view `[7.0, 7.5]` reveals how `baz` merely touches zero (triple root) while `bar` crosses it

### Question 4 — Bisection, Ridder & Brentq on `baz(t)`

Applies the three bracketing methods to the triple-root function `baz`. Since `baz` does not change sign at its roots, standard bracketing methods cannot detect them — convergence behavior and any failures are compared across all three intervals and methods.

---

## Sample Output

```
CS 3513, Spring 2025
Exercise 3
StudentName =  Eli Webb
GitHub Username =  eliwebb11

Question 1
method name     converged       root location             number of iterations      number of function calls
bisect          1               1023.3333333333...        ...                       ...

Question 2
method name     converged       root location             ...
ridder          1               0.3333333333...           ...
brentq          1               0.3333333333...           ...
newton          1               0.3333333333...           ...
...
```
