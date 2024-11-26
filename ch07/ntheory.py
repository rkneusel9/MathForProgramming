#
#  file:  ntheory.py
#
#  A collection of number theory routines
#
#  RTK, 05-Jan-2023
#  Last update:  31-Jan-2023
#
################################################################

import random
from math import floor, exp

def PrimesBrute(n):
    """Use brute force division checks to find primes less than or equal to n"""
    primes = []
    for p in range(2,n+1):
        prime = True
        for d in range(2,p//2+1):
            if (p%d) == 0:
                prime = False
                break
        if (prime):
            primes.append(p)
    return primes

def Primes(n):
    """Use Eratosthenes' sieve, algorithm in Sorenson 1990"""
    s = [True]*(n+1)
    p = 2
    while (p*p <= n):
        for f in range(p, n//p+1):
            s[p*f] = False
        p += 1
        while (not s[p]):
            p += 1
    primes = []
    for i,v in enumerate(s[2:-1]):
        if (v):
            primes.append(i+2)
    return primes

def PrimeFactors(n, only=False):
    """Return the prime factors of n using trial division"""
    p = {}
    t = 2
    while (n > 1):
        if ((n%t) == 0):
            if (t in p):
                p[t] += 1
            else:
                p[t] = 1
            n = n // t
        else:
            t += 1
    w = []
    for k in sorted(list(p.keys())):
        w.append((k,p[k]))
    if (only):
        w = [i[0] for i in w]
    return w

def NaiveTotient(n):
    """A naive implementation of Euler's totient function"""
    count = 0
    for m in range(1,n+1):
        if (GCD(m,n) == 1):
            count += 1
    return count

def Totient(n):
    """Euler's formula for phi(n)"""
    pf = [p[0] for p in PrimeFactors(n)]
    tot = n
    for p in pf:
        tot *= (1 - 1/p)
    return int(tot)

def isHarshad(n):
    """Is n a harshad number?"""
    v = sum([int(d) for d in str(n)])
    return (n%v) == 0

def Harshad(N):
    """Return harshad numbers <= N"""
    return [n for n in range(1, N+1) if isHarshad(n)]

def Divisors(n):
    """Return the divisors of n"""
    d = []
    for i in range(1,n//2+1):
        if ((n%i) == 0):
            d.append(i)
    d.append(n)
    return d

def Sigma(n, e=1):
    """Return sigma(n) == sigma_1(n)"""
    return sum([i**e for i in Divisors(n)])

def isPrime(n):
    """True if n is a prime"""
    pf = PrimeFactors(n)
    return (len(pf) == 1) and (pf[0][1] == 1)

def isComposite(n):
    """True if n is a composite number"""
    return not isPrime(n)

def isTwinPrime(a,b):
    """True if a and b are twin primes"""
    return isPrime(a) and isPrime(b) and (abs(a-b) == 2)

def isSemiprime(n):
    """True if n is a semiprime"""
    pf = PrimeFactors(n)
    if (len(pf) > 2):
        return False
    if (len(pf) == 1):
        return True if (pf[0][1] == 2) else False
    if (pf[0][1]==1) and (pf[1][1]==1):
        return True
    return False

def AliquotSum(n):
    """Aliquot sum of n"""
    return Sigma(n)-n

def AliquotSequence(n, m=50):
    """Aliquot sequence up to m terms"""
    seq = [n]
    while (len(seq) <= 100):
        if (seq[-1] == 0):  # or (Perfect(seq[-1])
            break
        seq.append(AliquotSum(seq[-1]))
    return seq

def isPerfect(n):
    """True if n is a perfect number"""
    return AliquotSum(n) == n

def GCD(a,b):
    """Return the greatest common divisor of a and b"""
    while (b):
        a,b = b,a%b
    return abs(a)

def GCD2(a,b):
    """Euclid's algorithm using differences, positive a,b only"""
    while (a != b):
        if (a>b):
            a -= b
        else:
            b -= a
    return a

def ExtendedGCD(a,b):
    """the extended Euclidean algorithm, positive a,b only"""
    r0,r1 = a,b
    s0,s1 = 1,0
    t0,t1 = 0,1
    while (r1 != 0):
        r = r0 - (r0//r1)*r1
        s = s0 - (r0//r1)*s1
        t = t0 - (r0//r1)*t1
        r0,r1 = r1,r
        s0,s1 = s1,s
        t0,t1 = t1,t
    return r0,s0,t0

def LCM(a,b):
    """Return the least common multiple of a and b"""
    return a*b//GCD(a,b)

def Coprime(a,b):
    """Are a and b coprime?"""
    return GCD(a,b) == 1

def MillerRabin(n, rounds=5):
    """Implementation of Miller-Rabin based on Wikipedia pseudocode"""
    #  Sanity checks
    if (n==2):
        return True
    if (n%2 == 0):
        return False

    #  Write n = d*2**s + 1 by incrementing s and dividing d=n by 2 until d is odd
    s = 0
    d = n-1
    while (d%2 == 0):
        s += 1
        d //= 2

    for k in range(rounds):
        a = int(random.randint(1,n-1))  # failure: n=65, a=8|18|47|57|64 (nonwitness numbers for 65)
        x = pow(a,d,n)  #(a**d) % n
        if (x==1) or (x == n-1):
            continue
        b = False
        for j in range(s-1):
            x = pow(x,2,n)  #x**2 % n
            if (x == n-1):
                b = True
                break
        if (b):
            continue
        return False
    return True

def Cows(n):
    """Return the first n Narayana's cows numbers"""
    cows = [1,1,1]
    if (n > 0) and (n < 4):
        return cows[:n]
    while (len(cows) < n):
        cows.append(cows[-1] + cows[-3])
    return cows

def isRuthAaron(n):
    """Is the sum of the prime factors of n equal to those of n+1?"""
    return sum(PrimeFactors(n,only=True)) == sum(PrimeFactors(n+1,only=True))

def HighlyComposite(n):
    """Return a list of highly composite numbers up to n"""
    if (n < 2):
        return [1]
    dv = [len(Divisors(i)) for i in range(1,n+1)]
    hc = [1]
    for k in range(1,len(dv)):
        if (dv[k] > max(dv[:k])):
            hc.append(k+1)
    return hc

def Factorial(n):
    """Iterative factorial"""
    if (n < 2):
        return 1
    f = 1
    while (n > 0):
        n,f = n-1, f*n
    return f

from decimal import *
def Subfactorial(n):
    """Return !n, the number of derangements"""
    getcontext().prec = 1000
    return int((Decimal(Factorial(n)) / Decimal(1).exp()).to_integral_exact())

def Goldbach(n):
    """Return all the unique ways to write n as the sum of two primes"""
    primes = Primes(n)
    ans = []
    for p in primes:
        for q in primes:
            if (p < q):
                continue
            if ((p+q) == n):
                ans.append((p,q))
    return ans

def NaiveModularInverse(a,n):
    """Naive search for the inverse of a mod n"""
    if (GCD(a,n) != 1):
        return None
    for i in range(0,n-1):
        if ((a*i) % n) == 1:
            return i

def ModularInverse(a,n):
    """Use the extended Euclidean algorithm to find the inverse of a"""
    g,s,t = ExtendedGCD(a,n)
    return None if (g!=1) else s

# end ntheory.py

