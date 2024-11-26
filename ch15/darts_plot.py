#  Make the darts.eps plot
import numpy as np
import matplotlib.pylab as plt
x = np.linspace(1,3,1000)
y = x**2*np.exp(x)
ym = 3**2*np.exp(3)

np.random.seed(8675309)
n = 100
xp = 1.0 + 2.0*np.random.random(n)
yp = 0.0 + ym*np.random.random(n)

plt.plot(x,y, color='k')
plt.plot(xp,yp, color='k', marker='+', linestyle='none')
plt.plot([1,3],[ym,ym], color='k', linewidth=0.7)
plt.plot([1,3],[0,0], color='k', linewidth=0.7)
plt.plot([1,1],[0,ym], color='k', linewidth=0.7)
plt.plot([3,3],[0,ym], color='k', linewidth=0.7)
plt.xlim((0.9,3.1))
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig('darts.eps', dpi=300)
plt.show()

