#include <stdio.h>

int main() {
    printf("%4d %4d %4d %4d\n", 33,7,33/7,33%7);
    printf("%4d %4d %4d %4d\n", -33,7,-33/7,-33%7);
    printf("%4d %4d %4d %4d\n", 33,-7,33/-7,33%-7);
    printf("%4d %4d %4d %4d\n", -33,-7,-33/-7,-33%-7);
    return 0;
}

