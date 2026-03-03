#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/wait.h>

void *thread_function1(void *arg) {
    printf("Thread 1 created\n");
    /* Thread does something meaningful task..*/
    pid_t pid = fork();
    if (pid == 0) {
        // In child, safely replace process image
        char *argv[] = {"ls", "-l", NULL};
        execvp("ls", argv);
        perror("execvp");
        exit(EXIT_FAILURE);
    } else if (pid > 0) {
        wait(NULL);
    } else {
        perror("fork");
    }
    printf("Thread 1 is done\n");
    pthread_exit(NULL);
}

void *thread_function2(void *arg) {
    printf("Thread 2 created\n");
    /* Thread does something meaningful task..*/
    printf("Thread 2 is done\n");
    pthread_exit(NULL);
}

int main() {
    pid_t pid;
    pthread_t thread1, thread2;

    printf("Main process started\n");

    if (pthread_create(&thread1, NULL, thread_function1, NULL) != 0) {
        perror("pthread_create");
        exit(EXIT_FAILURE);
    }

    if (pthread_create(&thread2, NULL, thread_function2, NULL) != 0) {
        perror("pthread_create");
        exit(EXIT_FAILURE);
    }

    pid = fork();
    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
        printf("Child process executing\n");
        exit(0);
    } else {
        printf("Parent process continuing\n");
        wait(NULL);
    }

    if (pthread_join(thread1, NULL) != 0) {
        perror("pthread_join thread1");
        exit(EXIT_FAILURE);
    }
    if (pthread_join(thread2, NULL) != 0) {
        perror("pthread_join thread2");
        exit(EXIT_FAILURE);
    }

    printf("Main process is done\n");
    return 0;
}
