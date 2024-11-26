#
#  file:  simp.py
#
#  Numeric integration via Simpson's rule
#
#  RTK, 12-Nov-2023
#  Last update:  12-Nov-2023
#
################################################################

import sys
from math import sqrt,sin,cos,tan,log,exp

if (len(sys.argv) == 1):
    print()
    print("simp <expr> <a> <b> <n>")
    print()
    print("  <expr>   - expression to integrate")
    print("  <a>, <b> - limits")
    print("  <n>      - number of trapezoids")
    print()
    exit(0)

expr = sys.argv[1]
a,b = float(sys.argv[2]), float(sys.argv[3])
n = int(sys.argv[4])

#  n must be even
if (n % 2):
    n += 1

h = (b-a)/n  # bin width

#  f(a) + f(b)
x = a
area = eval(expr)
x = b
area += eval(expr)

for i in range(1,n):
    x = a + i*h
    if (i % 2):
        area += 4*eval(expr)
    else:
        area += 2*eval(expr)

area *= h/3

print("Area under the curve = %0.8f" % area)

