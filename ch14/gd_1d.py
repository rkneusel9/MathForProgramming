#
#  file:  gd_1d.py
#
#  1D example of GD
#
#  RTK, 14-Feb-2021
#  Last update:  08-Nov-2023
#
################################################################

import sys
import os
import numpy as np
import matplotlib.pylab as plt

def f(x):
    return 6*x**2 - 12*x + 3

def deriv(f,x, h=1e-5):
    return (f(x+h) - f(x-h)) / (2*h)

#  Show a series of gradient descent steps
x = np.linspace(-1,3,1000)
plt.plot(x,f(x), color='k')

x = -0.9
eta = 0.03
for i in range(15):
    plt.plot(x, f(x), marker='o', color='k')
    x = x - eta * deriv(f,x)

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("gd_1d_steps.eps", dpi=300)
plt.show()
plt.close()
print("Minimum at (%0.6f, %0.6f)" % (x, f(x)))

#  Show oscillation if step size too large
x = np.linspace(0.75,1.25,1000)
plt.plot(x,f(x), color='k')
x = xold = 0.75
for i in range(14):
    plt.plot([xold,x], [f(xold),f(x)], marker='o', linestyle='dotted', color='k')
    xold = x
    x = x - 0.15 * deriv(f,x)

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("gd_1d_oscillating.eps", dpi=300)
plt.show()

