#
#  file:  logistic_cycle.py
#
#  Generate the bifurcation plot by varying r
#
#  RTK, 26-Dec-2022
#  Last update:  26-Dec-2022
#
################################################################

import numpy as np
import matplotlib.pylab as plt

#                       1   2            4            8   chaos
for k,r in enumerate([2.4,3.3,3.5,3.5644072661,3.9]):
    X = []; R = []
    x = 0.01
    for i in range(1500):
        x = r*x*(1-x)
    for i in range(60):
        X.append(x)
        R.append(i)
        x = r*x*(1-x)

    plt.figure(figsize=(14,3))
    plt.plot(R,X, marker='o', linewidth=0.7, color='k')
    plt.xlabel("Iteration")
    plt.ylabel("$x$")
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.savefig("logistic_cycle_%d.png" % k, dpi=300)
    plt.savefig("logistic_cycle_%d.eps" % k, dpi=300)
    plt.close()

