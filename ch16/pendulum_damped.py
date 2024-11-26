#
#  file:  pendulum_damped.py
#
#  Simulate a simple pendulum by transforming the second-order
#  equation of motion into a system of first-order equations.
#
#  This version include a damping term to represent friction
#  and air resistance.
#
#  RTK, 17-Nov-2023
#  Last update: 17-Nov-2023
#
################################################################

import sys
from math import sqrt, sin, cos
import matplotlib.pylab as plt

#  Use RK4 for each equation in the system
def dtheta(omega):
    """dtheta/dt = omega"""
    return omega

def domega(theta, omega):
    """domega/dt = -gamma*omega -(g/l)*sin(theta)"""
    return -gamma*omega - (g/length)*sin(theta)

def RK4(theta, omega, h):
    """A single time step for both coupled equations"""

    k1_theta = dtheta(omega)
    k1_omega = domega(theta, omega)

    k2_theta = dtheta(omega + 0.5*h*k1_omega)
    k2_omega = domega(theta + 0.5*h*k1_theta, omega + 0.5*h*k1_omega)

    k3_theta = dtheta(omega + 0.5*h*k2_omega)
    k3_omega = domega(theta + 0.5*h*k2_theta, omega + 0.5*h*k2_omega)

    k4_theta = dtheta(omega + h*k3_omega)
    k4_omega = domega(theta + h*k3_theta, omega + h*k3_omega)

    theta_new = theta + (h/6)*(k1_theta + 2*k2_theta + 2*k3_theta + k4_theta)
    omega_new = omega + (h/6)*(k1_omega + 2*k2_omega + 2*k3_omega + k4_omega)

    return theta_new, omega_new


if (len(sys.argv) == 1):
    print()
    print("pendulum_damped <length> <theta0> <gamma> <t1> <h> [<outfile>]")
    print()
    print("  <length>  -  pendulum length (m)")
    print("  <theta0>  -  initial angle (degrees)")
    print("  <gamma>   -  damping coefficient (e.g. 0.1-1)")
    print("  <t1>      -  ending time (s)")
    print("  <h>       -  delta-t time (step size)")
    print("  <outfile> -  output file to store theta over time (optional)")
    print()
    exit(0)

length = float(sys.argv[1])
theta0 = float(sys.argv[2]) * (3.14150265/180)  # to radians
gamma  = float(sys.argv[3])
t1     = float(sys.argv[4])
h      = float(sys.argv[5])

#  initial conditions
g = 9.81 # m/s^2
theta, omega, t0 = theta0, 0.0, 0.0  # omega0 = 0, release from rest
thetas, omegas, times = [theta], [omega], [t0]

#  run the simulation
while (times[-1] <= t1):
    theta, omega = RK4(theta, omega, h)
    thetas.append(theta)
    omegas.append(omega)
    times.append(times[-1] + h)

#  save, if requested
if (len(sys.argv) == 7):
    import numpy as np
    xy = np.zeros((len(times),2))
    xy[:,0] = times
    xy[:,1] = thetas
    np.save(sys.argv[6], xy)

#  plot the results showing position and velocity over time
plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.plot(times, thetas, color='k')
plt.title("Angular Position")
plt.ylabel("Angle (rad)")
plt.subplot(2,1,2)
plt.plot(times, omegas, color='k')
plt.title("Angular Velocity")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (rad/s)")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.show()

