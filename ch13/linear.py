#  Apply a given 2D linear transformation

import sys
import numpy as np
import matplotlib.pylab as plt
from PIL import Image

if (len(sys.argv) == 1):
    print()
    print("linear <matrix> [output]")
    print()
    print("  <matrix> -- transformation matrix (no spaces or in quotes)")
    print("  <output> -- output image file (optional)")
    print()
    exit(0)

M = eval("np.array("+sys.argv[1]+")")

#  image points -- keep every third point
im = np.array(Image.open("emil.png"))
x,y = np.where(1-im.T)
y = 512-y
x = x[::3]
y = y[::3]

#  apply the transformation
X=[]
Y=[]
for i in range(len(x)):
    v = M @ np.array([[x[i]],[y[i]]])
    X.append(v[0])
    Y.append(v[1])

#  plot the result
plt.plot(X,Y, marker=',', color='k', linestyle='none')
plt.axis('equal')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
if (len(sys.argv) == 3):
    plt.savefig(sys.argv[2], dpi=300)
plt.show()

