# plots of key continuous distributions
import numpy as np
import matplotlib.pylab as plt

N = 100_000_000
B = 100
x = np.arange(B)/B

#  uniform
t = np.random.random(N)
u = np.histogram(t, bins=B)[0]
u = u / u.sum()

#  normal
t = np.random.normal(0, 1, size=N)
n = np.histogram(t, bins=B)[0]
n = n / n.sum()

#  gamma
t = np.random.gamma(5.0, size=N)
g = np.histogram(t, bins=B)[0]
g = g / g.sum()

#  beta
t = np.random.beta(5,2, size=N)
b = np.histogram(t, bins=B)[0]
b = b / b.sum()

plt.plot(x,u,color='k',linestyle='solid', label='uniform')
plt.plot(x,n,color='k',linestyle='dotted', label='normal')
plt.plot(x,g,color='k',linestyle='dashed', label='gamma')
plt.plot(x,b,color='k',linestyle='dashdot', label='beta')
plt.xlabel("$x$")
plt.ylabel("Probability")
plt.legend(loc='best')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
#plt.savefig("continuous.eps", dpi=300)
plt.show()
plt.close()

