import numpy as np
import matplotlib.pylab as plt
x = np.linspace(-2,8,1000)
y = np.abs(x-3)
plt.plot(x,y, color='k')
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("abs.eps", dpi=300)
plt.show()

