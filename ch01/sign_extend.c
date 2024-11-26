// sign extension
#include <stdio.h>
#include <inttypes.h>

int main() {
    int8_t n = -42;

    printf("as signed 8-bit int : %d\n", n);
    printf("as signed 16-bit int: %d\n", (int16_t)n);
    printf("as unsigned 8-bit hex : %x\n", (uint8_t)n);
    printf("as unsigned 16-bit hex: %x\n", (uint16_t)n);

    return 0;
}

