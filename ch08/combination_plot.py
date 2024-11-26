import matplotlib.pylab as plt
from combinatorics import *
import sys

n = int(sys.argv[1])
r = range(1,n)
m = [nCr(n,r) for r in r]
plt.bar(r,m, fill=False, color='k', width=0.9)
plt.xlabel("$r$")
plt.ylabel("$C(%d,r)$" % n)
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("combination_plot.png", dpi=300)
plt.savefig("combination_plot.eps", dpi=300)
plt.close()

