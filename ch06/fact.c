#include <stdio.h>
#include <inttypes.h>

uint64_t fact(uint64_t n) {
    if (n < 2)
        return 1;
    else
        return n * fact(n-1);
}

int main() {
    for(int n=0; n<21; n++)
        printf("%2d! = %" PRIu64 "\n", n, fact(n));
    return 0;
}

