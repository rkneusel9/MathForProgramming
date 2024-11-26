#
#  file:  numeric_example.py
#
#  Compare solutions to y' = -2y, y(0)=3 ==> y(t) = 3e^{-2t}
#  using the exact solution, Euler approximation and
#  Runge-Kutta 4 approximation
#
#  RTK, 17-Nov-2023
#  Last update:  18-Nov-2023
#
################################################################

import sys
from math import exp
import matplotlib.pylab as plt

def dydt(y):
    return -2.0*y

def Euler(y,h):
    return y + dydt(y) * h

def RK4(y,h):
    k1 = dydt(y)
    k2 = dydt(y + 0.5*k1*h)
    k3 = dydt(y + 0.5*k2*h)
    k4 = dydt(y + k3*h)
    return y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)


if (len(sys.argv) == 1 ):
    print()
    print("numeric_example <h> euler|rk4")
    print()
    print("  <h> - timestep (e.g. 0.1)")
    print("  euler|rk4 - which technique to use")
    print()
    exit(0)

h = float(sys.argv[1])
mode = sys.argv[2].lower()

#  initial conditions
y = [3.0]
t = [0.0]

#  iterate
while (t[-1] < 4.0):
    t.append(t[-1] + h)
    if (mode == 'euler'):
        y.append(Euler(y[-1], h))
    else:
        y.append(RK4(y[-1], h))

#  exact solution
et = [t[-1]*(i/500) for i in range(500)]
ex = [3.0*exp(-2.0*i) for i in et]

plt.plot(et, ex, color='k', label='exact')
if (mode == 'euler'):
    plt.plot(t, y, color='k', marker='s', fillstyle='none', linestyle='none', label='Euler')
else:
    plt.plot(t, y, color='k', marker='o', fillstyle='none', linestyle='none', label='RK4')
plt.legend(loc='upper right')
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.tight_layout(pad=0, h_pad=0, w_pad=0)
plt.show()

