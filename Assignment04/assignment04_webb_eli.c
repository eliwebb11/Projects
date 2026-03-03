// Author Name: Eli Webb
// Email: eli.webb@okstate.edu
// Date: 11/4/2025
// Program Description: This program implements a multi-threaded producer-consumer model using circular buffers and pthreads in C. It supports three modes: Part A (basic producer-consumer), Deadlock (introducing deadlock with mutexes), and Fixed (resolving deadlock).

#define _DEFAULT_SOURCE
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <time.h>
#include <errno.h>
#include <stdarg.h>
#include <stdint.h>

#define BUFFER_SIZE 8
#define NUM_PRODUCERS 2
#define NUM_CONSUMERS 2
#define ITEMS_PER_PRODUCER 50

typedef enum { RUN_MODE_A, RUN_MODE_DEADLOCK, RUN_MODE_FIXED } run_mode_t;

typedef struct {
    int buf[BUFFER_SIZE];
    int head;
    int tail;
    int count;
} circ_buf_t;

circ_buf_t buffer;
pthread_mutex_t buffer_mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t not_full = PTHREAD_COND_INITIALIZER;
pthread_cond_t not_empty = PTHREAD_COND_INITIALIZER;
pthread_mutex_t mutex_left = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t mutex_right = PTHREAD_MUTEX_INITIALIZER;

int producers_done = 0;
int operations_done = 0;  // Total number of produce + consume operations
run_mode_t program_mode = RUN_MODE_A;

static void safe_printf(const char *fmt, ...)
{
    va_list ap;
    va_start(ap, fmt);
    pthread_mutex_lock(&buffer_mutex);
    vprintf(fmt, ap);
    fflush(stdout);
    pthread_mutex_unlock(&buffer_mutex);
    va_end(ap);
}

static void buffer_put(int item)
{
    buffer.buf[buffer.tail] = item;
    buffer.tail = (buffer.tail + 1) % BUFFER_SIZE;
    buffer.count++;
}

static int buffer_get()
{
    int item = buffer.buf[buffer.head];
    buffer.head = (buffer.head + 1) % BUFFER_SIZE;
    buffer.count--;
    return item;
}

void *producer_thread(void *arg)
{
    int id = (int)(intptr_t)arg;
    for (int i = 0; i < ITEMS_PER_PRODUCER; ++i) {
        int item = id * 1000 + i;

        // Deadlock or fixed mode locking
        if (program_mode == RUN_MODE_DEADLOCK || program_mode == RUN_MODE_FIXED) {
            if (program_mode == RUN_MODE_DEADLOCK) {
                if (id % 2 == 0) {
                    pthread_mutex_lock(&mutex_left);
                    usleep(1000);
                    pthread_mutex_lock(&mutex_right);
                } else {
                    pthread_mutex_lock(&mutex_right);
                    usleep(1000);
                    pthread_mutex_lock(&mutex_left);
                }
            } else { // fixed order
                pthread_mutex_lock(&mutex_left);
                usleep(1000);
                pthread_mutex_lock(&mutex_right);
            }
        }

        pthread_mutex_lock(&buffer_mutex);
        while (buffer.count == BUFFER_SIZE) {
            pthread_cond_wait(&not_full, &buffer_mutex);
        }
        buffer_put(item);
        operations_done++;  // Track progress
        printf("[Producer %d] produced item %d -> buffer now has %d item(s)\n", id, item, buffer.count);

        pthread_cond_signal(&not_empty);
        pthread_mutex_unlock(&buffer_mutex);

        if (program_mode == RUN_MODE_DEADLOCK || program_mode == RUN_MODE_FIXED) {
            pthread_mutex_unlock(&mutex_right);
            pthread_mutex_unlock(&mutex_left);
        }

        usleep(10000 + (rand() % 20000));
    }

    pthread_mutex_lock(&buffer_mutex);
    producers_done++;
    pthread_cond_broadcast(&not_empty);
    pthread_mutex_unlock(&buffer_mutex);

    return NULL;
}

