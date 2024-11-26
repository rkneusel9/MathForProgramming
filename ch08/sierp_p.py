import sys
import numpy as np
import matplotlib.pylab as plt
from combinatorics import *

p = int(sys.argv[1])
x = []
y = []
N = 256
for n in range(N):
    for r in range(n+1):
        off = (N-n) // 2
        if ((nCr(n,r) % p) != 0):
            x.append(r+off)
            y.append(n)

ax = plt.gca()
ax.invert_yaxis()
ax.set_aspect('equal')
plt.plot(x,y, marker='.', markersize=0.8, linestyle='none', color='k')
plt.xlabel("$r$")
plt.ylabel("$n$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("sierp_p_%d.png" % p, dpi=300)
plt.savefig("sierp_p_%d.eps" % p, dpi=300)
plt.show()

