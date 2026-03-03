#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/wait.h>

int global_var = 0;
static __thread int static_var = 0;   // Thread local static variable

void* thread_function(void* arg) {
    int local_var = 0;
    int* dynamic_var = (int*)calloc(1, sizeof(int));

    local_var++;
    (*dynamic_var)++;
    global_var++;
    static_var++;

    pid_t pid;
    int i;
    for (i = 0; i < 3; i++) {
        pid = fork();
        if (pid == 0) {
            local_var++;
            (*dynamic_var)++;
            global_var++;
            static_var++;
            printf("Child PID=%d final values: global=%d static=%d local=%d dynamic=%d\n", getpid(), global_var, static_var, local_var, *dynamic_var);
            free(dynamic_var);
            exit(0);
        }
    }

    for (i = 0; i < 3; i++) {
        wait(NULL);
    }

    printf("PID=%d TID=%lu global=%d static=%d local=%d dynamic=%d\n", getpid(), pthread_self(), global_var, static_var, local_var, *dynamic_var);

    free(dynamic_var);
    pthread_exit(NULL);
}

int main() {
    pthread_t threads[3];
    for (int i = 0; i < 3; i++)
        pthread_create(&threads[i], NULL, thread_function, NULL);

    for (int i = 0; i < 3; i++)
        pthread_join(threads[i], NULL);

    printf("Parent PID=%d final values: global=%d static=%d local=%d dynamic=%d\n", getpid(), global_var, static_var,);
    return 0;
}
