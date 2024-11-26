#
#  file:  logistic_map.py
#
#  Generate the bifurcation plot by varying r
#
#  RTK, 26-Dec-2022
#  Last update:  26-Dec-2022
#
################################################################

import numpy as np
import matplotlib.pylab as plt

X = []
R = []

for r in np.linspace(2.2,3.99,10000):
    x = 0.01
    for i in range(1500):
        x = r*x*(1-x)
    for i in range(600):
        X.append(x)
        R.append(r)
        x = r*x*(1-x)

plt.plot(R,X, marker=',', linestyle='none', color='k')
plt.plot([2.4,2.4],[0,1], linewidth=0.7, color='k')
plt.plot([3.3,3.3],[0,1], linewidth=0.7, color='k')
plt.plot([3.5,3.5],[0,1], linewidth=0.7, color='k')
plt.plot([3.5644072661,3.5644072661],[0,1], linewidth=0.7, color='k')
plt.plot([3.9,3.9],[0,1], linewidth=0.7, color='k')
plt.xlabel("$r$")
plt.ylabel("$x$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("logistic_map_plot.png", dpi=600)
plt.show()

