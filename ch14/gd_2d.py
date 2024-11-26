#
#  file:  gd_2d.py
#
#  2D example of gradient descent
#
#  RTK, 08-Nov-2023
#  Last update:  08-Nov-2023
#
################################################################

import numpy as np
import matplotlib.pylab as plt

def f(x,y):
    return 6*x**2 + 9*y**2 - 12*x - 14*y + 3

def dx(f,x,y, h=1e-5):
    return (f(x+h,y) - f(x-h,y)) / (2*h)

def dy(f,x,y, h=1e-5):
    return (f(x,y+h) - f(x,y-h)) / (2*h)

#  Gradient descent steps
N = 100
x,y = np.meshgrid(np.linspace(-1,3,N), np.linspace(-1,3,N))
z = f(x,y)
plt.contourf(x,y,z,10, cmap="Greys")
plt.contour(x,y,z,10, colors='k', linewidths=1)
plt.plot([0,0],[-1,3],color='k',linewidth=1)
plt.plot([-1,3],[0,0],color='k',linewidth=1)
plt.plot(1,0.7777778,color='k',marker='+')

#  Step size
eta = 0.02

x = xold = -0.5
y = yold = 2.9
for i in range(12):
    plt.plot([xold,x],[yold,y], marker='o', linestyle='dotted', color='k')
    xold = x
    yold = y
    x = x - eta * dx(f,x,y)
    y = y - eta * dy(f,x,y)

x = xold = 1.5
y = yold = -0.8
for i in range(12):
    plt.plot([xold,x],[yold,y], marker='s', linestyle='dotted', color='k')
    xold = x
    yold = y
    x = x - eta * dx(f,x,y)
    y = y - eta * dy(f,x,y)

x = xold = 2.7
y = yold = 2.3
for i in range(12):
    plt.plot([xold,x],[yold,y], marker='<', linestyle='dotted', color='k')
    xold = x
    yold = y
    x = x - eta * dx(f,x,y)
    y = y - eta * dy(f,x,y)

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("gd_2d_steps.eps", dpi=300)
plt.show()
plt.close()

#  New function
def f(x,y):
    return 6*x**2 + 40*y**2 - 12*x - 30*y + 3

N = 100
x,y = np.meshgrid(np.linspace(-1,3,N), np.linspace(-1,3,N))
z = f(x,y)
plt.contourf(x,y,z,10, cmap="Greys")
plt.contour(x,y,z,10, colors='k', linewidths=1)
plt.plot([0,0],[-1,3],color='k',linewidth=1)
plt.plot([-1,3],[0,0],color='k',linewidth=1)
plt.plot(1,0.375,color='k',marker='+')

x = xold = -0.5
y = yold = 2.3
for i in range(14):
    plt.plot([xold,x],[yold,y], marker='o', linestyle='dotted', color='k')
    xold = x
    yold = y
    x = x - eta * dx(f,x,y)
    y = y - eta * dy(f,x,y)

x = xold = 2.3
y = yold = 2.3
for i in range(14):
    plt.plot([xold,x],[yold,y], marker='s', linestyle='dotted', color='k')
    xold = x
    yold = y
    x = x - (eta/2) * dx(f,x,y)
    y = y - (eta/2) * dy(f,x,y)

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("gd_2d_oscillating.eps", dpi=300)
plt.show()
plt.close()

