//Author Name: Eli Webb
//Email: eli.webb@okstate.edu
//Date: 9/29/2025
//Program Description: Assignment02. Stuudenet registration system using three processes (frontend, database, logger) and a POSIX message queue.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <mqueue.h>
#include <time.h>

#define QUEUE_NAME "/student_reg_queue"
#define MAX_MSG_SIZE 256

//student info
typedef struct {
    long msg_type;
    char name[50];
    int id;
} Student;

//frontend process
void frontend_process() {
    const char *students[] = {"Alice", "Bob", "Charlie"};
    mqd_t mq = mq_open(QUEUE_NAME, O_WRONLY);
    if (mq == -1) {
        perror("[Frontend] mq_open");
        exit(1);
    }

    for (int i = 0; i < 3; i++) {
        Student s;
        s.msg_type = 1;
        strcpy(s.name, students[i]);
        s.id = -1;  //no id
        printf("[Frontend] @ %lds: Sending %s...\n", time(NULL) % 60, s.name);

        if (mq_send(mq, (char*)&s, sizeof(Student), 0) == -1) {
            perror("[Frontend] mq_send");
            exit(1);
        }
        sleep(1);
    }

    printf("[Frontend] @ %lds: All students submitted! My job is done.\n", time(NULL) % 60);
    mq_close(mq);
}

//database process
void database_process() {
    mqd_t mq = mq_open(QUEUE_NAME, O_RDWR);
    if (mq == -1) {
        perror("[Database] mq_open");
        exit(1);
    }

    int i = 0;
    while (i < 3) {
        Student s;
        if (mq_receive(mq, (char*)&s, sizeof(Student), NULL) == -1) {
            perror("[Database] mq_receive");
            exit(1);
        }
        if (s.msg_type == 1) {
            printf("[Database] @ %lds: Start processing %s...\n", time(NULL) % 60, s.name);
            sleep(3); //simulate slow work
            s.id = 1001 + i;
            s.msg_type = 2;
            printf("[Database] @ %lds: Finished processing %s. Assigned ID: %d\n", time(NULL) % 60, s.name, s.id);

            //send confirmation
            if (mq_send(mq, (char*)&s, sizeof(Student), 0) == -1) {
                perror("[Database] mq_send");
                exit(1);
            }
            i++;
        }
        else {
            if (mq_send(mq, (char*)&s, sizeof(Student), 0) == -1) {
                perror("[Database] mq_send requeue");
                exit(1);
            }
        }
    }
    mq_close(mq);
}

//logger process
void logger_process() {
    mqd_t mq = mq_open(QUEUE_NAME, O_RDWR);
    if (mq == -1) {
        perror("[Logger] mq_open");
        exit(1);
    }

    int i = 0;
    while (i < 3) {
        Student s;
        if (mq_receive(mq, (char*)&s, sizeof(Student), NULL) == -1) {
            perror("[Logger] mq_receive");
            exit(1);
        }

        if (s.msg_type == 2){
            printf("[Logger] @ %lds: CONFIRMED - ID: %d, Name: %s\n", time(NULL) % 60, s.id, s.name);
            i++;
        }
        else {
            if (mq_send(mq, (char*)&s, sizeof(Student), 0) == -1) {
                perror("[Logger] mq_send requeue");
                exit(1);
            }
        }
    }
    mq_close(mq);
}

int main() {
    mq_unlink(QUEUE_NAME);
    struct mq_attr attr;
    attr.mq_flags = 0;
    attr.mq_maxmsg = 10;
    attr.mq_msgsize = sizeof(Student);
    attr.mq_curmsgs = 0;

    //message queue
    mqd_t mq = mq_open(QUEUE_NAME, O_CREAT | O_RDWR, 0644, &attr);
    if (mq == -1) {
        perror("[Parent] mq_open");
        exit(1);
    }
    mq_close(mq);

    pid_t frontend_pid = fork();
    if (frontend_pid == 0) {
        frontend_process();
        exit(0);
    }

    pid_t database_pid = fork();
    if (database_pid == 0) {
        database_process();
        exit(0);
    }

    pid_t logger_pid = fork();
    if (logger_pid == 0) {
        logger_process();
        exit(0);
    }

    //parent wait for children
    wait(NULL);
    wait(NULL);
    wait(NULL);

    //clean up
    mq_unlink(QUEUE_NAME);
    printf("[Parent] All processes finished. Queue destroyed.\n");
    return 0;
}