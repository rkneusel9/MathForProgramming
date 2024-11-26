#  Simulate selecting marbles from a bag
from random import randint
red, blue = 11, 7
n = 1_000_000

#  Independent events -- return the marble to the bag
bag = [0]*blue + [1]*red
c = 0
for i in range(n):
    k = randint(0, len(bag)-1)
    if (bag[k] == 0): continue
    k = randint(0, len(bag)-1)
    if (bag[k] == 1): c += 1
print("Probability of reds (independent): %0.5f" % (c/n))

#  Dependent events -- pick a red, then pick red again
c = 0
for i in range(n):
    bag = [0]*blue + [1]*red
    k = randint(0, len(bag)-1)
    if (bag[k] == 0): continue
    bag.pop(k)
    k = randint(0, len(bag)-1)
    if (bag[k] == 1): c += 1
print("Probability of reds (dependent)  : %0.5f" % (c/n))

