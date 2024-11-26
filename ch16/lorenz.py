#  The Lorenz attractor
import sys
import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm

# Lorenz's original values:
s,r,b = 10, 28, 8/3

def derivatives(p):
    """Calculate the derivatives"""
    x,y,z = p
    xd = s*(y-x)
    yd = r*x - y - x*z
    zd = x*y - b*z
    return np.array([xd,yd,zd])

def rk4(p,h):
    """RK4 update"""
    k1 = derivatives(p)
    k2 = derivatives(p + 0.5*k1*h)
    k3 = derivatives(p + 0.5*k2*h)
    k4 = derivatives(p + k3*h)
    return (h/6)*(k1 + 2*k2 + 2*k3 + k4)

if (len(sys.argv) == 1):
    print()
    print("lorenz <x0,y0,z0> <n> <dt> <cmap>")
    print()
    print("  x0,y0,z0 - initial position, no spaces (e.g. 0.0,1.05,1.0)")
    print("  <n>    - number of steps (e.g. 25000)")
    print("  <h>    - timestep (e.g. 0.0025)")
    print("  <cmap> - Matplotlib color map name (e.g. 'inferno')")
    print("  <mode> - euler|rk4 (numeric mode)")
    print()
    exit(0)

x0,y0,z0 = [float(i) for i in sys.argv[1].split(",")]
n, h = int(sys.argv[2]), float(sys.argv[3])
cmap = cm.get_cmap(sys.argv[4])
mode = sys.argv[5].lower()

#  points and initial position
p = np.zeros((n,3))
c = [cmap(0)]
p[0] = (x0, y0, z0)

#  run the simulation
for i in range(1,n):
    if (mode == 'euler'):
        p[i] = p[i-1] + derivatives(p[i-1]) * h
    else:
        p[i] = p[i-1] + rk4(p[i-1],h)
    c.append(cmap(int(256*i/n)))

#  Print final 10 trajectory points
print(p[-10:,:])

#  Plot the attractor
ax = plt.figure().add_subplot(projection='3d')
ax.scatter(p[:,0],p[:,1],p[:,2], c=c, marker='.', s=1)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
plt.show()

