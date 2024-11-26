#include <stdio.h>
#include <inttypes.h>

uint64_t x = 1;

uint64_t minstd() {
    x = (48271*x) % 2147483647;
    return x;
}

float minstdf() {
    return minstd() / 2147483647.0;
}


int main() {
    FILE *f;
    uint8_t b;
    f = fopen("minstd.bin","wb");
    for(int i=0; i<10000000; i++) {
        b = (uint8_t)(minstd() & 0xff);
        fwrite((void*)&b, sizeof(uint8_t), 1, f);
    }
    fclose(f);
    return 0;
}

