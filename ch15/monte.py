#
#  file:  monte.py
#
#  Monte Carlo integration
#
#  RTK, 11-Nov-2023
#  Last update:  11-Nov-2023
#
################################################################

import sys
import numpy as np
from math import sqrt,sin,cos,tan,log,exp

if (len(sys.argv) == 1):
    print()
    print("monte <expr> <a> <b> <n>")
    print()
    print("  <expr> - the expression to integrate from <a> to <b>")
    print("  <n> - number of random samples to use")
    print()
    exit(0)

expr = sys.argv[1]
a,b = float(sys.argv[2]), float(sys.argv[3])
n = int(sys.argv[4])

samples = a + (b-a)*np.random.random(n)
f = np.zeros(n)
for i in range(n):
    x = samples[i]
    f[i] = eval(expr)

area = (b-a)*f.mean()
print("Area under the curve = %0.8f" % area)

