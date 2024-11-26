#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int i=1,r=0,s=atoi(argv[1]);
    while (s>0) s-=i,i+=2,r++;
    printf("%d\n", r); return0; }

