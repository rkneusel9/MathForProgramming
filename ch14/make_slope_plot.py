#  Create the slope0.eps plot

import numpy as np
import matplotlib.pylab as plt

def PlotTangent(df,yf,x):
    m = eval(df)
    b = eval(yf) - m*x
    xx = np.linspace(x-0.03, x+0.03, 10)
    yy = m*xx + b
    plt.plot(xx,yy, color='k', linewidth=0.7)
    plt.plot(x,eval(yf), marker="o", fillstyle='none', color='k')

def PlotSecant(df,yf,x):
    m = eval(df)
    b = eval(yf) - m*x + 0.03
    xx = np.linspace(x-0.03, x+0.03, 10)
    yy = m*xx + b
    plt.plot(xx,yy, color='k', linewidth=0.7)

x = np.linspace(0,0.25,600)
yf = "np.sin(8*np.pi*x) + 0.2*np.sin(25*np.pi*x)"
df = "8*np.pi*np.cos(8*np.pi*x) + 0.2*25*np.pi*np.cos(25*np.pi*x)"
y = eval(yf)

#  tangent lines
plt.plot(x,y, color='k')
PlotTangent(df,yf, 0.0624)
PlotTangent(df,yf, 0.1382)
PlotTangent(df,yf, 0.2082)
PlotTangent(df,yf, 0.2349)
plt.xlim((0,0.25))
plt.ylim((y.min()-0.1*np.abs(y.min()),y.max()+0.1*y.max()))
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("slope0.eps", dpi=300)
plt.close()

#  secant line
plt.plot(x,y, color='k')
PlotTangent(df,yf, 0.0624)
PlotSecant(df,yf, 0.0624)
x = 0.05224; y = eval(yf)
plt.plot([x,x],[y,y], marker="o", color='k')
x = 0.07415; y = eval(yf)
plt.plot([x,x],[y,y], marker="o", color='k')
plt.xlim((0.02,0.1))
plt.ylim((0.65,0.95))
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig("slope1.eps", dpi=300)
plt.show()

