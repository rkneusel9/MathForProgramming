#  Create frames showing the slope when moving
#  over a curve
#
#  ffmpeg -framerate 8 -i frames/frame_%04d.png -c:v libx264 -vf "fps=8,scale=-1:-1" -pix_fmt yuv420p slopes.mp4
#

import os
import numpy as np
import matplotlib.pylab as plt

def PlotTangent(df,yf,x):
    m = eval(df)
    b = eval(yf) - m*x
    xx = np.linspace(x-0.02, x+0.02, 10)
    yy = m*xx + b
    plt.plot(xx,yy, color='k', linewidth=0.7)
    plt.plot(x,eval(yf), marker="o", fillstyle='none', color='k')

x = np.linspace(0,0.25,100)
yf = "np.sin(8*np.pi*x) + 0.2*np.sin(25*np.pi*x)"
df = "8*np.pi*np.cos(8*np.pi*x) + 0.2*25*np.pi*np.cos(25*np.pi*x)"
y = eval(yf)

os.system("rm -rf frames; mkdir frames")

k, p = 0, 0.01
while (p < 0.24):
    plt.plot(x,y, color='k')
    PlotTangent(df,yf, p)
    plt.xlim((0,0.25))
    plt.ylim((y.min()-0.1*np.abs(y.min()),y.max()+0.1*y.max()))
    plt.xlabel("$x$")
    plt.ylabel("$y$")
    plt.tight_layout(pad=0, w_pad=0, h_pad=0)
    plt.savefig("frames/frame_%04d.png" % k, dpi=100)
    plt.close()
    p += 0.0017
    k += 1

