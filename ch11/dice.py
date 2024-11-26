#  Simulate rolling two dice

from random import randint

N = 1_000_000
rolls = [randint(1,6)+randint(1,6) for i in range(N)]
counts = [0]*11
for roll in rolls:
    counts[roll-2] += 1

print([count/N for count in counts])

