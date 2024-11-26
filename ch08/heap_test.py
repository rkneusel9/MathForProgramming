#  Time to generate permutations using heap.c
#  to compare with 1977 Sedgewick TABLE 1

import numpy as np
import time
import os

timing = []

for n in range(1,16):
    s = time.time()
    e = os.system("heap %d" % n)
    timing.append(time.time()-s)

np.save("heap_test.npy", np.array(timing))

#  1             1
#  2             2
#  3             6
#  4            24
#  5           120
#  6           720
#  7          5040
#  8         40320
#  9        362880
# 10       3628800
# 11      39916800
# 12     479001600
# 13    6227020800
# 14   87178291200
# 15 1307674368000


