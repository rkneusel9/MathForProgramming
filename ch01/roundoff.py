#
#  file:  roundoff.py
#
#  Demonstrate catastrophic roundoff error
#
#  RTK, 07-Aug-2022
#  Last update: 07-Aug-2022
#
################################################################

import numpy as np
import sys
from fractions import *

if (len(sys.argv) == 1):
    print()
    print("roundoff <n>")
    print()
    print("  <n> - number of times to repeat the sequence (e.g. 5)")
    print()
    exit(0)

N = int(sys.argv[1])

p = Fraction(np.pi)
pi = p
for i in range(N):
    p= p*p*p + 33*p*p + Fraction(1,1)
    p= p - Fraction(1,1)
    p= p - 33*pi**2
    p= p/(pi*pi)
pi = p

p = np.pi
for i in range(N):
    p= p*p*p + 33*p*p + 1
    p= p - 1
    p= p - 33*np.pi**2
    p= p/(np.pi*np.pi)
pf = p

print("pi       : %0.18f" % np.pi)
print("rational : %0.18f" % float(pi))
print("computer : %0.18f" % pf)
print()

