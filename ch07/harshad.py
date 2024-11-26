import matplotlib.pylab as plt
from ntheory import *
N = 800_000
M = 800
x = list(range(1,N,M))
y = [len(Harshad(i))/i for i in x]
plt.plot(x,y,color='k')
plt.ylim((0.097,0.15))
plt.xlabel("$n$")
plt.ylabel("Fraction")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("harshad.png", dpi=300)
plt.savefig("harshad.eps", dpi=300)
plt.close()

