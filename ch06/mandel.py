#
#  file: mandel.py
#
#  Generate a Mandelbrot set image more efficiently
#
#  time python3 -W ignore mandel.py -2 0.6 0.001 -1.1 1.1 0.001 400 mandel.png
#
#  RTK, 06-Feb-2022
#  Last update:  26-Dec-2022
#
################################################################

import sys
import numpy as np
from matplotlib import cm
from PIL import Image


################################################################
#  Mandelbrot
#
def Mandelbrot(x0,x1,xinc, y0,y1,yinc, nmax):
    """Generate the image"""

    x = x0
    i = 0
    while (x <= x1):
        y = y0
        j = 0
        while (y <= y1):
            y += yinc
            j += 1
        x += xinc
        i += 1

    c = np.zeros((j,i), dtype="complex64")
    z = np.zeros((j,i), dtype="complex64")
    img = 255*np.ones((j,i), dtype="uint8")

    x = x0
    i = 0
    while (x <= x1):
        y = y0
        j = 0
        while (y <= y1):
            c[j,i] = complex(x,y)
            y += yinc
            j += 1
        x += xinc
        i += 1
    
    for k in range(nmax):
        z = z*z + c

    img[np.where(np.abs(z) < 2)] = 0
    return img


if (len(sys.argv) == 1):
    print()
    print("mandelbrot <x0> <x1> <xinc> <y0> <y1> <yinc> <n> <output>")
    print()
    print("  <x0,x1,xinc> - low, high, inc in x")
    print("  <y0,y1,yinc> - low, high, inc in y")
    print("  <n>          - max iterations per point")
    print("  <output>     - output image name")
    print()
    exit(0)

x0   = float(sys.argv[1])
x1   = float(sys.argv[2])
xinc = float(sys.argv[3])

y0   = float(sys.argv[4])
y1   = float(sys.argv[5])
yinc = float(sys.argv[6])

nmax = int(sys.argv[7])
oname= sys.argv[8]

img = Mandelbrot(x0,x1,xinc, y0,y1,yinc, nmax)
Image.fromarray(img).save(oname)

