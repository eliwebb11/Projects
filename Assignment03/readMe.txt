# Assignment 03 — Threads, Processes & Memory

---

## Overview

This assignment explores the behavior of shared and private memory variables across threads and forked processes in C. Programs demonstrate how `global`, `static`, `local`, and dynamically allocated variables behave under different concurrency models, including race conditions and thread-local storage.

---

## Files

| File | Description |
|------|-------------|
| `Question1.c` | Fork 3 child processes, each spawning 3 threads; observe variable scope |
| `Question2b.c` | Threads fork child processes; shared static variable across threads |
| `Question2c.c` | Same as 2b but with thread-local (`__thread`) static variable |
| `Question3.c` | Mixed `fork()` + `pthread` program; demonstrates exec-in-thread issues |
| `Question4.c` | 5 threads each doing 100,000 increments; demonstrates race conditions |

---

## Compilation & Running

```bash
gcc Question1.c  -o question1  -lpthread && ./question1
gcc Question2b.c -o question2b -lpthread && ./question2b
gcc Question2c.c -o question2c -lpthread && ./question2c
gcc Question3.c  -o question3  -lpthread && ./question3
gcc Question4.c  -o question4  -lpthread && ./question4
```

---

## Program Summaries

### Question 1 — Fork then Thread

The parent forks 3 child processes. Each child spawns 3 threads, and each thread increments all 4 variable types.

**Key behavior:** Forked children get a copy-on-write snapshot of the parent's memory. Threads within a child share that child's global/static space, so those reach 3 after all threads finish. The parent's copies remain at 0 since it never runs the thread function.

| Variable | Parent | Each Child |
|----------|--------|------------|
| global_var | 0 | 3 |
| static_var | 0 | 3 |
| local_var | — | 1 (per thread) |
| dynamic_var | — | 1 (per thread) |

---

### Question 2b — Thread then Fork

3 threads are created first. Each thread increments variables, then forks 3 child processes.

**Key behavior:** Children inherit the thread's already-incremented memory snapshot (values at 1), then increment again (reaching 2). Threads wait for their children before printing. Since all 3 threads share global/static, those can reach up to 3 in the parent (with race conditions possible).

| Variable | Parent Thread | Each Child |
|----------|---------------|------------|
| global_var | 3 | 4 |
| static_var | 3 | 4 |
| local_var | 1 | 2 |
| dynamic_var | 1 | 2 |

---

### Question 2c — Thread-Local Static

Same structure as 2b, but `static_var` is declared with `__thread`, giving each thread its own private copy.

**Key behavior:** `static_var` no longer accumulates across threads — each thread starts at 0 independently, reaches 1 after its own increment, then 2 in its children. `global_var` still races across threads. The parent's `static_var` prints as 0 since main's thread-local copy was never incremented.

---

### Question 3 — Fork + Exec Inside a Thread

Creates 2 threads and forks from main. Thread 1 calls `fork()` internally and uses `execvp("ls", ...)` in the child.

**Key behavior:** Calling `execvp()` inside a thread replaces the entire process image, which is dangerous in a multithreaded program. Output order is non-deterministic. Identified issues include reusing a single `pthread_t` for two threads, missing `pthread_exit()` on exec failure, and mixing `fork()` with threads.

**Possible outputs vary** based on scheduling — thread 1 may or may not complete before the main fork, and exec may succeed or fail.

---

### Question 4 — Race Condition Demo

5 threads each increment `global_var`, `static_var`, `local_var`, and `dynamic_var` 100,000 times each.

**Key behavior:** `local_var` and `dynamic_var` are private per thread — both reliably reach their expected values (100,042 and 100,000 respectively). `global_var` and `static_var` are shared with no synchronization, so increments are lost due to race conditions and the final values fall well short of the expected 500,000.

---

## Notes

- All programs require linking with `-lpthread`
- Output order for multi-threaded programs is non-deterministic and may vary between runs
- Question 2c's `__thread` keyword requires GCC with C11 or later (`-std=c11` if needed)
