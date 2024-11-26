// Example Boolean functions
#include <stdio.h>
#include <inttypes.h>

uint8_t f(uint8_t x, uint8_t y) {
    return !x && (x || !y);
}

uint8_t fd(uint8_t x, uint8_t y) {
    return !x || (x && !y);
}

uint8_t fc(uint8_t x, uint8_t y) {
    return x || (!x && y);
}

uint8_t g(uint8_t a, uint8_t b, uint8_t c) {
    return (a || b&&!c) && (a&&b || !b&&c);
}

int main() {
    uint8_t x,y,a,b,c;
    
    printf("x y f\n-----\n");
    for(x=0; x<2; x++)
        for(y=0; y<2; y++)
            printf("%d %d %d\n", x, y, f(x,y));
    printf("\n");

    printf("x y fd\n-----\n");
    for(x=0; x<2; x++)
        for(y=0; y<2; y++)
            printf("%d %d %d\n", x, y, fd(x,y));
    printf("\n");

    printf("x y fc\n-----\n");
    for(x=0; x<2; x++)
        for(y=0; y<2; y++)
            printf("%d %d %d\n", x, y, fc(x,y));
    printf("\n");

    printf("a b c g\n-------\n");
    for(a=0; a<2; a++)
        for(b=0; b<2; b++)
            for(c=0; c<2; c++)
                printf("%d %d %d %d\n", a,b,c, g(a,b,c));
    printf("\n");

    return 0;
}

