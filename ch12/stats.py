#
#  file:  stats.py
#
#  Assorted stats-related routines
#
#  RTK, 01-Oct-2023
#  Last update:  07-Oct-2023
#
################################################################

import random
from math import sqrt

def pmean(v, power=1.0):
    """Power mean"""
    s = 0.0
    for t in v:
        s += t**power
    return (s/len(v))**(1/power)

def amean(v, weights=None):
    """Arithmetic mean of a vector"""
    if (weights is None):
        return pmean(v)
    n = sum(weights)
    weights = [weights[i]/n for i in range(len(weights))]
    s = 0.0
    for i in range(len(v)):
        s += weights[i] * v[i]
    return s

def gmean(v):
    """Geometric mean"""
    return pmean(v, power=1e-9)

def hmean(v):
    """Harmonic mean"""
    return pmean(v, power=-1.0)

def median(v):
    """Median of a list"""
    t,n = sorted(v), len(v)
    if (n % 2): return t[n//2]
    return (t[n//2-1] + t[n//2]) / 2

def mode(v):
    """Modes of a list"""
    #  count occurrences
    d = {}
    for t in v:
        if (t in d):
            d[t] += 1
        else:
            d[t] = 1

    #  find the mode, if any
    mx,idx = 1,-1
    for k in d.keys():
        if (d[k] > mx):
            mx = d[k]
            idx = k
    if (mx == 1):
        return []

    #  look for multiple modes
    modes = [idx]
    for k in d.keys():
        if (d[k] == mx) and (k != modes[0]):
            modes.append(k)
    return modes

def std(v):
    """Calculate the unbiased standard deviation"""
    xb = amean(v)
    s = 0.0
    for t in v:
        s += (xb-t)**2
    return sqrt(s / (len(v)-1))

def mad(v):
    """Median absolute deviation"""
    md = median(v)
    m = []
    for t in v:
        m.append(abs(md-t))
    return median(m)

def pearson(x,y):
    """Calculate the Pearson correlation between x and y"""
    mx,my = amean(x), amean(y)
    cov = xd = yd = 0.0
    for i in range(len(x)):
        a,b = x[i]-mx, y[i]-my
        cov += a*b
        xd += a**2
        yd += b**2
    return cov / (sqrt(xd)*sqrt(yd))

try:
    from scipy.stats import spearmanr
    def spearman(x,y):
        """A wrapper on spearmanr"""
        return spearmanr(x,y)[0]
except:
    pass

def Cohen_d(x,y, paired=False):
    """Calculate Cohen's d for independent or paired data"""

    if (not paired):
        m1, s1 = amean(x), std(x)
        m2, s2 = amean(y), std(y)
        n1, n2 = len(x), len(y)
        sp = sqrt(((n1-1)*s1**2+(n2-1)*s2**2)/(n1+n2-2))
        return (m1-m2) / sp
    ds = [x[i]-y[i] for i in range(len(x))]
    return amean(ds) / std(ds)

def t_critical(x1,x2, alpha=0.05, paired=False):
    """Return the critical t value for the CI at alpha"""
    from scipy.stats import t

    if (not paired):
        m1,s1,n1 = amean(x1), std(x1), len(x1)
        m2,s2,n2 = amean(x2), std(x2), len(x2)
        num = (s1**2/n1 + s2**2/n2)**2
        den = s1**4/(n1**2*(n1-1)) + s2**4/(n2**2*(n2-1))
        df = num / den
    else:
        df = len(x1) - 1
    return t.ppf(1-alpha/2, df)


#
#  Examples
#
def Means():
    """An example involving means"""

    #  HM <= GM <= AM
    v = [1,3,2,6,3,9]
    print("HM <= GM <= AM:", v)
    print("    harmonic    %0.5f" % hmean(v))
    print("    geometric   %0.5f" % gmean(v))
    print("    arithmetic  %0.5f" % amean(v))
    print()

    #  Outlier sensitivity
    v = [1,3,2,6,3,100,5,4,7]
    t = [1,3,2,6,3,5,4,7]
    print("Sensitivity:", v)
    print("    harmonic    %8.5f" % hmean(v))
    print("    geometric   %8.5f" % gmean(v))
    print("    arithmetic  %8.5f" % amean(v))
    print("    no outlier  %8.5f" % amean(t))
    print()


def SE():
    """SE as estimate in standard deviation of the means"""
    
    for n in [100, 1000, 10_000, 100_000, 1_000_000, 10_000_000]:
        p = [random.randint(0,99) for i in range(n)]
        se = std(p) / sqrt(n)
        ms = []
        for m in range(10):
            p = [random.randint(0,99) for i in range(n)]
            ms.append(amean(p))
        sd = std(ms)
        print("SE = %0.5f, SD means = %0.5f (%8d)" % (se,sd,n))
    print()


def MAD():
    """Compare std and mad as outliers are added"""
    v = [random.randint(0,99) for i in range(30)]
    a,b = std(v), mad(v)
    print("std: %0.5f, mad: %0.5f" % (a,b))
    v += [127]
    a,b = std(v), mad(v)
    print("std: %0.5f, mad: %0.5f" % (a,b))
    v += [213]
    a,b = std(v), mad(v)
    print("std: %0.5f, mad: %0.5f" % (a,b))


def Quantile():
    """Show quantiles histograms"""
    import numpy as np
    import matplotlib.pylab as plt
    s = np.random.beta(2,10,60_000_000)
    m = s.mean()
    h,x = np.histogram(s, bins=1000)
    h = h / h.sum()
    x = 0.5*(x[1:] + x[:-1])
    q10,q25,q50,q75,q90 = np.quantile(s,[0.1,0.25,0.5,0.75,0.9],interpolation='midpoint')
    plt.plot(x,h, color='k', linewidth=0.7)
    plt.plot([m,m],[0,h.max()], color='k', linestyle='solid')
    plt.plot([q10,q10],[0,h.max()], color='k', linestyle='dotted')
    plt.plot([q25,q25],[0,h.max()], color='k', linestyle='dotted')
    plt.plot([q50,q50],[0,h.max()], color='k', linestyle='dashed')
    plt.plot([q75,q75],[0,h.max()], color='k', linestyle='dotted')
    plt.plot([q90,q90],[0,h.max()], color='k', linestyle='dotted')
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.savefig("quantiles_beta.png", dpi=300)
    plt.savefig("quantiles_beta.eps", dpi=300)
    plt.show()

    s = np.random.normal(size=60_000_000)
    m = s.mean()
    h,x = np.histogram(s, bins=1000)
    h = h / h.sum()
    x = 0.5*(x[1:] + x[:-1])
    q10,q16,q25,q50,q75,q84,q90 = np.quantile(s,[0.1,0.16,0.25,0.5,0.75,0.84,0.9],interpolation='midpoint')
    plt.plot(x,h, color='k', linewidth=0.7)
    plt.plot([m,m],[0,h.max()], color='k', linestyle='solid')
    plt.plot([q10,q10],[0,h.max()], color='k', linestyle='dotted')
    plt.plot([q25,q25],[0,h.max()], color='k', linestyle='dotted')
    plt.plot([q50,q50],[0,h.max()], color='k', linestyle='dashed')
    plt.plot([q75,q75],[0,h.max()], color='k', linestyle='dotted')
    plt.plot([q90,q90],[0,h.max()], color='k', linestyle='dotted')
    plt.plot([q16,q16],[0,h.max()], color='k', linestyle='dashdot')
    plt.plot([q84,q84],[0,h.max()], color='k', linestyle='dashdot')
    plt.xlim((-4,4))
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.savefig("quantiles_normal.png", dpi=300)
    plt.savefig("quantiles_normal.eps", dpi=300)
    plt.show()


def BoxPlot():
    """An example box plot"""
    import numpy as np
    import matplotlib.pylab as plt
    ds = np.zeros((100,3))
    for i in range(100):
        ds[i,:] = [np.random.gamma(1,20), np.random.beta(2,7), np.random.beta(20,10)]
    ds[:,0] = ds[:,0] / ds[:,0].max()
    ds[:,1] = ds[:,1] / ds[:,1].max()
    ds[:,2] = ds[:,2] / ds[:,2].max()
    plt.boxplot(ds)
    plt.xlabel("Variable")
    plt.ylabel("$y$")
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.savefig("boxplot.eps", dpi=300)
    plt.savefig("boxplot.png", dpi=300)
    plt.show()


def Pearson():
    """A Pearson correlation example"""
    import numpy as np
    import matplotlib.pylab as plt
    ds = np.zeros((100,2))

    #  positive correlation
    for i in range(100):
        v = 10*np.random.random()
        ds[i,:] = [v, v**2 + v + 35*np.random.normal()]
    x,y = ds[:,0], ds[:,1]
    x = x / x.max()
    y = y / y.max()
    r = pearson(x,y)
    m,b = np.polyfit(x,y,1)
    plt.plot(x,y, marker='+', linestyle='none', color='k')
    x.sort()
    plt.plot(x, m*x+b, color='k', linewidth=1.2)
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.title("Pearson(x,y) = %0.5f" % r)
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.savefig("pearson_pos.eps", dpi=300)
    plt.show()

    #  negative correlation
    for i in range(100):
        v = 10*np.random.random()
        ds[i,:] = [v, -(v**2 + v + 35*np.random.normal())]
    x,y = ds[:,0], ds[:,1]
    x = x / x.max()
    y = y / y.max()
    r = pearson(x,y)
    m,b = np.polyfit(x,y,1)
    plt.plot(x,y, marker='+', linestyle='none', color='k')
    x.sort()
    plt.plot(x, m*x+b, color='k', linewidth=1.2)
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.title("Pearson(x,y) = %0.5f" % r)
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.savefig("pearson_neg.eps", dpi=300)
    plt.show()

    #  no correlation
    ds = np.random.random(size=(100,2))
    x,y = ds[:,0], ds[:,1]
    r = pearson(x,y)
    m,b = np.polyfit(x,y,1)
    plt.plot(x,y, marker='+', linestyle='none', color='k')
    x.sort()
    plt.plot(x, m*x+b, color='k', linewidth=1.2)
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.title("Pearson(x,y) = %0.5f" % r)
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.savefig("pearson_none.eps", dpi=300)
    plt.show()


def Correlation():
    """Compare the Pearson and Spearman correlation coefficients"""
    import numpy as np
    import matplotlib.pylab as plt
    x = np.linspace(0,3,30)
    y = x**7*np.pi**x
    plt.plot(x,y, color='k', label="$y=x^7\pi^x$")
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.title("Pearson = %0.5f, Spearman = %0.5f" % (pearson(x,y), spearman(x,y)))
    plt.legend(loc='best')
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.savefig("correlations.eps", dpi=300)
    plt.show()

# Anscombe's quartet:

x0 = [10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]
y0 = [8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]

x1 = [10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]
y1 = [9.14,8.14,8.74,8.77,9.26,8.1,6.13,3.1,9.13,7.26,4.74]

x2 = [10.0,8.0,13.0,9.0,11.0,14.0,6.0,4.0,12.0,7.0,5.0]
y2 = [7.46,6.77,12.74,7.11,7.81,8.84,6.08,5.39,8.15,6.42,5.73]

x3 = [8.0,8.0,8.0,8.0,8.0,8.0,8.0,19.0,8.0,8.0,8.0]
y3 = [6.58,5.76,7.71,8.84,8.47,7.04,5.25,12.5,5.56,7.91,6.89]

# end stats.py

