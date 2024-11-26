#  Find the unique odd starting values that lead to a
#  maximum of 9232

from sympy import isprime
import numpy as np
from collatz import *

def factor2(n):
    k = 0
    while True:
        n = n // 2
        k += 1
        if (n%2) == 1:
            return k,n

s = []
r = []
for i in range(1,1001):
    if (i%2) == 0:
        k,v = factor2(i)
        f = collatz(v)
    else:
        f = collatz(i)
        v = i
    s.append(max(f))
    r.append(v)
s = np.array(s)
r = np.array(r)

b = np.zeros(max(s)+1, dtype="uint16")
for t in s:
    b[t] += 1

idx = np.where(b!=0)[0]
v = b[idx]
k = idx.copy()
i = np.argsort(v)[::-1]
v = v[i]
k = k[i]

for i in range(len(v)):
    if (v[i] > 9):
        print("%7d  %d" % (k[i],v[i]))

i = np.where(s==9232)[0]
z = np.unique(r[i])  # all unique, reduced n w/max 9232
z.sort()
print()
print("%d unique reduced values w/9232 as maximum" % len(z))
print()
print(z)
np.save("collatz_unique_9232.npy", z)

prime = [isprime(i) for i in z]
nprime = len(np.where(prime)[0])
print()
print("%d prime out of %d = %0.5f" % (nprime, len(z), nprime/len(z)))
print()

