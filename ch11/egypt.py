#  Simulate the Thebes, Tanis, Abydos example
from random import random

c, n = 0, 1_000_000
for i in range(n):
    r = random()
    if (r < 0.75):
        if (random() < 0.02): c += 1
    elif (r < (0.75+0.23)):
        if (random() < 0.03): c += 1
    else:
        if (random() < 0.10): c += 1

print("probability of priestly class = %0.5f" % (c/n))

