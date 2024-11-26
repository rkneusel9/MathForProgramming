#
#  file:  sym_indef.py
#
#  Indefinite integrals using SymPy
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
    print("sym_indef <expr>")
    print()
    print("  <expr>   - expression to integrate")
    print()
    exit(0)

expr = sys.argv[1]
x = symbols('x')
f = eval(expr)

anti = integrate(f,x)
print("Indefinite integral is:\n    f(x) =", anti, "+ C")

