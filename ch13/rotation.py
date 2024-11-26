#  2D rotation example

import numpy as np
import matplotlib.pylab as plt
from PIL import Image

#  image points -- keep every third point
im = np.array(Image.open("emil.png"))
x,y = np.where(1-im.T)
y = 512-y
x = x[::3]
y = y[::3]

#  normal orientation
plt.plot(x,y, marker=',', color='k', linestyle='none')
plt.xlim((0,511))
plt.ylim((0,511))
plt.axis('equal')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig('emil0.eps', dpi=300)
plt.show()

#  rotate 42 degrees
X=[]
Y=[]
t = 42.0*np.pi/180.0
M = np.array([[np.cos(t), -np.sin(t)],[np.sin(t), np.cos(t)]])

for i in range(len(x)):
    v = M @ np.array([[x[i]],[y[i]]])
    X.append(v[0])
    Y.append(v[1])

#  plot
plt.plot(X,Y, marker=',', color='k', linestyle='none')
plt.axis('equal')
plt.tight_layout(pad=0, w_pad=0, h_pad=0)
plt.savefig('emil1.eps', dpi=300)
plt.show()

