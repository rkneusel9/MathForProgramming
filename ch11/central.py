#  Central limit theorem
import numpy as np
import matplotlib.pylab as plt

def sequential(v):
    """Sequential search"""
    probs = v / v.sum()
    k = 0
    u = np.random.random()
    while u > 0:
        u -= probs[k]
        k += 1
    return k-1

#  Beta(5,2) plot
#n = np.random.beta(5,2, size=100_000_000)
#h,x = np.histogram(n, bins=1000)
#h = h / h.sum()
#x = 0.5*(x[1:] + x[:-1])
#plt.plot(x,h, color='k')
#plt.xlabel("$x$")
#plt.ylabel("$y$")
#plt.tight_layout(pad=0, w_pad=0, h_pad=0)
#plt.savefig("beta.eps", dpi=300)
#plt.savefig("beta.png", dpi=300)

#  Example 1 -- an arbitrary discrete distribution to estimate the
#               distribution mean
dm = (2*0 + 4*1 + 6*2 + 1*3 + 9*4) / (2+4+6+1+9)

print("Example 1 -- mean of an arbitrary discrete distribution:")
print()
print("                             CLT               LLN")
v = np.array([2,4,6,1,9])
m = []
for i in range(3):
    n = np.array([sequential(v) for i in range(40)])
    m.append(n.mean())
m = np.array(m)
t = np.array([sequential(v) for i in range(40*3)])
d0= np.abs(m.mean()-dm)
d1= np.abs(t.mean()-dm)
print("Mean of the means (n=  3) is %0.4f (%0.4f), %0.4f (%0.4f)" % (m.mean(), d0, t.mean(), d1), d0<d1)

m = []
for i in range(5):
    n = np.array([sequential(v) for i in range(40)])
    m.append(n.mean())
m = np.array(m)
t = np.array([sequential(v) for i in range(40*5)])
d0= np.abs(m.mean()-dm)
d1= np.abs(t.mean()-dm)
print("Mean of the means (n=  5) is %0.4f (%0.4f), %0.4f (%0.4f)" % (m.mean(), d0, t.mean(), d1), d0<d1)

m = []
for i in range(10):
    n = np.array([sequential(v) for i in range(40)])
    m.append(n.mean())
m = np.array(m)
t = np.array([sequential(v) for i in range(40*10)])
d0= np.abs(m.mean()-dm)
d1= np.abs(t.mean()-dm)
print("Mean of the means (n= 10) is %0.4f (%0.4f), %0.4f (%0.4f)" % (m.mean(), d0, t.mean(), d1), d0<d1)

m = []
for i in range(50):
    n = np.array([sequential(v) for i in range(40)])
    m.append(n.mean())
m = np.array(m)
t = np.array([sequential(v) for i in range(40*50)])
d0= np.abs(m.mean()-dm)
d1= np.abs(t.mean()-dm)
print("Mean of the means (n= 50) is %0.4f (%0.4f), %0.4f (%0.4f)" % (m.mean(), d0, t.mean(), d1), d0<d1)

m = []
for i in range(100):
    n = np.array([sequential(v) for i in range(40)])
    m.append(n.mean())
m = np.array(m)
t = np.array([sequential(v) for i in range(40*100)])
d0= np.abs(m.mean()-dm)
d1= np.abs(t.mean()-dm)
print("Mean of the means (n=100) is %0.4f (%0.4f), %0.4f (%0.4f)" % (m.mean(), d0, t.mean(), d1), d0<d1)

print("Actual distribution mean  is %0.4f" % dm)
print()

#  Example 2 -- a continuous distribution
print("Example 2 -- mean of a continuous distribution:")
print()

z = 5 / (5 + 2)  # exact mean of Beta(5,2)

for M in [60, 600, 6000]:
    m = np.zeros(M)
    for i in range(M):
        t = np.random.beta(5,2,size=40)
        m[i] = t.mean()
    print("Beta(5,2) mean of the means = %0.7f  (n=%d)" % (m.mean(),M))
    h,x = np.histogram(m, bins=40)
    h = h / h.sum()
    plt.bar(x[:-1]+0.5*(x[1]-x[0]), h, width=0.8*(x[1]-x[0]), color='k', fill=False)
    plt.plot([z,z], [0,1.05*h.max()], color='k', linestyle='dashed')
    plt.xlabel("Mean")
    plt.ylabel("Probability")
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.savefig("central_limit%d.eps" % M, dpi=300)
    plt.savefig("central_limit%d.png" % M, dpi=300)
    plt.close()

print("Beta(5,2) true mean         = %0.7f" % z)
print()

#  Example 3 -- the law of large numbers
N = [10,50,100,150,200,250,300,350,400,450,500]
for i in range(1,21):
    N += [1000*i]
m = []
for n in N:
    t = np.random.beta(5,2, size=n)
    m.append(t.mean())

plt.plot(N,m, color='k')
plt.plot([N[0],N[-1]],[z,z], color='k', linestyle='dashed', linewidth=0.7)
plt.xlabel("Number of samples")
plt.ylabel("Sample mean")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("large_numbers.png", dpi=300)
plt.savefig("large_numbers.eps", dpi=300)
plt.close()

