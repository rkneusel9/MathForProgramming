// Is your system big or little endian?
#include <stdio.h>
#include <inttypes.h>

int main() {
    uint32_t v = 0x11223344;
    uint8_t *p = (uint8_t *)&v;
    
    printf("Your system is ");

    switch (*p) {
        case 0x11:
            printf("big-endian\n");
            break;
        case 0x44:
            printf("little-endian\n");
            break;
        default:
            printf("something else\n");
    }
   
    return 0;
}

