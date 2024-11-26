#  Law of large numbers
import numpy as np
import matplotlib.pylab as plt

m = []
for n in np.linspace(1,8,30):
    t = np.random.normal(1,1,size=int(10**n))
    m.append(t.mean())

plt.plot(np.linspace(1,8,30), m)
plt.plot([1,8],[1,1], linestyle="--", color='k')
plt.xlabel("Exponent $10^n$")
plt.ylabel("Single sample mean")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("large_numbers.eps", dpi=300)
#plt.show()

