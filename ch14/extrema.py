import numpy as np
import matplotlib.pylab as plt

def f(x):
    return x**3 -3*x**2-3*x+4

x = np.linspace(-2.5,4.5,100)
y = f(x) 
r0,r1 = 1-np.sqrt(2), 1+np.sqrt(2)

plt.plot(x,y, color='k')
plt.plot([r0-1,r0+1],[f(r0),f(r0)], color='k', linewidth=0.7)
plt.plot([r0,r0],[f(r0)-3,f(r0)+3], color='k', linewidth=0.7)
plt.plot([r1-1,r1+1],[f(r1),f(r1)], color='k', linewidth=0.7)
plt.plot([r1,r1],[f(r1)-3,f(r1)+3], color='k', linewidth=0.7)
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("extrema.eps", dpi=300)
plt.show()

