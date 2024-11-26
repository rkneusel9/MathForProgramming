// The bits of a 32-bit float
#include <stdio.h>
#include <inttypes.h>

int main() {
    float v = 2.718;
    uint32_t *p = (uint32_t *)&v;
    printf("%08x\n", *p);
    printf("%1.8f\n", v);
    return 0;
}

