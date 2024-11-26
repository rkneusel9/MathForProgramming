#include <stdio.h>

void move(int n, int src, int dst, int spare) {
    if (n == 0)
        printf("move %d from %d to %d\n", n, src, dst);
    else {
        move(n-1, src, spare, dst);
        printf("move %d from %d to %d\n", n, src, dst);
        move(n-1, spare, dst, src);
    }
}

int main() {
    //  move *4* disks from peg 1 to peg 3
    move(3,1,3,2);
    return 0;
}

