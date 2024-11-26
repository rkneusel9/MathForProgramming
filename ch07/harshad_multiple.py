# MHN chain lengths

import numpy as np
from ntheory import *

N = 100_000_000
w = []

for i in range(1,N+1):
    if isHarshad(i):
        k = 1
        v = sum([int(d) for d in str(i)])
        n = i//v
        last = 0
        if isHarshad(n):
            k = 0
            while isHarshad(n) and (n != last):
                k += 1
                v = sum([int(d) for d in str(n)])
                last = n
                n = n//v
        w.append((i,k))

h = np.array(w)

# frequency
mh = h[:,1].max()
for i in range(1,mh+1):
    t = len(np.where(h[:,1]==i)[0])
    print("% 2d: % 9d" % (i,t))
print()
print(h[np.where(h[:,1]==mh)[0],0])
print()
print("(%d harshad numbers <= %d)" % (h.shape[0],N))
print()


