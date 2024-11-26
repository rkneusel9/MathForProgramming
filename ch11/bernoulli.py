#  Generate Bernoulli samples
import numpy as np

def bernoulli(p, size=1):
    """Samples from a Bernoulli distribution"""
    n = np.random.random(size)
    return (n < p).astype("uint8")

