#
#  file:  powers.py
#
#  Compare loop and recursive power functions
#
#  RTK, 20-Dec-2022
#  Last update:  30-Dec-2022
#
################################################################

import time
import numpy as np
import matplotlib.pylab as plt

def PowerLoop(b, n):
    """Return b**n using a loop"""

    ans = 1
    while (n > 0):
        ans *= b
        n -= 1
    return ans


def PowerRecursive(b, n):
    """Use recursion to calculate b**n"""

    if (n==0):
        return 1
    elif ((n%2)==0):
        return PowerRecursive(b,n//2)*PowerRecursive(b,n//2)
    else:
        return PowerRecursive(b,(n-1)//2)*b*PowerRecursive(b,(n-1)//2)


if (__name__ == "__main__"):
    loop = []
    recursive = []
    n = [10,100,500,1000,5000,10000,20000,30000,40000,50000,80000,100000,200000,300000,400000,500000]
    for t in n:
        s = time.time(); 
        PowerLoop(4,t);
        loop.append(time.time()-s)
        s = time.time(); 
        PowerRecursive(4,t);
        recursive.append(time.time()-s)

    plt.plot(n,loop, marker='o', fillstyle='none', linewidth=0.7, color='k', label='loop')
    plt.plot(n,recursive, marker='s', fillstyle='none', linewidth=0.7, color='k', label='recursive')
    plt.xlabel("Exponent")
    plt.ylabel("Time (s)")
    plt.legend(loc='best')
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.savefig("powers.png", dpi=300)
    plt.savefig("powers.eps", dpi=300)
    plt.close()

