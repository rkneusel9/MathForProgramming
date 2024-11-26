#
#  file: rviewer.py
#
#  Visualize relations
#
#  RTK, 15-Nov-2022  (happy birthday to human #8 billion!)
#  Last update:  15-Nov-2022
#
################################################################

import os
import sys
import matplotlib.pylab as plt
import numpy as np

def InRelation(a,b,R):
    """Return True if a,b in the relation, R"""
    return eval(R)

#
#  main:
#
if (len(sys.argv) == 1):
    print()
    print("rviewer <relation> <xlo> <xhi> <xstep> <ylo> <yhi> <ystep> <plotname>")
    print()
    print("  <relation>       - code for the relation")
    print("  <lo>,<hi>,<step> - x and y axis limits and step size")
    print("  <plotname>       - output plot filename")
    print()
    exit(0)

R = sys.argv[1]
xlo,xhi,xstep = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
ylo,yhi,ystep = float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7])
oname = sys.argv[8]

nx = int((xhi-xlo)/xstep) + 1
ny = int((yhi-ylo)/ystep) + 1
A = np.linspace(xlo,xhi,nx)
B = np.linspace(ylo,yhi,ny)

points = []
for a in A:
    for b in B:
        if (InRelation(a,b,R)):
            points.append((a,b))

if (len(points) == 0):
    print("The relation is empty")
    exit(1)
points = np.array(points)

plt.plot(points[:,0], points[:,1], marker='o', markersize=0.5, linestyle='none', color='k')
plt.xlim((xlo,xhi))
plt.ylim((ylo,yhi))
plt.xlabel("$a$")
plt.ylabel("$b$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig(oname, dpi=300)
plt.show()

