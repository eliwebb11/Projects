# CS 3513 — Exercise 4: Applied Root Finding

---

## Overview

This exercise applies root-finding methods to three real-world engineering and physics problems: open-channel hydraulics, pipe bend geometry, and the van der Waals gas equation. Each question plots the equation being solved and finds the root numerically.

---

## Files

| File | Description |
|------|-------------|
| `exercise4.py` | Main script containing all three questions |
| `ex4q1plot.pdf` | Plot of the hydraulic equation for Question 1 |
| `ex4q2aplot.pdf` | Pipe equation plot for θ = π/2 |
| `ex4q2bplot.pdf` | Pipe equation plot for θ = 3π/5 |
| `ex4q2cplot.pdf` | Pipe equation plot for θ = 2π/3 |
| `ex4q3plot.pdf` | Plot of the van der Waals equation for Question 3 |

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
python exercise4.py
```

All PDF plots are saved to the working directory automatically.

---

## Question Summaries

### Question 1 — Open Channel Flow (Brent's Method)

Finds the water level `h` at a bump in a channel using conservation of energy (Bernoulli's equation). Given a flow rate `Q = 1.2 m³/s`, channel width `b = 1.8 m`, upstream water level `h0 = 0.6 m`, and bump height `H = 0.075 m`, the equation solved is:

```
Q²/(2g·b²·h0²) + h0  =  Q²/(2g·b²·h²) + h + H
```

**Method:** Brent's method (`scipy.optimize.brentq`) on the interval `[0.4, 0.6]`

---

### Question 2 — Optimal Pipe Bend Angle (fsolve)

Finds the optimal bend angle `α` that minimizes total pipe length `L` connecting two pipe segments of widths `w0 = 10` and `w1 = 8`. The equation balances the angular contributions of both segments:

```
w0·cos(α)/sin²(α)  =  w1·cos(φ)/sin²(φ)     where φ = π - α - θ
```

Solved for three joint angles: **θ = π/2, 3π/5, 2π/3**. Total pipe length `L` is reported for each case.

**Method:** `scipy.optimize.fsolve` with initial guess `α = 0.5`

---

### Question 3 — Van der Waals Gas Volume (Newton-Raphson)

Finds the molar volume `V` of a real gas (chloroform) at `P = 2.0 atm` and `T = 313 K` using the van der Waals equation:

```
(P + a·n²/V²)(V - n·b) = nRT
```

With constants `a = 6.254198 atm·L²/mol²` and `b = 0.05422 L/mol`.

**Method:** Newton-Raphson (`scipy.optimize.newton`) with initial guess `V = 12 L`

---

## Sample Output

```
CS 3513, Spring 2025
Exercise 4
StudentName =  Eli Webb
GitHub Username =  eliwebb11

Question 1
Solution: h = 0.5*** m
Method: Brent's method

Question 2
a: Alpha = 0.**** L = **.**
b: Alpha = 0.**** L = **.**
c: Alpha = 0.**** L = **.**
Method: fsolve

Question 3
Solution: V = **.**  L
Method: Newton Raphson
Initial Value: 12
```
