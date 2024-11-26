# Show that the chain rule does, indeed, produce a function
# that determines the slope of the tangent line at any given point

import sys
import numpy as np
import matplotlib.pylab as plt

if (len(sys.argv) == 1):
    print()
    print("chain <x>")
    print()
    print("plot a curve and the tangent line at <x> where <x> in [0,2]")
    print()
    exit(0)

def h(x):
    return 3*(np.sin(x**3+2*x))**2

def dh(x):
    return 6.0*(3.0*x**2+2.0)*np.sin(x**3+2*x)*np.cos(x**3+2*x)

def PlotTangent(x):
    m = dh(x)
    b = h(x) - m*x
    xx = np.linspace(x-0.3, x+0.3, 10)
    yy = m*xx + b
    plt.plot(xx,yy, color='k', linewidth=0.7)
    plt.plot(x,h(x), marker='o', fillstyle='none', color='k')

t = float(sys.argv[1])
x = np.linspace(0,2,600)
plt.plot(x,h(x), color='k')
PlotTangent(t)
plt.xlim((0,2.05))
plt.ylim((0,3.05))
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.show()
plt.close()

plt.plot(x,dh(x), linestyle='dashed', color='k')
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.show()
plt.close()

