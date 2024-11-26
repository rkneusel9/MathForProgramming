#  A brief symbolic differentiation example

import numpy as np
import matplotlib.pylab as plt
from sympy import symbols, diff, lambdify, sin, exp

#  'x' is a symbol
x = symbols('x')

#  f(x)
f = 2*sin(3*x) + 20*exp(-0.5*((x - 8)**2)/0.6)

#  f'(x)
fp = diff(f,x)
print(fp)

#  Make the SymPy expressions into NumPy functions
f_numpy = lambdify(x, f, modules=['numpy'])
fp_numpy = lambdify(x, fp, modules=['numpy'])

#  NumPy f(x) and f'(x)
xv = np.linspace(0, 10, 200)
y = f_numpy(xv)
yp = fp_numpy(xv)

import pdb; pdb.set_trace()

#  Plot
plt.plot(xv,y, color='k', label='f(x)')
plt.plot(xv,yp, color='k', linestyle='dashed', label="f'(x)")
plt.legend(loc='upper right')
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.show()

