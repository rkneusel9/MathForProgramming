#
#  file:  dual_test.py
#
#  Generate f(x) and f'(x)
#
#  RTK, 16-Feb-2022
#  Last update:  09-Nov-2023
#
################################################################

from dual import *
import numpy as np
import matplotlib.pylab as plt

N = 200
x = np.linspace(-10,10,N)
y,yp = np.zeros(N), np.zeros(N)
for i in range(N):
    u = Dual(x[i],1)
    v = u*u.sin() + u*u.cos()
    y[i], yp[i] = v.a, v.b

plt.plot(x,y, color='k', label='f(x)')
plt.plot(x,yp,color='k', linestyle='dashed', label="f'(x)")
plt.legend(loc='upper right')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("dual_plot_1.eps", dpi=300)
plt.show()

x = np.linspace(-5,5,N)
y,yp = np.zeros(N), np.zeros(N)
for i in range(N):
    v = (Dual(-0.5,0)*Dual(x[i],1)**2).exp()
    y[i], yp[i] = v.a, v.b

plt.plot(x,y, color='k', label='f(x)')
plt.plot(x,yp,color='k', linestyle='dashed', label="f'(x)")
plt.legend(loc='upper right')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("dual_plot_2.eps", dpi=300)
plt.show()

x = np.linspace(-10,10,N)
y,yp = np.zeros(N), np.zeros(N)
for i in range(N):
    v = (Dual(1,0) + (Dual(-1,0)*Dual(x[i],1)).exp())**(-1)
    y[i], yp[i] = v.a, v.b

plt.plot(x,y, color='k', label='f(x)')
plt.plot(x,yp,color='k', linestyle='dashed', label="f'(x)")
plt.legend(loc='upper right')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("dual_plot_3.eps", dpi=300)
plt.show()

x = np.linspace(0,10,N)
y,yp = np.zeros(N), np.zeros(N)
for i in range(N):
    u = Dual(x[i],1)
    v = Dual(2,0)*(Dual(3,0)*u).sin() + Dual(20,0)*(Dual(-0.5,0)*(u-Dual(8,0))**2/Dual(0.6,0)).exp()
    y[i], yp[i] = v.a, v.b

plt.plot(x,y, color='k', label='f(x)')
plt.plot(x,yp,color='k', linestyle='dashed', label="f'(x)")
plt.legend(loc='upper right')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("dual_plot_4.eps", dpi=300)
plt.show()

