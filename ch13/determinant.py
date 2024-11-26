#  Calculate the determinant recursively using cofactors

def determinant(A):
    """Calculate the determinant recursively"""

    def minor(A,i,j):
        m = A[:i] + A[i+1:]  # remove row i
        for i in range(len(m)):
            m[i] = m[i][:j] + m[i][j+1:]  # and column j
        return m

    #  base case
    if (len(A) == 1) and (len(A[0]) == 1):
        return A[0][0]

    #  recursive case
    det = 0
    for j in range(len(A[0])):  # columns, expand across row 0
        cof = (-1)**j * A[0][j] * determinant(minor(A,0,j))
        det += cof
    return det


