#
#  file: projectile.py
#
#  Projectile motion with air resistance
#
#  RTK, 17-Nov-2023
#  Last update:  22-Nov-2023
#
################################################################

import sys
import numpy as np
import matplotlib.pylab as plt

def RK4(state, h, k):
    """Runge-Kutta 4 step"""

    def derivatives(state, k):
        x, y, vx, vy = state
        dxdt = vx
        dydt = vy
        vmag = np.sqrt(vx**2 + vy**2)
        dvxdt = -k*vmag*vx
        dvydt = -9.81 - k*vmag*vy
        return np.array([dxdt, dydt, dvxdt, dvydt])

    k1 = derivatives(state, k)
    k2 = derivatives(state + 0.5*k1*h, k)
    k3 = derivatives(state + 0.5*k2*h, k)
    k4 = derivatives(state + k3*h, k)
    return state + (h/6)*(k1 + 2*k2 + 2*k3 + k4)


if (len(sys.argv) == 1):
    print()
    print("projectile <angle> <muzzle> <drag> <h>")
    print()
    print("  <angle>  - launch angle relative to x-axis (degrees)")
    print("  <muzzle> - muzzle velocity (e.g. 100 m/s)")
    print("  <drag>   - k drag coefficient (e.g. 0.01 for 10 cm cannonball)")
    print("  <h>      - time step (e.g. 0.05 s)")
    print()
    exit(0)

vangle = float(sys.argv[1]) * (np.pi/180)  # radians
vmag = float(sys.argv[2])
k = float(sys.argv[3])
h = float(sys.argv[4])

#  initial state
vx = vmag*np.cos(vangle)
vy = vmag*np.sin(vangle)
state = np.array([0.0, 0.0, vx, vy])

x,y = [state[0]],[state[1]]

while (True):
    state = RK4(state, h, k) 
    if (state[1] <= 0):
        print("Hit the ground (x = %0.2f meters)" % state[0])
        break
    x.append(state[0])
    y.append(state[1])

if (len(sys.argv) == 5):
    plt.plot(x,y, marker='+', linestyle='none', color='k')
    plt.xlabel("Range (m)")
    plt.ylabel("Altitude (m)")
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.show()

