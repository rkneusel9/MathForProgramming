#  Matrix multiplication using lists of lists
def matmul(A,B):
    I, K = len(A), len(A[0])
    J = len(B[0])
    C = [[0]*J for i in range(I)]
    for i in range(I):
        for j in range(J):
            for k in range(K):
                C[i][j] += A[i][k]*B[k][j]
    return C

