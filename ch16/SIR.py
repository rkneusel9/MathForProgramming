#
#  file: SIR.py
#
#  The SIR model for epidemics
#
#  RTK, 18-Nov-2023
#  Last update:  24-Nov-2023
#
################################################################

import sys
import numpy as np
import matplotlib.pylab as plt

def RK4(state, beta, gamma, N, h=1):
    """Runge-Kutta 4 step"""

    def derivatives(state, beta, gamma, N):
        S,I,R = state
        dSdt = -beta*S*I/N
        dIdt = beta*S*I/N - gamma*I
        dRdt = gamma*I
        return np.array([dSdt, dIdt, dRdt])

    k1 = derivatives(state, beta, gamma, N)
    k2 = derivatives(state + 0.5*k1, beta, gamma, N)
    k3 = derivatives(state + 0.5*k2, beta, gamma, N)
    k4 = derivatives(state + k3, beta, gamma, N)
    return state + (h/6)*(k1 + 2*k2 + 2*k3 + k4)


if (len(sys.argv) == 1):
    print()
    print("SIR <beta> <gamma> <fS> <fI> <N> <days> [<outfile>]")
    print()
    print("  <beta>    - SIR beta parameter (e.g. 0.25)")
    print("  <gamma>   - SIR gamma parameter (e.g. 0.15)")
    print("  <fS>      - fraction initially susceptible, e.g. 0.95")
    print("  <fI>      - fraction initially infected, e.g. 0.05")
    print("  <N>       - population size")
    print("  <days>    - number of timesteps (e.g. 100 days)")
    print("  <outfile> - if present, suppress plot and stores rates in a NumPy file")
    print()
    exit(0)

beta  = float(sys.argv[1])
gamma = float(sys.argv[2])
fS    = float(sys.argv[3])
fI    = float(sys.argv[4])
N     = int(sys.argv[5])
ts    = int(sys.argv[6])

#  initial state
S0 = int(fS*N)
I0 = int(fI*N)
R0 = 0
state = np.array([S0,I0,R0])
S,I,R,t = [S0], [I0], [R0], [0]

for i in range(ts):
    state = RK4(state, beta, gamma, N)
    S.append(state[0])
    I.append(state[1])
    R.append(state[2])
    t.append(t[-1] + 1)

if (len(sys.argv) == 7):
    plt.plot(t,S, color='k', linestyle='solid', label='susceptible')
    plt.plot(t,I, color='k', linestyle='dashed', label='infected')
    plt.plot(t,R, color='k', linestyle='dotted', label='recovered')
    plt.legend(loc='best')
    plt.xlabel("Time")
    plt.ylabel("People")
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.show()
else:
    d = np.zeros((len(t),4))
    d[:,0] = t
    d[:,1] = S
    d[:,2] = I
    d[:,3] = R
    np.save(sys.argv[7], d)

