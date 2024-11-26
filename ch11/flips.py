#  Test von Neumann's de-bias trick

from random import random

def Flip(p=0.7):
    return "H" if (random() < p) else "T"

#  show bias
flips = [Flip(0.9) for i in range(100_000)]
print("biased  : H= %d, T= %d" % (flips.count('H'), flips.count('T')))

#  de-bias
raw = [(Flip(0.9), Flip(0.9)) for i in range(100_000)]
flips = [i[0] for i in raw if i[0] != i[1]]
print("unbiased: H= %d, T= %d" % (flips.count('H'), flips.count('T')))

