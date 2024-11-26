#
#  file:  minmax.py
#
#  Plot a function, its derivative, and highlight the zeros of
#  the derivative as corresponding to the minima and maxima
#  of the function
#
#  RTK, 02-Nov-2023
#  Last update: 02-Nov-2023
#
################################################################

import numpy as np
import matplotlib.pylab as plt

def f(x):
    return x**2*np.exp(-x**2)

def df(x):
    return 2*x*np.exp(-x**2)*(1-x**2)

lo,hi,n = -3,3,300
x = np.linspace(lo,hi,n)
plt.plot(x,f(x), color='k', linestyle='solid')
plt.plot(x,df(x), color='k', linestyle='dashed')
plt.plot([lo,hi],[0,0], color='k', linestyle='solid', linewidth=0.5)
plt.plot([0,0], [min(df(x)),max(df(x))], color='k', linewidth=0.5)
plt.plot([-1,-1],[0,f(-1)], color='k', linewidth=0.5)
plt.plot([+1,+1],[0,f(-1)], color='k', linewidth=0.5)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("minmax.eps", dpi=300)
plt.show()

