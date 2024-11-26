#
#  file: combinatorics.py
#
#  Python combinatorics functions
#
#  RTK, 28-Feb-2023
#  Last update:  04-Jun-2023
#
################################################################

import random

def Factorial(n):
    """Recursive factorial"""
    if (n < 2):
        return 1
    else:
        return n * Factorial(n-1)


def Fact(n):
    """Iterative factorial"""
    fact = 1
    while (n>0):
        fact *= n
        n -= 1
    return fact


def PowerSet(A):
    """Return the power set of a list"""
    def zbin(v,n):
        return format(v,'b').zfill(n)

    pset = [[]]
    n = len(A)
    for k in range(1,2**len(A)):
        s = zbin(k,n)
        p = []
        for i,c in enumerate(s):
            if (c=="1"):
                p.append(A[i])
        pset.append(p)
    return pset


def nPr(n,r):
    """Return the number of permutations of n things taken r at a time"""
    return Fact(n) // Fact(n-r)

def P(n,r):
    """Use a reduction to find P(n,r)"""
    from functools import reduce
    return reduce(lambda x,y: x*y, range(n,n-r,-1))

def nCr(n,r):
    """Return the number of combinations of n things taken r at a time"""
    return nPr(n,r) // Fact(r)


def Combinations(A,m):
    """Return all combinations of the elements of A taken m at a time"""
    comb = []
    n = len(A)
    f = lambda a,b: format(a,'b').zfill(b)
    for k in range(2**len(A)):
        s = f(k,n)
        if (m == len([i for i in s if i=='1'])):
            p = []
            for i,c in enumerate(s):
                if (c=="1"):
                    p.append(A[i])
            comb.append(p)
    return comb


def Permutations(A):
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


def Perms(A,m):
    """Return all permutations of A taken m elements at a time"""

    perm = []
    n = len(A)
    for k in range(2**len(A)):
        s = (lambda a,b: format(a,'b').zfill(b))(k,n)
        if (m == len([i for i in s if i=='1'])):
            p = []
            for i,c in enumerate(s):
                if (c=="1"):
                    p.append(A[i])
            for t in Permutations(p):
                perm.append(t)
    return perm


def Pigeon0(n):
    """Select n+1 random natural numbers, return any whose difference is divisible by n"""
    ans = []
    m = [random.randint(1,99) for i in range(n+1)]
    for i in range(len(m)):
        for j in range(len(m)):
            if ((m[i]-m[j]) % n == 0) and (m[i] > m[j]):
                ans.append((m[i],m[j]))
    return ans


def Pigeon1():
    """Select 10 random natural numbers and return a consecutive set that sum to a multiple of ten"""
    m = [random.randint(1,99) for i in range(10)]
    s = [sum(m[:i]) for i in range(1,11)]
    for i in range(9):
        for j in range(i+1,10):
            if ((s[j] - s[i]) % 10 == 0):
                t = m[(i+1):(j+1)]
                return s[j], s[i], j, i, sum(t), t


def ProbPigeon(m=10, n=5):
    """Probabilistic pigeonhole principle"""
    return 1.0 - Fact(m) / (Fact(m-n)*m**n)


def ProbPigeonSim(trials, m=10, n=5):
    """Simulate the probabilistic pigeonhole principle placing n items in m boxes"""
    count = 0
    for t in range(trials):
        boxes = [0]*m
        for k in range(n):
            boxes[random.randint(0,m-1)] += 1
        if (max(boxes) > 1):
            count += 1
    return count / trials


# end combinatorics.py

