#  A simple numeric differentiation example

import numpy as np
import matplotlib.pylab as plt

def f(x):
    return x**2 + np.sin(3*x)

def deriv(f,x, h=1e-4):
    return (f(x+h) - f(x)) / h

#  Plot the function
x = np.linspace(0,2,400)
plt.plot(x,f(x), color='k', label='function')

#  And the first derivative calculated numerically
plt.plot(x,deriv(f,x), color='k', linewidth=0.7, label='numeric')

#  And the symbolic derivative offset slightly to show the shape
#  matches
y = 2*x + 3*np.cos(3*x) + 0.2
plt.plot(x,y, linestyle='dotted', color='k', linewidth=0.7, label='symbolic')

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.legend(loc='best')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
#plt.savefig('numeric.eps', dpi=300)
plt.show()

#  Compare forward and central differences
def cderiv(f,x, h=1e-4):
    return (f(x+h)-f(x-h)) / (2*h)

print("Forward     Exact       Central")
for i in range(10):
    fd = deriv(f,x[i])
    cd = cderiv(f,x[i])
    ex = 2*x[i] + 3*np.cos(3*x[i])
    print("%0.8f  %0.8f  %0.8f" % (fd,ex,cd))

