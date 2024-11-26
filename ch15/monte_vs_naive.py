#  Compare mean calculated area as a function of the number of samples
import os
import numpy as np

def run(name, n):
    cmd = "python3 %s.py 'x**2' 10 12 %d >/tmp/tmp" % (name,n)
    os.system(cmd)
    return float(open("/tmp/tmp").read()[:-1].split()[-1])

M = 10
N = [100,1000,5000,10_000,30_000,60_000,120_000,240_000,480_000,960_000]

for n in N:
    a = []
    for j in range(M):
        a.append(run("monte",n))
    monte,mse = np.array(a).mean(), np.array(a).std(ddof=1) / np.sqrt(M)
    a = []
    for j in range(M):
        a.append(run("naive",n))
    naive,nse = np.array(a).mean(), np.array(a).std(ddof=1) / np.sqrt(M)
    print("%6d:  %0.5f (%0.5f)  %0.5f (%0.5f)" % (n,naive,nse,monte,mse))

