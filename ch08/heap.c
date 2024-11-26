// Permutation generation

#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>

uint8_t *A;
uint64_t count = 0;
int n;

void pp(uint8_t *A) {
    count++;
    return;
    //for(int i=0; i<n; i++)
    //    printf("%d ", A[i]);
    //printf("\n");
}

void heap(int k, uint8_t *A) {
    uint8_t t;
    if (k==1) {
        pp(A);
    } else {
        heap(k-1,A);
        for(int i=0; i<k-1; i++) {
            if (k%2 == 0) {
                t=A[i]; A[i]=A[k-1]; A[k-1]=t;
            } else {
                t=A[0]; A[0]=A[k-1]; A[k-1]=t;
            }
            heap(k-1,A);
        }
    }
}

int main(int argc, char *argv[]) {
    n = atoi(argv[1]);
    A = (uint8_t *)malloc(n*sizeof(uint8_t));
    for(int i=1; i<=n; i++)
        A[i] = i+1;
    heap(n,A);
    printf("%" PRIu64 "\n", count);
    return 0;
}

