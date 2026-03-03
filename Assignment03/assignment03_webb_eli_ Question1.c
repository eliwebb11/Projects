#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/wait.h>

int global_var = 0;

static int static_var = 0;

void* thread_function(void* arg) {
    int local_var = 0;

    int* dynamic_var = (int*)malloc(sizeof(int));
    *dynamic_var = 0;

    local_var++;
    (*dynamic_var)++;
    global_var++;
    static_var++;

    // current state before freeing memory
    printf("PID=%d TID=%lu: global_var=%d static_var=%d local_var=%d *dynamic_var=%d\n", getpid(), pthread_self(), global_var, static_var, local_var, *dynamic_var);

    free(dynamic_var);
    pthread_exit(NULL);
}

int main() {
int i;
pid_t pid;

    for (i = 0; i < 3; i++) {
        pid = fork();
        if (pid == 0) {
            pthread_t threads[3];
            int j;
            for (j = 0; j < 3; j++) {
                pthread_create(&threads[j], NULL, thread_function, NULL);
            }
            for (j = 0; j < 3; j++) {
            pthread_join(threads[j], NULL);
            }

            // final values in the child before exit
            printf("Child PID=%d final values: global_var=%d static_var=%d \n", getpid(), global_var, static_var);

            exit(0);
        }
        else if (pid < 0) {
            fprintf(stderr, "Fork failed\n");
            return 1;
        }
    }
    for (i = 0; i < 3; i++) {
        wait(NULL);
    }
    // parent values at end
    printf("Parent PID=%d final values: global_var=%d, static_var=%d \n", getpid(), global_var, static_var);
    
    return 0;
}