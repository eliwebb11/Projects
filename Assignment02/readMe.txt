# Student Registration System

---

## Overview

A multi-process student registration system written in C that simulates a real-world pipeline using three concurrent processes communicating over a **POSIX message queue**. When a student is submitted by the frontend, the database assigns them an ID, and the logger confirms the registration — all happening in parallel via IPC.

---

## Architecture

```
[Frontend] ──► [Message Queue] ──► [Database] ──► [Message Queue] ──► [Logger]
```

The system uses three child processes forked from a parent:

| Process      | Role                                                                 |
|--------------|----------------------------------------------------------------------|
| **Frontend** | Submits student names to the queue (msg_type = 1)                   |
| **Database** | Receives type-1 messages, assigns a student ID, re-sends as type-2  |
| **Logger**   | Receives type-2 messages and logs confirmed registrations           |

Each process re-queues messages it isn't meant to handle, allowing all three to share a single queue without message loss.

---

## Files

```
assignment02.c   — Full source code (single-file program)
```

---

## Requirements

- Linux or any POSIX-compliant OS
- GCC compiler
- POSIX real-time library (`librt`)

---

## Compilation

```bash
gcc assignment02.c -o assignment02 -lrt
```

---

## Running

```bash
./assignment02
```

---

## Sample Output

```
[Frontend] @ 12s: Sending Alice...
[Database] @ 12s: Start processing Alice...
[Frontend] @ 13s: Sending Bob...
[Database] @ 15s: Finished processing Alice. Assigned ID: 1001
[Logger]   @ 15s: CONFIRMED - ID: 1001, Name: Alice
[Frontend] @ 14s: Sending Charlie...
...
[Parent] All processes finished. Queue destroyed.
```

> Timestamps reflect seconds within the current minute (`time(NULL) % 60`).

---

## How It Works

1. The **parent process** creates the POSIX message queue (`/student_reg_queue`) with a max of 10 messages.
2. Three child processes are forked: frontend, database, and logger.
3. The **frontend** sends 3 students (Alice, Bob, Charlie) as `msg_type = 1`, one per second.
4. The **database** polls for `msg_type = 1` messages, simulates a 3-second processing delay, assigns IDs starting at 1001, then re-sends as `msg_type = 2`.
5. The **logger** polls for `msg_type = 2` messages and prints a confirmation for each.
6. The **parent** waits for all three children to finish, then destroys the queue.

---

## Notes

- The message queue is unlinked at startup to ensure a clean state on each run.
- Database and logger use a **requeue pattern** — messages of the wrong type are put back on the queue so the correct process can pick them up.
- The `Student` struct is sent directly as raw bytes over the message queue.
