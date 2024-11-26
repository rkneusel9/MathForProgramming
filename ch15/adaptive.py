#
#  file:  adaptive.py
#
#  Numeric integration via adaptive Simpson's rule
#
#  E.g.,
#   python3 adaptive.py 'x**2*sin(3*x-4)*exp(-x**2)+cos(sin(3*x**3))' 0 6
#   (function too complex for SymPy)
#
#  RTK, 15-Nov-2023
#  Last update:  15-Nov-2023
#
################################################################

import sys
from math import sqrt,sin,cos,tan,log,exp

def Simpson(f, a, b, n=2):
    """Standard Simpson's rule"""
    if (n % 2):
        n += 1
    h = (b-a)/n
    x = a
    area = eval(f)
    x = b
    area += eval(f)
    for i in range(1,n):
        x = a + i*h
        if (i % 2):
            area += 4*eval(f)
        else:
            area += 2*eval(f)
    return area*(h/3)


def AdaptiveSimpson(f, a, b, epsilon=1e-6, max_depth=100, depth=0):
    """Adaptive Simpson's rule that recurses on subdivisions"""
    m = (a + b) / 2
    s_ab = Simpson(f, a, b)  #  whole interval
    s_am = Simpson(f, a, m)  #  first half
    s_mb = Simpson(f, m, b)  #  second half

    #  The difference is below the threshold, return
    if (abs(s_ab - (s_am + s_mb)) < epsilon):
        return s_am + s_mb

    #  Max recursion depth is reached, return the current approximation
    if (depth >= max_depth):
        return s_am + s_mb

    #  Apply Simpson's rule recursively to each half of the interval
    left = AdaptiveSimpson(f, a, m, epsilon=epsilon, depth=depth+1)
    right = AdaptiveSimpson(f, m, b, epsilon=epsilon, depth=depth+1)
    return left + right


if (len(sys.argv) == 1):
    print()
    print("adaptive <expr> <a> <b>")
    print()
    print("  <expr>   - expression to integrate")
    print("  <a>, <b> - limits")
    print()
    exit(0)

expr = sys.argv[1]
a,b = float(sys.argv[2]), float(sys.argv[3])

print("Area under the curve = %0.8f" % AdaptiveSimpson(expr,a,b, epsilon=1e-10))

