# Producer-Consumer with Deadlock Demo

---

## Overview

A multi-threaded producer-consumer program using circular buffers and POSIX threads in C. The program runs in one of three modes to demonstrate correct synchronization, intentional deadlock, and the fix for that deadlock.

---

## Files

| File | Description |
|------|-------------|
| `assignment04_webb_eli.c` | Full source code |

---

## Compilation

```bash
gcc assignment04_webb_eli.c -o assignment04 -lpthread
```

---

## Running

The program requires exactly one mode flag:

```bash
./assignment04 --partA      # Basic producer-consumer
./assignment04 --deadlock   # Introduces deadlock
./assignment04 --fixed      # Resolves the deadlock
```

Shorthand flags `A`, `D`, and `F` also work.

---

## Program Structure

| Component | Count | Description |
|-----------|-------|-------------|
| Producers | 2 | Each produces 50 items into the circular buffer |
| Consumers | 2 | Consume items until all producers are done and buffer is empty |
| Monitor | 1 | Background thread that checks for stalls every 3 seconds |
| Buffer | 8 slots | Circular buffer shared between all producers and consumers |

---

## Modes

### `--partA` — Basic Producer-Consumer

Standard producer-consumer synchronization using a single mutex (`buffer_mutex`) and two condition variables (`not_full`, `not_empty`). Producers block when the buffer is full; consumers block when it is empty. No deadlock is possible.

### `--deadlock` — Intentional Deadlock

Two additional mutexes (`mutex_left`, `mutex_right`) are introduced. Even-numbered producers lock left then right; odd-numbered producers lock right then left. This inconsistent ordering creates a circular wait where each producer holds one lock and waits for the other, causing the program to hang.

**All four deadlock conditions are present:**

- **Mutual exclusion** — mutexes can only be held by one thread at a time
- **Hold and wait** — each producer holds one lock while waiting to acquire the other
- **No preemption** — locks are not forcibly released; threads must unlock themselves
- **Circular wait** — Producer 1 holds left and waits for right; Producer 2 holds right and waits for left

### `--fixed` — Deadlock Resolution

Both producers acquire locks in the same consistent order (left then right). This eliminates circular wait — since no two producers can be waiting on each other, deadlock cannot occur.

---

## Monitor Thread

The monitor thread wakes every 3 seconds and checks whether `operations_done` has increased since its last check. If no progress is detected for 6 consecutive seconds (2 checks), it prints a stall warning. This makes deadlock in `--deadlock` mode visible in the output.

```
[Monitor] Warning: no activity detected for 6 seconds. Possible stall.
```

---

## Sample Output (`--partA`)

```
[Producer 1] produced item 1000 -> buffer now has 1 item(s)
[Consumer 1] consumed item 1000 -> buffer now has 0 item(s)
[Producer 2] produced item 2000 -> buffer now has 1 item(s)
[Monitor] System healthy: progress observed.
...
All producers and consumers have finished. Final buffer count = 0
```

---

## Notes

- Compile with `-lpthread` on all platforms
- The deadlock mode may hang indefinitely — use `Ctrl+C` to terminate
- Output order is non-deterministic due to thread scheduling
