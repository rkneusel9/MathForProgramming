def Bubble(A, display=False):
    """Bubble sort in place"""

    for i in range(len(A)-1):
        for j in range(i+1,len(A)):
            if (A[i] > A[j]):
                A[i], A[j] = A[j], A[i]
        if (display):
            print(A)

if (__name__ == "__main__"):
    A = ['Moe','Larry','Shemp','Curly']
    Bubble(A, display=True)

