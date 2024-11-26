#  Simulate selecting a car from Crazy Ernie's lot
from random import randint

#  41 red Fords, 33 red Teslas, 37 blue Fords, 10 blue Teslas
cars = [0]*41 + [1]*33 + [2]*37 + [3]*10

c, n = 0, 100_000
for i in range(n):
    k = randint(0,120)          #  pick a vehicle
    if (cars[k] != 3): c += 1   #  red or a Ford

print("Probability of red or Ford = %0.5f" % (c/n))

