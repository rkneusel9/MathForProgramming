#include <stdio.h>

int binary(int *A, int n, int v) {
    int mid, lo=0, hi=n-1;

    while (lo <= hi) {
        printf("%d %d %d\n",A[lo],v,A[hi]);
        mid = (lo + hi) / 2;
        if (A[mid] == v)
            return mid;
        else
            if (A[mid] < v)
                lo = mid + 1;
            else
                hi = mid - 1;
    }
}


int main() {
    int A[] = {0,2,4,5,6,8,11,12,13,17,22,23,25,34,38,42,66,72,88,99};
    int v = 8;

    printf("A[%d]=%d\n", binary(A,20,v),v);
    return 0;
}

