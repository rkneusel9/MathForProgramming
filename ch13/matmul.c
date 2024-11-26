// Naive matrix multiplication -- necessary checks ignored to make the code
//                                easier to read.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// index into a 2D array stored in row-major order for element (i,j) (m is column size)
#define IX(i,j,m) ((i)*(m)+(j))

// multiply matrices, n x m times m x p --> n x p output
int *matmul(int *A, int *B, int n, int m, int p) {
    int *C = (int *)malloc(n*p*sizeof(int));
    int i,j,k;
    
    //  zero the output matrix
    memset((void*)C, 0, n*p*sizeof(int));

    //  update each element
    for(i=0; i<n; i++)
        for(j=0; j<p; j++)
            for(k=0; k<m; k++)
                C[IX(i,j,p)] += A[IX(i,k,m)]*B[IX(k,j,p)];

    return C;
}


// print an n x m matrix
void pp(int *A, int n, int m) {
    int i,j;
    for(i=0; i<n; i++) {
        for (j=0; j<m; j++)
            printf("%2d ", A[IX(i,j,m)]);
        printf("\n");
    }
}


int main() {
    int i,j;
    int A[9] = {1,2,3,4,5,6,7,8,9};  // [[1,2,3],[4,5,6],[7,8,9]]
    int B[9] = {1,1,1,2,2,2,3,3,3};  // [[1,1,1],[2,2,2],[3,3,3]]
    int *C = (int *)NULL;

    printf("A*B:\n");
    C = matmul(A,B, 3,3,3);
    pp(C,3,3);
    free(C);

    printf("\nB*A:\n");
    C = matmul(B,A, 3,3,3);
    pp(C,3,3);
    free(C);

    return 0;
}

