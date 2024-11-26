#include <stdio.h>
#include <inttypes.h>
#include <time.h>

uint32_t seed;
uint32_t xorshift32(void) {
    seed ^= (seed<<13);
    seed ^= (seed>>17);
    seed ^= (seed<< 5);
    return seed;
}

double xorshift(void) {
    return xorshift32() / (double)0xFFFFFFFF;
}


int main(int argc, char *argv[]) {
    int i,c=0, n=1000000;
    double r;

    // seed xorshift
    seed = (uint32_t)time(NULL);

    // simulate
    for(i=0; i < n; i++) {
        r = xorshift();
        if (r < 0.75) {
            if (xorshift() < 0.02) c++;
        } else {
            if (r < 0.98) {
                if (xorshift() < 0.03) c++;
            } else {
                if (xorshift() < 0.10) c++;
            }
        }
    }

    printf("probability of priestly class = %0.5f\n", c/(double)n);

    return 0;
}
