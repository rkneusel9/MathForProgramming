#
#  file:  mystic.py
#
#  Generate complete graph images, i.e., "mystic roses"
#
#  RTK, 24-Jun-2024
#  Last update:  24-Jun-2024
#
################################################################

import sys
import numpy as np
import matplotlib.pylab as plt

if (len(sys.argv) == 1):
    print()
    print("mystic <n> [<outfile>]")
    print()
    print("  <n>       - number of points (min 2)")
    print("  <outfile> - optional output file base name (e.g. rose_4)")
    print()
    exit(0)

N = int(sys.argv[1])
oname = "" if (len(sys.argv) < 3) else sys.argv[2]

x = []
y = []

#  place N points equidistant on the unit circle
dt = 2*np.pi / N
for i in range(N):
    x.append(np.cos(i*dt))
    y.append(np.sin(i*dt))

#  for each point, draw a segment to every other point
fig, ax = plt.subplots()
ax.axis('equal')
for i in range(N):
    for j in range(N):
        if (i == j):
            continue
        plt.plot([x[i],x[j]],[y[i],y[j]], marker='o', linewidth=0.7, color='k')

#  generate and save the plot
plt.axis('off')
plt.axis('off')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

if (oname != ""):
    plt.savefig(oname+".png", dpi=500, bbox_inches='tight', pad_inches=0)
    plt.savefig(oname+".eps", dpi=300, bbox_inches='tight', pad_inches=0)

plt.show()


