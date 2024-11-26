#include <stdio.h>
#include <inttypes.h>
#include <math.h>

int main() {
    double y;
    y = log(-4.3);
    printf("log(-4.3) = %0.8f\n", y);
    y = exp(1000);
    printf("exp(1000)= %0.8f\n", y);
    return 0;
}

