#  Simulate the Border Collie example
from random import randint

dogs = [1]*4 + [0]*92
c, n = 0, 100_000

for i in range(n):
    x,y,z = [dogs[randint(0,95)] for i in range(3)]
    if (x+y+z): continue
    c += 1

print("Probability that none are Border Collies = %0.5f" % (c/n))

