# Numerical Differentiation

---

## Overview

This exercise explores multiple approaches to numerical differentiation: finite differences, Richardson extrapolation, automatic differentiation via JAX, and discrete derivative estimation on tabular data.

---

## Files

| File | Description |
|------|-------------|
| `exercise6.py` | Main script containing both questions |

---

## Requirements

- Python 3
- NumPy, JAX

```bash
pip install numpy jax
```

---

## Running

```bash
python exercise6.py
```

---

## Question Summaries

### Question 1 — Derivatives of tanh(x) at x = π/5

Seven sub-parts compute or estimate the first and second derivatives of `f(x) = tanh(x)` at `t = π/5`.

| Part | Method | Description |
|------|--------|-------------|
| (a) | Analytical | Exact value: `1/cosh²(t)` |
| (b) | Finite difference | Central difference with step `h = π/10` |
| (c) | Finite difference | Central difference with smaller step `h = π/20` |
| (d) | Richardson extrapolation | Combines (b) and (c): `(4·h2 - h1) / 3` for higher-order accuracy |
| (e) | Automatic differentiation | First derivative via JAX `grad()` |
| (f) | Finite difference | Second derivative using 3-point stencil with `h = π/20` |
| (g) | Automatic differentiation | Second derivative via JAX `grad(grad())` |

Richardson extrapolation (d) improves on the raw finite difference estimates by canceling the leading error term. JAX automatic differentiation (e, g) produces machine-precision results without approximation.

---

### Question 2 — Velocity and Acceleration from Position Data

Uses tabular position data `x(t)` sampled every 2 seconds from `t = 0` to `t = 16`.

- **(a)** Estimates velocity at `t = 10` using a central finite difference on the surrounding data points
- **(b)** Estimates acceleration at `t = 10` using the 3-point second-derivative stencil
- **(c)** Re-estimates velocity at `t = 10` using `numpy.gradient`, which applies central differences across the full dataset

---
