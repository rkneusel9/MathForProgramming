from fibonacci import *
import numpy as np
import time
import sys

f0 = []
f1 = []
ff = []

N = 20
M = int(sys.argv[1])

for i in range(N):
    s = time.time(); _ = fib0(M); f0.append(time.time()-s)
    s = time.time(); _ = fib1(M); f1.append(time.time()-s)
    s = time.time(); _ = fib(M);  ff.append(time.time()-s)

f0 = np.array(f0)
f1 = np.array(f1)
ff = np.array(ff)

print()
print("Time to calculate F_%d (%d reps)" % (M,N))
print()
print("fib0: %0.10f +/- %0.10f" % (f0.mean(), f0.std(ddof=1)/np.sqrt(N)))
print("fib1: %0.10f +/- %0.10f" % (f1.mean(), f1.std(ddof=1)/np.sqrt(N)))
print("fib : %0.10f +/- %0.10f" % (ff.mean(), ff.std(ddof=1)/np.sqrt(N)))
print()
print("fib0 is %0.3f times faster than fib1" % (f1.mean()/f0.mean(),))
print("fib0 is %0.3f times faster than fib" % (ff.mean()/f0.mean(),))
print()

