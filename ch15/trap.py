#
#  file:  trap.py
#
#  Numeric integration via the trapezoidal rule.
#
#  RTK, 12-Nov-2023
#  Last update:  12-Nov-2023
#
################################################################

import sys
from math import sqrt,sin,cos,tan,log,exp

if (len(sys.argv) == 1):
    print()
    print("trap <expr> <a> <b> <n>")
    print()
    print("  <expr>   - expression to integrate")
    print("  <a>, <b> - limits")
    print("  <n>      - number of trapezoids")
    print()
    exit(0)

expr = sys.argv[1]
a,b = float(sys.argv[2]), float(sys.argv[3])
n = int(sys.argv[4])

h = (b-a)/n  # trapezoid width
area = 0.0   # area under the curve

for i in range(n):
    x = a + i*h
    e0 = eval(expr)
    x = a + (i+1)*h
    e1 = eval(expr)
    area += 0.5*(e0 + e1) * h

print("Area under the curve = %0.8f" % area)

