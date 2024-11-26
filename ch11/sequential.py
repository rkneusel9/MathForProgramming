#  Sample an arbitrary discrete distribution via sequential search
import numpy as np

def sequential(v):
    """Sequential search"""
    probs = v / v.sum()
    k = 0
    u = np.random.random()
    while u > 0:
        u -= probs[k]
        k += 1
    return k-1

