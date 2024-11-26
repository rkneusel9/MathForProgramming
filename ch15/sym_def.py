#
#  file:  sym_def.py
#
#  Definite integrals using SymPy
#
#  RTK, 12-Nov-2023
#  Last update:  12-Nov-2023
#
################################################################

import sys
from sympy import symbols, integrate
from sympy import sqrt,sin,cos,tan,log,exp

if (len(sys.argv) == 1):
    print()
    print("sym_def <expr> <a> <b>")
    print()
    print("  <expr>   - expression to integrate")
    print("  <a>, <b> - limits")
    print()
    exit(0)

expr = sys.argv[1]
a,b = float(sys.argv[2]), float(sys.argv[3])

x = symbols('x')
f = eval(expr)

anti = integrate(f,x)
defi = anti.subs(x,b) - anti.subs(x,a)
area = defi.evalf()

print("Area under the curve = %0.8f" % area)

