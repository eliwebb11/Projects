#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define NUM_THREADS 5

int global_var = 0;       // Global variable
static int static_var = 0; // Static variable

// Structure to pass multiple variables to the thread
typedef struct {
    int local_var;
    int *dynamic_var;
} thread_data_t;

void *thread_func(void *arg) {
    thread_data_t *data = (thread_data_t *)arg;

    int local_var = data->local_var;
    int *dynamic_var = data->dynamic_var;

    for (int i = 0; i < 100000; ++i) {
        local_var++;        // Increment local copy
        global_var++;       // Increment global variable
        static_var++;       // Increment static variable
        (*dynamic_var)++;   // Increment dynamic variable
    }

    printf("Thread finished: global=%d, static=%d, local=%d, dynamic=%d\n", global_var, static_var, local_var, *dynamic_var);

    free(dynamic_var); // Free the dynamically allocated variable
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[NUM_THREADS];

    int local_var = 42;

    for (int i = 0; i < NUM_THREADS; ++i) {
        thread_data_t *data = (thread_data_t *)malloc(sizeof(thread_data_t));
        data->local_var = local_var;
        data->dynamic_var = (int *)malloc(sizeof(int));
        *(data->dynamic_var) = 0;

        int rc = pthread_create(&threads[i], NULL, thread_func, (void *)data);
        if (rc != 0) {
            printf("Error: pthread_create() failed\n");
            free(data->dynamic_var);
            free(data);
            return 1;
        }
    }

    // Join all threads
    for (int i = 0; i < NUM_THREADS; ++i) {
        int rc = pthread_join(threads[i], NULL);
        if (rc != 0) {
            printf("Error: pthread_join() failed\n");
            return 1;
        }
    }

    printf("Main thread finished: global=%d static=%d local=%d\n", global_var, static_var, local_var);
 
    return 0;
}
