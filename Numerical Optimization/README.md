# Numerical Optimization

---

## Overview

This exercise applies scalar and multidimensional optimization methods from SciPy to three problems: minimizing a parametric integral, finding the closest point on a parabola, and computing the geometric median of point clouds.

---

## Files

| File | Description |
|------|-------------|
| `exercise8.py` | Main script containing all three questions |
| `ex8q1plot.pdf` | Plot of f(p) vs p for Question 1 |
| `ex8q2plot.pdf` | Parabola and distance curve for Question 2 |
| `ex8q3plotA.pdf` | Contour plot with geometric median for point set A |
| `ex8q3plotB.pdf` | Contour plot with geometric median for point set B |
| `ex8pointsA.txt` | Input point cloud for Question 3 (set A) |
| `ex8pointsB.txt` | Input point cloud for Question 3 (set B) |

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
python exercise8.py
```

> **Note:** The file paths in Question 2 and Question 3 are currently hardcoded to a local Windows path. Update the `savefig` and `loadtxt` paths to match your environment before running.

---

## Question Summaries

### Question 1 — Minimizing a Parametric Integral

Defines `f(p) = ∫₀^π sin(x)·cos(p·x) dx` and finds the value of `p ∈ [0, 10]` that minimizes it. The integral is evaluated numerically at each `p` using `scipy.integrate.quad`, and the minimum is found using bounded scalar minimization.

**Method:** `scipy.optimize.minimize_scalar` with `method='bounded'`  
**Output:** Optimal `p`, minimum value `f(p)`, and number of function evaluations

**Plot:** `f(p)` over `p ∈ [-10, 10]` saved to `ex8q1plot.pdf`

---

### Question 2 — Closest Point on a Parabola

Finds the point `(x, x²)` on the parabola `y = x²` that is closest to the target point `(1, 2)`. The Euclidean distance from any point on the parabola to the target is minimized as a scalar function of `x`.

**Method:** `scipy.optimize.minimize_scalar` with `method='brent'`  
**Output:** Closest point coordinates and minimum distance

**Plot:** The parabola and distance function overlaid on the same axes, saved to `ex8q2plot.pdf`

---

### Question 3 — Geometric Median of Point Clouds

Computes the geometric median — the point minimizing total Euclidean distance to all points in a set — for two input files (`ex8pointsA.txt`, `ex8pointsB.txt`). Unlike the mean, the geometric median is robust to outliers.

**Method:** `scipy.optimize.minimize` with `method='Nelder-Mead'`, initialized at the first point in the set  
**Output:** Median coordinates printed for each set

**Plots:** Contour maps of the total distance function with data points (red) and the computed median (green star), saved to `ex8q3plotA.pdf` and `ex8q3plotB.pdf`

---
