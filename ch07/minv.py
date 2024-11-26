#  modular multiplicative inverse -- from Wikipedia article "Extended Euclidean algorithm"

def naive(a,n):
    """Naive search for the inverse of a mod n"""
    for i in range(0,n-1):
        if ((a*i) % n) == 1:
            return i
    return None

def minv(a,n):
    """Return the multiplicative inverse of a mod n or None"""
    t,r,newt,newr = 0,n,1,a

    while (newr != 0):
        quotient = r // newr
        t,newt = newt, t-quotient*newt
        r,newr = newr, r-quotient*newr

    if (r > 1):
        return None  # no inverse
    if (t < 0):
        t += n
    return t

def inv(a,n):
    """Recursive inverse"""
    return a if (a<=1) else n - (n//a)*inv(n%a,n) % n

