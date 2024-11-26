#
#  file: equivalence.py
#
#  Print the elements of the relation (assuming an equivalence relation)
#
#  RTK, 19-Nov
#  Last update:  19-Nov-2022
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
    print("equivalence <relation> <xlo> <xhi> <xstep> <ylo> <yhi> <ystep>")
    print()
    print("  <relation>       - code for the relation")
    print("  <lo>,<hi>,<step> - x and y axis limits and step size")
    print()
    exit(0)

R = sys.argv[1]
xlo,xhi,xstep = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
ylo,yhi,ystep = float(sys.argv[5]), float(sys.argv[6]), float(sys.argv[7])

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

for i in range(len(points)):
    print("(%0.4f,%0.4f), " % (points[i,0],points[i,1]), end="")
    if (i!=0) and (i%18==0):
        print()
print()

