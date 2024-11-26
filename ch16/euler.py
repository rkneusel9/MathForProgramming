import numpy as np
import matplotlib.pyplot as plt

def pendulum_euler(theta0, omega0, length, g=9.81, dt=0.01, T=10):
    """
    Simulate a nonlinear pendulum using the Euler method.

    Parameters:
    theta0 : float
        Initial angle (in radians).
    omega0 : float
        Initial angular velocity (in radians per second).
    length : float
        Length of the pendulum (in meters).
    g : float, optional
        Acceleration due to gravity (in meters per second squared).
    dt : float, optional
        Time step for the Euler method (in seconds).
    T : float, optional
        Total time of simulation (in seconds).

    Returns:
    t : ndarray
        Array of time points.
    theta : ndarray
        Array of angles over time.
    omega : ndarray
        Array of angular velocities over time.
    """

    # Number of steps
    N = int(T / dt)

    # Arrays to store time, angle, and angular velocity
    t = np.linspace(0, T, N)
    theta = np.zeros(N)
    omega = np.zeros(N)

    # Initial conditions
    theta[0] = theta0
    omega[0] = omega0

    # Euler's method
    for i in range(N - 1):
        theta[i + 1] = theta[i] + omega[i] * dt
        omega[i + 1] = omega[i] - (g / length) * np.sin(theta[i]) * dt

    return t, theta, omega

# Example usage
theta0 = np.pi / 4  # Initial angle of 45 degrees
omega0 = 0.0        # Initial angular velocity
length = 1.0        # Length of the pendulum in meters

t, theta, omega = pendulum_euler(theta0, omega0, length)

# Plotting
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, theta)
plt.title('Pendulum Angle Over Time')
plt.ylabel('Angle (rad)')

plt.subplot(2, 1, 2)
plt.plot(t, omega)
plt.title('Pendulum Angular Velocity Over Time')
plt.ylabel('Angular Velocity (rad/s)')
plt.xlabel('Time (s)')
plt.show()

