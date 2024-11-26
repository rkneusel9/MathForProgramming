#
#  file:  darts.py
#
#  Random darts approach to finding the area under a curve
#
#  RTK, 11-Nov-2023
#  Last update:  15-Nov-2023
#
################################################################

import sys
import numpy as np
from math import sqrt,sin,cos,tan,log,exp

if (len(sys.argv) == 1):
    print("darts <expr> <a> <b> <n>")
    print()
    print("  <expr>  - the curve")
    print("  <a>,<b> - limits in x")
    print("  <n>     - number of darts")
    print()
    exit(0)

expr = sys.argv[1]
a,b = float(sys.argv[2]), float(sys.argv[3])
n = int(sys.argv[4])

c, ymax, m = 0, -1, 1000

for i in range(m):
    x = a + i*(b-a)/m
    y = eval(expr)
    if (y > ymax):
        ymax = y

for i in range(n):
    x = a + (b-a)*np.random.random()
    y = ymax*np.random.random()
    f = eval(expr)
    if (y < f):
        c += 1

area = (c/n)*(b-a)*ymax
print("Area under the curve = %0.8f" % area)