void *consumer_thread(void *arg)
{
    int id = (int)(intptr_t)arg;
    while (1) {
        pthread_mutex_lock(&buffer_mutex);
        while (buffer.count == 0 && producers_done < NUM_PRODUCERS) {
            pthread_cond_wait(&not_empty, &buffer_mutex);
        }

        if (buffer.count == 0 && producers_done >= NUM_PRODUCERS) {
            pthread_mutex_unlock(&buffer_mutex);
            break;
        }

        int item = buffer_get();
        operations_done++;  // Track progress
        printf("[Consumer %d] consumed item %d -> buffer now has %d item(s)\n", id, item, buffer.count);

        pthread_cond_signal(&not_full);
        pthread_mutex_unlock(&buffer_mutex);

        usleep(15000 + (rand() % 25000));
    }
    return NULL;
}

// Monitor thread function
void *monitor_thread(void *arg)
{
    int last_count = 0;
    int idle_checks = 0;

    while (1) {
        sleep(3);  // Check every 3 seconds

        pthread_mutex_lock(&buffer_mutex);
        int current_count = operations_done;
        int producers_finished = (producers_done >= NUM_PRODUCERS);
        pthread_mutex_unlock(&buffer_mutex);

        if (current_count > last_count) {
            printf("[Monitor] System healthy: progress observed.\n");
            last_count = current_count;
            idle_checks = 0;
        } else {
            idle_checks++;
            if (idle_checks >= 2) {  // 2 consecutive checks = 6 seconds idle
                printf("[Monitor] Warning: no activity detected for 6 seconds. Possible stall.\n");
                idle_checks = 0;
            }
        }

        if (producers_finished && buffer.count == 0) {
            break;  // System finished
        }
    }
    return NULL;
}

static void usage(const char *prog)
{
    fprintf(stderr, "Usage: %s [--partA | --deadlock | --fixed]\n", prog);
    exit(EXIT_FAILURE);
}

int main(int argc, char **argv)
{
    if (argc != 2) usage(argv[0]);

    if (strcmp(argv[1], "--partA") == 0 || strcmp(argv[1], "A") == 0) {
        program_mode = RUN_MODE_A;
    } else if (strcmp(argv[1], "--deadlock") == 0 || strcmp(argv[1], "D") == 0) {
        program_mode = RUN_MODE_DEADLOCK;
    } else if (strcmp(argv[1], "--fixed") == 0 || strcmp(argv[1], "F") == 0) {
        program_mode = RUN_MODE_FIXED;
    } else {
        usage(argv[0]);
    }

    srand((unsigned)time(NULL) ^ (unsigned)getpid());
    buffer.head = buffer.tail = buffer.count = 0;

    pthread_t producers[NUM_PRODUCERS];
    pthread_t consumers[NUM_CONSUMERS];
    pthread_t monitor;

    // Create consumers
    for (int i = 0; i < NUM_CONSUMERS; ++i) {
        int rc = pthread_create(&consumers[i], NULL, consumer_thread, (void *)(intptr_t)(i+1));
        if (rc != 0) {
            fprintf(stderr, "Error creating consumer %d: %s\n", i+1, strerror(rc));
            exit(EXIT_FAILURE);
        }
    }

    // Create producers
    for (int i = 0; i < NUM_PRODUCERS; ++i) {
        int rc = pthread_create(&producers[i], NULL, producer_thread, (void *)(intptr_t)(i+1));
        if (rc != 0) {
            fprintf(stderr, "Error creating producer %d: %s\n", i+1, strerror(rc));
            exit(EXIT_FAILURE);
        }
    }

    // Create monitor thread
    int rc = pthread_create(&monitor, NULL, monitor_thread, NULL);
    if (rc != 0) {
        fprintf(stderr, "Error creating monitor thread: %s\n", strerror(rc));
        exit(EXIT_FAILURE);
    }

    // Join producers
    for (int i = 0; i < NUM_PRODUCERS; ++i) {
        pthread_join(producers[i], NULL);
    }

    // Join consumers
    for (int i = 0; i < NUM_CONSUMERS; ++i) {
        pthread_join(consumers[i], NULL);
    }

    // Join monitor
    pthread_join(monitor, NULL);

    printf("All producers and consumers have finished. Final buffer count = %d\n", buffer.count);
    return 0;
}
