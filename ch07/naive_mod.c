#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    unsigned int a,n,i;

    a = atoi(argv[1]);
    n = atoi(argv[2]);

    for (i=0; i < n-1; i++)
        if (((a*i) % n) == 1) {
            printf("%d\n", i);
            return;
        }
    printf("no inverse\n");
    return 0;
}

