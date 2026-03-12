# Projects — Eli Webb

CS graduate from Oklahoma State University (Dec 2025). This repository contains coursework and personal projects spanning systems programming, concurrent software design, applied AI, and numerical computing.

---

## Systems Programming (C)

### Producer-Consumer with Deadlock Demo
**Technologies:** C, POSIX Threads, Mutexes, Condition Variables

A multi-threaded producer-consumer system built to demonstrate and diagnose deadlocks in concurrent software.

- 2 producers, 2 consumers, and an 8-slot circular buffer coordinated with mutexes and condition variables to process 100 total items without data loss
- 3 run modes: correct synchronization, intentional deadlock, and deadlock resolution — deliberately engineering the deadlock by satisfying all four necessary conditions (mutual exclusion, hold-and-wait, no preemption, circular wait)
- Background monitor thread polling every 3 seconds to detect deadlock-induced stalls
- Thread-local storage variant demonstrating per-thread memory isolation

---

### Student Registration System
**Technologies:** C, POSIX Message Queues, Process Forking

A 3-process pipeline simulating a student registration backend using inter-process communication.

- Frontend, database, and logger processes communicate over POSIX message queues
- Implements a requeue pattern for handling concurrent registration requests
- Forked child processes handle independent execution paths with isolated memory

---

### Threads, Processes & Memory
**Technologies:** C, pthreads, fork()

A collection of 5 focused programs exploring the boundary between threads and processes at the OS level.

- Fork vs. thread memory isolation experiments
- Race condition demonstration: 5 threads × 100,000 increments without synchronization
- Thread-local storage using `__thread` keyword

---

## Applied AI & Machine Learning

### Reinforcement Learning Agent
**Technologies:** C#, Python, Unity ML-Agents

Designed and trained an autonomous agent to optimize reward-driven behavior across multi-episode training sessions.

- Agent learns to collect targets and avoid obstacles through iterative policy refinement
- Tuned hyperparameters including learning rate, batch size, and reward scaling; monitored convergence metrics to achieve stable policy improvement
- Engineered simulation environments to test behavioral generalization beyond training conditions

---

## Numerical Methods (Python)

A series of Python projects applying numerical algorithms to real engineering and scientific problems.

### Applied Root-Finding — Engineering Problems
**Technologies:** Python, NumPy, SciPy, Matplotlib

- Applied Brent's method, Newton-Raphson, and `fsolve` to 3 real engineering problems: open-channel flow (Bernoulli's equation), real gas molar volume (van der Waals equation), and pipe bend geometry optimization
- Compared convergence behavior and accuracy across methods for simple and triple-root functions

### Gaussian Elimination with Partial Pivoting
**Technologies:** Python, NumPy

- Built Gaussian elimination with partial pivoting from scratch on a 5×5 linear system
- Includes back substitution, residual norm analysis, and verification against NumPy's solver

### Floating-Point Precision & Catastrophic Cancellation
**Technologies:** Python, `decimal` module

- Diagnosed catastrophic cancellation in standard float arithmetic
- Determined a minimum of 37 decimal digits of precision required for correct evaluation using Python's `decimal` module

### Numerical Differentiation & Integration
**Technologies:** Python, NumPy, JAX, Matplotlib

- Central differences and Richardson extrapolation for derivative approximation
- JAX autodifferentiation benchmarked against manual methods
- Trapezoidal, Romberg, Simpson's, and adaptive quadrature on oscillatory functions and P-V data

### Numerical Optimization
**Technologies:** Python, SciPy

- Nelder-Mead and bounded minimization on multi-variable objective functions
- Geometric median of point clouds

---

## Databases

### Full-Stack Course Evaluation System
**Technologies:** Python, SQLite, SQL

A team-built system for submitting and querying course evaluations with a normalized relational backend.

- Designed normalized relational schemas with associative tables and enforced unique ID generation for accurate data linkage across professors, courses, and degree records
- Built backend logic for data submission, relational linking, and SQL query optimization
- Implemented structured input validation and secure data persistence

---

## Contact

**Email:** elibwebb123@gmail.com  
**LinkedIn:** linkedin.com/in/eli-webb1  
**GitHub:** github.com/eliwebb11
