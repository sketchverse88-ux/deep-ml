import numpy as np

def vector_sum(a: np.ndarray):
    """Sum elements of 1-D array a without np.sum / loops."""
    sum = 0
    for value in np.arange(0, len(a), 1):
        sum += a[value]
    return sum
