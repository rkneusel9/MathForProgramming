import numpy as np
from sympy import isprime
from scipy.stats import ttest_1samp
import matplotlib.pylab as plt
import random

s = []
for i in range(1000):
    v = (np.argsort(np.random.random(1000))+1)[:188]
    p = 0
    for t in v:
        if (isprime(t)):
            p += 1
    s.append(p/188)

s = np.array(s)
print()
print("Fraction prime: %0.7f +/- %0.7f" % (s.mean(), s.std(ddof=1)/np.sqrt(len(s))))
t,p = ttest_1samp(s,0.35106)
print("(t=%0.6f, p=%0.8f)" % (t,p))
print()

h,x = np.histogram(s, bins=60)
h = h / h.sum()
x = 0.5*(x[:-1]+x[1:])
plt.bar(x,h, color='k', width=0.8*(x[1]-x[0]))
plt.plot([0.35106,0.35106],[0,s.max()], linewidth=1.2, color='k')
plt.xlabel("Fraction prime")
plt.ylabel("Fraction")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("collatz_fraction_prime.png", dpi=300)
plt.savefig("collatz_fraction_prime.eps", dpi=300)
plt.show()

