# CS 3513 — Exercise 2: Precision, Derivatives & Cancellation Error

---

## Overview

This exercise investigates the effects of floating-point precision on numerical computation, including catastrophic cancellation, finite difference approximations of derivatives, and the stability of equivalent algebraic formulas.

---

## Files

| File | Description |
|------|-------------|
| `exercise2.py` | Main script containing all three questions |

---

## Requirements

- Python 3
- NumPy (`pip install numpy`)

---

## Running

```bash
python exercise2.py
```

---

## Question Summaries

### Question 1 — Catastrophic Cancellation & Decimal Precision

Evaluates the function `foo(a, b)` at `a = 77617`, `b = 33096` using Python's standard `float` type and then Python's `decimal.Decimal` class at increasing precision levels (5, 10, 20, 30, 40, 50, 60 digits).

The standard `float` result is severely wrong due to catastrophic cancellation — large intermediate terms nearly cancel, and double-precision doesn't have enough digits to represent the result correctly. By incrementally increasing decimal precision and narrowing back down, the minimum precision needed to get at least 16 correct digits is determined to be **37 decimal digits**.

### Question 2 — Finite Difference & Derivative Approximation

For the function `bar(x, c) = tanh(c·x)`, this question examines how well the finite difference ratio `(bar(x+dx, c) - bar(x, c)) / dx` approximates the true first derivative `d_bar(x, c) = c / cosh²(c·x)`.

Tests are run across a grid of:

- `x` values: `1e-2`, `1e-8`, `1e-16`
- Step sizes `dx = x / loop_value` for `loop_value` in `1e6`, `1e12`
- `c` values: `1e1`, `1e2`, `1e4`

For each combination, the table shows `bar(x,c)`, `bar(x+dx,c)`, the absolute difference (delta), the ratio delta/dx, the true derivative, and the estimated error. Very small `dx` values cause subtractive cancellation, degrading accuracy even as `dx → 0`.

### Question 3 — X-Intercept Formulas & Cancellation

Two algebraically equivalent formulas for computing the x-intercept from two points are implemented:

- **Method A:** `x = (x1·y0 - x0·y1) / (y0 - y1)`
- **Method B:** `x = x0 - ((x1 - x0)·y0) / (y1 - y0)`

Both are evaluated at 3-digit decimal precision using points `(1.02, 3.32)` and `(1.31, 4.31)`, then compared against a 16-digit reference. Method B is more numerically stable — Method A involves subtracting large products that can suffer from cancellation error, while Method B's structure keeps intermediate values smaller and closer in magnitude.

---

## Sample Output

```
CS 3513, Spring 2025
Exercise 2
StudentName =  Eli Webb
GitHub Username =  eliwebb11

Question 1
   float result is  -1.1805916207174113e+21
   Using Decimal precision of 5, result is  ...
   ...
   Need at least  37  decimal digits of precision to evaluate foo(a,b)

Question 2
   x=1.00e-02, dx=1.00e-08
     c          bar(x,c)  bar(x+dx,c) ; delta     ; ratio     ; devir     : est diff
   ...

Question 3
   methodA's x-intercept is  ...
   methodB's x-intercept is  ...
   methodB is the better formula due to lower cancellation error.
```
