# Permutation generation

def Heap(A):
    """Return a list of the permutations of the elements of A"""
    
    def heap(k,A):
        if (k==1):
            perms.append(A[:])
        else:
            heap(k-1,A)
            for i in range(k-1):
                if (k%2 == 0):
                    A[i], A[k-1] = A[k-1], A[i]
                else:
                    A[0], A[k-1] = A[k-1], A[0]
                heap(k-1,A)

    perms = []
    heap(len(A),A)
    return perms

