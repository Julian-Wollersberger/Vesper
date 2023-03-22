#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <iostream>

void* Thread(void *vargp) {

    printf("Perkele!\n");
    return NULL;
}

int main() {

    pthread_t id;
    pthread_create(&id, NULL, Thread, NULL);

    pthread_join(id, NULL);

return 0;
}