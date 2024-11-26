//  0.1 is a repeating binary "decimal"
#include <stdio.h>

int main() {
    float s = 0.0;

    for(int i=0; i < 100; i++)
        s += 0.1;

    printf("%0.16f\n", s);
    return 0;
}

