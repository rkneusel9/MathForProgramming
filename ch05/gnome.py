def Gnome(A, display=False):
    """Gnome sort in place"""
    
    p = 0
    while (p < len(A)):
        if (p == 0) or (A[p] >= A[p-1]):
            p += 1
        else:
            A[p], A[p-1] = A[p-1], A[p]
            p -= 1
        if (display):
            print(A, p)

if (__name__ == "__main__"):
    A = ['Moe','Larry','Shemp','Curly']
    Gnome(A, display=True)

