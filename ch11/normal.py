#  Use the Box-Muller transform to sample from 
#  a normal distribution
import numpy as np

def norm(mu=0, sigma=1):
    if (norm.state):
        norm.state = False
        return sigma*norm.z2 + mu
    else:
        u1,u2 = np.random.random(2)
        m = np.sqrt(-2.0*np.log(u1))
        z1 = m*np.cos(2*np.pi*u2)
        norm.z2 = m*np.sin(2*np.pi*u2)
        norm.state = True
        return sigma*z1 + mu
norm.state = False

def normal(mu=0, sigma=1, size=1):
    """Return samples from N(mu,sigma)"""
    return np.array([norm(mu,sigma) for i in range(size)])


def main():
    """An example"""
    import matplotlib.pylab as plt

    mu, sigma, n = 5.0, 2.0, 10_000

    #  plot PDF
    x = np.linspace(-3,15,1000)
    y = (1/np.sqrt(2*np.pi*2))*np.exp(-0.5*((x-mu)**2/sigma**2))
    y = y / y.max()  # force y.max = 1
    plt.plot(x,y, color='k', linewidth=0.7)

    #  simulate with samples
    s = normal(mu, sigma, n)
    h,x = np.histogram(s, bins=60)
    x = 0.5*(x[1:] + x[:-1])
    h = h / h.sum()
    h = h / h.max() # force h.max = 1
    plt.bar(x,h, width=0.8*(x[1]-x[0]), fill=False, color='k')

    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.savefig("normal.eps", dpi=300)
    plt.show()

if (__name__ == "__main__"):
    main()

