#  Plot SIR results for several diseases
import os
import numpy as np
import matplotlib.pylab as plt

#  Measles
os.system("python3 SIR.py 1.25 0.0833 0.98 0.02 10000 100 /tmp/ttt.npy")
measles = np.load("/tmp/ttt.npy")

#  Rubella
os.system("python3 SIR.py 0.46 0.0714 0.98 0.02 10000 100 /tmp/ttt.npy")
rubella = np.load("/tmp/ttt.npy")

#  COVID
os.system("python3 SIR.py 0.28 0.1111 0.98 0.02 10000 100 /tmp/ttt.npy")
covid = np.load("/tmp/ttt.npy")

#  S plot
plt.plot(measles[:,0], measles[:,1], color='k', linestyle='solid', label='Measles')
plt.plot(rubella[:,0], rubella[:,1], color='k', linestyle='dashed', label='Rubella')
plt.plot(covid[:,0], covid[:,1], color='k', linestyle='dotted', label='COVID-19')
plt.xlabel("Days")
plt.ylabel("People")
plt.title("Susceptible")
plt.legend(loc='best')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig('SIR_plot_S.eps', dpi=300)
plt.show()

#  I plot
plt.plot(measles[:,0], measles[:,2], color='k', linestyle='solid', label='Measles')
plt.plot(rubella[:,0], rubella[:,2], color='k', linestyle='dashed', label='Rubella')
plt.plot(covid[:,0], covid[:,2], color='k', linestyle='dotted', label='COVID-19')
plt.xlabel("Days")
plt.ylabel("People")
plt.title("Infected")
plt.legend(loc='best')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig('SIR_plot_I.eps', dpi=300)
plt.show()

#  R plot
plt.plot(measles[:,0], measles[:,3], color='k', linestyle='solid', label='Measles')
plt.plot(rubella[:,0], rubella[:,3], color='k', linestyle='dashed', label='Rubella')
plt.plot(covid[:,0], covid[:,3], color='k', linestyle='dotted', label='COVID-19')
plt.xlabel("Days")
plt.ylabel("People")
plt.title("Recovered")
plt.legend(loc='best')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig('SIR_plot_R.eps', dpi=300)
plt.show()

