# Logistic map
import sys
import numpy as np
import matplotlib.pylab as plt

r = 3.9

def A(x):
    return r*x*(1-x)

def B(x):
    return r*x - r*x*x

def C(x):
    return x*(r - r*x)

def D(x):
    return r*x - r*x**2

N = int(sys.argv[1])
x = [[0.25, 0.25, 0.25, 0.25]]

for i in range(N):
    if (i < 10) or (i > N-11):
        print("%6d: %0.16f  %0.16f  %0.16f  %0.16f" % (i,x[-1][0],x[-1][1],x[-1][2],x[-1][3]))
    x.append([A(x[-1][0]),B(x[-1][1]),C(x[-1][2]),D(x[-1][3])])

z = np.array(x)

plt.subplot(2,2,1)
plt.plot(z[0:100,0], color='k', marker='o', fillstyle='none', linewidth=0.6)
plt.xlim((50,100))
plt.subplot(2,2,2)
plt.plot(z[0:100,1], color='k', marker='s', fillstyle='none', linewidth=0.6)
plt.xlim((50,100))
plt.subplot(2,2,3)
plt.plot(z[0:100,2], color='k', marker='d', fillstyle='none', linewidth=0.6)
plt.xlim((50,100))
plt.subplot(2,2,4)
plt.plot(z[0:100,3], color='k', marker='^', fillstyle='none', linewidth=0.6)
plt.xlim((50,100))
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("logistic_plot0.png", dpi=300)
plt.savefig("logistic_plot0.eps", dpi=300)
plt.show()
plt.close()

plt.plot(np.arange(100),z[0:100,0], color='k', marker='o', fillstyle='none', linestyle='none')
plt.plot(np.arange(100),z[0:100,3], color='k', marker='^', fillstyle='none', linestyle='none')
plt.plot([54.5,54.5],[0,1],linestyle='dashed',color='k')
plt.show()



