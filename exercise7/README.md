# Numerical Integration

---

## Overview

This exercise applies several numerical integration methods — trapezoidal rule, Romberg integration, Simpson's rule, and SciPy's adaptive quadrature — to three different problems, comparing accuracy and efficiency across approaches.

---

## Files

| File | Description |
|------|-------------|
| `exercise7.py` | Main script containing all three questions |
| `ex7q1plot.pdf` | Plot of `f(x) = e^(-x²)` over [0, 1] |
| `ex7q2plot.pdf` | Plot of the oscillatory function for Question 2 |
| `ex7q3plot.pdf` | Pressure vs. Volume data plot for Question 3 |

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
python exercise7.py
```

---

## Question Summaries

### Question 1 — Integrating e^(-x²) over [0, 1]

The exact value is known analytically via the error function: `erf(1)·√π / 2`.

| Part | Method | Description |
|------|--------|-------------|
| (a) | Analytical | Reference value computed from `math.erf` |
| (b) | Plot | Visualizes `f(x) = e^(-x²)` |
| (c) | Trapezoidal rule | Applied at 8 refinement levels (n = 1, 2, 4, ..., 128); error printed at each level |
| (d) | Romberg integration | Richardson extrapolation table built from trapezoidal estimates; diagonal entries `R[i][i]` shown with errors |
| (e) | `scipy.integrate.quad` | Adaptive quadrature estimate and error vs. exact value |
| (f) | Function call count | Compares total evaluations for `quad` vs. Romberg (255 for 8 levels) |

---

### Question 2 — Integrating an Oscillatory Function over [1.5, 4]

Integrates `f(x) = (200 / (2x³ - x²)) · (5·sin(20/x))²`, a rapidly oscillating function. The `quad` result is used as the reference since no closed-form exists.

| Part | Method |
|------|--------|
| (a) | Plot of `f(x)` over [1.5, 4] |
| (b) | `scipy.integrate.quad` — adaptive quadrature with error estimate |
| (c) | Trapezoidal rule at 8 refinement levels; error relative to `quad` |
| (d) | Romberg table built from trapezoidal estimates; diagonal shown with errors |

The oscillatory nature of this function makes fixed-grid methods converge slowly compared to adaptive quadrature.

---

### Question 3 — Work from Pressure-Volume Data

Integrates tabular pressure-volume data (9 data points, `v` from 0.75 to 2.75 cubic inches) to estimate mechanical work in inch-pounds.

| Part | Method |
|------|--------|
| (a) | Plot of P vs. V with styled markers |
| (b) | `scipy.integrate.trapezoid` |
| (c) | `scipy.integrate.simpson` |
| (d) | `scipy.integrate.romb` with full table output |
| (e) | Discussion — Simpson is preferred over Romberg for this dataset because its quadratic approximation better captures the curvature of the P-V relationship, and it is better suited to small, evenly-spaced datasets |

---
