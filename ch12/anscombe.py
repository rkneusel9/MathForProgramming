import matplotlib.pylab as plt
import numpy as np
from stats import *

fig, ax = plt.subplots(2,2)

ax[0,0].plot(x0,y0, marker='+', linestyle='none', color='k')
ax[0,1].plot(x1,y1, marker='+', linestyle='none', color='k')
ax[1,0].plot(x2,y2, marker='+', linestyle='none', color='k')
ax[1,1].plot(x3,y3, marker='+', linestyle='none', color='k')

for i in range(2):
    for j in range(2):
        ax[i,j].set_xlim((0,20))
        ax[i,j].set_ylim((0,13))

plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("anscombe.eps", dpi=300)
plt.close()

d = np.zeros((11,4))
d[:,0] = y0
d[:,1] = y1
d[:,2] = y2
d[:,3] = y3

plt.boxplot(d, showmeans=True, labels=['$y_0$','$y_1$','$y_2$','$y_3$'])
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("anscombe_box.eps", dpi=300)
plt.show()

